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
from .TCC_Curve import TCC_Curve

class Fuse(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'Fuse'
    _cls_idx = 33
    _cls_int_idx = {
        2,
        4,
        12,
    }
    _cls_float_idx = {
        6,
        7,
        11,
    }
    _cls_prop_idx = {
        'monitoredobj': 1,
        'monitoredterm': 2,
        'switchedobj': 3,
        'switchedterm': 4,
        'fusecurve': 5,
        'ratedcurrent': 6,
        'delay': 7,
        'action': 8,
        'normal': 9,
        'state': 10,
        'basefreq': 11,
        'enabled': 12,
        'like': 13,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[FuseProperties]) -> Fuse:
        """
        Edit this Fuse.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_MonitoredObj_str(self) -> str:
        return self._get_prop_string(1)

    def _set_MonitoredObj_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    MonitoredObj_str = property(_get_MonitoredObj_str, _set_MonitoredObj_str) # type: str
    """
    Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Fuse is connected. This is the "monitored" element. There is no default; must be specified.

    DSS property name: `MonitoredObj`, DSS property index: 1.
    """

    def _get_MonitoredObj(self) -> DSSObj:
        return self._get_obj(1, None)

    def _set_MonitoredObj(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    MonitoredObj = property(_get_MonitoredObj, _set_MonitoredObj) # type: DSSObj
    """
    Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Fuse is connected. This is the "monitored" element. There is no default; must be specified.

    DSS property name: `MonitoredObj`, DSS property index: 1.
    """

    def _get_MonitoredTerm(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_MonitoredTerm(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    MonitoredTerm = property(_get_MonitoredTerm, _set_MonitoredTerm) # type: int
    """
    Number of the terminal of the circuit element to which the Fuse is connected. 1 or 2, typically.  Default is 1.

    DSS property name: `MonitoredTerm`, DSS property index: 2.
    """

    def _get_SwitchedObj_str(self) -> str:
        return self._get_prop_string(3)

    def _set_SwitchedObj_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(3, value, flags)

    SwitchedObj_str = property(_get_SwitchedObj_str, _set_SwitchedObj_str) # type: str
    """
    Name of circuit element switch that the Fuse controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

    DSS property name: `SwitchedObj`, DSS property index: 3.
    """

    def _get_SwitchedObj(self) -> DSSObj:
        return self._get_obj(3, None)

    def _set_SwitchedObj(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(3, value, flags)
            return

        self._set_string_o(3, value, flags)

    SwitchedObj = property(_get_SwitchedObj, _set_SwitchedObj) # type: DSSObj
    """
    Name of circuit element switch that the Fuse controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

    DSS property name: `SwitchedObj`, DSS property index: 3.
    """

    def _get_SwitchedTerm(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 4)

    def _set_SwitchedTerm(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    SwitchedTerm = property(_get_SwitchedTerm, _set_SwitchedTerm) # type: int
    """
    Number of the terminal of the controlled element in which the switch is controlled by the Fuse. 1 or 2, typically.  Default is 1.  Assumes all phases of the element have a fuse of this type.

    DSS property name: `SwitchedTerm`, DSS property index: 4.
    """

    def _get_FuseCurve_str(self) -> str:
        return self._get_prop_string(5)

    def _set_FuseCurve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(5, value, flags)

    FuseCurve_str = property(_get_FuseCurve_str, _set_FuseCurve_str) # type: str
    """
    Name of the TCC Curve object that determines the fuse blowing.  Must have been previously defined as a TCC_Curve object. Default is "Tlink". Multiplying the current values in the curve by the "RatedCurrent" value gives the actual current.

    DSS property name: `FuseCurve`, DSS property index: 5.
    """

    def _get_FuseCurve(self) -> TCC_Curve:
        return self._get_obj(5, TCC_Curve)

    def _set_FuseCurve(self, value: Union[AnyStr, TCC_Curve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(5, value, flags)
            return

        self._set_string_o(5, value, flags)

    FuseCurve = property(_get_FuseCurve, _set_FuseCurve) # type: TCC_Curve
    """
    Name of the TCC Curve object that determines the fuse blowing.  Must have been previously defined as a TCC_Curve object. Default is "Tlink". Multiplying the current values in the curve by the "RatedCurrent" value gives the actual current.

    DSS property name: `FuseCurve`, DSS property index: 5.
    """

    def _get_RatedCurrent(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_RatedCurrent(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    RatedCurrent = property(_get_RatedCurrent, _set_RatedCurrent) # type: float
    """
    Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

    DSS property name: `RatedCurrent`, DSS property index: 6.
    """

    def _get_Delay(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_Delay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: float
    """
    Fixed delay time (sec) added to Fuse blowing time determined from the TCC curve. Default is 0.0. Used to represent fuse clearing time or any other delay.

    DSS property name: `Delay`, DSS property index: 7.
    """

    def Action(self, value: Union[AnyStr, int, enums.FuseAction], flags: enums.SetterFlags = 0):
        """
        DEPRECATED. See "State" property.

        DSS property name: `Action`, DSS property index: 8.
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 8, value, flags)
            return

        self._set_string_o(8, value)

    def close(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(FuseAction.close)'''
        self._lib.Obj_SetInt32(self._ptr, 8, enums.FuseAction.close, flags)

    def open(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(FuseAction.open)'''
        self._lib.Obj_SetInt32(self._ptr, 8, enums.FuseAction.open, flags)

    def _get_Normal(self) -> List[enums.FuseState]:
        return [enums.FuseState(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 9)]

    def _set_Normal(self, value: Union[List[Union[int, enums.FuseState]], List[AnyStr]], flags: enums.SetterFlags = 0):
        if len(value) and not isinstance(value[0], int):
            self._set_string_array_o(9, value, flags)
            return
        self._set_int32_array_o(9, value, flags)

    Normal = property(_get_Normal, _set_Normal) # type: enums.FuseState
    """
    ARRAY of strings {Open | Closed} representing the Normal state of the fuse in each phase of the controlled element. The fuse reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

    DSS property name: `Normal`, DSS property index: 9.
    """

    def _get_Normal_str(self) -> List[str]:
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 9)

    def _set_Normal_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Normal(value, flags)

    Normal_str = property(_get_Normal_str, _set_Normal_str) # type: List[str]
    """
    ARRAY of strings {Open | Closed} representing the Normal state of the fuse in each phase of the controlled element. The fuse reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

    DSS property name: `Normal`, DSS property index: 9.
    """

    def _get_State(self) -> List[enums.FuseState]:
        return [enums.FuseState(val) for val in self._get_int32_list(self._lib.Obj_GetInt32Array, self._ptr, 10)]

    def _set_State(self, value: Union[List[Union[int, enums.FuseState]], List[AnyStr]], flags: enums.SetterFlags = 0):
        if len(value) and not isinstance(value[0], int):
            self._set_string_array_o(10, value, flags)
            return
        self._set_int32_array_o(10, value, flags)

    State = property(_get_State, _set_State) # type: enums.FuseState
    """
    ARRAY of strings {Open | Closed} representing the Actual state of the fuse in each phase of the controlled element. Upon setting, immediately forces state of fuse(s). Simulates manual control on Fuse. Defaults to Closed for all phases.

    DSS property name: `State`, DSS property index: 10.
    """

    def _get_State_str(self) -> List[str]:
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 10)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: List[str]
    """
    ARRAY of strings {Open | Closed} representing the Actual state of the fuse in each phase of the controlled element. Upon setting, immediately forces state of fuse(s). Simulates manual control on Fuse. Defaults to Closed for all phases.

    DSS property name: `State`, DSS property index: 10.
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 11.
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 12) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 12, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 12.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_string_o(13, value)


class FuseProperties(TypedDict):
    MonitoredObj: Union[AnyStr, DSSObj]
    MonitoredTerm: int
    SwitchedObj: Union[AnyStr, DSSObj]
    SwitchedTerm: int
    FuseCurve: Union[AnyStr, TCC_Curve]
    RatedCurrent: float
    Delay: float
    Action: Union[AnyStr, int, enums.FuseAction]
    Normal: Union[List[Union[int, enums.FuseState]], List[AnyStr]]
    State: Union[List[Union[int, enums.FuseState]], List[AnyStr]]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class FuseBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'Fuse'
    _obj_cls = Fuse
    _cls_idx = 33
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[FuseBatchProperties]) -> FuseBatch:
        """
        Edit this Fuse batch.

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
        def __iter__(self) -> Iterator[Fuse]:
            yield from DSSBatch.__iter__(self)

    def _get_MonitoredObj_str(self) -> List[str]:
        return self._get_batch_str_prop(1)

    def _set_MonitoredObj_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    MonitoredObj_str = property(_get_MonitoredObj_str, _set_MonitoredObj_str) # type: List[str]
    """
    Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Fuse is connected. This is the "monitored" element. There is no default; must be specified.

    DSS property name: `MonitoredObj`, DSS property index: 1.
    """

    def _get_MonitoredObj(self) -> List[DSSObj]:
        return self._get_batch_obj_prop(1)

    def _set_MonitoredObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    MonitoredObj = property(_get_MonitoredObj, _set_MonitoredObj) # type: List[DSSObj]
    """
    Full object name of the circuit element, typically a line, transformer, load, or generator, to which the Fuse is connected. This is the "monitored" element. There is no default; must be specified.

    DSS property name: `MonitoredObj`, DSS property index: 1.
    """

    def _get_MonitoredTerm(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 2)

    def _set_MonitoredTerm(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    MonitoredTerm = property(_get_MonitoredTerm, _set_MonitoredTerm) # type: BatchInt32ArrayProxy
    """
    Number of the terminal of the circuit element to which the Fuse is connected. 1 or 2, typically.  Default is 1.

    DSS property name: `MonitoredTerm`, DSS property index: 2.
    """

    def _get_SwitchedObj_str(self) -> List[str]:
        return self._get_batch_str_prop(3)

    def _set_SwitchedObj_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(3, value, flags)

    SwitchedObj_str = property(_get_SwitchedObj_str, _set_SwitchedObj_str) # type: List[str]
    """
    Name of circuit element switch that the Fuse controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

    DSS property name: `SwitchedObj`, DSS property index: 3.
    """

    def _get_SwitchedObj(self) -> List[DSSObj]:
        return self._get_batch_obj_prop(3)

    def _set_SwitchedObj(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(3, value, flags)

    SwitchedObj = property(_get_SwitchedObj, _set_SwitchedObj) # type: List[DSSObj]
    """
    Name of circuit element switch that the Fuse controls. Specify the full object name.Defaults to the same as the Monitored element. This is the "controlled" element.

    DSS property name: `SwitchedObj`, DSS property index: 3.
    """

    def _get_SwitchedTerm(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 4)

    def _set_SwitchedTerm(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(4, value, flags)

    SwitchedTerm = property(_get_SwitchedTerm, _set_SwitchedTerm) # type: BatchInt32ArrayProxy
    """
    Number of the terminal of the controlled element in which the switch is controlled by the Fuse. 1 or 2, typically.  Default is 1.  Assumes all phases of the element have a fuse of this type.

    DSS property name: `SwitchedTerm`, DSS property index: 4.
    """

    def _get_FuseCurve_str(self) -> List[str]:
        return self._get_batch_str_prop(5)

    def _set_FuseCurve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(5, value, flags)

    FuseCurve_str = property(_get_FuseCurve_str, _set_FuseCurve_str) # type: List[str]
    """
    Name of the TCC Curve object that determines the fuse blowing.  Must have been previously defined as a TCC_Curve object. Default is "Tlink". Multiplying the current values in the curve by the "RatedCurrent" value gives the actual current.

    DSS property name: `FuseCurve`, DSS property index: 5.
    """

    def _get_FuseCurve(self) -> List[TCC_Curve]:
        return self._get_batch_obj_prop(5)

    def _set_FuseCurve(self, value: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(5, value, flags)

    FuseCurve = property(_get_FuseCurve, _set_FuseCurve) # type: List[TCC_Curve]
    """
    Name of the TCC Curve object that determines the fuse blowing.  Must have been previously defined as a TCC_Curve object. Default is "Tlink". Multiplying the current values in the curve by the "RatedCurrent" value gives the actual current.

    DSS property name: `FuseCurve`, DSS property index: 5.
    """

    def _get_RatedCurrent(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 6)

    def _set_RatedCurrent(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    RatedCurrent = property(_get_RatedCurrent, _set_RatedCurrent) # type: BatchFloat64ArrayProxy
    """
    Multiplier or actual phase amps for the phase TCC curve.  Defaults to 1.0.

    DSS property name: `RatedCurrent`, DSS property index: 6.
    """

    def _get_Delay(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 7)

    def _set_Delay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: BatchFloat64ArrayProxy
    """
    Fixed delay time (sec) added to Fuse blowing time determined from the TCC curve. Default is 0.0. Used to represent fuse clearing time or any other delay.

    DSS property name: `Delay`, DSS property index: 7.
    """

    def Action(self, value: Union[AnyStr, int, enums.FuseAction], flags: enums.SetterFlags = 0):
        """
        DEPRECATED. See "State" property.

        DSS property name: `Action`, DSS property index: 8.
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(8, value, flags)
        else:
            self._set_batch_int32_array(8, value, flags)

    def close(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(FuseAction.close)'''
        self._set_batch_int32_array(8, enums.FuseAction.close, flags)

    def open(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(FuseAction.open)'''
        self._set_batch_int32_array(8, enums.FuseAction.open, flags)

    def _get_Normal(self) -> List[Int32Array]:
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 9)
            for x in self._unpack()
        ]

    def _set_Normal(self, value: Union[List[Union[int, enums.FuseState]], List[AnyStr]], flags: enums.SetterFlags = 0): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._unpack():
                self._lib.Obj_SetStringArray(x, 9, value_ptr, value_count, flags)

            self._check_for_error()
            return

        self._set_batch_int32_array(9, value, flags)

    Normal = property(_get_Normal, _set_Normal) # type: List[Int32Array]
    """
    ARRAY of strings {Open | Closed} representing the Normal state of the fuse in each phase of the controlled element. The fuse reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

    DSS property name: `Normal`, DSS property index: 9.
    """

    def _get_Normal_str(self) -> List[List[str]]:
        return self._get_string_ll(9)

    def _set_Normal_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Normal(value, flags)

    Normal_str = property(_get_Normal_str, _set_Normal_str) # type: List[List[str]]
    """
    ARRAY of strings {Open | Closed} representing the Normal state of the fuse in each phase of the controlled element. The fuse reverts to this state for reset, change of mode, etc. Defaults to "State" if not specifically declared.

    DSS property name: `Normal`, DSS property index: 9.
    """

    def _get_State(self) -> List[Int32Array]:
        return [
            self._get_int32_array(self._lib.Obj_GetInt32Array, x, 10)
            for x in self._unpack()
        ]

    def _set_State(self, value: Union[List[Union[int, enums.FuseState]], List[AnyStr]], flags: enums.SetterFlags = 0): #TODO: list of lists
        if len(value) and not isinstance(value[0], int):
            value, value_ptr, value_count = self._prepare_string_array(value)
            for x in self._unpack():
                self._lib.Obj_SetStringArray(x, 10, value_ptr, value_count, flags)

            self._check_for_error()
            return

        self._set_batch_int32_array(10, value, flags)

    State = property(_get_State, _set_State) # type: List[Int32Array]
    """
    ARRAY of strings {Open | Closed} representing the Actual state of the fuse in each phase of the controlled element. Upon setting, immediately forces state of fuse(s). Simulates manual control on Fuse. Defaults to Closed for all phases.

    DSS property name: `State`, DSS property index: 10.
    """

    def _get_State_str(self) -> List[List[str]]:
        return self._get_string_ll(10)

    def _set_State_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_State(value, flags)

    State_str = property(_get_State_str, _set_State_str) # type: List[List[str]]
    """
    ARRAY of strings {Open | Closed} representing the Actual state of the fuse in each phase of the controlled element. Upon setting, immediately forces state of fuse(s). Simulates manual control on Fuse. Defaults to Closed for all phases.

    DSS property name: `State`, DSS property index: 10.
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 11.
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(12)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(12, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 12.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 13.
        """
        self._set_batch_string(13, value, flags)

class FuseBatchProperties(TypedDict):
    MonitoredObj: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    MonitoredTerm: Union[int, Int32Array]
    SwitchedObj: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    SwitchedTerm: Union[int, Int32Array]
    FuseCurve: Union[AnyStr, TCC_Curve, List[AnyStr], List[TCC_Curve]]
    RatedCurrent: Union[float, Float64Array]
    Delay: Union[float, Float64Array]
    Action: Union[AnyStr, int, enums.FuseAction]
    Normal: Union[List[Union[int, enums.FuseState]], List[AnyStr]]
    State: Union[List[Union[int, enums.FuseState]], List[AnyStr]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IFuse(IDSSObj, FuseBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Fuse, FuseBatch)
        FuseBatch.__init__(self, self._api_util, sync_cls_idx=Fuse._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Fuse:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> FuseBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) Fuse objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[Fuse]:
            yield from FuseBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[FuseProperties]) -> Fuse:
        """
        Creates a new Fuse.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[FuseBatchProperties]) -> FuseBatch:
        """
        Creates a new batch of Fuse objects

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
