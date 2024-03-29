# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from .common import Base
from .types import Float64Array, Int32Array
from typing import AnyStr
from dss.enums import DSSPropertyNameStyle

class ISettings(Base):
    __slots__ = []

    _columns = [
        'Trapezoidal',
        'LossRegs',
        'VoltageBases',
        'ZoneLock',
        'EmergVminpu',
        'PriceSignal',
        'CktModel',
        'UEregs',
        'UEweight',
        'PriceCurve',
        'NormVminpu',
        'LossWeight',
        'EmergVmaxpu',
        'AutoBusList',
        'NormVmaxpu',
        'AllowDuplicates',
        'ControlTrace',
        'LoadsTerminalCheck',
        'IterateDisabled',
    ]

    @property
    def AllowDuplicates(self) -> bool:
        '''
        Designates whether to allow duplicate names of objects
        
        **NOTE**: for DSS-Extensions, we are considering removing this option in a future 
        release since it has performance impacts even when not used.
        '''
        return self._check_for_error(self._lib.Settings_Get_AllowDuplicates()) != 0

    @AllowDuplicates.setter
    def AllowDuplicates(self, Value: bool):
        self._check_for_error(self._lib.Settings_Set_AllowDuplicates(Value))

    @property
    def AutoBusList(self) -> str:
        '''List of Buses or (File=xxxx) syntax for the AutoAdd solution mode.'''
        return self._get_string(self._check_for_error(self._lib.Settings_Get_AutoBusList()))

    @AutoBusList.setter
    def AutoBusList(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Settings_Set_AutoBusList(Value))

    @property
    def CktModel(self) -> int:
        '''{dssMultiphase (0) * | dssPositiveSeq (1) } Indicate if the circuit model is positive sequence.'''
        return self._check_for_error(self._lib.Settings_Get_CktModel())

    @CktModel.setter
    def CktModel(self, Value: int):
        self._check_for_error(self._lib.Settings_Set_CktModel(Value))

    @property
    def ControlTrace(self) -> bool:
        '''{True | False*} Denotes whether to trace the control actions to a file.'''
        return self._check_for_error(self._lib.Settings_Get_ControlTrace()) != 0

    @ControlTrace.setter
    def ControlTrace(self, Value: bool):
        self._check_for_error(self._lib.Settings_Set_ControlTrace(Value))

    @property
    def EmergVmaxpu(self) -> float:
        '''Per Unit maximum voltage for Emergency conditions.'''
        return self._check_for_error(self._lib.Settings_Get_EmergVmaxpu())

    @EmergVmaxpu.setter
    def EmergVmaxpu(self, Value: float):
        self._check_for_error(self._lib.Settings_Set_EmergVmaxpu(Value))

    @property
    def EmergVminpu(self) -> float:
        '''Per Unit minimum voltage for Emergency conditions.'''
        return self._check_for_error(self._lib.Settings_Get_EmergVminpu())

    @EmergVminpu.setter
    def EmergVminpu(self, Value: float):
        self._check_for_error(self._lib.Settings_Set_EmergVminpu(Value))

    @property
    def LossRegs(self) -> Int32Array:
        '''Integer array defining which energy meter registers to use for computing losses'''
        self._check_for_error(self._lib.Settings_Get_LossRegs_GR())
        return self._get_int32_gr_array()

    @LossRegs.setter
    def LossRegs(self, Value: Int32Array):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.Settings_Set_LossRegs(ValuePtr, ValueCount))

    @property
    def LossWeight(self) -> float:
        '''Weighting factor applied to Loss register values.'''
        return self._check_for_error(self._lib.Settings_Get_LossWeight())

    @LossWeight.setter
    def LossWeight(self, Value: float):
        self._check_for_error(self._lib.Settings_Set_LossWeight(Value))

    @property
    def NormVmaxpu(self) -> float:
        '''Per Unit maximum voltage for Normal conditions.'''
        return self._check_for_error(self._lib.Settings_Get_NormVmaxpu())

    @NormVmaxpu.setter
    def NormVmaxpu(self, Value: float):
        self._check_for_error(self._lib.Settings_Set_NormVmaxpu(Value))

    @property
    def NormVminpu(self) -> float:
        '''Per Unit minimum voltage for Normal conditions.'''
        return self._check_for_error(self._lib.Settings_Get_NormVminpu())

    @NormVminpu.setter
    def NormVminpu(self, Value: float):
        self._check_for_error(self._lib.Settings_Set_NormVminpu(Value))

    @property
    def PriceCurve(self) -> str:
        '''Name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.'''
        return self._get_string(self._check_for_error(self._lib.Settings_Get_PriceCurve()))

    @PriceCurve.setter
    def PriceCurve(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.Settings_Set_PriceCurve(Value))

    @property
    def PriceSignal(self) -> float:
        '''Price Signal for the Circuit'''
        return self._check_for_error(self._lib.Settings_Get_PriceSignal())

    @PriceSignal.setter
    def PriceSignal(self, Value: float):
        self._check_for_error(self._lib.Settings_Set_PriceSignal(Value))

    @property
    def Trapezoidal(self) -> bool:
        '''Gets value of trapezoidal integration flag in energy meters. Defaults to `False`.'''
        return self._check_for_error(self._lib.Settings_Get_Trapezoidal()) != 0

    @Trapezoidal.setter
    def Trapezoidal(self, Value: bool):
        self._check_for_error(self._lib.Settings_Set_Trapezoidal(Value))

    @property
    def UEregs(self) -> Int32Array:
        '''Array of Integers defining energy meter registers to use for computing UE'''
        self._check_for_error(self._lib.Settings_Get_UEregs_GR())
        return self._get_int32_gr_array()

    @UEregs.setter
    def UEregs(self, Value: Int32Array):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._check_for_error(self._lib.Settings_Set_UEregs(ValuePtr, ValueCount))

    @property
    def UEweight(self) -> float:
        '''Weighting factor applied to UE register values.'''
        return self._check_for_error(self._lib.Settings_Get_UEweight())

    @UEweight.setter
    def UEweight(self, Value: float):
        self._check_for_error(self._lib.Settings_Set_UEweight(Value))

    @property
    def VoltageBases(self) -> Float64Array:
        '''Array of doubles defining the legal voltage bases in kV L-L'''
        self._check_for_error(self._lib.Settings_Get_VoltageBases_GR())
        return self._get_float64_gr_array()

    @VoltageBases.setter
    def VoltageBases(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._check_for_error(self._lib.Settings_Set_VoltageBases(ValuePtr, ValueCount))

    @property
    def ZoneLock(self) -> bool:
        '''{True | False*}  Locks Zones on energy meters to prevent rebuilding if a circuit change occurs.'''
        return self._check_for_error(self._lib.Settings_Get_ZoneLock()) != 0

    @ZoneLock.setter
    def ZoneLock(self, Value: bool):
        self._check_for_error(self._lib.Settings_Set_ZoneLock(Value))

    @property
    def AllocationFactors(self):
        '''(write-only) Sets all load allocation factors for all loads defined by XFKVA property to this value.'''
        raise AttributeError("This property is write-only!")

    @AllocationFactors.setter
    def AllocationFactors(self, Value: float):
        self._check_for_error(self._lib.Settings_Set_AllocationFactors(Value))

    @property
    def LoadsTerminalCheck(self) -> bool:
        '''
        Controls whether the terminals are checked when updating the currents in Load component. Defaults to True.
        If the loads are guaranteed to have their terminals closed throughout the simulation, this can be set to False to save some time.
        
        (API Extension)
        '''
        return self._check_for_error(self._lib.Settings_Get_LoadsTerminalCheck()) != 0

    @LoadsTerminalCheck.setter
    def LoadsTerminalCheck(self, Value: bool):
        self._check_for_error(self._lib.Settings_Set_LoadsTerminalCheck(Value))
        
    @property
    def IterateDisabled(self) -> int:
        '''
        Controls whether `First`/`Next` iteration includes or skips disabled circuit elements.
        The default behavior from OpenDSS is to skip those. The user can still activate the element by name or index.
        
        The default value for IterateDisabled is 0, keeping the original behavior.
        Set it to 1 (or `True`) to include disabled elements.
        Other numeric values are reserved for other potential behaviors.
        
        (API Extension)
        '''
        return self._check_for_error(self._lib.Settings_Get_IterateDisabled())

    @IterateDisabled.setter
    def IterateDisabled(self, Value: int):
        self._check_for_error(self._lib.Settings_Set_IterateDisabled(Value))

    @property
    def AdvancedTypes(self) -> bool:
        '''
        When enabled, there are **two side-effects**:
        
        - **Per DSS Context:** Complex arrays and complex numbers can be returned and consumed by the Python API.
        - **Global effect:** The low-level API provides matrix dimensions when available (`EnableArrayDimensions` is enabled).
        
        As a result, for example, `DSS.ActiveCircuit.ActiveCktElement.Yprim` is returned as a complex matrix instead
        of a plain array.
        
        When disabled, the legacy plain arrays are used and complex numbers cannot be consumed by the Python API.

        *Defaults to **False** for backwards compatibility.*
        
        (API Extension)
        '''
        
        arr_dim = self._check_for_error(self._lib.DSS_Get_EnableArrayDimensions()) != 0
        allow_complex = self._api_util._allow_complex
        return arr_dim and allow_complex

    @AdvancedTypes.setter
    def AdvancedTypes(self, Value: bool):
        self._check_for_error(self._lib.DSS_Set_EnableArrayDimensions(Value))
        self._api_util._allow_complex = bool(Value)

    @property
    def CompatFlags(self) -> int:
        '''
        Controls some compatibility flags introduced to toggle some behavior from the official OpenDSS.

        **THESE FLAGS ARE GLOBAL, affecting all DSS engines in the process.**

        The current bit flags are:

        - 0x1 (bit 0): If enabled, don't check for NaNs in the inner solution loop. This can lead to various errors.
            This flag is useful for legacy applications that don't handle OpenDSS API errors properly. Through the 
            development of DSS-Extensions, we noticed this is actually a quite common issue.
        - 0x2 (bit 1): Toggle worse precision for certain aspects of the engine. For example, the sequence-to-phase 
            (`As2p`) and sequence-to-phase (`Ap2s`) transform matrices. On DSS C-API, we fill the matrix explicitly
            using higher precision, while numerical inversion of an initially worse precision matrix is used in the 
            official OpenDSS. We will introduce better precision for other aspects of the engine in the future, 
            so this flag can be used to toggle the old/bad values where feasible.
        - 0x4 (bit 2): Toggle some InvControl behavior introduced in OpenDSS 9.6.1.1. It could be a regression 
            but needs further investigation, so we added this flag in the time being.

        These flags may change for each version of DSS C-API, but the same value will not be reused. That is,
        when we remove a compatibility flag, it will have no effect but will also not affect anything else
        besides raising an error if the user tries to toggle a flag that was available in a previous version.

        We expect to keep a very limited number of flags. Since the flags are more transient than the other
        options/flags, it was preferred to add this generic function instead of a separate function per
        flag.

        Related enumeration: DSSCompatFlags

        (API Extension)
        '''
        return self._check_for_error(self._lib.DSS_Get_CompatFlags())

    @CompatFlags.setter
    def CompatFlags(self, Value: int):
        self._check_for_error(self._lib.DSS_Set_CompatFlags(Value))

    @property
    def AllowForms(self) -> bool:
        '''Gets/sets whether text output is allowed'''
        return self._check_for_error(self._lib.DSS_Get_AllowForms()) != 0

    @AllowForms.setter
    def AllowForms(self, value: bool):
        self._check_for_error(self._lib.DSS_Set_AllowForms(value))

    @property
    def AllowEditor(self) -> bool:
        '''
        Gets/sets whether running the external editor for "Show" is allowed
        
        AllowEditor controls whether the external editor is used in commands like "Show".
        If you set to 0 (false), the editor is not executed. Note that other side effects,
        such as the creation of files, are not affected.

        (API Extension)
        '''
        return self._check_for_error(self._lib.DSS_Get_AllowEditor()) != 0

    @AllowEditor.setter
    def AllowEditor(self, value: bool):
        self._check_for_error(self._lib.DSS_Set_AllowEditor(value))

    @property
    def DataPath(self) -> str:
        '''DSS Data File Path.  Default path for reports, etc. from DSS'''
        return self._get_string(self._check_for_error(self._lib.DSS_Get_DataPath()))

    @DataPath.setter
    def DataPath(self, Value: AnyStr):
        if not isinstance(Value, bytes):
            Value = Value.encode(self._api_util.codec)

        self._check_for_error(self._lib.DSS_Set_DataPath(Value))

    @property
    def DefaultEditor(self) -> str:
        '''Returns the path name for the default text editor.'''
        return self._get_string(self._check_for_error(self._lib.DSS_Get_DefaultEditor()))

    def SetPropertyNameStyle(self, value: DSSPropertyNameStyle):
        '''Switch the property names according'''
        self._check_for_error(self._lib.Settings_SetPropertyNameStyle(value))

    @property
    def AllowChangeDir(self) -> bool:
        '''
        If disabled, the engine will not change the active working directory during execution. E.g. a "compile"
        command will not "chdir" to the file path.
        
        If you have issues with long paths, enabling this might help in some scenarios.
        
        Defaults to True (allow changes, backwards compatible) in the 0.10.x versions of DSS C-API. 
        This might change to False in future versions.
        
        This can also be set through the environment variable DSS_CAPI_ALLOW_CHANGE_DIR. Set it to 0 to
        disallow changing the active working directory.
        
        **(API Extension)**
        '''
        return self._check_for_error(self._lib.DSS_Get_AllowChangeDir()) != 0

    @AllowChangeDir.setter
    def AllowChangeDir(self, Value: bool):
        self._check_for_error(self._lib.DSS_Set_AllowChangeDir(Value))

    @property
    def AllowDOScmd(self) -> bool:
        '''
        If enabled, the `DOScmd` command is allowed. Otherwise, an error is reported if the user tries to use it.

        Defaults to False/0 (disabled state). Users should consider DOScmd deprecated on DSS-Extensions.

        This can also be set through the environment variable DSS_CAPI_ALLOW_DOSCMD. Setting it to 1 enables
        the command.

        **(API Extension)**
        '''
        return self._check_for_error(self._lib.DSS_Get_AllowDOScmd()) != 0

    @AllowDOScmd.setter
    def AllowDOScmd(self, Value: bool):
        self._check_for_error(self._lib.DSS_Set_AllowDOScmd(Value))

    @property
    def COMErrorResults(self) -> bool:
        '''
        If enabled, in case of errors or empty arrays, the API returns arrays with values compatible with the 
        official OpenDSS COM interface. 

        For example, consider the function `Loads_Get_ZIPV`. If there is no active circuit or active load element:

        - In the disabled state (COMErrorResults=False), the function will return "[]", an array with 0 elements.
        - In the enabled state (COMErrorResults=True), the function will return "[0.0]" instead. This should
        be compatible with the return value of the official COM interface.

        Defaults to True/1 (enabled state) in the v0.12.x series. This will change to false in future series.

        This can also be set through the environment variable `DSS_CAPI_COM_DEFAULTS`. Setting it to 0 disables
        the legacy/COM behavior. The value can be toggled through the API at any time.

        **(API Extension)**
        '''
        return self._check_for_error(self._lib.DSS_Get_COMErrorResults()) != 0

    @COMErrorResults.setter
    def COMErrorResults(self, Value: bool):
        self._check_for_error(self._lib.DSS_Set_COMErrorResults(Value))