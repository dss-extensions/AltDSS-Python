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
from .Spectrum import Spectrum as SpectrumObj

class Generic5(DSSObj, CircuitElementMixin, PCElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots + PCElementMixin._extra_slots
    _cls_name = 'Generic5'
    _cls_idx = 52
    _cls_int_idx = {
        1,
        6,
        16,
        18,
        19,
        28,
        37,
        40,
        43,
    }
    _cls_float_idx = {
        3,
        4,
        5,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        17,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        38,
        39,
        42,
    }
    _cls_prop_idx = {
        'phases': 1,
        'bus1': 2,
        'kv': 3,
        'kw': 4,
        'pf': 5,
        'conn': 6,
        'kva': 7,
        'p_ref1kw': 8,
        'p_ref2kw': 9,
        'p_ref3kw': 10,
        'v_ref1kvln': 11,
        'v_ref2kvln': 12,
        'v_ref3kvln': 13,
        'p_refkw': 14,
        'q_refkvar': 15,
        'cluster_num': 16,
        'v_refkvln': 17,
        'ctrl_mode': 18,
        'qv_flag': 19,
        'kcd': 20,
        'kcq': 21,
        'kqi': 22,
        'q_ref1kvar': 23,
        'q_ref2kvar': 24,
        'q_ref3kvar': 25,
        'pmaxkw': 26,
        'pminkw': 27,
        'pqpriority': 28,
        'pmppkw': 29,
        'pfctr1': 30,
        'pfctr2': 31,
        'pfctr3': 32,
        'pfctr4': 33,
        'pfctr5': 34,
        'pfctr6': 35,
        'pbiaskw': 36,
        'cc_switch': 37,
        'kcq_drp2': 38,
        'volt_trhd': 39,
        'droop': 40,
        'spectrum': 41,
        'basefreq': 42,
        'enabled': 43,
        'like': 44,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)
       PCElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[Generic5Properties]) -> Generic5:
        """
        Edit this Generic5.

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
    Number of Phases, this Induction Machine.  

    Name: `Phases`
    Default: 3
    """

    def _get_Bus1(self) -> str:
        return self._get_prop_string(2)

    def _set_Bus1(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: str
    """
    Bus to which the Induction Machine is connected.  May include specific node specification.

    Name: `Bus1`
    """

    def _get_kV(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kV(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kV = property(_get_kV, _set_kV) # type: float
    """
    Nominal rated (1.0 per unit) voltage, kV. For 2- and 3-phase machines, specify phase-phase kV. Otherwise, specify actual kV across each branch of the machine. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

    Name: `kV`
    Default: 12.47
    """

    def _get_kW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    kW = property(_get_kW, _set_kW) # type: float
    """
    Shaft Power, kW, for the Induction Machine. Output limit of a DG

    Name: `kW`
    Default: -0.001
    """

    def _get_PF(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 5)

    def _set_PF(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 5, value, flags)

    PF = property(_get_PF, _set_PF) # type: float
    """
    Present power factor for the machine. 

    **Read-only**

    Name: `PF`
    """

    def _get_Conn(self) -> enums.Connection:
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 6))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(6, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection
    """
    Connection of stator: Delta or Wye. Default is Delta.

    Name: `Conn`
    Default: Delta
    """

    def _get_Conn_str(self) -> str:
        return self._get_prop_string(6)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str
    """
    Connection of stator: Delta or Wye. Default is Delta.

    Name: `Conn`
    Default: Delta
    """

    def _get_kVA(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    def _set_kVA(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 7, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: float
    """
    Rated kVA for the machine.

    Name: `kVA`
    Default: -0.0012
    """

    def _get_P_Ref1kW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    def _set_P_Ref1kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 8, value, flags)

    P_Ref1kW = property(_get_P_Ref1kW, _set_P_Ref1kW) # type: float
    """
    P_ref1kW = 10, goes to P_ref1, unit kW, 1st phase set power

    Name: `P_Ref1kW`
    Default: 0.0
    """

    def _get_P_Ref2kW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    def _set_P_Ref2kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 9, value, flags)

    P_Ref2kW = property(_get_P_Ref2kW, _set_P_Ref2kW) # type: float
    """
    P_ref2kW = 10, goes to P_ref2, unit kW, 2nd phase set power

    Name: `P_Ref2kW`
    Default: 0.0
    """

    def _get_P_Ref3kW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    def _set_P_Ref3kW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 10, value, flags)

    P_Ref3kW = property(_get_P_Ref3kW, _set_P_Ref3kW) # type: float
    """
    P_ref3kW = 10, goes to P_ref3, unit kW, 3rd phase set power

    Name: `P_Ref3kW`
    Default: 0.0
    """

    def _get_V_Ref1kVLN(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_V_Ref1kVLN(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    V_Ref1kVLN = property(_get_V_Ref1kVLN, _set_V_Ref1kVLN) # type: float
    """
    V_ref1kVLN = 2.16, 1st phase set V, (Unit kV, L-N value): V mode will work if QV_flag =1(by default) V_ref is set which is prior to Q_ref 

    Name: `V_Ref1kVLN`
    Default: 0.0
    """

    def _get_V_Ref2kVLN(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_V_Ref2kVLN(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    V_Ref2kVLN = property(_get_V_Ref2kVLN, _set_V_Ref2kVLN) # type: float
    """
    V_ref2kVLN = 2.16, 2nd phase set V, (Unit kV, L-N value): V mode will work if QV_flag =1(by default) V_ref is set which is prior to Q_ref 

    Name: `V_Ref2kVLN`
    Default: 0.0
    """

    def _get_V_Ref3kVLN(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_V_Ref3kVLN(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    V_Ref3kVLN = property(_get_V_Ref3kVLN, _set_V_Ref3kVLN) # type: float
    """
    V_ref3kVLN = 2.16, 3rd phase set V, (Unit kV, L-N value): V mode will work if QV_flag =1(by default) V_ref is set which is prior to Q_ref 

    Name: `V_Ref3kVLN`
    Default: 0.0
    """

    def _get_P_RefkW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 14)

    def _set_P_RefkW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 14, value, flags)

    P_RefkW = property(_get_P_RefkW, _set_P_RefkW) # type: float
    """
    P_refkW = 10, goes to P_ref. Ref P Value (kW). P_ref has priority to kW which is nominal value. (Incide variable P_ref is W)

    Name: `P_RefkW`
    Default: 0.0
    """

    def _get_Q_RefkVAr(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 15)

    def _set_Q_RefkVAr(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 15, value, flags)

    Q_RefkVAr = property(_get_Q_RefkVAr, _set_Q_RefkVAr) # type: float
    """
    Q_refkVAr=10. Unit Qvar. Ref Q kVAr Value: work only when V_ref is not set

    Name: `Q_RefkVAr`
    Default: 0.0
    """

    def _get_Cluster_Num(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 16)

    def _set_Cluster_Num(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 16, value, flags)

    Cluster_Num = property(_get_Cluster_Num, _set_Cluster_Num) # type: int
    """
    Cluster_num: has to be coincident with Fmonitor attached. Default value is 0

    Name: `Cluster_Num`
    Default: 0
    """

    def _get_V_refkVLN(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    def _set_V_refkVLN(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 17, value, flags)

    V_refkVLN = property(_get_V_refkVLN, _set_V_refkVLN) # type: float
    """
    V_refkVLN = 2.16, pos sequence set V. V_ref (Unit kV, L-N value): V mode will work if QV_flag =1(by default) V_ref is set which is prior to Q_ref

    Name: `V_refkVLN`
    Default: 0.001
    """

    def _get_Ctrl_Mode(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 18)

    def _set_Ctrl_Mode(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 18, value, flags)

    Ctrl_Mode = property(_get_Ctrl_Mode, _set_Ctrl_Mode) # type: int
    """
    ctrl mode:     /// contrl mode     ///    ctrl_mode =0; phases = 3;  // pos avg control---p_ref, V_ref, Q_ref    \\n 
     ///    ctrl_mode =1; phases = 1; bus1 = 452.1;      ---p_ref1, V_ref1, Q_ref1 \\n
    ///    ctrl_mode =2; phases = 1; bus1 = 452.2;      ---p_ref2, V_ref2, Q_ref2 \\n
    ///    ctrl_mode =3; phases = 1; bus1 = 452.3;      ---p_ref3, V_ref3, Q_ref3 \\n
    ///    ctrl_mode =4; phases = 3; bus1 = 452.2;      ---p_ref1,2,3, V_ref1,2,3, Q_ref1,2,3

    Name: `Ctrl_Mode`
    Default: 0
    """

    def _get_QV_flag(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 19)

    def _set_QV_flag(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 19, value, flags)

    QV_flag = property(_get_QV_flag, _set_QV_flag) # type: int
    """
    QV_flag : 0-Q_ref mode; 1- V_ref mode

    Name: `QV_flag`
    Default: 0
    """

    def _get_kcd(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 20)

    def _set_kcd(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 20, value, flags)

    kcd = property(_get_kcd, _set_kcd) # type: float
    """
    kcd: Idi control gain

    Name: `kcd`
    Default: 0.1
    """

    def _get_kcq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 21)

    def _set_kcq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 21, value, flags)

    kcq = property(_get_kcq, _set_kcq) # type: float
    """
    kcq: Iqi control gain to delta V

    Name: `kcq`
    Default: 0.1
    """

    def _get_kqi(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_kqi(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    kqi = property(_get_kqi, _set_kqi) # type: float
    """
    kqi: Iqi control gain to delta Q

    Name: `kqi`
    Default: 0.1
    """

    def _get_Q_ref1kvar(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 23)

    def _set_Q_ref1kvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 23, value, flags)

    Q_ref1kvar = property(_get_Q_ref1kvar, _set_Q_ref1kvar) # type: float
    """
    Q_ref1kVAr=10. Unit Qvar. Ref Q kVAr Value: work only when V_ref is not set

    Name: `Q_ref1kvar`
    Default: 0.0
    """

    def _get_Q_ref2kvar(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 24)

    def _set_Q_ref2kvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 24, value, flags)

    Q_ref2kvar = property(_get_Q_ref2kvar, _set_Q_ref2kvar) # type: float
    """
    Q_ref2kVAr=10. Unit Qvar. Ref Q kVAr Value: work only when V_ref is not set

    Name: `Q_ref2kvar`
    Default: 0.0
    """

    def _get_Q_ref3kvar(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 25)

    def _set_Q_ref3kvar(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 25, value, flags)

    Q_ref3kvar = property(_get_Q_ref3kvar, _set_Q_ref3kvar) # type: float
    """
    Q_ref3kVAr=10. Unit Qvar. Ref Q kVAr Value: work only when V_ref is not set

    Name: `Q_ref3kvar`
    Default: 0.0
    """

    def _get_PMaxkW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    def _set_PMaxkW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 26, value, flags)

    PMaxkW = property(_get_PMaxkW, _set_PMaxkW) # type: float
    """
    PmaxkW = 100, goes to Pmax, unit kW, set max active power output; Operation limit of active power for DG
      Pmax should be less than or equal to kW

    Name: `PMaxkW`
    Default: -0.001
    """

    def _get_PMinkW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    def _set_PMinkW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 27, value, flags)

    PMinkW = property(_get_PMinkW, _set_PMinkW) # type: float
    """
    PminkW = 10, goes to Pmin, unit kW; Operation limit of active power for DG

    Name: `PMinkW`
    Default: 0.0
    """

    def _get_PQPriority(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 28)

    def _set_PQPriority(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 28, value, flags)

    PQPriority = property(_get_PQPriority, _set_PQPriority) # type: int
    """
    PQpriority, goes to PQpriority, define how to set Qmax. 0: Q,1: P 

    Name: `PQPriority`
    Default: 1
    """

    def _get_PmppkW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 29)

    def _set_PmppkW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 29, value, flags)

    PmppkW = property(_get_PmppkW, _set_PmppkW) # type: float
    """
    PmppkW = 100, goes to Pmpp, unit kW, input Pmpp to calculate kW;
      kW := (Pmpp + Pbias)*Pfctr1*Pfctr2*Pfctr3*Pfctr4*Pfctr5*Pfctr6;
    Pbias = 0 by default, Pfctr*=1 by default; These properties will overwrite kW.

    Name: `PmppkW`
    Default: 0.001
    """

    def _get_Pfctr1(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 30)

    def _set_Pfctr1(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 30, value, flags)

    Pfctr1 = property(_get_Pfctr1, _set_Pfctr1) # type: float
    """
    Pfctr1 = 0.16, see PmppkW

    Name: `Pfctr1`
    Default: 1.0
    """

    def _get_Pfctr2(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    def _set_Pfctr2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 31, value, flags)

    Pfctr2 = property(_get_Pfctr2, _set_Pfctr2) # type: float
    """
    Pfctr2 = 1, 1 by default, see PmppkW

    Name: `Pfctr2`
    Default: 1.0
    """

    def _get_Pfctr3(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    def _set_Pfctr3(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 32, value, flags)

    Pfctr3 = property(_get_Pfctr3, _set_Pfctr3) # type: float
    """
    Pfctr3 = 1, 1 by default, see PmppkW

    Name: `Pfctr3`
    Default: 1.0
    """

    def _get_Pfctr4(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    def _set_Pfctr4(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 33, value, flags)

    Pfctr4 = property(_get_Pfctr4, _set_Pfctr4) # type: float
    """
    Pfctr4= 1, 1 by default, see PmppkW

    Name: `Pfctr4`
    Default: 1.0
    """

    def _get_Pfctr5(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    def _set_Pfctr5(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 34, value, flags)

    Pfctr5 = property(_get_Pfctr5, _set_Pfctr5) # type: float
    """
    Pfctr5 =1, 1 by default, see PmppkW

    Name: `Pfctr5`
    Default: 1.0
    """

    def _get_Pfctr6(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    def _set_Pfctr6(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 35, value, flags)

    Pfctr6 = property(_get_Pfctr6, _set_Pfctr6) # type: float
    """
    Pfctr6 = 1, 1 by default, see PmppkW

    Name: `Pfctr6`
    Default: 1.0
    """

    def _get_PbiaskW(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    def _set_PbiaskW(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 36, value, flags)

    PbiaskW = property(_get_PbiaskW, _set_PbiaskW) # type: float
    """
    Pbias = -0.1, 0 by default, see PmppkW

    Name: `PbiaskW`
    Default: 0.0
    """

    def _get_CC_Switch(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 37) != 0

    def _set_CC_Switch(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 37, value, flags)

    CC_Switch = property(_get_CC_Switch, _set_CC_Switch) # type: bool
    """
    CC_Switch: default value is false.
    CC_Switch = true --cooperate control on
    CC_Switch = false -- cooperate control off

    Name: `CC_Switch`
    Default: False
    """

    def _get_kcq_drp2(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 38)

    def _set_kcq_drp2(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 38, value, flags)

    kcq_drp2 = property(_get_kcq_drp2, _set_kcq_drp2) # type: float
    """
    kcq_drp2. the droop gain: 0.0~0.1

    Name: `kcq_drp2`
    Default: 0.0
    """

    def _get_Volt_Trhd(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 39)

    def _set_Volt_Trhd(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 39, value, flags)

    Volt_Trhd = property(_get_Volt_Trhd, _set_Volt_Trhd) # type: float
    """
    Volt_Trhd. 0.~0.05. 0 means v has to follow v_ref

    Name: `Volt_Trhd`
    Default: 0.0
    """

    def _get_Droop(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 40)

    def _set_Droop(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 40, value, flags)

    Droop = property(_get_Droop, _set_Droop) # type: int
    """
    droop type: integer: 2- Q = kcq_drp2 * (1-v_dg). others: integral droop with kcq.

    Name: `Droop`
    Default: 0
    """

    def _get_Spectrum_str(self) -> str:
        return self._get_prop_string(41)

    def _set_Spectrum_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(41, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: str
    """
    Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter.

    Name: `Spectrum`
    Default: default
    """

    def _get_Spectrum(self) -> SpectrumObj:
        return self._get_obj(41, SpectrumObj)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(41, value, flags)
            return

        self._set_string_o(41, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: SpectrumObj
    """
    Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter.

    Name: `Spectrum`
    Default: default
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 42)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 42, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    Name: `BaseFreq`
    Units: Hz
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 43) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 43, value, flags)

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
        self._set_string_o(44, value)


class Generic5Properties(TypedDict):
    Phases: int
    Bus1: AnyStr
    kV: float
    kW: float
    PF: float
    Conn: Union[AnyStr, int, enums.Connection]
    kVA: float
    P_Ref1kW: float
    P_Ref2kW: float
    P_Ref3kW: float
    V_Ref1kVLN: float
    V_Ref2kVLN: float
    V_Ref3kVLN: float
    P_RefkW: float
    Q_RefkVAr: float
    Cluster_Num: int
    V_refkVLN: float
    Ctrl_Mode: int
    QV_flag: int
    kcd: float
    kcq: float
    kqi: float
    Q_ref1kvar: float
    Q_ref2kvar: float
    Q_ref3kvar: float
    PMaxkW: float
    PMinkW: float
    PQPriority: int
    PmppkW: float
    Pfctr1: float
    Pfctr2: float
    Pfctr3: float
    Pfctr4: float
    Pfctr5: float
    Pfctr6: float
    PbiaskW: float
    CC_Switch: bool
    kcq_drp2: float
    Volt_Trhd: float
    Droop: int
    Spectrum: Union[AnyStr, SpectrumObj]
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class Generic5Batch(DSSBatch, CircuitElementBatchMixin, PCElementBatchMixin):
    _cls_name = 'Generic5'
    _obj_cls = Generic5
    _cls_idx = 52
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)
       PCElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[Generic5BatchProperties]) -> Generic5Batch:
        """
        Edit this Generic5 batch.

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
        def __iter__(self) -> Iterator[Generic5]:
            yield from DSSBatch.__iter__(self)

    def _get_Phases(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 1)

    def _set_Phases(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(1, value, flags)

    Phases = property(_get_Phases, _set_Phases) # type: BatchInt32ArrayProxy
    """
    Number of Phases, this Induction Machine.  

    Name: `Phases`
    Default: 3
    """

    def _get_Bus1(self) -> List[str]:
        return self._get_batch_str_prop(2)

    def _set_Bus1(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(2, value, flags)

    Bus1 = property(_get_Bus1, _set_Bus1) # type: List[str]
    """
    Bus to which the Induction Machine is connected.  May include specific node specification.

    Name: `Bus1`
    """

    def _get_kV(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kV(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kV = property(_get_kV, _set_kV) # type: BatchFloat64ArrayProxy
    """
    Nominal rated (1.0 per unit) voltage, kV. For 2- and 3-phase machines, specify phase-phase kV. Otherwise, specify actual kV across each branch of the machine. If wye (star), specify phase-neutral kV. If delta or phase-phase connected, specify phase-phase kV.

    Name: `kV`
    Default: 12.47
    """

    def _get_kW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    kW = property(_get_kW, _set_kW) # type: BatchFloat64ArrayProxy
    """
    Shaft Power, kW, for the Induction Machine. Output limit of a DG

    Name: `kW`
    Default: -0.001
    """

    def _get_PF(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 5)

    def _set_PF(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(5, value, flags)

    PF = property(_get_PF, _set_PF) # type: BatchFloat64ArrayProxy
    """
    Present power factor for the machine. 

    **Read-only**

    Name: `PF`
    """

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 6)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(6, value, flags)
            return

        self._set_batch_int32_array(6, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy
    """
    Connection of stator: Delta or Wye. Default is Delta.

    Name: `Conn`
    Default: Delta
    """

    def _get_Conn_str(self) -> List[str]:
        return self._get_batch_str_prop(6)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]
    """
    Connection of stator: Delta or Wye. Default is Delta.

    Name: `Conn`
    Default: Delta
    """

    def _get_kVA(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 7)

    def _set_kVA(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(7, value, flags)

    kVA = property(_get_kVA, _set_kVA) # type: BatchFloat64ArrayProxy
    """
    Rated kVA for the machine.

    Name: `kVA`
    Default: -0.0012
    """

    def _get_P_Ref1kW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 8)

    def _set_P_Ref1kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(8, value, flags)

    P_Ref1kW = property(_get_P_Ref1kW, _set_P_Ref1kW) # type: BatchFloat64ArrayProxy
    """
    P_ref1kW = 10, goes to P_ref1, unit kW, 1st phase set power

    Name: `P_Ref1kW`
    Default: 0.0
    """

    def _get_P_Ref2kW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 9)

    def _set_P_Ref2kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(9, value, flags)

    P_Ref2kW = property(_get_P_Ref2kW, _set_P_Ref2kW) # type: BatchFloat64ArrayProxy
    """
    P_ref2kW = 10, goes to P_ref2, unit kW, 2nd phase set power

    Name: `P_Ref2kW`
    Default: 0.0
    """

    def _get_P_Ref3kW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 10)

    def _set_P_Ref3kW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(10, value, flags)

    P_Ref3kW = property(_get_P_Ref3kW, _set_P_Ref3kW) # type: BatchFloat64ArrayProxy
    """
    P_ref3kW = 10, goes to P_ref3, unit kW, 3rd phase set power

    Name: `P_Ref3kW`
    Default: 0.0
    """

    def _get_V_Ref1kVLN(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_V_Ref1kVLN(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    V_Ref1kVLN = property(_get_V_Ref1kVLN, _set_V_Ref1kVLN) # type: BatchFloat64ArrayProxy
    """
    V_ref1kVLN = 2.16, 1st phase set V, (Unit kV, L-N value): V mode will work if QV_flag =1(by default) V_ref is set which is prior to Q_ref 

    Name: `V_Ref1kVLN`
    Default: 0.0
    """

    def _get_V_Ref2kVLN(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 12)

    def _set_V_Ref2kVLN(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    V_Ref2kVLN = property(_get_V_Ref2kVLN, _set_V_Ref2kVLN) # type: BatchFloat64ArrayProxy
    """
    V_ref2kVLN = 2.16, 2nd phase set V, (Unit kV, L-N value): V mode will work if QV_flag =1(by default) V_ref is set which is prior to Q_ref 

    Name: `V_Ref2kVLN`
    Default: 0.0
    """

    def _get_V_Ref3kVLN(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_V_Ref3kVLN(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    V_Ref3kVLN = property(_get_V_Ref3kVLN, _set_V_Ref3kVLN) # type: BatchFloat64ArrayProxy
    """
    V_ref3kVLN = 2.16, 3rd phase set V, (Unit kV, L-N value): V mode will work if QV_flag =1(by default) V_ref is set which is prior to Q_ref 

    Name: `V_Ref3kVLN`
    Default: 0.0
    """

    def _get_P_RefkW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 14)

    def _set_P_RefkW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(14, value, flags)

    P_RefkW = property(_get_P_RefkW, _set_P_RefkW) # type: BatchFloat64ArrayProxy
    """
    P_refkW = 10, goes to P_ref. Ref P Value (kW). P_ref has priority to kW which is nominal value. (Incide variable P_ref is W)

    Name: `P_RefkW`
    Default: 0.0
    """

    def _get_Q_RefkVAr(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 15)

    def _set_Q_RefkVAr(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(15, value, flags)

    Q_RefkVAr = property(_get_Q_RefkVAr, _set_Q_RefkVAr) # type: BatchFloat64ArrayProxy
    """
    Q_refkVAr=10. Unit Qvar. Ref Q kVAr Value: work only when V_ref is not set

    Name: `Q_RefkVAr`
    Default: 0.0
    """

    def _get_Cluster_Num(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 16)

    def _set_Cluster_Num(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(16, value, flags)

    Cluster_Num = property(_get_Cluster_Num, _set_Cluster_Num) # type: BatchInt32ArrayProxy
    """
    Cluster_num: has to be coincident with Fmonitor attached. Default value is 0

    Name: `Cluster_Num`
    Default: 0
    """

    def _get_V_refkVLN(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 17)

    def _set_V_refkVLN(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(17, value, flags)

    V_refkVLN = property(_get_V_refkVLN, _set_V_refkVLN) # type: BatchFloat64ArrayProxy
    """
    V_refkVLN = 2.16, pos sequence set V. V_ref (Unit kV, L-N value): V mode will work if QV_flag =1(by default) V_ref is set which is prior to Q_ref

    Name: `V_refkVLN`
    Default: 0.001
    """

    def _get_Ctrl_Mode(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 18)

    def _set_Ctrl_Mode(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(18, value, flags)

    Ctrl_Mode = property(_get_Ctrl_Mode, _set_Ctrl_Mode) # type: BatchInt32ArrayProxy
    """
    ctrl mode:     /// contrl mode     ///    ctrl_mode =0; phases = 3;  // pos avg control---p_ref, V_ref, Q_ref    \\n 
     ///    ctrl_mode =1; phases = 1; bus1 = 452.1;      ---p_ref1, V_ref1, Q_ref1 \\n
    ///    ctrl_mode =2; phases = 1; bus1 = 452.2;      ---p_ref2, V_ref2, Q_ref2 \\n
    ///    ctrl_mode =3; phases = 1; bus1 = 452.3;      ---p_ref3, V_ref3, Q_ref3 \\n
    ///    ctrl_mode =4; phases = 3; bus1 = 452.2;      ---p_ref1,2,3, V_ref1,2,3, Q_ref1,2,3

    Name: `Ctrl_Mode`
    Default: 0
    """

    def _get_QV_flag(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 19)

    def _set_QV_flag(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(19, value, flags)

    QV_flag = property(_get_QV_flag, _set_QV_flag) # type: BatchInt32ArrayProxy
    """
    QV_flag : 0-Q_ref mode; 1- V_ref mode

    Name: `QV_flag`
    Default: 0
    """

    def _get_kcd(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 20)

    def _set_kcd(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(20, value, flags)

    kcd = property(_get_kcd, _set_kcd) # type: BatchFloat64ArrayProxy
    """
    kcd: Idi control gain

    Name: `kcd`
    Default: 0.1
    """

    def _get_kcq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 21)

    def _set_kcq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(21, value, flags)

    kcq = property(_get_kcq, _set_kcq) # type: BatchFloat64ArrayProxy
    """
    kcq: Iqi control gain to delta V

    Name: `kcq`
    Default: 0.1
    """

    def _get_kqi(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 22)

    def _set_kqi(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    kqi = property(_get_kqi, _set_kqi) # type: BatchFloat64ArrayProxy
    """
    kqi: Iqi control gain to delta Q

    Name: `kqi`
    Default: 0.1
    """

    def _get_Q_ref1kvar(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 23)

    def _set_Q_ref1kvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(23, value, flags)

    Q_ref1kvar = property(_get_Q_ref1kvar, _set_Q_ref1kvar) # type: BatchFloat64ArrayProxy
    """
    Q_ref1kVAr=10. Unit Qvar. Ref Q kVAr Value: work only when V_ref is not set

    Name: `Q_ref1kvar`
    Default: 0.0
    """

    def _get_Q_ref2kvar(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 24)

    def _set_Q_ref2kvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(24, value, flags)

    Q_ref2kvar = property(_get_Q_ref2kvar, _set_Q_ref2kvar) # type: BatchFloat64ArrayProxy
    """
    Q_ref2kVAr=10. Unit Qvar. Ref Q kVAr Value: work only when V_ref is not set

    Name: `Q_ref2kvar`
    Default: 0.0
    """

    def _get_Q_ref3kvar(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 25)

    def _set_Q_ref3kvar(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(25, value, flags)

    Q_ref3kvar = property(_get_Q_ref3kvar, _set_Q_ref3kvar) # type: BatchFloat64ArrayProxy
    """
    Q_ref3kVAr=10. Unit Qvar. Ref Q kVAr Value: work only when V_ref is not set

    Name: `Q_ref3kvar`
    Default: 0.0
    """

    def _get_PMaxkW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 26)

    def _set_PMaxkW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(26, value, flags)

    PMaxkW = property(_get_PMaxkW, _set_PMaxkW) # type: BatchFloat64ArrayProxy
    """
    PmaxkW = 100, goes to Pmax, unit kW, set max active power output; Operation limit of active power for DG
      Pmax should be less than or equal to kW

    Name: `PMaxkW`
    Default: -0.001
    """

    def _get_PMinkW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 27)

    def _set_PMinkW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(27, value, flags)

    PMinkW = property(_get_PMinkW, _set_PMinkW) # type: BatchFloat64ArrayProxy
    """
    PminkW = 10, goes to Pmin, unit kW; Operation limit of active power for DG

    Name: `PMinkW`
    Default: 0.0
    """

    def _get_PQPriority(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 28)

    def _set_PQPriority(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(28, value, flags)

    PQPriority = property(_get_PQPriority, _set_PQPriority) # type: BatchInt32ArrayProxy
    """
    PQpriority, goes to PQpriority, define how to set Qmax. 0: Q,1: P 

    Name: `PQPriority`
    Default: 1
    """

    def _get_PmppkW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 29)

    def _set_PmppkW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(29, value, flags)

    PmppkW = property(_get_PmppkW, _set_PmppkW) # type: BatchFloat64ArrayProxy
    """
    PmppkW = 100, goes to Pmpp, unit kW, input Pmpp to calculate kW;
      kW := (Pmpp + Pbias)*Pfctr1*Pfctr2*Pfctr3*Pfctr4*Pfctr5*Pfctr6;
    Pbias = 0 by default, Pfctr*=1 by default; These properties will overwrite kW.

    Name: `PmppkW`
    Default: 0.001
    """

    def _get_Pfctr1(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 30)

    def _set_Pfctr1(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(30, value, flags)

    Pfctr1 = property(_get_Pfctr1, _set_Pfctr1) # type: BatchFloat64ArrayProxy
    """
    Pfctr1 = 0.16, see PmppkW

    Name: `Pfctr1`
    Default: 1.0
    """

    def _get_Pfctr2(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 31)

    def _set_Pfctr2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(31, value, flags)

    Pfctr2 = property(_get_Pfctr2, _set_Pfctr2) # type: BatchFloat64ArrayProxy
    """
    Pfctr2 = 1, 1 by default, see PmppkW

    Name: `Pfctr2`
    Default: 1.0
    """

    def _get_Pfctr3(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 32)

    def _set_Pfctr3(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(32, value, flags)

    Pfctr3 = property(_get_Pfctr3, _set_Pfctr3) # type: BatchFloat64ArrayProxy
    """
    Pfctr3 = 1, 1 by default, see PmppkW

    Name: `Pfctr3`
    Default: 1.0
    """

    def _get_Pfctr4(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 33)

    def _set_Pfctr4(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(33, value, flags)

    Pfctr4 = property(_get_Pfctr4, _set_Pfctr4) # type: BatchFloat64ArrayProxy
    """
    Pfctr4= 1, 1 by default, see PmppkW

    Name: `Pfctr4`
    Default: 1.0
    """

    def _get_Pfctr5(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 34)

    def _set_Pfctr5(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(34, value, flags)

    Pfctr5 = property(_get_Pfctr5, _set_Pfctr5) # type: BatchFloat64ArrayProxy
    """
    Pfctr5 =1, 1 by default, see PmppkW

    Name: `Pfctr5`
    Default: 1.0
    """

    def _get_Pfctr6(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 35)

    def _set_Pfctr6(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(35, value, flags)

    Pfctr6 = property(_get_Pfctr6, _set_Pfctr6) # type: BatchFloat64ArrayProxy
    """
    Pfctr6 = 1, 1 by default, see PmppkW

    Name: `Pfctr6`
    Default: 1.0
    """

    def _get_PbiaskW(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 36)

    def _set_PbiaskW(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(36, value, flags)

    PbiaskW = property(_get_PbiaskW, _set_PbiaskW) # type: BatchFloat64ArrayProxy
    """
    Pbias = -0.1, 0 by default, see PmppkW

    Name: `PbiaskW`
    Default: 0.0
    """

    def _get_CC_Switch(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(37)
        ]

    def _set_CC_Switch(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(37, value, flags)

    CC_Switch = property(_get_CC_Switch, _set_CC_Switch) # type: List[bool]
    """
    CC_Switch: default value is false.
    CC_Switch = true --cooperate control on
    CC_Switch = false -- cooperate control off

    Name: `CC_Switch`
    Default: False
    """

    def _get_kcq_drp2(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 38)

    def _set_kcq_drp2(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(38, value, flags)

    kcq_drp2 = property(_get_kcq_drp2, _set_kcq_drp2) # type: BatchFloat64ArrayProxy
    """
    kcq_drp2. the droop gain: 0.0~0.1

    Name: `kcq_drp2`
    Default: 0.0
    """

    def _get_Volt_Trhd(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 39)

    def _set_Volt_Trhd(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(39, value, flags)

    Volt_Trhd = property(_get_Volt_Trhd, _set_Volt_Trhd) # type: BatchFloat64ArrayProxy
    """
    Volt_Trhd. 0.~0.05. 0 means v has to follow v_ref

    Name: `Volt_Trhd`
    Default: 0.0
    """

    def _get_Droop(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 40)

    def _set_Droop(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(40, value, flags)

    Droop = property(_get_Droop, _set_Droop) # type: BatchInt32ArrayProxy
    """
    droop type: integer: 2- Q = kcq_drp2 * (1-v_dg). others: integral droop with kcq.

    Name: `Droop`
    Default: 0
    """

    def _get_Spectrum_str(self) -> List[str]:
        return self._get_batch_str_prop(41)

    def _set_Spectrum_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(41, value, flags)

    Spectrum_str = property(_get_Spectrum_str, _set_Spectrum_str) # type: List[str]
    """
    Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter.

    Name: `Spectrum`
    Default: default
    """

    def _get_Spectrum(self) -> List[SpectrumObj]:
        return self._get_batch_obj_prop(41)

    def _set_Spectrum(self, value: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(41, value, flags)

    Spectrum = property(_get_Spectrum, _set_Spectrum) # type: List[SpectrumObj]
    """
    Name of harmonic voltage or current spectrum for this IndMach012. Voltage behind Xd" for machine - default. Current injection for inverter.

    Name: `Spectrum`
    Default: default
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 42)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(42, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    Name: `BaseFreq`
    Units: Hz
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(43)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(43, value, flags)

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
        self._set_batch_string(44, value, flags)

class Generic5BatchProperties(TypedDict):
    Phases: Union[int, Int32Array]
    Bus1: Union[AnyStr, List[AnyStr]]
    kV: Union[float, Float64Array]
    kW: Union[float, Float64Array]
    PF: Union[float, Float64Array]
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    kVA: Union[float, Float64Array]
    P_Ref1kW: Union[float, Float64Array]
    P_Ref2kW: Union[float, Float64Array]
    P_Ref3kW: Union[float, Float64Array]
    V_Ref1kVLN: Union[float, Float64Array]
    V_Ref2kVLN: Union[float, Float64Array]
    V_Ref3kVLN: Union[float, Float64Array]
    P_RefkW: Union[float, Float64Array]
    Q_RefkVAr: Union[float, Float64Array]
    Cluster_Num: Union[int, Int32Array]
    V_refkVLN: Union[float, Float64Array]
    Ctrl_Mode: Union[int, Int32Array]
    QV_flag: Union[int, Int32Array]
    kcd: Union[float, Float64Array]
    kcq: Union[float, Float64Array]
    kqi: Union[float, Float64Array]
    Q_ref1kvar: Union[float, Float64Array]
    Q_ref2kvar: Union[float, Float64Array]
    Q_ref3kvar: Union[float, Float64Array]
    PMaxkW: Union[float, Float64Array]
    PMinkW: Union[float, Float64Array]
    PQPriority: Union[int, Int32Array]
    PmppkW: Union[float, Float64Array]
    Pfctr1: Union[float, Float64Array]
    Pfctr2: Union[float, Float64Array]
    Pfctr3: Union[float, Float64Array]
    Pfctr4: Union[float, Float64Array]
    Pfctr5: Union[float, Float64Array]
    Pfctr6: Union[float, Float64Array]
    PbiaskW: Union[float, Float64Array]
    CC_Switch: bool
    kcq_drp2: Union[float, Float64Array]
    Volt_Trhd: Union[float, Float64Array]
    Droop: Union[int, Int32Array]
    Spectrum: Union[AnyStr, SpectrumObj, List[AnyStr], List[SpectrumObj]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

#TODO: warn that begin_edit=False with extra params will be ignored?

class IGeneric5(IDSSObj, Generic5Batch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Generic5, Generic5Batch)
        Generic5Batch.__init__(self, self._api_util, sync_cls_idx=Generic5._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Generic5:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> Generic5Batch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) Generic5 objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[Generic5]:
            yield from Generic5Batch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[Generic5Properties]) -> Generic5:
        """
        Creates a new Generic5.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[Generic5BatchProperties]) -> Generic5Batch:
        """
        Creates a new batch of Generic5 objects

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
