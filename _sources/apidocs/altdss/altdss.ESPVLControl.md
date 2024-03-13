# {py:mod}`altdss.ESPVLControl`

```{py:module} altdss.ESPVLControl
```

```{autodoc2-docstring} altdss.ESPVLControl
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ESPVLControl <altdss.ESPVLControl.ESPVLControl>`
  - ```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl
    :summary:
    ```
* - {py:obj}`ESPVLControlBatch <altdss.ESPVLControl.ESPVLControlBatch>`
  - ```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch
    :summary:
    ```
* - {py:obj}`ESPVLControlBatchProperties <altdss.ESPVLControl.ESPVLControlBatchProperties>`
  - ```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties
    :summary:
    ```
* - {py:obj}`ESPVLControlProperties <altdss.ESPVLControl.ESPVLControlProperties>`
  - ```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties
    :summary:
    ```
* - {py:obj}`IESPVLControl <altdss.ESPVLControl.IESPVLControl>`
  - ```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl
    :summary:
    ```
````

### API

`````{py:class} ESPVLControl(api_util, ptr)
:canonical: altdss.ESPVLControl.ESPVLControl

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl
```

````{py:attribute} BaseFreq
:canonical: altdss.ESPVLControl.ESPVLControl.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.ESPVLControl.ESPVLControl.Close

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControl.Currents

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.ESPVLControl.ESPVLControl.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.DisplayName
```

````

````{py:attribute} Element
:canonical: altdss.ESPVLControl.ESPVLControl.Element
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.ESPVLControl.ESPVLControl.Element_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.ESPVLControl.ESPVLControl.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Enabled
```

````

````{py:method} FullName() -> str
:canonical: altdss.ESPVLControl.ESPVLControl.FullName

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.ESPVLControl.ESPVLControl.GUID

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.ESPVLControl.ESPVLControl.Handle

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.ESPVLControl.ESPVLControl.HasOCPDevice

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.ESPVLControl.ESPVLControl.HasSwitchControl

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.ESPVLControl.ESPVLControl.HasVoltControl

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.ESPVLControl.ESPVLControl.IsIsolated

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.ESPVLControl.ESPVLControl.IsOpen

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.ESPVLControl.ESPVLControl.Like

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Like
```

````

````{py:attribute} LocalControlList
:canonical: altdss.ESPVLControl.ESPVLControl.LocalControlList
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.LocalControlList
```

````

````{py:attribute} LocalControlWeights
:canonical: altdss.ESPVLControl.ESPVLControl.LocalControlWeights
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.LocalControlWeights
```

````

````{py:method} Losses() -> complex
:canonical: altdss.ESPVLControl.ESPVLControl.Losses

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.ESPVLControl.ESPVLControl.MaxCurrent

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.ESPVLControl.ESPVLControl.Name
:type: str

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.ESPVLControl.NodeOrder

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.ESPVLControl.NodeRef

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.ESPVLControl.ESPVLControl.NumConductors

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.ESPVLControl.ESPVLControl.NumControllers

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.ESPVLControl.ESPVLControl.NumPhases

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.ESPVLControl.ESPVLControl.NumTerminals

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.ESPVLControl.ESPVLControl.OCPDevice

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.ESPVLControl.ESPVLControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.ESPVLControl.ESPVLControl.OCPDeviceType

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.ESPVLControl.ESPVLControl.Open

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Open
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ESPVLControl.ESPVLControl.PVSystemList
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.PVSystemList
```

````

````{py:attribute} PVSystemWeights
:canonical: altdss.ESPVLControl.ESPVLControl.PVSystemWeights
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.PVSystemWeights
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControl.PhaseLosses

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControl.Powers

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Powers
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.ESPVLControl.Residuals

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.ESPVLControl.SeqCurrents

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControl.SeqPowers

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.ESPVLControl.SeqVoltages

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.SeqVoltages
```

````

````{py:attribute} StorageList
:canonical: altdss.ESPVLControl.ESPVLControl.StorageList
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.StorageList
```

````

````{py:attribute} StorageWeights
:canonical: altdss.ESPVLControl.ESPVLControl.StorageWeights
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.StorageWeights
```

````

````{py:attribute} Terminal
:canonical: altdss.ESPVLControl.ESPVLControl.Terminal
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControl.TotalPowers

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.ESPVLControl.ESPVLControl.Type
:type: altdss.enums.ESPVLControlType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.ESPVLControl.ESPVLControl.Type_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Type_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControl.Voltages

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.ESPVLControl.VoltagesMagAng

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControl.YPrim

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.ESPVLControl.ESPVLControl.__hash__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.ESPVLControl.ESPVLControl.__init__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.ESPVLControl.ESPVLControl.__ne__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.ESPVLControl.ESPVLControl.__repr__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.ESPVLControl.ESPVLControl.begin_edit

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.ESPVLControl.ESPVLControl.end_edit

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.end_edit
```

````

````{py:attribute} kWBand
:canonical: altdss.ESPVLControl.ESPVLControl.kWBand
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.kWBand
```

````

````{py:attribute} kvarLimit
:canonical: altdss.ESPVLControl.ESPVLControl.kvarLimit
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.kvarLimit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.ESPVLControl.ESPVLControl.to_json

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControl.to_json
```

````

`````

`````{py:class} ESPVLControlBatch(api_util, **kwargs)
:canonical: altdss.ESPVLControl.ESPVLControlBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.ESPVLControl.ESPVLControlBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Currents

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.CurrentsMagAng
```

````

````{py:attribute} Element
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.ESPVLControl.ESPVLControlBatch.FullName

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.ESPVLControl.ESPVLControlBatch.GUID

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Handle

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.HasOCPDevice

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.HasSwitchControl

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.HasVoltControl

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.IsIsolated

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Like

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Like
```

````

````{py:attribute} LocalControlList
:canonical: altdss.ESPVLControl.ESPVLControlBatch.LocalControlList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.LocalControlList
```

````

````{py:attribute} LocalControlWeights
:canonical: altdss.ESPVLControl.ESPVLControlBatch.LocalControlWeights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.LocalControlWeights
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Losses

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.MaxCurrent

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.NumConductors

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.NumControllers

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.NumPhases

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.NumTerminals

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.ESPVLControl.ESPVLControlBatch.OCPDevice

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.ESPVLControl.ESPVLControlBatch.OCPDeviceType

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.OCPDeviceType
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ESPVLControl.ESPVLControlBatch.PVSystemList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.PVSystemList
```

````

````{py:attribute} PVSystemWeights
:canonical: altdss.ESPVLControl.ESPVLControlBatch.PVSystemWeights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.PVSystemWeights
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.PhaseLosses

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Powers

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.SeqCurrents

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.SeqPowers

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.SeqVoltages

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.SeqVoltages
```

````

````{py:attribute} StorageList
:canonical: altdss.ESPVLControl.ESPVLControlBatch.StorageList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.StorageList
```

````

````{py:attribute} StorageWeights
:canonical: altdss.ESPVLControl.ESPVLControlBatch.StorageWeights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.StorageWeights
```

````

````{py:attribute} Terminal
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.TotalPowers

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Type
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Type_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Type_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.ESPVLControlBatch.Voltages

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.ESPVLControlBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.ESPVLControl.ESPVLControlBatch.__call__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.ESPVLControl.ESPVLControlBatch.__getitem__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.ESPVLControl.ESPVLControlBatch.__init__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.ESPVLControl.ESPVLControlBatch.__iter__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.ESPVLControl.ESPVLControlBatch.__len__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.ESPVLControl.ESPVLControlBatch.batch

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.ESPVLControl.ESPVLControlBatch.begin_edit

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.ESPVLControl.ESPVLControlBatch.end_edit

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.end_edit
```

````

````{py:attribute} kWBand
:canonical: altdss.ESPVLControl.ESPVLControlBatch.kWBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.kWBand
```

````

````{py:attribute} kvarLimit
:canonical: altdss.ESPVLControl.ESPVLControlBatch.kvarLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.kvarLimit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.ESPVLControl.ESPVLControlBatch.to_json

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.ESPVLControl.ESPVLControlBatch.to_list

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatch.to_list
```

````

`````

`````{py:class} ESPVLControlBatchProperties()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.BaseFreq
```

````

````{py:attribute} Element
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.Like
```

````

````{py:attribute} LocalControlList
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.LocalControlList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.LocalControlList
```

````

````{py:attribute} LocalControlWeights
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.LocalControlWeights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.LocalControlWeights
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.PVSystemList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.PVSystemList
```

````

````{py:attribute} PVSystemWeights
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.PVSystemWeights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.PVSystemWeights
```

````

````{py:attribute} StorageList
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.StorageList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.StorageList
```

````

````{py:attribute} StorageWeights
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.StorageWeights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.StorageWeights
```

````

````{py:attribute} Terminal
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.Terminal
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.Terminal
```

````

````{py:attribute} Type
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.Type
:type: typing.Union[typing.AnyStr, int, altdss.enums.ESPVLControlType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.ESPVLControlType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.Type
```

````

````{py:method} __contains__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__contains__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__delattr__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__delitem__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__dir__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__format__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__ge__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__getitem__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__getstate__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__gt__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__init__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__ior__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__iter__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__le__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__len__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__lt__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__ne__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__new__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__or__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__reduce__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__repr__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__reversed__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__ror__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__setitem__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__str__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.clear

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.copy

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.get

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.items

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.items
```

````

````{py:attribute} kWBand
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.kWBand
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.kWBand
```

````

````{py:method} keys()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.keys

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.keys
```

````

````{py:attribute} kvarLimit
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.kvarLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.kvarLimit
```

````

````{py:method} pop()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.pop

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.popitem

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.setdefault

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.update

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.ESPVLControl.ESPVLControlBatchProperties.values

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlBatchProperties.values
```

````

`````

`````{py:class} ESPVLControlProperties()
:canonical: altdss.ESPVLControl.ESPVLControlProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.ESPVLControl.ESPVLControlProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.BaseFreq
```

````

````{py:attribute} Element
:canonical: altdss.ESPVLControl.ESPVLControlProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.ESPVLControl.ESPVLControlProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.ESPVLControl.ESPVLControlProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.Like
```

````

````{py:attribute} LocalControlList
:canonical: altdss.ESPVLControl.ESPVLControlProperties.LocalControlList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.LocalControlList
```

````

````{py:attribute} LocalControlWeights
:canonical: altdss.ESPVLControl.ESPVLControlProperties.LocalControlWeights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.LocalControlWeights
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ESPVLControl.ESPVLControlProperties.PVSystemList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.PVSystemList
```

````

````{py:attribute} PVSystemWeights
:canonical: altdss.ESPVLControl.ESPVLControlProperties.PVSystemWeights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.PVSystemWeights
```

````

````{py:attribute} StorageList
:canonical: altdss.ESPVLControl.ESPVLControlProperties.StorageList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.StorageList
```

````

````{py:attribute} StorageWeights
:canonical: altdss.ESPVLControl.ESPVLControlProperties.StorageWeights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.StorageWeights
```

````

````{py:attribute} Terminal
:canonical: altdss.ESPVLControl.ESPVLControlProperties.Terminal
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.Terminal
```

````

````{py:attribute} Type
:canonical: altdss.ESPVLControl.ESPVLControlProperties.Type
:type: typing.Union[typing.AnyStr, int, altdss.enums.ESPVLControlType]
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.Type
```

````

````{py:method} __contains__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__contains__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__delattr__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__delitem__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__dir__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__format__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__ge__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__getattribute__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__getitem__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__getstate__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__gt__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__init__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__ior__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__iter__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__le__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__len__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__lt__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__ne__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__new__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__or__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__reduce__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__reduce_ex__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__repr__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__reversed__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__ror__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__setitem__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__sizeof__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__str__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.__subclasshook__

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.clear

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.copy

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.copy
```

````

````{py:method} get()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.get

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.get
```

````

````{py:method} items()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.items

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.items
```

````

````{py:attribute} kWBand
:canonical: altdss.ESPVLControl.ESPVLControlProperties.kWBand
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.kWBand
```

````

````{py:method} keys()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.keys

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.keys
```

````

````{py:attribute} kvarLimit
:canonical: altdss.ESPVLControl.ESPVLControlProperties.kvarLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.kvarLimit
```

````

````{py:method} pop()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.pop

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.popitem

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.setdefault

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.update

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.update
```

````

````{py:method} values()
:canonical: altdss.ESPVLControl.ESPVLControlProperties.values

```{autodoc2-docstring} altdss.ESPVLControl.ESPVLControlProperties.values
```

````

`````

`````{py:class} IESPVLControl(iobj)
:canonical: altdss.ESPVLControl.IESPVLControl

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.ESPVLControl.ESPVLControlBatch`

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl
```

````{py:attribute} BaseFreq
:canonical: altdss.ESPVLControl.IESPVLControl.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.IESPVLControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.IESPVLControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.IESPVLControl.Currents

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.IESPVLControl.CurrentsMagAng

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.CurrentsMagAng
```

````

````{py:attribute} Element
:canonical: altdss.ESPVLControl.IESPVLControl.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.ESPVLControl.IESPVLControl.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.ESPVLControl.IESPVLControl.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.ESPVLControl.IESPVLControl.FullName

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.ESPVLControl.IESPVLControl.GUID

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.IESPVLControl.Handle

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.ESPVLControl.IESPVLControl.HasOCPDevice

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.ESPVLControl.IESPVLControl.HasSwitchControl

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.ESPVLControl.IESPVLControl.HasVoltControl

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.ESPVLControl.IESPVLControl.IsIsolated

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.ESPVLControl.IESPVLControl.Like

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Like
```

````

````{py:attribute} LocalControlList
:canonical: altdss.ESPVLControl.IESPVLControl.LocalControlList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.LocalControlList
```

````

````{py:attribute} LocalControlWeights
:canonical: altdss.ESPVLControl.IESPVLControl.LocalControlWeights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.LocalControlWeights
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.IESPVLControl.Losses

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.IESPVLControl.MaxCurrent

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.ESPVLControl.IESPVLControl.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.IESPVLControl.NumConductors

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.IESPVLControl.NumControllers

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.IESPVLControl.NumPhases

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.IESPVLControl.NumTerminals

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.ESPVLControl.IESPVLControl.OCPDevice

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.ESPVLControl.IESPVLControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.ESPVLControl.IESPVLControl.OCPDeviceType

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.OCPDeviceType
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ESPVLControl.IESPVLControl.PVSystemList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.PVSystemList
```

````

````{py:attribute} PVSystemWeights
:canonical: altdss.ESPVLControl.IESPVLControl.PVSystemWeights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.PVSystemWeights
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.IESPVLControl.PhaseLosses

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.IESPVLControl.Powers

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.IESPVLControl.SeqCurrents

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.IESPVLControl.SeqPowers

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.IESPVLControl.SeqVoltages

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.SeqVoltages
```

````

````{py:attribute} StorageList
:canonical: altdss.ESPVLControl.IESPVLControl.StorageList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.StorageList
```

````

````{py:attribute} StorageWeights
:canonical: altdss.ESPVLControl.IESPVLControl.StorageWeights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.StorageWeights
```

````

````{py:attribute} Terminal
:canonical: altdss.ESPVLControl.IESPVLControl.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.IESPVLControl.TotalPowers

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.ESPVLControl.IESPVLControl.Type
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.ESPVLControl.IESPVLControl.Type_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Type_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.ESPVLControl.IESPVLControl.Voltages

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.ESPVLControl.IESPVLControl.VoltagesMagAng

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.ESPVLControl.IESPVLControl.__call__

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.ESPVLControl.IESPVLControl.__contains__

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.ESPVLControl.IESPVLControl.__getitem__

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.ESPVLControl.IESPVLControl.__init__

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.ESPVLControl.IESPVLControl.__iter__

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.ESPVLControl.IESPVLControl.__len__

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.ESPVLControl.IESPVLControl.batch

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.ESPVLControl.ESPVLControlBatchProperties]) -> altdss.ESPVLControl.ESPVLControlBatch
:canonical: altdss.ESPVLControl.IESPVLControl.batch_new

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.ESPVLControl.IESPVLControl.begin_edit

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.ESPVLControl.IESPVLControl.end_edit

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.ESPVLControl.IESPVLControl.find

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.find
```

````

````{py:attribute} kWBand
:canonical: altdss.ESPVLControl.IESPVLControl.kWBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.kWBand
```

````

````{py:attribute} kvarLimit
:canonical: altdss.ESPVLControl.IESPVLControl.kvarLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.kvarLimit
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.ESPVLControl.ESPVLControlProperties]) -> altdss.ESPVLControl.ESPVLControl
:canonical: altdss.ESPVLControl.IESPVLControl.new

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.ESPVLControl.IESPVLControl.to_json

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.to_json
```

````

````{py:method} to_list()
:canonical: altdss.ESPVLControl.IESPVLControl.to_list

```{autodoc2-docstring} altdss.ESPVLControl.IESPVLControl.to_list
```

````

`````
