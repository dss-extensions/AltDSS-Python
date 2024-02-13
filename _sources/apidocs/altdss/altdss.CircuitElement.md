# {py:mod}`altdss.CircuitElement`

```{py:module} altdss.CircuitElement
```

```{autodoc2-docstring} altdss.CircuitElement
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CircuitElementBatch <altdss.CircuitElement.CircuitElementBatch>`
  - ```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch
    :summary:
    ```
* - {py:obj}`CircuitElementBatchMixin <altdss.CircuitElement.CircuitElementBatchMixin>`
  - ```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin
    :summary:
    ```
* - {py:obj}`CircuitElementMixin <altdss.CircuitElement.CircuitElementMixin>`
  - ```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin
    :summary:
    ```
* - {py:obj}`ElementHasRegistersMixin <altdss.CircuitElement.ElementHasRegistersMixin>`
  - ```{autodoc2-docstring} altdss.CircuitElement.ElementHasRegistersMixin
    :summary:
    ```
````

### API

`````{py:class} CircuitElementBatch(func, parent, sync_cls_idx=ExtraClassIDs.CktElements)
:canonical: altdss.CircuitElement.CircuitElementBatch

Bases: {py:obj}`altdss.Batch.NonUniformBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch
```

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatch.Currents

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.CurrentsMagAng
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.CircuitElement.CircuitElementBatch.FullName

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.CircuitElement.CircuitElementBatch.GUID

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatch.Handle

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.CircuitElement.CircuitElementBatch.HasOCPDevice

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.CircuitElement.CircuitElementBatch.HasSwitchControl

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.CircuitElement.CircuitElementBatch.HasVoltControl

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.CircuitElement.CircuitElementBatch.IsIsolated

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.IsIsolated
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatch.Losses

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.CircuitElement.CircuitElementBatch.MaxCurrent

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.CircuitElement.CircuitElementBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatch.NumConductors

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatch.NumControllers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatch.NumPhases

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatch.NumTerminals

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.CircuitElement.CircuitElementBatch.OCPDevice

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.CircuitElement.CircuitElementBatch.OCPDeviceType

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatch.PhaseLosses

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatch.Powers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementBatch.SeqCurrents

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatch.SeqPowers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementBatch.SeqVoltages

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatch.TotalPowers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatch.Voltages

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.CircuitElement.CircuitElementBatch.__call__

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.__call__
```

````

````{py:method} __init__(func, parent, sync_cls_idx=ExtraClassIDs.CktElements)
:canonical: altdss.CircuitElement.CircuitElementBatch.__init__

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[altdss.DSSObj.DSSObj]
:canonical: altdss.CircuitElement.CircuitElementBatch.__iter__

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.CircuitElement.CircuitElementBatch.__len__

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.__len__
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.CircuitElement.CircuitElementBatch.to_json

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.CircuitElement.CircuitElementBatch.to_list

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatch.to_list
```

````

`````

`````{py:class} CircuitElementBatchMixin
:canonical: altdss.CircuitElement.CircuitElementBatchMixin

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin
```

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.ComplexSeqCurrents

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.ComplexSeqVoltages

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.Currents

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.CurrentsMagAng

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.CurrentsMagAng
```

````

````{py:method} GUID() -> str
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.GUID

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.Handle

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.HasOCPDevice

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.HasSwitchControl

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.HasVoltControl

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.IsIsolated

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.IsIsolated
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.Losses

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.MaxCurrent

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.MaxCurrent
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.NumConductors

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.NumControllers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.NumPhases

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.NumTerminals

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.OCPDevice

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.OCPDeviceIndex

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.OCPDeviceType

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.PhaseLosses

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.Powers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.SeqCurrents

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.SeqPowers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.SeqVoltages

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.TotalPowers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.Voltages

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementBatchMixin.VoltagesMagAng

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementBatchMixin.VoltagesMagAng
```

````

`````

`````{py:class} CircuitElementMixin(*args)
:canonical: altdss.CircuitElement.CircuitElementMixin

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin
```

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.CircuitElement.CircuitElementMixin.Close

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementMixin.ComplexSeqCurrents

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementMixin.ComplexSeqVoltages

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementMixin.Currents

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.CircuitElement.CircuitElementMixin.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.DisplayName
```

````

````{py:method} GUID() -> str
:canonical: altdss.CircuitElement.CircuitElementMixin.GUID

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.CircuitElement.CircuitElementMixin.Handle

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.CircuitElement.CircuitElementMixin.HasOCPDevice

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.CircuitElement.CircuitElementMixin.HasSwitchControl

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.CircuitElement.CircuitElementMixin.HasVoltControl

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.CircuitElement.CircuitElementMixin.IsIsolated

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.CircuitElement.CircuitElementMixin.IsOpen

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.IsOpen
```

````

````{py:method} Losses() -> complex
:canonical: altdss.CircuitElement.CircuitElementMixin.Losses

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.CircuitElement.CircuitElementMixin.MaxCurrent

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.MaxCurrent
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementMixin.NodeOrder

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.CircuitElement.CircuitElementMixin.NodeRef

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.CircuitElement.CircuitElementMixin.NumConductors

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.CircuitElement.CircuitElementMixin.NumControllers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.CircuitElement.CircuitElementMixin.NumPhases

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.CircuitElement.CircuitElementMixin.NumTerminals

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.CircuitElement.CircuitElementMixin.OCPDevice

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.CircuitElement.CircuitElementMixin.OCPDeviceIndex

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.CircuitElement.CircuitElementMixin.OCPDeviceType

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.CircuitElement.CircuitElementMixin.Open

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementMixin.PhaseLosses

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementMixin.Powers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.Powers
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementMixin.Residuals

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementMixin.SeqCurrents

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementMixin.SeqPowers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementMixin.SeqVoltages

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementMixin.TotalPowers

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementMixin.Voltages

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.CircuitElementMixin.VoltagesMagAng

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.CircuitElement.CircuitElementMixin.YPrim

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.YPrim
```

````

````{py:method} __init__(*args)
:canonical: altdss.CircuitElement.CircuitElementMixin.__init__

```{autodoc2-docstring} altdss.CircuitElement.CircuitElementMixin.__init__
```

````

`````

`````{py:class} ElementHasRegistersMixin
:canonical: altdss.CircuitElement.ElementHasRegistersMixin

```{autodoc2-docstring} altdss.CircuitElement.ElementHasRegistersMixin
```

````{py:method} RegisterNames() -> typing.List[str]
:canonical: altdss.CircuitElement.ElementHasRegistersMixin.RegisterNames

```{autodoc2-docstring} altdss.CircuitElement.ElementHasRegistersMixin.RegisterNames
```

````

````{py:method} RegisterValues() -> altdss.types.Float64Array
:canonical: altdss.CircuitElement.ElementHasRegistersMixin.RegisterValues

```{autodoc2-docstring} altdss.CircuitElement.ElementHasRegistersMixin.RegisterValues
```

````

````{py:method} RegistersDict() -> typing.Dict[str, float]
:canonical: altdss.CircuitElement.ElementHasRegistersMixin.RegistersDict

```{autodoc2-docstring} altdss.CircuitElement.ElementHasRegistersMixin.RegistersDict
```

````

`````
