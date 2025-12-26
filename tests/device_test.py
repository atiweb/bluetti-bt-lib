import unittest

from bluetti_bt_lib import BluettiDevice
from bluetti_bt_lib.fields import DecimalField, FieldName, UIntField


class TestDevice(unittest.TestCase):
    def test_get_polling_registers(self):
        device = BluettiDevice(
            [
                DecimalField(FieldName.DC_INPUT_CURRENT, 1214, 1),
                UIntField(FieldName.AC_OUTPUT_POWER, 142),
                UIntField(FieldName.DC_INPUT_POWER, 144),
                UIntField(FieldName.DC_OUTPUT_POWER, 140),
                DecimalField(FieldName.DC_INPUT_VOLTAGE, 1213, 1),
                UIntField(FieldName.AC_INPUT_POWER, 146),
                DecimalField(FieldName.AC_INPUT_FREQUENCY, 1300, 1),
            ]
        )

        registers = device.get_polling_registers()

        self.assertEqual(len(registers), 3)
        self.assertEqual(registers[0].starting_address, 140)
        self.assertEqual(registers[-1].starting_address, 1300)
