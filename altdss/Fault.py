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
from .PDElement import PDElementBatchMixin, PDElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin

class Fault(DSSObj, CircuitElementMixin, PDElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PDElementMixin._extra_slots
    _cls_name = 'Fault'
    _cls_idx = 25
    _cls_int_idx = {
        3,
        8,
        16,
    }
    _cls_float_idx = {
        4,
        5,
        7,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
    }
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'phases': 3,
        'r': 4,
        'pctstddev': 5,
        '%stddev': 5,
        'gmatrix': 6,
        'ontime': 7,
        'temporary': 8,
        'minamps': 9,
        'normamps': 10,
        'emergamps': 11,
        'faultrate': 12,
        'pctperm': 13,
        'repair': 14,
        'basefreq': 15,
        'enabled': 16,
        'like': 17,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PDElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[FaultProperties]) -> Fault:
        """
        Edit this Fault.

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
    Name of first bus. Examples:

    bus1=busname
    bus1=busname.1.2.3

    Bus2 automatically defaults to busname.0,0,0 unless it was previously defined. 

    DSS property name: `Bus1`, DSS property index: 1.
    """

    def _get_Bus2(self) -> str:
        return self._get_prop_string(2)

    def _set_Bus2(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: str
    """
    Name of 2nd bus of the 2-terminal Fault object. Defaults to all phases connected to first bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

    That is, the Fault defaults to a ground fault unless otherwise specified.

    DSS property name: `Bus2`, DSS property index: 2.
    """

    def _get_Phases(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 3)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 3, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int
    """
    Number of Phases. Default is 1.

    DSS property name: `Phases`, DSS property index: 3.
    """

    def _get_R(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_R(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    R = property(_get_R, _set_R) # type: float
    """
    Resistance, each phase, ohms. Default is 0.0001. Assumed to be Mean value if gaussian random mode.Max value if uniform mode.  A Fault is actually a series resistance that defaults to a wye connection to ground on the second terminal.  You may reconnect the 2nd terminal to achieve whatever connection.  Use the Gmatrix property to specify an arbitrary conductance matrix.

    DSS property name: `R`, DSS property index: 4.
    """

    def _get_pctStdDev(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_pctStdDev(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    pctStdDev = property(_get_pctStdDev, _set_pctStdDev) # type: float
    """
    Percent standard deviation in resistance to assume for Monte Carlo fault (MF) solution mode for GAUSSIAN distribution. Default is 0 (no variation from mean).

    DSS property name: `%StdDev`, DSS property index: 5.
    """

    def _get_GMatrix(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    def _set_GMatrix(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(6, value, flags)

    GMatrix = property(_get_GMatrix, _set_GMatrix) # type: Float64Array
    """
    Use this to specify a nodal conductance (G) matrix to represent some arbitrary resistance network. Specify in lower triangle form as usual for DSS matrices.

    DSS property name: `GMatrix`, DSS property index: 6.
    """

    def _get_OnTime(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_OnTime(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    OnTime = property(_get_OnTime, _set_OnTime) # type: float
    """
    Time (sec) at which the fault is established for time varying simulations. Default is 0.0 (on at the beginning of the simulation)

    DSS property name: `OnTime`, DSS property index: 7.
    """

    def _get_Temporary(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 8) != 0

    def _set_Temporary(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 8, value, flags)

    Temporary = property(_get_Temporary, _set_Temporary) # type: bool
    """
    {Yes | No} Default is No.  Designate whether the fault is temporary.  For Time-varying simulations, the fault will be removed if the current through the fault drops below the MINAMPS criteria.

    DSS property name: `Temporary`, DSS property index: 8.
    """

    def _get_MinAmps(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_MinAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    MinAmps = property(_get_MinAmps, _set_MinAmps) # type: float
    """
    Minimum amps that can sustain a temporary fault. Default is 5.

    DSS property name: `MinAmps`, DSS property index: 9.
    """

    def _get_NormAmps(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_NormAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: float
    """
    Normal rated current.

    DSS property name: `NormAmps`, DSS property index: 10.
    """

    def _get_EmergAmps(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_EmergAmps(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: float
    """
    Maximum or emerg current.

    DSS property name: `EmergAmps`, DSS property index: 11.
    """

    def _get_FaultRate(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_FaultRate(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: float
    """
    Failure rate per year.

    DSS property name: `FaultRate`, DSS property index: 12.
    """

    def _get_pctPerm(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_pctPerm(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: float
    """
    Percent of failures that become permanent.

    DSS property name: `pctPerm`, DSS property index: 13.
    """

    def _get_Repair(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_Repair(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: float
    """
    Hours to repair.

    DSS property name: `Repair`, DSS property index: 14.
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


class FaultProperties(TypedDict):
    Bus1: AnyStr
    Bus2: AnyStr
    Phases: int
    R: float
    pctStdDev: float
    GMatrix: Float64Array
    OnTime: float
    Temporary: bool
    MinAmps: float
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class FaultBatch(DSSBatch, CircuitElementBatchMixin, PDElementBatchMixin):
    _cls_name = 'Fault'
    _obj_cls = Fault
    _cls_idx = 25
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PDElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[FaultBatchProperties]) -> FaultBatch:
        """
        Edit this Fault batch.

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
        def __iter__(self) -> Iterator[Fault]:
            yield from DSSBatch.__iter__(self)

    def _get_Bus1(self) -> List[str]:
        return self._get_batch_str_prop(1)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]
    """
    Name of first bus. Examples:

    bus1=busname
    bus1=busname.1.2.3

    Bus2 automatically defaults to busname.0,0,0 unless it was previously defined. 

    DSS property name: `Bus1`, DSS property index: 1.
    """

    def _get_Bus2(self) -> List[str]:
        return self._get_batch_str_prop(2)

    def _set_Bus2(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus2 = property(_get_Bus2, _set_Bus2) # type: List[str]
    """
    Name of 2nd bus of the 2-terminal Fault object. Defaults to all phases connected to first bus, node 0, if not specified. (Shunt Wye Connection to ground reference)

    That is, the Fault defaults to a ground fault unless otherwise specified.

    DSS property name: `Bus2`, DSS property index: 2.
    """

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 3)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(3, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy
    """
    Number of Phases. Default is 1.

    DSS property name: `Phases`, DSS property index: 3.
    """

    def _get_R(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_R(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    R = property(_get_R, _set_R) # type: BatchFloat64ArrayProxy
    """
    Resistance, each phase, ohms. Default is 0.0001. Assumed to be Mean value if gaussian random mode.Max value if uniform mode.  A Fault is actually a series resistance that defaults to a wye connection to ground on the second terminal.  You may reconnect the 2nd terminal to achieve whatever connection.  Use the Gmatrix property to specify an arbitrary conductance matrix.

    DSS property name: `R`, DSS property index: 4.
    """

    def _get_pctStdDev(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_pctStdDev(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    pctStdDev = property(_get_pctStdDev, _set_pctStdDev) # type: BatchFloat64ArrayProxy
    """
    Percent standard deviation in resistance to assume for Monte Carlo fault (MF) solution mode for GAUSSIAN distribution. Default is 0 (no variation from mean).

    DSS property name: `%StdDev`, DSS property index: 5.
    """

    def _get_GMatrix(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._unpack()
        ]

    def _set_GMatrix(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(6, value, flags)

    GMatrix = property(_get_GMatrix, _set_GMatrix) # type: List[Float64Array]
    """
    Use this to specify a nodal conductance (G) matrix to represent some arbitrary resistance network. Specify in lower triangle form as usual for DSS matrices.

    DSS property name: `GMatrix`, DSS property index: 6.
    """

    def _get_OnTime(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 7)

    def _set_OnTime(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    OnTime = property(_get_OnTime, _set_OnTime) # type: BatchFloat64ArrayProxy
    """
    Time (sec) at which the fault is established for time varying simulations. Default is 0.0 (on at the beginning of the simulation)

    DSS property name: `OnTime`, DSS property index: 7.
    """

    def _get_Temporary(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(8)
        ]

    def _set_Temporary(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(8, value, flags)

    Temporary = property(_get_Temporary, _set_Temporary) # type: List[bool]
    """
    {Yes | No} Default is No.  Designate whether the fault is temporary.  For Time-varying simulations, the fault will be removed if the current through the fault drops below the MINAMPS criteria.

    DSS property name: `Temporary`, DSS property index: 8.
    """

    def _get_MinAmps(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 9)

    def _set_MinAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    MinAmps = property(_get_MinAmps, _set_MinAmps) # type: BatchFloat64ArrayProxy
    """
    Minimum amps that can sustain a temporary fault. Default is 5.

    DSS property name: `MinAmps`, DSS property index: 9.
    """

    def _get_NormAmps(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 10)

    def _set_NormAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    NormAmps = property(_get_NormAmps, _set_NormAmps) # type: BatchFloat64ArrayProxy
    """
    Normal rated current.

    DSS property name: `NormAmps`, DSS property index: 10.
    """

    def _get_EmergAmps(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_EmergAmps(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    EmergAmps = property(_get_EmergAmps, _set_EmergAmps) # type: BatchFloat64ArrayProxy
    """
    Maximum or emerg current.

    DSS property name: `EmergAmps`, DSS property index: 11.
    """

    def _get_FaultRate(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 12)

    def _set_FaultRate(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    FaultRate = property(_get_FaultRate, _set_FaultRate) # type: BatchFloat64ArrayProxy
    """
    Failure rate per year.

    DSS property name: `FaultRate`, DSS property index: 12.
    """

    def _get_pctPerm(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_pctPerm(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    pctPerm = property(_get_pctPerm, _set_pctPerm) # type: BatchFloat64ArrayProxy
    """
    Percent of failures that become permanent.

    DSS property name: `pctPerm`, DSS property index: 13.
    """

    def _get_Repair(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 14)

    def _set_Repair(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    Repair = property(_get_Repair, _set_Repair) # type: BatchFloat64ArrayProxy
    """
    Hours to repair.

    DSS property name: `Repair`, DSS property index: 14.
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

class FaultBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Bus2: Union[AnyStr, List[AnyStr]]
    Phases: Union[int, Int32Array]
    R: Union[float, Float64Array]
    pctStdDev: Union[float, Float64Array]
    GMatrix: Float64Array
    OnTime: Union[float, Float64Array]
    Temporary: bool
    MinAmps: Union[float, Float64Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IFault(IDSSObj, FaultBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Fault, FaultBatch)
        FaultBatch.__init__(self, self._api_util, sync_cls_idx=Fault._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Fault:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> FaultBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) Fault objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[Fault]:
            yield from FaultBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[FaultProperties]) -> Fault:
        """
        Creates a new Fault.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[FaultBatchProperties]) -> FaultBatch:
        """
        Creates a new batch of Fault objects

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
