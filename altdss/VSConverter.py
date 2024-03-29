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
from .Spectrum import Spectrum as SpectrumObj

class VSConverter(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'VSConverter'
    _cls_idx = 46
    _cls_int_idx = {
        1,
        6,
        19,
        22,
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
        17,
        18,
        21,
    }
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kvac': 3,
        'kvdc': 4,
        'kw': 5,
        'ndc': 6,
        'rac': 7,
        'xac': 8,
        'm0': 9,
        'd0': 10,
        'mmin': 11,
        'mmax': 12,
        'iacmax': 13,
        'idcmax': 14,
        'vacref': 15,
        'pacref': 16,
        'qacref': 17,
        'vdcref': 18,
        'vscmode': 19,
        'spectrum': 20,
        'basefreq': 21,
        'enabled': 22,
        'like': 23,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[VSConverterProperties]) -> VSConverter:
        """
        Edit this VSConverter.

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
    Number of AC plus DC conductors. Default is 4. AC phases numbered before DC conductors.

    DSS property name: `Phases`, DSS property index: 1.
    """

    def _get_Bus1(self) -> str:
        return self._get_prop_string(2)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str
    """
    Name of converter bus, containing both AC and DC conductors. Bus2 is always ground.

    DSS property name: `Bus1`, DSS property index: 2.
    """

    def _get_kVAC(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kVAC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kVAC = property(_get_kVAC, _set_kVAC) # type: float
    """
    Nominal AC line-neutral voltage in kV. Must be specified > 0.

    DSS property name: `kVAC`, DSS property index: 3.
    """

    def _get_kVDC(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_kVDC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    kVDC = property(_get_kVDC, _set_kVDC) # type: float
    """
    Nominal DC voltage in kV. Must be specified > 0.

    DSS property name: `kVDC`, DSS property index: 4.
    """

    def _get_kW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    kW = property(_get_kW, _set_kW) # type: float
    """
    Nominal converter power in kW. Must be specified > 0.

    DSS property name: `kW`, DSS property index: 5.
    """

    def _get_NDC(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 6)

    def _set_NDC(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    NDC = property(_get_NDC, _set_NDC) # type: int
    """
    Number of DC conductors. Default is 1. DC conductors numbered after AC phases.

    DSS property name: `NDC`, DSS property index: 6.
    """

    def _get_RAC(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_RAC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    RAC = property(_get_RAC, _set_RAC) # type: float
    """
    AC resistance (ohms) for the converter transformer, plus any series reactors. Default is 0.
    Must be 0 for Vac control mode.

    DSS property name: `RAC`, DSS property index: 7.
    """

    def _get_XAC(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_XAC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    XAC = property(_get_XAC, _set_XAC) # type: float
    """
    AC reactance (ohms) for the converter transformer, plus any series reactors. Default is 0.
    Must be 0 for Vac control mode. Must be >0 for PacVac, PacQac or VacVdc control mode.

    DSS property name: `XAC`, DSS property index: 8.
    """

    def _get_M0(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_M0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    M0 = property(_get_M0, _set_M0) # type: float
    """
    Fixed or initial value of the modulation index. Default is 0.5.

    DSS property name: `M0`, DSS property index: 9.
    """

    def _get_d0(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_d0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    d0 = property(_get_d0, _set_d0) # type: float
    """
    Fixed or initial value of the power angle in degrees. Default is 0.

    DSS property name: `d0`, DSS property index: 10.
    """

    def _get_MMin(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_MMin(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    MMin = property(_get_MMin, _set_MMin) # type: float
    """
    Minimum value of modulation index. Default is 0.1.

    DSS property name: `MMin`, DSS property index: 11.
    """

    def _get_MMax(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_MMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    MMax = property(_get_MMax, _set_MMax) # type: float
    """
    Maximum value of modulation index. Default is 0.9.

    DSS property name: `MMax`, DSS property index: 12.
    """

    def _get_IACMax(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_IACMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    IACMax = property(_get_IACMax, _set_IACMax) # type: float
    """
    Maximum value of AC line current, per-unit of nominal. Default is 2.

    DSS property name: `IACMax`, DSS property index: 13.
    """

    def _get_IDCMax(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_IDCMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    IDCMax = property(_get_IDCMax, _set_IDCMax) # type: float
    """
    Maximum value of DC current, per-unit of nominal. Default is 2.

    DSS property name: `IDCMax`, DSS property index: 14.
    """

    def _get_VACRef(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_VACRef(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    VACRef = property(_get_VACRef, _set_VACRef) # type: float
    """
    Reference AC line-to-neutral voltage, RMS Volts. Default is 0.
    Applies to PacVac and VdcVac control modes, influencing m.

    DSS property name: `VACRef`, DSS property index: 15.
    """

    def _get_PACRef(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_PACRef(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    PACRef = property(_get_PACRef, _set_PACRef) # type: float
    """
    Reference total AC real power, Watts. Default is 0.
    Applies to PacVac and PacQac control modes, influencing d.

    DSS property name: `PACRef`, DSS property index: 16.
    """

    def _get_QACRef(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_QACRef(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    QACRef = property(_get_QACRef, _set_QACRef) # type: float
    """
    Reference total AC reactive power, Vars. Default is 0.
    Applies to PacQac and VdcQac control modes, influencing m.

    DSS property name: `QACRef`, DSS property index: 17.
    """

    def _get_VDCRef(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_VDCRef(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    VDCRef = property(_get_VDCRef, _set_VDCRef) # type: float
    """
    Reference DC voltage, Volts. Default is 0.
    Applies to VdcVac control mode, influencing d.

    DSS property name: `VDCRef`, DSS property index: 18.
    """

    def _get_VSCMode(self) -> enums.VSConverterControlMode:
        return enums.VSConverterControlMode(self._lib.Obj_GetInt32(self._ptr, 19))

    def _set_VSCMode(self, value: Union[AnyStr, int, enums.VSConverterControlMode], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(19, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 19, value, flags)

    VSCMode = property(_get_VSCMode, _set_VSCMode) # type: enums.VSConverterControlMode
    """
    Control Mode (Fixed|PacVac|PacQac|VdcVac|VdcQac). Default is Fixed.

    DSS property name: `VSCMode`, DSS property index: 19.
    """

    def _get_VSCMode_str(self) -> str:
        return self._get_prop_string(19)

    def _set_VSCMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_VSCMode(value, flags)

    VSCMode_str = property(_get_VSCMode_str, _set_VSCMode_str) # type: str
    """
    Control Mode (Fixed|PacVac|PacQac|VdcVac|VdcQac). Default is Fixed.

    DSS property name: `VSCMode`, DSS property index: 19.
    """

    def _get_Spectrum_str(self) -> str:
        return self._get_prop_string(20)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(20, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str
    """
    Name of harmonic spectrum for this device.

    DSS property name: `Spectrum`, DSS property index: 20.
    """

    def _get_Spectrum(self) -> SpectrumObj:
        return self._get_obj(20, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(20, value, flags)
            return

        self._set_string_o(20, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj
    """
    Name of harmonic spectrum for this device.

    DSS property name: `Spectrum`, DSS property index: 20.
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 21.
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 22) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 22, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 22.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 23.
        """
        self._set_string_o(23, value)


class VSConverterProperties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kVAC: float
    kVDC: float
    kW: float
    NDC: int
    RAC: float
    XAC: float
    M0: float
    d0: float
    MMin: float
    MMax: float
    IACMax: float
    IDCMax: float
    VACRef: float
    PACRef: float
    QACRef: float
    VDCRef: float
    VSCMode: Union[AnyStr, int, enums.VSConverterControlMode]
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class VSConverterBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'VSConverter'
    _obj_cls = VSConverter
    _cls_idx = 46
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[VSConverterBatchProperties]) -> VSConverterBatch:
        """
        Edit this VSConverter batch.

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
        def __iter__(self) -> Iterator[VSConverter]:
            yield from DSSBatch.__iter__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy
    """
    Number of AC plus DC conductors. Default is 4. AC phases numbered before DC conductors.

    DSS property name: `Phases`, DSS property index: 1.
    """

    def _get_Bus1(self) -> List[str]:
        return self._get_batch_str_prop(2)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]
    """
    Name of converter bus, containing both AC and DC conductors. Bus2 is always ground.

    DSS property name: `Bus1`, DSS property index: 2.
    """

    def _get_kVAC(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kVAC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kVAC = property(_get_kVAC, _set_kVAC) # type: BatchFloat64ArrayProxy
    """
    Nominal AC line-neutral voltage in kV. Must be specified > 0.

    DSS property name: `kVAC`, DSS property index: 3.
    """

    def _get_kVDC(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_kVDC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    kVDC = property(_get_kVDC, _set_kVDC) # type: BatchFloat64ArrayProxy
    """
    Nominal DC voltage in kV. Must be specified > 0.

    DSS property name: `kVDC`, DSS property index: 4.
    """

    def _get_kW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    kW = property(_get_kW, _set_kW) # type: BatchFloat64ArrayProxy
    """
    Nominal converter power in kW. Must be specified > 0.

    DSS property name: `kW`, DSS property index: 5.
    """

    def _get_NDC(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 6)

    def _set_NDC(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(6, value, flags)

    NDC = property(_get_NDC, _set_NDC) # type: BatchInt32ArrayProxy
    """
    Number of DC conductors. Default is 1. DC conductors numbered after AC phases.

    DSS property name: `NDC`, DSS property index: 6.
    """

    def _get_RAC(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 7)

    def _set_RAC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    RAC = property(_get_RAC, _set_RAC) # type: BatchFloat64ArrayProxy
    """
    AC resistance (ohms) for the converter transformer, plus any series reactors. Default is 0.
    Must be 0 for Vac control mode.

    DSS property name: `RAC`, DSS property index: 7.
    """

    def _get_XAC(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 8)

    def _set_XAC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    XAC = property(_get_XAC, _set_XAC) # type: BatchFloat64ArrayProxy
    """
    AC reactance (ohms) for the converter transformer, plus any series reactors. Default is 0.
    Must be 0 for Vac control mode. Must be >0 for PacVac, PacQac or VacVdc control mode.

    DSS property name: `XAC`, DSS property index: 8.
    """

    def _get_M0(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 9)

    def _set_M0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    M0 = property(_get_M0, _set_M0) # type: BatchFloat64ArrayProxy
    """
    Fixed or initial value of the modulation index. Default is 0.5.

    DSS property name: `M0`, DSS property index: 9.
    """

    def _get_d0(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 10)

    def _set_d0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    d0 = property(_get_d0, _set_d0) # type: BatchFloat64ArrayProxy
    """
    Fixed or initial value of the power angle in degrees. Default is 0.

    DSS property name: `d0`, DSS property index: 10.
    """

    def _get_MMin(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_MMin(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    MMin = property(_get_MMin, _set_MMin) # type: BatchFloat64ArrayProxy
    """
    Minimum value of modulation index. Default is 0.1.

    DSS property name: `MMin`, DSS property index: 11.
    """

    def _get_MMax(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 12)

    def _set_MMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    MMax = property(_get_MMax, _set_MMax) # type: BatchFloat64ArrayProxy
    """
    Maximum value of modulation index. Default is 0.9.

    DSS property name: `MMax`, DSS property index: 12.
    """

    def _get_IACMax(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_IACMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    IACMax = property(_get_IACMax, _set_IACMax) # type: BatchFloat64ArrayProxy
    """
    Maximum value of AC line current, per-unit of nominal. Default is 2.

    DSS property name: `IACMax`, DSS property index: 13.
    """

    def _get_IDCMax(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 14)

    def _set_IDCMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    IDCMax = property(_get_IDCMax, _set_IDCMax) # type: BatchFloat64ArrayProxy
    """
    Maximum value of DC current, per-unit of nominal. Default is 2.

    DSS property name: `IDCMax`, DSS property index: 14.
    """

    def _get_VACRef(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 15)

    def _set_VACRef(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    VACRef = property(_get_VACRef, _set_VACRef) # type: BatchFloat64ArrayProxy
    """
    Reference AC line-to-neutral voltage, RMS Volts. Default is 0.
    Applies to PacVac and VdcVac control modes, influencing m.

    DSS property name: `VACRef`, DSS property index: 15.
    """

    def _get_PACRef(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 16)

    def _set_PACRef(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    PACRef = property(_get_PACRef, _set_PACRef) # type: BatchFloat64ArrayProxy
    """
    Reference total AC real power, Watts. Default is 0.
    Applies to PacVac and PacQac control modes, influencing d.

    DSS property name: `PACRef`, DSS property index: 16.
    """

    def _get_QACRef(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 17)

    def _set_QACRef(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    QACRef = property(_get_QACRef, _set_QACRef) # type: BatchFloat64ArrayProxy
    """
    Reference total AC reactive power, Vars. Default is 0.
    Applies to PacQac and VdcQac control modes, influencing m.

    DSS property name: `QACRef`, DSS property index: 17.
    """

    def _get_VDCRef(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 18)

    def _set_VDCRef(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    VDCRef = property(_get_VDCRef, _set_VDCRef) # type: BatchFloat64ArrayProxy
    """
    Reference DC voltage, Volts. Default is 0.
    Applies to VdcVac control mode, influencing d.

    DSS property name: `VDCRef`, DSS property index: 18.
    """

    def _get_VSCMode(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 19)

    def _set_VSCMode(self, value: Union[AnyStr, int, enums.VSConverterControlMode, List[AnyStr], List[int], List[enums.VSConverterControlMode], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(19, value, flags)
            return

        self._set_batch_int32_array(19, value, flags)

    VSCMode = property(_get_VSCMode, _set_VSCMode) # type: BatchInt32ArrayProxy
    """
    Control Mode (Fixed|PacVac|PacQac|VdcVac|VdcQac). Default is Fixed.

    DSS property name: `VSCMode`, DSS property index: 19.
    """

    def _get_VSCMode_str(self) -> List[str]:
        return self._get_batch_str_prop(19)

    def _set_VSCMode_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_VSCMode(value, flags)

    VSCMode_str = property(_get_VSCMode_str, _set_VSCMode_str) # type: List[str]
    """
    Control Mode (Fixed|PacVac|PacQac|VdcVac|VdcQac). Default is Fixed.

    DSS property name: `VSCMode`, DSS property index: 19.
    """

    def _get_Spectrum_str(self) -> List[str]:
        return self._get_batch_str_prop(20)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(20, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]
    """
    Name of harmonic spectrum for this device.

    DSS property name: `Spectrum`, DSS property index: 20.
    """

    def _get_Spectrum(self) -> List[SpectrumObj]:
        return self._get_batch_obj_prop(20)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(20, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]
    """
    Name of harmonic spectrum for this device.

    DSS property name: `Spectrum`, DSS property index: 20.
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 21)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 21.
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(22)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(22, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 22.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 23.
        """
        self._set_batch_string(23, value, flags)

class VSConverterBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kVAC: Union[float, Float64Array]
    kVDC: Union[float, Float64Array]
    kW: Union[float, Float64Array]
    NDC: Union[int, Int32Array]
    RAC: Union[float, Float64Array]
    XAC: Union[float, Float64Array]
    M0: Union[float, Float64Array]
    d0: Union[float, Float64Array]
    MMin: Union[float, Float64Array]
    MMax: Union[float, Float64Array]
    IACMax: Union[float, Float64Array]
    IDCMax: Union[float, Float64Array]
    VACRef: Union[float, Float64Array]
    PACRef: Union[float, Float64Array]
    QACRef: Union[float, Float64Array]
    VDCRef: Union[float, Float64Array]
    VSCMode: Union[AnyStr, int, enums.VSConverterControlMode, List[AnyStr], List[int], List[enums.VSConverterControlMode], Int32Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IVSConverter(IDSSObj, VSConverterBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, VSConverter, VSConverterBatch)
        VSConverterBatch.__init__(self, self._api_util, sync_cls_idx=VSConverter._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> VSConverter:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> VSConverterBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) VSConverter objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[VSConverter]:
            yield from VSConverterBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[VSConverterProperties]) -> VSConverter:
        """
        Creates a new VSConverter.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[VSConverterBatchProperties]) -> VSConverterBatch:
        """
        Creates a new batch of VSConverter objects

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
