# Copyright (c) 2021-2024 Paulo Meira
# Copyright (c) 2021-2024 DSS-Extensions contributors
from __future__ import annotations
from typing import Union, List, AnyStr, Optional, Iterator, TYPE_CHECKING
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy
from .common import LIST_LIKE
from .PCElement import PCElementBatchMixin, PCElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .LoadShape import LoadShape
from .Spectrum import Spectrum as SpectrumObj

class IndMach012(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'IndMach012'
    _cls_idx = 39
    _cls_int_idx = {
        1,
        6,
        17,
        21,
        24,
    }
    _cls_float_idx = {
        3,
        4,
        5,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        23,
    }
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'kw': 4,
        'pf': 5,
        'conn': 6,
        'kva': 7,
        'h': 8,
        'd': 9,
        'purs': 10,
        'puxs': 11,
        'purr': 12,
        'puxr': 13,
        'puxm': 14,
        'slip': 15,
        'maxslip': 16,
        'slipoption': 17,
        'yearly': 18,
        'daily': 19,
        'duty': 20,
        'debugtrace': 21,
        'spectrum': 22,
        'basefreq': 23,
        'enabled': 24,
        'like': 25,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[IndMach012Properties]) -> IndMach012:
        """
        Edit this IndMach012.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_Phases(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int
    """
    Number of Phases, this Induction Machine.  

    DSS property name: `Phases`, DSS property index: 1.
    """

    def _get_Bus1(self) -> str:
        return self._get_prop_string(2)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str
    """
    Bus to which the Induction Machine is connected.  May include specific node specification.

    DSS property name: `Bus1`, DSS property index: 2.
    """

    def _get_kV(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kV = property(_get_kV, _set_kV) # type: float
    """
    Nominal rated (1.0 per unit) voltage, kV. For 2- and 3-phase machines, specify phase-phase kV. Otherwise, specify actual kV across each branch of the machine. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

    DSS property name: `kV`, DSS property index: 3.
    """

    def _get_kW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    kW = property(_get_kW, _set_kW) # type: float
    """
    Shaft Power, kW, for the Induction Machine.  A positive value denotes power for a load. 
    Negative value denotes an induction generator. 

    DSS property name: `kW`, DSS property index: 4.
    """

    def _get_PF(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_PF(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    PF = property(_get_PF, _set_PF) # type: float
    """
    [Read Only] Present power factor for the machine. 

    DSS property name: `PF`, DSS property index: 5.
    """

    def _get_Conn(self) -> enums.Connection:
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 6))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(6, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection
    """
    Connection of stator: Delta or Wye. Default is Delta.

    DSS property name: `Conn`, DSS property index: 6.
    """

    def _get_Conn_str(self) -> str:
        return self._get_prop_string(6)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str
    """
    Connection of stator: Delta or Wye. Default is Delta.

    DSS property name: `Conn`, DSS property index: 6.
    """

    def _get_kVA(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_kVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: float
    """
    Rated kVA for the machine.

    DSS property name: `kVA`, DSS property index: 7.
    """

    def _get_H(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_H(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    H = property(_get_H, _set_H) # type: float
    """
    Per unit mass constant of the machine.  MW-sec/MVA.  Default is 1.0.

    DSS property name: `H`, DSS property index: 8.
    """

    def _get_D(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_D(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    D = property(_get_D, _set_D) # type: float
    """
    Damping constant.  Usual range is 0 to 4. Default is 1.0.  Adjust to get damping in Dynamics mode,

    DSS property name: `D`, DSS property index: 9.
    """

    def _get_puRs(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_puRs(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    puRs = property(_get_puRs, _set_puRs) # type: float
    """
    Per unit stator resistance. Default is 0.0053.

    DSS property name: `puRs`, DSS property index: 10.
    """

    def _get_puXs(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_puXs(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    puXs = property(_get_puXs, _set_puXs) # type: float
    """
    Per unit stator leakage reactance. Default is 0.106.

    DSS property name: `puXs`, DSS property index: 11.
    """

    def _get_puRr(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_puRr(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    puRr = property(_get_puRr, _set_puRr) # type: float
    """
    Per unit rotor  resistance. Default is 0.007.

    DSS property name: `puRr`, DSS property index: 12.
    """

    def _get_puXr(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_puXr(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    puXr = property(_get_puXr, _set_puXr) # type: float
    """
    Per unit rotor leakage reactance. Default is 0.12.

    DSS property name: `puXr`, DSS property index: 13.
    """

    def _get_puXm(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_puXm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    puXm = property(_get_puXm, _set_puXm) # type: float
    """
    Per unit magnetizing reactance.Default is 4.0.

    DSS property name: `puXm`, DSS property index: 14.
    """

    def _get_Slip(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_Slip(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    Slip = property(_get_Slip, _set_Slip) # type: float
    """
    Initial slip value. Default is 0.007

    DSS property name: `Slip`, DSS property index: 15.
    """

    def _get_MaxSlip(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_MaxSlip(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    MaxSlip = property(_get_MaxSlip, _set_MaxSlip) # type: float
    """
    Max slip value to allow. Default is 0.1. Set this before setting slip.

    DSS property name: `MaxSlip`, DSS property index: 16.
    """

    def _get_SlipOption(self) -> enums.IndMach012SlipOption:
        return enums.IndMach012SlipOption(self._lib.Obj_GetInt32(self._ptr, 17))

    def _set_SlipOption(self, value: Union[AnyStr, int, enums.IndMach012SlipOption], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(17, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 17, value, flags)

    SlipOption = property(_get_SlipOption, _set_SlipOption) # type: enums.IndMach012SlipOption
    """
    Option for slip model. One of {fixedslip | variableslip*  }

    DSS property name: `SlipOption`, DSS property index: 17.
    """

    def _get_SlipOption_str(self) -> str:
        return self._get_prop_string(17)

    def _set_SlipOption_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_SlipOption(value, flags)

    SlipOption_str = property(_get_SlipOption_str, _set_SlipOption_str) # type: str
    """
    Option for slip model. One of {fixedslip | variableslip*  }

    DSS property name: `SlipOption`, DSS property index: 17.
    """

    def _get_Yearly_str(self) -> str:
        return self._get_prop_string(18)

    def _set_Yearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(18, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: str
    """
    LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

    DSS property name: `Yearly`, DSS property index: 18.
    """

    def _get_Yearly(self) -> LoadShape:
        return self._get_obj(18, LoadShape)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(18, value, flags)
            return

        self._set_string_o(18, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: LoadShape
    """
    LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

    DSS property name: `Yearly`, DSS property index: 18.
    """

    def _get_Daily_str(self) -> str:
        return self._get_prop_string(19)

    def _set_Daily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(19, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: str
    """
    LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

    DSS property name: `Daily`, DSS property index: 19.
    """

    def _get_Daily(self) -> LoadShape:
        return self._get_obj(19, LoadShape)

    def _set_Daily(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(19, value, flags)
            return

        self._set_string_o(19, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: LoadShape
    """
    LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

    DSS property name: `Daily`, DSS property index: 19.
    """

    def _get_Duty_str(self) -> str:
        return self._get_prop_string(20)

    def _set_Duty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(20, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: str
    """
    LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

    DSS property name: `Duty`, DSS property index: 20.
    """

    def _get_Duty(self) -> LoadShape:
        return self._get_obj(20, LoadShape)

    def _set_Duty(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(20, value, flags)
            return

        self._set_string_o(20, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: LoadShape
    """
    LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

    DSS property name: `Duty`, DSS property index: 20.
    """

    def _get_DebugTrace(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 21) != 0

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 21, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: bool
    """
    [Yes | No*] Write DebugTrace file.

    DSS property name: `DebugTrace`, DSS property index: 21.
    """

    def _get_Spectrum_str(self) -> str:
        return self._get_prop_string(22)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(22, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str
    """
    Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

    DSS property name: `Spectrum`, DSS property index: 22.
    """

    def _get_Spectrum(self) -> SpectrumObj:
        return self._get_obj(22, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(22, value, flags)
            return

        self._set_string_o(22, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj
    """
    Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

    DSS property name: `Spectrum`, DSS property index: 22.
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 23.
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 24) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 24, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 24.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 25.
        """
        self._set_string_o(25, value)


class IndMach012Properties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kV: float
    kW: float
    PF: float
    Conn: Union[AnyStr, int, enums.Connection]
    kVA: float
    H: float
    D: float
    puRs: float
    puXs: float
    puRr: float
    puXr: float
    puXm: float
    Slip: float
    MaxSlip: float
    SlipOption: Union[AnyStr, int, enums.IndMach012SlipOption]
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    DebugTrace: bool
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class IndMach012Batch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'IndMach012'
    _obj_cls = IndMach012
    _cls_idx = 39
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[IndMach012BatchProperties]) -> IndMach012Batch:
        """
        Edit this IndMach012 batch.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context for objects in the batch.
        It can be seen as a shortcut to manually setting each property, or a Pythonic
        analogous (but extended) to the DSS `BatchEdit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the objects.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    if TYPE_CHECKING:
        def __iter__(self) -> Iterator[IndMach012]:
            yield from DSSBatch.__iter__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy
    """
    Number of Phases, this Induction Machine.  

    DSS property name: `Phases`, DSS property index: 1.
    """

    def _get_Bus1(self) -> List[str]:
        return self._get_batch_str_prop(2)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]
    """
    Bus to which the Induction Machine is connected.  May include specific node specification.

    DSS property name: `Bus1`, DSS property index: 2.
    """

    def _get_kV(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kV = property(_get_kV, _set_kV) # type: BatchFloat64ArrayProxy
    """
    Nominal rated (1.0 per unit) voltage, kV. For 2- and 3-phase machines, specify phase-phase kV. Otherwise, specify actual kV across each branch of the machine. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

    DSS property name: `kV`, DSS property index: 3.
    """

    def _get_kW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    kW = property(_get_kW, _set_kW) # type: BatchFloat64ArrayProxy
    """
    Shaft Power, kW, for the Induction Machine.  A positive value denotes power for a load. 
    Negative value denotes an induction generator. 

    DSS property name: `kW`, DSS property index: 4.
    """

    def _get_PF(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_PF(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    PF = property(_get_PF, _set_PF) # type: BatchFloat64ArrayProxy
    """
    [Read Only] Present power factor for the machine. 

    DSS property name: `PF`, DSS property index: 5.
    """

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 6)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value, flags)
            return

        self._set_batch_int32_array(6, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy
    """
    Connection of stator: Delta or Wye. Default is Delta.

    DSS property name: `Conn`, DSS property index: 6.
    """

    def _get_Conn_str(self) -> List[str]:
        return self._get_batch_str_prop(6)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]
    """
    Connection of stator: Delta or Wye. Default is Delta.

    DSS property name: `Conn`, DSS property index: 6.
    """

    def _get_kVA(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 7)

    def _set_kVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: BatchFloat64ArrayProxy
    """
    Rated kVA for the machine.

    DSS property name: `kVA`, DSS property index: 7.
    """

    def _get_H(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 8)

    def _set_H(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    H = property(_get_H, _set_H) # type: BatchFloat64ArrayProxy
    """
    Per unit mass constant of the machine.  MW-sec/MVA.  Default is 1.0.

    DSS property name: `H`, DSS property index: 8.
    """

    def _get_D(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 9)

    def _set_D(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    D = property(_get_D, _set_D) # type: BatchFloat64ArrayProxy
    """
    Damping constant.  Usual range is 0 to 4. Default is 1.0.  Adjust to get damping in Dynamics mode,

    DSS property name: `D`, DSS property index: 9.
    """

    def _get_puRs(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 10)

    def _set_puRs(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    puRs = property(_get_puRs, _set_puRs) # type: BatchFloat64ArrayProxy
    """
    Per unit stator resistance. Default is 0.0053.

    DSS property name: `puRs`, DSS property index: 10.
    """

    def _get_puXs(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_puXs(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    puXs = property(_get_puXs, _set_puXs) # type: BatchFloat64ArrayProxy
    """
    Per unit stator leakage reactance. Default is 0.106.

    DSS property name: `puXs`, DSS property index: 11.
    """

    def _get_puRr(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 12)

    def _set_puRr(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    puRr = property(_get_puRr, _set_puRr) # type: BatchFloat64ArrayProxy
    """
    Per unit rotor  resistance. Default is 0.007.

    DSS property name: `puRr`, DSS property index: 12.
    """

    def _get_puXr(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_puXr(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    puXr = property(_get_puXr, _set_puXr) # type: BatchFloat64ArrayProxy
    """
    Per unit rotor leakage reactance. Default is 0.12.

    DSS property name: `puXr`, DSS property index: 13.
    """

    def _get_puXm(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 14)

    def _set_puXm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    puXm = property(_get_puXm, _set_puXm) # type: BatchFloat64ArrayProxy
    """
    Per unit magnetizing reactance.Default is 4.0.

    DSS property name: `puXm`, DSS property index: 14.
    """

    def _get_Slip(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 15)

    def _set_Slip(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    Slip = property(_get_Slip, _set_Slip) # type: BatchFloat64ArrayProxy
    """
    Initial slip value. Default is 0.007

    DSS property name: `Slip`, DSS property index: 15.
    """

    def _get_MaxSlip(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 16)

    def _set_MaxSlip(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    MaxSlip = property(_get_MaxSlip, _set_MaxSlip) # type: BatchFloat64ArrayProxy
    """
    Max slip value to allow. Default is 0.1. Set this before setting slip.

    DSS property name: `MaxSlip`, DSS property index: 16.
    """

    def _get_SlipOption(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 17)

    def _set_SlipOption(self, value: Union[AnyStr, int, enums.IndMach012SlipOption, List[AnyStr], List[int], List[enums.IndMach012SlipOption], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(17, value, flags)
            return

        self._set_batch_int32_array(17, value, flags)

    SlipOption = property(_get_SlipOption, _set_SlipOption) # type: BatchInt32ArrayProxy
    """
    Option for slip model. One of {fixedslip | variableslip*  }

    DSS property name: `SlipOption`, DSS property index: 17.
    """

    def _get_SlipOption_str(self) -> List[str]:
        return self._get_batch_str_prop(17)

    def _set_SlipOption_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_SlipOption(value, flags)

    SlipOption_str = property(_get_SlipOption_str, _set_SlipOption_str) # type: List[str]
    """
    Option for slip model. One of {fixedslip | variableslip*  }

    DSS property name: `SlipOption`, DSS property index: 17.
    """

    def _get_Yearly_str(self) -> List[str]:
        return self._get_batch_str_prop(18)

    def _set_Yearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(18, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: List[str]
    """
    LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

    DSS property name: `Yearly`, DSS property index: 18.
    """

    def _get_Yearly(self) -> List[LoadShape]:
        return self._get_batch_obj_prop(18)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(18, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: List[LoadShape]
    """
    LOADSHAPE object to use for yearly simulations.  Must be previously defined as a Loadshape object. Is set to the Daily load shape  when Daily is defined.  The daily load shape is repeated in this case. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. The default is no variation.

    DSS property name: `Yearly`, DSS property index: 18.
    """

    def _get_Daily_str(self) -> List[str]:
        return self._get_batch_str_prop(19)

    def _set_Daily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(19, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: List[str]
    """
    LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

    DSS property name: `Daily`, DSS property index: 19.
    """

    def _get_Daily(self) -> List[LoadShape]:
        return self._get_batch_obj_prop(19)

    def _set_Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(19, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: List[LoadShape]
    """
    LOADSHAPE object to use for daily simulations.  Must be previously defined as a Loadshape object of 24 hrs, typically. Set Status=Fixed to ignore Loadshape designation. Set to NONE to reset to no loadshape. Default is no variation (constant) if not defined. Side effect: Sets Yearly load shape if not already defined.

    DSS property name: `Daily`, DSS property index: 19.
    """

    def _get_Duty_str(self) -> List[str]:
        return self._get_batch_str_prop(20)

    def _set_Duty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(20, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: List[str]
    """
    LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

    DSS property name: `Duty`, DSS property index: 20.
    """

    def _get_Duty(self) -> List[LoadShape]:
        return self._get_batch_obj_prop(20)

    def _set_Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(20, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: List[LoadShape]
    """
    LOADSHAPE object to use for duty cycle simulations.  Must be previously defined as a Loadshape object.  Typically would have time intervals less than 1 hr. Designate the number of points to solve using the Set Number=xxxx command. If there are fewer points in the actual shape, the shape is assumed to repeat.Set to NONE to reset to no loadshape. Set Status=Fixed to ignore Loadshape designation.  Defaults to Daily curve If not specified.

    DSS property name: `Duty`, DSS property index: 20.
    """

    def _get_DebugTrace(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(21)
        ]

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(21, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: List[bool]
    """
    [Yes | No*] Write DebugTrace file.

    DSS property name: `DebugTrace`, DSS property index: 21.
    """

    def _get_Spectrum_str(self) -> List[str]:
        return self._get_batch_str_prop(22)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(22, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]
    """
    Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

    DSS property name: `Spectrum`, DSS property index: 22.
    """

    def _get_Spectrum(self) -> List[SpectrumObj]:
        return self._get_batch_obj_prop(22)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(22, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]
    """
    Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter. Default value is "default", which is defined when the DSS starts.

    DSS property name: `Spectrum`, DSS property index: 22.
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 23)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 23.
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(24)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(24, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 24.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 25.
        """
        self._set_batch_string(25, value, flags)

class IndMach012BatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kV: Union[float, Float64Array]
    kW: Union[float, Float64Array]
    PF: Union[float, Float64Array]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    kVA: Union[float, Float64Array]
    H: Union[float, Float64Array]
    D: Union[float, Float64Array]
    puRs: Union[float, Float64Array]
    puXs: Union[float, Float64Array]
    puRr: Union[float, Float64Array]
    puXr: Union[float, Float64Array]
    puXm: Union[float, Float64Array]
    Slip: Union[float, Float64Array]
    MaxSlip: Union[float, Float64Array]
    SlipOption: Union[AnyStr, int, enums.IndMach012SlipOption, List[AnyStr], List[int], List[enums.IndMach012SlipOption], Int32Array]
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    DebugTrace: bool
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IIndMach012(IDSSObj, IndMach012Batch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, IndMach012, IndMach012Batch)
        IndMach012Batch.__init__(self, self._api_util, sync_cls_idx=IndMach012._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> IndMach012:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> IndMach012Batch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) IndMach012 objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[IndMach012]:
            yield from IndMach012Batch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[IndMach012Properties]) -> IndMach012:
        """
        Creates a new IndMach012.

        :param name: The object's name is a required positional argument.

        :param activate: Activation (setting `activate` to true) is useful for integration with the classic API, and some internal OpenDSS commands.
        If you interact with this object only via the Alt API, no need to activate it (due to performance costs).

        :param begin_edit: This controls how the edit context is left after the object creation:
        - `True`: The object will be left in the edit state, requiring an `end_edit` call or equivalent.
        - `False`: No edit context is started.
        - `None`: If no properties are passed as keyword arguments, the object will be left in the edit state (assumes the user will fill the properties from Python attributes). Otherwise, the internal edit context will be finalized.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns the new DSS object, wrapped in Python.

        Note that, to make it easier for new users where the edit context might not be too relevant, AltDSS automatically opens/closes edit contexts for single properties if the object is not in the edit state already.
        """
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[IndMach012BatchProperties]) -> IndMach012Batch:
        """
        Creates a new batch of IndMach012 objects

        Either `names`, `count` or `df` is required. 

        :param begin_edit: The argument `begin_edit` indicates if the user want to leave the elements in the edit state, and requires a call to `end_edit()` or equivalent. The default `begin_edit` is set to `None`. With `None`, the behavior will be adjusted according the default of how the batch is created.
        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :param names: When using a list of names, each new object will match the names from this list. `begin_edit` defaults to `True` if no arguments for properties were passed, `False` otherwise.
        :param count: When using `count`, new objects will be created with based on a random prefix, with an increasing integer up to `count`. `begin_edit` defaults to `True` if no arguments for properties were passed, `False` otherwise.
        :param df: Currently **EXPERIMENTAL AND LIMITED**, tries to get the columns from a dataframe to populate the names and the DSS properties. `begin_edit` defaults to `False`.
        :return: Returns the new batch of DSS objects, wrapped in Python.

        Note that, to make it easier for new users where the edit context might not be too relevant, AltDSS automatically opens/closes edit contexts for single properties if the object is not in the edit state already.
        """
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
