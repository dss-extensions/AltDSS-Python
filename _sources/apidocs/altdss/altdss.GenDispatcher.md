# {py:mod}`altdss.GenDispatcher`

```{py:module} altdss.GenDispatcher
```

```{autodoc2-docstring} altdss.GenDispatcher
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GenDispatcher <altdss.GenDispatcher.GenDispatcher>`
  - ```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher
    :summary:
    ```
* - {py:obj}`GenDispatcherBatch <altdss.GenDispatcher.GenDispatcherBatch>`
  - ```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch
    :summary:
    ```
* - {py:obj}`GenDispatcherBatchProperties <altdss.GenDispatcher.GenDispatcherBatchProperties>`
  - ```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties
    :summary:
    ```
* - {py:obj}`GenDispatcherProperties <altdss.GenDispatcher.GenDispatcherProperties>`
  - ```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties
    :summary:
    ```
* - {py:obj}`IGenDispatcher <altdss.GenDispatcher.IGenDispatcher>`
  - ```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher
    :summary:
    ```
````

### API

`````{py:class} GenDispatcher(api_util, ptr)
:canonical: altdss.GenDispatcher.GenDispatcher

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher
```

````{py:attribute} BaseFreq
:canonical: altdss.GenDispatcher.GenDispatcher.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.GenDispatcher.GenDispatcher.Close

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcher.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcher.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcher.Currents

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.GenDispatcher.GenDispatcher.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.DisplayName
```

````

````{py:attribute} Element
:canonical: altdss.GenDispatcher.GenDispatcher.Element
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.GenDispatcher.GenDispatcher.Element_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.GenDispatcher.GenDispatcher.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Enabled
```

````

````{py:method} FullName() -> str
:canonical: altdss.GenDispatcher.GenDispatcher.FullName

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GenDispatcher.GenDispatcher.GUID

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.GUID
```

````

````{py:attribute} GenList
:canonical: altdss.GenDispatcher.GenDispatcher.GenList
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.GenList
```

````

````{py:method} Handle() -> int
:canonical: altdss.GenDispatcher.GenDispatcher.Handle

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GenDispatcher.GenDispatcher.HasOCPDevice

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GenDispatcher.GenDispatcher.HasSwitchControl

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GenDispatcher.GenDispatcher.HasVoltControl

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.GenDispatcher.GenDispatcher.IsIsolated

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.GenDispatcher.GenDispatcher.IsOpen

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.GenDispatcher.GenDispatcher.Like

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.GenDispatcher.GenDispatcher.Losses

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GenDispatcher.GenDispatcher.MaxCurrent

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GenDispatcher.GenDispatcher.Name
:type: str

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.GenDispatcher.NodeOrder

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.GenDispatcher.NodeRef

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.GenDispatcher.GenDispatcher.NumConductors

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.GenDispatcher.GenDispatcher.NumControllers

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.GenDispatcher.GenDispatcher.NumPhases

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.GenDispatcher.GenDispatcher.NumTerminals

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.GenDispatcher.GenDispatcher.OCPDevice

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.GenDispatcher.GenDispatcher.OCPDeviceIndex

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GenDispatcher.GenDispatcher.OCPDeviceType

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.GenDispatcher.GenDispatcher.Open

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcher.PhaseLosses

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcher.Powers

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Powers
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.GenDispatcher.Residuals

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.GenDispatcher.SeqCurrents

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcher.SeqPowers

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.GenDispatcher.SeqVoltages

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.SeqVoltages
```

````

````{py:attribute} Terminal
:canonical: altdss.GenDispatcher.GenDispatcher.Terminal
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcher.TotalPowers

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcher.Voltages

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.GenDispatcher.VoltagesMagAng

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.VoltagesMagAng
```

````

````{py:attribute} Weights
:canonical: altdss.GenDispatcher.GenDispatcher.Weights
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.Weights
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcher.YPrim

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.GenDispatcher.GenDispatcher.__hash__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.GenDispatcher.GenDispatcher.__init__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.GenDispatcher.GenDispatcher.__ne__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.GenDispatcher.GenDispatcher.__repr__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GenDispatcher.GenDispatcher.begin_edit

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GenDispatcher.GenDispatcher.end_edit

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.end_edit
```

````

````{py:attribute} kWBand
:canonical: altdss.GenDispatcher.GenDispatcher.kWBand
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.kWBand
```

````

````{py:attribute} kWLimit
:canonical: altdss.GenDispatcher.GenDispatcher.kWLimit
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.kWLimit
```

````

````{py:attribute} kvarLimit
:canonical: altdss.GenDispatcher.GenDispatcher.kvarLimit
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.kvarLimit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GenDispatcher.GenDispatcher.to_json

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcher.to_json
```

````

`````

`````{py:class} GenDispatcherBatch(api_util, **kwargs)
:canonical: altdss.GenDispatcher.GenDispatcherBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.GenDispatcher.GenDispatcherBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Currents

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.CurrentsMagAng
```

````

````{py:attribute} Element
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GenDispatcher.GenDispatcherBatch.FullName

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.GenDispatcher.GenDispatcherBatch.GUID

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.GUID
```

````

````{py:attribute} GenList
:canonical: altdss.GenDispatcher.GenDispatcherBatch.GenList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.GenList
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Handle

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.HasOCPDevice

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.HasSwitchControl

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.HasVoltControl

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.IsIsolated

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Like

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Losses

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.MaxCurrent

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.NumConductors

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.NumControllers

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.NumPhases

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.NumTerminals

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.GenDispatcher.GenDispatcherBatch.OCPDevice

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.GenDispatcher.GenDispatcherBatch.OCPDeviceType

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.PhaseLosses

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Powers

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.SeqCurrents

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.SeqPowers

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.SeqVoltages

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.SeqVoltages
```

````

````{py:attribute} Terminal
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.TotalPowers

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Voltages

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.GenDispatcherBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.VoltagesMagAng
```

````

````{py:attribute} Weights
:canonical: altdss.GenDispatcher.GenDispatcherBatch.Weights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.Weights
```

````

````{py:method} __call__()
:canonical: altdss.GenDispatcher.GenDispatcherBatch.__call__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.GenDispatcher.GenDispatcherBatch.__getitem__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.GenDispatcher.GenDispatcherBatch.__init__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GenDispatcher.GenDispatcherBatch.__iter__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GenDispatcher.GenDispatcherBatch.__len__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.GenDispatcher.GenDispatcherBatch.batch

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GenDispatcher.GenDispatcherBatch.begin_edit

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GenDispatcher.GenDispatcherBatch.end_edit

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.end_edit
```

````

````{py:attribute} kWBand
:canonical: altdss.GenDispatcher.GenDispatcherBatch.kWBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.kWBand
```

````

````{py:attribute} kWLimit
:canonical: altdss.GenDispatcher.GenDispatcherBatch.kWLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.kWLimit
```

````

````{py:attribute} kvarLimit
:canonical: altdss.GenDispatcher.GenDispatcherBatch.kvarLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.kvarLimit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GenDispatcher.GenDispatcherBatch.to_json

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GenDispatcher.GenDispatcherBatch.to_list

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatch.to_list
```

````

`````

`````{py:class} GenDispatcherBatchProperties()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.BaseFreq
```

````

````{py:attribute} Element
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.Enabled
```

````

````{py:attribute} GenList
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.GenList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.GenList
```

````

````{py:attribute} Like
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.Like
```

````

````{py:attribute} Terminal
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.Terminal
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.Terminal
```

````

````{py:attribute} Weights
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.Weights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.Weights
```

````

````{py:method} __contains__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__contains__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__delattr__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__delitem__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__dir__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__format__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__ge__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__getitem__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__getstate__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__gt__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__init__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__ior__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__iter__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__le__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__len__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__lt__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__ne__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__new__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__or__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__reduce__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__repr__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__reversed__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__ror__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__setitem__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__str__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.clear

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.copy

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.get

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.items

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.items
```

````

````{py:attribute} kWBand
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.kWBand
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.kWBand
```

````

````{py:attribute} kWLimit
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.kWLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.kWLimit
```

````

````{py:method} keys()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.keys

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.keys
```

````

````{py:attribute} kvarLimit
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.kvarLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.kvarLimit
```

````

````{py:method} pop()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.pop

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.popitem

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.setdefault

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.update

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.GenDispatcher.GenDispatcherBatchProperties.values

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherBatchProperties.values
```

````

`````

`````{py:class} GenDispatcherProperties()
:canonical: altdss.GenDispatcher.GenDispatcherProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.GenDispatcher.GenDispatcherProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.BaseFreq
```

````

````{py:attribute} Element
:canonical: altdss.GenDispatcher.GenDispatcherProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.GenDispatcher.GenDispatcherProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.Enabled
```

````

````{py:attribute} GenList
:canonical: altdss.GenDispatcher.GenDispatcherProperties.GenList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.GenList
```

````

````{py:attribute} Like
:canonical: altdss.GenDispatcher.GenDispatcherProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.Like
```

````

````{py:attribute} Terminal
:canonical: altdss.GenDispatcher.GenDispatcherProperties.Terminal
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.Terminal
```

````

````{py:attribute} Weights
:canonical: altdss.GenDispatcher.GenDispatcherProperties.Weights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.Weights
```

````

````{py:method} __contains__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__contains__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__delattr__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__delitem__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__dir__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__format__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__ge__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__getattribute__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__getitem__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__getstate__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__gt__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__init__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__ior__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__iter__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__le__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__len__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__lt__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__ne__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__new__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__or__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__reduce__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__repr__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__reversed__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__ror__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__setitem__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__sizeof__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__str__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.__subclasshook__

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.clear

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.copy

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.get

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.get
```

````

````{py:method} items()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.items

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.items
```

````

````{py:attribute} kWBand
:canonical: altdss.GenDispatcher.GenDispatcherProperties.kWBand
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.kWBand
```

````

````{py:attribute} kWLimit
:canonical: altdss.GenDispatcher.GenDispatcherProperties.kWLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.kWLimit
```

````

````{py:method} keys()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.keys

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.keys
```

````

````{py:attribute} kvarLimit
:canonical: altdss.GenDispatcher.GenDispatcherProperties.kvarLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.kvarLimit
```

````

````{py:method} pop()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.pop

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.popitem

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.setdefault

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.update

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.update
```

````

````{py:method} values()
:canonical: altdss.GenDispatcher.GenDispatcherProperties.values

```{autodoc2-docstring} altdss.GenDispatcher.GenDispatcherProperties.values
```

````

`````

`````{py:class} IGenDispatcher(iobj)
:canonical: altdss.GenDispatcher.IGenDispatcher

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.GenDispatcher.GenDispatcherBatch`

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher
```

````{py:attribute} BaseFreq
:canonical: altdss.GenDispatcher.IGenDispatcher.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.IGenDispatcher.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.IGenDispatcher.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.IGenDispatcher.Currents

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.IGenDispatcher.CurrentsMagAng

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.CurrentsMagAng
```

````

````{py:attribute} Element
:canonical: altdss.GenDispatcher.IGenDispatcher.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.GenDispatcher.IGenDispatcher.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.GenDispatcher.IGenDispatcher.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GenDispatcher.IGenDispatcher.FullName

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.GenDispatcher.IGenDispatcher.GUID

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.GUID
```

````

````{py:attribute} GenList
:canonical: altdss.GenDispatcher.IGenDispatcher.GenList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.GenList
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.IGenDispatcher.Handle

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.GenDispatcher.IGenDispatcher.HasOCPDevice

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.GenDispatcher.IGenDispatcher.HasSwitchControl

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.GenDispatcher.IGenDispatcher.HasVoltControl

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.GenDispatcher.IGenDispatcher.IsIsolated

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GenDispatcher.IGenDispatcher.Like

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.IGenDispatcher.Losses

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.IGenDispatcher.MaxCurrent

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GenDispatcher.IGenDispatcher.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.IGenDispatcher.NumConductors

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.IGenDispatcher.NumControllers

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.IGenDispatcher.NumPhases

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.IGenDispatcher.NumTerminals

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.GenDispatcher.IGenDispatcher.OCPDevice

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.GenDispatcher.IGenDispatcher.OCPDeviceIndex

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.GenDispatcher.IGenDispatcher.OCPDeviceType

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.IGenDispatcher.PhaseLosses

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.IGenDispatcher.Powers

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.IGenDispatcher.SeqCurrents

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.IGenDispatcher.SeqPowers

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.IGenDispatcher.SeqVoltages

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.SeqVoltages
```

````

````{py:attribute} Terminal
:canonical: altdss.GenDispatcher.IGenDispatcher.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.IGenDispatcher.TotalPowers

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GenDispatcher.IGenDispatcher.Voltages

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GenDispatcher.IGenDispatcher.VoltagesMagAng

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.VoltagesMagAng
```

````

````{py:attribute} Weights
:canonical: altdss.GenDispatcher.IGenDispatcher.Weights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.Weights
```

````

````{py:method} __call__()
:canonical: altdss.GenDispatcher.IGenDispatcher.__call__

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.GenDispatcher.IGenDispatcher.__contains__

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.GenDispatcher.IGenDispatcher.__getitem__

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.GenDispatcher.IGenDispatcher.__init__

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GenDispatcher.IGenDispatcher.__iter__

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GenDispatcher.IGenDispatcher.__len__

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.GenDispatcher.IGenDispatcher.batch

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.GenDispatcher.GenDispatcherBatchProperties]) -> altdss.GenDispatcher.GenDispatcherBatch
:canonical: altdss.GenDispatcher.IGenDispatcher.batch_new

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GenDispatcher.IGenDispatcher.begin_edit

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GenDispatcher.IGenDispatcher.end_edit

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.GenDispatcher.IGenDispatcher.find

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.find
```

````

````{py:attribute} kWBand
:canonical: altdss.GenDispatcher.IGenDispatcher.kWBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.kWBand
```

````

````{py:attribute} kWLimit
:canonical: altdss.GenDispatcher.IGenDispatcher.kWLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.kWLimit
```

````

````{py:attribute} kvarLimit
:canonical: altdss.GenDispatcher.IGenDispatcher.kvarLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.kvarLimit
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.GenDispatcher.GenDispatcherProperties]) -> altdss.GenDispatcher.GenDispatcher
:canonical: altdss.GenDispatcher.IGenDispatcher.new

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GenDispatcher.IGenDispatcher.to_json

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GenDispatcher.IGenDispatcher.to_list

```{autodoc2-docstring} altdss.GenDispatcher.IGenDispatcher.to_list
```

````

`````
