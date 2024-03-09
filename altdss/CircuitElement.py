from typing import Dict, List, Union, AnyStr
from dss.enums import OCPDevType
from .enums import ExtraClassIDs
from .types import Float64Array, Int32Array, ComplexArray, BoolArray
from .Batch import NonUniformBatch
from .DSSObj import DSSObj

class CircuitElementMixin:
    __slots__ = [] 
    # To avoid layout issues, let the final class use the following instead
    _extra_slots = ['Controllers', ]

    def __init__(self, *args):
        self.Controllers = NonUniformBatch(self._lib.Alt_CE_Get_Controllers, self)
        '''Controllers attached to this element.'''

    def GUID(self) -> str:
        '''
        Object's GUID/UUID. Currently used only in the CIM-related methods.

        Original COM help: https://opendss.epri.com/GUID.html
        '''
        return self._get_string(self._lib.Alt_CE_Get_GUID(self._ptr))

    def _get_DisplayName(self) -> str:
        return self._get_string(self._lib.Alt_CE_Get_DisplayName(self._ptr))
    
    def _set_DisplayName(self, value: AnyStr):
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Alt_CE_Set_DisplayName(self._ptr, value)

    DisplayName = property(_get_DisplayName, _set_DisplayName) # type: str
    '''
    Display name of the object (not necessarily unique)

    Original COM help: https://opendss.epri.com/DisplayName.html
    '''

    # TODO: is BusNames too redundant to keep?
    # def GetBusNames(self) -> List[str]:
    #     return self._get_string_array(self._lib.Alt_CE_Get_BusNames, self._ptr)

    # def SetBusNames(self, value: List[AnyStr]):
    #     value, value_ptr, value_count = self._prepare_string_array(value)
    #     self._lib.Alt_CE_Set_BusNames(self._ptr, value_ptr, value_count)

    # BusNames = property(GetBusNames, SetBusNames)

    def Handle(self) -> int:
        '''
        Index of this element into the circuit's element list.

        Original COM help: https://opendss.epri.com/Handle.html
        '''
        return self._lib.Alt_CE_Get_Handle(self._ptr)

    def NumConductors(self) -> int:
        '''
        Number of conductors per terminal

        Original COM help: https://opendss.epri.com/NumConductors.html
        '''
        return self._lib.Alt_CE_Get_NumConductors(self._ptr)

    def NumPhases(self) -> int: #TODO remove? Redundant
        '''
        Number of phases

        Original COM help: https://opendss.epri.com/NumPhases.html
        '''
        return self._lib.Alt_CE_Get_NumPhases(self._ptr)

    def NumTerminals(self) -> int:
        '''
        Number of terminals in this circuit element

        Original COM help: https://opendss.epri.com/NumTerminals.html
        '''
        return self._lib.Alt_CE_Get_NumTerminals(self._ptr)

    def NumControllers(self) -> int:
        '''
        Number of controllers connected to this device. 

        Original COM help: https://opendss.epri.com/NumControls.html
        '''
        return self._lib.Alt_CE_Get_NumControllers(self._ptr)

    def OCPDevice(self) -> Union[DSSObj, None]:
        '''
        Returns (as a Python object) the OCP device controlling this element, if any.
        '''
        return self._get_obj_from_ptr(self._lib.Alt_CE_Get_OCPDevice(self._ptr))

    def OCPDeviceIndex(self) -> int:
        '''
        Index into controller list of OCP Device controlling this circuit element

        Original COM help: https://opendss.epri.com/OCPDevIndex.html
        '''
        return self._lib.Alt_CE_Get_OCPDeviceIndex(self._ptr)

    def OCPDeviceType(self) -> OCPDevType:
        '''
        Type of OCP controller device

        Original COM help: https://opendss.epri.com/OCPDevType.html
        '''
        return OCPDevType(self._lib.Alt_CE_Get_OCPDeviceType(self._ptr))

    def IsIsolated(self) -> bool:
        '''
        Returns true if the element is isolated.
        Note that this only fetches the current value. See also the Topology interface.
        '''
        return self._lib.Alt_CE_Get_IsIsolated(self._ptr) != 0

    def HasOCPDevice(self) -> bool:
        '''
        Returns true if a recloser, relay, or fuse controlling the circuit element.

        OCP = Overcurrent Protection 

        Original COM help: https://opendss.epri.com/HasOCPDevice.html
        '''
        return self._lib.Alt_CE_Get_HasOCPDevice(self._ptr) != 0

    def HasSwitchControl(self) -> bool:
        '''
        Returns true if the element has a SwtControl attached.

        Original COM help: https://opendss.epri.com/HasSwitchControl.html
        '''
        return self._lib.Alt_CE_Get_HasSwitchControl(self._ptr) != 0

    def HasVoltControl(self) -> bool:
        '''
        Returns true if the element has a CapControl or RegControl attached.

        Original COM help: https://opendss.epri.com/HasVoltControl.html
        '''
        return self._lib.Alt_CE_Get_HasVoltControl(self._ptr) != 0

    def IsOpen(self, terminal: int, phase: int) -> bool:
        '''
        Returns true if the specified terminal and phase are open.

        If the `phase` parameter is zero, returns if **any** conductor at the terminal is open.
        '''
        return self._lib.Alt_CE_IsOpen(self._ptr, terminal, phase) != 0

    def MaxCurrent(self, terminal: int) -> float:
        '''
        Returns the maximum current (magnitude) at the specified terminal. 
        Use -1 as terminal to get the value across all terminals.
        '''
        return self._lib.Alt_CE_MaxCurrent(self._ptr, terminal)

    def Open(self, terminal: int, phase: int) -> None:
        '''
        Open the specified terminal and phase, if non-zero, or all conductors at the terminal.

        Original COM help: https://opendss.epri.com/Open1.html
        '''
        self._lib.Alt_CE_Open(self._ptr, terminal, phase)

    def Close(self, terminal: int, phase: int) -> None:
        '''
        Close the specified terminal and phase, if non-zero, or all conductors at the terminal.

        Original COM help: https://opendss.epri.com/Close1.html
        '''
        self._lib.Alt_CE_Close(self._ptr, terminal, phase)

    def NodeOrder(self) -> Int32Array:
        '''
        Array of integer containing the node numbers (representing phases, for example) for each conductor of each terminal.

        Be sure to run a solution to initialize the values after the circuit is created or modified.
        '''
        return self._get_int32_array(self._lib.Alt_CE_Get_NodeOrder, self._ptr)

    def NodeRef(self) -> Int32Array:
        '''
        Array of integers, a copy of the internal NodeRef of the CktElement.

        Be sure to run a solution to initialize the values after the circuit is created or modified.
        '''
        return self._get_int32_array(self._lib.Alt_CE_Get_NodeRef, self._ptr)

    def ComplexSeqVoltages(self) -> ComplexArray:
        '''
        Complex double array of Sequence Voltage for all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqVoltages1.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_ComplexSeqVoltages, self._ptr)

    def ComplexSeqCurrents(self) -> ComplexArray:
        '''
        Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqCurrents.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_ComplexSeqCurrents, self._ptr)

    def Currents(self) -> ComplexArray:
        '''
        Complex array of currents into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Currents1.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Currents, self._ptr)

    def Voltages(self) -> ComplexArray:
        '''
        Complex array of voltages at terminals

        Original COM help: https://opendss.epri.com/Voltages1.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Voltages, self._ptr)

    def Losses(self) -> complex:
        '''
        Total (complex) losses in the element, in VA (watts, vars)
        
        Original COM help: https://opendss.epri.com/Losses1.html
        '''
        return self._get_fcomplex128_simple(self._lib.Alt_CE_Get_Losses, self._ptr)

    def PhaseLosses(self) -> ComplexArray:
        '''
        Complex array of losses (kVA) by phase

        Original COM help: https://opendss.epri.com/PhaseLosses.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_PhaseLosses, self._ptr)

    def Powers(self) -> ComplexArray:
        '''
        Complex array of powers (kVA) into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Powers.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Powers, self._ptr)

    def SeqCurrents(self) -> Float64Array:
        '''
        Array of symmetrical component currents (magnitudes only) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqCurrents.html
        '''
        return self._get_float64_array(self._lib.Alt_CE_Get_SeqCurrents, self._ptr)

    def SeqPowers(self) -> ComplexArray:
        '''
        Complex array of sequence powers (kW, kvar) into each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqPowers.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_SeqPowers, self._ptr)

    def SeqVoltages(self) -> Float64Array:
        '''
        Double array of symmetrical component voltages (magnitudes only) at each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqVoltages1.html
        '''
        return self._get_float64_array(self._lib.Alt_CE_Get_SeqVoltages, self._ptr)

    def Residuals(self) -> Float64Array:
        '''
        Residual currents for each terminal: (magnitude, angle in degrees)

        Original COM help: https://opendss.epri.com/Residuals.html
        '''
        return self._get_float64_array(self._lib.Alt_CE_Get_Residuals, self._ptr)

    def YPrim(self) -> ComplexArray:
        '''
        YPrim matrix, column order, complex numbers

        Original COM help: https://opendss.epri.com/Yprim.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_YPrim, self._ptr)

    def VoltagesMagAng(self) -> Float64Array:
        '''
        Voltages at each conductor in magnitude, angle form as array of doubles.

        Original COM help: https://opendss.epri.com/VoltagesMagAng.html
        '''
        return self._get_float64_array(self._lib.Alt_CE_Get_VoltagesMagAng, self._ptr)

    def TotalPowers(self) -> ComplexArray:
        '''
        Returns an array with the total powers (complex, kVA) at ALL terminals of the active circuit element.

        Original COM help: https://opendss.epri.com/TotalPowers.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_TotalPowers, self._ptr)


class CircuitElementBatchMixin:
    __slots__ = []

    def GUID(self) -> List[str]:
        '''
        GUID/UUID for each object. Currently used only in the CIM-related methods.

        Original COM help: https://opendss.epri.com/GUID.html
        '''
        return [self._get_string(self._lib.Alt_CE_Get_GUID(ptr)) for ptr in self._unpack()]

    def Handle(self) -> Int32Array:
        '''
        Index of each element into the circuit's element list.

        Original COM help: https://opendss.epri.com/Handle.html
        '''
        return self._get_batch_int32_func("Alt_CE_Get_Handle")

    def NumConductors(self) -> Int32Array:
        '''
        Number of conductors per terminal for each element in the batch.

        Original COM help: https://opendss.epri.com/NumConductors.html
        '''
        return self._get_batch_int32_func("Alt_CE_Get_NumConductors")

    def NumPhases(self) -> Int32Array:
        '''
        Number of Phases for each element in this batch.

        Original COM help: https://opendss.epri.com/NumPhases.html
        '''
        return self._get_batch_int32_func("Alt_CE_Get_NumPhases")

    def NumTerminals(self) -> Int32Array:
        '''
        Number of terminals for each Circuit Element in the batch.

        Original COM help: https://opendss.epri.com/NumTerminals.html
        '''
        return self._get_batch_int32_func("Alt_CE_Get_NumTerminals")

    def NumControllers(self) -> Int32Array:
        '''
        Number of controllers connected to each device in the batch.

        Original COM help: https://opendss.epri.com/NumControls.html
        '''
        return self._get_batch_int32_func("Alt_CE_Get_NumControllers")

    def OCPDevice(self) -> List[Union[DSSObj, None]]: #TODO: use batch?
        '''
        Returns (as a list of Python objects) the OCP device controlling each element.
        '''
        return [self._get_obj_from_ptr(self._lib.Alt_CE_Get_OCPDevice(ptr)) for ptr in self._unpack()]

    def OCPDeviceIndex(self) -> Int32Array:
        '''
        For each element in the batch: index into each controller list of the OCP Device controlling each circuit element

        Original COM help: https://opendss.epri.com/OCPDevIndex.html
        '''
        return self._get_batch_int32_func("Alt_CE_Get_OCPDeviceIndex")

    def OCPDeviceType(self) -> List[OCPDevType]:
        '''
        For each element in the batch: type of OCP controller device

        Original COM help: https://opendss.epri.com/OCPDevType.html
        '''
        return [
            OCPDevType(val) for val in self._get_batch_int32_func("Alt_CE_Get_OCPDeviceType")
        ]

    def MaxCurrent(self, terminal: int) -> Float64Array:
        '''
        Returns the maximum current (magnitude) at the specified terminal for each element in this batch. 
        Use -1 as terminal to get the value across all terminals.
        '''
        return self._get_batch_float64_int32_func("Alt_CE_MaxCurrent", terminal)
    
    def IsIsolated(self) -> BoolArray:
        '''
        For each element in the batch: returns true if the element is isolated.
        Note that this only fetches the current value. See also the Topology interface.
        '''
        return self._get_batch_int32_func("Alt_CE_Get_IsIsolated").astype(bool)

    def HasOCPDevice(self) -> BoolArray:
        '''
        For each element in the batch: returns true if a recloser, relay, or fuse controlling the circuit element.

        OCP = Overcurrent Protection 

        Original COM help: https://opendss.epri.com/HasOCPDevice.html
        '''
        return self._get_batch_int32_func("Alt_CE_Get_HasOCPDevice").astype(bool)

    def HasSwitchControl(self) -> BoolArray:
        '''
        For each element in the batch: returns true if the element has a SwtControl attached.

        Original COM help: https://opendss.epri.com/HasSwitchControl.html
        '''
        return self._get_batch_int32_func("Alt_CE_Get_HasSwitchControl").astype(bool)

    def HasVoltControl(self) -> BoolArray:
        '''
        For each element in the batch: returns true if the element has a CapControl or RegControl attached.

        Original COM help: https://opendss.epri.com/HasVoltControl.html
        '''
        return self._get_batch_int32_func("Alt_CE_Get_HasVoltControl").astype(bool)

    def Powers(self) -> ComplexArray:
        '''
        Complex array of powers (kVA) into each conductor of each terminal, of each element in the batch.

        Original COM help: https://opendss.epri.com/Powers.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Powers, *self._get_ptr_cnt())

    def Losses(self) -> ComplexArray:
        '''
        For each element in the batch: total losses in the element, in VA (watts, vars).

        Original COM help: https://opendss.epri.com/Losses1.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Losses, *self._get_ptr_cnt())

    def PhaseLosses(self) -> ComplexArray:
        '''
        Complex array of losses (kVA) by phase

        Original COM help: https://opendss.epri.com/PhaseLosses.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_PhaseLosses, *self._get_ptr_cnt())

    def TotalPowers(self) -> ComplexArray:
        '''
        Returns an array with the total powers (complex, kVA) at all terminals of the circuit elements in this batch.

        The resulting array is equivalent to concatenating the TotalPowers for each element.        
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_TotalPowers, *self._get_ptr_cnt())

    def SeqPowers(self) -> ComplexArray:
        '''
        Complex array of sequence powers (kW, kvar) into each 3-phase terminal of each element

        Original COM help: https://opendss.epri.com/SeqPowers.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_SeqPowers, *self._get_ptr_cnt())

    def SeqCurrents(self) -> Float64Array:
        '''
        Array of symmetrical component currents (magnitudes only) into each 3-phase terminal of each element

        Original COM help: https://opendss.epri.com/SeqCurrents.html
        '''
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_SeqCurrents, *self._get_ptr_cnt())
        
    def ComplexSeqCurrents(self) -> ComplexArray:
        '''
        Complex double array of Sequence Currents for all conductors of all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqCurrents.html
        '''
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_ComplexSeqCurrents, *self._get_ptr_cnt())

    def Currents(self) -> ComplexArray:
        '''
        Complex array of currents into each conductor of each terminal

        Original COM help: https://opendss.epri.com/Currents1.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Currents, *self._get_ptr_cnt())

    def CurrentsMagAng(self) -> Float64Array:
        '''
        Currents in magnitude, angle (degrees) format as a array of doubles.

        Original COM help: https://opendss.epri.com/CurrentsMagAng.html
        '''
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_CurrentsMagAng, *self._get_ptr_cnt())

    def Voltages(self) -> ComplexArray:
        '''
        Complex array of voltages at terminals

        Original COM help: https://opendss.epri.com/Voltages1.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Voltages, *self._get_ptr_cnt())

    def SeqVoltages(self) -> Float64Array:
        '''
        Double array of symmetrical component voltages (magnitudes only) at each 3-phase terminal

        Original COM help: https://opendss.epri.com/SeqVoltages1.html
        '''
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_SeqVoltages, *self._get_ptr_cnt())

    def VoltagesMagAng(self) -> Float64Array:
        '''
        Voltages at each conductor in magnitude, angle form as array of doubles.

        Original COM help: https://opendss.epri.com/VoltagesMagAng.html
        '''
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_VoltagesMagAng, *self._get_ptr_cnt())

    def ComplexSeqVoltages(self) -> ComplexArray:
        '''
        Complex double array of Sequence Voltage for all terminals of active circuit element.

        Original COM help: https://opendss.epri.com/CplxSeqVoltages1.html
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_ComplexSeqVoltages, *self._get_ptr_cnt())


class ElementHasRegistersMixin:
    __slots__ = []
    _extra_slots = []

    def RegisterNames(self) -> List[str]:
        '''
        List of names of the energy meter registers for this element.
        
        See also the enums `EnergyMeterRegisters` and `GeneratorRegisters`.
        '''
        return self._get_string_array(self._lib.Alt_CE_Get_RegisterNames, self._ptr)

    def RegisterValues(self) -> Float64Array:
        '''
        Array of values in this element's energy meter registers.

        Original COM help: https://opendss.epri.com/RegisterValues.html
        '''
        return self._get_float64_array(self._lib.Alt_CE_Get_RegisterValues, self._ptr)

    def RegistersDict(self) -> Dict[str, float]:
        '''
        Convenience function: returns a dict of the element's energy meter register names mapping to their current values.
        '''
        return dict(zip(self.RegisterNames(), self.RegisterValues()))


class CircuitElementBatch(NonUniformBatch, CircuitElementBatchMixin):
    '''
    Non-uniform batch of circuit elements. Can contain distinct types, while providing 
    common functions
    '''

    __slots__ = []

    def __init__(self, func, parent, sync_cls_idx=ExtraClassIDs.CktElements, copy_safe=False):
        NonUniformBatch.__init__(self, func, parent, sync_cls_idx=sync_cls_idx, copy_safe=copy_safe)
        CircuitElementBatchMixin.__init__(self)
