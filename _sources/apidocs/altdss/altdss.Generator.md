# {py:mod}`altdss.Generator`

```{py:module} altdss.Generator
```

```{autodoc2-docstring} altdss.Generator
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Generator <altdss.Generator.Generator>`
  - ```{autodoc2-docstring} altdss.Generator.Generator
    :summary:
    ```
* - {py:obj}`GeneratorBatch <altdss.Generator.GeneratorBatch>`
  - ```{autodoc2-docstring} altdss.Generator.GeneratorBatch
    :summary:
    ```
* - {py:obj}`GeneratorBatchProperties <altdss.Generator.GeneratorBatchProperties>`
  - ```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties
    :summary:
    ```
* - {py:obj}`GeneratorProperties <altdss.Generator.GeneratorProperties>`
  - ```{autodoc2-docstring} altdss.Generator.GeneratorProperties
    :summary:
    ```
* - {py:obj}`IGenerator <altdss.Generator.IGenerator>`
  - ```{autodoc2-docstring} altdss.Generator.IGenerator
    :summary:
    ```
````

### API

`````{py:class} Generator(api_util, ptr)
:canonical: altdss.Generator.Generator

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`, {py:obj}`altdss.PCElement.ElementHasRegistersMixin`

```{autodoc2-docstring} altdss.Generator.Generator
```

````{py:attribute} Balanced
:canonical: altdss.Generator.Generator.Balanced
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Generator.Generator.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Generator.Generator.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.Generator.Generator.Class
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Class
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Generator.Generator.Close

```{autodoc2-docstring} altdss.Generator.Generator.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Generator.Generator.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Generator.Generator.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Generator.Generator.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Generator.Generator.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Generator.Generator.Conn
:type: altdss.enums.Connection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Generator.Generator.Conn_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Generator.Generator.Currents

```{autodoc2-docstring} altdss.Generator.Generator.Currents
```

````

````{py:attribute} D
:canonical: altdss.Generator.Generator.D
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.D
```

````

````{py:attribute} Daily
:canonical: altdss.Generator.Generator.Daily
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Generator.Generator.Daily_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Generator.Generator.DebugTrace
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.DebugTrace
```

````

````{py:attribute} DispMode
:canonical: altdss.Generator.Generator.DispMode
:type: altdss.enums.GeneratorDispatchMode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.DispMode
```

````

````{py:attribute} DispMode_str
:canonical: altdss.Generator.Generator.DispMode_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.DispMode_str
```

````

````{py:attribute} DispValue
:canonical: altdss.Generator.Generator.DispValue
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.DispValue
```

````

````{py:attribute} DisplayName
:canonical: altdss.Generator.Generator.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.DisplayName
```

````

````{py:attribute} Duty
:canonical: altdss.Generator.Generator.Duty
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.Generator.Generator.DutyStart
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.DutyStart
```

````

````{py:attribute} Duty_str
:canonical: altdss.Generator.Generator.Duty_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Duty_str
```

````

````{py:attribute} DynOut
:canonical: altdss.Generator.Generator.DynOut
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Generator.Generator.DynamicEq
:type: altdss.DynamicExp.DynamicExp
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.DynamicEq
```

````

````{py:attribute} DynamicEq_str
:canonical: altdss.Generator.Generator.DynamicEq_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.DynamicEq_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Generator.Generator.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.Generator.Generator.EnergyMeter

```{autodoc2-docstring} altdss.Generator.Generator.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Generator.Generator.EnergyMeterName

```{autodoc2-docstring} altdss.Generator.Generator.EnergyMeterName
```

````

````{py:attribute} ForceOn
:canonical: altdss.Generator.Generator.ForceOn
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.ForceOn
```

````

````{py:attribute} FuelkWh
:canonical: altdss.Generator.Generator.FuelkWh
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.FuelkWh
```

````

````{py:method} FullName() -> str
:canonical: altdss.Generator.Generator.FullName

```{autodoc2-docstring} altdss.Generator.Generator.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Generator.Generator.GUID

```{autodoc2-docstring} altdss.Generator.Generator.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.Generator.Generator.GetVariableValue

```{autodoc2-docstring} altdss.Generator.Generator.GetVariableValue
```

````

````{py:attribute} H
:canonical: altdss.Generator.Generator.H
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.H
```

````

````{py:method} Handle() -> int
:canonical: altdss.Generator.Generator.Handle

```{autodoc2-docstring} altdss.Generator.Generator.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Generator.Generator.HasOCPDevice

```{autodoc2-docstring} altdss.Generator.Generator.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Generator.Generator.HasSwitchControl

```{autodoc2-docstring} altdss.Generator.Generator.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Generator.Generator.HasVoltControl

```{autodoc2-docstring} altdss.Generator.Generator.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Generator.Generator.IsIsolated

```{autodoc2-docstring} altdss.Generator.Generator.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Generator.Generator.IsOpen

```{autodoc2-docstring} altdss.Generator.Generator.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Generator.Generator.Like

```{autodoc2-docstring} altdss.Generator.Generator.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Generator.Generator.Losses

```{autodoc2-docstring} altdss.Generator.Generator.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Generator.Generator.MaxCurrent

```{autodoc2-docstring} altdss.Generator.Generator.MaxCurrent
```

````

````{py:attribute} Maxkvar
:canonical: altdss.Generator.Generator.Maxkvar
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Maxkvar
```

````

````{py:attribute} Minkvar
:canonical: altdss.Generator.Generator.Minkvar
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Minkvar
```

````

````{py:attribute} Model
:canonical: altdss.Generator.Generator.Model
:type: altdss.enums.GeneratorModel
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Model
```

````

````{py:property} Name
:canonical: altdss.Generator.Generator.Name
:type: str

```{autodoc2-docstring} altdss.Generator.Generator.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Generator.Generator.NodeOrder

```{autodoc2-docstring} altdss.Generator.Generator.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Generator.Generator.NodeRef

```{autodoc2-docstring} altdss.Generator.Generator.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Generator.Generator.NumConductors

```{autodoc2-docstring} altdss.Generator.Generator.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Generator.Generator.NumControllers

```{autodoc2-docstring} altdss.Generator.Generator.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Generator.Generator.NumPhases

```{autodoc2-docstring} altdss.Generator.Generator.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Generator.Generator.NumTerminals

```{autodoc2-docstring} altdss.Generator.Generator.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Generator.Generator.OCPDevice

```{autodoc2-docstring} altdss.Generator.Generator.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Generator.Generator.OCPDeviceIndex

```{autodoc2-docstring} altdss.Generator.Generator.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Generator.Generator.OCPDeviceType

```{autodoc2-docstring} altdss.Generator.Generator.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Generator.Generator.Open

```{autodoc2-docstring} altdss.Generator.Generator.Open
```

````

````{py:attribute} PF
:canonical: altdss.Generator.Generator.PF
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.PF
```

````

````{py:attribute} PVFactor
:canonical: altdss.Generator.Generator.PVFactor
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.PVFactor
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Generator.Generator.PhaseLosses

```{autodoc2-docstring} altdss.Generator.Generator.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Generator.Generator.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Generator.Generator.Powers

```{autodoc2-docstring} altdss.Generator.Generator.Powers
```

````

````{py:method} Refuel(value: bool = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Generator.Generator.Refuel

```{autodoc2-docstring} altdss.Generator.Generator.Refuel
```

````

````{py:method} RegisterNames() -> typing.List[str]
:canonical: altdss.Generator.Generator.RegisterNames

```{autodoc2-docstring} altdss.Generator.Generator.RegisterNames
```

````

````{py:method} RegisterValues() -> altdss.types.Float64Array
:canonical: altdss.Generator.Generator.RegisterValues

```{autodoc2-docstring} altdss.Generator.Generator.RegisterValues
```

````

````{py:method} RegistersDict() -> typing.Dict[str, float]
:canonical: altdss.Generator.Generator.RegistersDict

```{autodoc2-docstring} altdss.Generator.Generator.RegistersDict
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Generator.Generator.Residuals

```{autodoc2-docstring} altdss.Generator.Generator.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Generator.Generator.SeqCurrents

```{autodoc2-docstring} altdss.Generator.Generator.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Generator.Generator.SeqPowers

```{autodoc2-docstring} altdss.Generator.Generator.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Generator.Generator.SeqVoltages

```{autodoc2-docstring} altdss.Generator.Generator.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.Generator.Generator.SetVariableValue

```{autodoc2-docstring} altdss.Generator.Generator.SetVariableValue
```

````

````{py:attribute} ShaftData
:canonical: altdss.Generator.Generator.ShaftData
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.ShaftData
```

````

````{py:attribute} ShaftModel
:canonical: altdss.Generator.Generator.ShaftModel
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.ShaftModel
```

````

````{py:attribute} Spectrum
:canonical: altdss.Generator.Generator.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Generator.Generator.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Spectrum_str
```

````

````{py:attribute} Status
:canonical: altdss.Generator.Generator.Status
:type: altdss.enums.GeneratorStatus
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Status
```

````

````{py:attribute} Status_str
:canonical: altdss.Generator.Generator.Status_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Status_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Generator.Generator.TotalPowers

```{autodoc2-docstring} altdss.Generator.Generator.TotalPowers
```

````

````{py:attribute} UseFuel
:canonical: altdss.Generator.Generator.UseFuel
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.UseFuel
```

````

````{py:attribute} UserData
:canonical: altdss.Generator.Generator.UserData
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Generator.Generator.UserModel
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Generator.Generator.VMaxpu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Generator.Generator.VMinpu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.VMinpu
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.Generator.Generator.VariableNames

```{autodoc2-docstring} altdss.Generator.Generator.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.Generator.Generator.VariableValues

```{autodoc2-docstring} altdss.Generator.Generator.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.Generator.Generator.VariablesDict

```{autodoc2-docstring} altdss.Generator.Generator.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Generator.Generator.Voltages

```{autodoc2-docstring} altdss.Generator.Generator.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Generator.Generator.VoltagesMagAng

```{autodoc2-docstring} altdss.Generator.Generator.VoltagesMagAng
```

````

````{py:attribute} Vpu
:canonical: altdss.Generator.Generator.Vpu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Vpu
```

````

````{py:attribute} XRdp
:canonical: altdss.Generator.Generator.XRdp
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.XRdp
```

````

````{py:attribute} Xd
:canonical: altdss.Generator.Generator.Xd
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Xd
```

````

````{py:attribute} Xdp
:canonical: altdss.Generator.Generator.Xdp
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Xdp
```

````

````{py:attribute} Xdpp
:canonical: altdss.Generator.Generator.Xdpp
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Xdpp
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Generator.Generator.YPrim

```{autodoc2-docstring} altdss.Generator.Generator.YPrim
```

````

````{py:attribute} Yearly
:canonical: altdss.Generator.Generator.Yearly
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Generator.Generator.Yearly_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.Yearly_str
```

````

````{py:method} __hash__()
:canonical: altdss.Generator.Generator.__hash__

```{autodoc2-docstring} altdss.Generator.Generator.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Generator.Generator.__init__

```{autodoc2-docstring} altdss.Generator.Generator.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Generator.Generator.__ne__

```{autodoc2-docstring} altdss.Generator.Generator.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Generator.Generator.__repr__

```{autodoc2-docstring} altdss.Generator.Generator.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Generator.Generator.begin_edit

```{autodoc2-docstring} altdss.Generator.Generator.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Generator.Generator.end_edit

```{autodoc2-docstring} altdss.Generator.Generator.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Generator.Generator.kV
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Generator.Generator.kVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Generator.Generator.kW
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.kW
```

````

````{py:attribute} kvar
:canonical: altdss.Generator.Generator.kvar
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.kvar
```

````

````{py:attribute} pctFuel
:canonical: altdss.Generator.Generator.pctFuel
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.pctFuel
```

````

````{py:attribute} pctReserve
:canonical: altdss.Generator.Generator.pctReserve
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.Generator.pctReserve
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Generator.Generator.to_json

```{autodoc2-docstring} altdss.Generator.Generator.to_json
```

````

`````

`````{py:class} GeneratorBatch(api_util, **kwargs)
:canonical: altdss.Generator.GeneratorBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.Generator.GeneratorBatch
```

````{py:attribute} Balanced
:canonical: altdss.Generator.GeneratorBatch.Balanced
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Generator.GeneratorBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Generator.GeneratorBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.Generator.GeneratorBatch.Class
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Class
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Generator.GeneratorBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Generator.GeneratorBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Generator.GeneratorBatch.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Generator.GeneratorBatch.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Generator.GeneratorBatch.Currents

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Generator.GeneratorBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.CurrentsMagAng
```

````

````{py:attribute} D
:canonical: altdss.Generator.GeneratorBatch.D
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.D
```

````

````{py:attribute} Daily
:canonical: altdss.Generator.GeneratorBatch.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Generator.GeneratorBatch.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Generator.GeneratorBatch.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.DebugTrace
```

````

````{py:attribute} DispMode
:canonical: altdss.Generator.GeneratorBatch.DispMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.DispMode
```

````

````{py:attribute} DispMode_str
:canonical: altdss.Generator.GeneratorBatch.DispMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.DispMode_str
```

````

````{py:attribute} DispValue
:canonical: altdss.Generator.GeneratorBatch.DispValue
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.DispValue
```

````

````{py:attribute} Duty
:canonical: altdss.Generator.GeneratorBatch.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.Generator.GeneratorBatch.DutyStart
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.DutyStart
```

````

````{py:attribute} Duty_str
:canonical: altdss.Generator.GeneratorBatch.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Duty_str
```

````

````{py:attribute} DynOut
:canonical: altdss.Generator.GeneratorBatch.DynOut
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Generator.GeneratorBatch.DynamicEq
:type: typing.List[altdss.DynamicExp.DynamicExp]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.DynamicEq
```

````

````{py:attribute} DynamicEq_str
:canonical: altdss.Generator.GeneratorBatch.DynamicEq_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.DynamicEq_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Generator.GeneratorBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Generator.GeneratorBatch.EnergyMeter

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Generator.GeneratorBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.EnergyMeterName
```

````

````{py:attribute} ForceOn
:canonical: altdss.Generator.GeneratorBatch.ForceOn
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.ForceOn
```

````

````{py:attribute} FuelkWh
:canonical: altdss.Generator.GeneratorBatch.FuelkWh
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.FuelkWh
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Generator.GeneratorBatch.FullName

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Generator.GeneratorBatch.GUID

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.GUID
```

````

````{py:attribute} H
:canonical: altdss.Generator.GeneratorBatch.H
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.H
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Generator.GeneratorBatch.Handle

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Generator.GeneratorBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Generator.GeneratorBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Generator.GeneratorBatch.HasVoltControl

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Generator.GeneratorBatch.IsIsolated

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Generator.GeneratorBatch.Like

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Generator.GeneratorBatch.Losses

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Generator.GeneratorBatch.MaxCurrent

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.MaxCurrent
```

````

````{py:attribute} Maxkvar
:canonical: altdss.Generator.GeneratorBatch.Maxkvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Maxkvar
```

````

````{py:attribute} Minkvar
:canonical: altdss.Generator.GeneratorBatch.Minkvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Minkvar
```

````

````{py:attribute} Model
:canonical: altdss.Generator.GeneratorBatch.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Model
```

````

````{py:property} Name
:canonical: altdss.Generator.GeneratorBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Generator.GeneratorBatch.NumConductors

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Generator.GeneratorBatch.NumControllers

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Generator.GeneratorBatch.NumPhases

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Generator.GeneratorBatch.NumTerminals

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Generator.GeneratorBatch.OCPDevice

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Generator.GeneratorBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Generator.GeneratorBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.Generator.GeneratorBatch.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.PF
```

````

````{py:attribute} PVFactor
:canonical: altdss.Generator.GeneratorBatch.PVFactor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.PVFactor
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Generator.GeneratorBatch.PhaseLosses

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Generator.GeneratorBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Generator.GeneratorBatch.Powers

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Powers
```

````

````{py:method} Refuel(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Generator.GeneratorBatch.Refuel

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Refuel
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Generator.GeneratorBatch.SeqCurrents

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Generator.GeneratorBatch.SeqPowers

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Generator.GeneratorBatch.SeqVoltages

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.SeqVoltages
```

````

````{py:attribute} ShaftData
:canonical: altdss.Generator.GeneratorBatch.ShaftData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.ShaftData
```

````

````{py:attribute} ShaftModel
:canonical: altdss.Generator.GeneratorBatch.ShaftModel
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.ShaftModel
```

````

````{py:attribute} Spectrum
:canonical: altdss.Generator.GeneratorBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Generator.GeneratorBatch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Spectrum_str
```

````

````{py:attribute} Status
:canonical: altdss.Generator.GeneratorBatch.Status
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Status
```

````

````{py:attribute} Status_str
:canonical: altdss.Generator.GeneratorBatch.Status_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Status_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Generator.GeneratorBatch.TotalPowers

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.TotalPowers
```

````

````{py:attribute} UseFuel
:canonical: altdss.Generator.GeneratorBatch.UseFuel
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.UseFuel
```

````

````{py:attribute} UserData
:canonical: altdss.Generator.GeneratorBatch.UserData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Generator.GeneratorBatch.UserModel
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Generator.GeneratorBatch.VMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Generator.GeneratorBatch.VMinpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.VMinpu
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Generator.GeneratorBatch.Voltages

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Generator.GeneratorBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.VoltagesMagAng
```

````

````{py:attribute} Vpu
:canonical: altdss.Generator.GeneratorBatch.Vpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Vpu
```

````

````{py:attribute} XRdp
:canonical: altdss.Generator.GeneratorBatch.XRdp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.XRdp
```

````

````{py:attribute} Xd
:canonical: altdss.Generator.GeneratorBatch.Xd
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Xd
```

````

````{py:attribute} Xdp
:canonical: altdss.Generator.GeneratorBatch.Xdp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Xdp
```

````

````{py:attribute} Xdpp
:canonical: altdss.Generator.GeneratorBatch.Xdpp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Xdpp
```

````

````{py:attribute} Yearly
:canonical: altdss.Generator.GeneratorBatch.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Generator.GeneratorBatch.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.Generator.GeneratorBatch.__call__

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Generator.GeneratorBatch.__getitem__

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Generator.GeneratorBatch.__init__

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Generator.GeneratorBatch.__iter__

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Generator.GeneratorBatch.__len__

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Generator.GeneratorBatch.batch

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Generator.GeneratorBatch.begin_edit

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Generator.GeneratorBatch.end_edit

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Generator.GeneratorBatch.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Generator.GeneratorBatch.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Generator.GeneratorBatch.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.kW
```

````

````{py:attribute} kvar
:canonical: altdss.Generator.GeneratorBatch.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.kvar
```

````

````{py:attribute} pctFuel
:canonical: altdss.Generator.GeneratorBatch.pctFuel
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.pctFuel
```

````

````{py:attribute} pctReserve
:canonical: altdss.Generator.GeneratorBatch.pctReserve
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.pctReserve
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Generator.GeneratorBatch.to_json

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Generator.GeneratorBatch.to_list

```{autodoc2-docstring} altdss.Generator.GeneratorBatch.to_list
```

````

`````

`````{py:class} GeneratorBatchProperties()
:canonical: altdss.Generator.GeneratorBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties
```

````{py:attribute} Balanced
:canonical: altdss.Generator.GeneratorBatchProperties.Balanced
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Generator.GeneratorBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Generator.GeneratorBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.Generator.GeneratorBatchProperties.Class
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Class
```

````

````{py:attribute} Conn
:canonical: altdss.Generator.GeneratorBatchProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.Connection], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Conn
```

````

````{py:attribute} D
:canonical: altdss.Generator.GeneratorBatchProperties.D
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.D
```

````

````{py:attribute} Daily
:canonical: altdss.Generator.GeneratorBatchProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Daily
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Generator.GeneratorBatchProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.DebugTrace
```

````

````{py:attribute} DispMode
:canonical: altdss.Generator.GeneratorBatchProperties.DispMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.GeneratorDispatchMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.GeneratorDispatchMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.DispMode
```

````

````{py:attribute} DispValue
:canonical: altdss.Generator.GeneratorBatchProperties.DispValue
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.DispValue
```

````

````{py:attribute} Duty
:canonical: altdss.Generator.GeneratorBatchProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.Generator.GeneratorBatchProperties.DutyStart
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.DutyStart
```

````

````{py:attribute} DynOut
:canonical: altdss.Generator.GeneratorBatchProperties.DynOut
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Generator.GeneratorBatchProperties.DynamicEq
:type: typing.Union[typing.AnyStr, altdss.DynamicExp.DynamicExp, typing.List[typing.AnyStr], typing.List[altdss.DynamicExp.DynamicExp]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.DynamicEq
```

````

````{py:attribute} Enabled
:canonical: altdss.Generator.GeneratorBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Enabled
```

````

````{py:attribute} ForceOn
:canonical: altdss.Generator.GeneratorBatchProperties.ForceOn
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.ForceOn
```

````

````{py:attribute} FuelkWh
:canonical: altdss.Generator.GeneratorBatchProperties.FuelkWh
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.FuelkWh
```

````

````{py:attribute} H
:canonical: altdss.Generator.GeneratorBatchProperties.H
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.H
```

````

````{py:attribute} Like
:canonical: altdss.Generator.GeneratorBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Like
```

````

````{py:attribute} Maxkvar
:canonical: altdss.Generator.GeneratorBatchProperties.Maxkvar
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Maxkvar
```

````

````{py:attribute} Minkvar
:canonical: altdss.Generator.GeneratorBatchProperties.Minkvar
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Minkvar
```

````

````{py:attribute} Model
:canonical: altdss.Generator.GeneratorBatchProperties.Model
:type: typing.Union[int, altdss.enums.GeneratorModel, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Model
```

````

````{py:attribute} PF
:canonical: altdss.Generator.GeneratorBatchProperties.PF
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.PF
```

````

````{py:attribute} PVFactor
:canonical: altdss.Generator.GeneratorBatchProperties.PVFactor
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.PVFactor
```

````

````{py:attribute} Phases
:canonical: altdss.Generator.GeneratorBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Phases
```

````

````{py:attribute} Refuel
:canonical: altdss.Generator.GeneratorBatchProperties.Refuel
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Refuel
```

````

````{py:attribute} ShaftData
:canonical: altdss.Generator.GeneratorBatchProperties.ShaftData
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.ShaftData
```

````

````{py:attribute} ShaftModel
:canonical: altdss.Generator.GeneratorBatchProperties.ShaftModel
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.ShaftModel
```

````

````{py:attribute} Spectrum
:canonical: altdss.Generator.GeneratorBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Spectrum
```

````

````{py:attribute} Status
:canonical: altdss.Generator.GeneratorBatchProperties.Status
:type: typing.Union[typing.AnyStr, int, altdss.enums.GeneratorStatus, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.GeneratorStatus], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Status
```

````

````{py:attribute} UseFuel
:canonical: altdss.Generator.GeneratorBatchProperties.UseFuel
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.UseFuel
```

````

````{py:attribute} UserData
:canonical: altdss.Generator.GeneratorBatchProperties.UserData
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Generator.GeneratorBatchProperties.UserModel
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Generator.GeneratorBatchProperties.VMaxpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Generator.GeneratorBatchProperties.VMinpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.VMinpu
```

````

````{py:attribute} Vpu
:canonical: altdss.Generator.GeneratorBatchProperties.Vpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Vpu
```

````

````{py:attribute} XRdp
:canonical: altdss.Generator.GeneratorBatchProperties.XRdp
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.XRdp
```

````

````{py:attribute} Xd
:canonical: altdss.Generator.GeneratorBatchProperties.Xd
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Xd
```

````

````{py:attribute} Xdp
:canonical: altdss.Generator.GeneratorBatchProperties.Xdp
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Xdp
```

````

````{py:attribute} Xdpp
:canonical: altdss.Generator.GeneratorBatchProperties.Xdpp
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Xdpp
```

````

````{py:attribute} Yearly
:canonical: altdss.Generator.GeneratorBatchProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.Generator.GeneratorBatchProperties.__contains__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Generator.GeneratorBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Generator.GeneratorBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Generator.GeneratorBatchProperties.__dir__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Generator.GeneratorBatchProperties.__format__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Generator.GeneratorBatchProperties.__ge__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Generator.GeneratorBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Generator.GeneratorBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Generator.GeneratorBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Generator.GeneratorBatchProperties.__gt__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Generator.GeneratorBatchProperties.__init__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Generator.GeneratorBatchProperties.__ior__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Generator.GeneratorBatchProperties.__iter__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Generator.GeneratorBatchProperties.__le__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Generator.GeneratorBatchProperties.__len__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Generator.GeneratorBatchProperties.__lt__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Generator.GeneratorBatchProperties.__ne__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Generator.GeneratorBatchProperties.__new__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Generator.GeneratorBatchProperties.__or__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Generator.GeneratorBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Generator.GeneratorBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Generator.GeneratorBatchProperties.__repr__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Generator.GeneratorBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Generator.GeneratorBatchProperties.__ror__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Generator.GeneratorBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Generator.GeneratorBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Generator.GeneratorBatchProperties.__str__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Generator.GeneratorBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Generator.GeneratorBatchProperties.clear

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Generator.GeneratorBatchProperties.copy

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Generator.GeneratorBatchProperties.get

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Generator.GeneratorBatchProperties.items

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Generator.GeneratorBatchProperties.kV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Generator.GeneratorBatchProperties.kVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Generator.GeneratorBatchProperties.kW
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.kW
```

````

````{py:method} keys()
:canonical: altdss.Generator.GeneratorBatchProperties.keys

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Generator.GeneratorBatchProperties.kvar
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.kvar
```

````

````{py:attribute} pctFuel
:canonical: altdss.Generator.GeneratorBatchProperties.pctFuel
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.pctFuel
```

````

````{py:attribute} pctReserve
:canonical: altdss.Generator.GeneratorBatchProperties.pctReserve
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.pctReserve
```

````

````{py:method} pop()
:canonical: altdss.Generator.GeneratorBatchProperties.pop

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Generator.GeneratorBatchProperties.popitem

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Generator.GeneratorBatchProperties.setdefault

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Generator.GeneratorBatchProperties.update

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Generator.GeneratorBatchProperties.values

```{autodoc2-docstring} altdss.Generator.GeneratorBatchProperties.values
```

````

`````

`````{py:class} GeneratorProperties()
:canonical: altdss.Generator.GeneratorProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Generator.GeneratorProperties
```

````{py:attribute} Balanced
:canonical: altdss.Generator.GeneratorProperties.Balanced
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Generator.GeneratorProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Generator.GeneratorProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.Generator.GeneratorProperties.Class
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Class
```

````

````{py:attribute} Conn
:canonical: altdss.Generator.GeneratorProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Conn
```

````

````{py:attribute} D
:canonical: altdss.Generator.GeneratorProperties.D
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.D
```

````

````{py:attribute} Daily
:canonical: altdss.Generator.GeneratorProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Daily
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Generator.GeneratorProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.DebugTrace
```

````

````{py:attribute} DispMode
:canonical: altdss.Generator.GeneratorProperties.DispMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.GeneratorDispatchMode]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.DispMode
```

````

````{py:attribute} DispValue
:canonical: altdss.Generator.GeneratorProperties.DispValue
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.DispValue
```

````

````{py:attribute} Duty
:canonical: altdss.Generator.GeneratorProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.Generator.GeneratorProperties.DutyStart
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.DutyStart
```

````

````{py:attribute} DynOut
:canonical: altdss.Generator.GeneratorProperties.DynOut
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Generator.GeneratorProperties.DynamicEq
:type: typing.Union[typing.AnyStr, altdss.DynamicExp.DynamicExp]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.DynamicEq
```

````

````{py:attribute} Enabled
:canonical: altdss.Generator.GeneratorProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Enabled
```

````

````{py:attribute} ForceOn
:canonical: altdss.Generator.GeneratorProperties.ForceOn
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.ForceOn
```

````

````{py:attribute} FuelkWh
:canonical: altdss.Generator.GeneratorProperties.FuelkWh
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.FuelkWh
```

````

````{py:attribute} H
:canonical: altdss.Generator.GeneratorProperties.H
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.H
```

````

````{py:attribute} Like
:canonical: altdss.Generator.GeneratorProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Like
```

````

````{py:attribute} Maxkvar
:canonical: altdss.Generator.GeneratorProperties.Maxkvar
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Maxkvar
```

````

````{py:attribute} Minkvar
:canonical: altdss.Generator.GeneratorProperties.Minkvar
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Minkvar
```

````

````{py:attribute} Model
:canonical: altdss.Generator.GeneratorProperties.Model
:type: typing.Union[int, altdss.enums.GeneratorModel]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Model
```

````

````{py:attribute} PF
:canonical: altdss.Generator.GeneratorProperties.PF
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.PF
```

````

````{py:attribute} PVFactor
:canonical: altdss.Generator.GeneratorProperties.PVFactor
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.PVFactor
```

````

````{py:attribute} Phases
:canonical: altdss.Generator.GeneratorProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Phases
```

````

````{py:attribute} Refuel
:canonical: altdss.Generator.GeneratorProperties.Refuel
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Refuel
```

````

````{py:attribute} ShaftData
:canonical: altdss.Generator.GeneratorProperties.ShaftData
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.ShaftData
```

````

````{py:attribute} ShaftModel
:canonical: altdss.Generator.GeneratorProperties.ShaftModel
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.ShaftModel
```

````

````{py:attribute} Spectrum
:canonical: altdss.Generator.GeneratorProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Spectrum
```

````

````{py:attribute} Status
:canonical: altdss.Generator.GeneratorProperties.Status
:type: typing.Union[typing.AnyStr, int, altdss.enums.GeneratorStatus]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Status
```

````

````{py:attribute} UseFuel
:canonical: altdss.Generator.GeneratorProperties.UseFuel
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.UseFuel
```

````

````{py:attribute} UserData
:canonical: altdss.Generator.GeneratorProperties.UserData
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Generator.GeneratorProperties.UserModel
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Generator.GeneratorProperties.VMaxpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Generator.GeneratorProperties.VMinpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.VMinpu
```

````

````{py:attribute} Vpu
:canonical: altdss.Generator.GeneratorProperties.Vpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Vpu
```

````

````{py:attribute} XRdp
:canonical: altdss.Generator.GeneratorProperties.XRdp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.XRdp
```

````

````{py:attribute} Xd
:canonical: altdss.Generator.GeneratorProperties.Xd
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Xd
```

````

````{py:attribute} Xdp
:canonical: altdss.Generator.GeneratorProperties.Xdp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Xdp
```

````

````{py:attribute} Xdpp
:canonical: altdss.Generator.GeneratorProperties.Xdpp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Xdpp
```

````

````{py:attribute} Yearly
:canonical: altdss.Generator.GeneratorProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.Generator.GeneratorProperties.__contains__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Generator.GeneratorProperties.__delattr__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Generator.GeneratorProperties.__delitem__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Generator.GeneratorProperties.__dir__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Generator.GeneratorProperties.__format__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Generator.GeneratorProperties.__ge__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Generator.GeneratorProperties.__getattribute__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Generator.GeneratorProperties.__getitem__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Generator.GeneratorProperties.__getstate__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Generator.GeneratorProperties.__gt__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Generator.GeneratorProperties.__init__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Generator.GeneratorProperties.__ior__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Generator.GeneratorProperties.__iter__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Generator.GeneratorProperties.__le__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Generator.GeneratorProperties.__len__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Generator.GeneratorProperties.__lt__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Generator.GeneratorProperties.__ne__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Generator.GeneratorProperties.__new__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Generator.GeneratorProperties.__or__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Generator.GeneratorProperties.__reduce__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Generator.GeneratorProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Generator.GeneratorProperties.__repr__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Generator.GeneratorProperties.__reversed__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Generator.GeneratorProperties.__ror__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Generator.GeneratorProperties.__setitem__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Generator.GeneratorProperties.__sizeof__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Generator.GeneratorProperties.__str__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Generator.GeneratorProperties.__subclasshook__

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Generator.GeneratorProperties.clear

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Generator.GeneratorProperties.copy

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Generator.GeneratorProperties.get

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.get
```

````

````{py:method} items()
:canonical: altdss.Generator.GeneratorProperties.items

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Generator.GeneratorProperties.kV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Generator.GeneratorProperties.kVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Generator.GeneratorProperties.kW
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.kW
```

````

````{py:method} keys()
:canonical: altdss.Generator.GeneratorProperties.keys

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Generator.GeneratorProperties.kvar
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.kvar
```

````

````{py:attribute} pctFuel
:canonical: altdss.Generator.GeneratorProperties.pctFuel
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.pctFuel
```

````

````{py:attribute} pctReserve
:canonical: altdss.Generator.GeneratorProperties.pctReserve
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.pctReserve
```

````

````{py:method} pop()
:canonical: altdss.Generator.GeneratorProperties.pop

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Generator.GeneratorProperties.popitem

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Generator.GeneratorProperties.setdefault

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Generator.GeneratorProperties.update

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.update
```

````

````{py:method} values()
:canonical: altdss.Generator.GeneratorProperties.values

```{autodoc2-docstring} altdss.Generator.GeneratorProperties.values
```

````

`````

`````{py:class} IGenerator(iobj)
:canonical: altdss.Generator.IGenerator

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Generator.GeneratorBatch`

```{autodoc2-docstring} altdss.Generator.IGenerator
```

````{py:attribute} Balanced
:canonical: altdss.Generator.IGenerator.Balanced
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Generator.IGenerator.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Generator.IGenerator.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.Generator.IGenerator.Class
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Class
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Generator.IGenerator.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Generator.IGenerator.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Generator.IGenerator.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Generator.IGenerator.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Generator.IGenerator.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Generator.IGenerator.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Generator.IGenerator.Currents

```{autodoc2-docstring} altdss.Generator.IGenerator.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Generator.IGenerator.CurrentsMagAng

```{autodoc2-docstring} altdss.Generator.IGenerator.CurrentsMagAng
```

````

````{py:attribute} D
:canonical: altdss.Generator.IGenerator.D
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.D
```

````

````{py:attribute} Daily
:canonical: altdss.Generator.IGenerator.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Generator.IGenerator.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Generator.IGenerator.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.DebugTrace
```

````

````{py:attribute} DispMode
:canonical: altdss.Generator.IGenerator.DispMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.DispMode
```

````

````{py:attribute} DispMode_str
:canonical: altdss.Generator.IGenerator.DispMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.DispMode_str
```

````

````{py:attribute} DispValue
:canonical: altdss.Generator.IGenerator.DispValue
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.DispValue
```

````

````{py:attribute} Duty
:canonical: altdss.Generator.IGenerator.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.Generator.IGenerator.DutyStart
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.DutyStart
```

````

````{py:attribute} Duty_str
:canonical: altdss.Generator.IGenerator.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Duty_str
```

````

````{py:attribute} DynOut
:canonical: altdss.Generator.IGenerator.DynOut
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Generator.IGenerator.DynamicEq
:type: typing.List[altdss.DynamicExp.DynamicExp]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.DynamicEq
```

````

````{py:attribute} DynamicEq_str
:canonical: altdss.Generator.IGenerator.DynamicEq_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.DynamicEq_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Generator.IGenerator.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Generator.IGenerator.EnergyMeter

```{autodoc2-docstring} altdss.Generator.IGenerator.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Generator.IGenerator.EnergyMeterName

```{autodoc2-docstring} altdss.Generator.IGenerator.EnergyMeterName
```

````

````{py:attribute} ForceOn
:canonical: altdss.Generator.IGenerator.ForceOn
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.ForceOn
```

````

````{py:attribute} FuelkWh
:canonical: altdss.Generator.IGenerator.FuelkWh
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.FuelkWh
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Generator.IGenerator.FullName

```{autodoc2-docstring} altdss.Generator.IGenerator.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Generator.IGenerator.GUID

```{autodoc2-docstring} altdss.Generator.IGenerator.GUID
```

````

````{py:attribute} H
:canonical: altdss.Generator.IGenerator.H
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.H
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Generator.IGenerator.Handle

```{autodoc2-docstring} altdss.Generator.IGenerator.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Generator.IGenerator.HasOCPDevice

```{autodoc2-docstring} altdss.Generator.IGenerator.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Generator.IGenerator.HasSwitchControl

```{autodoc2-docstring} altdss.Generator.IGenerator.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Generator.IGenerator.HasVoltControl

```{autodoc2-docstring} altdss.Generator.IGenerator.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Generator.IGenerator.IsIsolated

```{autodoc2-docstring} altdss.Generator.IGenerator.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Generator.IGenerator.Like

```{autodoc2-docstring} altdss.Generator.IGenerator.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Generator.IGenerator.Losses

```{autodoc2-docstring} altdss.Generator.IGenerator.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Generator.IGenerator.MaxCurrent

```{autodoc2-docstring} altdss.Generator.IGenerator.MaxCurrent
```

````

````{py:attribute} Maxkvar
:canonical: altdss.Generator.IGenerator.Maxkvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Maxkvar
```

````

````{py:attribute} Minkvar
:canonical: altdss.Generator.IGenerator.Minkvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Minkvar
```

````

````{py:attribute} Model
:canonical: altdss.Generator.IGenerator.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Model
```

````

````{py:property} Name
:canonical: altdss.Generator.IGenerator.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Generator.IGenerator.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Generator.IGenerator.NumConductors

```{autodoc2-docstring} altdss.Generator.IGenerator.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Generator.IGenerator.NumControllers

```{autodoc2-docstring} altdss.Generator.IGenerator.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Generator.IGenerator.NumPhases

```{autodoc2-docstring} altdss.Generator.IGenerator.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Generator.IGenerator.NumTerminals

```{autodoc2-docstring} altdss.Generator.IGenerator.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Generator.IGenerator.OCPDevice

```{autodoc2-docstring} altdss.Generator.IGenerator.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Generator.IGenerator.OCPDeviceIndex

```{autodoc2-docstring} altdss.Generator.IGenerator.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Generator.IGenerator.OCPDeviceType

```{autodoc2-docstring} altdss.Generator.IGenerator.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.Generator.IGenerator.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.PF
```

````

````{py:attribute} PVFactor
:canonical: altdss.Generator.IGenerator.PVFactor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.PVFactor
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Generator.IGenerator.PhaseLosses

```{autodoc2-docstring} altdss.Generator.IGenerator.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Generator.IGenerator.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Generator.IGenerator.Powers

```{autodoc2-docstring} altdss.Generator.IGenerator.Powers
```

````

````{py:method} Refuel(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Generator.IGenerator.Refuel

```{autodoc2-docstring} altdss.Generator.IGenerator.Refuel
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Generator.IGenerator.SeqCurrents

```{autodoc2-docstring} altdss.Generator.IGenerator.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Generator.IGenerator.SeqPowers

```{autodoc2-docstring} altdss.Generator.IGenerator.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Generator.IGenerator.SeqVoltages

```{autodoc2-docstring} altdss.Generator.IGenerator.SeqVoltages
```

````

````{py:attribute} ShaftData
:canonical: altdss.Generator.IGenerator.ShaftData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.ShaftData
```

````

````{py:attribute} ShaftModel
:canonical: altdss.Generator.IGenerator.ShaftModel
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.ShaftModel
```

````

````{py:attribute} Spectrum
:canonical: altdss.Generator.IGenerator.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Generator.IGenerator.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Spectrum_str
```

````

````{py:attribute} Status
:canonical: altdss.Generator.IGenerator.Status
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Status
```

````

````{py:attribute} Status_str
:canonical: altdss.Generator.IGenerator.Status_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Status_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Generator.IGenerator.TotalPowers

```{autodoc2-docstring} altdss.Generator.IGenerator.TotalPowers
```

````

````{py:attribute} UseFuel
:canonical: altdss.Generator.IGenerator.UseFuel
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.UseFuel
```

````

````{py:attribute} UserData
:canonical: altdss.Generator.IGenerator.UserData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Generator.IGenerator.UserModel
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Generator.IGenerator.VMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Generator.IGenerator.VMinpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.VMinpu
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Generator.IGenerator.Voltages

```{autodoc2-docstring} altdss.Generator.IGenerator.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Generator.IGenerator.VoltagesMagAng

```{autodoc2-docstring} altdss.Generator.IGenerator.VoltagesMagAng
```

````

````{py:attribute} Vpu
:canonical: altdss.Generator.IGenerator.Vpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Vpu
```

````

````{py:attribute} XRdp
:canonical: altdss.Generator.IGenerator.XRdp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.XRdp
```

````

````{py:attribute} Xd
:canonical: altdss.Generator.IGenerator.Xd
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Xd
```

````

````{py:attribute} Xdp
:canonical: altdss.Generator.IGenerator.Xdp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Xdp
```

````

````{py:attribute} Xdpp
:canonical: altdss.Generator.IGenerator.Xdpp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Xdpp
```

````

````{py:attribute} Yearly
:canonical: altdss.Generator.IGenerator.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Generator.IGenerator.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.Generator.IGenerator.__call__

```{autodoc2-docstring} altdss.Generator.IGenerator.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Generator.IGenerator.__contains__

```{autodoc2-docstring} altdss.Generator.IGenerator.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Generator.IGenerator.__getitem__

```{autodoc2-docstring} altdss.Generator.IGenerator.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Generator.IGenerator.__init__

```{autodoc2-docstring} altdss.Generator.IGenerator.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Generator.IGenerator.__iter__

```{autodoc2-docstring} altdss.Generator.IGenerator.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Generator.IGenerator.__len__

```{autodoc2-docstring} altdss.Generator.IGenerator.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Generator.IGenerator.batch

```{autodoc2-docstring} altdss.Generator.IGenerator.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Generator.GeneratorBatchProperties]) -> altdss.Generator.GeneratorBatch
:canonical: altdss.Generator.IGenerator.batch_new

```{autodoc2-docstring} altdss.Generator.IGenerator.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Generator.IGenerator.begin_edit

```{autodoc2-docstring} altdss.Generator.IGenerator.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Generator.IGenerator.end_edit

```{autodoc2-docstring} altdss.Generator.IGenerator.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Generator.IGenerator.find

```{autodoc2-docstring} altdss.Generator.IGenerator.find
```

````

````{py:attribute} kV
:canonical: altdss.Generator.IGenerator.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Generator.IGenerator.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Generator.IGenerator.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.kW
```

````

````{py:attribute} kvar
:canonical: altdss.Generator.IGenerator.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.kvar
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Generator.GeneratorProperties]) -> altdss.Generator.Generator
:canonical: altdss.Generator.IGenerator.new

```{autodoc2-docstring} altdss.Generator.IGenerator.new
```

````

````{py:attribute} pctFuel
:canonical: altdss.Generator.IGenerator.pctFuel
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.pctFuel
```

````

````{py:attribute} pctReserve
:canonical: altdss.Generator.IGenerator.pctReserve
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Generator.IGenerator.pctReserve
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Generator.IGenerator.to_json

```{autodoc2-docstring} altdss.Generator.IGenerator.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Generator.IGenerator.to_list

```{autodoc2-docstring} altdss.Generator.IGenerator.to_list
```

````

`````
