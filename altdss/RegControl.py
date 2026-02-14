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
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .AutoTrans import AutoTrans
from .Transformer import Transformer as TransformerObj

class RegControl(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'RegControl'
    _cls_idx = 21
    _cls_int_idx = {
        2,
        11,
        17,
        18,
        19,
        20,
        22,
        25,
        26,
        28,
        32,
        33,
        34,
        35,
        38,
    }
    _cls_float_idx = {
        3,
        4,
        5,
        6,
        7,
        8,
        10,
        12,
        13,
        14,
        15,
        16,
        21,
        23,
        24,
        27,
        30,
        31,
        36,
        37,
    }
    _cls_prop_idx = {
        'transformer': 1,
        'winding': 2,
        'vreg': 3,
        'band': 4,
        'ptratio': 5,
        'ctprim': 6,
        'r': 7,
        'x': 8,
        'bus': 9,
        'delay': 10,
        'reversible': 11,
        'revvreg': 12,
        'revband': 13,
        'revr': 14,
        'revx': 15,
        'tapdelay': 16,
        'debugtrace': 17,
        'maxtapchange': 18,
        'inversetime': 19,
        'tapwinding': 20,
        'vlimit': 21,
        'ptphase': 22,
        'revthreshold': 23,
        'revdelay': 24,
        'revneutral': 25,
        'eventlog': 26,
        'remoteptratio': 27,
        'tapnum': 28,
        'reset': 29,
        'ldc_z': 30,
        'rev_z': 31,
        'cogen': 32,
        'idle': 33,
        'idlereverse': 34,
        'idleforward': 35,
        'fwdthreshold': 36,
        'basefreq': 37,
        'enabled': 38,
        'like': 39,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[RegControlProperties]) -> RegControl:
        """
        Edit this RegControl.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_Transformer_str(self) -> str:
        return self._get_prop_string(1)

    def _set_Transformer_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Transformer_str = property(_get_Transformer_str, _set_Transformer_str) # type: str
    """
    Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

    Transformer=Xfmr1

    Name: `Transformer`
    """

    def _get_Transformer(self) -> Union[TransformerObj, AutoTrans]:
        return self._get_obj(1, None)

    def _set_Transformer(self, value: Union[AnyStr, TransformerObj, AutoTrans], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    Transformer = property(_get_Transformer, _set_Transformer) # type: TransformerObj, AutoTrans
    """
    Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

    Transformer=Xfmr1

    Name: `Transformer`
    """

    def _get_Winding(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Winding(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Winding = property(_get_Winding, _set_Winding) # type: int
    """
    Number of the winding of the transformer element that the RegControl is monitoring. 1 or 2, typically.  Side Effect: Sets TAPWINDING property to the same winding.

    Name: `Winding`
    Default: 1
    """

    def _get_VReg(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_VReg(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    VReg = property(_get_VReg, _set_VReg) # type: float
    """
    Voltage regulator setting for the winding being controlled.  Multiplying this value times the ptratio should yield the voltage across the WINDING of the controlled transformer.

    Name: `VReg`
    Units: V
    Default: 120.0
    """

    def _get_Band(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_Band(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    Band = property(_get_Band, _set_Band) # type: float
    """
    Bandwidth in VOLTS for the controlled bus (see help for ptratio property).

    Name: `Band`
    Default: 3.0
    """

    def _get_PTRatio(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_PTRatio(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    PTRatio = property(_get_PTRatio, _set_PTRatio) # type: float
    """
    Ratio of the PT that converts the controlled winding voltage to the regulator control voltage. If the winding is Wye, the line-to-neutral voltage is used.  Else, the line-to-line voltage is used. SIDE EFFECT: Also sets RemotePTRatio property.

    Name: `PTRatio`
    Default: 60.0
    """

    def _get_CTPrim(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    def _set_CTPrim(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 6, value, flags)

    CTPrim = property(_get_CTPrim, _set_CTPrim) # type: float
    """
    Rating of the primary CT rating for which the line amps convert to control rated amps. The typical default secondary ampere rating is 0.2 Amps (check with manufacturer specs). Current at which the LDC voltages match the R and X settings.

    Name: `CTPrim`
    Units: A
    Default: 300.0
    """

    def _get_R(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_R(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    R = property(_get_R, _set_R) # type: float
    """
    R setting on the line drop compensator in the regulator, expressed in VOLTS.

    Name: `R`
    Default: 0.0
    """

    def _get_X(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_X(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    X = property(_get_X, _set_X) # type: float
    """
    X setting on the line drop compensator in the regulator, expressed in VOLTS.

    Name: `X`
    Default: 0.0
    """

    def _get_Bus(self) -> str:
        return self._get_prop_string(9)

    def _set_Bus(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    Bus = property(_get_Bus, _set_Bus) # type: str
    """
    Name of a bus (busname.nodename) in the system to use as the controlled bus instead of the bus to which the transformer winding is connected or the R and X line drop compensator settings.  Do not specify this value if you wish to use the line drop compensator settings.  Default is null string. Assumes the base voltage for this bus is the same as the transformer winding base specified above. Note: This bus (1-phase) WILL BE CREATED by the regulator control upon SOLVE if not defined by some other device. You can specify the node of the bus you wish to sample (defaults to 1). If specified, the RegControl is redefined as a 1-phase device since only one voltage is used.

    Name: `Bus`
    """

    def _get_Delay(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_Delay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: float
    """
    Time delay from when the voltage goes out of band to when the tap changing begins. This is used to determine which regulator control will act first. You may specify any floating point number to achieve a model of whatever condition is necessary.

    Name: `Delay`
    Units: s
    Default: 15.0
    """

    def _get_Reversible(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 11) != 0

    def _set_Reversible(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 11, value, flags)

    Reversible = property(_get_Reversible, _set_Reversible) # type: bool
    """
    Indicates whether the regulator has a reverse operation mode (associated settings must be defined).
    Default is `No`, which means the regulator forward settings apply for both forward and reverse power flow.
    Typically applies only to line regulators and not to LTC on a substation transformer.

    Use the `RevNeutral`, `Idle`, `IdleReverse` and `IdleForward` properties to define the desired operating mode:
    - Bidirectional: `Reversible=yes`,`Idle=yes/no` (idling in the "no-load region" depends on the controller and is a functionality typically described in its datasheet)
    - Locked Forward: `Reversible=yes`, `IdleReverse=yes`
    - Reverse Idle: `Reversible=yes`, `Idle=yes`, `IdleReverse=yes`
    - Locked Reverse: `Reversible=yes`, `IdleForward=yes`
    - Neutral Idle: `Reversible=yes`, `RevNeutral=yes`, `Idle=yes/no` (idling in the "no-load region" depends on the controller and is a functionality typically described in its datasheet)

    Name: `Reversible`
    Default: False
    """

    def _get_RevVReg(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_RevVReg(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    RevVReg = property(_get_RevVReg, _set_RevVReg) # type: float
    """
    Voltage setting in volts for operation in the reverse direction.

    Name: `RevVReg`
    Default: 120.0
    """

    def _get_RevBand(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_RevBand(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    RevBand = property(_get_RevBand, _set_RevBand) # type: float
    """
    Bandwidth for operating in the reverse direction.

    Name: `RevBand`
    Default: 3.0
    """

    def _get_RevR(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_RevR(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    RevR = property(_get_RevR, _set_RevR) # type: float
    """
    R line drop compensator setting for reverse direction.

    Name: `RevR`
    Default: 0.0
    """

    def _get_RevX(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_RevX(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    RevX = property(_get_RevX, _set_RevX) # type: float
    """
    X line drop compensator setting for reverse direction.

    Name: `RevX`
    Default: 0.0
    """

    def _get_TapDelay(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_TapDelay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    TapDelay = property(_get_TapDelay, _set_TapDelay) # type: float
    """
    Delay between tap changes. This is how long it takes between changes after the first change.

    Name: `TapDelay`
    Units: s
    Default: 2.0
    """

    def _get_DebugTrace(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 17) != 0

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 17, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: bool
    """
    Turn this on to capture the progress of the regulator model for each control iteration.  Creates a separate file for each RegControl named "REG_name.csv".

    Name: `DebugTrace`
    Default: False
    """

    def _get_MaxTapChange(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 18)

    def _set_MaxTapChange(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 18, value, flags)

    MaxTapChange = property(_get_MaxTapChange, _set_MaxTapChange) # type: int
    """
    Maximum allowable tap change per control iteration in STATIC control mode.

    Set this to 1 to better approximate actual control action. 

    Set this to 0 to fix the tap in the current position.

    Name: `MaxTapChange`
    Default: 16
    """

    def _get_InverseTime(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 19) != 0

    def _set_InverseTime(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 19, value, flags)

    InverseTime = property(_get_InverseTime, _set_InverseTime) # type: bool
    """
    The time delay is adjusted inversely proportional to the amount the voltage is outside the band down to 10%.

    Name: `InverseTime`
    Default: False
    """

    def _get_TapWinding(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 20)

    def _set_TapWinding(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 20, value, flags)

    TapWinding = property(_get_TapWinding, _set_TapWinding) # type: int
    """
    Winding containing the actual taps, if different than the WINDING property. Defaults to the same winding as specified by the WINDING property.

    Name: `TapWinding`
    """

    def _get_VLimit(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_VLimit(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    VLimit = property(_get_VLimit, _set_VLimit) # type: float
    """
    Voltage Limit for bus to which regulated winding is connected (e.g. first customer). Set to a value greater then zero to activate this function.

    Name: `VLimit`
    Units: V
    Default: 0.0
    """

    def _get_PTPhase(self) -> Union[enums.RegControlPhaseSelection, int]:
        value = self._lib.Obj_GetInt32(self._ptr, 22)
        if value > 0:
            return value

        return enums.RegControlPhaseSelection(value)

    def _set_PTPhase(self, value: Union[AnyStr, int, enums.RegControlPhaseSelection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(22, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 22, value, flags)

    PTPhase = property(_get_PTPhase, _set_PTPhase) # type: enums.RegControlPhaseSelection
    """
    For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Must be less than or equal to the number of phases. Ignored for regulated bus.

    Name: `PTPhase`
    Default: 1
    """

    def _get_PTPhase_str(self) -> str:
        return self._get_prop_string(22)

    def _set_PTPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_PTPhase(value, flags)

    PTPhase_str = property(_get_PTPhase_str, _set_PTPhase_str) # type: str
    """
    For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Must be less than or equal to the number of phases. Ignored for regulated bus.

    Name: `PTPhase`
    Default: 1
    """

    def _get_RevThreshold(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_RevThreshold(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    RevThreshold = property(_get_RevThreshold, _set_RevThreshold) # type: float
    """
    kW reverse power threshold for reversing the direction of the regulator.

    Defines a no-load band between `-RevThreshold` and `+RevThreshold`.

    **Important**: If an uneven band is desired, set `RevThreshold` to the desired lower bound (negative values allowed) and reset the upper bound using `FwdThreshold` right after.

    Name: `RevThreshold`
    Units: kW
    Default: -100.0
    """

    def _get_RevDelay(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_RevDelay(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    RevDelay = property(_get_RevDelay, _set_RevDelay) # type: float
    """
    Time Delay for executing the reversing action once the threshold for reversing has been exceeded.

    Name: `RevDelay`
    Units: s
    Default: 60.0
    """

    def _get_RevNeutral(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 25) != 0

    def _set_RevNeutral(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 25, value, flags)

    RevNeutral = property(_get_RevNeutral, _set_RevNeutral) # type: bool
    """
    Set this to Yes if you want the regulator to go to neutral in the reverse direction or in cogen operation.

    Name: `RevNeutral`
    Default: False
    """

    def _get_EventLog(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 26) != 0

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 26, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: bool
    """
    Log control actions to Eventlog.

    Name: `EventLog`
    Default: False
    """

    def _get_RemotePTRatio(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_RemotePTRatio(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    RemotePTRatio = property(_get_RemotePTRatio, _set_RemotePTRatio) # type: float
    """
    When regulating a bus (the Bus= property is set), the PT ratio required to convert actual voltage at the remote bus to control voltage. Is initialized to PTratio property. Set this property after setting PTratio.

    Name: `RemotePTRatio`
    """

    def _get_TapNum(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 28)

    def _set_TapNum(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 28, value, flags)

    TapNum = property(_get_TapNum, _set_TapNum) # type: int
    """
    An integer number indicating the tap position that the controlled transformer winding tap position is currently at, or is being set to.  If being set, and the value is outside the range of the transformer min or max tap, then set to the min or max tap position as appropriate. Default is 0

    Name: `TapNum`
    Default: 0
    """

    def Reset(self, value: bool = True, flags: enums.SetterFlags = 0):
        """
        If Yes, forces Reset of this RegControl.

        Name: `Reset`
        Default: False
        """
        self._lib.Obj_SetInt32(self._ptr, 29, value, flags)

    def _get_LDC_Z(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    def _set_LDC_Z(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 30, value, flags)

    LDC_Z = property(_get_LDC_Z, _set_LDC_Z) # type: float
    """
    Z value for Beckwith LDC_Z control option. Volts adjustment at rated control current.

    Name: `LDC_Z`
    Default: 0.0
    """

    def _get_Rev_Z(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    def _set_Rev_Z(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 31, value, flags)

    Rev_Z = property(_get_Rev_Z, _set_Rev_Z) # type: float
    """
    Reverse Z value for Beckwith LDC_Z control option.

    Name: `Rev_Z`
    Default: 0.0
    """

    def _get_Cogen(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 32) != 0

    def _set_Cogen(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 32, value, flags)

    Cogen = property(_get_Cogen, _set_Cogen) # type: bool
    """
    Cogen feature. When enabled, continues looking forward if power reverses, but switches to reverse-mode LDC, vreg and band values.
    Optionally, use the `Idle` property to specify if the regulator should idle in the "no-load region" (functionality typically described in the controller datasheet).

    Name: `Cogen`
    Default: False
    """

    def _get_Idle(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 33) != 0

    def _set_Idle(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 33, value, flags)

    Idle = property(_get_Idle, _set_Idle) # type: bool
    """
    Enabling this property only has an effect when reversible or cogen properties are set to `yes`/`true`. For the "no-load region" where active power flow lies between `-revThreshold` and `+revThreshold`, the regulator will lock taps in the position it had before entering that region. Voltage override (`VLimit`) takes priority.

    Name: `Idle`
    Default: False
    """

    def _get_IdleReverse(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 34) != 0

    def _set_IdleReverse(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 34, value, flags)

    IdleReverse = property(_get_IdleReverse, _set_IdleReverse) # type: bool
    """
    Similar to the `Idle` property but applicable only when `Reversible=Yes` (not for cogen mode) AND `RevNeutral=No`. When enabled, the regulator will lock taps in the position it had before entering the reverse flow zone.
    Voltage override (Vlimit) takes priority.

    Name: `IdleReverse`
    Default: False
    """

    def _get_IdleForward(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 35) != 0

    def _set_IdleForward(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 35, value, flags)

    IdleForward = property(_get_IdleForward, _set_IdleForward) # type: bool
    """
    Similar to the `Idle` property but applicable only when `Reversible=Yes` (not for cogen mode). When enabled, the regulator will lock taps in the position it had before entering the forward flow zone.
    Voltage override (`VLimit`) takes priority.

    Name: `IdleForward`
    Default: False
    """

    def _get_FwdThreshold(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    def _set_FwdThreshold(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 36, value, flags)

    FwdThreshold = property(_get_FwdThreshold, _set_FwdThreshold) # type: float
    """
    kW forward power threshold to use in tandem with `RevTheshold`.
    If `RevThreshold` is defined, the value of `FwdThreshold` is also updated for an even no-load band.

    If you require an uneven no-load zone band, set `FwdThreshold` after setting `RevThreshold`, or in the same DSS command (edit context).

    Name: `FwdThreshold`
    Units: kW
    Default: 100.0
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 37)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 37, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    Name: `BaseFreq`
    Units: Hz
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 38) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 38, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool
    """
    Indicates whether this element is enabled.

    Name: `Enabled`
    Default: True
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        **Deprecated:** `Like` has been deprecated since at least 2021, see https://sourceforge.net/p/electricdss/discussion/861977/thread/8b59d21eb6/#b57c/f668

        Name: `Like`
        """
        self._set_string_o(39, value)


class RegControlProperties(TypedDict):
    Transformer: Union[AnyStr, TransformerObj, AutoTrans]
    Winding: int
    VReg: float
    Band: float
    PTRatio: float
    CTPrim: float
    R: float
    X: float
    Bus: AnyStr
    Delay: float
    Reversible: bool
    RevVReg: float
    RevBand: float
    RevR: float
    RevX: float
    TapDelay: float
    DebugTrace: bool
    MaxTapChange: int
    InverseTime: bool
    TapWinding: int
    VLimit: float
    PTPhase: Union[AnyStr, int, enums.RegControlPhaseSelection]
    RevThreshold: float
    RevDelay: float
    RevNeutral: bool
    EventLog: bool
    RemotePTRatio: float
    TapNum: int
    Reset: bool
    LDC_Z: float
    Rev_Z: float
    Cogen: bool
    Idle: bool
    IdleReverse: bool
    IdleForward: bool
    FwdThreshold: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class RegControlBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'RegControl'
    _obj_cls = RegControl
    _cls_idx = 21
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[RegControlBatchProperties]) -> RegControlBatch:
        """
        Edit this RegControl batch.

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
        def __iter__(self) -> Iterator[RegControl]:
            yield from DSSBatch.__iter__(self)

    def _get_Transformer_str(self) -> List[str]:
        return self._get_batch_str_prop(1)

    def _set_Transformer_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Transformer_str = property(_get_Transformer_str, _set_Transformer_str) # type: List[str]
    """
    Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

    Transformer=Xfmr1

    Name: `Transformer`
    """

    def _get_Transformer(self) -> List[Union[TransformerObj, AutoTrans]]:
        return self._get_batch_obj_prop(1)

    def _set_Transformer(self, value: Union[AnyStr, TransformerObj, AutoTrans, List[AnyStr], List[Union[TransformerObj, AutoTrans]]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Transformer = property(_get_Transformer, _set_Transformer) # type: List[Union[TransformerObj, AutoTrans]]
    """
    Name of Transformer or AutoTrans element to which the RegControl is connected. Do not specify the full object name; "Transformer" or "AutoTrans" is assumed for the object class.  Example:

    Transformer=Xfmr1

    Name: `Transformer`
    """

    def _get_Winding(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 2)

    def _set_Winding(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Winding = property(_get_Winding, _set_Winding) # type: BatchInt32ArrayProxy
    """
    Number of the winding of the transformer element that the RegControl is monitoring. 1 or 2, typically.  Side Effect: Sets TAPWINDING property to the same winding.

    Name: `Winding`
    Default: 1
    """

    def _get_VReg(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 3)

    def _set_VReg(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    VReg = property(_get_VReg, _set_VReg) # type: BatchFloat64ArrayProxy
    """
    Voltage regulator setting for the winding being controlled.  Multiplying this value times the ptratio should yield the voltage across the WINDING of the controlled transformer.

    Name: `VReg`
    Units: V
    Default: 120.0
    """

    def _get_Band(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_Band(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    Band = property(_get_Band, _set_Band) # type: BatchFloat64ArrayProxy
    """
    Bandwidth in VOLTS for the controlled bus (see help for ptratio property).

    Name: `Band`
    Default: 3.0
    """

    def _get_PTRatio(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_PTRatio(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    PTRatio = property(_get_PTRatio, _set_PTRatio) # type: BatchFloat64ArrayProxy
    """
    Ratio of the PT that converts the controlled winding voltage to the regulator control voltage. If the winding is Wye, the line-to-neutral voltage is used.  Else, the line-to-line voltage is used. SIDE EFFECT: Also sets RemotePTRatio property.

    Name: `PTRatio`
    Default: 60.0
    """

    def _get_CTPrim(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 6)

    def _set_CTPrim(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(6, value, flags)

    CTPrim = property(_get_CTPrim, _set_CTPrim) # type: BatchFloat64ArrayProxy
    """
    Rating of the primary CT rating for which the line amps convert to control rated amps. The typical default secondary ampere rating is 0.2 Amps (check with manufacturer specs). Current at which the LDC voltages match the R and X settings.

    Name: `CTPrim`
    Units: A
    Default: 300.0
    """

    def _get_R(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 7)

    def _set_R(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    R = property(_get_R, _set_R) # type: BatchFloat64ArrayProxy
    """
    R setting on the line drop compensator in the regulator, expressed in VOLTS.

    Name: `R`
    Default: 0.0
    """

    def _get_X(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 8)

    def _set_X(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    X = property(_get_X, _set_X) # type: BatchFloat64ArrayProxy
    """
    X setting on the line drop compensator in the regulator, expressed in VOLTS.

    Name: `X`
    Default: 0.0
    """

    def _get_Bus(self) -> List[str]:
        return self._get_batch_str_prop(9)

    def _set_Bus(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    Bus = property(_get_Bus, _set_Bus) # type: List[str]
    """
    Name of a bus (busname.nodename) in the system to use as the controlled bus instead of the bus to which the transformer winding is connected or the R and X line drop compensator settings.  Do not specify this value if you wish to use the line drop compensator settings.  Default is null string. Assumes the base voltage for this bus is the same as the transformer winding base specified above. Note: This bus (1-phase) WILL BE CREATED by the regulator control upon SOLVE if not defined by some other device. You can specify the node of the bus you wish to sample (defaults to 1). If specified, the RegControl is redefined as a 1-phase device since only one voltage is used.

    Name: `Bus`
    """

    def _get_Delay(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 10)

    def _set_Delay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    Delay = property(_get_Delay, _set_Delay) # type: BatchFloat64ArrayProxy
    """
    Time delay from when the voltage goes out of band to when the tap changing begins. This is used to determine which regulator control will act first. You may specify any floating point number to achieve a model of whatever condition is necessary.

    Name: `Delay`
    Units: s
    Default: 15.0
    """

    def _get_Reversible(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(11)
        ]

    def _set_Reversible(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(11, value, flags)

    Reversible = property(_get_Reversible, _set_Reversible) # type: List[bool]
    """
    Indicates whether the regulator has a reverse operation mode (associated settings must be defined).
    Default is `No`, which means the regulator forward settings apply for both forward and reverse power flow.
    Typically applies only to line regulators and not to LTC on a substation transformer.

    Use the `RevNeutral`, `Idle`, `IdleReverse` and `IdleForward` properties to define the desired operating mode:
    - Bidirectional: `Reversible=yes`,`Idle=yes/no` (idling in the "no-load region" depends on the controller and is a functionality typically described in its datasheet)
    - Locked Forward: `Reversible=yes`, `IdleReverse=yes`
    - Reverse Idle: `Reversible=yes`, `Idle=yes`, `IdleReverse=yes`
    - Locked Reverse: `Reversible=yes`, `IdleForward=yes`
    - Neutral Idle: `Reversible=yes`, `RevNeutral=yes`, `Idle=yes/no` (idling in the "no-load region" depends on the controller and is a functionality typically described in its datasheet)

    Name: `Reversible`
    Default: False
    """

    def _get_RevVReg(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 12)

    def _set_RevVReg(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    RevVReg = property(_get_RevVReg, _set_RevVReg) # type: BatchFloat64ArrayProxy
    """
    Voltage setting in volts for operation in the reverse direction.

    Name: `RevVReg`
    Default: 120.0
    """

    def _get_RevBand(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_RevBand(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    RevBand = property(_get_RevBand, _set_RevBand) # type: BatchFloat64ArrayProxy
    """
    Bandwidth for operating in the reverse direction.

    Name: `RevBand`
    Default: 3.0
    """

    def _get_RevR(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 14)

    def _set_RevR(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    RevR = property(_get_RevR, _set_RevR) # type: BatchFloat64ArrayProxy
    """
    R line drop compensator setting for reverse direction.

    Name: `RevR`
    Default: 0.0
    """

    def _get_RevX(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 15)

    def _set_RevX(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    RevX = property(_get_RevX, _set_RevX) # type: BatchFloat64ArrayProxy
    """
    X line drop compensator setting for reverse direction.

    Name: `RevX`
    Default: 0.0
    """

    def _get_TapDelay(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 16)

    def _set_TapDelay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    TapDelay = property(_get_TapDelay, _set_TapDelay) # type: BatchFloat64ArrayProxy
    """
    Delay between tap changes. This is how long it takes between changes after the first change.

    Name: `TapDelay`
    Units: s
    Default: 2.0
    """

    def _get_DebugTrace(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(17)
        ]

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(17, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: List[bool]
    """
    Turn this on to capture the progress of the regulator model for each control iteration.  Creates a separate file for each RegControl named "REG_name.csv".

    Name: `DebugTrace`
    Default: False
    """

    def _get_MaxTapChange(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 18)

    def _set_MaxTapChange(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(18, value, flags)

    MaxTapChange = property(_get_MaxTapChange, _set_MaxTapChange) # type: BatchInt32ArrayProxy
    """
    Maximum allowable tap change per control iteration in STATIC control mode.

    Set this to 1 to better approximate actual control action. 

    Set this to 0 to fix the tap in the current position.

    Name: `MaxTapChange`
    Default: 16
    """

    def _get_InverseTime(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(19)
        ]

    def _set_InverseTime(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(19, value, flags)

    InverseTime = property(_get_InverseTime, _set_InverseTime) # type: List[bool]
    """
    The time delay is adjusted inversely proportional to the amount the voltage is outside the band down to 10%.

    Name: `InverseTime`
    Default: False
    """

    def _get_TapWinding(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 20)

    def _set_TapWinding(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(20, value, flags)

    TapWinding = property(_get_TapWinding, _set_TapWinding) # type: BatchInt32ArrayProxy
    """
    Winding containing the actual taps, if different than the WINDING property. Defaults to the same winding as specified by the WINDING property.

    Name: `TapWinding`
    """

    def _get_VLimit(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 21)

    def _set_VLimit(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    VLimit = property(_get_VLimit, _set_VLimit) # type: BatchFloat64ArrayProxy
    """
    Voltage Limit for bus to which regulated winding is connected (e.g. first customer). Set to a value greater then zero to activate this function.

    Name: `VLimit`
    Units: V
    Default: 0.0
    """

    def _get_PTPhase(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 22)

    def _set_PTPhase(self, value: Union[AnyStr, int, enums.RegControlPhaseSelection, List[AnyStr], List[int], List[enums.RegControlPhaseSelection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(22, value, flags)
            return

        self._set_batch_int32_array(22, value, flags)

    PTPhase = property(_get_PTPhase, _set_PTPhase) # type: BatchInt32ArrayProxy
    """
    For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Must be less than or equal to the number of phases. Ignored for regulated bus.

    Name: `PTPhase`
    Default: 1
    """

    def _get_PTPhase_str(self) -> List[str]:
        return self._get_batch_str_prop(22)

    def _set_PTPhase_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_PTPhase(value, flags)

    PTPhase_str = property(_get_PTPhase_str, _set_PTPhase_str) # type: List[str]
    """
    For multi-phase transformers, the number of the phase being monitored or one of { MAX | MIN} for all phases. Must be less than or equal to the number of phases. Ignored for regulated bus.

    Name: `PTPhase`
    Default: 1
    """

    def _get_RevThreshold(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 23)

    def _set_RevThreshold(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    RevThreshold = property(_get_RevThreshold, _set_RevThreshold) # type: BatchFloat64ArrayProxy
    """
    kW reverse power threshold for reversing the direction of the regulator.

    Defines a no-load band between `-RevThreshold` and `+RevThreshold`.

    **Important**: If an uneven band is desired, set `RevThreshold` to the desired lower bound (negative values allowed) and reset the upper bound using `FwdThreshold` right after.

    Name: `RevThreshold`
    Units: kW
    Default: -100.0
    """

    def _get_RevDelay(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 24)

    def _set_RevDelay(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    RevDelay = property(_get_RevDelay, _set_RevDelay) # type: BatchFloat64ArrayProxy
    """
    Time Delay for executing the reversing action once the threshold for reversing has been exceeded.

    Name: `RevDelay`
    Units: s
    Default: 60.0
    """

    def _get_RevNeutral(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(25)
        ]

    def _set_RevNeutral(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(25, value, flags)

    RevNeutral = property(_get_RevNeutral, _set_RevNeutral) # type: List[bool]
    """
    Set this to Yes if you want the regulator to go to neutral in the reverse direction or in cogen operation.

    Name: `RevNeutral`
    Default: False
    """

    def _get_EventLog(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(26)
        ]

    def _set_EventLog(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(26, value, flags)

    EventLog = property(_get_EventLog, _set_EventLog) # type: List[bool]
    """
    Log control actions to Eventlog.

    Name: `EventLog`
    Default: False
    """

    def _get_RemotePTRatio(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 27)

    def _set_RemotePTRatio(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    RemotePTRatio = property(_get_RemotePTRatio, _set_RemotePTRatio) # type: BatchFloat64ArrayProxy
    """
    When regulating a bus (the Bus= property is set), the PT ratio required to convert actual voltage at the remote bus to control voltage. Is initialized to PTratio property. Set this property after setting PTratio.

    Name: `RemotePTRatio`
    """

    def _get_TapNum(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 28)

    def _set_TapNum(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(28, value, flags)

    TapNum = property(_get_TapNum, _set_TapNum) # type: BatchInt32ArrayProxy
    """
    An integer number indicating the tap position that the controlled transformer winding tap position is currently at, or is being set to.  If being set, and the value is outside the range of the transformer min or max tap, then set to the min or max tap position as appropriate. Default is 0

    Name: `TapNum`
    Default: 0
    """

    def Reset(self, value: Union[bool, List[bool]] = True, flags: enums.SetterFlags = 0):
        """
        If Yes, forces Reset of this RegControl.

        Name: `Reset`
        Default: False
        """
        self._set_batch_int32_array(29, value, flags)

    def _get_LDC_Z(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 30)

    def _set_LDC_Z(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(30, value, flags)

    LDC_Z = property(_get_LDC_Z, _set_LDC_Z) # type: BatchFloat64ArrayProxy
    """
    Z value for Beckwith LDC_Z control option. Volts adjustment at rated control current.

    Name: `LDC_Z`
    Default: 0.0
    """

    def _get_Rev_Z(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 31)

    def _set_Rev_Z(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(31, value, flags)

    Rev_Z = property(_get_Rev_Z, _set_Rev_Z) # type: BatchFloat64ArrayProxy
    """
    Reverse Z value for Beckwith LDC_Z control option.

    Name: `Rev_Z`
    Default: 0.0
    """

    def _get_Cogen(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(32)
        ]

    def _set_Cogen(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(32, value, flags)

    Cogen = property(_get_Cogen, _set_Cogen) # type: List[bool]
    """
    Cogen feature. When enabled, continues looking forward if power reverses, but switches to reverse-mode LDC, vreg and band values.
    Optionally, use the `Idle` property to specify if the regulator should idle in the "no-load region" (functionality typically described in the controller datasheet).

    Name: `Cogen`
    Default: False
    """

    def _get_Idle(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(33)
        ]

    def _set_Idle(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(33, value, flags)

    Idle = property(_get_Idle, _set_Idle) # type: List[bool]
    """
    Enabling this property only has an effect when reversible or cogen properties are set to `yes`/`true`. For the "no-load region" where active power flow lies between `-revThreshold` and `+revThreshold`, the regulator will lock taps in the position it had before entering that region. Voltage override (`VLimit`) takes priority.

    Name: `Idle`
    Default: False
    """

    def _get_IdleReverse(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(34)
        ]

    def _set_IdleReverse(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(34, value, flags)

    IdleReverse = property(_get_IdleReverse, _set_IdleReverse) # type: List[bool]
    """
    Similar to the `Idle` property but applicable only when `Reversible=Yes` (not for cogen mode) AND `RevNeutral=No`. When enabled, the regulator will lock taps in the position it had before entering the reverse flow zone.
    Voltage override (Vlimit) takes priority.

    Name: `IdleReverse`
    Default: False
    """

    def _get_IdleForward(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(35)
        ]

    def _set_IdleForward(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(35, value, flags)

    IdleForward = property(_get_IdleForward, _set_IdleForward) # type: List[bool]
    """
    Similar to the `Idle` property but applicable only when `Reversible=Yes` (not for cogen mode). When enabled, the regulator will lock taps in the position it had before entering the forward flow zone.
    Voltage override (`VLimit`) takes priority.

    Name: `IdleForward`
    Default: False
    """

    def _get_FwdThreshold(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 36)

    def _set_FwdThreshold(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(36, value, flags)

    FwdThreshold = property(_get_FwdThreshold, _set_FwdThreshold) # type: BatchFloat64ArrayProxy
    """
    kW forward power threshold to use in tandem with `RevTheshold`.
    If `RevThreshold` is defined, the value of `FwdThreshold` is also updated for an even no-load band.

    If you require an uneven no-load zone band, set `FwdThreshold` after setting `RevThreshold`, or in the same DSS command (edit context).

    Name: `FwdThreshold`
    Units: kW
    Default: 100.0
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 37)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(37, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    Name: `BaseFreq`
    Units: Hz
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(38)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(38, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]
    """
    Indicates whether this element is enabled.

    Name: `Enabled`
    Default: True
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        **Deprecated:** `Like` has been deprecated since at least 2021, see https://sourceforge.net/p/electricdss/discussion/861977/thread/8b59d21eb6/#b57c/f668

        Name: `Like`
        """
        self._set_batch_string(39, value, flags)

class RegControlBatchProperties(TypedDict):
    Transformer: Union[AnyStr, TransformerObj, AutoTrans, List[AnyStr], List[Union[TransformerObj, AutoTrans]]]
    Winding: Union[int, Int32Array]
    VReg: Union[float, Float64Array]
    Band: Union[float, Float64Array]
    PTRatio: Union[float, Float64Array]
    CTPrim: Union[float, Float64Array]
    R: Union[float, Float64Array]
    X: Union[float, Float64Array]
    Bus: Union[AnyStr, List[AnyStr]]
    Delay: Union[float, Float64Array]
    Reversible: bool
    RevVReg: Union[float, Float64Array]
    RevBand: Union[float, Float64Array]
    RevR: Union[float, Float64Array]
    RevX: Union[float, Float64Array]
    TapDelay: Union[float, Float64Array]
    DebugTrace: bool
    MaxTapChange: Union[int, Int32Array]
    InverseTime: bool
    TapWinding: Union[int, Int32Array]
    VLimit: Union[float, Float64Array]
    PTPhase: Union[AnyStr, int, enums.RegControlPhaseSelection, List[AnyStr], List[int], List[enums.RegControlPhaseSelection], Int32Array]
    RevThreshold: Union[float, Float64Array]
    RevDelay: Union[float, Float64Array]
    RevNeutral: bool
    EventLog: bool
    RemotePTRatio: Union[float, Float64Array]
    TapNum: Union[int, Int32Array]
    Reset: bool
    LDC_Z: Union[float, Float64Array]
    Rev_Z: Union[float, Float64Array]
    Cogen: bool
    Idle: bool
    IdleReverse: bool
    IdleForward: bool
    FwdThreshold: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IRegControl(IDSSObj, RegControlBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, RegControl, RegControlBatch)
        RegControlBatch.__init__(self, self._api_util, sync_cls_idx=RegControl._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> RegControl:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> RegControlBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) RegControl objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[RegControl]:
            yield from RegControlBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[RegControlProperties]) -> RegControl:
        """
        Creates a new RegControl.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[RegControlBatchProperties]) -> RegControlBatch:
        """
        Creates a new batch of RegControl objects

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
