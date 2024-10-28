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

class FMonitor(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'FMonitor'
    _cls_idx = 51
    _cls_int_idx = {
        2,
        5,
        6,
        7,
        10,
        13,
        15,
        17,
        23,
    }
    _cls_float_idx = {
        4,
        12,
        16,
        22,
    }
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'action': 3,
        'p_trans_ref': 4,
        'node_num': 5,
        'cluster_num': 6,
        'nodes': 7,
        'commvector': 8,
        'elemtableline': 9,
        'p_mode': 10,
        'commdelayvector': 11,
        't_intvl_smpl': 12,
        'maxlocalmem': 13,
        'volt_limits_pu': 14,
        'b_curt_ctrl': 15,
        'up_dly': 16,
        'virtual_ld_node': 17,
        'egen': 18,
        'attack_defense': 19,
        'comm_hide': 20,
        'comm_node_hide': 21,
        'basefreq': 22,
        'enabled': 23,
        'like': 24,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[FMonitorProperties]) -> FMonitor:
        """
        Edit this FMonitor.

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

    Name: `Element`
    Default: Vsource.source
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

    Name: `Element`
    Default: Vsource.source
    """

    def _get_Terminal(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Terminal(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: int
    """
    Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically. For monitoring states, attach monitor to terminal 1.

    Name: `Terminal`
    Default: 1
    """

    def Action(self, value: Union[AnyStr, int, enums.FMonitorAction], flags: enums.SetterFlags = 0):
        """
        {Clear | Save | Take | Process}
        (C)lears or (S)aves current buffer.
        (T)ake action takes a sample.
        (P)rocesses the data taken so far (e.g. Pst for mode 4).

        Note that monitors are automatically reset (cleared) when the Set Mode= command is issued. Otherwise, the user must explicitly reset all monitors (reset monitors command) or individual monitors with the Clear action.

        Name: `Action`
        """
        if isinstance(value, int):
            self._lib.Obj_SetInt32(self._ptr, 3, value, flags)
            return

        self._set_string_o(3, value)

    def Clear(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(FMonitorAction.Clear)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.FMonitorAction.Clear, flags)

    def Reset(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(FMonitorAction.Reset)'''
        self._lib.Obj_SetInt32(self._ptr, 3, enums.FMonitorAction.Reset, flags)

    def _get_P_Trans_Ref(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    def _set_P_Trans_Ref(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 4, value, flags)

    P_Trans_Ref = property(_get_P_Trans_Ref, _set_P_Trans_Ref) # type: float
    """
    P_trans_ref: P ref value for metered element(unit kW)

    Name: `P_Trans_Ref`
    Default: 0.0
    """

    def _get_Node_Num(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 5)

    def _set_Node_Num(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 5, value, flags)

    Node_Num = property(_get_Node_Num, _set_Node_Num) # type: int
    """
    Node_num
    Assign a node number within a cluster

    **Unused** (unused internally by the models, but can be used to transport data)

    Name: `Node_Num`
    Default: 0
    """

    def _get_Cluster_Num(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 6)

    def _set_Cluster_Num(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 6, value, flags)

    Cluster_Num = property(_get_Cluster_Num, _set_Cluster_Num) # type: int
    """
    Cluster_num

    Name: `Cluster_Num`
    Default: 0
    """

    def _get_Nodes(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 7)

    def _set_Nodes(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 7, value, flags)

    Nodes = property(_get_Nodes, _set_Nodes) # type: int
    """
    Nodes connected to this FMonitor. Example:(Nodes=33)

    Name: `Nodes`
    Default: 33
    """

    def _get_CommVector(self) -> str:
        return self._get_prop_string(8)

    def _set_CommVector(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(8, value, flags)

    CommVector = property(_get_CommVector, _set_CommVector) # type: str
    """
    CommVector of this FMonitor. 
    The first entry of this vector is the number of 
    Example:(CommVector={2,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0})
    The example show node #2 can communicate to node #1,#2,#3

    Name: `CommVector`
    """

    def _get_ElemTableLine(self) -> str:
        return self._get_prop_string(9)

    def _set_ElemTableLine(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(9, value, flags)

    ElemTableLine = property(_get_ElemTableLine, _set_ElemTableLine) # type: str
    """
    ElemTableLine of the each node within this cluster. 
    The first entry of this vector is the number of node within cluster 
    The second entry of this vector is element name 
    The third entry of this vector is terminal number 
    The fourth entry of this vector is voltage sensor 
    Example:(ElemTable={2,Line.1,1,1})
    The example show node #2 Element

    Name: `ElemTableLine`
    """

    def _get_P_Mode(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 10)

    def _set_P_Mode(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    P_Mode = property(_get_P_Mode, _set_P_Mode) # type: int
    """
    0 = real Power controlled by each p_ref on each DG
    1 = real Power on MeteredElem controlled by DGs according to P_trans_ref
    2 = Not defined
    3 = Not defined

    Name: `P_Mode`
    Default: 0
    """

    def _get_CommDelayVector(self) -> str:
        return self._get_prop_string(11)

    def _set_CommDelayVector(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(11, value, flags)

    CommDelayVector = property(_get_CommDelayVector, _set_CommDelayVector) # type: str
    """
    CommDelayVector of this FMonitor. 
    The first entry of this vector is the number of the node.
    Example:(CommVector={2,t1,0,t2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0})
    The example show node #2 can communicate to node #1 and #3 with time delay t1 and t2 separately

    Name: `CommDelayVector`
    """

    def _get_T_IntVL_Smpl(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_T_IntVL_Smpl(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    T_IntVL_Smpl = property(_get_T_IntVL_Smpl, _set_T_IntVL_Smpl) # type: float
    """
    T_intvl_smpl: 
    The information of each agent will be sampled at each T_comm time. Unit is second.
    T_intvl_smpl is also the minimal communication time between neighbor nodes.
    If T_intvl_smpl=0.0, no delay for the communication is enabled in the simulation.

    Name: `T_IntVL_Smpl`
    Default: 0.0
    """

    def _get_MaxLocalMem(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 13)

    def _set_MaxLocalMem(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 13, value, flags)

    MaxLocalMem = property(_get_MaxLocalMem, _set_MaxLocalMem) # type: int
    """
    MaxLocalMem: the max number of local memory size. No larger than 99

    Name: `MaxLocalMem`
    Default: 10
    """

    def _get_Volt_Limits_pu(self) -> str:
        return self._get_prop_string(14)

    def _set_Volt_Limits_pu(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(14, value, flags)

    Volt_Limits_pu = property(_get_Volt_Limits_pu, _set_Volt_Limits_pu) # type: str
    """
    Volt_limits_pu: example "Volt_limits_pu={a0,a1, a2}"
    a0: the phase number, 0 means pos. seq; a1: upper voltage limit of this cluster, usually 1.05;
    a2: upper voltage limit of this cluster, usually 0.95

    Name: `Volt_Limits_pu`
    Default: [0, 0, 0.94999999999999996]
    """

    def _get_b_Curt_Ctrl(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    def _set_b_Curt_Ctrl(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 15, value, flags)

    b_Curt_Ctrl = property(_get_b_Curt_Ctrl, _set_b_Curt_Ctrl) # type: bool
    """
    b_Curt_Ctrl:set P curtailment on/off;
    b_Curt_Ctrl=True: P curtailment will be implemented according to the system voltage (default);
    b_Curt_Ctrl=False: P curtailment will not be implemented.

    Name: `b_Curt_Ctrl`
    Default: False
    """

    def _get_Up_Dly(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    def _set_Up_Dly(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 16, value, flags)

    Up_Dly = property(_get_Up_Dly, _set_Up_Dly) # type: float
    """
    up_dly: delay time to upper level. For example: "up_dly := 0.05"
    It can be used to simulate the time delay between clusters

    Name: `Up_Dly`
    Default: 0.0
    """

    def _get_Virtual_LD_Node(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 17)

    def _set_Virtual_LD_Node(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 17, value, flags)

    Virtual_LD_Node = property(_get_Virtual_LD_Node, _set_Virtual_LD_Node) # type: int
    """
    Which node talks to upper level.

    Name: `Virtual_LD_Node`
    Default: 1
    """

    def _get_EGen(self) -> str:
        return self._get_prop_string(18)

    def _set_EGen(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(18, value, flags)

    EGen = property(_get_EGen, _set_EGen) # type: str
    """
    `EGen = {kVA_fm, M_fm, D_fm, Tau_fm, Ki_fm,init_time}`

    where equations are:

    `delta'' = omega`
    `M_fm * omega'' = puPm - puPe - D_fm*omega`
    `Tau_fm*Pm '' = Ki_fm * omega`
    `puPm = Pm / kVA_fm, puPe = Pe / kVAM_fm;`

    Everything is zero within init_time (default value is 0.5s);
    `k_dltP` is the coordinator for PV control input: `u_i = k_dltP * pu_DltP + omg_fm`.

    Name: `EGen`
    Default: [0, 0, 0, 0, 0, 0.5, 0]
    """

    def _get_Attack_Defense(self) -> str:
        return self._get_prop_string(19)

    def _set_Attack_Defense(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(19, value, flags)

    Attack_Defense = property(_get_Attack_Defense, _set_Attack_Defense) # type: str
    """
    Define attack and defense:

    `attack_defense = {atk , dfs , atk_time , atk_node_num  , d_atk0  , beta_dfs, D_beta, D_p }`.

    attack_defense has to be defined after ''nodes'.
    Example: `attack_defense = { true , false , 0.5 , 1 , 0.1 , 5, 1 , 1}`.
    Example:
    (1) under attack;
    (2) defense is off;
    (3) attack starts at 0.5s;
    (4) attack is on node 1;
    (5) initial value of attack: `d_0 = 0.1`;
    (6) `beta = 5`;
    (7) `D_beta` is used as a multiplier on $\\phi$;
    (8) `D_p` is used as the attack on gradient control: `D_p = 1`, which is normal; `D_p=-1`, gradient control work on the opposite.

    Name: `Attack_Defense`
    Default: ["no", "no", 0.5, 1, 0, 0, 1, 1]
    """

    def _get_Comm_Hide(self) -> str:
        return self._get_prop_string(20)

    def _set_Comm_Hide(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(20, value, flags)

    Comm_Hide = property(_get_Comm_Hide, _set_Comm_Hide) # type: str
    """
    Comm_hide={...}. It is defined like CommVector.

    Name: `Comm_Hide`
    """

    def _get_Comm_Node_Hide(self) -> str:
        return self._get_prop_string(21)

    def _set_Comm_Node_Hide(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(21, value, flags)

    Comm_Node_Hide = property(_get_Comm_Node_Hide, _set_Comm_Node_Hide) # type: str
    """
    Comm_node_hide={...}. It is defined like CommVector.

    Name: `Comm_Node_Hide`
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 22)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 22, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    Name: `BaseFreq`
    Units: Hz
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 23) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 23, value, flags)

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
        self._set_string_o(24, value)


class FMonitorProperties(TypedDict):
    Element: Union[AnyStr, DSSObj]
    Terminal: int
    Action: Union[AnyStr, int, enums.FMonitorAction]
    P_Trans_Ref: float
    Node_Num: int
    Cluster_Num: int
    Nodes: int
    CommVector: AnyStr
    ElemTableLine: AnyStr
    P_Mode: int
    CommDelayVector: AnyStr
    T_IntVL_Smpl: float
    MaxLocalMem: int
    Volt_Limits_pu: AnyStr
    b_Curt_Ctrl: bool
    Up_Dly: float
    Virtual_LD_Node: int
    EGen: AnyStr
    Attack_Defense: AnyStr
    Comm_Hide: AnyStr
    Comm_Node_Hide: AnyStr
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class FMonitorBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'FMonitor'
    _obj_cls = FMonitor
    _cls_idx = 51
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[FMonitorBatchProperties]) -> FMonitorBatch:
        """
        Edit this FMonitor batch.

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
        def __iter__(self) -> Iterator[FMonitor]:
            yield from DSSBatch.__iter__(self)

    def _get_Element_str(self) -> List[str]:
        return self._get_batch_str_prop(1)

    def _set_Element_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: List[str]
    """
    Name (Full Object name) of element to which the monitor is connected.

    Name: `Element`
    Default: Vsource.source
    """

    def _get_Element(self) -> List[DSSObj]:
        return self._get_batch_obj_prop(1)

    def _set_Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: List[DSSObj]
    """
    Name (Full Object name) of element to which the monitor is connected.

    Name: `Element`
    Default: Vsource.source
    """

    def _get_Terminal(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 2)

    def _set_Terminal(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: BatchInt32ArrayProxy
    """
    Number of the terminal of the circuit element to which the monitor is connected. 1 or 2, typically. For monitoring states, attach monitor to terminal 1.

    Name: `Terminal`
    Default: 1
    """

    def Action(self, value: Union[AnyStr, int, enums.FMonitorAction], flags: enums.SetterFlags = 0):
        """
        {Clear | Save | Take | Process}
        (C)lears or (S)aves current buffer.
        (T)ake action takes a sample.
        (P)rocesses the data taken so far (e.g. Pst for mode 4).

        Note that monitors are automatically reset (cleared) when the Set Mode= command is issued. Otherwise, the user must explicitly reset all monitors (reset monitors command) or individual monitors with the Clear action.

        Name: `Action`
        """
        if isinstance(value, (bytes, str)) or (isinstance(value, LIST_LIKE) and len(value) > 0 and isinstance(value[0], (bytes, str))):
            self._set_batch_string(3, value, flags)
        else:
            self._set_batch_int32_array(3, value, flags)

    def Clear(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(FMonitorAction.Clear)'''
        self._set_batch_int32_array(3, enums.FMonitorAction.Clear, flags)

    def Reset(self, flags: enums.SetterFlags = 0):
        '''Shortcut to Action(FMonitorAction.Reset)'''
        self._set_batch_int32_array(3, enums.FMonitorAction.Reset, flags)

    def _get_P_Trans_Ref(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 4)

    def _set_P_Trans_Ref(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(4, value, flags)

    P_Trans_Ref = property(_get_P_Trans_Ref, _set_P_Trans_Ref) # type: BatchFloat64ArrayProxy
    """
    P_trans_ref: P ref value for metered element(unit kW)

    Name: `P_Trans_Ref`
    Default: 0.0
    """

    def _get_Node_Num(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 5)

    def _set_Node_Num(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(5, value, flags)

    Node_Num = property(_get_Node_Num, _set_Node_Num) # type: BatchInt32ArrayProxy
    """
    Node_num
    Assign a node number within a cluster

    **Unused** (unused internally by the models, but can be used to transport data)

    Name: `Node_Num`
    Default: 0
    """

    def _get_Cluster_Num(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 6)

    def _set_Cluster_Num(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(6, value, flags)

    Cluster_Num = property(_get_Cluster_Num, _set_Cluster_Num) # type: BatchInt32ArrayProxy
    """
    Cluster_num

    Name: `Cluster_Num`
    Default: 0
    """

    def _get_Nodes(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 7)

    def _set_Nodes(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(7, value, flags)

    Nodes = property(_get_Nodes, _set_Nodes) # type: BatchInt32ArrayProxy
    """
    Nodes connected to this FMonitor. Example:(Nodes=33)

    Name: `Nodes`
    Default: 33
    """

    def _get_CommVector(self) -> List[str]:
        return self._get_batch_str_prop(8)

    def _set_CommVector(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(8, value, flags)

    CommVector = property(_get_CommVector, _set_CommVector) # type: List[str]
    """
    CommVector of this FMonitor. 
    The first entry of this vector is the number of 
    Example:(CommVector={2,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0})
    The example show node #2 can communicate to node #1,#2,#3

    Name: `CommVector`
    """

    def _get_ElemTableLine(self) -> List[str]:
        return self._get_batch_str_prop(9)

    def _set_ElemTableLine(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(9, value, flags)

    ElemTableLine = property(_get_ElemTableLine, _set_ElemTableLine) # type: List[str]
    """
    ElemTableLine of the each node within this cluster. 
    The first entry of this vector is the number of node within cluster 
    The second entry of this vector is element name 
    The third entry of this vector is terminal number 
    The fourth entry of this vector is voltage sensor 
    Example:(ElemTable={2,Line.1,1,1})
    The example show node #2 Element

    Name: `ElemTableLine`
    """

    def _get_P_Mode(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 10)

    def _set_P_Mode(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(10, value, flags)

    P_Mode = property(_get_P_Mode, _set_P_Mode) # type: BatchInt32ArrayProxy
    """
    0 = real Power controlled by each p_ref on each DG
    1 = real Power on MeteredElem controlled by DGs according to P_trans_ref
    2 = Not defined
    3 = Not defined

    Name: `P_Mode`
    Default: 0
    """

    def _get_CommDelayVector(self) -> List[str]:
        return self._get_batch_str_prop(11)

    def _set_CommDelayVector(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(11, value, flags)

    CommDelayVector = property(_get_CommDelayVector, _set_CommDelayVector) # type: List[str]
    """
    CommDelayVector of this FMonitor. 
    The first entry of this vector is the number of the node.
    Example:(CommVector={2,t1,0,t2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0})
    The example show node #2 can communicate to node #1 and #3 with time delay t1 and t2 separately

    Name: `CommDelayVector`
    """

    def _get_T_IntVL_Smpl(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 12)

    def _set_T_IntVL_Smpl(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    T_IntVL_Smpl = property(_get_T_IntVL_Smpl, _set_T_IntVL_Smpl) # type: BatchFloat64ArrayProxy
    """
    T_intvl_smpl: 
    The information of each agent will be sampled at each T_comm time. Unit is second.
    T_intvl_smpl is also the minimal communication time between neighbor nodes.
    If T_intvl_smpl=0.0, no delay for the communication is enabled in the simulation.

    Name: `T_IntVL_Smpl`
    Default: 0.0
    """

    def _get_MaxLocalMem(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 13)

    def _set_MaxLocalMem(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(13, value, flags)

    MaxLocalMem = property(_get_MaxLocalMem, _set_MaxLocalMem) # type: BatchInt32ArrayProxy
    """
    MaxLocalMem: the max number of local memory size. No larger than 99

    Name: `MaxLocalMem`
    Default: 10
    """

    def _get_Volt_Limits_pu(self) -> List[str]:
        return self._get_batch_str_prop(14)

    def _set_Volt_Limits_pu(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(14, value, flags)

    Volt_Limits_pu = property(_get_Volt_Limits_pu, _set_Volt_Limits_pu) # type: List[str]
    """
    Volt_limits_pu: example "Volt_limits_pu={a0,a1, a2}"
    a0: the phase number, 0 means pos. seq; a1: upper voltage limit of this cluster, usually 1.05;
    a2: upper voltage limit of this cluster, usually 0.95

    Name: `Volt_Limits_pu`
    Default: [0, 0, 0.94999999999999996]
    """

    def _get_b_Curt_Ctrl(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(15)
        ]

    def _set_b_Curt_Ctrl(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(15, value, flags)

    b_Curt_Ctrl = property(_get_b_Curt_Ctrl, _set_b_Curt_Ctrl) # type: List[bool]
    """
    b_Curt_Ctrl:set P curtailment on/off;
    b_Curt_Ctrl=True: P curtailment will be implemented according to the system voltage (default);
    b_Curt_Ctrl=False: P curtailment will not be implemented.

    Name: `b_Curt_Ctrl`
    Default: False
    """

    def _get_Up_Dly(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 16)

    def _set_Up_Dly(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(16, value, flags)

    Up_Dly = property(_get_Up_Dly, _set_Up_Dly) # type: BatchFloat64ArrayProxy
    """
    up_dly: delay time to upper level. For example: "up_dly := 0.05"
    It can be used to simulate the time delay between clusters

    Name: `Up_Dly`
    Default: 0.0
    """

    def _get_Virtual_LD_Node(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 17)

    def _set_Virtual_LD_Node(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(17, value, flags)

    Virtual_LD_Node = property(_get_Virtual_LD_Node, _set_Virtual_LD_Node) # type: BatchInt32ArrayProxy
    """
    Which node talks to upper level.

    Name: `Virtual_LD_Node`
    Default: 1
    """

    def _get_EGen(self) -> List[str]:
        return self._get_batch_str_prop(18)

    def _set_EGen(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(18, value, flags)

    EGen = property(_get_EGen, _set_EGen) # type: List[str]
    """
    `EGen = {kVA_fm, M_fm, D_fm, Tau_fm, Ki_fm,init_time}`

    where equations are:

    `delta'' = omega`
    `M_fm * omega'' = puPm - puPe - D_fm*omega`
    `Tau_fm*Pm '' = Ki_fm * omega`
    `puPm = Pm / kVA_fm, puPe = Pe / kVAM_fm;`

    Everything is zero within init_time (default value is 0.5s);
    `k_dltP` is the coordinator for PV control input: `u_i = k_dltP * pu_DltP + omg_fm`.

    Name: `EGen`
    Default: [0, 0, 0, 0, 0, 0.5, 0]
    """

    def _get_Attack_Defense(self) -> List[str]:
        return self._get_batch_str_prop(19)

    def _set_Attack_Defense(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(19, value, flags)

    Attack_Defense = property(_get_Attack_Defense, _set_Attack_Defense) # type: List[str]
    """
    Define attack and defense:

    `attack_defense = {atk , dfs , atk_time , atk_node_num  , d_atk0  , beta_dfs, D_beta, D_p }`.

    attack_defense has to be defined after ''nodes'.
    Example: `attack_defense = { true , false , 0.5 , 1 , 0.1 , 5, 1 , 1}`.
    Example:
    (1) under attack;
    (2) defense is off;
    (3) attack starts at 0.5s;
    (4) attack is on node 1;
    (5) initial value of attack: `d_0 = 0.1`;
    (6) `beta = 5`;
    (7) `D_beta` is used as a multiplier on $\\phi$;
    (8) `D_p` is used as the attack on gradient control: `D_p = 1`, which is normal; `D_p=-1`, gradient control work on the opposite.

    Name: `Attack_Defense`
    Default: ["no", "no", 0.5, 1, 0, 0, 1, 1]
    """

    def _get_Comm_Hide(self) -> List[str]:
        return self._get_batch_str_prop(20)

    def _set_Comm_Hide(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(20, value, flags)

    Comm_Hide = property(_get_Comm_Hide, _set_Comm_Hide) # type: List[str]
    """
    Comm_hide={...}. It is defined like CommVector.

    Name: `Comm_Hide`
    """

    def _get_Comm_Node_Hide(self) -> List[str]:
        return self._get_batch_str_prop(21)

    def _set_Comm_Node_Hide(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(21, value, flags)

    Comm_Node_Hide = property(_get_Comm_Node_Hide, _set_Comm_Node_Hide) # type: List[str]
    """
    Comm_node_hide={...}. It is defined like CommVector.

    Name: `Comm_Node_Hide`
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 22)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(22, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    Name: `BaseFreq`
    Units: Hz
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(23)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(23, value, flags)

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
        self._set_batch_string(24, value, flags)

class FMonitorBatchProperties(TypedDict):
    Element: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    Terminal: Union[int, Int32Array]
    Action: Union[AnyStr, int, enums.FMonitorAction]
    P_Trans_Ref: Union[float, Float64Array]
    Node_Num: Union[int, Int32Array]
    Cluster_Num: Union[int, Int32Array]
    Nodes: Union[int, Int32Array]
    CommVector: Union[AnyStr, List[AnyStr]]
    ElemTableLine: Union[AnyStr, List[AnyStr]]
    P_Mode: Union[int, Int32Array]
    CommDelayVector: Union[AnyStr, List[AnyStr]]
    T_IntVL_Smpl: Union[float, Float64Array]
    MaxLocalMem: Union[int, Int32Array]
    Volt_Limits_pu: Union[AnyStr, List[AnyStr]]
    b_Curt_Ctrl: bool
    Up_Dly: Union[float, Float64Array]
    Virtual_LD_Node: Union[int, Int32Array]
    EGen: Union[AnyStr, List[AnyStr]]
    Attack_Defense: Union[AnyStr, List[AnyStr]]
    Comm_Hide: Union[AnyStr, List[AnyStr]]
    Comm_Node_Hide: Union[AnyStr, List[AnyStr]]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class IFMonitor(IDSSObj, FMonitorBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, FMonitor, FMonitorBatch)
        FMonitorBatch.__init__(self, self._api_util, sync_cls_idx=FMonitor._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> FMonitor:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> FMonitorBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) FMonitor objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[FMonitor]:
            yield from FMonitorBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[FMonitorProperties]) -> FMonitor:
        """
        Creates a new FMonitor.

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

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[FMonitorBatchProperties]) -> FMonitorBatch:
        """
        Creates a new batch of FMonitor objects

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
