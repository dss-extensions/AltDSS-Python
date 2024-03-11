from typing import List, Optional
from .enums import ExtraClassIDs
from .types import Float64Array, Int32Array
from .DSSObj import DSSObj
from .CircuitElement import CircuitElementBatch

class PDElementMixin:
    __slots__ = []
    _extra_slots = []

    def EnergyMeter(self) -> Optional[DSSObj]:
        '''
        Energy Meter this element is assigned to.

        *Requires an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/EnergyMeter.html
        '''
        return self._get_obj_from_ptr(self._lib.Alt_PDE_Get_EnergyMeter(self._ptr)) # cannot use the EnergyMeter class here due to circular import

    def EnergyMeterName(self) -> str:
        '''
        Name of the Energy Meter this element is assigned to.

        *Requires an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/EnergyMeter.html
        '''
        return self._get_string(self._lib.Alt_PDE_Get_EnergyMeterName(self._ptr))

    def IsShunt(self) -> bool:
        '''
        Indicates if this PD element should be treated as a shunt element rather than a series element. 
        
        Applies to Capacitor, Reactor, Fault and GICTransformer elements.
        '''
        return self._lib.Alt_PDE_Get_IsShunt(self._ptr) != 0

    def AccumulatedL(self) -> float:
        '''
        Accumulated failure rate for this branch on downline.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/AccumulatedL.html
        '''
        return self._lib.Alt_PDE_Get_AccumulatedL(self._ptr)

    def Lambda(self) -> float:
        '''
        Failure rate for this branch. Faults per year including length of line.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/Lambda1.html
        '''
        return self._lib.Alt_PDE_Get_Lambda(self._ptr)

    def NumCustomers(self) -> int:
        '''
        Number of customers, this branch.

        *Requires an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/Numcustomers.html
        '''
        return self._lib.Alt_PDE_Get_NumCustomers(self._ptr)

    def ParentPDElement(self) -> Optional[DSSObj]:
        '''
        Parent PD element of this element, if any. 
        
        *Requires an energy meter with an updated zone.*
        '''
        return self._get_obj_from_ptr(self._lib.Alt_PDE_Get_ParentPDElement(self._ptr))

    def TotalCustomers(self) -> int:
        '''
        Total number of customers from this branch to the end of the zone
        
        *Requires a circuit with an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/TotalCustomers1.html
        '''
        return self._lib.Alt_PDE_Get_TotalCustomers(self._ptr)

    def FromTerminal(self) -> int:
        '''
        Number of the terminal of this PD element that is on the "from" side. 
        
        *Requires an energy meter with an updated zone.*
        '''
        return self._lib.Alt_PDE_Get_FromTerminal(self._ptr)

    def TotalMiles(self) -> float:
        '''
        Total miles of line from this element to the end of the zone. For recloser siting algorithm.
        
        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/TotalMiles1.html
        '''
        return self._lib.Alt_PDE_Get_TotalMiles(self._ptr)

    def TotalKilometers(self) -> float:
        '''
        Total kilometers of line from this element to the end of the zone. For recloser siting algorithm.
        
        *Requires a previous call to `RelCalc` command*
        '''
        return self._lib.Alt_PDE_Get_TotalMiles(self._ptr) * 1.609344

    def SectionID(self) -> int:
        '''
        Integer ID of the feeder section that this PDElement branch is part of.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/SectionID1.html
        '''
        return self._lib.Alt_PDE_Get_SectionID(self._ptr)

    def pctNormal(self, allNodes=False) -> float:
        '''
        Maximum current across the conductors as a percentage of the **normal** ampere rating.

        By default, only the nodes from the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `allNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        '''
        return self._lib.Alt_PDE_Get_pctNorm(self._ptr, allNodes)

    def pctEmergency(self, allNodes=False) -> float:
        '''
        Maximum current across the conductors as a percentage of the **emergency** ampere rating.

        By default, only the nodes from the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `allNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        '''
        return self._lib.Alt_PDE_Get_pctEmerg(self._ptr, allNodes)


class PDElementBatchMixin:
    __slots__ = []

    def EnergyMeter(self) -> List[Optional[DSSObj]]: #TODO: should we return a batch here?
        '''
        Return the energy meter for each of the elements in this batch.

        *Requires an energy meter with an updated zone.*
        '''
        return [self._get_obj_from_ptr(self._lib.Alt_PDE_Get_EnergyMeter(ptr)) for ptr in self._unpack()]

    def EnergyMeterName(self) -> List[str]:
        '''
        Return the energy meter *name* for each of the elements in this batch.

        *Requires an energy meter with an updated zone.*
        '''
        return [self._get_string(self._lib.Alt_PDE_Get_EnergyMeterName(ptr)) for ptr in self._unpack()]

    def IsShunt(self) -> List[bool]:
        '''
        Indicates if each of the PD elements in the batch should be treated as a shunt element rather than a series element. 
        
        Applies to Capacitor, Reactor, Fault and GICTransformer elements.
        '''
        return [self._lib.Alt_PDE_Get_IsShunt(ptr) != 0 for ptr in self._unpack()]

    def AccumulatedL(self) -> Float64Array:
        '''
        Accumulated failure rate for the branch on downline, for each branch in this batch.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/AccumulatedL.html
        '''
        return self._get_batch_float64_func("Alt_PDE_Get_AccumulatedL")

    def Lambda(self) -> Float64Array:
        '''
        Failure rate for each of the branches in the batch. Faults per year including length of line.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/Lambda1.html
        '''
        return self._get_batch_float64_func("Alt_PDE_Get_Lambda")

    def NumCustomers(self) -> Int32Array:
        '''
        Number of customers for each branch in the batch.

        *Requires an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/Numcustomers.html
        '''
        return self._get_batch_int32_func("Alt_PDE_Get_NumCustomers")

    def ParentPDElement(self) -> List[Optional[DSSObj]]: #TODO: should we return a batch here?
        '''
        Returns the parent PD element for each element in this batch.
        
        *Requires an energy meter with an updated zone.*
        '''
        return [self._get_obj_from_ptr(self._lib.Alt_PDE_Get_ParentPDElement(ptr)) for ptr in self._unpack()]

    def TotalCustomers(self) -> Int32Array:
        '''
        Total number of customers from each branch of this batch to the end of the zone
        
        *Requires a circuit with an energy meter with an updated zone.*

        Original COM help: https://opendss.epri.com/TotalCustomers1.html
        '''
        return self._get_batch_int32_func("Alt_PDE_Get_TotalCustomers")

    def FromTerminal(self) -> Int32Array:
        '''
        Number of the terminal of each PD element of this batch that is on the "from" side. 
        
        *Requires an energy meter with an updated zone.*
        '''
        return self._get_batch_int32_func("Alt_PDE_Get_FromTerminal")

    def TotalMiles(self) -> Float64Array:
        '''
        Total miles of line from this element to the end of the zone. For recloser siting algorithm.
        
        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/TotalMiles1.html
        '''
        return self._get_batch_float64_func("Alt_PDE_Get_TotalMiles")

    def TotalKilometers(self) -> Float64Array:
        '''
        Total kilometers of line from this element to the end of the zone. For recloser siting algorithm.
        
        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/TotalMiles1.html
        '''
        return self._get_batch_float64_func("Alt_PDE_Get_TotalMiles") * 1.609344

    def SectionID(self) -> Int32Array:
        '''
        Integer ID of the feeder section that each PDElement branch in this batch is part of.

        *Requires a previous call to `RelCalc` command*

        Original COM help: https://opendss.epri.com/SectionID1.html
        '''
        return self._get_batch_int32_func("Alt_PDE_Get_SectionID")
    
    def pctNormal(self, allNodes=False) -> Float64Array:
        '''
        For each element in the batch, calculate the maximum current across the conductors as a percentage of the **normal** ampere rating.

        By default, only the nodes from the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `allNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        '''
        return self._get_float64_array(self._lib.Alt_PDEBatch_Get_pctNorm, *self._get_ptr_cnt(), allNodes)

    def pctEmergency(self, allNodes=False) -> Float64Array:
        '''
        For each element in the batch, calculate the maximum current across the conductors as a percentage of the **emergency** ampere rating.

        By default, only the nodes from the *first terminal* is used for the maximum current, matching
        the behavior of the "export capacity" command. Pass `allNodes=True` to 
        force the analysis to all terminals.
        
        See also: 
        https://sourceforge.net/p/electricdss/discussion/beginners/thread/da5b93ca/
        '''
        return self._get_float64_array(self._lib.Alt_PDEBatch_Get_pctEmerg, *self._get_ptr_cnt(), allNodes)


class PDElementBatch(CircuitElementBatch, PDElementBatchMixin):
    '''
    Non-uniform batch of PD elements. Can contain distinct PD types, while providing 
    common functions
    '''

    __slots__ = []

    def __init__(self, func, parent, sync_cls_idx=ExtraClassIDs.PDElements, copy_safe=False):
        CircuitElementBatch.__init__(self, func, parent, sync_cls_idx=sync_cls_idx, copy_safe=copy_safe)
        PDElementBatchMixin.__init__(self)


__all__ = ('PDElementMixin', 'PDElementBatchMixin', 'PDElementBatch',)