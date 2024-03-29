# Copyright (c) 2021-2024 Paulo Meira
# Copyright (c) 2021-2024 DSS-Extensions contributors
from __future__ import annotations
from typing import Union, List, AnyStr, Optional, Iterator, TYPE_CHECKING
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchInt32ArrayProxy

class Spectrum(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'Spectrum'
    _cls_idx = 8
    _cls_int_idx = {
        1,
    }
    _cls_float_idx = {
    }
    _cls_prop_idx = {
        'numharm': 1,
        'harmonic': 2,
        'pctmag': 3,
        '%mag': 3,
        'angle': 4,
        'csvfile': 5,
        'like': 6,
    }


    def edit(self, **kwargs: Unpack[SpectrumProperties]) -> Spectrum:
        """
        Edit this Spectrum.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_NumHarm(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NumHarm(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NumHarm = property(_get_NumHarm, _set_NumHarm) # type: int
    """
    Number of frequencies in this spectrum. (See CSVFile)

    DSS property name: `NumHarm`, DSS property index: 1.
    """

    def _get_Harmonic(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 2)

    def _set_Harmonic(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(2, value, flags)

    Harmonic = property(_get_Harmonic, _set_Harmonic) # type: Float64Array
    """
    Array of harmonic values. You can also use the syntax
    harmonic = (file=filename)     !for text file one value per line
    harmonic = (dblfile=filename)  !for packed file of doubles
    harmonic = (sngfile=filename)  !for packed file of singles 

    DSS property name: `Harmonic`, DSS property index: 2.
    """

    def _get_pctMag(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    def _set_pctMag(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(3, value, flags)

    pctMag = property(_get_pctMag, _set_pctMag) # type: Float64Array
    """
    Array of magnitude values, assumed to be in PERCENT. You can also use the syntax
    %mag = (file=filename)     !for text file one value per line
    %mag = (dblfile=filename)  !for packed file of doubles
    %mag = (sngfile=filename)  !for packed file of singles 

    DSS property name: `%Mag`, DSS property index: 3.
    """

    def _get_Angle(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    def _set_Angle(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(4, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: Float64Array
    """
    Array of phase angle values, degrees.You can also use the syntax
    angle = (file=filename)     !for text file one value per line
    angle = (dblfile=filename)  !for packed file of doubles
    angle = (sngfile=filename)  !for packed file of singles 

    DSS property name: `Angle`, DSS property index: 4.
    """

    def _get_CSVFile(self) -> str:
        return self._get_prop_string(5)

    def _set_CSVFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(5, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: str
    """
    File of spectrum points with (harmonic, magnitude-percent, angle-degrees) values, one set of 3 per line, in CSV format. If fewer than NUMHARM frequencies found in the file, NUMHARM is set to the smaller value.

    DSS property name: `CSVFile`, DSS property index: 5.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 6.
        """
        self._set_string_o(6, value)


class SpectrumProperties(TypedDict):
    NumHarm: int
    Harmonic: Float64Array
    pctMag: Float64Array
    Angle: Float64Array
    CSVFile: AnyStr
    Like: AnyStr

class SpectrumBatch(DSSBatch):
    _cls_name = 'Spectrum'
    _obj_cls = Spectrum
    _cls_idx = 8
    __slots__ = []


    def edit(self, **kwargs: Unpack[SpectrumBatchProperties]) -> SpectrumBatch:
        """
        Edit this Spectrum batch.

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
        def __iter__(self) -> Iterator[Spectrum]:
            yield from DSSBatch.__iter__(self)

    def _get_NumHarm(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_NumHarm(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NumHarm = property(_get_NumHarm, _set_NumHarm) # type: BatchInt32ArrayProxy
    """
    Number of frequencies in this spectrum. (See CSVFile)

    DSS property name: `NumHarm`, DSS property index: 1.
    """

    def _get_Harmonic(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 2)
            for x in self._unpack()
        ]

    def _set_Harmonic(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(2, value, flags)

    Harmonic = property(_get_Harmonic, _set_Harmonic) # type: List[Float64Array]
    """
    Array of harmonic values. You can also use the syntax
    harmonic = (file=filename)     !for text file one value per line
    harmonic = (dblfile=filename)  !for packed file of doubles
    harmonic = (sngfile=filename)  !for packed file of singles 

    DSS property name: `Harmonic`, DSS property index: 2.
    """

    def _get_pctMag(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._unpack()
        ]

    def _set_pctMag(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(3, value, flags)

    pctMag = property(_get_pctMag, _set_pctMag) # type: List[Float64Array]
    """
    Array of magnitude values, assumed to be in PERCENT. You can also use the syntax
    %mag = (file=filename)     !for text file one value per line
    %mag = (dblfile=filename)  !for packed file of doubles
    %mag = (sngfile=filename)  !for packed file of singles 

    DSS property name: `%Mag`, DSS property index: 3.
    """

    def _get_Angle(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._unpack()
        ]

    def _set_Angle(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(4, value, flags)

    Angle = property(_get_Angle, _set_Angle) # type: List[Float64Array]
    """
    Array of phase angle values, degrees.You can also use the syntax
    angle = (file=filename)     !for text file one value per line
    angle = (dblfile=filename)  !for packed file of doubles
    angle = (sngfile=filename)  !for packed file of singles 

    DSS property name: `Angle`, DSS property index: 4.
    """

    def _get_CSVFile(self) -> List[str]:
        return self._get_batch_str_prop(5)

    def _set_CSVFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(5, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: List[str]
    """
    File of spectrum points with (harmonic, magnitude-percent, angle-degrees) values, one set of 3 per line, in CSV format. If fewer than NUMHARM frequencies found in the file, NUMHARM is set to the smaller value.

    DSS property name: `CSVFile`, DSS property index: 5.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 6.
        """
        self._set_batch_string(6, value, flags)

class SpectrumBatchProperties(TypedDict):
    NumHarm: Union[int, Int32Array]
    Harmonic: Float64Array
    pctMag: Float64Array
    Angle: Float64Array
    CSVFile: Union[AnyStr, List[AnyStr]]
    Like: AnyStr

class ISpectrum(IDSSObj, SpectrumBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Spectrum, SpectrumBatch)
        SpectrumBatch.__init__(self, self._api_util, sync_cls_idx=Spectrum._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Spectrum:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> SpectrumBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) Spectrum objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[Spectrum]:
            yield from SpectrumBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[SpectrumProperties]) -> Spectrum:
        """
        Creates a new Spectrum.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[SpectrumBatchProperties]) -> SpectrumBatch:
        """
        Creates a new batch of Spectrum objects

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
