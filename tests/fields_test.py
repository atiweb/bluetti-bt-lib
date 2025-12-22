import unittest

from bluetti_bt_lib.enums import EcoMode
from bluetti_bt_lib.fields import (
    DecimalField,
    DeviceField,
    FieldName,
    IntField,
    SelectField,
    UIntField,
)


class TestDeviceFields(unittest.TestCase):
    def test_device_field(self):
        field = DeviceField(FieldName.BATTERY_SOC, 102, 2)

        with self.assertRaises(NotImplementedError):
            field.parse(bytes(1))

        self.assertFalse(field.is_writeable())

        self.assertFalse(field.allowed_write_type(1))
        self.assertFalse(field.allowed_write_type(1.0))
        self.assertFalse(field.allowed_write_type("on"))

        for value in range(-149, 149):
            self.assertTrue(field.in_range(value))

    def test_int(self):
        field = IntField(FieldName.BATTERY_SOC, 102, 0, 100)
        self.assertTrue(field.in_range(0))
        self.assertTrue(field.in_range(49))
        self.assertTrue(field.in_range(100))
        self.assertFalse(field.in_range(-1))
        self.assertFalse(field.in_range(101))

    def test_uint(self):
        field = UIntField(FieldName.BATTERY_SOC, 102, 1, 0, 100)
        self.assertTrue(field.in_range(0))
        self.assertTrue(field.in_range(49))
        self.assertTrue(field.in_range(100))
        self.assertFalse(field.in_range(-1))
        self.assertFalse(field.in_range(101))

    def test_decimal(self):
        field = DecimalField(FieldName.BATTERY_SOC, 102, 1, 1, 0, 100)
        self.assertTrue(field.in_range(0))
        self.assertTrue(field.in_range(49))
        self.assertTrue(field.in_range(100))
        self.assertFalse(field.in_range(-1))
        self.assertFalse(field.in_range(101))

    def test_select(self):
        field = SelectField(FieldName.CTRL_ECO_TIME_MODE, 3064, EcoMode)
        self.assertEqual(field.parse(bytes([0, 4])), EcoMode.HOURS4)
