from pathlib import Path
from unittest import TestCase, main


class TestPosixShell(TestCase):
    def test_generated_shell_uses_posix_syntax(self):
        source = Path(__file__).parents[1] / "src/ugrd"
        self.assertNotIn('grep -qE "(^|\\\\s)', (source / "base/base.py").read_text())
        self.assertNotIn('grep -qE "(^|\\\\s)', (source / "base/cmdline.py").read_text())
        self.assertNotIn("read -p", (source / "fs/btrfs.py").read_text())


if __name__ == "__main__":
    main()
