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

class TSData(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'TSData'
    _cls_idx = 11
    _cls_int_idx = {
        10,
        12,
        14,
        18,
    }
    _cls_float_idx = {
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        11,
        13,
        15,
        16,
        17,
        20,
    }
    _cls_prop_idx = {
        'diashield': 1,
        'tapelayer': 2,
        'tapelap': 3,
        'epsr': 4,
        'inslayer': 5,
        'diains': 6,
        'diacable': 7,
        'rdc': 8,
        'rac': 9,
        'runits': 10,
        'gmrac': 11,
        'gmrunits': 12,
        'radius': 13,
        'radunits': 14,
        'normamps': 15,
        'emergamps': 16,
        'diam': 17,
        'seasons': 18,
        'ratings': 19,
        'capradius': 20,
        'like': 21,
    }


    def edit(self, **kwargs: Unpack[TSDataProperties]) -> TSData:
        """
        Edit this TSData.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_DiaShield(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 1)

    def _set_DiaShield(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 1, value, flags)

    DiaShield = property(_get_DiaShield, _set_DiaShield) # type: float
    """
    Diameter over tape shield; same units as radius; no default.

    DSS property name: `DiaShield`, DSS property index: 1.
    """

    def _get_TapeLayer(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_TapeLayer(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    TapeLayer = property(_get_TapeLayer, _set_TapeLayer) # type: float
    """
    Tape shield thickness; same units as radius; no default.

    DSS property name: `TapeLayer`, DSS property index: 2.
    """

    def _get_TapeLap(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_TapeLap(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    TapeLap = property(_get_TapeLap, _set_TapeLap) # type: float
    """
    Tape Lap in percent; default 20.0

    DSS property name: `TapeLap`, DSS property index: 3.
    """

    def _get_EpsR(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_EpsR(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    EpsR = property(_get_EpsR, _set_EpsR) # type: float
    """
    Insulation layer relative permittivity; default is 2.3.

    DSS property name: `EpsR`, DSS property index: 4.
    """

    def _get_InsLayer(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_InsLayer(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    InsLayer = property(_get_InsLayer, _set_InsLayer) # type: float
    """
    Insulation layer thickness; same units as radius; no default. With DiaIns, establishes inner radius for capacitance calculation.

    DSS property name: `InsLayer`, DSS property index: 5.
    """

    def _get_DiaIns(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_DiaIns(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    DiaIns = property(_get_DiaIns, _set_DiaIns) # type: float
    """
    Diameter over insulation layer; same units as radius; no default. Establishes outer radius for capacitance calculation.

    DSS property name: `DiaIns`, DSS property index: 6.
    """

    def _get_DiaCable(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_DiaCable(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    DiaCable = property(_get_DiaCable, _set_DiaCable) # type: float
    """
    Diameter over cable; same units as radius; no default.

    DSS property name: `DiaCable`, DSS property index: 7.
    """

    def _get_RDC(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_RDC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    RDC = property(_get_RDC, _set_RDC) # type: float
    """
    dc Resistance, ohms per unit length (see Runits). Defaults to Rac/1.02 if not specified.

    DSS property name: `RDC`, DSS property index: 8.
    """

    def _get_RAC(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_RAC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    RAC = property(_get_RAC, _set_RAC) # type: float
    """
    Resistance at 60 Hz per unit length. Defaults to 1.02*Rdc if not specified.

    DSS property name: `RAC`, DSS property index: 9.
    """

    def _get_RUnits(self) -> enums.LengthUnit:
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 10))

    def _set_RUnits(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(10, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    RUnits = property(_get_RUnits, _set_RUnits) # type: enums.LengthUnit
    """
    Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `RUnits`, DSS property index: 10.
    """

    def _get_RUnits_str(self) -> str:
        return self._get_prop_string(10)

    def _set_RUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_RUnits(value, flags)

    RUnits_str = property(_get_RUnits_str, _set_RUnits_str) # type: str
    """
    Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `RUnits`, DSS property index: 10.
    """

    def _get_GMRAC(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_GMRAC(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    GMRAC = property(_get_GMRAC, _set_GMRAC) # type: float
    """
    GMR at 60 Hz. Defaults to .7788*radius if not specified.

    DSS property name: `GMRAC`, DSS property index: 11.
    """

    def _get_GMRUnits(self) -> enums.LengthUnit:
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 12))

    def _set_GMRUnits(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(12, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 12, value, flags)

    GMRUnits = property(_get_GMRUnits, _set_GMRUnits) # type: enums.LengthUnit
    """
    Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `GMRUnits`, DSS property index: 12.
    """

    def _get_GMRUnits_str(self) -> str:
        return self._get_prop_string(12)

    def _set_GMRUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_GMRUnits(value, flags)

    GMRUnits_str = property(_get_GMRUnits_str, _set_GMRUnits_str) # type: str
    """
    Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `GMRUnits`, DSS property index: 12.
    """

    def _get_Radius(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_Radius(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    Radius = property(_get_Radius, _set_Radius) # type: float
    """
    Outside radius of conductor. Defaults to GMR/0.7788 if not specified.

    DSS property name: `Radius`, DSS property index: 13.
    """

    def _get_RadUnits(self) -> enums.LengthUnit:
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 14))

    def _set_RadUnits(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(14, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 14, value, flags)

    RadUnits = property(_get_RadUnits, _set_RadUnits) # type: enums.LengthUnit
    """
    Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `RadUnits`, DSS property index: 14.
    """

    def _get_RadUnits_str(self) -> str:
        return self._get_prop_string(14)

    def _set_RadUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_RadUnits(value, flags)

    RadUnits_str = property(_get_RadUnits_str, _set_RadUnits_str) # type: str
    """
    Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `RadUnits`, DSS property index: 14.
    """

    def _get_NormAmps(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float
    """
    Normal ampacity, amperes. Defaults to Emergency amps/1.5 if not specified.

    DSS property name: `NormAmps`, DSS property index: 15.
    """

    def _get_EmergAmps(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float
    """
    Emergency ampacity, amperes. Defaults to 1.5 * Normal Amps if not specified.

    DSS property name: `EmergAmps`, DSS property index: 16.
    """

    def _get_Diam(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_Diam(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    Diam = property(_get_Diam, _set_Diam) # type: float
    """
    Diameter; Alternative method for entering radius.

    DSS property name: `Diam`, DSS property index: 17.
    """

    def _get_Seasons(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 18)

    def _set_Seasons(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 18, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: int
    """
    Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

    DSS property name: `Seasons`, DSS property index: 18.
    """

    def _get_Ratings(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 19)

    def _set_Ratings(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(19, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: Float64Array
    """
    An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
    multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

    DSS property name: `Ratings`, DSS property index: 19.
    """

    def _get_CapRadius(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_CapRadius(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    CapRadius = property(_get_CapRadius, _set_CapRadius) # type: float
    """
    Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius. Define Diam or Radius property first.

    DSS property name: `CapRadius`, DSS property index: 20.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 21.
        """
        self._set_string_o(21, value)


class TSDataProperties(TypedDict):
    DiaShield: float
    TapeLayer: float
    TapeLap: float
    EpsR: float
    InsLayer: float
    DiaIns: float
    DiaCable: float
    RDC: float
    RAC: float
    RUnits: Union[AnyStr, int, enums.LengthUnit]
    GMRAC: float
    GMRUnits: Union[AnyStr, int, enums.LengthUnit]
    Radius: float
    RadUnits: Union[AnyStr, int, enums.LengthUnit]
    NormAmps: float
    EmergAmps: float
    Diam: float
    Seasons: int
    Ratings: Float64Array
    CapRadius: float
    Like: AnyStr

class TSDataBatch(DSSBatch):
    _cls_name = 'TSData'
    _obj_cls = TSData
    _cls_idx = 11
    __slots__ = []


    def edit(self, **kwargs: Unpack[TSDataBatchProperties]) -> TSDataBatch:
        """
        Edit this TSData batch.

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
        def __iter__(self) -> Iterator[TSData]:
            yield from DSSBatch.__iter__(self)

    def _get_DiaShield(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 1)

    def _set_DiaShield(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(1, value, flags)

    DiaShield = property(_get_DiaShield, _set_DiaShield) # type: BatchFloat64ArrayProxy
    """
    Diameter over tape shield; same units as radius; no default.

    DSS property name: `DiaShield`, DSS property index: 1.
    """

    def _get_TapeLayer(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 2)

    def _set_TapeLayer(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    TapeLayer = property(_get_TapeLayer, _set_TapeLayer) # type: BatchFloat64ArrayProxy
    """
    Tape shield thickness; same units as radius; no default.

    DSS property name: `TapeLayer`, DSS property index: 2.
    """

    def _get_TapeLap(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 3)

    def _set_TapeLap(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    TapeLap = property(_get_TapeLap, _set_TapeLap) # type: BatchFloat64ArrayProxy
    """
    Tape Lap in percent; default 20.0

    DSS property name: `TapeLap`, DSS property index: 3.
    """

    def _get_EpsR(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_EpsR(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    EpsR = property(_get_EpsR, _set_EpsR) # type: BatchFloat64ArrayProxy
    """
    Insulation layer relative permittivity; default is 2.3.

    DSS property name: `EpsR`, DSS property index: 4.
    """

    def _get_InsLayer(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_InsLayer(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    InsLayer = property(_get_InsLayer, _set_InsLayer) # type: BatchFloat64ArrayProxy
    """
    Insulation layer thickness; same units as radius; no default. With DiaIns, establishes inner radius for capacitance calculation.

    DSS property name: `InsLayer`, DSS property index: 5.
    """

    def _get_DiaIns(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 6)

    def _set_DiaIns(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    DiaIns = property(_get_DiaIns, _set_DiaIns) # type: BatchFloat64ArrayProxy
    """
    Diameter over insulation layer; same units as radius; no default. Establishes outer radius for capacitance calculation.

    DSS property name: `DiaIns`, DSS property index: 6.
    """

    def _get_DiaCable(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 7)

    def _set_DiaCable(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    DiaCable = property(_get_DiaCable, _set_DiaCable) # type: BatchFloat64ArrayProxy
    """
    Diameter over cable; same units as radius; no default.

    DSS property name: `DiaCable`, DSS property index: 7.
    """

    def _get_RDC(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 8)

    def _set_RDC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    RDC = property(_get_RDC, _set_RDC) # type: BatchFloat64ArrayProxy
    """
    dc Resistance, ohms per unit length (see Runits). Defaults to Rac/1.02 if not specified.

    DSS property name: `RDC`, DSS property index: 8.
    """

    def _get_RAC(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 9)

    def _set_RAC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    RAC = property(_get_RAC, _set_RAC) # type: BatchFloat64ArrayProxy
    """
    Resistance at 60 Hz per unit length. Defaults to 1.02*Rdc if not specified.

    DSS property name: `RAC`, DSS property index: 9.
    """

    def _get_RUnits(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 10)

    def _set_RUnits(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(10, value, flags)
            return

        self._set_batch_int32_array(10, value, flags)

    RUnits = property(_get_RUnits, _set_RUnits) # type: BatchInt32ArrayProxy
    """
    Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `RUnits`, DSS property index: 10.
    """

    def _get_RUnits_str(self) -> List[str]:
        return self._get_batch_str_prop(10)

    def _set_RUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_RUnits(value, flags)

    RUnits_str = property(_get_RUnits_str, _set_RUnits_str) # type: List[str]
    """
    Length units for resistance: ohms per {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `RUnits`, DSS property index: 10.
    """

    def _get_GMRAC(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_GMRAC(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    GMRAC = property(_get_GMRAC, _set_GMRAC) # type: BatchFloat64ArrayProxy
    """
    GMR at 60 Hz. Defaults to .7788*radius if not specified.

    DSS property name: `GMRAC`, DSS property index: 11.
    """

    def _get_GMRUnits(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 12)

    def _set_GMRUnits(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(12, value, flags)
            return

        self._set_batch_int32_array(12, value, flags)

    GMRUnits = property(_get_GMRUnits, _set_GMRUnits) # type: BatchInt32ArrayProxy
    """
    Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `GMRUnits`, DSS property index: 12.
    """

    def _get_GMRUnits_str(self) -> List[str]:
        return self._get_batch_str_prop(12)

    def _set_GMRUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_GMRUnits(value, flags)

    GMRUnits_str = property(_get_GMRUnits_str, _set_GMRUnits_str) # type: List[str]
    """
    Units for GMR: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `GMRUnits`, DSS property index: 12.
    """

    def _get_Radius(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_Radius(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    Radius = property(_get_Radius, _set_Radius) # type: BatchFloat64ArrayProxy
    """
    Outside radius of conductor. Defaults to GMR/0.7788 if not specified.

    DSS property name: `Radius`, DSS property index: 13.
    """

    def _get_RadUnits(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 14)

    def _set_RadUnits(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(14, value, flags)
            return

        self._set_batch_int32_array(14, value, flags)

    RadUnits = property(_get_RadUnits, _set_RadUnits) # type: BatchInt32ArrayProxy
    """
    Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `RadUnits`, DSS property index: 14.
    """

    def _get_RadUnits_str(self) -> List[str]:
        return self._get_batch_str_prop(14)

    def _set_RadUnits_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_RadUnits(value, flags)

    RadUnits_str = property(_get_RadUnits_str, _set_RadUnits_str) # type: List[str]
    """
    Units for outside radius: {mi|kft|km|m|Ft|in|cm|mm} Default=none.

    DSS property name: `RadUnits`, DSS property index: 14.
    """

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 15)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy
    """
    Normal ampacity, amperes. Defaults to Emergency amps/1.5 if not specified.

    DSS property name: `NormAmps`, DSS property index: 15.
    """

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 16)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy
    """
    Emergency ampacity, amperes. Defaults to 1.5 * Normal Amps if not specified.

    DSS property name: `EmergAmps`, DSS property index: 16.
    """

    def _get_Diam(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 17)

    def _set_Diam(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    Diam = property(_get_Diam, _set_Diam) # type: BatchFloat64ArrayProxy
    """
    Diameter; Alternative method for entering radius.

    DSS property name: `Diam`, DSS property index: 17.
    """

    def _get_Seasons(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 18)

    def _set_Seasons(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(18, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: BatchInt32ArrayProxy
    """
    Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

    DSS property name: `Seasons`, DSS property index: 18.
    """

    def _get_Ratings(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 19)
            for x in self._unpack()
        ]

    def _set_Ratings(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(19, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: List[Float64Array]
    """
    An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
    multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

    DSS property name: `Ratings`, DSS property index: 19.
    """

    def _get_CapRadius(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 20)

    def _set_CapRadius(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    CapRadius = property(_get_CapRadius, _set_CapRadius) # type: BatchFloat64ArrayProxy
    """
    Equivalent conductor radius for capacitance calcs. Specify this for bundled conductors. Defaults to same value as radius. Define Diam or Radius property first.

    DSS property name: `CapRadius`, DSS property index: 20.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 21.
        """
        self._set_batch_string(21, value, flags)

class TSDataBatchProperties(TypedDict):
    DiaShield: Union[float, Float64Array]
    TapeLayer: Union[float, Float64Array]
    TapeLap: Union[float, Float64Array]
    EpsR: Union[float, Float64Array]
    InsLayer: Union[float, Float64Array]
    DiaIns: Union[float, Float64Array]
    DiaCable: Union[float, Float64Array]
    RDC: Union[float, Float64Array]
    RAC: Union[float, Float64Array]
    RUnits: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    GMRAC: Union[float, Float64Array]
    GMRUnits: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    Radius: Union[float, Float64Array]
    RadUnits: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    Diam: Union[float, Float64Array]
    Seasons: Union[int, Int32Array]
    Ratings: Float64Array
    CapRadius: Union[float, Float64Array]
    Like: AnyStr

class ITSData(IDSSObj, TSDataBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, TSData, TSDataBatch)
        TSDataBatch.__init__(self, self._api_util, sync_cls_idx=TSData._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> TSData:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> TSDataBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) TSData objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[TSData]:
            yield from TSDataBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[TSDataProperties]) -> TSData:
        """
        Creates a new TSData.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[TSDataBatchProperties]) -> TSDataBatch:
        """
        Creates a new batch of TSData objects

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
