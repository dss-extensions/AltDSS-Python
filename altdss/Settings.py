# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from .common import Base, InvalidatedObjectIterator
from .types import Float64Array, Int32Array
from typing import AnyStr, Union, List
from dss.enums import DSSPropertyNameStyle, CktModels
from .DSSObj import DSSObj

class MapToIterators:
    def __init__(self, settings):
        self._api_util = settings._api_util
        self._previous_state = None
        self._tmp_it_objs = [None] * (self._api_util.lib.DSS_Get_NumClasses() + 1)

    def __enter__(self):
        self._previous_state = self._api_util._map_objs
        self._api_util._map_objs = self

    def _map_obj(self, obj_cls: int, ptr) -> DSSObj:
        idx = obj_cls._cls_idx
        it_obj = self._tmp_it_objs[idx]
        if it_obj is None:
            it_obj = obj_cls(self._api_util, InvalidatedObjectIterator)
            it_obj._is_iterator = True
            self._tmp_it_objs[idx] = it_obj

        it_obj._ptr = ptr
        return it_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._api_util._map_objs = self._previous_state
        # Invalidate our temporary iterators
        for it_obj in self._tmp_it_objs:
            if it_obj is None:
                continue

            it_obj._ptr = InvalidatedObjectIterator


class ISettings(Base):
    __slots__ = [
        '_command_dict'
    ]

    _columns = [
        'AdvancedTypes',
        'AllowChangeDir',
        'AllowDOScmd',
        'AllowDuplicates',
        'AllowEditor',
        'AllowForms',
        'AutoBusList',
        'CircuitModel',
        'COMErrorResults',
        'CompatFlags',
        'ControlTrace',
        'DataPath',
        'DefaultEditor',
        'EmergVMaxpu',
        'EmergVMinpu',
        'IterateDisabled',
        'LoadsTerminalCheck',
        'LossRegisters',
        'LossWeight',
        'NormalVMaxpu',
        'NormalVMinpu',
        'PriceCurve',
        'PriceSignal',
        'SkipCommands',
        'SkipFileRegExp',
        'Trapezoidal',
        'UERegisters',
        'UEWeight',
        'VoltageBases',
        'ZoneLock',
    ]

    def __init__(self, api_util):
        Base.__init__(self, api_util)
        num_commands = self._lib.DSS_Executive_Get_NumCommands()
        self._command_dict = {
            self._lib.DSS_Executive_Get_Command(i).lower(): i
            for i in range(1, num_commands + 1)
        }

    @property
    def AllowDuplicates(self) -> bool:
        '''
        Designates whether to allow duplicate names of objects

        False by default.
        
        **NOTE**: for DSS-Extensions, we are considering removing this option in a future 
        release since it has performance impacts even when not used.
        '''
        return self._lib.Settings_Get_AllowDuplicates()

    @AllowDuplicates.setter
    def AllowDuplicates(self, Value: bool):
        self._lib.Settings_Set_AllowDuplicates(Value)

    @property
    def AutoBusList(self) -> str:
        '''
        List of Buses or (File=xxxx) syntax for the AutoAdd solution mode.

        Original COM help: https://opendss.epri.com/AutoBusList.html
        '''
        return self._lib.Settings_Get_AutoBusList()

    @AutoBusList.setter
    def AutoBusList(self, Value: AnyStr):
        self._lib.Settings_Set_AutoBusList(Value)

    @property
    def CircuitModel(self) -> CktModels:
        '''
        Indicate if the circuit model is positive sequence.

        Original COM help: https://opendss.epri.com/CktModel.html
        '''
        return CktModels(self._lib.Settings_Get_CktModel())

    @CircuitModel.setter
    def CircuitModel(self, Value: Union[int, CktModels]):
        self._lib.Settings_Set_CktModel(Value)

    @property
    def ControlTrace(self) -> bool:
        '''
        Denotes whether to trace the control actions to a file.

        Original COM help: https://opendss.epri.com/ControlTrace.html
        '''
        return self._lib.Settings_Get_ControlTrace()

    @ControlTrace.setter
    def ControlTrace(self, Value: bool):
        self._lib.Settings_Set_ControlTrace(Value)

    @property
    def EmergVMaxpu(self) -> float:
        '''
        Per Unit maximum voltage for Emergency conditions.

        Original COM help: https://opendss.epri.com/EmergVmaxpu.html
        '''
        return self._lib.Settings_Get_EmergVmaxpu()

    @EmergVMaxpu.setter
    def EmergVMaxpu(self, Value: float):
        self._lib.Settings_Set_EmergVmaxpu(Value)

    @property
    def EmergVMinpu(self) -> float:
        '''
        Per Unit minimum voltage for Emergency conditions.

        Original COM help: https://opendss.epri.com/EmergVminpu.html
        '''
        return self._lib.Settings_Get_EmergVminpu()

    @EmergVMinpu.setter
    def EmergVMinpu(self, Value: float):
        self._lib.Settings_Set_EmergVminpu(Value)

    @property
    def LossRegisters(self) -> Int32Array:
        '''
        Integer array defining which energy meter registers to use for computing losses

        Original COM help: https://opendss.epri.com/LossRegs.html
        '''
        return self._lib.Settings_Get_LossRegs_GR()

    @LossRegisters.setter
    def LossRegisters(self, Value: Int32Array):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Settings_Set_LossRegs(ValuePtr, ValueCount)

    @property
    def LossWeight(self) -> float:
        '''
        Weighting factor applied to Loss register values.

        Original COM help: https://opendss.epri.com/LossWeight.html
        '''
        return self._lib.Settings_Get_LossWeight()

    @LossWeight.setter
    def LossWeight(self, Value: float):
        self._lib.Settings_Set_LossWeight(Value)

    @property
    def NormalVMaxpu(self) -> float:
        '''
        Per Unit maximum voltage for Normal conditions.

        Original COM help: https://opendss.epri.com/NormVmaxpu.html
        '''
        return self._lib.Settings_Get_NormVmaxpu()

    @NormalVMaxpu.setter
    def NormalVMaxpu(self, Value: float):
        self._lib.Settings_Set_NormVmaxpu(Value)

    @property
    def NormalVMinpu(self) -> float:
        '''
        Per Unit minimum voltage for Normal conditions.

        Original COM help: https://opendss.epri.com/NormVminpu.html
        '''
        return self._lib.Settings_Get_NormVminpu()

    @NormalVMinpu.setter
    def NormalVMinpu(self, Value: float):
        self._lib.Settings_Set_NormVminpu(Value)

    @property
    def PriceCurve(self) -> str:
        '''
        Name of LoadShape object that serves as the source of price signal data for yearly simulations, etc.

        Original COM help: https://opendss.epri.com/PriceCurve.html
        '''
        return self._lib.Settings_Get_PriceCurve()

    @PriceCurve.setter
    def PriceCurve(self, Value: AnyStr):
        self._lib.Settings_Set_PriceCurve(Value)

    @property
    def PriceSignal(self) -> float:
        '''
        Price Signal for the Circuit

        Original COM help: https://opendss.epri.com/PriceSignal.html
        '''
        return self._lib.Settings_Get_PriceSignal()

    @PriceSignal.setter
    def PriceSignal(self, Value: float):
        self._lib.Settings_Set_PriceSignal(Value)

    @property
    def Trapezoidal(self) -> bool:
        '''
        Gets value of trapezoidal integration flag in energy meters. Defaults to `False`.

        Original COM help: https://opendss.epri.com/Trapezoidal.html
        '''
        return self._lib.Settings_Get_Trapezoidal()

    @Trapezoidal.setter
    def Trapezoidal(self, Value: bool):
        self._lib.Settings_Set_Trapezoidal(Value)

    @property
    def UERegisters(self) -> Int32Array:
        '''
        Array of Integers defining energy meter registers to use for computing UE

        Original COM help: https://opendss.epri.com/UEregs.html
        '''
        return self._lib.Settings_Get_UEregs_GR()

    @UERegisters.setter
    def UERegisters(self, Value: Int32Array):
        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)
        self._lib.Settings_Set_UEregs(ValuePtr, ValueCount)

    @property
    def UEWeight(self) -> float:
        '''
        Weighting factor applied to UE register values.

        Original COM help: https://opendss.epri.com/UEweight.html
        '''
        return self._lib.Settings_Get_UEweight()

    @UEWeight.setter
    def UEWeight(self, Value: float):
        self._lib.Settings_Set_UEweight(Value)

    @property
    def VoltageBases(self) -> Float64Array:
        '''
        Array of doubles defining the legal voltage bases in kV L-L

        Original COM help: https://opendss.epri.com/VoltageBases.html
        '''
        return self._lib.Settings_Get_VoltageBases_GR()

    @VoltageBases.setter
    def VoltageBases(self, Value: Float64Array):
        Value, ValuePtr, ValueCount = self._prepare_float64_array(Value)
        self._lib.Settings_Set_VoltageBases(ValuePtr, ValueCount)

    @property
    def ZoneLock(self) -> bool:
        '''
        Locks Zones on energy meters to prevent rebuilding if a circuit change occurs.

        Original COM help: https://opendss.epri.com/ZoneLock.html
        '''
        return self._lib.Settings_Get_ZoneLock()

    @ZoneLock.setter
    def ZoneLock(self, Value: bool):
        self._lib.Settings_Set_ZoneLock(Value)

    @property
    def AllocationFactors(self):
        '''(write-only) Sets all load allocation factors for all loads defined by XFKVA property to this value.'''
        raise AttributeError("This property is write-only!")

    @AllocationFactors.setter
    def AllocationFactors(self, Value: float):
        self._lib.Settings_Set_AllocationFactors(Value)

    @property
    def LoadsTerminalCheck(self) -> bool:
        '''
        Controls whether the terminals are checked when updating the currents in Load component. Defaults to True.
        If the loads are guaranteed to have their terminals closed throughout the simulation, this can be set to False to save some time.
        
        **(API Extension)**
        '''
        return self._lib.Settings_Get_LoadsTerminalCheck()

    @LoadsTerminalCheck.setter
    def LoadsTerminalCheck(self, Value: bool):
        self._lib.Settings_Set_LoadsTerminalCheck(Value)
        
    @property
    def IterateDisabled(self) -> int:
        '''
        Controls whether `First`/`Next` iteration includes or skips disabled circuit elements.
        The default behavior from OpenDSS is to skip those. The user can still activate the element by name or index.
        
        The default value for IterateDisabled is 0, keeping the original behavior.
        Set it to 1 (or `True`) to include disabled elements.
        Other numeric values are reserved for other potential behaviors.
        
        **(API Extension)**
        '''
        return self._lib.Settings_Get_IterateDisabled()

    @IterateDisabled.setter
    def IterateDisabled(self, Value: int):
        self._lib.Settings_Set_IterateDisabled(Value)

    @property
    def AdvancedTypes(self) -> bool:
        '''
        When enabled, there are **two side-effects**:
        
        - **Per DSS Context:** Complex arrays and complex numbers can be returned and consumed by the Python API.
        - **Global effect:** The low-level API provides matrix dimensions when available (`EnableArrayDimensions` is enabled).
        
        As a result, for example, a `YPrim` matrix is returned as a complex matrix instead of a plain array.
        
        When disabled, the legacy plain arrays are used and complex numbers cannot be consumed by the Python API.

        *Defaults to **False** for backwards compatibility.*
        
        **(API Extension)**
        '''
        return self._lib.advanced_types

    @AdvancedTypes.setter
    def AdvancedTypes(self, Value: bool):
        self._lib.advanced_types = bool(Value)
    @property
    def CompatFlags(self) -> int:
        '''
        Controls some compatibility flags introduced to toggle some behavior from the official OpenDSS.

        **THE FLAGS ARE GLOBAL, affecting all DSS engines in the process.**

        These flags may change for each version of DSS C-API, but the same value will not be reused. That is,
        when we remove a compatibility flag, it will have no effect but will also not affect anything else
        besides raising an error if the user tries to toggle a flag that was available in a previous version.

        We expect to keep a very limited number of flags. Since the flags are more transient than the other
        options/flags, it was preferred to add this generic function instead of a separate function per
        flag.

        See the enumeration `DSSCompatFlags` for available flags, including description.

        **(API Extension)**
        '''
        return self._lib.DSS_Get_CompatFlags()

    @CompatFlags.setter
    def CompatFlags(self, Value: int):
        self._lib.DSS_Set_CompatFlags(Value)

    @property
    def AllowForms(self) -> bool:
        '''
        Gets/sets whether text output is allowed (DSS-Extensions) or general forms/windows are shown (official OpenDSS).

        Original COM help: https://opendss.epri.com/AllowForms.html
        '''
        return self._lib.DSS_Get_AllowForms()

    @AllowForms.setter
    def AllowForms(self, value: bool):
        self._lib.DSS_Set_AllowForms(value)

    @property
    def AllowEditor(self) -> bool:
        '''
        Gets/sets whether running the external editor for "Show" is allowed
        
        AllowEditor controls whether the external editor is used in commands like "Show".
        If you set to 0 (false), the editor is not executed. Note that other side effects,
        such as the creation of files, are not affected.

        **(API Extension)**
        '''
        return self._lib.DSS_Get_AllowEditor()

    @AllowEditor.setter
    def AllowEditor(self, value: bool):
        self._lib.DSS_Set_AllowEditor(value)

    @property
    def DataPath(self) -> str:
        '''
        DSS Data File Path.  Default path for reports, etc. from DSS

        Original COM help: https://opendss.epri.com/DataPath.html
        '''
        return self._lib.DSS_Get_DataPath()

    @DataPath.setter
    def DataPath(self, Value: AnyStr):
        self._lib.DSS_Set_DataPath(Value)

    @property
    def DefaultEditor(self) -> str:
        '''
        Returns the path name for the default text editor.

        Original COM help: https://opendss.epri.com/DefaultEditor.html
        '''
        return self._lib.DSS_Get_DefaultEditor()


    def SetPropertyNameStyle(self, value: DSSPropertyNameStyle):
        '''
        Switch the property names according to the target style.

        Use this method for compatibility with code that doesn't consider that
        OpenDSS is case insensitive. Check the enumeration for more:
        [DSSPropertyNameStyle](#dss_python_backend.enums.DSSPropertyNameStyle)

        **(API Extension)**
        '''
        self._lib.Settings_SetPropertyNameStyle(value)

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
        return self._lib.DSS_Get_AllowChangeDir()

    @AllowChangeDir.setter
    def AllowChangeDir(self, Value: bool):
        self._lib.DSS_Set_AllowChangeDir(Value)

    @property
    def AllowDOScmd(self) -> bool:
        '''
        If enabled, the `DOScmd` command is allowed. Otherwise, an error is reported if the user tries to use it.

        Defaults to False/0 (disabled state). Users should consider DOScmd deprecated on DSS-Extensions.

        This can also be set through the environment variable DSS_CAPI_ALLOW_DOSCMD. Setting it to 1 enables
        the command.

        **(API Extension)**
        '''
        return self._lib.DSS_Get_AllowDOScmd()

    @AllowDOScmd.setter
    def AllowDOScmd(self, Value: bool):
        self._lib.DSS_Set_AllowDOScmd(Value)

    @property
    def COMErrorResults(self) -> bool:
        '''
        If enabled, in case of errors or empty arrays, the API returns arrays with values compatible with the 
        official OpenDSS COM interface. 

        For example, consider the function `Loads_Get_ZIPV`. If there is no active circuit or active load element:

        - In the disabled state (COMErrorResults=False), the function will return "[]", an array with 0 elements.
        - In the enabled state (COMErrorResults=True), the function will return "[0.0]" instead. This should
        be compatible with the return value of the official COM interface.

        Defaults to False/0 (disabled state), starting DSS-Python v0.16.

        This can also be set through the environment variable `DSS_CAPI_COM_DEFAULTS`. Setting it to 0 disables
        the legacy/COM behavior. The value can be toggled through the API at any time.

        **(API Extension)**
        '''
        return self._lib.DSS_Get_COMErrorResults()

    @COMErrorResults.setter
    def COMErrorResults(self, Value: bool):
        self._lib.DSS_Set_COMErrorResults(Value)

    @property
    def SkipFileRegExp(self) -> str:
        '''
        Regular expression pattern to skip files.

        If a file name as provided in the input for the `Redirect` and `Compile` commands
        matches the regular expression pattern, it is skipped (the file is not read nor
        commands contained in the file are executed).

        Set to an empty string to reset/disable the filter.

        Case-insensitive.
        See https://regex.sorokin.engineer/en/latest/regular_expressions.html for information on 
        the expression syntax and options.

        Even if the `clear` command is included in `Settings.SkipCommands`, the `DSS.ClearAll()` method can 
        still be called. It resets both skip settings, `SkipCommands` and `SkipFileRegExp`.

        **(API Extension)**
        '''
        return self._lib.Settings_Get_SkipFileRegExp()

    @SkipFileRegExp.setter
    def SkipFileRegExp(self, Value: Union[AnyStr, None]):
        self._lib.Settings_Set_SkipFileRegExp(Value or '')
    
    @property
    def SkipCommands(self) -> List[str]:
        '''
        List of commands to skip

        List of strings representing the command names to skip when processing DSS text commands or files.

        If the `clear` command is included in `Settings.SkipCommands`, the `DSS.ClearAll()` method can 
        still be called and it will reset both skip settings, `SkipCommands` and `SkipFileRegExp`.

        **(API Extension)**
        '''
        
        return [
            self._lib.DSS_Executive_Get_Command(i)
            for i in self._lib.Settings_Get_SkipCommands_GR()
        ]

    @SkipCommands.setter
    def SkipCommands(self, Value: List[str]):
        if len(Value) != 0 and isinstance(Value[0], str):
            # map command names to integer codes
            Value = [self._command_dict[cmd_name] for cmd_name in Value]

        Value, ValuePtr, ValueCount = self._prepare_int32_array(Value)

        self._lib.Settings_Set_SkipCommands(ValuePtr, ValueCount)


    def map_to_iterators(self):
        '''
        Returns a Python context manager that temporary disables mapping new DSS objects
        to permanent Python objects; instead, use AltDSS object iterators where required. 

        Use this to remove the extra Python overhead if you do not plan to interact 
        with every single object in Python. The objects can always be accessed later
        through the implicit collections (e.g. `altdss.Load` for load objects).

        Alternatively, prefer the batch API to create objects in bulk, when possible.
        Batches do not instantiate individual Python objects for each DSS object when 
        they are created.

        For advanced users.

        **(API Extension)**
        '''
        return MapToIterators(self)

