from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "research-code-complexity" / "scripts" / "validate_profile.py"
SCHEMA = ROOT / "skills" / "research-code-complexity" / "assets" / "research-code-complexity.schema.json"
EXAMPLE = ROOT / "skills" / "research-code-complexity" / "assets" / "research-code-complexity.example.yaml"

spec = importlib.util.spec_from_file_location("validate_profile", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class ProfileValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.schema = module.load_schema(SCHEMA)

    def validate_text(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "profile.yaml"
            path.write_text(text, encoding="utf-8")
            return module.validate_profile(path, self.schema)

    def test_generic_example_is_valid(self) -> None:
        self.assertEqual([], module.validate_profile(EXAMPLE, self.schema))

    def test_partial_profile_is_valid(self) -> None:
        self.assertEqual([], self.validate_text('schema_version: "1.0"\n'))

    def test_unknown_key_is_rejected_with_path(self) -> None:
        errors = self.validate_text('schema_version: "1.0"\nproject:\n  lifecyle: exploratory\n')
        self.assertEqual(1, len(errors))
        self.assertIn("$.project", errors[0])
        self.assertIn("lifecyle", errors[0])

    def test_malformed_value_has_actionable_path(self) -> None:
        errors = self.validate_text('schema_version: "1.0"\ncomplexity:\n  review_threshold: 0\n')
        self.assertEqual(1, len(errors))
        self.assertIn("$.complexity.review_threshold", errors[0])

    def test_malformed_yaml_is_rejected(self) -> None:
        errors = self.validate_text('schema_version: "1.0"\nproject: [\n')
        self.assertEqual(1, len(errors))
        self.assertIn("invalid YAML", errors[0])

    def test_x_prefixed_extensions_are_forward_compatible(self) -> None:
        errors = self.validate_text(
            'schema_version: "1.0"\nx-lab-policy:\n  review_owner: domain-team\nproject:\n  x-domain-stage: pilot\n'
        )
        self.assertEqual([], errors)


if __name__ == "__main__":
    unittest.main()
