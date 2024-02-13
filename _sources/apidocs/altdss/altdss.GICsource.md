# {py:mod}`altdss.GICsource`

```{py:module} altdss.GICsource
```

```{autodoc2-docstring} altdss.GICsource
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GICsource <altdss.GICsource.GICsource>`
  - ```{autodoc2-docstring} altdss.GICsource.GICsource
    :summary:
    ```
* - {py:obj}`GICsourceBatch <altdss.GICsource.GICsourceBatch>`
  - ```{autodoc2-docstring} altdss.GICsource.GICsourceBatch
    :summary:
    ```
* - {py:obj}`GICsourceBatchProperties <altdss.GICsource.GICsourceBatchProperties>`
  - ```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties
    :summary:
    ```
* - {py:obj}`GICsourceProperties <altdss.GICsource.GICsourceProperties>`
  - ```{autodoc2-docstring} altdss.GICsource.GICsourceProperties
    :summary:
    ```
* - {py:obj}`IGICsource <altdss.GICsource.IGICsource>`
  - ```{autodoc2-docstring} altdss.GICsource.IGICsource
    :summary:
    ```
````

### API

`````{py:class} GICsource(api_util, ptr)
:canonical: altdss.GICsource.GICsource

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`

```{autodoc2-docstring} altdss.GICsource.GICsource
```

````{py:attribute} Angle
:canonical: altdss.GICsource.GICsource.Angle
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICsource.GICsource.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.GICsource.GICsource.Close

```{autodoc2-docstring} altdss.GICsource.GICsource.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsource.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GICsource.GICsource.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsource.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GICsource.GICsource.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsource.Currents

```{autodoc2-docstring} altdss.GICsource.GICsource.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.GICsource.GICsource.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.DisplayName
```

````

````{py:attribute} EE
:canonical: altdss.GICsource.GICsource.EE
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICsource.GICsource.EN
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICsource.GICsource.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.GICsource.GICsource.EnergyMeter

```{autodoc2-docstring} altdss.GICsource.GICsource.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.GICsource.GICsource.EnergyMeterName

```{autodoc2-docstring} altdss.GICsource.GICsource.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.GICsource.GICsource.Frequency
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Frequency
```

````

````{py:method} FullName() -> str
:canonical: altdss.GICsource.GICsource.FullName

```{autodoc2-docstring} altdss.GICsource.GICsource.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GICsource.GICsource.GUID

```{autodoc2-docstring} altdss.GICsource.GICsource.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.GICsource.GICsource.GetVariableValue

```{autodoc2-docstring} altdss.GICsource.GICsource.GetVariableValue
```

````

````{py:method} Handle() -> int
:canonical: altdss.GICsource.GICsource.Handle

```{autodoc2-docstring} altdss.GICsource.GICsource.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GICsource.GICsource.HasOCPDevice

```{autodoc2-docstring} altdss.GICsource.GICsource.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GICsource.GICsource.HasSwitchControl

```{autodoc2-docstring} altdss.GICsource.GICsource.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GICsource.GICsource.HasVoltControl

```{autodoc2-docstring} altdss.GICsource.GICsource.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.GICsource.GICsource.IsIsolated

```{autodoc2-docstring} altdss.GICsource.GICsource.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.GICsource.GICsource.IsOpen

```{autodoc2-docstring} altdss.GICsource.GICsource.IsOpen
```

````

````{py:attribute} Lat1
:canonical: altdss.GICsource.GICsource.Lat1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICsource.GICsource.Lat2
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Lat2
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.GICsource.GICsource.Like

```{autodoc2-docstring} altdss.GICsource.GICsource.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICsource.GICsource.Lon1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICsource.GICsource.Lon2
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Lon2
```

````

````{py:method} Losses() -> complex
:canonical: altdss.GICsource.GICsource.Losses

```{autodoc2-docstring} altdss.GICsource.GICsource.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GICsource.GICsource.MaxCurrent

```{autodoc2-docstring} altdss.GICsource.GICsource.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GICsource.GICsource.Name
:type: str

```{autodoc2-docstring} altdss.GICsource.GICsource.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.GICsource.GICsource.NodeOrder

```{autodoc2-docstring} altdss.GICsource.GICsource.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.GICsource.GICsource.NodeRef

```{autodoc2-docstring} altdss.GICsource.GICsource.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.GICsource.GICsource.NumConductors

```{autodoc2-docstring} altdss.GICsource.GICsource.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.GICsource.GICsource.NumControllers

```{autodoc2-docstring} altdss.GICsource.GICsource.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.GICsource.GICsource.NumPhases

```{autodoc2-docstring} altdss.GICsource.GICsource.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.GICsource.GICsource.NumTerminals

```{autodoc2-docstring} altdss.GICsource.GICsource.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.GICsource.GICsource.OCPDevice

```{autodoc2-docstring} altdss.GICsource.GICsource.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.GICsource.GICsource.OCPDeviceIndex

```{autodoc2-docstring} altdss.GICsource.GICsource.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GICsource.GICsource.OCPDeviceType

```{autodoc2-docstring} altdss.GICsource.GICsource.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.GICsource.GICsource.Open

```{autodoc2-docstring} altdss.GICsource.GICsource.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsource.PhaseLosses

```{autodoc2-docstring} altdss.GICsource.GICsource.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.GICsource.GICsource.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsource.Powers

```{autodoc2-docstring} altdss.GICsource.GICsource.Powers
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.GICsource.GICsource.Residuals

```{autodoc2-docstring} altdss.GICsource.GICsource.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GICsource.GICsource.SeqCurrents

```{autodoc2-docstring} altdss.GICsource.GICsource.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsource.SeqPowers

```{autodoc2-docstring} altdss.GICsource.GICsource.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GICsource.GICsource.SeqVoltages

```{autodoc2-docstring} altdss.GICsource.GICsource.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.GICsource.GICsource.SetVariableValue

```{autodoc2-docstring} altdss.GICsource.GICsource.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICsource.GICsource.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.GICsource.GICsource.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsource.TotalPowers

```{autodoc2-docstring} altdss.GICsource.GICsource.TotalPowers
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.GICsource.GICsource.VariableNames

```{autodoc2-docstring} altdss.GICsource.GICsource.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.GICsource.GICsource.VariableValues

```{autodoc2-docstring} altdss.GICsource.GICsource.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.GICsource.GICsource.VariablesDict

```{autodoc2-docstring} altdss.GICsource.GICsource.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsource.Voltages

```{autodoc2-docstring} altdss.GICsource.GICsource.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICsource.GICsource.VoltagesMagAng

```{autodoc2-docstring} altdss.GICsource.GICsource.VoltagesMagAng
```

````

````{py:attribute} Volts
:canonical: altdss.GICsource.GICsource.Volts
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsource.Volts
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsource.YPrim

```{autodoc2-docstring} altdss.GICsource.GICsource.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.GICsource.GICsource.__hash__

```{autodoc2-docstring} altdss.GICsource.GICsource.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.GICsource.GICsource.__init__

```{autodoc2-docstring} altdss.GICsource.GICsource.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.GICsource.GICsource.__ne__

```{autodoc2-docstring} altdss.GICsource.GICsource.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.GICsource.GICsource.__repr__

```{autodoc2-docstring} altdss.GICsource.GICsource.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GICsource.GICsource.begin_edit

```{autodoc2-docstring} altdss.GICsource.GICsource.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GICsource.GICsource.end_edit

```{autodoc2-docstring} altdss.GICsource.GICsource.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GICsource.GICsource.to_json

```{autodoc2-docstring} altdss.GICsource.GICsource.to_json
```

````

`````

`````{py:class} GICsourceBatch(api_util, **kwargs)
:canonical: altdss.GICsource.GICsourceBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch
```

````{py:attribute} Angle
:canonical: altdss.GICsource.GICsourceBatch.Angle
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICsource.GICsourceBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsourceBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsourceBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsourceBatch.Currents

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICsource.GICsourceBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.CurrentsMagAng
```

````

````{py:attribute} EE
:canonical: altdss.GICsource.GICsourceBatch.EE
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICsource.GICsourceBatch.EN
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICsource.GICsourceBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.GICsource.GICsourceBatch.EnergyMeter

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.GICsource.GICsourceBatch.EnergyMeterName

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.GICsource.GICsourceBatch.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GICsource.GICsourceBatch.FullName

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GICsource.GICsourceBatch.GUID

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.GICsource.GICsourceBatch.Handle

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GICsource.GICsourceBatch.HasOCPDevice

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GICsource.GICsourceBatch.HasSwitchControl

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GICsource.GICsourceBatch.HasVoltControl

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.GICsource.GICsourceBatch.IsIsolated

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.IsIsolated
```

````

````{py:attribute} Lat1
:canonical: altdss.GICsource.GICsourceBatch.Lat1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICsource.GICsourceBatch.Lat2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Lat2
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GICsource.GICsourceBatch.Like

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICsource.GICsourceBatch.Lon1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICsource.GICsourceBatch.Lon2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Lon2
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsourceBatch.Losses

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GICsource.GICsourceBatch.MaxCurrent

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GICsource.GICsourceBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.GICsource.GICsourceBatch.NumConductors

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.GICsource.GICsourceBatch.NumControllers

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.GICsource.GICsourceBatch.NumPhases

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.GICsource.GICsourceBatch.NumTerminals

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.GICsource.GICsourceBatch.OCPDevice

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.GICsource.GICsourceBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GICsource.GICsourceBatch.OCPDeviceType

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsourceBatch.PhaseLosses

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.GICsource.GICsourceBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsourceBatch.Powers

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GICsource.GICsourceBatch.SeqCurrents

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsourceBatch.SeqPowers

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GICsource.GICsourceBatch.SeqVoltages

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICsource.GICsourceBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.GICsource.GICsourceBatch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsourceBatch.TotalPowers

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.GICsourceBatch.Voltages

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICsource.GICsourceBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.VoltagesMagAng
```

````

````{py:attribute} Volts
:canonical: altdss.GICsource.GICsourceBatch.Volts
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.Volts
```

````

````{py:method} __call__()
:canonical: altdss.GICsource.GICsourceBatch.__call__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.GICsource.GICsourceBatch.__getitem__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.GICsource.GICsourceBatch.__init__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GICsource.GICsourceBatch.__iter__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GICsource.GICsourceBatch.__len__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GICsource.GICsourceBatch.begin_edit

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GICsource.GICsourceBatch.end_edit

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GICsource.GICsourceBatch.to_json

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GICsource.GICsourceBatch.to_list

```{autodoc2-docstring} altdss.GICsource.GICsourceBatch.to_list
```

````

`````

`````{py:class} GICsourceBatchProperties()
:canonical: altdss.GICsource.GICsourceBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties
```

````{py:attribute} Angle
:canonical: altdss.GICsource.GICsourceBatchProperties.Angle
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICsource.GICsourceBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.BaseFreq
```

````

````{py:attribute} EE
:canonical: altdss.GICsource.GICsourceBatchProperties.EE
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICsource.GICsourceBatchProperties.EN
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICsource.GICsourceBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.GICsource.GICsourceBatchProperties.Frequency
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Frequency
```

````

````{py:attribute} Lat1
:canonical: altdss.GICsource.GICsourceBatchProperties.Lat1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICsource.GICsourceBatchProperties.Lat2
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Lat2
```

````

````{py:attribute} Like
:canonical: altdss.GICsource.GICsourceBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICsource.GICsourceBatchProperties.Lon1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICsource.GICsourceBatchProperties.Lon2
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Lon2
```

````

````{py:attribute} Phases
:canonical: altdss.GICsource.GICsourceBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Phases
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICsource.GICsourceBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Spectrum
```

````

````{py:attribute} Volts
:canonical: altdss.GICsource.GICsourceBatchProperties.Volts
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.Volts
```

````

````{py:method} __contains__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__contains__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__delattr__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__delitem__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__dir__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__format__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__ge__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__getitem__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__getstate__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__gt__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__init__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__ior__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__iter__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__le__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__len__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__lt__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__ne__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__new__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__or__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__reduce__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__repr__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__reversed__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__ror__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__setitem__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__str__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GICsource.GICsourceBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GICsource.GICsourceBatchProperties.clear

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GICsource.GICsourceBatchProperties.copy

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GICsource.GICsourceBatchProperties.get

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.GICsource.GICsourceBatchProperties.items

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.GICsource.GICsourceBatchProperties.keys

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.GICsource.GICsourceBatchProperties.pop

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GICsource.GICsourceBatchProperties.popitem

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GICsource.GICsourceBatchProperties.setdefault

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GICsource.GICsourceBatchProperties.update

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.GICsource.GICsourceBatchProperties.values

```{autodoc2-docstring} altdss.GICsource.GICsourceBatchProperties.values
```

````

`````

`````{py:class} GICsourceProperties()
:canonical: altdss.GICsource.GICsourceProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties
```

````{py:attribute} Angle
:canonical: altdss.GICsource.GICsourceProperties.Angle
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICsource.GICsourceProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.BaseFreq
```

````

````{py:attribute} EE
:canonical: altdss.GICsource.GICsourceProperties.EE
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICsource.GICsourceProperties.EN
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICsource.GICsourceProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.GICsource.GICsourceProperties.Frequency
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Frequency
```

````

````{py:attribute} Lat1
:canonical: altdss.GICsource.GICsourceProperties.Lat1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICsource.GICsourceProperties.Lat2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Lat2
```

````

````{py:attribute} Like
:canonical: altdss.GICsource.GICsourceProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICsource.GICsourceProperties.Lon1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICsource.GICsourceProperties.Lon2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Lon2
```

````

````{py:attribute} Phases
:canonical: altdss.GICsource.GICsourceProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Phases
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICsource.GICsourceProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Spectrum
```

````

````{py:attribute} Volts
:canonical: altdss.GICsource.GICsourceProperties.Volts
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.Volts
```

````

````{py:method} __contains__()
:canonical: altdss.GICsource.GICsourceProperties.__contains__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GICsource.GICsourceProperties.__delattr__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GICsource.GICsourceProperties.__delitem__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GICsource.GICsourceProperties.__dir__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GICsource.GICsourceProperties.__format__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GICsource.GICsourceProperties.__ge__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GICsource.GICsourceProperties.__getattribute__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GICsource.GICsourceProperties.__getitem__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GICsource.GICsourceProperties.__getstate__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GICsource.GICsourceProperties.__gt__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GICsource.GICsourceProperties.__init__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GICsource.GICsourceProperties.__ior__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GICsource.GICsourceProperties.__iter__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GICsource.GICsourceProperties.__le__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GICsource.GICsourceProperties.__len__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GICsource.GICsourceProperties.__lt__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GICsource.GICsourceProperties.__ne__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GICsource.GICsourceProperties.__new__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GICsource.GICsourceProperties.__or__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GICsource.GICsourceProperties.__reduce__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GICsource.GICsourceProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GICsource.GICsourceProperties.__repr__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GICsource.GICsourceProperties.__reversed__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GICsource.GICsourceProperties.__ror__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GICsource.GICsourceProperties.__setitem__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GICsource.GICsourceProperties.__sizeof__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GICsource.GICsourceProperties.__str__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GICsource.GICsourceProperties.__subclasshook__

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GICsource.GICsourceProperties.clear

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GICsource.GICsourceProperties.copy

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GICsource.GICsourceProperties.get

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.get
```

````

````{py:method} items()
:canonical: altdss.GICsource.GICsourceProperties.items

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.items
```

````

````{py:method} keys()
:canonical: altdss.GICsource.GICsourceProperties.keys

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.GICsource.GICsourceProperties.pop

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GICsource.GICsourceProperties.popitem

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GICsource.GICsourceProperties.setdefault

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GICsource.GICsourceProperties.update

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.update
```

````

````{py:method} values()
:canonical: altdss.GICsource.GICsourceProperties.values

```{autodoc2-docstring} altdss.GICsource.GICsourceProperties.values
```

````

`````

`````{py:class} IGICsource(iobj)
:canonical: altdss.GICsource.IGICsource

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.GICsource.GICsourceBatch`

```{autodoc2-docstring} altdss.GICsource.IGICsource
```

````{py:attribute} Angle
:canonical: altdss.GICsource.IGICsource.Angle
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICsource.IGICsource.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.IGICsource.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GICsource.IGICsource.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.IGICsource.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GICsource.IGICsource.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.IGICsource.Currents

```{autodoc2-docstring} altdss.GICsource.IGICsource.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICsource.IGICsource.CurrentsMagAng

```{autodoc2-docstring} altdss.GICsource.IGICsource.CurrentsMagAng
```

````

````{py:attribute} EE
:canonical: altdss.GICsource.IGICsource.EE
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.EE
```

````

````{py:attribute} EN
:canonical: altdss.GICsource.IGICsource.EN
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.EN
```

````

````{py:attribute} Enabled
:canonical: altdss.GICsource.IGICsource.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.GICsource.IGICsource.EnergyMeter

```{autodoc2-docstring} altdss.GICsource.IGICsource.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.GICsource.IGICsource.EnergyMeterName

```{autodoc2-docstring} altdss.GICsource.IGICsource.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.GICsource.IGICsource.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GICsource.IGICsource.FullName

```{autodoc2-docstring} altdss.GICsource.IGICsource.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GICsource.IGICsource.GUID

```{autodoc2-docstring} altdss.GICsource.IGICsource.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.GICsource.IGICsource.Handle

```{autodoc2-docstring} altdss.GICsource.IGICsource.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GICsource.IGICsource.HasOCPDevice

```{autodoc2-docstring} altdss.GICsource.IGICsource.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GICsource.IGICsource.HasSwitchControl

```{autodoc2-docstring} altdss.GICsource.IGICsource.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GICsource.IGICsource.HasVoltControl

```{autodoc2-docstring} altdss.GICsource.IGICsource.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.GICsource.IGICsource.IsIsolated

```{autodoc2-docstring} altdss.GICsource.IGICsource.IsIsolated
```

````

````{py:attribute} Lat1
:canonical: altdss.GICsource.IGICsource.Lat1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Lat1
```

````

````{py:attribute} Lat2
:canonical: altdss.GICsource.IGICsource.Lat2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Lat2
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GICsource.IGICsource.Like

```{autodoc2-docstring} altdss.GICsource.IGICsource.Like
```

````

````{py:attribute} Lon1
:canonical: altdss.GICsource.IGICsource.Lon1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Lon1
```

````

````{py:attribute} Lon2
:canonical: altdss.GICsource.IGICsource.Lon2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Lon2
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.IGICsource.Losses

```{autodoc2-docstring} altdss.GICsource.IGICsource.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GICsource.IGICsource.MaxCurrent

```{autodoc2-docstring} altdss.GICsource.IGICsource.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GICsource.IGICsource.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GICsource.IGICsource.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.GICsource.IGICsource.NumConductors

```{autodoc2-docstring} altdss.GICsource.IGICsource.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.GICsource.IGICsource.NumControllers

```{autodoc2-docstring} altdss.GICsource.IGICsource.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.GICsource.IGICsource.NumPhases

```{autodoc2-docstring} altdss.GICsource.IGICsource.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.GICsource.IGICsource.NumTerminals

```{autodoc2-docstring} altdss.GICsource.IGICsource.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.GICsource.IGICsource.OCPDevice

```{autodoc2-docstring} altdss.GICsource.IGICsource.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.GICsource.IGICsource.OCPDeviceIndex

```{autodoc2-docstring} altdss.GICsource.IGICsource.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GICsource.IGICsource.OCPDeviceType

```{autodoc2-docstring} altdss.GICsource.IGICsource.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.IGICsource.PhaseLosses

```{autodoc2-docstring} altdss.GICsource.IGICsource.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.GICsource.IGICsource.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.IGICsource.Powers

```{autodoc2-docstring} altdss.GICsource.IGICsource.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GICsource.IGICsource.SeqCurrents

```{autodoc2-docstring} altdss.GICsource.IGICsource.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.IGICsource.SeqPowers

```{autodoc2-docstring} altdss.GICsource.IGICsource.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GICsource.IGICsource.SeqVoltages

```{autodoc2-docstring} altdss.GICsource.IGICsource.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.GICsource.IGICsource.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.GICsource.IGICsource.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.IGICsource.TotalPowers

```{autodoc2-docstring} altdss.GICsource.IGICsource.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GICsource.IGICsource.Voltages

```{autodoc2-docstring} altdss.GICsource.IGICsource.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICsource.IGICsource.VoltagesMagAng

```{autodoc2-docstring} altdss.GICsource.IGICsource.VoltagesMagAng
```

````

````{py:attribute} Volts
:canonical: altdss.GICsource.IGICsource.Volts
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GICsource.IGICsource.Volts
```

````

````{py:method} __call__()
:canonical: altdss.GICsource.IGICsource.__call__

```{autodoc2-docstring} altdss.GICsource.IGICsource.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.GICsource.IGICsource.__contains__

```{autodoc2-docstring} altdss.GICsource.IGICsource.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.GICsource.IGICsource.__getitem__

```{autodoc2-docstring} altdss.GICsource.IGICsource.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.GICsource.IGICsource.__init__

```{autodoc2-docstring} altdss.GICsource.IGICsource.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GICsource.IGICsource.__iter__

```{autodoc2-docstring} altdss.GICsource.IGICsource.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GICsource.IGICsource.__len__

```{autodoc2-docstring} altdss.GICsource.IGICsource.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.GICsource.IGICsource.batch

```{autodoc2-docstring} altdss.GICsource.IGICsource.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.GICsource.GICsourceBatchProperties]) -> altdss.GICsource.GICsourceBatch
:canonical: altdss.GICsource.IGICsource.batch_new

```{autodoc2-docstring} altdss.GICsource.IGICsource.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GICsource.IGICsource.begin_edit

```{autodoc2-docstring} altdss.GICsource.IGICsource.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GICsource.IGICsource.end_edit

```{autodoc2-docstring} altdss.GICsource.IGICsource.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.GICsource.IGICsource.find

```{autodoc2-docstring} altdss.GICsource.IGICsource.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.GICsource.GICsourceProperties]) -> altdss.GICsource.GICsource
:canonical: altdss.GICsource.IGICsource.new

```{autodoc2-docstring} altdss.GICsource.IGICsource.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GICsource.IGICsource.to_json

```{autodoc2-docstring} altdss.GICsource.IGICsource.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GICsource.IGICsource.to_list

```{autodoc2-docstring} altdss.GICsource.IGICsource.to_list
```

````

`````
