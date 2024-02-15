from __future__ import annotations
from typing import Union, List, AnyStr, Optional, TYPE_CHECKING
import numpy as np

from weakref import WeakKeyDictionary

# These were copied directly from DSS-Python; they may change later
# from .DSSEvents import IDSSEvents
from .Error import IError
from .ReduceCkt import IReduceCkt
from .Topology import ITopology
from .YMatrix import IYMatrix

from .common import CffiApiUtil
from dss.enums import DSSJSONFlags
from .enums import *
from .Bus import IBuses
from .CircuitElement import CircuitElementBatch
from .ControlQueue import IControlQueue
from .Obj import IObj
from .PCElement import PCElementBatch
from .PDElement import PDElementBatch
from .Settings import ISettings
from .Solution import ISolution
from .ZIP import IZIP
from .types import Float64Array, ComplexArray

if TYPE_CHECKING:
    try:
        from dss import IDSS as DSSPython
    except:
        DSSPython = None

    try:
        from opendssdirect.OpenDSSDirect import OpenDSSDirect
    except:
        OpenDSSDirect = None


class AltDSS(IObj):
    __slots__ = [
        'Bus',
        'ControlQueue',
        'Element',
        'Error',
        # 'Events',
        # 'Parallel',
        'PCElement',
        'PDElement',
        'ReduceCircuit',
        'Settings',
        'Solution',
        'Topology',
        'YMatrix',
        'ZIP',
        '_ptr',
    ]
    _ctx_to_dss = WeakKeyDictionary()
   
    Bus: IBuses
    ControlQueue: IControlQueue
    Element: CircuitElementBatch
    Error: IError
    # Events: IDSSEvents
    # Parallel: IParallel
    PCElement: PCElementBatch
    PDElement: PDElementBatch
    ReduceCircuit: IReduceCkt
    Settings: ISettings
    Solution: ISolution
    Topology: ITopology
    YMatrix: IYMatrix
    ZIP: IZIP

    @classmethod
    def _get_instance(cls: AltDSS, api_util: CffiApiUtil = None, ctx=None) -> AltDSS:
        '''
        If there is an existing AltDSS instance for a context, return it.
        Otherwise, try to wrap the context into a new AltDSS API instance.
        '''
        if api_util is None:
            # If none exists, something is probably wrong elsewhere,
            # so let's allow the IndexError to propagate
            api_util = CffiApiUtil._ctx_to_util[ctx]

        dss = cls._ctx_to_dss.get(api_util.ctx)
        if dss is None:
            dss = cls(api_util)

        return dss


    def __init__(self, api_util):
        '''
        Creates a new AltDSS instance for the DSS context specified in `api_util`.

        Not intended for typical usage. For creating new separate DSS instances, refer
        to the `AltDSS.NewContext` method.
        '''
        IObj.__init__(self, api_util)
        AltDSS._ctx_to_dss[api_util.ctx] = self
        self._ptr = api_util.ctx

        self.Bus = IBuses(self._api_util)
        self.ControlQueue = IControlQueue(self._api_util)
        self.Element = CircuitElementBatch(None, self)
        self.Error = IError(self._api_util)
        # self.Events = IDSSEvents(self._api_util)
        # self.Parallel = IParallel(self._api_util)
        self.PCElement = PCElementBatch(None, self)
        self.PDElement = PDElementBatch(None, self)
        self.ReduceCircuit = IReduceCkt(self._api_util)
        self.Settings = ISettings(self._api_util)
        self.Solution = ISolution(self._api_util)
        self.Topology = ITopology(self._api_util)
        self.YMatrix = IYMatrix(self._api_util)
        self.ZIP = IZIP(self._api_util)


    def DisableElement(self, name: AnyStr):
        '''
        Disable a circuit element by name (removes from circuit but leave in database).
        '''
        if not isinstance(name, bytes):
            name = name.encode(self._api_util.codec)

        self._check_for_error(self._lib.Circuit_Disable(name))

    def EnableElement(self, name: AnyStr):
        '''
        Enable a circuit element by name
        '''
        if not isinstance(name, bytes):
            name = name.encode(self._api_util.codec)

        self._check_for_error(self._lib.Circuit_Enable(name))

    def NodeDistancesByPhase(self, Phase: int) -> Float64Array:
        '''Returns an array of doubles representing the distances to parent EnergyMeter. Sequence of array corresponds to other node ByPhase properties.'''
        self._check_for_error(self._lib.Circuit_Get_AllNodeDistancesByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def NodeNamesByPhase(self, Phase: int) -> List[str]:
        '''Return array of strings of the node names for the By Phase criteria. Sequence corresponds to other ByPhase properties.'''
        return self._check_for_error(self._get_string_array(self._lib.Circuit_Get_AllNodeNamesByPhase, Phase))

    def NodeVmagByPhase(self, Phase: int) -> Float64Array:
        '''Returns Array of doubles represent voltage magnitudes for nodes on the specified phase.'''
        self._check_for_error(self._lib.Circuit_Get_AllNodeVmagByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def NodeVmagPUByPhase(self, Phase: int) -> Float64Array:
        '''Returns array of per unit voltage magnitudes for each node by phase'''
        self._check_for_error(self._lib.Circuit_Get_AllNodeVmagPUByPhase_GR(Phase))
        return self._get_float64_gr_array()

    def BusDistances(self) -> Float64Array:
        '''
        Returns distance from each bus to parent EnergyMeter. Corresponds to sequence in AllBusNames.
        '''
        self._check_for_error(self._lib.Circuit_Get_AllBusDistances_GR())
        return self._get_float64_gr_array()

    def BusNames(self) -> List[str]:
        '''
        Array of strings containing names of all buses in circuit (see AllNodeNames).
        '''
        return self._check_for_error(self._get_string_array(self._lib.Circuit_Get_AllBusNames))

    def BusVmag(self) -> Float64Array:
        '''
        Array of magnitudes (doubles) of voltages at all buses
        '''
        self._check_for_error(self._lib.Circuit_Get_AllBusVmag_GR())
        return self._get_float64_gr_array()

    def BusVmagPu(self) -> Float64Array:
        '''
        Double Array of all bus voltages (each node) magnitudes in Per unit
        '''
        self._check_for_error(self._lib.Circuit_Get_AllBusVmagPu_GR())
        return self._get_float64_gr_array()

    def BusVolts(self) -> ComplexArray:
        '''
        Complex array of all bus, node voltages from most recent solution
        '''
        self._check_for_error(self._lib.Circuit_Get_AllBusVolts_GR())
        return self._get_fcomplex128_gr_array()

    def NodeDistances(self) -> Float64Array:
        '''
        Returns an array of distances from parent EnergyMeter for each Node. Corresponds to AllBusVMag sequence.
        '''
        self._check_for_error(self._lib.Circuit_Get_AllNodeDistances_GR())
        return self._get_float64_gr_array()

    def NodeNames(self) -> List[str]:
        '''
        Array of strings containing full name of each node in system in same order as returned by AllBusVolts, etc.
        '''
        return self._check_for_error(self._get_string_array(self._lib.Circuit_Get_AllNodeNames))

    def LineLosses(self) -> complex:
        '''
        Complex total line losses in the circuit
        '''
        self._check_for_error(self._lib.Circuit_Get_LineLosses_GR())
        return self._get_fcomplex128_gr_simple()

    def Losses(self) -> complex:
        '''
        Total losses in active circuit, complex number (two-element array of double).
        '''
        self._check_for_error(self._lib.Circuit_Get_Losses_GR())
        return self._get_fcomplex128_gr_simple()

    @property
    def Name(self) -> str:
        '''Name of the active circuit.'''
        return self._get_string(self._check_for_error(self._lib.Circuit_Get_Name()))

    @property
    def NumBuses(self) -> int:
        '''Total number of Buses in the circuit.'''
        return self._check_for_error(self._lib.Circuit_Get_NumBuses())

    @property
    def NumCircuitElements(self) -> int:
        '''Number of CircuitElements in the circuit.'''
        return self._check_for_error(self._lib.Circuit_Get_NumCktElements())

    @property
    def NumNodes(self) -> int:
        '''Total number of nodes in the circuit.'''
        return self._check_for_error(self._lib.Circuit_Get_NumNodes())

    @property
    def SubstationLosses(self) -> complex: 
        '''Complex losses in all transformers designated to substations.'''
        self._check_for_error(self._lib.Circuit_Get_SubstationLosses_GR())
        return self._get_fcomplex128_gr_simple()

    def SystemY(self, dense=False) -> ComplexArray:
        '''
        Get the system Y complex matrix.
        Requires either a previous solution or explicitly building the matrix.

        In AltDSS, defaults to the sparse matrix data.
        
        Use `dense=True` to force a dense matrix. Beware the
        memory requirements. The recommendation is to only use dense
        matrices for small systems.
        '''
        if dense:
            self._check_for_error(self._lib.Circuit_Get_SystemY_GR())
            return self._get_fcomplex128_gr_array()

        ffi = self._api_util.ffi
        
        nBus = ffi.new('uint32_t*')
        nBus[0] = 0
        nNz = ffi.new('uint32_t*')
        nNz[0] = 0

        ColPtr = ffi.new('int32_t**')
        RowIdxPtr = ffi.new('int32_t**')
        cValsPtr = ffi.new('double**')

        self._lib.YMatrix_GetCompressedYMatrix(True, nBus, nNz, ColPtr, RowIdxPtr, cValsPtr)

        if not nBus[0] or not nNz[0]:
            res = None
        else:
            # return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix
            res = (
                np.frombuffer(ffi.buffer(cValsPtr[0], nNz[0] * 16), dtype=complex).copy(),
                np.frombuffer(ffi.buffer(RowIdxPtr[0], nNz[0] * 4), dtype=np.int32).copy(),
                np.frombuffer(ffi.buffer(ColPtr[0], (nBus[0] + 1) * 4), dtype=np.int32).copy()
            )

        self._lib.DSS_Dispose_PInteger(ColPtr)
        self._lib.DSS_Dispose_PInteger(RowIdxPtr)
        self._lib.DSS_Dispose_PDouble(cValsPtr)
        
        self._check_for_error()

        return res


    def TotalPower(self) -> complex:
        '''Total power (complex), kVA delivered to the circuit'''
        self._check_for_error(self._lib.Circuit_Get_TotalPower_GR())
        return self._get_fcomplex128_gr_simple()

    def YCurrents(self) -> ComplexArray:
        '''Array of doubles containing complex injection currents for the present solution. It is the "I" vector of I=YV'''
        self._check_for_error(self._lib.Circuit_Get_YCurrents_GR())
        return self._get_fcomplex128_gr_array()

    def YNodeOrder(self) -> List[str]:
        '''Array of strings containing the names of the nodes in the same order as the Y matrix'''
        return self._check_for_error(self._get_string_array(self._lib.Circuit_Get_YNodeOrder))

    def YNodeVarray(self) -> ComplexArray:
        '''Complex array of actual node voltages in same order as SystemY matrix.'''
        self._check_for_error(self._lib.Circuit_Get_YNodeVarray_GR())
        return self._get_fcomplex128_gr_array()

    def Capacity(self, Start: float, Increment: float) -> float:
        '''
        Compute the maximum load the active circuit can serve in the PRESENT YEAR.
        
        This method uses the EnergyMeter objects with the registers set with the 
        `SET UEREGS= (...)` command for the AutoAdd functions. 

        Returns the metered kW (load + losses - generation) and per unit load multiplier 
        for the loading level at which something in the system reports an overload or 
        undervoltage. If no violations, then it returns the metered kW for peak load 
        for the year (1.0 multiplier). 
        
        Aborts and returns 0 if no EnergyMeters.

        Original COM help: https://opendss.epri.com/Capacity1.html
        '''
        return self._check_for_error(self._lib.Circuit_Capacity(Start, Increment))

    def TakeSample(self):
        '''
        Force all Meters and Monitors to take a sample.
        '''
        self._check_for_error(self._lib.Circuit_Sample())

    def SaveSample(self):
        '''
        Force all meters and monitors to save their current buffers.
        '''
        self._check_for_error(self._lib.Circuit_SaveSample())

    def UpdateStorage(self):
        '''
        Force an update to all storage classes. 

        Typically done after a solution. Done automatically in intrinsic solution modes.

        Original COM help: https://opendss.epri.com/UpdateStorage.html
        '''
        self._check_for_error(self._lib.Circuit_UpdateStorage()) #TODO: move to the dedicated class/API

    def Clear(self):
        self('clear')

    def ClearAll(self):
        self._check_for_error(self._lib.DSS_ClearAll())

    def to_json(self, options: DSSJSONFlags = 0) -> str:
        '''
        Returns data for all objects and basic circuit properties as a JSON-encoded string.
        The JSON data is organized using 

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.
        '''
        return self._get_string(self._check_for_error(self._lib.Circuit_ToJSON(options)))

    def NewContext(self) -> AltDSS:
        '''
        Creates a new DSS engine context, wrapped by the AltDSS classes.
        
        An AltDSS Context encapsulates most of the global state of the original OpenDSS engine,
        allowing the user to create multiple instances in the same process. By creating contexts
        manually, the management of threads and potential issues should be handled by the user.
        '''
        ffi = self._api_util.ffi
        lib = self._api_util.lib_unpatched
        new_ctx = ffi.gc(lib.ctx_New(), lib.ctx_Dispose)
        new_api_util = CffiApiUtil(ffi, lib, new_ctx)
        new_api_util._allow_complex = self._api_util._allow_complex
        return type(self)(new_api_util)


    def Command(self, value: Optional[AnyStr]) -> Optional[str]:
        '''
        Input command **string** for the DSS engine.
        
        If no command is provided, the latest command string is returned.

        Prefer using the `Commands` function or the call operator from this class.
        '''
        if value is None:
            return self._get_string(self._check_for_error(self._lib.Text_Get_Command()))

        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Text_Set_Command(value))


    def Commands(self, Value: Union[AnyStr, List[AnyStr]]):
        '''
        Runs a list of strings or a large string as commands directly in the DSS engine.
        Intermediate results from the classic `Text.Result` are ignored.

        Value can be a list of strings, or a single large string (usually faster, but varies).
        '''
        if isinstance(Value, str) or isinstance(Value, bytes):
            if not isinstance(Value, bytes):
                Value = Value.encode(self._api_util.codec)
            
            self._check_for_error(self._lib.Text_CommandBlock(Value))
        else:
            self._check_for_error(self._set_string_array(self._lib.Text_CommandArray, Value))

    @property
    def TextResult(self) -> str:
        """Result string for the last DSS command (classic `Text.Result`)."""
        return self._get_string(self._check_for_error(self._lib.Text_Get_Result()))
    

    def Version(self) -> str:
        from . import __version__
        return self._get_string(self._check_for_error(self._lib.DSS_Get_Version())) + f'\nAltDSS-Python version: {__version__}'


    def __call__(self, cmds: Union[AnyStr, List[AnyStr]]):
        '''
        Pass either a single string (with either one or multiples commands, separated by new lines),
        or a list of strings.

        Shortcut to `AltDSS.Commands()`.

        Examples:
        ``` 
            # single command
            dss("new Circuit.test") 

            # list of commands
            dss(["new Circuit.test", "new Line.line1 bus1=a bus2=b"])

            # block of commands in a big string
            dss("""
                clear
                new Circuit.test
                new Line.line1 bus1=a bus2=b
                new Load.load1 bus1=a bus2=b
            """)
        ```
        '''
        self.Commands(cmds)


    def to_dss_python(self) -> DSSPython:
        """
        Returns an instance of DSS-Python for the active DSS Context.

        A compatible DSS-Python (`pip install dss-python`) is required.
        """
        from dss import IDSS as DSSPython
        return DSSPython._get_instance(ctx=self._api_util.ctx, api_util=self._api_util)


    def to_opendssdirect(self) -> OpenDSSDirect:
        """
        Returns an instance of OpenDSSDirect.py for the active DSS Context.

        A compatible OpenDSSDirect.py (`pip install OpenDSSDirect.py`) is required.
        """
        from opendssdirect.OpenDSSDirect import OpenDSSDirect
        return OpenDSSDirect._get_instance(ctx=self._api_util.ctx, api_util=self._api_util)
