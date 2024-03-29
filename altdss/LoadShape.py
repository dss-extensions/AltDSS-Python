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
from .LoadShapeExtras import LoadShapeBatchMixin, LoadShapeObjMixin

class LoadShape(DSSObj, LoadShapeObjMixin):
    __slots__ = DSSObj._extra_slots + LoadShapeObjMixin._extra_slots
    _cls_name = 'LoadShape'
    _cls_idx = 2
    _cls_int_idx = {
        1,
        12,
        21,
        22,
    }
    _cls_float_idx = {
        2,
        5,
        6,
        13,
        14,
        15,
        16,
        17,
        18,
    }
    _cls_prop_idx = {
        'npts': 1,
        'interval': 2,
        'mult': 3,
        'hour': 4,
        'mean': 5,
        'stddev': 6,
        'csvfile': 7,
        'sngfile': 8,
        'dblfile': 9,
        'action': 10,
        'qmult': 11,
        'useactual': 12,
        'pmax': 13,
        'qmax': 14,
        'sinterval': 15,
        'minterval': 16,
        'pbase': 17,
        'qbase': 18,
        'pmult': 19,
        'pqcsvfile': 20,
        'memorymapping': 21,
        'interpolation': 22,
        'like': 23,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       LoadShapeObjMixin.__init__(self)

    def edit(self, **kwargs: Unpack[LoadShapeProperties]) -> LoadShape:
        """
        Edit this LoadShape.

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
    Max number of points to expect in load shape vectors. This gets reset to the number of multiplier values found (in files only) if less than specified.

    DSS property name: `NPts`, DSS property index: 1.
    """

    def _get_Interval(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 2)

    def _set_Interval(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 2, value, flags)

    Interval = property(_get_Interval, _set_Interval) # type: float
    """
    Time interval for fixed interval data, hrs. Default = 1. If Interval = 0 then time data (in hours) may be at either regular or  irregular intervals and time value must be specified using either the Hour property or input files. Then values are interpolated when Interval=0, but not for fixed interval data.  

    See also "sinterval" and "minterval".

    DSS property name: `Interval`, DSS property index: 2.
    """

    def _get_Hour(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 4)

    def _set_Hour(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(4, value, flags)

    Hour = property(_get_Hour, _set_Hour) # type: Float64Array
    """
    Array of hour values. Only necessary to define for variable interval data (Interval=0). If you set Interval>0 to denote fixed interval data, DO NOT USE THIS PROPERTY. You can also use the syntax: 
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
    Mean of the active power multipliers.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently. Used for Monte Carlo load simulations.

    DSS property name: `Mean`, DSS property index: 5.
    """

    def _get_StdDev(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_StdDev(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    StdDev = property(_get_StdDev, _set_StdDev) # type: float
    """
    Standard deviation of active power multipliers.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently.Is overwritten if you subsequently read in a curve

    Used for Monte Carlo load simulations.

    DSS property name: `StdDev`, DSS property index: 6.
    """

    def _get_CSVFile(self) -> str:
        return self._get_prop_string(7)

    def _set_CSVFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(7, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: str
    """
    Switch input of active power load curve data to a CSV text file containing (hour, mult) points, or simply (mult) values for fixed time interval data, one per line. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `CSVFile`, DSS property index: 7.
    """

    def _get_SngFile(self) -> str:
        return self._get_prop_string(8)

    def _set_SngFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(8, value, flags)

    SngFile = property(_get_SngFile, _set_SngFile) # type: str
    """
    Switch input of active power load curve data to a binary file of singles containing (hour, mult) points, or simply (mult) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `SngFile`, DSS property index: 8.
    """

    def _get_DblFile(self) -> str:
        return self._get_prop_string(9)

    def _set_DblFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    DblFile = property(_get_DblFile, _set_DblFile) # type: str
    """
    Switch input of active power load curve data to a binary file of doubles containing (hour, mult) points, or simply (mult) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `DblFile`, DSS property index: 9.
    """

    def Action(self, value: Union[AnyStr, int, enums.LoadShapeAction], flags: enums.SetterFlags = 0):
        """
        {NORMALIZE | DblSave | SngSave} After defining load curve data, setting action=normalize will modify the multipliers so that the peak is 1.0. The mean and std deviation are recomputed.

        Setting action=DblSave or SngSave will cause the present mult and qmult values to be written to either a packed file of double or single. The filename is the loadshape name. The mult array will have a "_P" appended on the file name and the qmult array, if it exists, will have "_Q" appended.

        DSS property name: `Action`, DSS property index: 10.
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 10, value, flags)
            return

        self._set_string_o(10, value)

    def Normalize(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(LoadShapeAction.Normalize)'''
        self._lib.Obj_SetInt32(self._ptr, 10, enums.LoadShapeAction.Normalize, flags)

    def DblSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(LoadShapeAction.DblSave)'''
        self._lib.Obj_SetInt32(self._ptr, 10, enums.LoadShapeAction.DblSave, flags)

    def SngSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(LoadShapeAction.SngSave)'''
        self._lib.Obj_SetInt32(self._ptr, 10, enums.LoadShapeAction.SngSave, flags)

    def _get_QMult(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 11)

    def _set_QMult(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(11, value, flags)

    QMult = property(_get_QMult, _set_QMult) # type: Float64Array
    """
    Array of multiplier values for reactive power (Q).  You can also use the syntax: 
    qmult = (file=filename)     !for text file one value per line
    qmult = (dblfile=filename)  !for packed file of doubles
    qmult = (sngfile=filename)  !for packed file of singles 
    qmult = (file=MyCSVFile.csv, col=4, header=yes)  !for multicolumn CSV files 

    DSS property name: `QMult`, DSS property index: 11.
    """

    def _get_UseActual(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    def _set_UseActual(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 12, value, flags)

    UseActual = property(_get_UseActual, _set_UseActual) # type: bool
    """
    {Yes | No* | True | False*} If true, signifies to Load, Generator, Vsource, or other objects to use the return value as the actual kW, kvar, kV, or other value rather than a multiplier. Nominally for AMI Load data but may be used for other functions.

    DSS property name: `UseActual`, DSS property index: 12.
    """

    def _get_PMax(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_PMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    PMax = property(_get_PMax, _set_PMax) # type: float
    """
    kW value at the time of max power. Is automatically set upon reading in a loadshape. Use this property to override the value automatically computed or to retrieve the value computed.

    DSS property name: `PMax`, DSS property index: 13.
    """

    def _get_QMax(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_QMax(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    QMax = property(_get_QMax, _set_QMax) # type: float
    """
    kvar value at the time of max kW power. Is automatically set upon reading in a loadshape. Use this property to override the value automatically computed or to retrieve the value computed.

    DSS property name: `QMax`, DSS property index: 14.
    """

    def _get_SInterval(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_SInterval(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    SInterval = property(_get_SInterval, _set_SInterval) # type: float
    """
    Specify fixed interval in SECONDS. Alternate way to specify Interval property.

    DSS property name: `SInterval`, DSS property index: 15.
    """

    def _get_MInterval(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_MInterval(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    MInterval = property(_get_MInterval, _set_MInterval) # type: float
    """
    Specify fixed interval in MINUTES. Alternate way to specify Interval property.

    DSS property name: `MInterval`, DSS property index: 16.
    """

    def _get_PBase(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_PBase(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    PBase = property(_get_PBase, _set_PBase) # type: float
    """
    Base P value for normalization. Default is zero, meaning the peak will be used.

    DSS property name: `PBase`, DSS property index: 17.
    """

    def _get_QBase(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_QBase(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    QBase = property(_get_QBase, _set_QBase) # type: float
    """
    Base Q value for normalization. Default is zero, meaning the peak will be used.

    DSS property name: `QBase`, DSS property index: 18.
    """

    def _get_PMult(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 19)

    def _set_PMult(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(19, value, flags)

    PMult = property(_get_PMult, _set_PMult) # type: Float64Array
    """
    Synonym for "mult".

    DSS property name: `PMult`, DSS property index: 19.
    """

    def _get_PQCSVFile(self) -> str:
        return self._get_prop_string(20)

    def _set_PQCSVFile(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(20, value, flags)

    PQCSVFile = property(_get_PQCSVFile, _set_PQCSVFile) # type: str
    """
    Switch input to a CSV text file containing (active, reactive) power (P, Q) multiplier pairs, one per row. 
    If the interval=0, there should be 3 items on each line: (hour, Pmult, Qmult)

    DSS property name: `PQCSVFile`, DSS property index: 20.
    """

    def _get_MemoryMapping(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 21) != 0

    def _set_MemoryMapping(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 21, value, flags)

    MemoryMapping = property(_get_MemoryMapping, _set_MemoryMapping) # type: bool
    """
    {Yes | No* | True | False*} Enables the memory mapping functionality for dealing with large amounts of load shapes. 
    By default is False. Use it to accelerate the model loading when the containing a large number of load shapes.

    DSS property name: `MemoryMapping`, DSS property index: 21.
    """

    def _get_Interpolation(self) -> enums.LoadShapeInterpolation:
        return enums.LoadShapeInterpolation(self._lib.Obj_GetInt32(self._ptr, 22))

    def _set_Interpolation(self, value: Union[AnyStr, int, enums.LoadShapeInterpolation], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(22, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 22, value, flags)

    Interpolation = property(_get_Interpolation, _set_Interpolation) # type: enums.LoadShapeInterpolation
    """
    {AVG* | EDGE} Defines the interpolation method used for connecting distant dots within the load shape.

    By default is AVG (average), which will return a multiplier for missing intervals based on the closest multiplier in time.
    EDGE interpolation keeps the last known value for missing intervals until the next defined multiplier arrives.

    DSS property name: `Interpolation`, DSS property index: 22.
    """

    def _get_Interpolation_str(self) -> str:
        return self._get_prop_string(22)

    def _set_Interpolation_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Interpolation(value, flags)

    Interpolation_str = property(_get_Interpolation_str, _set_Interpolation_str) # type: str
    """
    {AVG* | EDGE} Defines the interpolation method used for connecting distant dots within the load shape.

    By default is AVG (average), which will return a multiplier for missing intervals based on the closest multiplier in time.
    EDGE interpolation keeps the last known value for missing intervals until the next defined multiplier arrives.

    DSS property name: `Interpolation`, DSS property index: 22.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 23.
        """
        self._set_string_o(23, value)


class LoadShapeProperties(TypedDict):
    NPts: int
    Interval: float
    Hour: Float64Array
    Mean: float
    StdDev: float
    CSVFile: AnyStr
    SngFile: AnyStr
    DblFile: AnyStr
    Action: Union[AnyStr, int, enums.LoadShapeAction]
    QMult: Float64Array
    UseActual: bool
    PMax: float
    QMax: float
    SInterval: float
    MInterval: float
    PBase: float
    QBase: float
    PMult: Float64Array
    PQCSVFile: AnyStr
    MemoryMapping: bool
    Interpolation: Union[AnyStr, int, enums.LoadShapeInterpolation]
    Like: AnyStr

class LoadShapeBatch(DSSBatch, LoadShapeBatchMixin):
    _cls_name = 'LoadShape'
    _obj_cls = LoadShape
    _cls_idx = 2
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       LoadShapeBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[LoadShapeBatchProperties]) -> LoadShapeBatch:
        """
        Edit this LoadShape batch.

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
        def __iter__(self) -> Iterator[LoadShape]:
            yield from DSSBatch.__iter__(self)

    def _get_NPts(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_NPts(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    NPts = property(_get_NPts, _set_NPts) # type: BatchInt32ArrayProxy
    """
    Max number of points to expect in load shape vectors. This gets reset to the number of multiplier values found (in files only) if less than specified.

    DSS property name: `NPts`, DSS property index: 1.
    """

    def _get_Interval(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 2)

    def _set_Interval(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(2, value, flags)

    Interval = property(_get_Interval, _set_Interval) # type: BatchFloat64ArrayProxy
    """
    Time interval for fixed interval data, hrs. Default = 1. If Interval = 0 then time data (in hours) may be at either regular or  irregular intervals and time value must be specified using either the Hour property or input files. Then values are interpolated when Interval=0, but not for fixed interval data.  

    See also "sinterval" and "minterval".

    DSS property name: `Interval`, DSS property index: 2.
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
    Array of hour values. Only necessary to define for variable interval data (Interval=0). If you set Interval>0 to denote fixed interval data, DO NOT USE THIS PROPERTY. You can also use the syntax: 
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
    Mean of the active power multipliers.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently. Used for Monte Carlo load simulations.

    DSS property name: `Mean`, DSS property index: 5.
    """

    def _get_StdDev(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 6)

    def _set_StdDev(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    StdDev = property(_get_StdDev, _set_StdDev) # type: BatchFloat64ArrayProxy
    """
    Standard deviation of active power multipliers.  This is computed on demand the first time a value is needed.  However, you may set it to another value independently.Is overwritten if you subsequently read in a curve

    Used for Monte Carlo load simulations.

    DSS property name: `StdDev`, DSS property index: 6.
    """

    def _get_CSVFile(self) -> List[str]:
        return self._get_batch_str_prop(7)

    def _set_CSVFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(7, value, flags)

    CSVFile = property(_get_CSVFile, _set_CSVFile) # type: List[str]
    """
    Switch input of active power load curve data to a CSV text file containing (hour, mult) points, or simply (mult) values for fixed time interval data, one per line. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `CSVFile`, DSS property index: 7.
    """

    def _get_SngFile(self) -> List[str]:
        return self._get_batch_str_prop(8)

    def _set_SngFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(8, value, flags)

    SngFile = property(_get_SngFile, _set_SngFile) # type: List[str]
    """
    Switch input of active power load curve data to a binary file of singles containing (hour, mult) points, or simply (mult) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `SngFile`, DSS property index: 8.
    """

    def _get_DblFile(self) -> List[str]:
        return self._get_batch_str_prop(9)

    def _set_DblFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    DblFile = property(_get_DblFile, _set_DblFile) # type: List[str]
    """
    Switch input of active power load curve data to a binary file of doubles containing (hour, mult) points, or simply (mult) values for fixed time interval data, packed one after another. NOTE: This action may reset the number of points to a lower value.

    DSS property name: `DblFile`, DSS property index: 9.
    """

    def Action(self, value: Union[AnyStr, int, enums.LoadShapeAction], flags: enums.SetterFlags = 0):
        """
        {NORMALIZE | DblSave | SngSave} After defining load curve data, setting action=normalize will modify the multipliers so that the peak is 1.0. The mean and std deviation are recomputed.

        Setting action=DblSave or SngSave will cause the present mult and qmult values to be written to either a packed file of double or single. The filename is the loadshape name. The mult array will have a "_P" appended on the file name and the qmult array, if it exists, will have "_Q" appended.

        DSS property name: `Action`, DSS property index: 10.
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(10, value, flags)
        else:
            self._set_batch_int32_array(10, value, flags)

    def Normalize(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(LoadShapeAction.Normalize)'''
        self._set_batch_int32_array(10, enums.LoadShapeAction.Normalize, flags)

    def DblSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(LoadShapeAction.DblSave)'''
        self._set_batch_int32_array(10, enums.LoadShapeAction.DblSave, flags)

    def SngSave(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(LoadShapeAction.SngSave)'''
        self._set_batch_int32_array(10, enums.LoadShapeAction.SngSave, flags)

    def _get_QMult(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 11)
            for x in self._unpack()
        ]

    def _set_QMult(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(11, value, flags)

    QMult = property(_get_QMult, _set_QMult) # type: List[Float64Array]
    """
    Array of multiplier values for reactive power (Q).  You can also use the syntax: 
    qmult = (file=filename)     !for text file one value per line
    qmult = (dblfile=filename)  !for packed file of doubles
    qmult = (sngfile=filename)  !for packed file of singles 
    qmult = (file=MyCSVFile.csv, col=4, header=yes)  !for multicolumn CSV files 

    DSS property name: `QMult`, DSS property index: 11.
    """

    def _get_UseActual(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(12)
        ]

    def _set_UseActual(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(12, value, flags)

    UseActual = property(_get_UseActual, _set_UseActual) # type: List[bool]
    """
    {Yes | No* | True | False*} If true, signifies to Load, Generator, Vsource, or other objects to use the return value as the actual kW, kvar, kV, or other value rather than a multiplier. Nominally for AMI Load data but may be used for other functions.

    DSS property name: `UseActual`, DSS property index: 12.
    """

    def _get_PMax(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_PMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    PMax = property(_get_PMax, _set_PMax) # type: BatchFloat64ArrayProxy
    """
    kW value at the time of max power. Is automatically set upon reading in a loadshape. Use this property to override the value automatically computed or to retrieve the value computed.

    DSS property name: `PMax`, DSS property index: 13.
    """

    def _get_QMax(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 14)

    def _set_QMax(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    QMax = property(_get_QMax, _set_QMax) # type: BatchFloat64ArrayProxy
    """
    kvar value at the time of max kW power. Is automatically set upon reading in a loadshape. Use this property to override the value automatically computed or to retrieve the value computed.

    DSS property name: `QMax`, DSS property index: 14.
    """

    def _get_SInterval(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 15)

    def _set_SInterval(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    SInterval = property(_get_SInterval, _set_SInterval) # type: BatchFloat64ArrayProxy
    """
    Specify fixed interval in SECONDS. Alternate way to specify Interval property.

    DSS property name: `SInterval`, DSS property index: 15.
    """

    def _get_MInterval(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 16)

    def _set_MInterval(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    MInterval = property(_get_MInterval, _set_MInterval) # type: BatchFloat64ArrayProxy
    """
    Specify fixed interval in MINUTES. Alternate way to specify Interval property.

    DSS property name: `MInterval`, DSS property index: 16.
    """

    def _get_PBase(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 17)

    def _set_PBase(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    PBase = property(_get_PBase, _set_PBase) # type: BatchFloat64ArrayProxy
    """
    Base P value for normalization. Default is zero, meaning the peak will be used.

    DSS property name: `PBase`, DSS property index: 17.
    """

    def _get_QBase(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 18)

    def _set_QBase(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    QBase = property(_get_QBase, _set_QBase) # type: BatchFloat64ArrayProxy
    """
    Base Q value for normalization. Default is zero, meaning the peak will be used.

    DSS property name: `QBase`, DSS property index: 18.
    """

    def _get_PMult(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 19)
            for x in self._unpack()
        ]

    def _set_PMult(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(19, value, flags)

    PMult = property(_get_PMult, _set_PMult) # type: List[Float64Array]
    """
    Synonym for "mult".

    DSS property name: `PMult`, DSS property index: 19.
    """

    def _get_PQCSVFile(self) -> List[str]:
        return self._get_batch_str_prop(20)

    def _set_PQCSVFile(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(20, value, flags)

    PQCSVFile = property(_get_PQCSVFile, _set_PQCSVFile) # type: List[str]
    """
    Switch input to a CSV text file containing (active, reactive) power (P, Q) multiplier pairs, one per row. 
    If the interval=0, there should be 3 items on each line: (hour, Pmult, Qmult)

    DSS property name: `PQCSVFile`, DSS property index: 20.
    """

    def _get_MemoryMapping(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(21)
        ]

    def _set_MemoryMapping(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(21, value, flags)

    MemoryMapping = property(_get_MemoryMapping, _set_MemoryMapping) # type: List[bool]
    """
    {Yes | No* | True | False*} Enables the memory mapping functionality for dealing with large amounts of load shapes. 
    By default is False. Use it to accelerate the model loading when the containing a large number of load shapes.

    DSS property name: `MemoryMapping`, DSS property index: 21.
    """

    def _get_Interpolation(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 22)

    def _set_Interpolation(self, value: Union[AnyStr, int, enums.LoadShapeInterpolation, List[AnyStr], List[int], List[enums.LoadShapeInterpolation], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(22, value, flags)
            return

        self._set_batch_int32_array(22, value, flags)

    Interpolation = property(_get_Interpolation, _set_Interpolation) # type: BatchInt32ArrayProxy
    """
    {AVG* | EDGE} Defines the interpolation method used for connecting distant dots within the load shape.

    By default is AVG (average), which will return a multiplier for missing intervals based on the closest multiplier in time.
    EDGE interpolation keeps the last known value for missing intervals until the next defined multiplier arrives.

    DSS property name: `Interpolation`, DSS property index: 22.
    """

    def _get_Interpolation_str(self) -> List[str]:
        return self._get_batch_str_prop(22)

    def _set_Interpolation_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Interpolation(value, flags)

    Interpolation_str = property(_get_Interpolation_str, _set_Interpolation_str) # type: List[str]
    """
    {AVG* | EDGE} Defines the interpolation method used for connecting distant dots within the load shape.

    By default is AVG (average), which will return a multiplier for missing intervals based on the closest multiplier in time.
    EDGE interpolation keeps the last known value for missing intervals until the next defined multiplier arrives.

    DSS property name: `Interpolation`, DSS property index: 22.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 23.
        """
        self._set_batch_string(23, value, flags)

class LoadShapeBatchProperties(TypedDict):
    NPts: Union[int, Int32Array]
    Interval: Union[float, Float64Array]
    Hour: Float64Array
    Mean: Union[float, Float64Array]
    StdDev: Union[float, Float64Array]
    CSVFile: Union[AnyStr, List[AnyStr]]
    SngFile: Union[AnyStr, List[AnyStr]]
    DblFile: Union[AnyStr, List[AnyStr]]
    Action: Union[AnyStr, int, enums.LoadShapeAction]
    QMult: Float64Array
    UseActual: bool
    PMax: Union[float, Float64Array]
    QMax: Union[float, Float64Array]
    SInterval: Union[float, Float64Array]
    MInterval: Union[float, Float64Array]
    PBase: Union[float, Float64Array]
    QBase: Union[float, Float64Array]
    PMult: Float64Array
    PQCSVFile: Union[AnyStr, List[AnyStr]]
    MemoryMapping: bool
    Interpolation: Union[AnyStr, int, enums.LoadShapeInterpolation, List[AnyStr], List[int], List[enums.LoadShapeInterpolation], Int32Array]
    Like: AnyStr

class ILoadShape(IDSSObj, LoadShapeBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, LoadShape, LoadShapeBatch)
        LoadShapeBatch.__init__(self, self._api_util, sync_cls_idx=LoadShape._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> LoadShape:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> LoadShapeBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) LoadShape objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[LoadShape]:
            yield from LoadShapeBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[LoadShapeProperties]) -> LoadShape:
        """
        Creates a new LoadShape.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[LoadShapeBatchProperties]) -> LoadShapeBatch:
        """
        Creates a new batch of LoadShape objects

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
