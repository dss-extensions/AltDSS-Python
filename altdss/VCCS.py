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
from .PCElement import PCElementBatchMixin, PCElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .Spectrum import Spectrum as SpectrumObj
from .XYcurve import XYcurve

class VCCS(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'VCCS'
    _cls_idx = 18
    _cls_int_idx = {
        2,
        10,
        16,
    }
    _cls_float_idx = {
        3,
        4,
        5,
        9,
        11,
        12,
        13,
        15,
    }
    _cls_prop_idx = {
        'bus1': 1,
        'phases': 2,
        'prated': 3,
        'vrated': 4,
        'ppct': 5,
        'bp1': 6,
        'bp2': 7,
        'filter': 8,
        'fsample': 9,
        'rmsmode': 10,
        'imaxpu': 11,
        'vrmstau': 12,
        'irmstau': 13,
        'spectrum': 14,
        'basefreq': 15,
        'enabled': 16,
        'like': 17,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[VCCSProperties]) -> VCCS:
        """
        Edit this VCCS.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_Bus1(self) -> str:
        return self._get_prop_string(1)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str
    """
    Name of bus to which source is connected.
    bus1=busname
    bus1=busname.1.2.3

    DSS property name: `Bus1`, DSS property index: 1.
    """

    def _get_Phases(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int
    """
    Number of phases.  Defaults to 1.

    DSS property name: `Phases`, DSS property index: 2.
    """

    def _get_PRated(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_PRated(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    PRated = property(_get_PRated, _set_PRated) # type: float
    """
    Total rated power, in Watts.

    DSS property name: `PRated`, DSS property index: 3.
    """

    def _get_VRated(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_VRated(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    VRated = property(_get_VRated, _set_VRated) # type: float
    """
    Rated line-to-line voltage, in Volts

    DSS property name: `VRated`, DSS property index: 4.
    """

    def _get_Ppct(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_Ppct(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    Ppct = property(_get_Ppct, _set_Ppct) # type: float
    """
    Steady-state operating output, in percent of rated.

    DSS property name: `Ppct`, DSS property index: 5.
    """

    def _get_BP1_str(self) -> str:
        return self._get_prop_string(6)

    def _set_BP1_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(6, value, flags)

    BP1_str = property(_get_BP1_str, _set_BP1_str) # type: str
    """
    XYCurve defining the input piece-wise linear block.

    DSS property name: `BP1`, DSS property index: 6.
    """

    def _get_BP1(self) -> XYcurve:
        return self._get_obj(6, XYcurve)

    def _set_BP1(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(6, value, flags)
            return

        self._set_string_o(6, value, flags)

    BP1 = property(_get_BP1, _set_BP1) # type: XYcurve
    """
    XYCurve defining the input piece-wise linear block.

    DSS property name: `BP1`, DSS property index: 6.
    """

    def _get_BP2_str(self) -> str:
        return self._get_prop_string(7)

    def _set_BP2_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(7, value, flags)

    BP2_str = property(_get_BP2_str, _set_BP2_str) # type: str
    """
    XYCurve defining the output piece-wise linear block.

    DSS property name: `BP2`, DSS property index: 7.
    """

    def _get_BP2(self) -> XYcurve:
        return self._get_obj(7, XYcurve)

    def _set_BP2(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(7, value, flags)
            return

        self._set_string_o(7, value, flags)

    BP2 = property(_get_BP2, _set_BP2) # type: XYcurve
    """
    XYCurve defining the output piece-wise linear block.

    DSS property name: `BP2`, DSS property index: 7.
    """

    def _get_Filter_str(self) -> str:
        return self._get_prop_string(8)

    def _set_Filter_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(8, value, flags)

    Filter_str = property(_get_Filter_str, _set_Filter_str) # type: str
    """
    XYCurve defining the digital filter coefficients (x numerator, y denominator).

    DSS property name: `Filter`, DSS property index: 8.
    """

    def _get_Filter(self) -> XYcurve:
        return self._get_obj(8, XYcurve)

    def _set_Filter(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(8, value, flags)
            return

        self._set_string_o(8, value, flags)

    Filter = property(_get_Filter, _set_Filter) # type: XYcurve
    """
    XYCurve defining the digital filter coefficients (x numerator, y denominator).

    DSS property name: `Filter`, DSS property index: 8.
    """

    def _get_FSample(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_FSample(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    FSample = property(_get_FSample, _set_FSample) # type: float
    """
    Sample frequency [Hz} for the digital filter.

    DSS property name: `FSample`, DSS property index: 9.
    """

    def _get_RMSMode(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    def _set_RMSMode(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    RMSMode = property(_get_RMSMode, _set_RMSMode) # type: bool
    """
    True if only Hz is used to represent a phase-locked loop (PLL), ignoring the BP1, BP2 and time-domain transformations. Default is no.

    DSS property name: `RMSMode`, DSS property index: 10.
    """

    def _get_IMaxpu(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_IMaxpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    IMaxpu = property(_get_IMaxpu, _set_IMaxpu) # type: float
    """
    Maximum output current in per-unit of rated; defaults to 1.1

    DSS property name: `IMaxpu`, DSS property index: 11.
    """

    def _get_VRMSTau(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_VRMSTau(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    VRMSTau = property(_get_VRMSTau, _set_VRMSTau) # type: float
    """
    Time constant in sensing Vrms for the PLL; defaults to 0.0015

    DSS property name: `VRMSTau`, DSS property index: 12.
    """

    def _get_IRMSTau(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_IRMSTau(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    IRMSTau = property(_get_IRMSTau, _set_IRMSTau) # type: float
    """
    Time constant in producing Irms from the PLL; defaults to 0.0015

    DSS property name: `IRMSTau`, DSS property index: 13.
    """

    def _get_Spectrum_str(self) -> str:
        return self._get_prop_string(14)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(14, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str
    """
    Harmonic spectrum assumed for this source.  Default is "default".

    DSS property name: `Spectrum`, DSS property index: 14.
    """

    def _get_Spectrum(self) -> SpectrumObj:
        return self._get_obj(14, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(14, value, flags)
            return

        self._set_string_o(14, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj
    """
    Harmonic spectrum assumed for this source.  Default is "default".

    DSS property name: `Spectrum`, DSS property index: 14.
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 15.
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 16) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 16, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 16.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 17.
        """
        self._set_string_o(17, value)


class VCCSProperties(TypedDict):
    Bus1: AnyStr
    Phases: int
    PRated: float
    VRated: float
    Ppct: float
    BP1: Union[AnyStr, XYcurve]
    BP2: Union[AnyStr, XYcurve]
    Filter: Union[AnyStr, XYcurve]
    FSample: float
    RMSMode: bool
    IMaxpu: float
    VRMSTau: float
    IRMSTau: float
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class VCCSBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'VCCS'
    _obj_cls = VCCS
    _cls_idx = 18
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[VCCSBatchProperties]) -> VCCSBatch:
        """
        Edit this VCCS batch.

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
        def __iter__(self) -> Iterator[VCCS]:
            yield from DSSBatch.__iter__(self)

    def _get_Bus1(self) -> List[str]:
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]
    """
    Name of bus to which source is connected.
    bus1=busname
    bus1=busname.1.2.3

    DSS property name: `Bus1`, DSS property index: 1.
    """

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 2)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy
    """
    Number of phases.  Defaults to 1.

    DSS property name: `Phases`, DSS property index: 2.
    """

    def _get_PRated(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 3)

    def _set_PRated(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    PRated = property(_get_PRated, _set_PRated) # type: BatchFloat64ArrayProxy
    """
    Total rated power, in Watts.

    DSS property name: `PRated`, DSS property index: 3.
    """

    def _get_VRated(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_VRated(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    VRated = property(_get_VRated, _set_VRated) # type: BatchFloat64ArrayProxy
    """
    Rated line-to-line voltage, in Volts

    DSS property name: `VRated`, DSS property index: 4.
    """

    def _get_Ppct(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_Ppct(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    Ppct = property(_get_Ppct, _set_Ppct) # type: BatchFloat64ArrayProxy
    """
    Steady-state operating output, in percent of rated.

    DSS property name: `Ppct`, DSS property index: 5.
    """

    def _get_BP1_str(self) -> List[str]:
        return self._get_batch_str_prop(6)

    def _set_BP1_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(6, value, flags)

    BP1_str = property(_get_BP1_str, _set_BP1_str) # type: List[str]
    """
    XYCurve defining the input piece-wise linear block.

    DSS property name: `BP1`, DSS property index: 6.
    """

    def _get_BP1(self) -> List[XYcurve]:
        return self._get_batch_obj_prop(6)

    def _set_BP1(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(6, value, flags)

    BP1 = property(_get_BP1, _set_BP1) # type: List[XYcurve]
    """
    XYCurve defining the input piece-wise linear block.

    DSS property name: `BP1`, DSS property index: 6.
    """

    def _get_BP2_str(self) -> List[str]:
        return self._get_batch_str_prop(7)

    def _set_BP2_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(7, value, flags)

    BP2_str = property(_get_BP2_str, _set_BP2_str) # type: List[str]
    """
    XYCurve defining the output piece-wise linear block.

    DSS property name: `BP2`, DSS property index: 7.
    """

    def _get_BP2(self) -> List[XYcurve]:
        return self._get_batch_obj_prop(7)

    def _set_BP2(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(7, value, flags)

    BP2 = property(_get_BP2, _set_BP2) # type: List[XYcurve]
    """
    XYCurve defining the output piece-wise linear block.

    DSS property name: `BP2`, DSS property index: 7.
    """

    def _get_Filter_str(self) -> List[str]:
        return self._get_batch_str_prop(8)

    def _set_Filter_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(8, value, flags)

    Filter_str = property(_get_Filter_str, _set_Filter_str) # type: List[str]
    """
    XYCurve defining the digital filter coefficients (x numerator, y denominator).

    DSS property name: `Filter`, DSS property index: 8.
    """

    def _get_Filter(self) -> List[XYcurve]:
        return self._get_batch_obj_prop(8)

    def _set_Filter(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(8, value, flags)

    Filter = property(_get_Filter, _set_Filter) # type: List[XYcurve]
    """
    XYCurve defining the digital filter coefficients (x numerator, y denominator).

    DSS property name: `Filter`, DSS property index: 8.
    """

    def _get_FSample(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 9)

    def _set_FSample(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    FSample = property(_get_FSample, _set_FSample) # type: BatchFloat64ArrayProxy
    """
    Sample frequency [Hz} for the digital filter.

    DSS property name: `FSample`, DSS property index: 9.
    """

    def _get_RMSMode(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(10)
        ]

    def _set_RMSMode(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(10, value, flags)

    RMSMode = property(_get_RMSMode, _set_RMSMode) # type: List[bool]
    """
    True if only Hz is used to represent a phase-locked loop (PLL), ignoring the BP1, BP2 and time-domain transformations. Default is no.

    DSS property name: `RMSMode`, DSS property index: 10.
    """

    def _get_IMaxpu(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_IMaxpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    IMaxpu = property(_get_IMaxpu, _set_IMaxpu) # type: BatchFloat64ArrayProxy
    """
    Maximum output current in per-unit of rated; defaults to 1.1

    DSS property name: `IMaxpu`, DSS property index: 11.
    """

    def _get_VRMSTau(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 12)

    def _set_VRMSTau(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    VRMSTau = property(_get_VRMSTau, _set_VRMSTau) # type: BatchFloat64ArrayProxy
    """
    Time constant in sensing Vrms for the PLL; defaults to 0.0015

    DSS property name: `VRMSTau`, DSS property index: 12.
    """

    def _get_IRMSTau(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_IRMSTau(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    IRMSTau = property(_get_IRMSTau, _set_IRMSTau) # type: BatchFloat64ArrayProxy
    """
    Time constant in producing Irms from the PLL; defaults to 0.0015

    DSS property name: `IRMSTau`, DSS property index: 13.
    """

    def _get_Spectrum_str(self) -> List[str]:
        return self._get_batch_str_prop(14)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(14, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]
    """
    Harmonic spectrum assumed for this source.  Default is "default".

    DSS property name: `Spectrum`, DSS property index: 14.
    """

    def _get_Spectrum(self) -> List[SpectrumObj]:
        return self._get_batch_obj_prop(14)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(14, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]
    """
    Harmonic spectrum assumed for this source.  Default is "default".

    DSS property name: `Spectrum`, DSS property index: 14.
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 15)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 15.
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(16)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(16, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 16.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 17.
        """
        self._set_batch_string(17, value, flags)

class VCCSBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Phases: Union[int, Int32Array]
    PRated: Union[float, Float64Array]
    VRated: Union[float, Float64Array]
    Ppct: Union[float, Float64Array]
    BP1: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    BP2: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    Filter: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    FSample: Union[float, Float64Array]
    RMSMode: bool
    IMaxpu: Union[float, Float64Array]
    VRMSTau: Union[float, Float64Array]
    IRMSTau: Union[float, Float64Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IVCCS(IDSSObj, VCCSBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, VCCS, VCCSBatch)
        VCCSBatch.__init__(self, self._api_util, sync_cls_idx=VCCS._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> VCCS:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> VCCSBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) VCCS objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[VCCS]:
            yield from VCCSBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[VCCSProperties]) -> VCCS:
        """
        Creates a new VCCS.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[VCCSBatchProperties]) -> VCCSBatch:
        """
        Creates a new batch of VCCS objects

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
