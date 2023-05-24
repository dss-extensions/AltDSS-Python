'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2022 Paulo Meira

Copyright (c) 2018-2022 DSS-Extensions contributors
'''
from ._cffi_api_util import Base
from ._types import Float64Array

class IDSSimComs(Base):
    __slots__ = []

    def BusVoltage(self, Index: int) -> Float64Array:
        self.CheckForError(self._lib.DSSimComs_BusVoltage_GR(Index))
        return self._get_float64_gr_array()

    def BusVoltagepu(self, Index: int) -> Float64Array:
        self.CheckForError(self._lib.DSSimComs_BusVoltagepu_GR(Index))
        return self._get_float64_gr_array()


