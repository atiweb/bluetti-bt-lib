import struct

from . import DeviceField, FieldName


class BoolFieldNonZero(DeviceField):
    """Bool field where any non-zero value means True.
    
    Used for devices like AC2P where ac_output_on register (2011) returns:
    - 0x0001 (1) = ON
    - 0x0003 (3) = OFF but still non-zero
    
    Some Bluetti devices return non-standard boolean values like 3 for ON state.
    This field treats any non-zero value as True.
    """
    def __init__(self, name: FieldName, address: int):
        super().__init__(name, address, 1)

    def parse(self, data: bytes) -> bool:
        num = struct.unpack("!H", data)[0]
        # Any non-zero value means ON
        return num != 0
