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
from .PDElement import PDElementBatchMixin, PDElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .TransformerExtras import TransformerObjMixin

class AutoTrans(DSSObj, CircuitElementMixin, PDElementMixin, TransformerObjMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PDElementMixin._extra_slots + TransformerObjMixin._extra_slots
    _cls_name = 'AutoTrans'
    _cls_idx = 41
    _cls_int_idx = {
        1,
        2,
        3,
        11,
        30,
        33,
        39,
        40,
        48,
    }
    _cls_float_idx = {
        6,
        7,
        8,
        9,
        10,
        17,
        18,
        19,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        31,
        32,
        35,
        36,
        42,
        43,
        44,
        45,
        46,
        47,
    }
    _cls_prop_idx = {
        'phases': 1,
        'windings': 2,
        'wdg': 3,
        'bus': 4,
        'conn': 5,
        'kv': 6,
        'kva': 7,
        'tap': 8,
        'pctr': 9,
        '%r': 9,
        'rdcohms': 10,
        'core': 11,
        'buses': 12,
        'conns': 13,
        'kvs': 14,
        'kvas': 15,
        'taps': 16,
        'xhx': 17,
        'xht': 18,
        'xxt': 19,
        'xscarray': 20,
        'thermal': 21,
        'n': 22,
        'm': 23,
        'flrise': 24,
        'hsrise': 25,
        'pctloadloss': 26,
        '%loadloss': 26,
        'pctnoloadloss': 27,
        '%noloadloss': 27,
        'normhkva': 28,
        'emerghkva': 29,
        'sub': 30,
        'maxtap': 31,
        'mintap': 32,
        'numtaps': 33,
        'subname': 34,
        'pctimag': 35,
        '%imag': 35,
        'ppm_antifloat': 36,
        'pctrs': 37,
        '%rs': 37,
        'bank': 38,
        'xrconst': 39,
        'leadlag': 40,
        'wdgcurrents': 41,
        'normamps': 42,
        'emergamps': 43,
        'faultrate': 44,
        'pctperm': 45,
        'repair': 46,
        'basefreq': 47,
        'enabled': 48,
        'like': 49,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PDElementMixin.__init__(self)
       TransformerObjMixin.__init__(self)

    def edit(self, **kwargs: Unpack[AutoTransProperties]) -> AutoTrans:
        """
        Edit this AutoTrans.

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
    Number of phases this AutoTrans. Default is 3.

    DSS property name: `Phases`, DSS property index: 1.
    """

    def _get_Windings(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Windings(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Windings = property(_get_Windings, _set_Windings) # type: int
    """
    Number of windings, this AutoTrans. (Also is the number of terminals) Default is 2. This property triggers memory allocation for the AutoTrans and will cause other properties to revert to default values.

    DSS property name: `Windings`, DSS property index: 2.
    """

    def _get_pctR(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 9)

    def _set_pctR(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(9, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: Float64Array
    """
    Percent ac resistance this winding.  This value is for the power flow model.Is derived from the full load losses in the transformer test report.

    DSS property name: `%R`, DSS property index: 9.
    """

    def _get_RDCOhms(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 10)

    def _set_RDCOhms(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(10, value, flags)

    RDCOhms = property(_get_RDCOhms, _set_RDCOhms) # type: Float64Array
    """
    Winding dc resistance in OHMS. Specify this for GIC analysis. From transformer test report (divide by number of phases). Defaults to 85% of %R property (the ac value that includes stray losses).

    DSS property name: `RDCOhms`, DSS property index: 10.
    """

    def _get_Core(self) -> enums.CoreType:
        return enums.CoreType(self._lib.Obj_GetInt32(self._ptr, 11))

    def _set_Core(self, value: Union[AnyStr, int, enums.CoreType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(11, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 11, value, flags)

    Core = property(_get_Core, _set_Core) # type: enums.CoreType
    """
    {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis in auxiliary programs. Not used inside OpenDSS.

    DSS property name: `Core`, DSS property index: 11.
    """

    def _get_Core_str(self) -> str:
        return self._get_prop_string(11)

    def _set_Core_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Core(value, flags)

    Core_str = property(_get_Core_str, _set_Core_str) # type: str
    """
    {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis in auxiliary programs. Not used inside OpenDSS.

    DSS property name: `Core`, DSS property index: 11.
    """

    def _get_Buses(self) -> List[str]:
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 12)

    def _set_Buses(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 12, value_ptr, value_count, flags)
        self._check_for_error()

    Buses = property(_get_Buses, _set_Buses) # type: List[str]
    """
    Use this to specify all the bus connections at once using an array. Example:

    New AutoTrans.T1 buses=[Hbus, Xbus]

    DSS property name: `Buses`, DSS property index: 12.
    """

    def _get_Conns(self) -> List[enums.AutoTransConnection]:
        return [enums.AutoTransConnection(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 13)]

    def _set_Conns(self, value: Union[List[Union[int, enums.AutoTransConnection]], List[AnyStr]], flags: enums.SetterFlags = 0):
        if len(value) and not isinstance(value[0], int):
            self._set_string_array_o(13, value, flags)
            return
        self._set_int32_array_o(13, value, flags)

    Conns = property(_get_Conns, _set_Conns) # type: enums.AutoTransConnection
    """
    Use this to specify all the Winding connections at once using an array. Example:

    New AutoTrans.T1 buses=[Hbus, Xbus] ~ conns=(series, wye)

    DSS property name: `Conns`, DSS property index: 13.
    """

    def _get_Conns_str(self) -> List[str]:
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 13)

    def _set_Conns_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conns(value, flags)

    Conns_str = property(_get_Conns_str, _set_Conns_str) # type: List[str]
    """
    Use this to specify all the Winding connections at once using an array. Example:

    New AutoTrans.T1 buses=[Hbus, Xbus] ~ conns=(series, wye)

    DSS property name: `Conns`, DSS property index: 13.
    """

    def _get_kVs(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    def _set_kVs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(14, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: Float64Array
    """
    Use this to specify the kV ratings of all windings at once using an array. Example:

    New AutoTrans.T1 buses=[Hbus, Xbus] 
    ~ conns=(series, wye)
    ~ kvs=(115, 12.47)

    See kV= property for voltage rules.

    DSS property name: `kVs`, DSS property index: 14.
    """

    def _get_kVAs(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 15)

    def _set_kVAs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(15, value, flags)

    kVAs = property(_get_kVAs, _set_kVAs) # type: Float64Array
    """
    Use this to specify the kVA ratings of all windings at once using an array.

    DSS property name: `kVAs`, DSS property index: 15.
    """

    def _get_Taps(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 16)

    def _set_Taps(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(16, value, flags)

    Taps = property(_get_Taps, _set_Taps) # type: Float64Array
    """
    Use this to specify the p.u. tap of all windings at once using an array.

    DSS property name: `Taps`, DSS property index: 16.
    """

    def _get_XHX(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_XHX(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    XHX = property(_get_XHX, _set_XHX) # type: float
    """
    Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding AutoTranss. On the kVA base of winding 1(H-X). 

    DSS property name: `XHX`, DSS property index: 17.
    """

    def _get_XHT(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_XHT(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    XHT = property(_get_XHT, _set_XHT) # type: float
    """
    Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding AutoTranss only. On the kVA base of winding 1(H-X). 

    DSS property name: `XHT`, DSS property index: 18.
    """

    def _get_XXT(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 19)

    def _set_XXT(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 19, value, flags)

    XXT = property(_get_XXT, _set_XXT) # type: float
    """
    Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding AutoTranss only. On the kVA base of winding 1(H-X).  

    DSS property name: `XXT`, DSS property index: 19.
    """

    def _get_XSCArray(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 20)

    def _set_XSCArray(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(20, value, flags)

    XSCArray = property(_get_XSCArray, _set_XSCArray) # type: Float64Array
    """
    Use this to specify the percent reactance between all pairs of windings as an array. All values are on the kVA base of winding 1.  The order of the values is as follows:

    (x12 13 14... 23 24.. 34 ..)  

    There will be n(n-1)/2 values, where n=number of windings.

    DSS property name: `XSCArray`, DSS property index: 20.
    """

    def _get_Thermal(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_Thermal(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    Thermal = property(_get_Thermal, _set_Thermal) # type: float
    """
    Thermal time constant of the AutoTrans in hours.  Typically about 2.

    DSS property name: `Thermal`, DSS property index: 21.
    """

    def _get_n(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_n(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    n = property(_get_n, _set_n) # type: float
    """
    n Exponent for thermal properties in IEEE C57.  Typically 0.8.

    DSS property name: `n`, DSS property index: 22.
    """

    def _get_m(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_m(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    m = property(_get_m, _set_m) # type: float
    """
    m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

    DSS property name: `m`, DSS property index: 23.
    """

    def _get_FLRise(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_FLRise(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    FLRise = property(_get_FLRise, _set_FLRise) # type: float
    """
    Temperature rise, deg C, for full load.  Default is 65.

    DSS property name: `FLRise`, DSS property index: 24.
    """

    def _get_HSRise(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_HSRise(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    HSRise = property(_get_HSRise, _set_HSRise) # type: float
    """
    Hot spot temperature rise, deg C.  Default is 15.

    DSS property name: `HSRise`, DSS property index: 25.
    """

    def _get_pctLoadLoss(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_pctLoadLoss(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    pctLoadLoss = property(_get_pctLoadLoss, _set_pctLoadLoss) # type: float
    """
    Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

    DSS property name: `%LoadLoss`, DSS property index: 26.
    """

    def _get_pctNoLoadLoss(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_pctNoLoadLoss(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    pctNoLoadLoss = property(_get_pctNoLoadLoss, _set_pctNoLoadLoss) # type: float
    """
    Percent no load losses at rated excitation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

    DSS property name: `%NoLoadLoss`, DSS property index: 27.
    """

    def _get_NormHkVA(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 28)

    def _set_NormHkVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 28, value, flags)

    NormHkVA = property(_get_NormHkVA, _set_NormHkVA) # type: float
    """
    Normal maximum kVA rating of H winding (winding 1+2).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

    DSS property name: `NormHkVA`, DSS property index: 28.
    """

    def _get_EmergHkVA(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    def _set_EmergHkVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 29, value, flags)

    EmergHkVA = property(_get_EmergHkVA, _set_EmergHkVA) # type: float
    """
    Emergency (contingency)  kVA rating of H winding (winding 1+2).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

    DSS property name: `EmergHkVA`, DSS property index: 29.
    """

    def _get_Sub(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 30) != 0

    def _set_Sub(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 30, value, flags)

    Sub = property(_get_Sub, _set_Sub) # type: bool
    """
    ={Yes|No}  Designates whether this AutoTrans is to be considered a substation.Default is No.

    DSS property name: `Sub`, DSS property index: 30.
    """

    def _get_MaxTap(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 31)

    def _set_MaxTap(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(31, value, flags)

    MaxTap = property(_get_MaxTap, _set_MaxTap) # type: Float64Array
    """
    Max per unit tap for the active winding.  Default is 1.10

    DSS property name: `MaxTap`, DSS property index: 31.
    """

    def _get_MinTap(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 32)

    def _set_MinTap(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(32, value, flags)

    MinTap = property(_get_MinTap, _set_MinTap) # type: Float64Array
    """
    Min per unit tap for the active winding.  Default is 0.90

    DSS property name: `MinTap`, DSS property index: 32.
    """

    def _get_NumTaps(self) -> Int32Array:
        return self._get_int32_array(self._lib.Obj_GetInt32Array, self._ptr, 33)

    def _set_NumTaps(self, value: Int32Array, flags: enums.SetterFlags = 0):
        self._set_int32_array_o(33, value, flags)

    NumTaps = property(_get_NumTaps, _set_NumTaps) # type: Int32Array
    """
    Total number of taps between min and max tap.  Default is 32 (16 raise and 16 lower taps about the neutral position). The neutral position is not counted.

    DSS property name: `NumTaps`, DSS property index: 33.
    """

    def _get_SubName(self) -> str:
        return self._get_prop_string(34)

    def _set_SubName(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(34, value, flags)

    SubName = property(_get_SubName, _set_SubName) # type: str
    """
    Substation Name. Optional. Default is null. If specified, printed on plots

    DSS property name: `SubName`, DSS property index: 34.
    """

    def _get_pctIMag(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    def _set_pctIMag(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 35, value, flags)

    pctIMag = property(_get_pctIMag, _set_pctIMag) # type: float
    """
    Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

    DSS property name: `%IMag`, DSS property index: 35.
    """

    def _get_ppm_Antifloat(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    def _set_ppm_Antifloat(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 36, value, flags)

    ppm_Antifloat = property(_get_ppm_Antifloat, _set_ppm_Antifloat) # type: float
    """
    Default=1 ppm.  Parts per million of AutoTrans winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

    DSS property name: `ppm_Antifloat`, DSS property index: 36.
    """

    def _get_pctRs(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 37)

    def _set_pctRs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(37, value, flags)

    pctRs = property(_get_pctRs, _set_pctRs) # type: Float64Array
    """
    Use this property to specify all the winding ac %resistances using an array. Example:

    New AutoTrans.T1 buses=[Hibus, lowbus] ~ %Rs=(0.2  0.3)

    DSS property name: `%Rs`, DSS property index: 37.
    """

    def _get_Bank(self) -> str:
        return self._get_prop_string(38)

    def _set_Bank(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(38, value, flags)

    Bank = property(_get_Bank, _set_Bank) # type: str
    """
    Name of the bank this transformer is part of, for CIM, MultiSpeak, and other interfaces.

    DSS property name: `Bank`, DSS property index: 38.
    """

    def _get_XRConst(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 39) != 0

    def _set_XRConst(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 39, value, flags)

    XRConst = property(_get_XRConst, _set_XRConst) # type: bool
    """
    ={Yes|No} Default is NO. Signifies whether or not the X/R is assumed constant for harmonic studies.

    DSS property name: `XRConst`, DSS property index: 39.
    """

    def _get_LeadLag(self) -> enums.PhaseSequence:
        return enums.PhaseSequence(self._lib.Obj_GetInt32(self._ptr, 40))

    def _set_LeadLag(self, value: Union[AnyStr, int, enums.PhaseSequence], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(40, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 40, value, flags)

    LeadLag = property(_get_LeadLag, _set_LeadLag) # type: enums.PhaseSequence
    """
    {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

    DSS property name: `LeadLag`, DSS property index: 40.
    """

    def _get_LeadLag_str(self) -> str:
        return self._get_prop_string(40)

    def _set_LeadLag_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LeadLag(value, flags)

    LeadLag_str = property(_get_LeadLag_str, _set_LeadLag_str) # type: str
    """
    {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

    DSS property name: `LeadLag`, DSS property index: 40.
    """

    def _get_NormAmps(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 42, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float
    """
    Normal rated current.

    DSS property name: `NormAmps`, DSS property index: 42.
    """

    def _get_EmergAmps(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 43)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 43, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float
    """
    Maximum or emerg current.

    DSS property name: `EmergAmps`, DSS property index: 43.
    """

    def _get_FaultRate(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    def _set_FaultRate(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 44, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: float
    """
    Failure rate per year.

    DSS property name: `FaultRate`, DSS property index: 44.
    """

    def _get_pctPerm(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 45)

    def _set_pctPerm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 45, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: float
    """
    Percent of failures that become permanent.

    DSS property name: `pctPerm`, DSS property index: 45.
    """

    def _get_Repair(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 46)

    def _set_Repair(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 46, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: float
    """
    Hours to repair.

    DSS property name: `Repair`, DSS property index: 46.
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 47)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 47, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 47.
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 48) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 48, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 48.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 49.
        """
        self._set_string_o(49, value)


class AutoTransProperties(TypedDict):
    Phases: int
    Windings: int
    pctR: Float64Array
    RDCOhms: Float64Array
    Core: Union[AnyStr, int, enums.CoreType]
    Buses: List[AnyStr]
    Conns: Union[List[Union[int, enums.AutoTransConnection]], List[AnyStr]]
    kVs: Float64Array
    kVAs: Float64Array
    Taps: Float64Array
    XHX: float
    XHT: float
    XXT: float
    XSCArray: Float64Array
    Thermal: float
    n: float
    m: float
    FLRise: float
    HSRise: float
    pctLoadLoss: float
    pctNoLoadLoss: float
    NormHkVA: float
    EmergHkVA: float
    Sub: bool
    MaxTap: Float64Array
    MinTap: Float64Array
    NumTaps: Int32Array
    SubName: AnyStr
    pctIMag: float
    ppm_Antifloat: float
    pctRs: Float64Array
    Bank: AnyStr
    XRConst: bool
    LeadLag: Union[AnyStr, int, enums.PhaseSequence]
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class AutoTransBatch(DSSBatch, CircuitElementBatchMixin, PDElementBatchMixin):
    _cls_name = 'AutoTrans'
    _obj_cls = AutoTrans
    _cls_idx = 41
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PDElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[AutoTransBatchProperties]) -> AutoTransBatch:
        """
        Edit this AutoTrans batch.

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
        def __iter__(self) -> Iterator[AutoTrans]:
            yield from DSSBatch.__iter__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy
    """
    Number of phases this AutoTrans. Default is 3.

    DSS property name: `Phases`, DSS property index: 1.
    """

    def _get_Windings(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 2)

    def _set_Windings(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Windings = property(_get_Windings, _set_Windings) # type: BatchInt32ArrayProxy
    """
    Number of windings, this AutoTrans. (Also is the number of terminals) Default is 2. This property triggers memory allocation for the AutoTrans and will cause other properties to revert to default values.

    DSS property name: `Windings`, DSS property index: 2.
    """

    def _get_pctR(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 9)
            for x in self._unpack()
        ]

    def _set_pctR(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(9, value, flags)

    pctR = property(_get_pctR, _set_pctR) # type: List[Float64Array]
    """
    Percent ac resistance this winding.  This value is for the power flow model.Is derived from the full load losses in the transformer test report.

    DSS property name: `%R`, DSS property index: 9.
    """

    def _get_RDCOhms(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 10)
            for x in self._unpack()
        ]

    def _set_RDCOhms(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(10, value, flags)

    RDCOhms = property(_get_RDCOhms, _set_RDCOhms) # type: List[Float64Array]
    """
    Winding dc resistance in OHMS. Specify this for GIC analysis. From transformer test report (divide by number of phases). Defaults to 85% of %R property (the ac value that includes stray losses).

    DSS property name: `RDCOhms`, DSS property index: 10.
    """

    def _get_Core(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 11)

    def _set_Core(self, value: Union[AnyStr, int, enums.CoreType, List[AnyStr], List[int], List[enums.CoreType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(11, value, flags)
            return

        self._set_batch_int32_array(11, value, flags)

    Core = property(_get_Core, _set_Core) # type: BatchInt32ArrayProxy
    """
    {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis in auxiliary programs. Not used inside OpenDSS.

    DSS property name: `Core`, DSS property index: 11.
    """

    def _get_Core_str(self) -> List[str]:
        return self._get_batch_str_prop(11)

    def _set_Core_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Core(value, flags)

    Core_str = property(_get_Core_str, _set_Core_str) # type: List[str]
    """
    {Shell*|5-leg|3-Leg|1-phase|core-1-phase|4-leg} Core Type. Used for GIC analysis in auxiliary programs. Not used inside OpenDSS.

    DSS property name: `Core`, DSS property index: 11.
    """

    def _get_Buses(self) -> List[List[str]]:
        return self._get_string_ll(12)

    def _set_Buses(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 12, value_ptr, value_count, flags)

        self._check_for_error()

    Buses = property(_get_Buses, _set_Buses) # type: List[List[str]]
    """
    Use this to specify all the bus connections at once using an array. Example:

    New AutoTrans.T1 buses=[Hbus, Xbus]

    DSS property name: `Buses`, DSS property index: 12.
    """

    def _get_Conns(self) -> List[Int32Array]:
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 13)
            for x in self._unpack()
        ]

    def _set_Conns(self, value: Union[List[Union[int, enums.AutoTransConnection]], List[AnyStr]], flags: enums.SetterFlags = 0): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._unpack():
                self._lib.Obj_SetStringArray(x, 13, value_ptr, value_count, flags)

            self._check_for_error()
            return

        self._set_batch_int32_array(13, value, flags)

    Conns = property(_get_Conns, _set_Conns) # type: List[Int32Array]
    """
    Use this to specify all the Winding connections at once using an array. Example:

    New AutoTrans.T1 buses=[Hbus, Xbus] ~ conns=(series, wye)

    DSS property name: `Conns`, DSS property index: 13.
    """

    def _get_Conns_str(self) -> List[List[str]]:
        return self._get_string_ll(13)

    def _set_Conns_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conns(value, flags)

    Conns_str = property(_get_Conns_str, _set_Conns_str) # type: List[List[str]]
    """
    Use this to specify all the Winding connections at once using an array. Example:

    New AutoTrans.T1 buses=[Hbus, Xbus] ~ conns=(series, wye)

    DSS property name: `Conns`, DSS property index: 13.
    """

    def _get_kVs(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._unpack()
        ]

    def _set_kVs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(14, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: List[Float64Array]
    """
    Use this to specify the kV ratings of all windings at once using an array. Example:

    New AutoTrans.T1 buses=[Hbus, Xbus] 
    ~ conns=(series, wye)
    ~ kvs=(115, 12.47)

    See kV= property for voltage rules.

    DSS property name: `kVs`, DSS property index: 14.
    """

    def _get_kVAs(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 15)
            for x in self._unpack()
        ]

    def _set_kVAs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(15, value, flags)

    kVAs = property(_get_kVAs, _set_kVAs) # type: List[Float64Array]
    """
    Use this to specify the kVA ratings of all windings at once using an array.

    DSS property name: `kVAs`, DSS property index: 15.
    """

    def _get_Taps(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 16)
            for x in self._unpack()
        ]

    def _set_Taps(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(16, value, flags)

    Taps = property(_get_Taps, _set_Taps) # type: List[Float64Array]
    """
    Use this to specify the p.u. tap of all windings at once using an array.

    DSS property name: `Taps`, DSS property index: 16.
    """

    def _get_XHX(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 17)

    def _set_XHX(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    XHX = property(_get_XHX, _set_XHX) # type: BatchFloat64ArrayProxy
    """
    Use this to specify the percent reactance, H-L (winding 1 to winding 2).  Use for 2- or 3-winding AutoTranss. On the kVA base of winding 1(H-X). 

    DSS property name: `XHX`, DSS property index: 17.
    """

    def _get_XHT(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 18)

    def _set_XHT(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    XHT = property(_get_XHT, _set_XHT) # type: BatchFloat64ArrayProxy
    """
    Use this to specify the percent reactance, H-T (winding 1 to winding 3).  Use for 3-winding AutoTranss only. On the kVA base of winding 1(H-X). 

    DSS property name: `XHT`, DSS property index: 18.
    """

    def _get_XXT(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 19)

    def _set_XXT(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(19, value, flags)

    XXT = property(_get_XXT, _set_XXT) # type: BatchFloat64ArrayProxy
    """
    Use this to specify the percent reactance, L-T (winding 2 to winding 3).  Use for 3-winding AutoTranss only. On the kVA base of winding 1(H-X).  

    DSS property name: `XXT`, DSS property index: 19.
    """

    def _get_XSCArray(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 20)
            for x in self._unpack()
        ]

    def _set_XSCArray(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(20, value, flags)

    XSCArray = property(_get_XSCArray, _set_XSCArray) # type: List[Float64Array]
    """
    Use this to specify the percent reactance between all pairs of windings as an array. All values are on the kVA base of winding 1.  The order of the values is as follows:

    (x12 13 14... 23 24.. 34 ..)  

    There will be n(n-1)/2 values, where n=number of windings.

    DSS property name: `XSCArray`, DSS property index: 20.
    """

    def _get_Thermal(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 21)

    def _set_Thermal(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    Thermal = property(_get_Thermal, _set_Thermal) # type: BatchFloat64ArrayProxy
    """
    Thermal time constant of the AutoTrans in hours.  Typically about 2.

    DSS property name: `Thermal`, DSS property index: 21.
    """

    def _get_n(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 22)

    def _set_n(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    n = property(_get_n, _set_n) # type: BatchFloat64ArrayProxy
    """
    n Exponent for thermal properties in IEEE C57.  Typically 0.8.

    DSS property name: `n`, DSS property index: 22.
    """

    def _get_m(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 23)

    def _set_m(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    m = property(_get_m, _set_m) # type: BatchFloat64ArrayProxy
    """
    m Exponent for thermal properties in IEEE C57.  Typically 0.9 - 1.0

    DSS property name: `m`, DSS property index: 23.
    """

    def _get_FLRise(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 24)

    def _set_FLRise(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    FLRise = property(_get_FLRise, _set_FLRise) # type: BatchFloat64ArrayProxy
    """
    Temperature rise, deg C, for full load.  Default is 65.

    DSS property name: `FLRise`, DSS property index: 24.
    """

    def _get_HSRise(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 25)

    def _set_HSRise(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    HSRise = property(_get_HSRise, _set_HSRise) # type: BatchFloat64ArrayProxy
    """
    Hot spot temperature rise, deg C.  Default is 15.

    DSS property name: `HSRise`, DSS property index: 25.
    """

    def _get_pctLoadLoss(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 26)

    def _set_pctLoadLoss(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    pctLoadLoss = property(_get_pctLoadLoss, _set_pctLoadLoss) # type: BatchFloat64ArrayProxy
    """
    Percent load loss at full load. The %R of the High and Low windings (1 and 2) are adjusted to agree at rated kVA loading.

    DSS property name: `%LoadLoss`, DSS property index: 26.
    """

    def _get_pctNoLoadLoss(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 27)

    def _set_pctNoLoadLoss(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    pctNoLoadLoss = property(_get_pctNoLoadLoss, _set_pctNoLoadLoss) # type: BatchFloat64ArrayProxy
    """
    Percent no load losses at rated excitation voltage. Default is 0. Converts to a resistance in parallel with the magnetizing impedance in each winding.

    DSS property name: `%NoLoadLoss`, DSS property index: 27.
    """

    def _get_NormHkVA(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 28)

    def _set_NormHkVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(28, value, flags)

    NormHkVA = property(_get_NormHkVA, _set_NormHkVA) # type: BatchFloat64ArrayProxy
    """
    Normal maximum kVA rating of H winding (winding 1+2).  Usually 100% - 110% of maximum nameplate rating, depending on load shape. Defaults to 110% of kVA rating of Winding 1.

    DSS property name: `NormHkVA`, DSS property index: 28.
    """

    def _get_EmergHkVA(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 29)

    def _set_EmergHkVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(29, value, flags)

    EmergHkVA = property(_get_EmergHkVA, _set_EmergHkVA) # type: BatchFloat64ArrayProxy
    """
    Emergency (contingency)  kVA rating of H winding (winding 1+2).  Usually 140% - 150% of maximum nameplate rating, depending on load shape. Defaults to 150% of kVA rating of Winding 1.

    DSS property name: `EmergHkVA`, DSS property index: 29.
    """

    def _get_Sub(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(30)
        ]

    def _set_Sub(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(30, value, flags)

    Sub = property(_get_Sub, _set_Sub) # type: List[bool]
    """
    ={Yes|No}  Designates whether this AutoTrans is to be considered a substation.Default is No.

    DSS property name: `Sub`, DSS property index: 30.
    """

    def _get_MaxTap(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 31)
            for x in self._unpack()
        ]

    def _set_MaxTap(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(31, value, flags)

    MaxTap = property(_get_MaxTap, _set_MaxTap) # type: List[Float64Array]
    """
    Max per unit tap for the active winding.  Default is 1.10

    DSS property name: `MaxTap`, DSS property index: 31.
    """

    def _get_MinTap(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 32)
            for x in self._unpack()
        ]

    def _set_MinTap(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(32, value, flags)

    MinTap = property(_get_MinTap, _set_MinTap) # type: List[Float64Array]
    """
    Min per unit tap for the active winding.  Default is 0.90

    DSS property name: `MinTap`, DSS property index: 32.
    """

    def _get_NumTaps(self) -> List[Int32Array]:
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 33)
            for x in self._unpack()
        ]

    def _set_NumTaps(self, value: Union[Int32Array, List[Int32Array]], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array_prop(33, value, flags)

    NumTaps = property(_get_NumTaps, _set_NumTaps) # type: List[Int32Array]
    """
    Total number of taps between min and max tap.  Default is 32 (16 raise and 16 lower taps about the neutral position). The neutral position is not counted.

    DSS property name: `NumTaps`, DSS property index: 33.
    """

    def _get_SubName(self) -> List[str]:
        return self._get_batch_str_prop(34)

    def _set_SubName(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(34, value, flags)

    SubName = property(_get_SubName, _set_SubName) # type: List[str]
    """
    Substation Name. Optional. Default is null. If specified, printed on plots

    DSS property name: `SubName`, DSS property index: 34.
    """

    def _get_pctIMag(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 35)

    def _set_pctIMag(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(35, value, flags)

    pctIMag = property(_get_pctIMag, _set_pctIMag) # type: BatchFloat64ArrayProxy
    """
    Percent magnetizing current. Default=0.0. Magnetizing branch is in parallel with windings in each phase. Also, see "ppm_antifloat".

    DSS property name: `%IMag`, DSS property index: 35.
    """

    def _get_ppm_Antifloat(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 36)

    def _set_ppm_Antifloat(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(36, value, flags)

    ppm_Antifloat = property(_get_ppm_Antifloat, _set_ppm_Antifloat) # type: BatchFloat64ArrayProxy
    """
    Default=1 ppm.  Parts per million of AutoTrans winding VA rating connected to ground to protect against accidentally floating a winding without a reference. If positive then the effect is adding a very large reactance to ground.  If negative, then a capacitor.

    DSS property name: `ppm_Antifloat`, DSS property index: 36.
    """

    def _get_pctRs(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 37)
            for x in self._unpack()
        ]

    def _set_pctRs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(37, value, flags)

    pctRs = property(_get_pctRs, _set_pctRs) # type: List[Float64Array]
    """
    Use this property to specify all the winding ac %resistances using an array. Example:

    New AutoTrans.T1 buses=[Hibus, lowbus] ~ %Rs=(0.2  0.3)

    DSS property name: `%Rs`, DSS property index: 37.
    """

    def _get_Bank(self) -> List[str]:
        return self._get_batch_str_prop(38)

    def _set_Bank(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(38, value, flags)

    Bank = property(_get_Bank, _set_Bank) # type: List[str]
    """
    Name of the bank this transformer is part of, for CIM, MultiSpeak, and other interfaces.

    DSS property name: `Bank`, DSS property index: 38.
    """

    def _get_XRConst(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(39)
        ]

    def _set_XRConst(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(39, value, flags)

    XRConst = property(_get_XRConst, _set_XRConst) # type: List[bool]
    """
    ={Yes|No} Default is NO. Signifies whether or not the X/R is assumed constant for harmonic studies.

    DSS property name: `XRConst`, DSS property index: 39.
    """

    def _get_LeadLag(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 40)

    def _set_LeadLag(self, value: Union[AnyStr, int, enums.PhaseSequence, List[AnyStr], List[int], List[enums.PhaseSequence], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(40, value, flags)
            return

        self._set_batch_int32_array(40, value, flags)

    LeadLag = property(_get_LeadLag, _set_LeadLag) # type: BatchInt32ArrayProxy
    """
    {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

    DSS property name: `LeadLag`, DSS property index: 40.
    """

    def _get_LeadLag_str(self) -> List[str]:
        return self._get_batch_str_prop(40)

    def _set_LeadLag_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LeadLag(value, flags)

    LeadLag_str = property(_get_LeadLag_str, _set_LeadLag_str) # type: List[str]
    """
    {Lead | Lag (default) | ANSI (default) | Euro } Designation in mixed Delta-wye connections the relationship between HV to LV winding. Default is ANSI 30 deg lag, e.g., Dy1 of Yd1 vector group. To get typical European Dy11 connection, specify either "lead" or "Euro"

    DSS property name: `LeadLag`, DSS property index: 40.
    """

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 42)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(42, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy
    """
    Normal rated current.

    DSS property name: `NormAmps`, DSS property index: 42.
    """

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 43)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(43, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy
    """
    Maximum or emerg current.

    DSS property name: `EmergAmps`, DSS property index: 43.
    """

    def _get_FaultRate(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 44)

    def _set_FaultRate(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(44, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: BatchFloat64ArrayProxy
    """
    Failure rate per year.

    DSS property name: `FaultRate`, DSS property index: 44.
    """

    def _get_pctPerm(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 45)

    def _set_pctPerm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(45, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: BatchFloat64ArrayProxy
    """
    Percent of failures that become permanent.

    DSS property name: `pctPerm`, DSS property index: 45.
    """

    def _get_Repair(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 46)

    def _set_Repair(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(46, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: BatchFloat64ArrayProxy
    """
    Hours to repair.

    DSS property name: `Repair`, DSS property index: 46.
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 47)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(47, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 47.
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(48)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(48, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 48.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 49.
        """
        self._set_batch_string(49, value, flags)

class AutoTransBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Windings: Union[int, Int32Array]
    pctR: Float64Array
    RDCOhms: Float64Array
    Core: Union[AnyStr, int, enums.CoreType, List[AnyStr], List[int], List[enums.CoreType], Int32Array]
    Buses: List[AnyStr]
    Conns: Union[List[Union[int, enums.AutoTransConnection]], List[AnyStr]]
    kVs: Float64Array
    kVAs: Float64Array
    Taps: Float64Array
    XHX: Union[float, Float64Array]
    XHT: Union[float, Float64Array]
    XXT: Union[float, Float64Array]
    XSCArray: Float64Array
    Thermal: Union[float, Float64Array]
    n: Union[float, Float64Array]
    m: Union[float, Float64Array]
    FLRise: Union[float, Float64Array]
    HSRise: Union[float, Float64Array]
    pctLoadLoss: Union[float, Float64Array]
    pctNoLoadLoss: Union[float, Float64Array]
    NormHkVA: Union[float, Float64Array]
    EmergHkVA: Union[float, Float64Array]
    Sub: bool
    MaxTap: Float64Array
    MinTap: Float64Array
    NumTaps: Int32Array
    SubName: Union[AnyStr, List[AnyStr]]
    pctIMag: Union[float, Float64Array]
    ppm_Antifloat: Union[float, Float64Array]
    pctRs: Float64Array
    Bank: Union[AnyStr, List[AnyStr]]
    XRConst: bool
    LeadLag: Union[AnyStr, int, enums.PhaseSequence, List[AnyStr], List[int], List[enums.PhaseSequence], Int32Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IAutoTrans(IDSSObj, AutoTransBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, AutoTrans, AutoTransBatch)
        AutoTransBatch.__init__(self, self._api_util, sync_cls_idx=AutoTrans._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> AutoTrans:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> AutoTransBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) AutoTrans objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[AutoTrans]:
            yield from AutoTransBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[AutoTransProperties]) -> AutoTrans:
        """
        Creates a new AutoTrans.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[AutoTransBatchProperties]) -> AutoTransBatch:
        """
        Creates a new batch of AutoTrans objects

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
