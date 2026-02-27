# Copyright (c) 2021-2026 Paulo Meira
# Copyright (c) 2021-2026 DSS-Extensions contributors
from __future__ import annotations
from typing import Union, List, AnyStr, Optional, Iterator, TYPE_CHECKING
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy
from .common import LIST_LIKE

class LineSpacing(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'LineSpacing'
    _cls_idx = 12
    _cls_int_idx = {
        1,
        2,
        5,
        6,
    }
    _cls_float_idx = {
        7,
        8,
        9,
        10,
    }
    _cls_prop_idx = {
        'nconds': 1,
        'nphases': 2,
        'x': 3,
        'h': 4,
        'units': 5,
        'detailed': 6,
        'eqdistphph': 7,
        'eqdistphn': 8,
        'avgphaseheight': 9,
        'avgneutralheight': 10,
        'like': 11,
    }


    def edit(self, **kwargs: Unpack[LineSpacingProperties]) -> LineSpacing:
        """
        Edit this LineSpacing.

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
    Number of wires in this geometry. Triggers memory allocations. Define first!

    Name: `NConds`
    """

    def _get_NPhases(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_NPhases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    NPhases = property(_get_NPhases, _set_NPhases) # type: int
    """
    Number of retained phase conductors. If less than the number of wires, list the retained phase coordinates first.

    Name: `NPhases`
    Default: 3
    """

    def _get_X(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    def _set_X(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(3, value, flags)

    X = property(_get_X, _set_X) # type: Float64Array
    """
    Array of wire X coordinates.

    Name: `X`
    Default: [0.0, 0.0, 0.0]
    """

    def _get_H(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    def _set_H(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(4, value, flags)

    H = property(_get_H, _set_H) # type: Float64Array
    """
    Array of wire Heights.

    Name: `H`
    Default: [0.0, 0.0, 0.0]
    """

    def _get_Units(self) -> enums.LengthUnit:
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 5))

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(5, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    Units = property(_get_Units, _set_Units) # type: enums.LengthUnit
    """
    Units for x and h. Initial default is "ft", but defaults to last unit defined

    Name: `Units`
    Default: ft
    """

    def _get_Units_str(self) -> str:
        return self._get_prop_string(5)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: str
    """
    Units for x and h. Initial default is "ft", but defaults to last unit defined

    Name: `Units`
    Default: ft
    """

    def _get_Detailed(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 6) != 0

    def _set_Detailed(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Detailed = property(_get_Detailed, _set_Detailed) # type: bool
    """
    Determines whether the spacing uses a detailed cross-section coordinates with x and h arrays (Yes/True), or uses equivalent spacing fields (No/False). The equivalent spacing fields are `EqDistPhPh`, `EqDistPhN`, `AvgPhaseHeight` and `AvgNeutralHeight`.

    Name: `Detailed`
    Default: True
    """

    def _get_EqDistPhPh(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_EqDistPhPh(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    EqDistPhPh = property(_get_EqDistPhPh, _set_EqDistPhPh) # type: float
    """
    Equivalent distance between phase conductors. Used for equivalent distance modeling (`Detailed=yes`) as opposed to detailed cross-section coordinates.

    Name: `EqDistPhPh`
    Default: 0.0
    """

    def _get_EqDistPhN(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_EqDistPhN(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    EqDistPhN = property(_get_EqDistPhN, _set_EqDistPhN) # type: float
    """
    Equivalent distance between phase and neutral conductors. Used for equivalent distance modeling (`Detailed=yes`) as opposed to detailed cross-section coordinates.

    Name: `EqDistPhN`
    Default: 0.0
    """

    def _get_AvgPhaseHeight(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_AvgPhaseHeight(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    AvgPhaseHeight = property(_get_AvgPhaseHeight, _set_AvgPhaseHeight) # type: float
    """
    Average height of phase conductors. Used for equivalent distance modeling (`Detailed=yes`) as opposed to detailed cross-section coordinates.

    Name: `AvgPhaseHeight`
    Default: 0.0
    """

    def _get_AvgNeutralHeight(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_AvgNeutralHeight(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    AvgNeutralHeight = property(_get_AvgNeutralHeight, _set_AvgNeutralHeight) # type: float
    """
    Average height of neutral conductors. Used for equivalent distance modeling (`Detailed=yes`) as opposed to detailed cross-section coordinates.

    Name: `AvgNeutralHeight`
    Default: 0.0
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        **Deprecated:** `Like` has been deprecated since at least 2021, see https://sourceforge.net/p/electricdss/discussion/861977/thread/8b59d21eb6/#b57c/f668

        Name: `Like`
        """
        self._set_string_o(11, value)


class LineSpacingProperties(TypedDict):
    NConds: int
    NPhases: int
    X: Float64Array
    H: Float64Array
    Units: Union[AnyStr, int, enums.LengthUnit]
    Detailed: bool
    EqDistPhPh: float
    EqDistPhN: float
    AvgPhaseHeight: float
    AvgNeutralHeight: float
    Like: AnyStr

class LineSpacingBatch(DSSBatch):
    _cls_name = 'LineSpacing'
    _obj_cls = LineSpacing
    _cls_idx = 12
    __slots__ = []


    def edit(self, **kwargs: Unpack[LineSpacingBatchProperties]) -> LineSpacingBatch:
        """
        Edit this LineSpacing batch.

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
        def __iter__(self) -> Iterator[LineSpacing]:
            yield from DSSBatch.__iter__(self)

    def _get_NConds(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_NConds(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NConds = property(_get_NConds, _set_NConds) # type: BatchInt32ArrayProxy
    """
    Number of wires in this geometry. Triggers memory allocations. Define first!

    Name: `NConds`
    """

    def _get_NPhases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 2)

    def _set_NPhases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    NPhases = property(_get_NPhases, _set_NPhases) # type: BatchInt32ArrayProxy
    """
    Number of retained phase conductors. If less than the number of wires, list the retained phase coordinates first.

    Name: `NPhases`
    Default: 3
    """

    def _get_X(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._unpack()
        ]

    def _set_X(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(3, value, flags)

    X = property(_get_X, _set_X) # type: List[Float64Array]
    """
    Array of wire X coordinates.

    Name: `X`
    Default: [0.0, 0.0, 0.0]
    """

    def _get_H(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._unpack()
        ]

    def _set_H(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(4, value, flags)

    H = property(_get_H, _set_H) # type: List[Float64Array]
    """
    Array of wire Heights.

    Name: `H`
    Default: [0.0, 0.0, 0.0]
    """

    def _get_Units(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 5)

    def _set_Units(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(5, value, flags)
            return

        self._set_batch_int32_array(5, value, flags)

    Units = property(_get_Units, _set_Units) # type: BatchInt32ArrayProxy
    """
    Units for x and h. Initial default is "ft", but defaults to last unit defined

    Name: `Units`
    Default: ft
    """

    def _get_Units_str(self) -> List[str]:
        return self._get_batch_str_prop(5)

    def _set_Units_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Units(value, flags)

    Units_str = property(_get_Units_str, _set_Units_str) # type: List[str]
    """
    Units for x and h. Initial default is "ft", but defaults to last unit defined

    Name: `Units`
    Default: ft
    """

    def _get_Detailed(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(6)
        ]

    def _set_Detailed(self, value: Union[bool, List[bool]], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(6, value, flags)

    Detailed = property(_get_Detailed, _set_Detailed) # type: List[bool]
    """
    Determines whether the spacing uses a detailed cross-section coordinates with x and h arrays (Yes/True), or uses equivalent spacing fields (No/False). The equivalent spacing fields are `EqDistPhPh`, `EqDistPhN`, `AvgPhaseHeight` and `AvgNeutralHeight`.

    Name: `Detailed`
    Default: True
    """

    def _get_EqDistPhPh(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 7)

    def _set_EqDistPhPh(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    EqDistPhPh = property(_get_EqDistPhPh, _set_EqDistPhPh) # type: BatchFloat64ArrayProxy
    """
    Equivalent distance between phase conductors. Used for equivalent distance modeling (`Detailed=yes`) as opposed to detailed cross-section coordinates.

    Name: `EqDistPhPh`
    Default: 0.0
    """

    def _get_EqDistPhN(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 8)

    def _set_EqDistPhN(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    EqDistPhN = property(_get_EqDistPhN, _set_EqDistPhN) # type: BatchFloat64ArrayProxy
    """
    Equivalent distance between phase and neutral conductors. Used for equivalent distance modeling (`Detailed=yes`) as opposed to detailed cross-section coordinates.

    Name: `EqDistPhN`
    Default: 0.0
    """

    def _get_AvgPhaseHeight(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 9)

    def _set_AvgPhaseHeight(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    AvgPhaseHeight = property(_get_AvgPhaseHeight, _set_AvgPhaseHeight) # type: BatchFloat64ArrayProxy
    """
    Average height of phase conductors. Used for equivalent distance modeling (`Detailed=yes`) as opposed to detailed cross-section coordinates.

    Name: `AvgPhaseHeight`
    Default: 0.0
    """

    def _get_AvgNeutralHeight(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 10)

    def _set_AvgNeutralHeight(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    AvgNeutralHeight = property(_get_AvgNeutralHeight, _set_AvgNeutralHeight) # type: BatchFloat64ArrayProxy
    """
    Average height of neutral conductors. Used for equivalent distance modeling (`Detailed=yes`) as opposed to detailed cross-section coordinates.

    Name: `AvgNeutralHeight`
    Default: 0.0
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        **Deprecated:** `Like` has been deprecated since at least 2021, see https://sourceforge.net/p/electricdss/discussion/861977/thread/8b59d21eb6/#b57c/f668

        Name: `Like`
        """
        self._set_batch_string(11, value, flags)

class LineSpacingBatchProperties(TypedDict):
    NConds: Union[int, Int32Array]
    NPhases: Union[int, Int32Array]
    X: Float64Array
    H: Float64Array
    Units: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    Detailed: bool
    EqDistPhPh: Union[float, Float64Array]
    EqDistPhN: Union[float, Float64Array]
    AvgPhaseHeight: Union[float, Float64Array]
    AvgNeutralHeight: Union[float, Float64Array]
    Like: AnyStr

class ILineSpacing(IDSSObj, LineSpacingBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, LineSpacing, LineSpacingBatch)
        LineSpacingBatch.__init__(self, self._api_util, sync_cls_idx=LineSpacing._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> LineSpacing:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> LineSpacingBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) LineSpacing objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[LineSpacing]:
            yield from LineSpacingBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[LineSpacingProperties]) -> LineSpacing:
        """
        Creates a new LineSpacing.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[LineSpacingBatchProperties]) -> LineSpacingBatch:
        """
        Creates a new batch of LineSpacing objects

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
