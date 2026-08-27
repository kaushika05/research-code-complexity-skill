from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "validate_repository.py"
spec = importlib.util.spec_from_file_location("validate_repository", SCRIPT)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(module)


class RepositoryValidationTests(unittest.TestCase):
    def test_release_repository_is_consistent(self) -> None:
        self.assertEqual(0, module.main())


if __name__ == "__main__":
    unittest.main()
