"""Exercise workflow helper outputs and failure effects in temporary workspaces."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
TASK_BRIEF = ROOT / "skills/subagent-driven-development/scripts/task-brief"
START_SERVER = ROOT / "skills/brainstorming/scripts/start-server.sh"
FIND_POLLUTER = ROOT / "skills/systematic-debugging/find-polluter.sh"


class WorkspaceTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="workflow-helper-test-")
        self.addCleanup(self.temporary.cleanup)
        self.work = Path(self.temporary.name)

    def run_helper(self, script, *args, env=None, timeout=5):
        return subprocess.run(
            ["bash", str(script), *map(str, args)],
            cwd=self.work, env=env, capture_output=True, text=True, timeout=timeout,
        )


class TaskBriefTest(WorkspaceTest):
    def setUp(self):
        super().setUp()
        self.plan = self.work / "implementation-plan.md"
        self.plan.write_text(
            "# Plan\n\n### Task 1: First\nFirst criterion.\n"
            "\n### Task 2: Second\nSecond criterion.\n"
        )
        self.output = self.work / "brief.md"

    def test_missing_task_preserves_existing_brief(self):
        self.output.write_text("Existing brief with ownership and evidence.\n")
        result = self.run_helper(TASK_BRIEF, self.plan, 99, self.output)
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertEqual(self.output.read_text(), "Existing brief with ownership and evidence.\n")
        self.assertEqual(list(self.work.glob(".task-brief.*")), [])

    def test_missing_task_does_not_publish_an_empty_brief(self):
        result = self.run_helper(TASK_BRIEF, self.plan, 99, self.output)
        self.assertEqual(result.returncode, 3, result.stderr)
        self.assertFalse(self.output.exists())

    def test_invalid_task_number_preserves_output(self):
        self.output.write_text("Retained result.\n")
        for value in ("0", "-1", "../other", "1.*"):
            with self.subTest(value=value):
                result = self.run_helper(TASK_BRIEF, self.plan, value, self.output)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertEqual(self.output.read_text(), "Retained result.\n")

    def test_success_replaces_only_the_selected_brief(self):
        self.output.write_text("Old brief.\n")
        result = self.run_helper(TASK_BRIEF, self.plan, 2, self.output)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.output.read_text(), "### Task 2: Second\nSecond criterion.\n")

    def test_output_directory_is_rejected_without_publishing_a_file(self):
        destination = self.work / "reports"
        destination.mkdir()
        result = self.run_helper(TASK_BRIEF, self.plan, 1, destination)
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertEqual(list(destination.iterdir()), [])
        self.assertEqual(list(self.work.glob(".task-brief.*")), [])

    def test_literal_headings_inside_fences_do_not_change_task_boundaries(self):
        for opening, closing in (
            ("~~~markdown", "~~~"),
            ("   ~~~~markdown", "   ~~~~~"),
            ("```markdown", "```"),
            ("````markdown", "````"),
        ):
            with self.subTest(opening=opening):
                literal = (
                    f"{opening}\n### Task 2: Literal example\n"
                    "```\n### Task 3: Another literal example\n"
                    f"{closing}\n"
                ) if opening.startswith("````") else (
                    f"{opening}\n### Task 2: Literal example\n{closing}\n"
                )
                first = "### Task 1: Real first task\n" + literal + "First acceptance criterion.\n\n"
                second = "### Task 2: Real second task\nSecond acceptance criterion.\n\n"
                self.plan.write_text(
                    "# Plan\n\n" + first + second + "### Task 3: Real third task\nThird criterion.\n"
                )
                for number, expected in ((1, first), (2, second)):
                    result = self.run_helper(TASK_BRIEF, self.plan, number, self.output)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertEqual(self.output.read_text(), expected)

    def test_default_output_stays_in_the_ignored_plan_workspace(self):
        subprocess.run(["git", "init", "--quiet"], cwd=self.work, check=True)
        result = self.run_helper(TASK_BRIEF, self.plan, 1)
        self.assertEqual(result.returncode, 0, result.stderr)
        expected = self.work / ".kryptonite/sdd/implementation-plan/task-1-brief.md"
        self.assertIn("First criterion.", expected.read_text())
        ignored = subprocess.run(
            ["git", "check-ignore", str(expected)], cwd=self.work, capture_output=True,
        )
        self.assertEqual(ignored.returncode, 0)


class ServerOptionTest(WorkspaceTest):
    def setUp(self):
        super().setUp()
        commands = tempfile.TemporaryDirectory(prefix="server-option-command-test-")
        self.addCleanup(commands.cleanup)
        node = Path(commands.name) / "node"
        node.write_text("#!/bin/sh\nexit 1\n")
        node.chmod(0o755)
        # Argument rejection must never start a real server, even if regressed.
        self.environment = dict(os.environ, PATH=commands.name + os.pathsep + os.environ["PATH"])

    def test_missing_empty_or_flag_values_fail_before_starting(self):
        for option in ("--project-dir", "--host", "--url-host", "--idle-timeout-minutes"):
            for rest in ((), ("",), ("--foreground",)):
                with self.subTest(option=option, rest=rest):
                    result = self.run_helper(START_SERVER, option, *rest, env=self.environment)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(option, result.stdout)
                    self.assertEqual(list(self.work.iterdir()), [])

    def test_valid_option_values_are_consumed(self):
        for option, value in (
            ("--project-dir", str(self.work / "project with spaces")),
            ("--host", "127.0.0.1"),
            ("--url-host", "localhost"),
            ("--idle-timeout-minutes", "1"),
        ):
            with self.subTest(option=option):
                result = self.run_helper(START_SERVER, option, value, "--unknown", env=self.environment)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("Unknown argument: --unknown", result.stdout)
                self.assertEqual(list(self.work.iterdir()), [])


class PollutionInvestigationTest(WorkspaceTest):
    def setUp(self):
        super().setUp()
        (self.work / "src").mkdir()
        (self.work / "bin").mkdir()
        npm = self.work / "bin/npm"
        npm.write_text(
            '#!/bin/sh\nprintf "%s\\n" "$2" >> "$PROBE_CALL_LOG"\n'
            'case "$2" in\n'
            '  *polluter*) touch "$PROBE_POLLUTION"; exit 9 ;;\n'
            '  *failed*) exit 9 ;;\n'
            'esac\nexit 0\n'
        )
        npm.chmod(0o755)
        self.calls = self.work / "calls.log"
        self.pollution = self.work / "unexpected-state"
        self.environment = dict(os.environ, PATH=str(self.work / "bin") + os.pathsep + os.environ["PATH"])
        self.environment.update(PROBE_CALL_LOG=str(self.calls), PROBE_POLLUTION=str(self.pollution))

    def investigate(self):
        return self.run_helper(FIND_POLLUTER, self.pollution, "src/**/*.test.js", env=self.environment)

    def test_successful_clean_run_returns_success(self):
        (self.work / "src/clean.test.js").touch()
        result = self.investigate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("No polluter found", result.stdout)
        self.assertEqual(self.calls.read_text().splitlines(), ["./src/clean.test.js"])

    def test_test_file_with_spaces_is_passed_as_one_argument(self):
        (self.work / "src/clean case.test.js").touch()
        result = self.investigate()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.calls.read_text().splitlines(), ["./src/clean case.test.js"])

    def test_failed_run_reports_incomplete_verification(self):
        (self.work / "src/failed.test.js").touch()
        result = self.investigate()
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertIn("9", result.stderr)
        self.assertNotIn("all tests clean", result.stdout)

    def test_no_matching_tests_is_incomplete(self):
        result = self.investigate()
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertFalse(self.calls.exists())

    def test_existing_pollution_prevents_a_clean_verdict(self):
        (self.work / "src/clean.test.js").touch()
        self.pollution.touch()
        result = self.investigate()
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertFalse(self.calls.exists())

    def test_failed_polluter_is_still_identified(self):
        (self.work / "src/polluter.test.js").touch()
        result = self.investigate()
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("FOUND POLLUTER", result.stdout)
        self.assertTrue(self.pollution.exists())


if __name__ == "__main__":
    unittest.main()
