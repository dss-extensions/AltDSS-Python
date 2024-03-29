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
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .MonitorExtras import MonitorObjMixin

class Monitor(DSSObj, CircuitElementMixin, MonitorObjMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + MonitorObjMixin._extra_slots
    _cls_name = 'Monitor'
    _cls_idx = 47
    _cls_int_idx = {
        2,
        3,
        5,
        6,
        7,
        9,
    }
    _cls_float_idx = {
        8,
    }
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'mode': 3,
        'action': 4,
        'residual': 5,
        'vipolar': 6,
        'ppolar': 7,
        'basefreq': 8,
        'enabled': 9,
        'like': 10,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       MonitorObjMixin.__init__(self)

    def edit(self, **kwargs: Unpack[MonitorProperties]) -> Monitor:
        """
        Edit this Monitor.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_Element_str(self) -> str:
        return self._get_prop_string(1)

    def _set_Element_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: str
    """
    Name (Full Object name) of element to which the monitor is connected.

    DSS property name: `Element`, DSS property index: 1.
    """

    def _get_Element(self) -> DSSObj:
        return self._get_obj(1, None)

    def _set_Element(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: DSSObj
    """
    Name (Full Object name) of element to which the monitor is connected.

    DSS property name: `Element`, DSS property index: 1.
    """

    def _get_Terminal(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Terminal(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: int
    """
    Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically. For monitoring states, attach monitor to terminal 1.

    DSS property name: `Terminal`, DSS property index: 2.
    """

    def _get_Mode(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 3)

    def _set_Mode(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 3, value, flags)

    Mode = property(_get_Mode, _set_Mode) # type: int
    """
    Bitmask integer designating the values the monitor is to capture: 
    0 = Voltages and currents at designated terminal
    1 = Powers at designated terminal
    2 = Tap Position (Transformer Device only)
    3 = State Variables (PCElements only)
    4 = Flicker level and severity index (Pst) for voltages. No adders apply.
        Flicker level at simulation time step, Pst at 10-minute time step.
    5 = Solution variables (Iterations, etc).
    Normally, these would be actual phasor quantities from solution.
    6 = Capacitor Switching (Capacitors only)
    7 = Storage state vars (Storage device only)
    8 = All winding currents (Transformer device only)
    9 = Losses, watts and var (of monitored device)
    10 = All Winding voltages (Transformer device only)
    Normally, these would be actual phasor quantities from solution.
    11 = All terminal node voltages and line currents of monitored device
    12 = All terminal node voltages LL and line currents of monitored device
    Combine mode with adders below to achieve other results for terminal quantities:
    +16 = Sequence quantities
    +32 = Magnitude only
    +64 = Positive sequence only or avg of all phases

    Mix adder to obtain desired results. For example:
    Mode=112 will save positive sequence voltage and current magnitudes only
    Mode=48 will save all sequence voltages and currents, but magnitude only.

    DSS property name: `Mode`, DSS property index: 3.
    """

    def Action(self, value: Union[AnyStr, int, enums.MonitorAction], flags: enums.SetterFlags = 0):
        """
        {Clear | Save | Take | Process}
        (C)lears or (S)aves current buffer.
        (T)ake action takes a sample.
        (P)rocesses the data taken so far (e.g. Pst for mode 4).

        Note that monitors are automatically reset (cleared) when the Set Mode= command is issued. Otherwise, the user must explicitly reset all monitors (reset monitors command) or individual monitors with the Clear action.

        DSS property name: `Action`, DSS property index: 4.
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 4, value, flags)
            return

        self._set_string_o(4, value)

    def Clear(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.Clear)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.Clear, flags)

    def Save(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.Save)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.Save, flags)

    def TakeSample(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.TakeSample)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.TakeSample, flags)

    def Process(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.Process)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.Process, flags)

    def Reset(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.Reset)'''
        self._lib.Obj_SetInt32(self._ptr, 4, enums.MonitorAction.Reset, flags)

    def _get_Residual(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 5) != 0

    def _set_Residual(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    Residual = property(_get_Residual, _set_Residual) # type: bool
    """
    {Yes/True | No/False} Default = No.  Include Residual cbannel (sum of all phases) for voltage and current. Does not apply to sequence quantity modes or power modes.

    DSS property name: `Residual`, DSS property index: 5.
    """

    def _get_VIPolar(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 6) != 0

    def _set_VIPolar(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    VIPolar = property(_get_VIPolar, _set_VIPolar) # type: bool
    """
    {Yes/True | No/False} Default = YES. Report voltage and current in polar form (Mag/Angle). (default)  Otherwise, it will be real and imaginary.

    DSS property name: `VIPolar`, DSS property index: 6.
    """

    def _get_PPolar(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 7) != 0

    def _set_PPolar(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 7, value, flags)

    PPolar = property(_get_PPolar, _set_PPolar) # type: bool
    """
    {Yes/True | No/False} Default = YES. Report power in Apparent power, S, in polar form (Mag/Angle).(default)  Otherwise, is P and Q

    DSS property name: `PPolar`, DSS property index: 7.
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 8.
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 9) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 9, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 9.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 10.
        """
        self._set_string_o(10, value)


class MonitorProperties(TypedDict):
    Element: Union[AnyStr, DSSObj]
    Terminal: int
    Mode: int
    Action: Union[AnyStr, int, enums.MonitorAction]
    Residual: bool
    VIPolar: bool
    PPolar: bool
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class MonitorBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'Monitor'
    _obj_cls = Monitor
    _cls_idx = 47
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[MonitorBatchProperties]) -> MonitorBatch:
        """
        Edit this Monitor batch.

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
        def __iter__(self) -> Iterator[Monitor]:
            yield from DSSBatch.__iter__(self)

    def _get_Element_str(self) -> List[str]:
        return self._get_batch_str_prop(1)

    def _set_Element_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: List[str]
    """
    Name (Full Object name) of element to which the monitor is connected.

    DSS property name: `Element`, DSS property index: 1.
    """

    def _get_Element(self) -> List[DSSObj]:
        return self._get_batch_obj_prop(1)

    def _set_Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: List[DSSObj]
    """
    Name (Full Object name) of element to which the monitor is connected.

    DSS property name: `Element`, DSS property index: 1.
    """

    def _get_Terminal(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 2)

    def _set_Terminal(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: BatchInt32ArrayProxy
    """
    Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically. For monitoring states, attach monitor to terminal 1.

    DSS property name: `Terminal`, DSS property index: 2.
    """

    def _get_Mode(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 3)

    def _set_Mode(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(3, value, flags)

    Mode = property(_get_Mode, _set_Mode) # type: BatchInt32ArrayProxy
    """
    Bitmask integer designating the values the monitor is to capture: 
    0 = Voltages and currents at designated terminal
    1 = Powers at designated terminal
    2 = Tap Position (Transformer Device only)
    3 = State Variables (PCElements only)
    4 = Flicker level and severity index (Pst) for voltages. No adders apply.
        Flicker level at simulation time step, Pst at 10-minute time step.
    5 = Solution variables (Iterations, etc).
    Normally, these would be actual phasor quantities from solution.
    6 = Capacitor Switching (Capacitors only)
    7 = Storage state vars (Storage device only)
    8 = All winding currents (Transformer device only)
    9 = Losses, watts and var (of monitored device)
    10 = All Winding voltages (Transformer device only)
    Normally, these would be actual phasor quantities from solution.
    11 = All terminal node voltages and line currents of monitored device
    12 = All terminal node voltages LL and line currents of monitored device
    Combine mode with adders below to achieve other results for terminal quantities:
    +16 = Sequence quantities
    +32 = Magnitude only
    +64 = Positive sequence only or avg of all phases

    Mix adder to obtain desired results. For example:
    Mode=112 will save positive sequence voltage and current magnitudes only
    Mode=48 will save all sequence voltages and currents, but magnitude only.

    DSS property name: `Mode`, DSS property index: 3.
    """

    def Action(self, value: Union[AnyStr, int, enums.MonitorAction], flags: enums.SetterFlags = 0):
        """
        {Clear | Save | Take | Process}
        (C)lears or (S)aves current buffer.
        (T)ake action takes a sample.
        (P)rocesses the data taken so far (e.g. Pst for mode 4).

        Note that monitors are automatically reset (cleared) when the Set Mode= command is issued. Otherwise, the user must explicitly reset all monitors (reset monitors command) or individual monitors with the Clear action.

        DSS property name: `Action`, DSS property index: 4.
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(4, value, flags)
        else:
            self._set_batch_int32_array(4, value, flags)

    def Clear(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.Clear)'''
        self._set_batch_int32_array(4, enums.MonitorAction.Clear, flags)

    def Save(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.Save)'''
        self._set_batch_int32_array(4, enums.MonitorAction.Save, flags)

    def TakeSample(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.TakeSample)'''
        self._set_batch_int32_array(4, enums.MonitorAction.TakeSample, flags)

    def Process(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.Process)'''
        self._set_batch_int32_array(4, enums.MonitorAction.Process, flags)

    def Reset(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(MonitorAction.Reset)'''
        self._set_batch_int32_array(4, enums.MonitorAction.Reset, flags)

    def _get_Residual(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(5)
        ]

    def _set_Residual(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(5, value, flags)

    Residual = property(_get_Residual, _set_Residual) # type: List[bool]
    """
    {Yes/True | No/False} Default = No.  Include Residual cbannel (sum of all phases) for voltage and current. Does not apply to sequence quantity modes or power modes.

    DSS property name: `Residual`, DSS property index: 5.
    """

    def _get_VIPolar(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(6)
        ]

    def _set_VIPolar(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(6, value, flags)

    VIPolar = property(_get_VIPolar, _set_VIPolar) # type: List[bool]
    """
    {Yes/True | No/False} Default = YES. Report voltage and current in polar form (Mag/Angle). (default)  Otherwise, it will be real and imaginary.

    DSS property name: `VIPolar`, DSS property index: 6.
    """

    def _get_PPolar(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(7)
        ]

    def _set_PPolar(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(7, value, flags)

    PPolar = property(_get_PPolar, _set_PPolar) # type: List[bool]
    """
    {Yes/True | No/False} Default = YES. Report power in Apparent power, S, in polar form (Mag/Angle).(default)  Otherwise, is P and Q

    DSS property name: `PPolar`, DSS property index: 7.
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 8)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 8.
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(9)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(9, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 9.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 10.
        """
        self._set_batch_string(10, value, flags)

class MonitorBatchProperties(TypedDict):
    Element: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    Terminal: Union[int, Int32Array]
    Mode: Union[int, Int32Array]
    Action: Union[AnyStr, int, enums.MonitorAction]
    Residual: bool
    VIPolar: bool
    PPolar: bool
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IMonitor(IDSSObj, MonitorBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Monitor, MonitorBatch)
        MonitorBatch.__init__(self, self._api_util, sync_cls_idx=Monitor._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Monitor:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> MonitorBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) Monitor objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[Monitor]:
            yield from MonitorBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[MonitorProperties]) -> Monitor:
        """
        Creates a new Monitor.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[MonitorBatchProperties]) -> MonitorBatch:
        """
        Creates a new batch of Monitor objects

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
