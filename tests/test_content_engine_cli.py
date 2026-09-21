"""Focused regression tests for side-effect-free content-engine CLI help."""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from tools.nova_content_engine.cli import main


class ContentEngineCliHelpTests(unittest.TestCase):
    def test_help_exits_successfully_without_discovery_or_blueprint(self) -> None:
        output = io.StringIO()

        with (
            patch("tools.nova_content_engine.cli.resolve_topic") as resolve_topic,
            patch("tools.nova_content_engine.cli.TopicDiscovery.discover") as discover,
            patch("tools.nova_content_engine.cli.BlueprintManager.load_or_build") as load_blueprint,
            redirect_stdout(output),
        ):
            exit_code = main(["--help"])

        self.assertEqual(exit_code, 0)
        self.assertIn("usage:", output.getvalue().lower())
        self.assertIn("--topic", output.getvalue())
        resolve_topic.assert_not_called()
        discover.assert_not_called()
        load_blueprint.assert_not_called()


if __name__ == "__main__":
    unittest.main()
