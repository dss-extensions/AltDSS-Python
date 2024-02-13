# {py:mod}`altdss.GICLine`

```{py:module} altdss.GICLine
```

```{autodoc2-docstring} altdss.GICLine
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GICLine <altdss.GICLine.GICLine>`
  - ```{autodoc2-docstring} altdss.GICLine.GICLine
    :summary:
    ```
* - {py:obj}`GICLineBatch <altdss.GICLine.GICLineBatch>`
  - ```{autodoc2-docstring} altdss.GICLine.GICLineBatch
    :summary:
    ```
* - {py:obj}`GICLineBatchProperties <altdss.GICLine.GICLineBatchProperties>`
  - ```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties
    :summary:
    ```
* - {py:obj}`GICLineProperties <altdss.GICLine.GICLineProperties>`
  - ```{autodoc2-docstring} altdss.GICLine.GICLineProperties
    :summary:
    ```
* - {py:obj}`IGICLine <altdss.GICLine.IGICLine>`
  - ```{autodoc2-docstring} altdss.GICLine.IGICLine
    :summary:
    ```
````

### API

`````{py:class} GICLine(api_util, ptr)
:canonical: altdss.GICLine.GICLine

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`

```{autodoc2-docstring} altdss.GICLine.GICLine
```

````{py:attribute} Angle
:canonical: altdss.GICLine.GICLine.Angle
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICLine.GICLine.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.GICLine.GICLine.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.GICLine.GICLine.Bus2
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Bus2
```

````

````{py:attribute} C
:canonical: altdss.GICLine.GICLine.C
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.C
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.GICLine.GICLine.Close

```{autodoc2-docstring} altdss.GICLine.GICLine.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLine.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GICLine.GICLine.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLine.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GICLine.GICLine.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLine.Currents

```{autodoc2-docstring} altdss.GICLine.GICLine.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.GICLine.GICLine.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.DisplayName
```

````

````{py:attribute} EE
:canonical: altdss.GICLine.GICLine.EE
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICLine.GICLine.EN
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICLine.GICLine.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.GICLine.GICLine.EnergyMeter

```{autodoc2-docstring} altdss.GICLine.GICLine.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.GICLine.GICLine.EnergyMeterName

```{autodoc2-docstring} altdss.GICLine.GICLine.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.GICLine.GICLine.Frequency
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Frequency
```

````

````{py:method} FullName() -> str
:canonical: altdss.GICLine.GICLine.FullName

```{autodoc2-docstring} altdss.GICLine.GICLine.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GICLine.GICLine.GUID

```{autodoc2-docstring} altdss.GICLine.GICLine.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.GICLine.GICLine.GetVariableValue

```{autodoc2-docstring} altdss.GICLine.GICLine.GetVariableValue
```

````

````{py:method} Handle() -> int
:canonical: altdss.GICLine.GICLine.Handle

```{autodoc2-docstring} altdss.GICLine.GICLine.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GICLine.GICLine.HasOCPDevice

```{autodoc2-docstring} altdss.GICLine.GICLine.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GICLine.GICLine.HasSwitchControl

```{autodoc2-docstring} altdss.GICLine.GICLine.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GICLine.GICLine.HasVoltControl

```{autodoc2-docstring} altdss.GICLine.GICLine.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.GICLine.GICLine.IsIsolated

```{autodoc2-docstring} altdss.GICLine.GICLine.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.GICLine.GICLine.IsOpen

```{autodoc2-docstring} altdss.GICLine.GICLine.IsOpen
```

````

````{py:attribute} Lat1
:canonical: altdss.GICLine.GICLine.Lat1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICLine.GICLine.Lat2
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Lat2
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.GICLine.GICLine.Like

```{autodoc2-docstring} altdss.GICLine.GICLine.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICLine.GICLine.Lon1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICLine.GICLine.Lon2
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Lon2
```

````

````{py:method} Losses() -> complex
:canonical: altdss.GICLine.GICLine.Losses

```{autodoc2-docstring} altdss.GICLine.GICLine.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GICLine.GICLine.MaxCurrent

```{autodoc2-docstring} altdss.GICLine.GICLine.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GICLine.GICLine.Name
:type: str

```{autodoc2-docstring} altdss.GICLine.GICLine.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.GICLine.GICLine.NodeOrder

```{autodoc2-docstring} altdss.GICLine.GICLine.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.GICLine.GICLine.NodeRef

```{autodoc2-docstring} altdss.GICLine.GICLine.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.GICLine.GICLine.NumConductors

```{autodoc2-docstring} altdss.GICLine.GICLine.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.GICLine.GICLine.NumControllers

```{autodoc2-docstring} altdss.GICLine.GICLine.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.GICLine.GICLine.NumPhases

```{autodoc2-docstring} altdss.GICLine.GICLine.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.GICLine.GICLine.NumTerminals

```{autodoc2-docstring} altdss.GICLine.GICLine.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.GICLine.GICLine.OCPDevice

```{autodoc2-docstring} altdss.GICLine.GICLine.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.GICLine.GICLine.OCPDeviceIndex

```{autodoc2-docstring} altdss.GICLine.GICLine.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GICLine.GICLine.OCPDeviceType

```{autodoc2-docstring} altdss.GICLine.GICLine.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.GICLine.GICLine.Open

```{autodoc2-docstring} altdss.GICLine.GICLine.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLine.PhaseLosses

```{autodoc2-docstring} altdss.GICLine.GICLine.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.GICLine.GICLine.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLine.Powers

```{autodoc2-docstring} altdss.GICLine.GICLine.Powers
```

````

````{py:attribute} R
:canonical: altdss.GICLine.GICLine.R
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.R
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.GICLine.GICLine.Residuals

```{autodoc2-docstring} altdss.GICLine.GICLine.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GICLine.GICLine.SeqCurrents

```{autodoc2-docstring} altdss.GICLine.GICLine.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLine.SeqPowers

```{autodoc2-docstring} altdss.GICLine.GICLine.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GICLine.GICLine.SeqVoltages

```{autodoc2-docstring} altdss.GICLine.GICLine.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.GICLine.GICLine.SetVariableValue

```{autodoc2-docstring} altdss.GICLine.GICLine.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICLine.GICLine.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.GICLine.GICLine.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLine.TotalPowers

```{autodoc2-docstring} altdss.GICLine.GICLine.TotalPowers
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.GICLine.GICLine.VariableNames

```{autodoc2-docstring} altdss.GICLine.GICLine.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.GICLine.GICLine.VariableValues

```{autodoc2-docstring} altdss.GICLine.GICLine.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.GICLine.GICLine.VariablesDict

```{autodoc2-docstring} altdss.GICLine.GICLine.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLine.Voltages

```{autodoc2-docstring} altdss.GICLine.GICLine.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICLine.GICLine.VoltagesMagAng

```{autodoc2-docstring} altdss.GICLine.GICLine.VoltagesMagAng
```

````

````{py:attribute} Volts
:canonical: altdss.GICLine.GICLine.Volts
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.Volts
```

````

````{py:attribute} X
:canonical: altdss.GICLine.GICLine.X
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLine.X
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLine.YPrim

```{autodoc2-docstring} altdss.GICLine.GICLine.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.GICLine.GICLine.__hash__

```{autodoc2-docstring} altdss.GICLine.GICLine.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.GICLine.GICLine.__init__

```{autodoc2-docstring} altdss.GICLine.GICLine.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.GICLine.GICLine.__ne__

```{autodoc2-docstring} altdss.GICLine.GICLine.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.GICLine.GICLine.__repr__

```{autodoc2-docstring} altdss.GICLine.GICLine.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GICLine.GICLine.begin_edit

```{autodoc2-docstring} altdss.GICLine.GICLine.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GICLine.GICLine.end_edit

```{autodoc2-docstring} altdss.GICLine.GICLine.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GICLine.GICLine.to_json

```{autodoc2-docstring} altdss.GICLine.GICLine.to_json
```

````

`````

`````{py:class} GICLineBatch(api_util, **kwargs)
:canonical: altdss.GICLine.GICLineBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.GICLine.GICLineBatch
```

````{py:attribute} Angle
:canonical: altdss.GICLine.GICLineBatch.Angle
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICLine.GICLineBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.GICLine.GICLineBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.GICLine.GICLineBatch.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Bus2
```

````

````{py:attribute} C
:canonical: altdss.GICLine.GICLineBatch.C
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.C
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLineBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLineBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLineBatch.Currents

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICLine.GICLineBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.CurrentsMagAng
```

````

````{py:attribute} EE
:canonical: altdss.GICLine.GICLineBatch.EE
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICLine.GICLineBatch.EN
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICLine.GICLineBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.GICLine.GICLineBatch.EnergyMeter

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.GICLine.GICLineBatch.EnergyMeterName

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.GICLine.GICLineBatch.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GICLine.GICLineBatch.FullName

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GICLine.GICLineBatch.GUID

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.GICLine.GICLineBatch.Handle

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GICLine.GICLineBatch.HasOCPDevice

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GICLine.GICLineBatch.HasSwitchControl

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GICLine.GICLineBatch.HasVoltControl

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.GICLine.GICLineBatch.IsIsolated

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.IsIsolated
```

````

````{py:attribute} Lat1
:canonical: altdss.GICLine.GICLineBatch.Lat1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICLine.GICLineBatch.Lat2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Lat2
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GICLine.GICLineBatch.Like

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICLine.GICLineBatch.Lon1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICLine.GICLineBatch.Lon2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Lon2
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLineBatch.Losses

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GICLine.GICLineBatch.MaxCurrent

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GICLine.GICLineBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.GICLine.GICLineBatch.NumConductors

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.GICLine.GICLineBatch.NumControllers

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.GICLine.GICLineBatch.NumPhases

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.GICLine.GICLineBatch.NumTerminals

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.GICLine.GICLineBatch.OCPDevice

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.GICLine.GICLineBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GICLine.GICLineBatch.OCPDeviceType

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLineBatch.PhaseLosses

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.GICLine.GICLineBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLineBatch.Powers

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Powers
```

````

````{py:attribute} R
:canonical: altdss.GICLine.GICLineBatch.R
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.R
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GICLine.GICLineBatch.SeqCurrents

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLineBatch.SeqPowers

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GICLine.GICLineBatch.SeqVoltages

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICLine.GICLineBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.GICLine.GICLineBatch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLineBatch.TotalPowers

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.GICLineBatch.Voltages

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICLine.GICLineBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.VoltagesMagAng
```

````

````{py:attribute} Volts
:canonical: altdss.GICLine.GICLineBatch.Volts
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.Volts
```

````

````{py:attribute} X
:canonical: altdss.GICLine.GICLineBatch.X
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.X
```

````

````{py:method} __call__()
:canonical: altdss.GICLine.GICLineBatch.__call__

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.GICLine.GICLineBatch.__getitem__

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.GICLine.GICLineBatch.__init__

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GICLine.GICLineBatch.__iter__

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GICLine.GICLineBatch.__len__

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GICLine.GICLineBatch.begin_edit

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GICLine.GICLineBatch.end_edit

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GICLine.GICLineBatch.to_json

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GICLine.GICLineBatch.to_list

```{autodoc2-docstring} altdss.GICLine.GICLineBatch.to_list
```

````

`````

`````{py:class} GICLineBatchProperties()
:canonical: altdss.GICLine.GICLineBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties
```

````{py:attribute} Angle
:canonical: altdss.GICLine.GICLineBatchProperties.Angle
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICLine.GICLineBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.GICLine.GICLineBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.GICLine.GICLineBatchProperties.Bus2
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Bus2
```

````

````{py:attribute} C
:canonical: altdss.GICLine.GICLineBatchProperties.C
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.C
```

````

````{py:attribute} EE
:canonical: altdss.GICLine.GICLineBatchProperties.EE
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICLine.GICLineBatchProperties.EN
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICLine.GICLineBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.GICLine.GICLineBatchProperties.Frequency
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Frequency
```

````

````{py:attribute} Lat1
:canonical: altdss.GICLine.GICLineBatchProperties.Lat1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICLine.GICLineBatchProperties.Lat2
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Lat2
```

````

````{py:attribute} Like
:canonical: altdss.GICLine.GICLineBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICLine.GICLineBatchProperties.Lon1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICLine.GICLineBatchProperties.Lon2
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Lon2
```

````

````{py:attribute} Phases
:canonical: altdss.GICLine.GICLineBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Phases
```

````

````{py:attribute} R
:canonical: altdss.GICLine.GICLineBatchProperties.R
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.R
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICLine.GICLineBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Spectrum
```

````

````{py:attribute} Volts
:canonical: altdss.GICLine.GICLineBatchProperties.Volts
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.Volts
```

````

````{py:attribute} X
:canonical: altdss.GICLine.GICLineBatchProperties.X
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.X
```

````

````{py:method} __contains__()
:canonical: altdss.GICLine.GICLineBatchProperties.__contains__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GICLine.GICLineBatchProperties.__delattr__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GICLine.GICLineBatchProperties.__delitem__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GICLine.GICLineBatchProperties.__dir__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GICLine.GICLineBatchProperties.__format__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GICLine.GICLineBatchProperties.__ge__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GICLine.GICLineBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GICLine.GICLineBatchProperties.__getitem__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GICLine.GICLineBatchProperties.__getstate__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GICLine.GICLineBatchProperties.__gt__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GICLine.GICLineBatchProperties.__init__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GICLine.GICLineBatchProperties.__ior__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GICLine.GICLineBatchProperties.__iter__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GICLine.GICLineBatchProperties.__le__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GICLine.GICLineBatchProperties.__len__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GICLine.GICLineBatchProperties.__lt__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GICLine.GICLineBatchProperties.__ne__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GICLine.GICLineBatchProperties.__new__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GICLine.GICLineBatchProperties.__or__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GICLine.GICLineBatchProperties.__reduce__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GICLine.GICLineBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GICLine.GICLineBatchProperties.__repr__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GICLine.GICLineBatchProperties.__reversed__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GICLine.GICLineBatchProperties.__ror__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GICLine.GICLineBatchProperties.__setitem__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GICLine.GICLineBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GICLine.GICLineBatchProperties.__str__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GICLine.GICLineBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GICLine.GICLineBatchProperties.clear

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GICLine.GICLineBatchProperties.copy

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GICLine.GICLineBatchProperties.get

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.GICLine.GICLineBatchProperties.items

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.GICLine.GICLineBatchProperties.keys

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.GICLine.GICLineBatchProperties.pop

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GICLine.GICLineBatchProperties.popitem

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GICLine.GICLineBatchProperties.setdefault

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GICLine.GICLineBatchProperties.update

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.GICLine.GICLineBatchProperties.values

```{autodoc2-docstring} altdss.GICLine.GICLineBatchProperties.values
```

````

`````

`````{py:class} GICLineProperties()
:canonical: altdss.GICLine.GICLineProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GICLine.GICLineProperties
```

````{py:attribute} Angle
:canonical: altdss.GICLine.GICLineProperties.Angle
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICLine.GICLineProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.GICLine.GICLineProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.GICLine.GICLineProperties.Bus2
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Bus2
```

````

````{py:attribute} C
:canonical: altdss.GICLine.GICLineProperties.C
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.C
```

````

````{py:attribute} EE
:canonical: altdss.GICLine.GICLineProperties.EE
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICLine.GICLineProperties.EN
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICLine.GICLineProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.GICLine.GICLineProperties.Frequency
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Frequency
```

````

````{py:attribute} Lat1
:canonical: altdss.GICLine.GICLineProperties.Lat1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICLine.GICLineProperties.Lat2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Lat2
```

````

````{py:attribute} Like
:canonical: altdss.GICLine.GICLineProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICLine.GICLineProperties.Lon1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICLine.GICLineProperties.Lon2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Lon2
```

````

````{py:attribute} Phases
:canonical: altdss.GICLine.GICLineProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Phases
```

````

````{py:attribute} R
:canonical: altdss.GICLine.GICLineProperties.R
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.R
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICLine.GICLineProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Spectrum
```

````

````{py:attribute} Volts
:canonical: altdss.GICLine.GICLineProperties.Volts
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.Volts
```

````

````{py:attribute} X
:canonical: altdss.GICLine.GICLineProperties.X
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.X
```

````

````{py:method} __contains__()
:canonical: altdss.GICLine.GICLineProperties.__contains__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GICLine.GICLineProperties.__delattr__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GICLine.GICLineProperties.__delitem__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GICLine.GICLineProperties.__dir__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GICLine.GICLineProperties.__format__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GICLine.GICLineProperties.__ge__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GICLine.GICLineProperties.__getattribute__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GICLine.GICLineProperties.__getitem__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GICLine.GICLineProperties.__getstate__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GICLine.GICLineProperties.__gt__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GICLine.GICLineProperties.__init__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GICLine.GICLineProperties.__ior__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GICLine.GICLineProperties.__iter__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GICLine.GICLineProperties.__le__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GICLine.GICLineProperties.__len__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GICLine.GICLineProperties.__lt__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GICLine.GICLineProperties.__ne__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GICLine.GICLineProperties.__new__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GICLine.GICLineProperties.__or__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GICLine.GICLineProperties.__reduce__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GICLine.GICLineProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GICLine.GICLineProperties.__repr__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GICLine.GICLineProperties.__reversed__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GICLine.GICLineProperties.__ror__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GICLine.GICLineProperties.__setitem__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GICLine.GICLineProperties.__sizeof__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GICLine.GICLineProperties.__str__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GICLine.GICLineProperties.__subclasshook__

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GICLine.GICLineProperties.clear

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GICLine.GICLineProperties.copy

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GICLine.GICLineProperties.get

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.get
```

````

````{py:method} items()
:canonical: altdss.GICLine.GICLineProperties.items

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.items
```

````

````{py:method} keys()
:canonical: altdss.GICLine.GICLineProperties.keys

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.GICLine.GICLineProperties.pop

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GICLine.GICLineProperties.popitem

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GICLine.GICLineProperties.setdefault

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GICLine.GICLineProperties.update

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.update
```

````

````{py:method} values()
:canonical: altdss.GICLine.GICLineProperties.values

```{autodoc2-docstring} altdss.GICLine.GICLineProperties.values
```

````

`````

`````{py:class} IGICLine(iobj)
:canonical: altdss.GICLine.IGICLine

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.GICLine.GICLineBatch`

```{autodoc2-docstring} altdss.GICLine.IGICLine
```

````{py:attribute} Angle
:canonical: altdss.GICLine.IGICLine.Angle
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICLine.IGICLine.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.GICLine.IGICLine.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.GICLine.IGICLine.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Bus2
```

````

````{py:attribute} C
:canonical: altdss.GICLine.IGICLine.C
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.C
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.IGICLine.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GICLine.IGICLine.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.IGICLine.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GICLine.IGICLine.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.IGICLine.Currents

```{autodoc2-docstring} altdss.GICLine.IGICLine.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICLine.IGICLine.CurrentsMagAng

```{autodoc2-docstring} altdss.GICLine.IGICLine.CurrentsMagAng
```

````

````{py:attribute} EE
:canonical: altdss.GICLine.IGICLine.EE
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICLine.IGICLine.EN
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICLine.IGICLine.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.GICLine.IGICLine.EnergyMeter

```{autodoc2-docstring} altdss.GICLine.IGICLine.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.GICLine.IGICLine.EnergyMeterName

```{autodoc2-docstring} altdss.GICLine.IGICLine.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.GICLine.IGICLine.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GICLine.IGICLine.FullName

```{autodoc2-docstring} altdss.GICLine.IGICLine.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GICLine.IGICLine.GUID

```{autodoc2-docstring} altdss.GICLine.IGICLine.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.GICLine.IGICLine.Handle

```{autodoc2-docstring} altdss.GICLine.IGICLine.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GICLine.IGICLine.HasOCPDevice

```{autodoc2-docstring} altdss.GICLine.IGICLine.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GICLine.IGICLine.HasSwitchControl

```{autodoc2-docstring} altdss.GICLine.IGICLine.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GICLine.IGICLine.HasVoltControl

```{autodoc2-docstring} altdss.GICLine.IGICLine.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.GICLine.IGICLine.IsIsolated

```{autodoc2-docstring} altdss.GICLine.IGICLine.IsIsolated
```

````

````{py:attribute} Lat1
:canonical: altdss.GICLine.IGICLine.Lat1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICLine.IGICLine.Lat2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Lat2
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GICLine.IGICLine.Like

```{autodoc2-docstring} altdss.GICLine.IGICLine.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICLine.IGICLine.Lon1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICLine.IGICLine.Lon2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Lon2
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.IGICLine.Losses

```{autodoc2-docstring} altdss.GICLine.IGICLine.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GICLine.IGICLine.MaxCurrent

```{autodoc2-docstring} altdss.GICLine.IGICLine.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GICLine.IGICLine.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GICLine.IGICLine.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.GICLine.IGICLine.NumConductors

```{autodoc2-docstring} altdss.GICLine.IGICLine.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.GICLine.IGICLine.NumControllers

```{autodoc2-docstring} altdss.GICLine.IGICLine.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.GICLine.IGICLine.NumPhases

```{autodoc2-docstring} altdss.GICLine.IGICLine.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.GICLine.IGICLine.NumTerminals

```{autodoc2-docstring} altdss.GICLine.IGICLine.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.GICLine.IGICLine.OCPDevice

```{autodoc2-docstring} altdss.GICLine.IGICLine.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.GICLine.IGICLine.OCPDeviceIndex

```{autodoc2-docstring} altdss.GICLine.IGICLine.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GICLine.IGICLine.OCPDeviceType

```{autodoc2-docstring} altdss.GICLine.IGICLine.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.IGICLine.PhaseLosses

```{autodoc2-docstring} altdss.GICLine.IGICLine.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.GICLine.IGICLine.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.IGICLine.Powers

```{autodoc2-docstring} altdss.GICLine.IGICLine.Powers
```

````

````{py:attribute} R
:canonical: altdss.GICLine.IGICLine.R
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.R
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GICLine.IGICLine.SeqCurrents

```{autodoc2-docstring} altdss.GICLine.IGICLine.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.IGICLine.SeqPowers

```{autodoc2-docstring} altdss.GICLine.IGICLine.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GICLine.IGICLine.SeqVoltages

```{autodoc2-docstring} altdss.GICLine.IGICLine.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICLine.IGICLine.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.GICLine.IGICLine.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.IGICLine.TotalPowers

```{autodoc2-docstring} altdss.GICLine.IGICLine.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GICLine.IGICLine.Voltages

```{autodoc2-docstring} altdss.GICLine.IGICLine.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICLine.IGICLine.VoltagesMagAng

```{autodoc2-docstring} altdss.GICLine.IGICLine.VoltagesMagAng
```

````

````{py:attribute} Volts
:canonical: altdss.GICLine.IGICLine.Volts
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.Volts
```

````

````{py:attribute} X
:canonical: altdss.GICLine.IGICLine.X
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICLine.IGICLine.X
```

````

````{py:method} __call__()
:canonical: altdss.GICLine.IGICLine.__call__

```{autodoc2-docstring} altdss.GICLine.IGICLine.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.GICLine.IGICLine.__contains__

```{autodoc2-docstring} altdss.GICLine.IGICLine.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.GICLine.IGICLine.__getitem__

```{autodoc2-docstring} altdss.GICLine.IGICLine.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.GICLine.IGICLine.__init__

```{autodoc2-docstring} altdss.GICLine.IGICLine.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GICLine.IGICLine.__iter__

```{autodoc2-docstring} altdss.GICLine.IGICLine.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GICLine.IGICLine.__len__

```{autodoc2-docstring} altdss.GICLine.IGICLine.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.GICLine.IGICLine.batch

```{autodoc2-docstring} altdss.GICLine.IGICLine.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.GICLine.GICLineBatchProperties]) -> altdss.GICLine.GICLineBatch
:canonical: altdss.GICLine.IGICLine.batch_new

```{autodoc2-docstring} altdss.GICLine.IGICLine.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GICLine.IGICLine.begin_edit

```{autodoc2-docstring} altdss.GICLine.IGICLine.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GICLine.IGICLine.end_edit

```{autodoc2-docstring} altdss.GICLine.IGICLine.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.GICLine.IGICLine.find

```{autodoc2-docstring} altdss.GICLine.IGICLine.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.GICLine.GICLineProperties]) -> altdss.GICLine.GICLine
:canonical: altdss.GICLine.IGICLine.new

```{autodoc2-docstring} altdss.GICLine.IGICLine.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GICLine.IGICLine.to_json

```{autodoc2-docstring} altdss.GICLine.IGICLine.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GICLine.IGICLine.to_list

```{autodoc2-docstring} altdss.GICLine.IGICLine.to_list
```

````

`````
