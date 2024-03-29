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

class GICLine(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'GICLine'
    _cls_idx = 44
    _cls_int_idx = {
        6,
        18,
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
        17,
    }
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'volts': 3,
        'angle': 4,
        'frequency': 5,
        'phases': 6,
        'r': 7,
        'x': 8,
        'c': 9,
        'en': 10,
        'ee': 11,
        'lat1': 12,
        'lon1': 13,
        'lat2': 14,
        'lon2': 15,
        'spectrum': 16,
        'basefreq': 17,
        'enabled': 18,
        'like': 19,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[GICLineProperties]) -> GICLine:
        """
        Edit this GICLine.

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
    Name of bus to which the main terminal (1) is connected.
    bus1=busname
    bus1=busname.1.2.3

    DSS property name: `Bus1`, DSS property index: 1.
    """

    def _get_Bus2(self) -> str:
        return self._get_prop_string(2)

    def _set_Bus2(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: str
    """
    Name of bus to which 2nd terminal is connected.
    bus2=busname
    bus2=busname.1.2.3

    No Default; must be specified.

    DSS property name: `Bus2`, DSS property index: 2.
    """

    def _get_Volts(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_Volts(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    Volts = property(_get_Volts, _set_Volts) # type: float
    """
    Voltage magnitude, in volts, of the GIC voltage induced across this line. When specified, voltage source is assumed defined by Voltage and Angle properties. 

    Specify this value

    OR

    EN, EE, lat1, lon1, lat2, lon2. 

    Not both!!  Last one entered will take precedence. Assumed identical in each phase of the Line object.

    DSS property name: `Volts`, DSS property index: 3.
    """

    def _get_Angle(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_Angle(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: float
    """
    Phase angle in degrees of first phase. Default=0.0.  See Voltage property

    DSS property name: `Angle`, DSS property index: 4.
    """

    def _get_Frequency(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_Frequency(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: float
    """
    Source frequency.  Defaults to 0.1 Hz.

    DSS property name: `Frequency`, DSS property index: 5.
    """

    def _get_Phases(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 6)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int
    """
    Number of phases.  Defaults to 3.

    DSS property name: `Phases`, DSS property index: 6.
    """

    def _get_R(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_R(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    R = property(_get_R, _set_R) # type: float
    """
    Resistance of line, ohms of impedance in series with GIC voltage source. 

    DSS property name: `R`, DSS property index: 7.
    """

    def _get_X(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_X(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    X = property(_get_X, _set_X) # type: float
    """
    Reactance at base frequency, ohms. Default = 0.0. This value is generally not important for GIC studies but may be used if desired.

    DSS property name: `X`, DSS property index: 8.
    """

    def _get_C(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_C(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    C = property(_get_C, _set_C) # type: float
    """
    Value of line blocking capacitance in microfarads. Default = 0.0, implying that there is no line blocking capacitor.

    DSS property name: `C`, DSS property index: 9.
    """

    def _get_EN(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_EN(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    EN = property(_get_EN, _set_EN) # type: float
    """
    Northward Electric field (V/km). If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

    DSS property name: `EN`, DSS property index: 10.
    """

    def _get_EE(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_EE(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    EE = property(_get_EE, _set_EE) # type: float
    """
    Eastward Electric field (V/km).  If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

    DSS property name: `EE`, DSS property index: 11.
    """

    def _get_Lat1(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_Lat1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    Lat1 = property(_get_Lat1, _set_Lat1) # type: float
    """
    Latitude of Bus1 (degrees)

    DSS property name: `Lat1`, DSS property index: 12.
    """

    def _get_Lon1(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_Lon1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    Lon1 = property(_get_Lon1, _set_Lon1) # type: float
    """
    Longitude of Bus1 (degrees)

    DSS property name: `Lon1`, DSS property index: 13.
    """

    def _get_Lat2(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_Lat2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    Lat2 = property(_get_Lat2, _set_Lat2) # type: float
    """
    Latitude of Bus2 (degrees)

    DSS property name: `Lat2`, DSS property index: 14.
    """

    def _get_Lon2(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_Lon2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    Lon2 = property(_get_Lon2, _set_Lon2) # type: float
    """
    Longitude of Bus2 (degrees)

    DSS property name: `Lon2`, DSS property index: 15.
    """

    def _get_Spectrum_str(self) -> str:
        return self._get_prop_string(16)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(16, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str
    """
    Inherited Property for all PCElements. Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

    DSS property name: `Spectrum`, DSS property index: 16.
    """

    def _get_Spectrum(self) -> SpectrumObj:
        return self._get_obj(16, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(16, value, flags)
            return

        self._set_string_o(16, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj
    """
    Inherited Property for all PCElements. Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

    DSS property name: `Spectrum`, DSS property index: 16.
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Inherited Property for all PCElements. Base frequency for specification of reactance value.

    DSS property name: `BaseFreq`, DSS property index: 17.
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 18) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 18, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 18.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 19.
        """
        self._set_string_o(19, value)


class GICLineProperties(TypedDict):
    Bus1: AnyStr
    Bus2: AnyStr
    Volts: float
    Angle: float
    Frequency: float
    Phases: int
    R: float
    X: float
    C: float
    EN: float
    EE: float
    Lat1: float
    Lon1: float
    Lat2: float
    Lon2: float
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class GICLineBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'GICLine'
    _obj_cls = GICLine
    _cls_idx = 44
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[GICLineBatchProperties]) -> GICLineBatch:
        """
        Edit this GICLine batch.

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
        def __iter__(self) -> Iterator[GICLine]:
            yield from DSSBatch.__iter__(self)

    def _get_Bus1(self) -> List[str]:
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]
    """
    Name of bus to which the main terminal (1) is connected.
    bus1=busname
    bus1=busname.1.2.3

    DSS property name: `Bus1`, DSS property index: 1.
    """

    def _get_Bus2(self) -> List[str]:
        return self._get_batch_str_prop(2)

    def _set_Bus2(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: List[str]
    """
    Name of bus to which 2nd terminal is connected.
    bus2=busname
    bus2=busname.1.2.3

    No Default; must be specified.

    DSS property name: `Bus2`, DSS property index: 2.
    """

    def _get_Volts(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 3)

    def _set_Volts(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    Volts = property(_get_Volts, _set_Volts) # type: BatchFloat64ArrayProxy
    """
    Voltage magnitude, in volts, of the GIC voltage induced across this line. When specified, voltage source is assumed defined by Voltage and Angle properties. 

    Specify this value

    OR

    EN, EE, lat1, lon1, lat2, lon2. 

    Not both!!  Last one entered will take precedence. Assumed identical in each phase of the Line object.

    DSS property name: `Volts`, DSS property index: 3.
    """

    def _get_Angle(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_Angle(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: BatchFloat64ArrayProxy
    """
    Phase angle in degrees of first phase. Default=0.0.  See Voltage property

    DSS property name: `Angle`, DSS property index: 4.
    """

    def _get_Frequency(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_Frequency(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    Frequency = property(_get_Frequency, _set_Frequency) # type: BatchFloat64ArrayProxy
    """
    Source frequency.  Defaults to 0.1 Hz.

    DSS property name: `Frequency`, DSS property index: 5.
    """

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 6)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(6, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy
    """
    Number of phases.  Defaults to 3.

    DSS property name: `Phases`, DSS property index: 6.
    """

    def _get_R(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 7)

    def _set_R(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    R = property(_get_R, _set_R) # type: BatchFloat64ArrayProxy
    """
    Resistance of line, ohms of impedance in series with GIC voltage source. 

    DSS property name: `R`, DSS property index: 7.
    """

    def _get_X(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 8)

    def _set_X(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    X = property(_get_X, _set_X) # type: BatchFloat64ArrayProxy
    """
    Reactance at base frequency, ohms. Default = 0.0. This value is generally not important for GIC studies but may be used if desired.

    DSS property name: `X`, DSS property index: 8.
    """

    def _get_C(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 9)

    def _set_C(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    C = property(_get_C, _set_C) # type: BatchFloat64ArrayProxy
    """
    Value of line blocking capacitance in microfarads. Default = 0.0, implying that there is no line blocking capacitor.

    DSS property name: `C`, DSS property index: 9.
    """

    def _get_EN(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 10)

    def _set_EN(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    EN = property(_get_EN, _set_EN) # type: BatchFloat64ArrayProxy
    """
    Northward Electric field (V/km). If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

    DSS property name: `EN`, DSS property index: 10.
    """

    def _get_EE(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_EE(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    EE = property(_get_EE, _set_EE) # type: BatchFloat64ArrayProxy
    """
    Eastward Electric field (V/km).  If specified, Voltage and Angle are computed from EN, EE, lat and lon values.

    DSS property name: `EE`, DSS property index: 11.
    """

    def _get_Lat1(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 12)

    def _set_Lat1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    Lat1 = property(_get_Lat1, _set_Lat1) # type: BatchFloat64ArrayProxy
    """
    Latitude of Bus1 (degrees)

    DSS property name: `Lat1`, DSS property index: 12.
    """

    def _get_Lon1(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_Lon1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    Lon1 = property(_get_Lon1, _set_Lon1) # type: BatchFloat64ArrayProxy
    """
    Longitude of Bus1 (degrees)

    DSS property name: `Lon1`, DSS property index: 13.
    """

    def _get_Lat2(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 14)

    def _set_Lat2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    Lat2 = property(_get_Lat2, _set_Lat2) # type: BatchFloat64ArrayProxy
    """
    Latitude of Bus2 (degrees)

    DSS property name: `Lat2`, DSS property index: 14.
    """

    def _get_Lon2(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 15)

    def _set_Lon2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    Lon2 = property(_get_Lon2, _set_Lon2) # type: BatchFloat64ArrayProxy
    """
    Longitude of Bus2 (degrees)

    DSS property name: `Lon2`, DSS property index: 15.
    """

    def _get_Spectrum_str(self) -> List[str]:
        return self._get_batch_str_prop(16)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(16, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]
    """
    Inherited Property for all PCElements. Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

    DSS property name: `Spectrum`, DSS property index: 16.
    """

    def _get_Spectrum(self) -> List[SpectrumObj]:
        return self._get_batch_obj_prop(16)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(16, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]
    """
    Inherited Property for all PCElements. Name of harmonic spectrum for this source.  Default is "defaultvsource", which is defined when the DSS starts.

    DSS property name: `Spectrum`, DSS property index: 16.
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 17)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Inherited Property for all PCElements. Base frequency for specification of reactance value.

    DSS property name: `BaseFreq`, DSS property index: 17.
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(18)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(18, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 18.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 19.
        """
        self._set_batch_string(19, value, flags)

class GICLineBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Bus2: Union[AnyStr, List[AnyStr]]
    Volts: Union[float, Float64Array]
    Angle: Union[float, Float64Array]
    Frequency: Union[float, Float64Array]
    Phases: Union[int, Int32Array]
    R: Union[float, Float64Array]
    X: Union[float, Float64Array]
    C: Union[float, Float64Array]
    EN: Union[float, Float64Array]
    EE: Union[float, Float64Array]
    Lat1: Union[float, Float64Array]
    Lon1: Union[float, Float64Array]
    Lat2: Union[float, Float64Array]
    Lon2: Union[float, Float64Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IGICLine(IDSSObj, GICLineBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, GICLine, GICLineBatch)
        GICLineBatch.__init__(self, self._api_util, sync_cls_idx=GICLine._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> GICLine:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> GICLineBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) GICLine objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[GICLine]:
            yield from GICLineBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[GICLineProperties]) -> GICLine:
        """
        Creates a new GICLine.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[GICLineBatchProperties]) -> GICLineBatch:
        """
        Creates a new batch of GICLine objects

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
