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

class PriceShape(DSSObj):
    __slots__ = DSSObj._extra_slots
    _cls_name = 'PriceShape'
    _cls_idx = 4
    _cls_int_idx = {
        1,
    }
    _cls_float_idx = {
        2,
        5,
        6,
        10,
        11,
    }
    _cls_prop_idx = {
        'npts': 1,
        'interval': 2,
        'price': 3,
        'hour': 4,
        'mean': 5,
        'stddev': 6,
        'csvfile': 7,
        'sngfile': 8,
        'dblfile': 9,
        'sinterval': 10,
        'minterval': 11,
        'action': 12,
        'like': 13,
    }


    def edit(self, **kwargs: Unpack[PriceShapeProperties]) -> PriceShape:
        """
        Edit this PriceShape.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_NPts(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_NPts(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    NPts = property(_get_NPts, _set_NPts) # type: int
    """
    Max number of points to expect in price shape vectors. This gets reset to the number of Price values found if less than specified.

    DSS property name: `NPts`, DSS property index: 1.
    """

    def _get_Interval(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_Interval(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    Interval = property(_get_Interval, _set_Interval) # type: float
    """
    Time interval for fixed interval data, hrs. Default = 1. If Interval = 0 then time data (in hours) may be at irregular intervals and time value must be specified using either the Hour property or input files. Then values are interpolated when Interval=0, but not for fixed interval data.  

    See also "sinterval" and "minterval".

    DSS property name: `Interval`, DSS property index: 2.
    """

    def _get_Price(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 3)

    def _set_Price(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(3, value, flags)

    Price = property(_get_Price, _set_Price) # type: Float64Array
    """
    Array of Price values.  Units should be compatible with the object using the data. You can also use the syntax: 
    Price = (file=filename)     !for text file one value per line
    Price = (dblfile=filename)  !for packed file of doubles
    Price = (sngfile=filename)  !for packed file of singles 

    Note: this property will reset Npts if the  number of values in the files are fewer.

    DSS property name: `Price`, DSS property index: 3.
    """

    def _get_Hour(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    def _set_Hour(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(4, value, flags)

    Hour = property(_get_Hour, _set_Hour) # type: Float64Array
    """
    Array of hour values. Only necessary to define this property for variable interval data. If the data are fixed interval, do not use this property. You can also use the syntax: 
    hour = (file=filename)     !for text file one value per line
    hour = (dblfile=filename)  !for packed file of doubles
    hour = (sngfile=filename)  !for packed file of singles 

    DSS property name: `Hour`, DSS property index: 4.
    """

    def _get_Mean(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_Mean(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    Mean = property(_get_Mean, _set_Mean) # type: float
    """
    Mean of the Price curve values.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently. Used for Monte Carlo load simulations.

    DSS property name: `Mean`, DSS property index: 5.
    """

    def _get_StdDev(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_StdDev(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    StdDev = property(_get_StdDev, _set_StdDev) # type: float
    """
    Standard deviation of the Prices.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently.Is overwritten if you subsequently read in a curve

    Used for Monte Carlo load simulations.

    DSS property name: `StdDev`, DSS property index: 6.
    """

    def _get_CSVFile(self) -> str:
        return self._get_prop_string(7)

    def _set_CSVFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(7, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: str
    """
    Switch input of  Price curve data to a csv file containing (hour, Price) points, or simply (Price) values for fixed time interval data, one per line. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `CSVFile`, DSS property index: 7.
    """

    def _get_SngFile(self) -> str:
        return self._get_prop_string(8)

    def _set_SngFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(8, value, flags)

    SngFile = property(_get_SngFile, _set_SngFile) # type: str
    """
    Switch input of  Price curve data to a binary file of singles containing (hour, Price) points, or simply (Price) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `SngFile`, DSS property index: 8.
    """

    def _get_DblFile(self) -> str:
        return self._get_prop_string(9)

    def _set_DblFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    DblFile = property(_get_DblFile, _set_DblFile) # type: str
    """
    Switch input of  Price curve data to a binary file of doubles containing (hour, Price) points, or simply (Price) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `DblFile`, DSS property index: 9.
    """

    def _get_SInterval(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_SInterval(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    SInterval = property(_get_SInterval, _set_SInterval) # type: float
    """
    Specify fixed interval in SECONDS. Alternate way to specify Interval property.

    DSS property name: `SInterval`, DSS property index: 10.
    """

    def _get_MInterval(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_MInterval(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    MInterval = property(_get_MInterval, _set_MInterval) # type: float
    """
    Specify fixed interval in MINUTES. Alternate way to specify Interval property.

    DSS property name: `MInterval`, DSS property index: 11.
    """

    def Action(self, value: Union[AnyStr, int, enums.PriceShapeAction], flags: enums.SetterFlags = 0):
        """
        {DblSave | SngSave} After defining Price curve data... Setting action=DblSave or SngSave will cause the present "Price" values to be written to either a packed file of double or single. The filename is the PriceShape name. 

        DSS property name: `Action`, DSS property index: 12.
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 12, value, flags)
            return

        self._set_string_o(12, value)

    def DblSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(PriceShapeAction.DblSave)'''
        self._lib.Obj_SetInt32(self._ptr, 12, enums.PriceShapeAction.DblSave, flags)

    def SngSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(PriceShapeAction.SngSave)'''
        self._lib.Obj_SetInt32(self._ptr, 12, enums.PriceShapeAction.SngSave, flags)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_string_o(13, value)


class PriceShapeProperties(TypedDict):
    NPts: int
    Interval: float
    Price: Float64Array
    Hour: Float64Array
    Mean: float
    StdDev: float
    CSVFile: AnyStr
    SngFile: AnyStr
    DblFile: AnyStr
    SInterval: float
    MInterval: float
    Action: Union[AnyStr, int, enums.PriceShapeAction]
    Like: AnyStr

class PriceShapeBatch(DSSBatch):
    _cls_name = 'PriceShape'
    _obj_cls = PriceShape
    _cls_idx = 4
    __slots__ = []


    def edit(self, **kwargs: Unpack[PriceShapeBatchProperties]) -> PriceShapeBatch:
        """
        Edit this PriceShape batch.

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
        def __iter__(self) -> Iterator[PriceShape]:
            yield from DSSBatch.__iter__(self)

    def _get_NPts(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_NPts(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NPts = property(_get_NPts, _set_NPts) # type: BatchInt32ArrayProxy
    """
    Max number of points to expect in price shape vectors. This gets reset to the number of Price values found if less than specified.

    DSS property name: `NPts`, DSS property index: 1.
    """

    def _get_Interval(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 2)

    def _set_Interval(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    Interval = property(_get_Interval, _set_Interval) # type: BatchFloat64ArrayProxy
    """
    Time interval for fixed interval data, hrs. Default = 1. If Interval = 0 then time data (in hours) may be at irregular intervals and time value must be specified using either the Hour property or input files. Then values are interpolated when Interval=0, but not for fixed interval data.  

    See also "sinterval" and "minterval".

    DSS property name: `Interval`, DSS property index: 2.
    """

    def _get_Price(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 3)
            for x in self._unpack()
        ]

    def _set_Price(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(3, value, flags)

    Price = property(_get_Price, _set_Price) # type: List[Float64Array]
    """
    Array of Price values.  Units should be compatible with the object using the data. You can also use the syntax: 
    Price = (file=filename)     !for text file one value per line
    Price = (dblfile=filename)  !for packed file of doubles
    Price = (sngfile=filename)  !for packed file of singles 

    Note: this property will reset Npts if the  number of values in the files are fewer.

    DSS property name: `Price`, DSS property index: 3.
    """

    def _get_Hour(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 4)
            for x in self._unpack()
        ]

    def _set_Hour(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(4, value, flags)

    Hour = property(_get_Hour, _set_Hour) # type: List[Float64Array]
    """
    Array of hour values. Only necessary to define this property for variable interval data. If the data are fixed interval, do not use this property. You can also use the syntax: 
    hour = (file=filename)     !for text file one value per line
    hour = (dblfile=filename)  !for packed file of doubles
    hour = (sngfile=filename)  !for packed file of singles 

    DSS property name: `Hour`, DSS property index: 4.
    """

    def _get_Mean(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_Mean(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    Mean = property(_get_Mean, _set_Mean) # type: BatchFloat64ArrayProxy
    """
    Mean of the Price curve values.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently. Used for Monte Carlo load simulations.

    DSS property name: `Mean`, DSS property index: 5.
    """

    def _get_StdDev(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 6)

    def _set_StdDev(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    StdDev = property(_get_StdDev, _set_StdDev) # type: BatchFloat64ArrayProxy
    """
    Standard deviation of the Prices.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently.Is overwritten if you subsequently read in a curve

    Used for Monte Carlo load simulations.

    DSS property name: `StdDev`, DSS property index: 6.
    """

    def _get_CSVFile(self) -> List[str]:
        return self._get_batch_str_prop(7)

    def _set_CSVFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(7, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: List[str]
    """
    Switch input of  Price curve data to a csv file containing (hour, Price) points, or simply (Price) values for fixed time interval data, one per line. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `CSVFile`, DSS property index: 7.
    """

    def _get_SngFile(self) -> List[str]:
        return self._get_batch_str_prop(8)

    def _set_SngFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(8, value, flags)

    SngFile = property(_get_SngFile, _set_SngFile) # type: List[str]
    """
    Switch input of  Price curve data to a binary file of singles containing (hour, Price) points, or simply (Price) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `SngFile`, DSS property index: 8.
    """

    def _get_DblFile(self) -> List[str]:
        return self._get_batch_str_prop(9)

    def _set_DblFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    DblFile = property(_get_DblFile, _set_DblFile) # type: List[str]
    """
    Switch input of  Price curve data to a binary file of doubles containing (hour, Price) points, or simply (Price) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `DblFile`, DSS property index: 9.
    """

    def _get_SInterval(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 10)

    def _set_SInterval(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    SInterval = property(_get_SInterval, _set_SInterval) # type: BatchFloat64ArrayProxy
    """
    Specify fixed interval in SECONDS. Alternate way to specify Interval property.

    DSS property name: `SInterval`, DSS property index: 10.
    """

    def _get_MInterval(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_MInterval(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    MInterval = property(_get_MInterval, _set_MInterval) # type: BatchFloat64ArrayProxy
    """
    Specify fixed interval in MINUTES. Alternate way to specify Interval property.

    DSS property name: `MInterval`, DSS property index: 11.
    """

    def Action(self, value: Union[AnyStr, int, enums.PriceShapeAction], flags: enums.SetterFlags = 0):
        """
        {DblSave | SngSave} After defining Price curve data... Setting action=DblSave or SngSave will cause the present "Price" values to be written to either a packed file of double or single. The filename is the PriceShape name. 

        DSS property name: `Action`, DSS property index: 12.
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(12, value, flags)
        else:
            self._set_batch_int32_array(12, value, flags)

    def DblSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(PriceShapeAction.DblSave)'''
        self._set_batch_int32_array(12, enums.PriceShapeAction.DblSave, flags)

    def SngSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(PriceShapeAction.SngSave)'''
        self._set_batch_int32_array(12, enums.PriceShapeAction.SngSave, flags)

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_batch_string(13, value, flags)

class PriceShapeBatchProperties(TypedDict):
    NPts: Union[int, Int32Array]
    Interval: Union[float, Float64Array]
    Price: Float64Array
    Hour: Float64Array
    Mean: Union[float, Float64Array]
    StdDev: Union[float, Float64Array]
    CSVFile: Union[AnyStr, List[AnyStr]]
    SngFile: Union[AnyStr, List[AnyStr]]
    DblFile: Union[AnyStr, List[AnyStr]]
    SInterval: Union[float, Float64Array]
    MInterval: Union[float, Float64Array]
    Action: Union[AnyStr, int, enums.PriceShapeAction]
    Like: AnyStr

class IPriceShape(IDSSObj, PriceShapeBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, PriceShape, PriceShapeBatch)
        PriceShapeBatch.__init__(self, self._api_util, sync_cls_idx=PriceShape._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> PriceShape:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> PriceShapeBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) PriceShape objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[PriceShape]:
            yield from PriceShapeBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[PriceShapeProperties]) -> PriceShape:
        """
        Creates a new PriceShape.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[PriceShapeBatchProperties]) -> PriceShapeBatch:
        """
        Creates a new batch of PriceShape objects

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
