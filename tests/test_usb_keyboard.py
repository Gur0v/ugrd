from pathlib import Path
from unittest import TestCase, main


class TestUsbKeyboard(TestCase):
    def test_usb_keyboard_drivers_are_included(self):
        root = Path(__file__).parents[1] / "src/ugrd/kmod"
        input_source = (root / "input.py").read_text()
        usb_config = (root / "usb.toml").read_text()
        self.assertIn("input_dev.resolve().parts", input_source)
        self.assertIn("'usbhid'", usb_config)
        self.assertIn("'hid_generic'", usb_config)


if __name__ == "__main__":
    main()
