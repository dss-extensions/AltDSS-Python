'''
A compatibility layer for DSS C-API that mimics the official OpenDSS COM interface.

Copyright (c) 2016-2018 Paulo Meira
'''
from __future__ import absolute_import
from .._cffi_api_util import Base

class ISettings(Base):
    __slots__ = []

    @property
    def AllowDuplicates(self):
        '''{True | False*} Designates whether to allow duplicate names of objects'''
        return self._lib.Settings_Get_AllowDuplicates() != 0

    @AllowDuplicates.setter
    def AllowDuplicates(self, Value):
        self._lib.Settings_Set_AllowDuplicates(Value)

    @property
    def AutoBusList(self):
        '''List of Buses or (File=xxxx) syntax for the AutoAdd solution mode.'''
        return self._get_string(self._lib.Settings_Get_AutoBusList())

    @AutoBusList.setter
    def AutoBusList(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Settings_Set_AutoBusList(Value)

    @property
    def CktModel(self):
        '''{dssMultiphase * | dssPositiveSeq} IIndicate if the circuit model is positive sequence.'''
        return self._lib.Settings_Get_CktModel()

    @CktModel.setter
    def CktModel(self, Value):
        self._lib.Settings_Set_CktModel(Value)

    @property
    def ControlTrace(self):
        '''{True | False*} Denotes whether to trace the control actions to a file.'''
        return self._lib.Settings_Get_ControlTrace() != 0

    @ControlTrace.setter
    def ControlTrace(self, Value):
        self._lib.Settings_Set_ControlTrace(Value)

    @property
    def EmergVmaxpu(self):
        '''Per Unit maximum voltage for Emergency conditions.'''
        return self._lib.Settings_Get_EmergVmaxpu()

    @EmergVmaxpu.setter
    def EmergVmaxpu(self, Value):
        self._lib.Settings_Set_EmergVmaxpu(Value)

    @property
    def EmergVminpu(self):
        '''Per Unit minimum voltage for Emergency conditions.'''
        return self._lib.Settings_Get_EmergVminpu()

    @EmergVminpu.setter
    def EmergVminpu(self, Value):
        self._lib.Settings_Set_EmergVminpu(Value)

    @property
    def LossRegs(self):
        '''Integer array defining which energy meter registers to use for computing losses'''
        return self._get_int32_array(self._lib.Settings_Get_LossRegs)

    @LossRegs.setter
    def LossRegs(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Settings_Set_LossRegs(ValuePtr, ValueCount)

    @property
    def LossWeight(self):
        '''Weighting factor applied to Loss register values.'''
        return self._lib.Settings_Get_LossWeight()

    @LossWeight.setter
    def LossWeight(self, Value):
        self._lib.Settings_Set_LossWeight(Value)

    @property
    def NormVmaxpu(self):
        '''Per Unit maximum voltage for Normal conditions.'''
        return self._lib.Settings_Get_NormVmaxpu()

    @NormVmaxpu.setter
    def NormVmaxpu(self, Value):
        self._lib.Settings_Set_NormVmaxpu(Value)

    @property
    def NormVminpu(self):
        '''Per Unit minimum voltage for Normal conditions.'''
        return self._lib.Settings_Get_NormVminpu()

    @NormVminpu.setter
    def NormVminpu(self, Value):
        self._lib.Settings_Set_NormVminpu(Value)

    @property
    def PriceCurve(self):
        '''Name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.'''
        return self._get_string(self._lib.Settings_Get_PriceCurve())

    @PriceCurve.setter
    def PriceCurve(self, Value):
        if type(Value) is not bytes:
            Value = Value.encode(self._api_util.codec)

        self._lib.Settings_Set_PriceCurve(Value)

    @property
    def PriceSignal(self):
        '''Price Signal for the Circuit'''
        return self._lib.Settings_Get_PriceSignal()

    @PriceSignal.setter
    def PriceSignal(self, Value):
        self._lib.Settings_Set_PriceSignal(Value)

    @property
    def Trapezoidal(self):
        '''{True | False *} Gets value of trapezoidal integration flag in energy meters.'''
        return self._lib.Settings_Get_Trapezoidal() != 0

    @Trapezoidal.setter
    def Trapezoidal(self, Value):
        self._lib.Settings_Set_Trapezoidal(Value)

    @property
    def UEregs(self):
        '''Array of Integers defining energy meter registers to use for computing UE'''
        return self._get_int32_array(self._lib.Settings_Get_UEregs)

    @UEregs.setter
    def UEregs(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Settings_Set_UEregs(ValuePtr, ValueCount)

    @property
    def UEweight(self):
        '''Weighting factor applied to UE register values.'''
        return self._lib.Settings_Get_UEweight()

    @UEweight.setter
    def UEweight(self, Value):
        self._lib.Settings_Set_UEweight(Value)

    @property
    def VoltageBases(self):
        '''Array of doubles defining the legal voltage bases in kV L-L'''
        return self._get_float64_array(self._lib.Settings_Get_VoltageBases)

    @VoltageBases.setter
    def VoltageBases(self, Value):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Settings_Set_VoltageBases(ValuePtr, ValueCount)

    @property
    def ZoneLock(self):
        '''{True | False*}  Locks Zones on energy meters to prevent rebuilding if a circuit change occurs.'''
        return self._lib.Settings_Get_ZoneLock() != 0

    @ZoneLock.setter
    def ZoneLock(self, Value):
        self._lib.Settings_Set_ZoneLock(Value)

    @property
    def AllocationFactors(self):
        '''(write-only) Sets all load allocation factors for all loads defined by XFKVA property to this value.'''
        raise AttributeError("This property is write-only!")

    @AllocationFactors.setter
    def AllocationFactors(self, Value):
        self._lib.Settings_Set_AllocationFactors(Value)