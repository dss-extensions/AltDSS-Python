# {py:mod}`altdss.Fuse`

```{py:module} altdss.Fuse
```

```{autodoc2-docstring} altdss.Fuse
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Fuse <altdss.Fuse.Fuse>`
  - ```{autodoc2-docstring} altdss.Fuse.Fuse
    :summary:
    ```
* - {py:obj}`FuseBatch <altdss.Fuse.FuseBatch>`
  - ```{autodoc2-docstring} altdss.Fuse.FuseBatch
    :summary:
    ```
* - {py:obj}`FuseBatchProperties <altdss.Fuse.FuseBatchProperties>`
  - ```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties
    :summary:
    ```
* - {py:obj}`FuseProperties <altdss.Fuse.FuseProperties>`
  - ```{autodoc2-docstring} altdss.Fuse.FuseProperties
    :summary:
    ```
* - {py:obj}`IFuse <altdss.Fuse.IFuse>`
  - ```{autodoc2-docstring} altdss.Fuse.IFuse
    :summary:
    ```
````

### API

`````{py:class} Fuse(api_util, ptr)
:canonical: altdss.Fuse.Fuse

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.Fuse.Fuse
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.FuseAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.Fuse.Action

```{autodoc2-docstring} altdss.Fuse.Fuse.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Fuse.Fuse.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Fuse.Fuse.Close

```{autodoc2-docstring} altdss.Fuse.Fuse.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.Fuse.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Fuse.Fuse.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.Fuse.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Fuse.Fuse.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.Fuse.Currents

```{autodoc2-docstring} altdss.Fuse.Fuse.Currents
```

````

````{py:attribute} Delay
:canonical: altdss.Fuse.Fuse.Delay
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.Delay
```

````

````{py:attribute} DisplayName
:canonical: altdss.Fuse.Fuse.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.DisplayName
```

````

````{py:attribute} Enabled
:canonical: altdss.Fuse.Fuse.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.Enabled
```

````

````{py:method} FullName() -> str
:canonical: altdss.Fuse.Fuse.FullName

```{autodoc2-docstring} altdss.Fuse.Fuse.FullName
```

````

````{py:attribute} FuseCurve
:canonical: altdss.Fuse.Fuse.FuseCurve
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.FuseCurve
```

````

````{py:attribute} FuseCurve_str
:canonical: altdss.Fuse.Fuse.FuseCurve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.FuseCurve_str
```

````

````{py:method} GUID() -> str
:canonical: altdss.Fuse.Fuse.GUID

```{autodoc2-docstring} altdss.Fuse.Fuse.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.Fuse.Fuse.Handle

```{autodoc2-docstring} altdss.Fuse.Fuse.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Fuse.Fuse.HasOCPDevice

```{autodoc2-docstring} altdss.Fuse.Fuse.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Fuse.Fuse.HasSwitchControl

```{autodoc2-docstring} altdss.Fuse.Fuse.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Fuse.Fuse.HasVoltControl

```{autodoc2-docstring} altdss.Fuse.Fuse.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Fuse.Fuse.IsIsolated

```{autodoc2-docstring} altdss.Fuse.Fuse.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Fuse.Fuse.IsOpen

```{autodoc2-docstring} altdss.Fuse.Fuse.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Fuse.Fuse.Like

```{autodoc2-docstring} altdss.Fuse.Fuse.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Fuse.Fuse.Losses

```{autodoc2-docstring} altdss.Fuse.Fuse.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Fuse.Fuse.MaxCurrent

```{autodoc2-docstring} altdss.Fuse.Fuse.MaxCurrent
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Fuse.Fuse.MonitoredObj
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.MonitoredObj
```

````

````{py:attribute} MonitoredObj_str
:canonical: altdss.Fuse.Fuse.MonitoredObj_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.MonitoredObj_str
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Fuse.Fuse.MonitoredTerm
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.MonitoredTerm
```

````

````{py:property} Name
:canonical: altdss.Fuse.Fuse.Name
:type: str

```{autodoc2-docstring} altdss.Fuse.Fuse.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Fuse.Fuse.NodeOrder

```{autodoc2-docstring} altdss.Fuse.Fuse.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Fuse.Fuse.NodeRef

```{autodoc2-docstring} altdss.Fuse.Fuse.NodeRef
```

````

````{py:attribute} Normal
:canonical: altdss.Fuse.Fuse.Normal
:type: altdss.enums.FuseState
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.Fuse.Fuse.Normal_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.Normal_str
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Fuse.Fuse.NumConductors

```{autodoc2-docstring} altdss.Fuse.Fuse.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Fuse.Fuse.NumControllers

```{autodoc2-docstring} altdss.Fuse.Fuse.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Fuse.Fuse.NumPhases

```{autodoc2-docstring} altdss.Fuse.Fuse.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Fuse.Fuse.NumTerminals

```{autodoc2-docstring} altdss.Fuse.Fuse.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Fuse.Fuse.OCPDevice

```{autodoc2-docstring} altdss.Fuse.Fuse.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Fuse.Fuse.OCPDeviceIndex

```{autodoc2-docstring} altdss.Fuse.Fuse.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Fuse.Fuse.OCPDeviceType

```{autodoc2-docstring} altdss.Fuse.Fuse.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Fuse.Fuse.Open

```{autodoc2-docstring} altdss.Fuse.Fuse.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.Fuse.PhaseLosses

```{autodoc2-docstring} altdss.Fuse.Fuse.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.Fuse.Powers

```{autodoc2-docstring} altdss.Fuse.Fuse.Powers
```

````

````{py:attribute} RatedCurrent
:canonical: altdss.Fuse.Fuse.RatedCurrent
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.RatedCurrent
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Fuse.Fuse.Residuals

```{autodoc2-docstring} altdss.Fuse.Fuse.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Fuse.Fuse.SeqCurrents

```{autodoc2-docstring} altdss.Fuse.Fuse.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.Fuse.SeqPowers

```{autodoc2-docstring} altdss.Fuse.Fuse.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Fuse.Fuse.SeqVoltages

```{autodoc2-docstring} altdss.Fuse.Fuse.SeqVoltages
```

````

````{py:attribute} State
:canonical: altdss.Fuse.Fuse.State
:type: altdss.enums.FuseState
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.State
```

````

````{py:attribute} State_str
:canonical: altdss.Fuse.Fuse.State_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Fuse.Fuse.SwitchedObj
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.Fuse.Fuse.SwitchedObj_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Fuse.Fuse.SwitchedTerm
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.Fuse.SwitchedTerm
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.Fuse.TotalPowers

```{autodoc2-docstring} altdss.Fuse.Fuse.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.Fuse.Voltages

```{autodoc2-docstring} altdss.Fuse.Fuse.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fuse.Fuse.VoltagesMagAng

```{autodoc2-docstring} altdss.Fuse.Fuse.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.Fuse.YPrim

```{autodoc2-docstring} altdss.Fuse.Fuse.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.Fuse.Fuse.__hash__

```{autodoc2-docstring} altdss.Fuse.Fuse.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Fuse.Fuse.__init__

```{autodoc2-docstring} altdss.Fuse.Fuse.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Fuse.Fuse.__ne__

```{autodoc2-docstring} altdss.Fuse.Fuse.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Fuse.Fuse.__repr__

```{autodoc2-docstring} altdss.Fuse.Fuse.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Fuse.Fuse.begin_edit

```{autodoc2-docstring} altdss.Fuse.Fuse.begin_edit
```

````

````{py:method} close(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.Fuse.close

```{autodoc2-docstring} altdss.Fuse.Fuse.close
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Fuse.Fuse.end_edit

```{autodoc2-docstring} altdss.Fuse.Fuse.end_edit
```

````

````{py:method} open(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.Fuse.open

```{autodoc2-docstring} altdss.Fuse.Fuse.open
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Fuse.Fuse.to_json

```{autodoc2-docstring} altdss.Fuse.Fuse.to_json
```

````

`````

`````{py:class} FuseBatch(api_util, **kwargs)
:canonical: altdss.Fuse.FuseBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.Fuse.FuseBatch
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.FuseAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.FuseBatch.Action

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Fuse.FuseBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.FuseBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Fuse.FuseBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.FuseBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Fuse.FuseBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.FuseBatch.Currents

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fuse.FuseBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Fuse.FuseBatch.CurrentsMagAng
```

````

````{py:attribute} Delay
:canonical: altdss.Fuse.FuseBatch.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.Fuse.FuseBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Fuse.FuseBatch.FullName

```{autodoc2-docstring} altdss.Fuse.FuseBatch.FullName
```

````

````{py:attribute} FuseCurve
:canonical: altdss.Fuse.FuseBatch.FuseCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.FuseCurve
```

````

````{py:attribute} FuseCurve_str
:canonical: altdss.Fuse.FuseBatch.FuseCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.FuseCurve_str
```

````

````{py:method} GUID() -> str
:canonical: altdss.Fuse.FuseBatch.GUID

```{autodoc2-docstring} altdss.Fuse.FuseBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Fuse.FuseBatch.Handle

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Fuse.FuseBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Fuse.FuseBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Fuse.FuseBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Fuse.FuseBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Fuse.FuseBatch.HasVoltControl

```{autodoc2-docstring} altdss.Fuse.FuseBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Fuse.FuseBatch.IsIsolated

```{autodoc2-docstring} altdss.Fuse.FuseBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.FuseBatch.Like

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.FuseBatch.Losses

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Fuse.FuseBatch.MaxCurrent

```{autodoc2-docstring} altdss.Fuse.FuseBatch.MaxCurrent
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Fuse.FuseBatch.MonitoredObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.MonitoredObj
```

````

````{py:attribute} MonitoredObj_str
:canonical: altdss.Fuse.FuseBatch.MonitoredObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.MonitoredObj_str
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Fuse.FuseBatch.MonitoredTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.MonitoredTerm
```

````

````{py:property} Name
:canonical: altdss.Fuse.FuseBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Name
```

````

````{py:attribute} Normal
:canonical: altdss.Fuse.FuseBatch.Normal
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.Fuse.FuseBatch.Normal_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Normal_str
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Fuse.FuseBatch.NumConductors

```{autodoc2-docstring} altdss.Fuse.FuseBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Fuse.FuseBatch.NumControllers

```{autodoc2-docstring} altdss.Fuse.FuseBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Fuse.FuseBatch.NumPhases

```{autodoc2-docstring} altdss.Fuse.FuseBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Fuse.FuseBatch.NumTerminals

```{autodoc2-docstring} altdss.Fuse.FuseBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Fuse.FuseBatch.OCPDevice

```{autodoc2-docstring} altdss.Fuse.FuseBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Fuse.FuseBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Fuse.FuseBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Fuse.FuseBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Fuse.FuseBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.FuseBatch.PhaseLosses

```{autodoc2-docstring} altdss.Fuse.FuseBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.FuseBatch.Powers

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Powers
```

````

````{py:attribute} RatedCurrent
:canonical: altdss.Fuse.FuseBatch.RatedCurrent
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.RatedCurrent
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Fuse.FuseBatch.SeqCurrents

```{autodoc2-docstring} altdss.Fuse.FuseBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.FuseBatch.SeqPowers

```{autodoc2-docstring} altdss.Fuse.FuseBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Fuse.FuseBatch.SeqVoltages

```{autodoc2-docstring} altdss.Fuse.FuseBatch.SeqVoltages
```

````

````{py:attribute} State
:canonical: altdss.Fuse.FuseBatch.State
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.State
```

````

````{py:attribute} State_str
:canonical: altdss.Fuse.FuseBatch.State_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Fuse.FuseBatch.SwitchedObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.Fuse.FuseBatch.SwitchedObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Fuse.FuseBatch.SwitchedTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.FuseBatch.SwitchedTerm
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.FuseBatch.TotalPowers

```{autodoc2-docstring} altdss.Fuse.FuseBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.FuseBatch.Voltages

```{autodoc2-docstring} altdss.Fuse.FuseBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fuse.FuseBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Fuse.FuseBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.Fuse.FuseBatch.__call__

```{autodoc2-docstring} altdss.Fuse.FuseBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Fuse.FuseBatch.__getitem__

```{autodoc2-docstring} altdss.Fuse.FuseBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Fuse.FuseBatch.__init__

```{autodoc2-docstring} altdss.Fuse.FuseBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Fuse.FuseBatch.__iter__

```{autodoc2-docstring} altdss.Fuse.FuseBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Fuse.FuseBatch.__len__

```{autodoc2-docstring} altdss.Fuse.FuseBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Fuse.FuseBatch.begin_edit

```{autodoc2-docstring} altdss.Fuse.FuseBatch.begin_edit
```

````

````{py:method} close(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.FuseBatch.close

```{autodoc2-docstring} altdss.Fuse.FuseBatch.close
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Fuse.FuseBatch.end_edit

```{autodoc2-docstring} altdss.Fuse.FuseBatch.end_edit
```

````

````{py:method} open(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.FuseBatch.open

```{autodoc2-docstring} altdss.Fuse.FuseBatch.open
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Fuse.FuseBatch.to_json

```{autodoc2-docstring} altdss.Fuse.FuseBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Fuse.FuseBatch.to_list

```{autodoc2-docstring} altdss.Fuse.FuseBatch.to_list
```

````

`````

`````{py:class} FuseBatchProperties()
:canonical: altdss.Fuse.FuseBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties
```

````{py:attribute} Action
:canonical: altdss.Fuse.FuseBatchProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.FuseAction]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Fuse.FuseBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.BaseFreq
```

````

````{py:attribute} Delay
:canonical: altdss.Fuse.FuseBatchProperties.Delay
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.Fuse.FuseBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.Enabled
```

````

````{py:attribute} FuseCurve
:canonical: altdss.Fuse.FuseBatchProperties.FuseCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.FuseCurve
```

````

````{py:attribute} Like
:canonical: altdss.Fuse.FuseBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.Like
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Fuse.FuseBatchProperties.MonitoredObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.MonitoredObj
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Fuse.FuseBatchProperties.MonitoredTerm
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.MonitoredTerm
```

````

````{py:attribute} Normal
:canonical: altdss.Fuse.FuseBatchProperties.Normal
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.FuseState]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.Normal
```

````

````{py:attribute} RatedCurrent
:canonical: altdss.Fuse.FuseBatchProperties.RatedCurrent
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.RatedCurrent
```

````

````{py:attribute} State
:canonical: altdss.Fuse.FuseBatchProperties.State
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.FuseState]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.State
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Fuse.FuseBatchProperties.SwitchedObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.SwitchedObj
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Fuse.FuseBatchProperties.SwitchedTerm
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.SwitchedTerm
```

````

````{py:method} __contains__()
:canonical: altdss.Fuse.FuseBatchProperties.__contains__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Fuse.FuseBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Fuse.FuseBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Fuse.FuseBatchProperties.__dir__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Fuse.FuseBatchProperties.__format__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Fuse.FuseBatchProperties.__ge__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Fuse.FuseBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Fuse.FuseBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Fuse.FuseBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Fuse.FuseBatchProperties.__gt__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Fuse.FuseBatchProperties.__init__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Fuse.FuseBatchProperties.__ior__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Fuse.FuseBatchProperties.__iter__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Fuse.FuseBatchProperties.__le__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Fuse.FuseBatchProperties.__len__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Fuse.FuseBatchProperties.__lt__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Fuse.FuseBatchProperties.__ne__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Fuse.FuseBatchProperties.__new__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Fuse.FuseBatchProperties.__or__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Fuse.FuseBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Fuse.FuseBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Fuse.FuseBatchProperties.__repr__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Fuse.FuseBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Fuse.FuseBatchProperties.__ror__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Fuse.FuseBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Fuse.FuseBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Fuse.FuseBatchProperties.__str__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Fuse.FuseBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Fuse.FuseBatchProperties.clear

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Fuse.FuseBatchProperties.copy

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Fuse.FuseBatchProperties.get

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Fuse.FuseBatchProperties.items

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Fuse.FuseBatchProperties.keys

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Fuse.FuseBatchProperties.pop

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Fuse.FuseBatchProperties.popitem

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Fuse.FuseBatchProperties.setdefault

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Fuse.FuseBatchProperties.update

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Fuse.FuseBatchProperties.values

```{autodoc2-docstring} altdss.Fuse.FuseBatchProperties.values
```

````

`````

`````{py:class} FuseProperties()
:canonical: altdss.Fuse.FuseProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Fuse.FuseProperties
```

````{py:attribute} Action
:canonical: altdss.Fuse.FuseProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.FuseAction]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Fuse.FuseProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.BaseFreq
```

````

````{py:attribute} Delay
:canonical: altdss.Fuse.FuseProperties.Delay
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.Fuse.FuseProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.Enabled
```

````

````{py:attribute} FuseCurve
:canonical: altdss.Fuse.FuseProperties.FuseCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.FuseCurve
```

````

````{py:attribute} Like
:canonical: altdss.Fuse.FuseProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.Like
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Fuse.FuseProperties.MonitoredObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.MonitoredObj
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Fuse.FuseProperties.MonitoredTerm
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.MonitoredTerm
```

````

````{py:attribute} Normal
:canonical: altdss.Fuse.FuseProperties.Normal
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.FuseState]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.Normal
```

````

````{py:attribute} RatedCurrent
:canonical: altdss.Fuse.FuseProperties.RatedCurrent
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.RatedCurrent
```

````

````{py:attribute} State
:canonical: altdss.Fuse.FuseProperties.State
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.FuseState]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.State
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Fuse.FuseProperties.SwitchedObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.SwitchedObj
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Fuse.FuseProperties.SwitchedTerm
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Fuse.FuseProperties.SwitchedTerm
```

````

````{py:method} __contains__()
:canonical: altdss.Fuse.FuseProperties.__contains__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Fuse.FuseProperties.__delattr__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Fuse.FuseProperties.__delitem__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Fuse.FuseProperties.__dir__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Fuse.FuseProperties.__format__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Fuse.FuseProperties.__ge__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Fuse.FuseProperties.__getattribute__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Fuse.FuseProperties.__getitem__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Fuse.FuseProperties.__getstate__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Fuse.FuseProperties.__gt__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Fuse.FuseProperties.__init__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Fuse.FuseProperties.__ior__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Fuse.FuseProperties.__iter__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Fuse.FuseProperties.__le__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Fuse.FuseProperties.__len__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Fuse.FuseProperties.__lt__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Fuse.FuseProperties.__ne__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Fuse.FuseProperties.__new__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Fuse.FuseProperties.__or__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Fuse.FuseProperties.__reduce__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Fuse.FuseProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Fuse.FuseProperties.__repr__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Fuse.FuseProperties.__reversed__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Fuse.FuseProperties.__ror__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Fuse.FuseProperties.__setitem__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Fuse.FuseProperties.__sizeof__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Fuse.FuseProperties.__str__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Fuse.FuseProperties.__subclasshook__

```{autodoc2-docstring} altdss.Fuse.FuseProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Fuse.FuseProperties.clear

```{autodoc2-docstring} altdss.Fuse.FuseProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Fuse.FuseProperties.copy

```{autodoc2-docstring} altdss.Fuse.FuseProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Fuse.FuseProperties.get

```{autodoc2-docstring} altdss.Fuse.FuseProperties.get
```

````

````{py:method} items()
:canonical: altdss.Fuse.FuseProperties.items

```{autodoc2-docstring} altdss.Fuse.FuseProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Fuse.FuseProperties.keys

```{autodoc2-docstring} altdss.Fuse.FuseProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Fuse.FuseProperties.pop

```{autodoc2-docstring} altdss.Fuse.FuseProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Fuse.FuseProperties.popitem

```{autodoc2-docstring} altdss.Fuse.FuseProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Fuse.FuseProperties.setdefault

```{autodoc2-docstring} altdss.Fuse.FuseProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Fuse.FuseProperties.update

```{autodoc2-docstring} altdss.Fuse.FuseProperties.update
```

````

````{py:method} values()
:canonical: altdss.Fuse.FuseProperties.values

```{autodoc2-docstring} altdss.Fuse.FuseProperties.values
```

````

`````

`````{py:class} IFuse(iobj)
:canonical: altdss.Fuse.IFuse

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Fuse.FuseBatch`

```{autodoc2-docstring} altdss.Fuse.IFuse
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.FuseAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.IFuse.Action

```{autodoc2-docstring} altdss.Fuse.IFuse.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Fuse.IFuse.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.IFuse.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Fuse.IFuse.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.IFuse.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Fuse.IFuse.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.IFuse.Currents

```{autodoc2-docstring} altdss.Fuse.IFuse.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fuse.IFuse.CurrentsMagAng

```{autodoc2-docstring} altdss.Fuse.IFuse.CurrentsMagAng
```

````

````{py:attribute} Delay
:canonical: altdss.Fuse.IFuse.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.Fuse.IFuse.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Fuse.IFuse.FullName

```{autodoc2-docstring} altdss.Fuse.IFuse.FullName
```

````

````{py:attribute} FuseCurve
:canonical: altdss.Fuse.IFuse.FuseCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.FuseCurve
```

````

````{py:attribute} FuseCurve_str
:canonical: altdss.Fuse.IFuse.FuseCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.FuseCurve_str
```

````

````{py:method} GUID() -> str
:canonical: altdss.Fuse.IFuse.GUID

```{autodoc2-docstring} altdss.Fuse.IFuse.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Fuse.IFuse.Handle

```{autodoc2-docstring} altdss.Fuse.IFuse.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Fuse.IFuse.HasOCPDevice

```{autodoc2-docstring} altdss.Fuse.IFuse.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Fuse.IFuse.HasSwitchControl

```{autodoc2-docstring} altdss.Fuse.IFuse.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Fuse.IFuse.HasVoltControl

```{autodoc2-docstring} altdss.Fuse.IFuse.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Fuse.IFuse.IsIsolated

```{autodoc2-docstring} altdss.Fuse.IFuse.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.IFuse.Like

```{autodoc2-docstring} altdss.Fuse.IFuse.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.IFuse.Losses

```{autodoc2-docstring} altdss.Fuse.IFuse.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Fuse.IFuse.MaxCurrent

```{autodoc2-docstring} altdss.Fuse.IFuse.MaxCurrent
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Fuse.IFuse.MonitoredObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.MonitoredObj
```

````

````{py:attribute} MonitoredObj_str
:canonical: altdss.Fuse.IFuse.MonitoredObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.MonitoredObj_str
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Fuse.IFuse.MonitoredTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.MonitoredTerm
```

````

````{py:property} Name
:canonical: altdss.Fuse.IFuse.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Fuse.IFuse.Name
```

````

````{py:attribute} Normal
:canonical: altdss.Fuse.IFuse.Normal
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.Fuse.IFuse.Normal_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.Normal_str
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Fuse.IFuse.NumConductors

```{autodoc2-docstring} altdss.Fuse.IFuse.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Fuse.IFuse.NumControllers

```{autodoc2-docstring} altdss.Fuse.IFuse.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Fuse.IFuse.NumPhases

```{autodoc2-docstring} altdss.Fuse.IFuse.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Fuse.IFuse.NumTerminals

```{autodoc2-docstring} altdss.Fuse.IFuse.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Fuse.IFuse.OCPDevice

```{autodoc2-docstring} altdss.Fuse.IFuse.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Fuse.IFuse.OCPDeviceIndex

```{autodoc2-docstring} altdss.Fuse.IFuse.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Fuse.IFuse.OCPDeviceType

```{autodoc2-docstring} altdss.Fuse.IFuse.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.IFuse.PhaseLosses

```{autodoc2-docstring} altdss.Fuse.IFuse.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.IFuse.Powers

```{autodoc2-docstring} altdss.Fuse.IFuse.Powers
```

````

````{py:attribute} RatedCurrent
:canonical: altdss.Fuse.IFuse.RatedCurrent
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.RatedCurrent
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Fuse.IFuse.SeqCurrents

```{autodoc2-docstring} altdss.Fuse.IFuse.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.IFuse.SeqPowers

```{autodoc2-docstring} altdss.Fuse.IFuse.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Fuse.IFuse.SeqVoltages

```{autodoc2-docstring} altdss.Fuse.IFuse.SeqVoltages
```

````

````{py:attribute} State
:canonical: altdss.Fuse.IFuse.State
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.State
```

````

````{py:attribute} State_str
:canonical: altdss.Fuse.IFuse.State_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Fuse.IFuse.SwitchedObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.Fuse.IFuse.SwitchedObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Fuse.IFuse.SwitchedTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Fuse.IFuse.SwitchedTerm
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.IFuse.TotalPowers

```{autodoc2-docstring} altdss.Fuse.IFuse.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Fuse.IFuse.Voltages

```{autodoc2-docstring} altdss.Fuse.IFuse.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fuse.IFuse.VoltagesMagAng

```{autodoc2-docstring} altdss.Fuse.IFuse.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.Fuse.IFuse.__call__

```{autodoc2-docstring} altdss.Fuse.IFuse.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Fuse.IFuse.__contains__

```{autodoc2-docstring} altdss.Fuse.IFuse.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Fuse.IFuse.__getitem__

```{autodoc2-docstring} altdss.Fuse.IFuse.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Fuse.IFuse.__init__

```{autodoc2-docstring} altdss.Fuse.IFuse.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Fuse.IFuse.__iter__

```{autodoc2-docstring} altdss.Fuse.IFuse.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Fuse.IFuse.__len__

```{autodoc2-docstring} altdss.Fuse.IFuse.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Fuse.IFuse.batch

```{autodoc2-docstring} altdss.Fuse.IFuse.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Fuse.FuseBatchProperties]) -> altdss.Fuse.FuseBatch
:canonical: altdss.Fuse.IFuse.batch_new

```{autodoc2-docstring} altdss.Fuse.IFuse.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Fuse.IFuse.begin_edit

```{autodoc2-docstring} altdss.Fuse.IFuse.begin_edit
```

````

````{py:method} close(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.IFuse.close

```{autodoc2-docstring} altdss.Fuse.IFuse.close
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Fuse.IFuse.end_edit

```{autodoc2-docstring} altdss.Fuse.IFuse.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Fuse.IFuse.find

```{autodoc2-docstring} altdss.Fuse.IFuse.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Fuse.FuseProperties]) -> altdss.Fuse.Fuse
:canonical: altdss.Fuse.IFuse.new

```{autodoc2-docstring} altdss.Fuse.IFuse.new
```

````

````{py:method} open(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fuse.IFuse.open

```{autodoc2-docstring} altdss.Fuse.IFuse.open
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Fuse.IFuse.to_json

```{autodoc2-docstring} altdss.Fuse.IFuse.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Fuse.IFuse.to_list

```{autodoc2-docstring} altdss.Fuse.IFuse.to_list
```

````

`````
