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
from .PCElement import PCElementBatchMixin, PCElementMixin
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin
from .DynamicExp import DynamicExp
from .LoadShape import LoadShape
from .Spectrum import Spectrum as SpectrumObj
from .XYcurve import XYcurve

class WindGen(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'WindGen'
    _cls_idx = 28
    _cls_int_idx = {
        1,
        6,
        10,
        12,
        13,
        27,
        28,
        29,
        30,
        32,
        45,
    }
    _cls_float_idx = {
        3,
        4,
        5,
        11,
        14,
        15,
        16,
        17,
        18,
        21,
        22,
        23,
        24,
        25,
        26,
        31,
        34,
        35,
        36,
        37,
        38,
        40,
        41,
        42,
        44,
    }
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'kw': 4,
        'pf': 5,
        'model': 6,
        'yearly': 7,
        'daily': 8,
        'duty': 9,
        'conn': 10,
        'kvar': 11,
        'cls': 12,
        'class': 12,
        'debugtrace': 13,
        'vminpu': 14,
        'vmaxpu': 15,
        'kva': 16,
        'mva': 17,
        'dutystart': 18,
        'dynamiceq': 19,
        'dynout': 20,
        'rthev': 21,
        'xthev': 22,
        'vss': 23,
        'pss': 24,
        'qss': 25,
        'vwind': 26,
        'qmode': 27,
        'simmechflg': 28,
        'apcflg': 29,
        'qflg': 30,
        'delt0': 31,
        'n_wtg': 32,
        'vv_curve': 33,
        'ag': 34,
        'cp': 35,
        'lamda': 36,
        'p': 37,
        'pd': 38,
        'ploss': 39,
        'rad': 40,
        'vcutin': 41,
        'vcutout': 42,
        'spectrum': 43,
        'basefreq': 44,
        'enabled': 45,
        'like': 46,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[WindGenProperties]) -> WindGen:
        """
        Edit this WindGen.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_Phases(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 1)

    def _set_Phases(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: int
    """
    Number of phases for this WindGen. Power is evenly divided among phases.

    Name: `Phases`
    Default: 3
    """

    def _get_Bus1(self) -> str:
        return self._get_prop_string(2)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str
    """
    Bus to which the WindGen is connected.  May include specific node specification.

    Name: `Bus1`
    """

    def _get_kV(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kV = property(_get_kV, _set_kV) # type: float
    """
    Nominal rated (1.0 per unit) voltage, kV, for WindGen. For 2- and 3-phase WindGens, specify phase-phase kV.
    Otherwise, for phases=1 or phases>3, specify actual kV across each branch of the WindGen.
    If wye (star), specify phase-neutral kV.
    If delta or phase-phase connected, specify phase-phase kV.

    Name: `kV`
    Units: kV
    Default: 12.47
    """

    def _get_kW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    kW = property(_get_kW, _set_kW) # type: float
    """
    Total base kW for the WindGen.
    A positive value denotes power coming OUT of the element, which is the opposite of a load. This value is modified depending on the dispatch mode.
    Unaffected by the global load multiplier and growth curves.
    If you want there to be more generation, you must add more WindGens or change this value.

    Name: `kW`
    Units: kW
    Default: 1000.0
    """

    def _get_PF(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_PF(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    PF = property(_get_PF, _set_PF) # type: float
    """
    WindGen power factor. Enter negative for leading powerfactor (when kW and kvar have opposite signs.)
    A positive power factor for a WindGen signifies that the WindGen produces vars as is typical for a synchronous WindGen.
    Induction machines would be generally specified with a negative power factor.

    Name: `PF`
    Default: 0.88
    """

    def _get_Model(self) -> enums.WindGenModel:
        return enums.WindGenModel(self._lib.Obj_GetInt32(self._ptr, 6))

    def _set_Model(self, value: Union[int, enums.WindGenModel], flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Model = property(_get_Model, _set_Model) # type: enums.WindGenModel
    """
    Integer code for the model to use for generation variation with voltage.
    Valid values are (**NOTE:** this is under review):
    1:WindGen injects a constant kW at specified power factor.
    2:WindGen is modeled as a constant admittance.
    4:Const kW, Fixed Q (Q never varies)
    5:Const kW, Fixed Q (as a constant reactance)

    Name: `Model`
    Default: 1
    """

    def _get_Yearly_str(self) -> str:
        return self._get_prop_string(7)

    def _set_Yearly_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(7, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: str
    """
    Wind speed shape to use for yearly-mode simulations.  Must be previously defined as a LoadShape object.
    If this is not specified, a constant value is assumed (no variation).
    Set to NONE to reset to no LoadShape.
    Nominally for 8760 simulations. If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

    Name: `Yearly`
    """

    def _get_Yearly(self) -> LoadShape:
        return self._get_obj(7, LoadShape)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(7, value, flags)
            return

        self._set_string_o(7, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: LoadShape
    """
    Wind speed shape to use for yearly-mode simulations.  Must be previously defined as a LoadShape object.
    If this is not specified, a constant value is assumed (no variation).
    Set to NONE to reset to no LoadShape.
    Nominally for 8760 simulations. If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

    Name: `Yearly`
    """

    def _get_Daily_str(self) -> str:
        return self._get_prop_string(8)

    def _set_Daily_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(8, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: str
    """
    Wind speed shape to use for daily-mode simulations. Must be previously defined as a LoadShape object of 24 hrs, typically.
    Set to NONE to reset to no LoadShape.

    Name: `Daily`
    """

    def _get_Daily(self) -> LoadShape:
        return self._get_obj(8, LoadShape)

    def _set_Daily(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(8, value, flags)
            return

        self._set_string_o(8, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: LoadShape
    """
    Wind speed shape to use for daily-mode simulations. Must be previously defined as a LoadShape object of 24 hrs, typically.
    Set to NONE to reset to no LoadShape.

    Name: `Daily`
    """

    def _get_Duty_str(self) -> str:
        return self._get_prop_string(9)

    def _set_Duty_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: str
    """
    Load shape to use for duty cycle dispatch simulations such as for wind or solar generation.
    Must be previously defined as a LoadShape object.
    Typically would have time intervals less than 1 hr -- perhaps, in seconds.
    Set to NONE to reset to no LoadShape.
    Designate the number of points to solve using the Set Number=xxxx command.
    If there are fewer points in the actual shape, the shape is assumed to repeat.

    Name: `Duty`
    """

    def _get_Duty(self) -> LoadShape:
        return self._get_obj(9, LoadShape)

    def _set_Duty(self, value: Union[AnyStr, LoadShape], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(9, value, flags)
            return

        self._set_string_o(9, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: LoadShape
    """
    Load shape to use for duty cycle dispatch simulations such as for wind or solar generation.
    Must be previously defined as a LoadShape object.
    Typically would have time intervals less than 1 hr -- perhaps, in seconds.
    Set to NONE to reset to no LoadShape.
    Designate the number of points to solve using the Set Number=xxxx command.
    If there are fewer points in the actual shape, the shape is assumed to repeat.

    Name: `Duty`
    """

    def _get_Conn(self) -> enums.Connection:
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 10))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(10, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection
    """
    ={wye|LN|delta|LL}. Default is wye.

    Name: `Conn`
    Default: Wye
    """

    def _get_Conn_str(self) -> str:
        return self._get_prop_string(10)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str
    """
    ={wye|LN|delta|LL}. Default is wye.

    Name: `Conn`
    Default: Wye
    """

    def _get_kvar(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_kvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: float
    """
    Specify the base kvar. Alternative to specifying the power factor.
    Side effect: the power factor value is altered to agree based on present value of kW.

    Name: `kvar`
    Units: kvar
    """

    def _get_Class(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 12)

    def _set_Class(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 12, value, flags)

    Class = property(_get_Class, _set_Class) # type: int
    """
    An arbitrary integer number representing the class of WindGen so that WindGen values may be segregated by class.

    Name: `Class`
    Default: 1
    """

    def _get_DebugTrace(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 13) != 0

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 13, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: bool
    """
    Turn this on to capture the progress of the WindGen model for each iteration.
    Creates a separate file for each WindGen named "WINDGEN_name.CSV".

    Name: `DebugTrace`
    Default: False
    """

    def _get_Vminpu(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_Vminpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    Vminpu = property(_get_Vminpu, _set_Vminpu) # type: float
    """
    Minimum per unit voltage for which the Model is assumed to apply. Below this value, the WindGen model reverts to a constant impedance model. For model 7, the current is limited to the value computed for constant power at VMinPU.

    Name: `Vminpu`
    Default: 0.9
    """

    def _get_Vmaxpu(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_Vmaxpu(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    Vmaxpu = property(_get_Vmaxpu, _set_Vmaxpu) # type: float
    """
    Maximum per unit voltage for which the Model is assumed to apply.
    Above this value, the WindGen model reverts to a constant impedance model.

    Name: `Vmaxpu`
    Default: 1.1
    """

    def _get_kVA(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_kVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: float
    """
    kVA rating of electrical machine. Defaults to 1.2 times "kW" if not specified. Applied to machine or inverter definition for Dynamics mode solutions. 

    Name: `kVA`
    """

    def _get_MVA(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_MVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    MVA = property(_get_MVA, _set_MVA) # type: float
    """
    MVA rating of electrical machine. Alternative to using the "kVA" property.

    Name: `MVA`
    """

    def _get_DutyStart(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    def _set_DutyStart(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 18, value, flags)

    DutyStart = property(_get_DutyStart, _set_DutyStart) # type: float
    """
    Starting time offset [hours] into the duty cycle shape for this WindGen.

    Name: `DutyStart`
    Units: hour
    Default: 0.0
    """

    def _get_DynamicEq_str(self) -> str:
        return self._get_prop_string(19)

    def _set_DynamicEq_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(19, value, flags)

    DynamicEq_str = property(_get_DynamicEq_str, _set_DynamicEq_str) # type: str
    """
    The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator.
    if not defined, the generator dynamics will follow the built-in dynamic equation.

    Name: `DynamicEq`
    """

    def _get_DynamicEq(self) -> DynamicExp:
        return self._get_obj(19, DynamicExp)

    def _set_DynamicEq(self, value: Union[AnyStr, DynamicExp], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(19, value, flags)
            return

        self._set_string_o(19, value, flags)

    DynamicEq = property(_get_DynamicEq, _set_DynamicEq) # type: DynamicExp
    """
    The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator.
    if not defined, the generator dynamics will follow the built-in dynamic equation.

    Name: `DynamicEq`
    """

    def _get_DynOut(self) -> List[str]:
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 20)

    def _set_DynOut(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, 20, value_ptr, value_count, flags)
        self._check_for_error()

    DynOut = property(_get_DynOut, _set_DynOut) # type: List[str]
    """
    The name of the variables within the Dynamic equation that will be used to govern the generator dynamics.
    This generator model requires 2 outputs from the dynamic equation: 
    1. Shaft speed (velocity) relative to synchronous speed.
    2. Shaft, or power, angle (relative to synchronous reference frame).
    The output variables need to be defined in the same order.

    Name: `DynOut`
    """

    def _get_RThev(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_RThev(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    RThev = property(_get_RThev, _set_RThev) # type: float
    """
    Per unit Thévenin equivalent R.

    Name: `RThev`
    Default: 0.0
    """

    def _get_XThev(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_XThev(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    XThev = property(_get_XThev, _set_XThev) # type: float
    """
    Per unit Thévenin equivalent X.

    Name: `XThev`
    Default: 0.05
    """

    def _get_VSS(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_VSS(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    VSS = property(_get_VSS, _set_VSS) # type: float
    """
    Steady state voltage magnitude.

    Name: `VSS`
    Units: pu (voltage)
    Default: 1.0
    """

    def _get_PSS(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_PSS(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    PSS = property(_get_PSS, _set_PSS) # type: float
    """
    Steady state output real power.

    Name: `PSS`
    Default: 1.0
    """

    def _get_QSS(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_QSS(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    QSS = property(_get_QSS, _set_QSS) # type: float
    """
    Steady state output reactive power.

    Name: `QSS`
    Default: 0.0
    """

    def _get_VWind(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_VWind(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    VWind = property(_get_VWind, _set_VWind) # type: float
    """
    Wind speed in m/s

    Name: `VWind`
    Default: 12.0
    """

    def _get_QMode(self) -> enums.WindGenQMode:
        return enums.WindGenQMode(self._lib.Obj_GetInt32(self._ptr, 27))

    def _set_QMode(self, value: Union[int, enums.WindGenQMode], flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 27, value, flags)

    QMode = property(_get_QMode, _set_QMode) # type: enums.WindGenQMode
    """
    Q control mode (0:Q, 1:PF, 2:VV).

    Name: `QMode`
    Default: 0
    """

    def _get_SimMechFlg(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 28)

    def _set_SimMechFlg(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 28, value, flags)

    SimMechFlg = property(_get_SimMechFlg, _set_SimMechFlg) # type: int
    """
    1 to simulate mechanical system. Otherwise (0) only uses the electrical system. For dynamics simulation purposes.

    Name: `SimMechFlg`
    Default: 1
    """

    def _get_APCFlg(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 29)

    def _set_APCFlg(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 29, value, flags)

    APCFlg = property(_get_APCFlg, _set_APCFlg) # type: int
    """
    1 to enable active power control.

    Name: `APCFlg`
    Default: 0
    """

    def _get_QFlg(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 30)

    def _set_QFlg(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 30, value, flags)

    QFlg = property(_get_QFlg, _set_QFlg) # type: int
    """
    1 to enable reactive power and voltage control.

    Name: `QFlg`
    Default: 1
    """

    def _get_delt0(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    def _set_delt0(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 31, value, flags)

    delt0 = property(_get_delt0, _set_delt0) # type: float
    """
    User defined internal simulation step.

    Name: `delt0`
    Default: 5e-05
    """

    def _get_N_WTG(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 32)

    def _set_N_WTG(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 32, value, flags)

    N_WTG = property(_get_N_WTG, _set_N_WTG) # type: int
    """
    Number of WTG in aggregation.

    Name: `N_WTG`
    Default: 1
    """

    def _get_VV_Curve_str(self) -> str:
        return self._get_prop_string(33)

    def _set_VV_Curve_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(33, value, flags)

    VV_Curve_str = property(_get_VV_Curve_str, _set_VV_Curve_str) # type: str
    """
    Name of the XY curve defining the control curve for implementing volt-var (VV) control with this inverter.

    Name: `VV_Curve`
    """

    def _get_VV_Curve(self) -> XYcurve:
        return self._get_obj(33, XYcurve)

    def _set_VV_Curve(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(33, value, flags)
            return

        self._set_string_o(33, value, flags)

    VV_Curve = property(_get_VV_Curve, _set_VV_Curve) # type: XYcurve
    """
    Name of the XY curve defining the control curve for implementing volt-var (VV) control with this inverter.

    Name: `VV_Curve`
    """

    def _get_Ag(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    def _set_Ag(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 34, value, flags)

    Ag = property(_get_Ag, _set_Ag) # type: float
    """
    Gearbox ratio.

    Name: `Ag`
    Default: 0.011111111111111112
    """

    def _get_Cp(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    def _set_Cp(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 35, value, flags)

    Cp = property(_get_Cp, _set_Cp) # type: float
    """
    Turbine performance coefficient.

    Name: `Cp`
    Default: 0.41
    """

    def _get_Lamda(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    def _set_Lamda(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 36, value, flags)

    Lamda = property(_get_Lamda, _set_Lamda) # type: float
    """
    Tip speed ratio.

    Name: `Lamda`
    Default: 7.95
    """

    def _get_P(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 37)

    def _set_P(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 37, value, flags)

    P = property(_get_P, _set_P) # type: float
    """
    Number of pole pairs of the induction generator.

    Name: `P`
    Default: 2.0
    """

    def _get_pd(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 38)

    def _set_pd(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 38, value, flags)

    pd = property(_get_pd, _set_pd) # type: float
    """
    Air density in kg/m3.

    Name: `pd`
    Default: 1.225
    """

    def _get_PLoss_str(self) -> str:
        return self._get_prop_string(39)

    def _set_PLoss_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(39, value, flags)

    PLoss_str = property(_get_PLoss_str, _set_PLoss_str) # type: str
    """
    Name of the XYCurve object describing the active power losses in pct versus the wind speed.

    Name: `PLoss`
    """

    def _get_PLoss(self) -> XYcurve:
        return self._get_obj(39, XYcurve)

    def _set_PLoss(self, value: Union[AnyStr, XYcurve], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(39, value, flags)
            return

        self._set_string_o(39, value, flags)

    PLoss = property(_get_PLoss, _set_PLoss) # type: XYcurve
    """
    Name of the XYCurve object describing the active power losses in pct versus the wind speed.

    Name: `PLoss`
    """

    def _get_Rad(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 40)

    def _set_Rad(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 40, value, flags)

    Rad = property(_get_Rad, _set_Rad) # type: float
    """
    Rotor radius in meters.

    Name: `Rad`
    Default: 40.0
    """

    def _get_VCutIn(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 41)

    def _set_VCutIn(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 41, value, flags)

    VCutIn = property(_get_VCutIn, _set_VCutIn) # type: float
    """
    Cut-in speed for the wind generator.

    Name: `VCutIn`
    Default: 5.0
    """

    def _get_VCutOut(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    def _set_VCutOut(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 42, value, flags)

    VCutOut = property(_get_VCutOut, _set_VCutOut) # type: float
    """
    Cut-out speed for the wind generator.

    Name: `VCutOut`
    Default: 23.0
    """

    def _get_Spectrum_str(self) -> str:
        return self._get_prop_string(43)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(43, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str
    """
    Name of harmonic voltage or current spectrum for this WindGen.
    Voltage behind Xd" for machine - default. Current injection for inverter.

    Name: `Spectrum`
    Default: defaultgen
    """

    def _get_Spectrum(self) -> SpectrumObj:
        return self._get_obj(43, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(43, value, flags)
            return

        self._set_string_o(43, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj
    """
    Name of harmonic voltage or current spectrum for this WindGen.
    Voltage behind Xd" for machine - default. Current injection for inverter.

    Name: `Spectrum`
    Default: defaultgen
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 44)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 44, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    Name: `BaseFreq`
    Units: Hz
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 45) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 45, value, flags)

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
        self._set_string_o(46, value)


class WindGenProperties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kV: float
    kW: float
    PF: float
    Model: Union[int, enums.WindGenModel]
    Yearly: Union[AnyStr, LoadShape]
    Daily: Union[AnyStr, LoadShape]
    Duty: Union[AnyStr, LoadShape]
    Conn: Union[AnyStr, int, enums.Connection]
    kvar: float
    Class: int
    DebugTrace: bool
    Vminpu: float
    Vmaxpu: float
    kVA: float
    MVA: float
    DutyStart: float
    DynamicEq: Union[AnyStr, DynamicExp]
    DynOut: List[AnyStr]
    RThev: float
    XThev: float
    VSS: float
    PSS: float
    QSS: float
    VWind: float
    QMode: Union[int, enums.WindGenQMode]
    SimMechFlg: int
    APCFlg: int
    QFlg: int
    delt0: float
    N_WTG: int
    VV_Curve: Union[AnyStr, XYcurve]
    Ag: float
    Cp: float
    Lamda: float
    P: float
    pd: float
    PLoss: Union[AnyStr, XYcurve]
    Rad: float
    VCutIn: float
    VCutOut: float
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class WindGenBatch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'WindGen'
    _obj_cls = WindGen
    _cls_idx = 28
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[WindGenBatchProperties]) -> WindGenBatch:
        """
        Edit this WindGen batch.

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
        def __iter__(self) -> Iterator[WindGen]:
            yield from DSSBatch.__iter__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy
    """
    Number of phases for this WindGen. Power is evenly divided among phases.

    Name: `Phases`
    Default: 3
    """

    def _get_Bus1(self) -> List[str]:
        return self._get_batch_str_prop(2)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]
    """
    Bus to which the WindGen is connected.  May include specific node specification.

    Name: `Bus1`
    """

    def _get_kV(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kV = property(_get_kV, _set_kV) # type: BatchFloat64ArrayProxy
    """
    Nominal rated (1.0 per unit) voltage, kV, for WindGen. For 2- and 3-phase WindGens, specify phase-phase kV.
    Otherwise, for phases=1 or phases>3, specify actual kV across each branch of the WindGen.
    If wye (star), specify phase-neutral kV.
    If delta or phase-phase connected, specify phase-phase kV.

    Name: `kV`
    Units: kV
    Default: 12.47
    """

    def _get_kW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    kW = property(_get_kW, _set_kW) # type: BatchFloat64ArrayProxy
    """
    Total base kW for the WindGen.
    A positive value denotes power coming OUT of the element, which is the opposite of a load. This value is modified depending on the dispatch mode.
    Unaffected by the global load multiplier and growth curves.
    If you want there to be more generation, you must add more WindGens or change this value.

    Name: `kW`
    Units: kW
    Default: 1000.0
    """

    def _get_PF(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_PF(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    PF = property(_get_PF, _set_PF) # type: BatchFloat64ArrayProxy
    """
    WindGen power factor. Enter negative for leading powerfactor (when kW and kvar have opposite signs.)
    A positive power factor for a WindGen signifies that the WindGen produces vars as is typical for a synchronous WindGen.
    Induction machines would be generally specified with a negative power factor.

    Name: `PF`
    Default: 0.88
    """

    def _get_Model(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 6)

    def _set_Model(self, value: Union[int, enums.WindGenModel, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(6, value, flags)

    Model = property(_get_Model, _set_Model) # type: BatchInt32ArrayProxy
    """
    Integer code for the model to use for generation variation with voltage.
    Valid values are (**NOTE:** this is under review):
    1:WindGen injects a constant kW at specified power factor.
    2:WindGen is modeled as a constant admittance.
    4:Const kW, Fixed Q (Q never varies)
    5:Const kW, Fixed Q (as a constant reactance)

    Name: `Model`
    Default: 1
    """

    def _get_Yearly_str(self) -> List[str]:
        return self._get_batch_str_prop(7)

    def _set_Yearly_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(7, value, flags)

    Yearly_str = property(_get_Yearly_str, _set_Yearly_str) # type: List[str]
    """
    Wind speed shape to use for yearly-mode simulations.  Must be previously defined as a LoadShape object.
    If this is not specified, a constant value is assumed (no variation).
    Set to NONE to reset to no LoadShape.
    Nominally for 8760 simulations. If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

    Name: `Yearly`
    """

    def _get_Yearly(self) -> List[LoadShape]:
        return self._get_batch_obj_prop(7)

    def _set_Yearly(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(7, value, flags)

    Yearly = property(_get_Yearly, _set_Yearly) # type: List[LoadShape]
    """
    Wind speed shape to use for yearly-mode simulations.  Must be previously defined as a LoadShape object.
    If this is not specified, a constant value is assumed (no variation).
    Set to NONE to reset to no LoadShape.
    Nominally for 8760 simulations. If there are fewer points in the designated shape than the number of points in the solution, the curve is repeated.

    Name: `Yearly`
    """

    def _get_Daily_str(self) -> List[str]:
        return self._get_batch_str_prop(8)

    def _set_Daily_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(8, value, flags)

    Daily_str = property(_get_Daily_str, _set_Daily_str) # type: List[str]
    """
    Wind speed shape to use for daily-mode simulations. Must be previously defined as a LoadShape object of 24 hrs, typically.
    Set to NONE to reset to no LoadShape.

    Name: `Daily`
    """

    def _get_Daily(self) -> List[LoadShape]:
        return self._get_batch_obj_prop(8)

    def _set_Daily(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(8, value, flags)

    Daily = property(_get_Daily, _set_Daily) # type: List[LoadShape]
    """
    Wind speed shape to use for daily-mode simulations. Must be previously defined as a LoadShape object of 24 hrs, typically.
    Set to NONE to reset to no LoadShape.

    Name: `Daily`
    """

    def _get_Duty_str(self) -> List[str]:
        return self._get_batch_str_prop(9)

    def _set_Duty_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    Duty_str = property(_get_Duty_str, _set_Duty_str) # type: List[str]
    """
    Load shape to use for duty cycle dispatch simulations such as for wind or solar generation.
    Must be previously defined as a LoadShape object.
    Typically would have time intervals less than 1 hr -- perhaps, in seconds.
    Set to NONE to reset to no LoadShape.
    Designate the number of points to solve using the Set Number=xxxx command.
    If there are fewer points in the actual shape, the shape is assumed to repeat.

    Name: `Duty`
    """

    def _get_Duty(self) -> List[LoadShape]:
        return self._get_batch_obj_prop(9)

    def _set_Duty(self, value: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(9, value, flags)

    Duty = property(_get_Duty, _set_Duty) # type: List[LoadShape]
    """
    Load shape to use for duty cycle dispatch simulations such as for wind or solar generation.
    Must be previously defined as a LoadShape object.
    Typically would have time intervals less than 1 hr -- perhaps, in seconds.
    Set to NONE to reset to no LoadShape.
    Designate the number of points to solve using the Set Number=xxxx command.
    If there are fewer points in the actual shape, the shape is assumed to repeat.

    Name: `Duty`
    """

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 10)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(10, value, flags)
            return

        self._set_batch_int32_array(10, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy
    """
    ={wye|LN|delta|LL}. Default is wye.

    Name: `Conn`
    Default: Wye
    """

    def _get_Conn_str(self) -> List[str]:
        return self._get_batch_str_prop(10)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]
    """
    ={wye|LN|delta|LL}. Default is wye.

    Name: `Conn`
    Default: Wye
    """

    def _get_kvar(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_kvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    kvar = property(_get_kvar, _set_kvar) # type: BatchFloat64ArrayProxy
    """
    Specify the base kvar. Alternative to specifying the power factor.
    Side effect: the power factor value is altered to agree based on present value of kW.

    Name: `kvar`
    Units: kvar
    """

    def _get_Class(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 12)

    def _set_Class(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(12, value, flags)

    Class = property(_get_Class, _set_Class) # type: BatchInt32ArrayProxy
    """
    An arbitrary integer number representing the class of WindGen so that WindGen values may be segregated by class.

    Name: `Class`
    Default: 1
    """

    def _get_DebugTrace(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(13)
        ]

    def _set_DebugTrace(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(13, value, flags)

    DebugTrace = property(_get_DebugTrace, _set_DebugTrace) # type: List[bool]
    """
    Turn this on to capture the progress of the WindGen model for each iteration.
    Creates a separate file for each WindGen named "WINDGEN_name.CSV".

    Name: `DebugTrace`
    Default: False
    """

    def _get_Vminpu(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 14)

    def _set_Vminpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    Vminpu = property(_get_Vminpu, _set_Vminpu) # type: BatchFloat64ArrayProxy
    """
    Minimum per unit voltage for which the Model is assumed to apply. Below this value, the WindGen model reverts to a constant impedance model. For model 7, the current is limited to the value computed for constant power at VMinPU.

    Name: `Vminpu`
    Default: 0.9
    """

    def _get_Vmaxpu(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 15)

    def _set_Vmaxpu(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    Vmaxpu = property(_get_Vmaxpu, _set_Vmaxpu) # type: BatchFloat64ArrayProxy
    """
    Maximum per unit voltage for which the Model is assumed to apply.
    Above this value, the WindGen model reverts to a constant impedance model.

    Name: `Vmaxpu`
    Default: 1.1
    """

    def _get_kVA(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 16)

    def _set_kVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: BatchFloat64ArrayProxy
    """
    kVA rating of electrical machine. Defaults to 1.2 times "kW" if not specified. Applied to machine or inverter definition for Dynamics mode solutions. 

    Name: `kVA`
    """

    def _get_MVA(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 17)

    def _set_MVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    MVA = property(_get_MVA, _set_MVA) # type: BatchFloat64ArrayProxy
    """
    MVA rating of electrical machine. Alternative to using the "kVA" property.

    Name: `MVA`
    """

    def _get_DutyStart(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 18)

    def _set_DutyStart(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(18, value, flags)

    DutyStart = property(_get_DutyStart, _set_DutyStart) # type: BatchFloat64ArrayProxy
    """
    Starting time offset [hours] into the duty cycle shape for this WindGen.

    Name: `DutyStart`
    Units: hour
    Default: 0.0
    """

    def _get_DynamicEq_str(self) -> List[str]:
        return self._get_batch_str_prop(19)

    def _set_DynamicEq_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(19, value, flags)

    DynamicEq_str = property(_get_DynamicEq_str, _set_DynamicEq_str) # type: List[str]
    """
    The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator.
    if not defined, the generator dynamics will follow the built-in dynamic equation.

    Name: `DynamicEq`
    """

    def _get_DynamicEq(self) -> List[DynamicExp]:
        return self._get_batch_obj_prop(19)

    def _set_DynamicEq(self, value: Union[AnyStr, DynamicExp, List[AnyStr], List[DynamicExp]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(19, value, flags)

    DynamicEq = property(_get_DynamicEq, _set_DynamicEq) # type: List[DynamicExp]
    """
    The name of the dynamic equation (DynamicExp) that will be used for defining the dynamic behavior of the generator.
    if not defined, the generator dynamics will follow the built-in dynamic equation.

    Name: `DynamicEq`
    """

    def _get_DynOut(self) -> List[List[str]]:
        return self._get_string_ll(20)

    def _set_DynOut(self, value: List[AnyStr], flags: enums.SetterFlags = 0):
        value, value_ptr, value_count = self._prepare_string_array(value)
        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, 20, value_ptr, value_count, flags)

        self._check_for_error()

    DynOut = property(_get_DynOut, _set_DynOut) # type: List[List[str]]
    """
    The name of the variables within the Dynamic equation that will be used to govern the generator dynamics.
    This generator model requires 2 outputs from the dynamic equation: 
    1. Shaft speed (velocity) relative to synchronous speed.
    2. Shaft, or power, angle (relative to synchronous reference frame).
    The output variables need to be defined in the same order.

    Name: `DynOut`
    """

    def _get_RThev(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 21)

    def _set_RThev(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    RThev = property(_get_RThev, _set_RThev) # type: BatchFloat64ArrayProxy
    """
    Per unit Thévenin equivalent R.

    Name: `RThev`
    Default: 0.0
    """

    def _get_XThev(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 22)

    def _set_XThev(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    XThev = property(_get_XThev, _set_XThev) # type: BatchFloat64ArrayProxy
    """
    Per unit Thévenin equivalent X.

    Name: `XThev`
    Default: 0.05
    """

    def _get_VSS(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 23)

    def _set_VSS(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    VSS = property(_get_VSS, _set_VSS) # type: BatchFloat64ArrayProxy
    """
    Steady state voltage magnitude.

    Name: `VSS`
    Units: pu (voltage)
    Default: 1.0
    """

    def _get_PSS(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 24)

    def _set_PSS(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    PSS = property(_get_PSS, _set_PSS) # type: BatchFloat64ArrayProxy
    """
    Steady state output real power.

    Name: `PSS`
    Default: 1.0
    """

    def _get_QSS(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 25)

    def _set_QSS(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    QSS = property(_get_QSS, _set_QSS) # type: BatchFloat64ArrayProxy
    """
    Steady state output reactive power.

    Name: `QSS`
    Default: 0.0
    """

    def _get_VWind(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 26)

    def _set_VWind(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    VWind = property(_get_VWind, _set_VWind) # type: BatchFloat64ArrayProxy
    """
    Wind speed in m/s

    Name: `VWind`
    Default: 12.0
    """

    def _get_QMode(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 27)

    def _set_QMode(self, value: Union[int, enums.WindGenQMode, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(27, value, flags)

    QMode = property(_get_QMode, _set_QMode) # type: BatchInt32ArrayProxy
    """
    Q control mode (0:Q, 1:PF, 2:VV).

    Name: `QMode`
    Default: 0
    """

    def _get_SimMechFlg(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 28)

    def _set_SimMechFlg(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(28, value, flags)

    SimMechFlg = property(_get_SimMechFlg, _set_SimMechFlg) # type: BatchInt32ArrayProxy
    """
    1 to simulate mechanical system. Otherwise (0) only uses the electrical system. For dynamics simulation purposes.

    Name: `SimMechFlg`
    Default: 1
    """

    def _get_APCFlg(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 29)

    def _set_APCFlg(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(29, value, flags)

    APCFlg = property(_get_APCFlg, _set_APCFlg) # type: BatchInt32ArrayProxy
    """
    1 to enable active power control.

    Name: `APCFlg`
    Default: 0
    """

    def _get_QFlg(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 30)

    def _set_QFlg(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(30, value, flags)

    QFlg = property(_get_QFlg, _set_QFlg) # type: BatchInt32ArrayProxy
    """
    1 to enable reactive power and voltage control.

    Name: `QFlg`
    Default: 1
    """

    def _get_delt0(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 31)

    def _set_delt0(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(31, value, flags)

    delt0 = property(_get_delt0, _set_delt0) # type: BatchFloat64ArrayProxy
    """
    User defined internal simulation step.

    Name: `delt0`
    Default: 5e-05
    """

    def _get_N_WTG(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 32)

    def _set_N_WTG(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(32, value, flags)

    N_WTG = property(_get_N_WTG, _set_N_WTG) # type: BatchInt32ArrayProxy
    """
    Number of WTG in aggregation.

    Name: `N_WTG`
    Default: 1
    """

    def _get_VV_Curve_str(self) -> List[str]:
        return self._get_batch_str_prop(33)

    def _set_VV_Curve_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(33, value, flags)

    VV_Curve_str = property(_get_VV_Curve_str, _set_VV_Curve_str) # type: List[str]
    """
    Name of the XY curve defining the control curve for implementing volt-var (VV) control with this inverter.

    Name: `VV_Curve`
    """

    def _get_VV_Curve(self) -> List[XYcurve]:
        return self._get_batch_obj_prop(33)

    def _set_VV_Curve(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(33, value, flags)

    VV_Curve = property(_get_VV_Curve, _set_VV_Curve) # type: List[XYcurve]
    """
    Name of the XY curve defining the control curve for implementing volt-var (VV) control with this inverter.

    Name: `VV_Curve`
    """

    def _get_Ag(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 34)

    def _set_Ag(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(34, value, flags)

    Ag = property(_get_Ag, _set_Ag) # type: BatchFloat64ArrayProxy
    """
    Gearbox ratio.

    Name: `Ag`
    Default: 0.011111111111111112
    """

    def _get_Cp(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 35)

    def _set_Cp(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(35, value, flags)

    Cp = property(_get_Cp, _set_Cp) # type: BatchFloat64ArrayProxy
    """
    Turbine performance coefficient.

    Name: `Cp`
    Default: 0.41
    """

    def _get_Lamda(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 36)

    def _set_Lamda(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(36, value, flags)

    Lamda = property(_get_Lamda, _set_Lamda) # type: BatchFloat64ArrayProxy
    """
    Tip speed ratio.

    Name: `Lamda`
    Default: 7.95
    """

    def _get_P(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 37)

    def _set_P(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(37, value, flags)

    P = property(_get_P, _set_P) # type: BatchFloat64ArrayProxy
    """
    Number of pole pairs of the induction generator.

    Name: `P`
    Default: 2.0
    """

    def _get_pd(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 38)

    def _set_pd(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(38, value, flags)

    pd = property(_get_pd, _set_pd) # type: BatchFloat64ArrayProxy
    """
    Air density in kg/m3.

    Name: `pd`
    Default: 1.225
    """

    def _get_PLoss_str(self) -> List[str]:
        return self._get_batch_str_prop(39)

    def _set_PLoss_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(39, value, flags)

    PLoss_str = property(_get_PLoss_str, _set_PLoss_str) # type: List[str]
    """
    Name of the XYCurve object describing the active power losses in pct versus the wind speed.

    Name: `PLoss`
    """

    def _get_PLoss(self) -> List[XYcurve]:
        return self._get_batch_obj_prop(39)

    def _set_PLoss(self, value: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(39, value, flags)

    PLoss = property(_get_PLoss, _set_PLoss) # type: List[XYcurve]
    """
    Name of the XYCurve object describing the active power losses in pct versus the wind speed.

    Name: `PLoss`
    """

    def _get_Rad(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 40)

    def _set_Rad(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(40, value, flags)

    Rad = property(_get_Rad, _set_Rad) # type: BatchFloat64ArrayProxy
    """
    Rotor radius in meters.

    Name: `Rad`
    Default: 40.0
    """

    def _get_VCutIn(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 41)

    def _set_VCutIn(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(41, value, flags)

    VCutIn = property(_get_VCutIn, _set_VCutIn) # type: BatchFloat64ArrayProxy
    """
    Cut-in speed for the wind generator.

    Name: `VCutIn`
    Default: 5.0
    """

    def _get_VCutOut(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 42)

    def _set_VCutOut(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(42, value, flags)

    VCutOut = property(_get_VCutOut, _set_VCutOut) # type: BatchFloat64ArrayProxy
    """
    Cut-out speed for the wind generator.

    Name: `VCutOut`
    Default: 23.0
    """

    def _get_Spectrum_str(self) -> List[str]:
        return self._get_batch_str_prop(43)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(43, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]
    """
    Name of harmonic voltage or current spectrum for this WindGen.
    Voltage behind Xd" for machine - default. Current injection for inverter.

    Name: `Spectrum`
    Default: defaultgen
    """

    def _get_Spectrum(self) -> List[SpectrumObj]:
        return self._get_batch_obj_prop(43)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(43, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]
    """
    Name of harmonic voltage or current spectrum for this WindGen.
    Voltage behind Xd" for machine - default. Current injection for inverter.

    Name: `Spectrum`
    Default: defaultgen
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 44)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(44, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    Name: `BaseFreq`
    Units: Hz
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(45)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(45, value, flags)

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
        self._set_batch_string(46, value, flags)

class WindGenBatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kV: Union[float, Float64Array]
    kW: Union[float, Float64Array]
    PF: Union[float, Float64Array]
    Model: Union[int, enums.WindGenModel, Int32Array]
    Yearly: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Daily: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Duty: Union[AnyStr, LoadShape, List[AnyStr], List[LoadShape]]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    kvar: Union[float, Float64Array]
    Class: Union[int, Int32Array]
    DebugTrace: bool
    Vminpu: Union[float, Float64Array]
    Vmaxpu: Union[float, Float64Array]
    kVA: Union[float, Float64Array]
    MVA: Union[float, Float64Array]
    DutyStart: Union[float, Float64Array]
    DynamicEq: Union[AnyStr, DynamicExp, List[AnyStr], List[DynamicExp]]
    DynOut: List[AnyStr]
    RThev: Union[float, Float64Array]
    XThev: Union[float, Float64Array]
    VSS: Union[float, Float64Array]
    PSS: Union[float, Float64Array]
    QSS: Union[float, Float64Array]
    VWind: Union[float, Float64Array]
    QMode: Union[int, enums.WindGenQMode, Int32Array]
    SimMechFlg: Union[int, Int32Array]
    APCFlg: Union[int, Int32Array]
    QFlg: Union[int, Int32Array]
    delt0: Union[float, Float64Array]
    N_WTG: Union[int, Int32Array]
    VV_Curve: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    Ag: Union[float, Float64Array]
    Cp: Union[float, Float64Array]
    Lamda: Union[float, Float64Array]
    P: Union[float, Float64Array]
    pd: Union[float, Float64Array]
    PLoss: Union[AnyStr, XYcurve, List[AnyStr], List[XYcurve]]
    Rad: Union[float, Float64Array]
    VCutIn: Union[float, Float64Array]
    VCutOut: Union[float, Float64Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IWindGen(IDSSObj, WindGenBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, WindGen, WindGenBatch)
        WindGenBatch.__init__(self, self._api_util, sync_cls_idx=WindGen._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> WindGen:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> WindGenBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) WindGen objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[WindGen]:
            yield from WindGenBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[WindGenProperties]) -> WindGen:
        """
        Creates a new WindGen.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[WindGenBatchProperties]) -> WindGenBatch:
        """
        Creates a new batch of WindGen objects

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
