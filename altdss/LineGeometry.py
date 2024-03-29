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
from .CNData import CNData
from .LineSpacing import LineSpacing
from .TSData import TSData
from .WireData import WireData

class LineGeometry(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'LineGeometry'
    _cls_idx = 13
    _cls_int_idx = {
        1,
        2,
        3,
        7,
        10,
        17,
        19,
    }
    _cls_float_idx = {
        5,
        6,
        8,
        9,
    }
    _cls_prop_idx = {
        'nconds': 1,
        'nphases': 2,
        'cond': 3,
        'wire': 4,
        'x': 5,
        'h': 6,
        'units': 7,
        'normamps': 8,
        'emergamps': 9,
        'reduce': 10,
        'spacing': 11,
        'wires': 12,
        'conductors': 12,
        'cncable': 13,
        'tscable': 14,
        'cncables': 15,
        'tscables': 16,
        'seasons': 17,
        'ratings': 18,
        'linetype': 19,
        'like': 20,
    }


    def edit(self, **kwargs: Unpack[LineGeometryProperties]) -> LineGeometry:
        """
        Edit this LineGeometry.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_NConds(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NConds(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NConds = property(_get_NConds, _set_NConds) # type: int
    """
    Number of conductors in this geometry. Default is 3. Triggers memory allocations. Define first!

    DSS property name: `NConds`, DSS property index: 1.
    """

    def _get_NPhases(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_NPhases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    NPhases = property(_get_NPhases, _set_NPhases) # type: int
    """
    Number of phases. Default =3; All other conductors are considered neutrals and might be reduced out.

    DSS property name: `NPhases`, DSS property index: 2.
    """

    def _get_Conductors_str(self) -> List[str]:
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 12)

    def _set_Conductors_str(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        self._set_string_array_o(12, value, flags | enums.SetterFlags.AllowAllConductors)

    Conductors_str = property(_get_Conductors_str, _set_Conductors_str) # type: List[str]
    """
    Code from WireData. MUST BE PREVIOUSLY DEFINED. no default.
    Specifies use of Overhead Line parameter calculation,
    Unless Tape Shield cable previously assigned to phases, and this wire is a neutral.

    DSS property name: `Wire`, DSS property index: 4.
    """

    def _get_Conductors(self) -> List[Union[WireData, CNData, TSData]]:
        return self._get_obj_array(12, None)

    def _set_Conductors(self, value: List[Union[AnyStr, Union[WireData, CNData, TSData]]], flags: enums.SetterFlags = 0):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array_o(12, value, flags | enums.SetterFlags.AllowAllConductors)
            return

        self._set_obj_array(12, value, flags | enums.SetterFlags.AllowAllConductors)

    Conductors = property(_get_Conductors, _set_Conductors) # type: List[Union[WireData, CNData, TSData]]
    """
    Code from WireData. MUST BE PREVIOUSLY DEFINED. no default.
    Specifies use of Overhead Line parameter calculation,
    Unless Tape Shield cable previously assigned to phases, and this wire is a neutral.

    DSS property name: `Wire`, DSS property index: 4.
    """

    def _get_X(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 5)

    def _set_X(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(5, value, flags)

    X = property(_get_X, _set_X) # type: Float64Array
    """
    x coordinate.

    DSS property name: `X`, DSS property index: 5.
    """

    def _get_H(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    def _set_H(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(6, value, flags)

    H = property(_get_H, _set_H) # type: Float64Array
    """
    Height of conductor.

    DSS property name: `H`, DSS property index: 6.
    """

    def _get_Units(self) -> enums.LengthUnit:
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 7))

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(7, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 7, value, flags)

    Units = property(_get_Units, _set_Units) # type: enums.LengthUnit
    """
    Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

    DSS property name: `Units`, DSS property index: 7.
    """

    def _get_Units_str(self) -> str:
        return self._get_prop_string(7)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: str
    """
    Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

    DSS property name: `Units`, DSS property index: 7.
    """

    def _get_NormAmps(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float
    """
    Normal ampacity, amperes for the line. Defaults to first conductor if not specified.

    DSS property name: `NormAmps`, DSS property index: 8.
    """

    def _get_EmergAmps(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float
    """
    Emergency ampacity, amperes. Defaults to first conductor if not specified.

    DSS property name: `EmergAmps`, DSS property index: 9.
    """

    def _get_Reduce(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 10) != 0

    def _set_Reduce(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    Reduce = property(_get_Reduce, _set_Reduce) # type: bool
    """
    {Yes | No} Default = no. Reduce to Nphases (Kron Reduction). Reduce out neutrals.

    DSS property name: `Reduce`, DSS property index: 10.
    """

    def _get_Spacing_str(self) -> str:
        return self._get_prop_string(11)

    def _set_Spacing_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(11, value, flags)

    Spacing_str = property(_get_Spacing_str, _set_Spacing_str) # type: str
    """
    Reference to a LineSpacing for use in a line constants calculation.
    Alternative to x, h, and units. MUST BE PREVIOUSLY DEFINED.
    Must match "nconds" as previously defined for this geometry.
    Must be used in conjunction with the Wires property.

    DSS property name: `Spacing`, DSS property index: 11.
    """

    def _get_Spacing(self) -> LineSpacing:
        return self._get_obj(11, LineSpacing)

    def _set_Spacing(self, value: Union[AnyStr, LineSpacing], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(11, value, flags)
            return

        self._set_string_o(11, value, flags)

    Spacing = property(_get_Spacing, _set_Spacing) # type: LineSpacing
    """
    Reference to a LineSpacing for use in a line constants calculation.
    Alternative to x, h, and units. MUST BE PREVIOUSLY DEFINED.
    Must match "nconds" as previously defined for this geometry.
    Must be used in conjunction with the Wires property.

    DSS property name: `Spacing`, DSS property index: 11.
    """

    def _get_Seasons(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 17)

    def _set_Seasons(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 17, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: int
    """
    Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property. Defaults to first conductor if not specified.

    DSS property name: `Seasons`, DSS property index: 17.
    """

    def _get_Ratings(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 18)

    def _set_Ratings(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(18, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: Float64Array
    """
    An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
    multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.Defaults to first conductor if not specified.

    DSS property name: `Ratings`, DSS property index: 18.
    """

    def _get_LineType(self) -> enums.LineType:
        return enums.LineType(self._lib.Obj_GetInt32(self._ptr, 19))

    def _set_LineType(self, value: Union[AnyStr, int, enums.LineType], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(19, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 19, value, flags)

    LineType = property(_get_LineType, _set_LineType) # type: enums.LineType
    """
    Code designating the type of line. 
    One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

    OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

    DSS property name: `LineType`, DSS property index: 19.
    """

    def _get_LineType_str(self) -> str:
        return self._get_prop_string(19)

    def _set_LineType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LineType(value, flags)

    LineType_str = property(_get_LineType_str, _set_LineType_str) # type: str
    """
    Code designating the type of line. 
    One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

    OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

    DSS property name: `LineType`, DSS property index: 19.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 20.
        """
        self._set_string_o(20, value)


class LineGeometryProperties(TypedDict):
    NConds: int
    NPhases: int
    Conductors: List[Union[AnyStr, Union[WireData, CNData, TSData]]]
    X: Float64Array
    H: Float64Array
    Units: Union[AnyStr, int, enums.LengthUnit]
    NormAmps: float
    EmergAmps: float
    Reduce: bool
    Spacing: Union[AnyStr, LineSpacing]
    Seasons: int
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType]
    Like: AnyStr

class LineGeometryBatch(DSSBatch):
    _cls_name = 'LineGeometry'
    _obj_cls = LineGeometry
    _cls_idx = 13
    __slots__ = []


    def edit(self, **kwargs: Unpack[LineGeometryBatchProperties]) -> LineGeometryBatch:
        """
        Edit this LineGeometry batch.

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
        def __iter__(self) -> Iterator[LineGeometry]:
            yield from DSSBatch.__iter__(self)

    def _get_NConds(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_NConds(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NConds = property(_get_NConds, _set_NConds) # type: BatchInt32ArrayProxy
    """
    Number of conductors in this geometry. Default is 3. Triggers memory allocations. Define first!

    DSS property name: `NConds`, DSS property index: 1.
    """

    def _get_NPhases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 2)

    def _set_NPhases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    NPhases = property(_get_NPhases, _set_NPhases) # type: BatchInt32ArrayProxy
    """
    Number of phases. Default =3; All other conductors are considered neutrals and might be reduced out.

    DSS property name: `NPhases`, DSS property index: 2.
    """

    def _get_Conductors_str(self) -> List[List[str]]:
        return self._get_string_ll(12)

    def _set_Conductors_str(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        self._set_batch_stringlist_prop(12, value, flags | enums.SetterFlags.AllowAllConductors)

    Conductors_str = property(_get_Conductors_str, _set_Conductors_str) # type: List[List[str]]
    """
    Code from WireData. MUST BE PREVIOUSLY DEFINED. no default.
    Specifies use of Overhead Line parameter calculation,
    Unless Tape Shield cable previously assigned to phases, and this wire is a neutral.

    DSS property name: `Wire`, DSS property index: 4.
    """

    def _get_Conductors(self) -> List[List[Union[WireData, CNData, TSData]]]:
        return self._get_obj_ll(12, None)

    def _set_Conductors(self, value: Union[List[AnyStr], List[Union[WireData, CNData, TSData]]], flags: enums.SetterFlags = 0):
        if (not len(value)) or isinstance(value[0], (bytes, str)) or (len(value[0]) and isinstance(value[0][0], (bytes, str))):
            self._set_batch_stringlist_prop(12, value, flags | enums.SetterFlags.AllowAllConductors)
            return

        self._set_batch_objlist_prop(12, value, flags | enums.SetterFlags.AllowAllConductors)

    Conductors = property(_get_Conductors, _set_Conductors) # type: List[List[Union[WireData, CNData, TSData]]]
    """
    Code from WireData. MUST BE PREVIOUSLY DEFINED. no default.
    Specifies use of Overhead Line parameter calculation,
    Unless Tape Shield cable previously assigned to phases, and this wire is a neutral.

    DSS property name: `Wire`, DSS property index: 4.
    """

    def _get_X(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 5)
            for x in self._unpack()
        ]

    def _set_X(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(5, value, flags)

    X = property(_get_X, _set_X) # type: List[Float64Array]
    """
    x coordinate.

    DSS property name: `X`, DSS property index: 5.
    """

    def _get_H(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._unpack()
        ]

    def _set_H(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(6, value, flags)

    H = property(_get_H, _set_H) # type: List[Float64Array]
    """
    Height of conductor.

    DSS property name: `H`, DSS property index: 6.
    """

    def _get_Units(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 7)

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(7, value, flags)
            return

        self._set_batch_int32_array(7, value, flags)

    Units = property(_get_Units, _set_Units) # type: BatchInt32ArrayProxy
    """
    Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

    DSS property name: `Units`, DSS property index: 7.
    """

    def _get_Units_str(self) -> List[str]:
        return self._get_batch_str_prop(7)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: List[str]
    """
    Units for x and h: {mi|kft|km|m|Ft|in|cm } Initial default is "ft", but defaults to last unit defined

    DSS property name: `Units`, DSS property index: 7.
    """

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 8)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy
    """
    Normal ampacity, amperes for the line. Defaults to first conductor if not specified.

    DSS property name: `NormAmps`, DSS property index: 8.
    """

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 9)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy
    """
    Emergency ampacity, amperes. Defaults to first conductor if not specified.

    DSS property name: `EmergAmps`, DSS property index: 9.
    """

    def _get_Reduce(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(10)
        ]

    def _set_Reduce(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(10, value, flags)

    Reduce = property(_get_Reduce, _set_Reduce) # type: List[bool]
    """
    {Yes | No} Default = no. Reduce to Nphases (Kron Reduction). Reduce out neutrals.

    DSS property name: `Reduce`, DSS property index: 10.
    """

    def _get_Spacing_str(self) -> List[str]:
        return self._get_batch_str_prop(11)

    def _set_Spacing_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(11, value, flags)

    Spacing_str = property(_get_Spacing_str, _set_Spacing_str) # type: List[str]
    """
    Reference to a LineSpacing for use in a line constants calculation.
    Alternative to x, h, and units. MUST BE PREVIOUSLY DEFINED.
    Must match "nconds" as previously defined for this geometry.
    Must be used in conjunction with the Wires property.

    DSS property name: `Spacing`, DSS property index: 11.
    """

    def _get_Spacing(self) -> List[LineSpacing]:
        return self._get_batch_obj_prop(11)

    def _set_Spacing(self, value: Union[AnyStr, LineSpacing, List[AnyStr], List[LineSpacing]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(11, value, flags)

    Spacing = property(_get_Spacing, _set_Spacing) # type: List[LineSpacing]
    """
    Reference to a LineSpacing for use in a line constants calculation.
    Alternative to x, h, and units. MUST BE PREVIOUSLY DEFINED.
    Must match "nconds" as previously defined for this geometry.
    Must be used in conjunction with the Wires property.

    DSS property name: `Spacing`, DSS property index: 11.
    """

    def _get_Seasons(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 17)

    def _set_Seasons(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(17, value, flags)

    Seasons = property(_get_Seasons, _set_Seasons) # type: BatchInt32ArrayProxy
    """
    Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property. Defaults to first conductor if not specified.

    DSS property name: `Seasons`, DSS property index: 17.
    """

    def _get_Ratings(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 18)
            for x in self._unpack()
        ]

    def _set_Ratings(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(18, value, flags)

    Ratings = property(_get_Ratings, _set_Ratings) # type: List[Float64Array]
    """
    An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
    multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.Defaults to first conductor if not specified.

    DSS property name: `Ratings`, DSS property index: 18.
    """

    def _get_LineType(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 19)

    def _set_LineType(self, value: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(19, value, flags)
            return

        self._set_batch_int32_array(19, value, flags)

    LineType = property(_get_LineType, _set_LineType) # type: BatchInt32ArrayProxy
    """
    Code designating the type of line. 
    One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

    OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

    DSS property name: `LineType`, DSS property index: 19.
    """

    def _get_LineType_str(self) -> List[str]:
        return self._get_batch_str_prop(19)

    def _set_LineType_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_LineType(value, flags)

    LineType_str = property(_get_LineType_str, _set_LineType_str) # type: List[str]
    """
    Code designating the type of line. 
    One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

    OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

    DSS property name: `LineType`, DSS property index: 19.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 20.
        """
        self._set_batch_string(20, value, flags)

class LineGeometryBatchProperties(TypedDict):
    NConds: Union[int, Int32Array]
    NPhases: Union[int, Int32Array]
    Conductors: Union[List[AnyStr], List[Union[WireData, CNData, TSData]]]
    X: Float64Array
    H: Float64Array
    Units: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    Reduce: bool
    Spacing: Union[AnyStr, LineSpacing, List[AnyStr], List[LineSpacing]]
    Seasons: Union[int, Int32Array]
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array]
    Like: AnyStr

class ILineGeometry(IDSSObj, LineGeometryBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, LineGeometry, LineGeometryBatch)
        LineGeometryBatch.__init__(self, self._api_util, sync_cls_idx=LineGeometry._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> LineGeometry:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> LineGeometryBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) LineGeometry objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[LineGeometry]:
            yield from LineGeometryBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[LineGeometryProperties]) -> LineGeometry:
        """
        Creates a new LineGeometry.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[LineGeometryBatchProperties]) -> LineGeometryBatch:
        """
        Creates a new batch of LineGeometry objects

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
