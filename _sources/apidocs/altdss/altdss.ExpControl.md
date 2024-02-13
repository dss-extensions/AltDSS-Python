# {py:mod}`altdss.ExpControl`

```{py:module} altdss.ExpControl
```

```{autodoc2-docstring} altdss.ExpControl
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ExpControl <altdss.ExpControl.ExpControl>`
  - ```{autodoc2-docstring} altdss.ExpControl.ExpControl
    :summary:
    ```
* - {py:obj}`ExpControlBatch <altdss.ExpControl.ExpControlBatch>`
  - ```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch
    :summary:
    ```
* - {py:obj}`ExpControlBatchProperties <altdss.ExpControl.ExpControlBatchProperties>`
  - ```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties
    :summary:
    ```
* - {py:obj}`ExpControlProperties <altdss.ExpControl.ExpControlProperties>`
  - ```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties
    :summary:
    ```
* - {py:obj}`IExpControl <altdss.ExpControl.IExpControl>`
  - ```{autodoc2-docstring} altdss.ExpControl.IExpControl
    :summary:
    ```
````

### API

`````{py:class} ExpControl(api_util, ptr)
:canonical: altdss.ExpControl.ExpControl

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.ExpControl.ExpControl
```

````{py:attribute} BaseFreq
:canonical: altdss.ExpControl.ExpControl.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.ExpControl.ExpControl.Close

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.ExpControl.ExpControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.ExpControl.ExpControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControl.Currents

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Currents
```

````

````{py:attribute} DERList
:canonical: altdss.ExpControl.ExpControl.DERList
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.DERList
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.ExpControl.ExpControl.DeltaQ_Factor
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.DeltaQ_Factor
```

````

````{py:attribute} DisplayName
:canonical: altdss.ExpControl.ExpControl.DisplayName
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.DisplayName
```

````

````{py:attribute} Enabled
:canonical: altdss.ExpControl.ExpControl.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.ExpControl.ExpControl.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.EventLog
```

````

````{py:method} FullName() -> str
:canonical: altdss.ExpControl.ExpControl.FullName

```{autodoc2-docstring} altdss.ExpControl.ExpControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.ExpControl.ExpControl.GUID

```{autodoc2-docstring} altdss.ExpControl.ExpControl.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.ExpControl.ExpControl.Handle

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.ExpControl.ExpControl.HasOCPDevice

```{autodoc2-docstring} altdss.ExpControl.ExpControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.ExpControl.ExpControl.HasSwitchControl

```{autodoc2-docstring} altdss.ExpControl.ExpControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.ExpControl.ExpControl.HasVoltControl

```{autodoc2-docstring} altdss.ExpControl.ExpControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.ExpControl.ExpControl.IsIsolated

```{autodoc2-docstring} altdss.ExpControl.ExpControl.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.ExpControl.ExpControl.IsOpen

```{autodoc2-docstring} altdss.ExpControl.ExpControl.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.ExpControl.ExpControl.Like

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.ExpControl.ExpControl.Losses

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.ExpControl.ExpControl.MaxCurrent

```{autodoc2-docstring} altdss.ExpControl.ExpControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.ExpControl.ExpControl.Name
:type: str

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.ExpControl.NodeOrder

```{autodoc2-docstring} altdss.ExpControl.ExpControl.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.ExpControl.NodeRef

```{autodoc2-docstring} altdss.ExpControl.ExpControl.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.ExpControl.ExpControl.NumConductors

```{autodoc2-docstring} altdss.ExpControl.ExpControl.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.ExpControl.ExpControl.NumControllers

```{autodoc2-docstring} altdss.ExpControl.ExpControl.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.ExpControl.ExpControl.NumPhases

```{autodoc2-docstring} altdss.ExpControl.ExpControl.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.ExpControl.ExpControl.NumTerminals

```{autodoc2-docstring} altdss.ExpControl.ExpControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.ExpControl.ExpControl.OCPDevice

```{autodoc2-docstring} altdss.ExpControl.ExpControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.ExpControl.ExpControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.ExpControl.ExpControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.ExpControl.ExpControl.OCPDeviceType

```{autodoc2-docstring} altdss.ExpControl.ExpControl.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.ExpControl.ExpControl.Open

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Open
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ExpControl.ExpControl.PVSystemList
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.PVSystemList
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControl.PhaseLosses

```{autodoc2-docstring} altdss.ExpControl.ExpControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControl.Powers

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Powers
```

````

````{py:attribute} PreferQ
:canonical: altdss.ExpControl.ExpControl.PreferQ
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.PreferQ
```

````

````{py:attribute} QBias
:canonical: altdss.ExpControl.ExpControl.QBias
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.QBias
```

````

````{py:attribute} QMaxLag
:canonical: altdss.ExpControl.ExpControl.QMaxLag
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.QMaxLag
```

````

````{py:attribute} QMaxLead
:canonical: altdss.ExpControl.ExpControl.QMaxLead
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.QMaxLead
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.ExpControl.Residuals

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.ExpControl.SeqCurrents

```{autodoc2-docstring} altdss.ExpControl.ExpControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControl.SeqPowers

```{autodoc2-docstring} altdss.ExpControl.ExpControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.ExpControl.SeqVoltages

```{autodoc2-docstring} altdss.ExpControl.ExpControl.SeqVoltages
```

````

````{py:attribute} Slope
:canonical: altdss.ExpControl.ExpControl.Slope
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Slope
```

````

````{py:attribute} TResponse
:canonical: altdss.ExpControl.ExpControl.TResponse
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.TResponse
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControl.TotalPowers

```{autodoc2-docstring} altdss.ExpControl.ExpControl.TotalPowers
```

````

````{py:attribute} VReg
:canonical: altdss.ExpControl.ExpControl.VReg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.VReg
```

````

````{py:attribute} VRegMax
:canonical: altdss.ExpControl.ExpControl.VRegMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.VRegMax
```

````

````{py:attribute} VRegMin
:canonical: altdss.ExpControl.ExpControl.VRegMin
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.VRegMin
```

````

````{py:attribute} VRegTau
:canonical: altdss.ExpControl.ExpControl.VRegTau
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControl.VRegTau
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControl.Voltages

```{autodoc2-docstring} altdss.ExpControl.ExpControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.ExpControl.VoltagesMagAng

```{autodoc2-docstring} altdss.ExpControl.ExpControl.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControl.YPrim

```{autodoc2-docstring} altdss.ExpControl.ExpControl.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.ExpControl.ExpControl.__hash__

```{autodoc2-docstring} altdss.ExpControl.ExpControl.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.ExpControl.ExpControl.__init__

```{autodoc2-docstring} altdss.ExpControl.ExpControl.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.ExpControl.ExpControl.__ne__

```{autodoc2-docstring} altdss.ExpControl.ExpControl.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.ExpControl.ExpControl.__repr__

```{autodoc2-docstring} altdss.ExpControl.ExpControl.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.ExpControl.ExpControl.begin_edit

```{autodoc2-docstring} altdss.ExpControl.ExpControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.ExpControl.ExpControl.end_edit

```{autodoc2-docstring} altdss.ExpControl.ExpControl.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.ExpControl.ExpControl.to_json

```{autodoc2-docstring} altdss.ExpControl.ExpControl.to_json
```

````

`````

`````{py:class} ExpControlBatch(api_util, **kwargs)
:canonical: altdss.ExpControl.ExpControlBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.ExpControl.ExpControlBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControlBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControlBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControlBatch.Currents

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.ExpControlBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.CurrentsMagAng
```

````

````{py:attribute} DERList
:canonical: altdss.ExpControl.ExpControlBatch.DERList
:type: typing.List[typing.List[str]]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.DERList
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.ExpControl.ExpControlBatch.DeltaQ_Factor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.DeltaQ_Factor
```

````

````{py:attribute} Enabled
:canonical: altdss.ExpControl.ExpControlBatch.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.ExpControl.ExpControlBatch.EventLog
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.ExpControl.ExpControlBatch.FullName

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.ExpControl.ExpControlBatch.GUID

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.ExpControlBatch.Handle

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.ExpControl.ExpControlBatch.HasOCPDevice

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.ExpControl.ExpControlBatch.HasSwitchControl

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.ExpControl.ExpControlBatch.HasVoltControl

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.ExpControl.ExpControlBatch.IsIsolated

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.ExpControl.ExpControlBatch.Like

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControlBatch.Losses

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.ExpControl.ExpControlBatch.MaxCurrent

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.ExpControl.ExpControlBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.ExpControlBatch.NumConductors

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.ExpControlBatch.NumControllers

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.ExpControlBatch.NumPhases

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.ExpControlBatch.NumTerminals

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.ExpControl.ExpControlBatch.OCPDevice

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.ExpControlBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.ExpControl.ExpControlBatch.OCPDeviceType

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.OCPDeviceType
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ExpControl.ExpControlBatch.PVSystemList
:type: typing.List[typing.List[str]]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.PVSystemList
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControlBatch.PhaseLosses

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControlBatch.Powers

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.Powers
```

````

````{py:attribute} PreferQ
:canonical: altdss.ExpControl.ExpControlBatch.PreferQ
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.PreferQ
```

````

````{py:attribute} QBias
:canonical: altdss.ExpControl.ExpControlBatch.QBias
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.QBias
```

````

````{py:attribute} QMaxLag
:canonical: altdss.ExpControl.ExpControlBatch.QMaxLag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.QMaxLag
```

````

````{py:attribute} QMaxLead
:canonical: altdss.ExpControl.ExpControlBatch.QMaxLead
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.QMaxLead
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.ExpControlBatch.SeqCurrents

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControlBatch.SeqPowers

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.ExpControlBatch.SeqVoltages

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.SeqVoltages
```

````

````{py:attribute} Slope
:canonical: altdss.ExpControl.ExpControlBatch.Slope
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.Slope
```

````

````{py:attribute} TResponse
:canonical: altdss.ExpControl.ExpControlBatch.TResponse
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.TResponse
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControlBatch.TotalPowers

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.TotalPowers
```

````

````{py:attribute} VReg
:canonical: altdss.ExpControl.ExpControlBatch.VReg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.VReg
```

````

````{py:attribute} VRegMax
:canonical: altdss.ExpControl.ExpControlBatch.VRegMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.VRegMax
```

````

````{py:attribute} VRegMin
:canonical: altdss.ExpControl.ExpControlBatch.VRegMin
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.VRegMin
```

````

````{py:attribute} VRegTau
:canonical: altdss.ExpControl.ExpControlBatch.VRegTau
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.VRegTau
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.ExpControlBatch.Voltages

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.ExpControlBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.ExpControl.ExpControlBatch.__call__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.ExpControl.ExpControlBatch.__getitem__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.ExpControl.ExpControlBatch.__init__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.ExpControl.ExpControlBatch.__iter__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.ExpControl.ExpControlBatch.__len__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.ExpControl.ExpControlBatch.begin_edit

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.ExpControl.ExpControlBatch.end_edit

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.ExpControl.ExpControlBatch.to_json

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.ExpControl.ExpControlBatch.to_list

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatch.to_list
```

````

`````

`````{py:class} ExpControlBatchProperties()
:canonical: altdss.ExpControl.ExpControlBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.ExpControl.ExpControlBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.BaseFreq
```

````

````{py:attribute} DERList
:canonical: altdss.ExpControl.ExpControlBatchProperties.DERList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.DERList
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.ExpControl.ExpControlBatchProperties.DeltaQ_Factor
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.DeltaQ_Factor
```

````

````{py:attribute} Enabled
:canonical: altdss.ExpControl.ExpControlBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.ExpControl.ExpControlBatchProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.EventLog
```

````

````{py:attribute} Like
:canonical: altdss.ExpControl.ExpControlBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.Like
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ExpControl.ExpControlBatchProperties.PVSystemList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.PVSystemList
```

````

````{py:attribute} PreferQ
:canonical: altdss.ExpControl.ExpControlBatchProperties.PreferQ
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.PreferQ
```

````

````{py:attribute} QBias
:canonical: altdss.ExpControl.ExpControlBatchProperties.QBias
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.QBias
```

````

````{py:attribute} QMaxLag
:canonical: altdss.ExpControl.ExpControlBatchProperties.QMaxLag
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.QMaxLag
```

````

````{py:attribute} QMaxLead
:canonical: altdss.ExpControl.ExpControlBatchProperties.QMaxLead
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.QMaxLead
```

````

````{py:attribute} Slope
:canonical: altdss.ExpControl.ExpControlBatchProperties.Slope
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.Slope
```

````

````{py:attribute} TResponse
:canonical: altdss.ExpControl.ExpControlBatchProperties.TResponse
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.TResponse
```

````

````{py:attribute} VReg
:canonical: altdss.ExpControl.ExpControlBatchProperties.VReg
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.VReg
```

````

````{py:attribute} VRegMax
:canonical: altdss.ExpControl.ExpControlBatchProperties.VRegMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.VRegMax
```

````

````{py:attribute} VRegMin
:canonical: altdss.ExpControl.ExpControlBatchProperties.VRegMin
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.VRegMin
```

````

````{py:attribute} VRegTau
:canonical: altdss.ExpControl.ExpControlBatchProperties.VRegTau
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.VRegTau
```

````

````{py:method} __contains__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__contains__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__delattr__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__delitem__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__dir__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__format__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__ge__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__getitem__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__getstate__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__gt__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__init__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__ior__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__iter__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__le__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__len__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__lt__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__ne__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__new__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__or__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__reduce__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__repr__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__reversed__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__ror__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__setitem__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__str__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.ExpControl.ExpControlBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.ExpControl.ExpControlBatchProperties.clear

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.ExpControl.ExpControlBatchProperties.copy

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.ExpControl.ExpControlBatchProperties.get

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.ExpControl.ExpControlBatchProperties.items

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.ExpControl.ExpControlBatchProperties.keys

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.ExpControl.ExpControlBatchProperties.pop

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.ExpControl.ExpControlBatchProperties.popitem

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.ExpControl.ExpControlBatchProperties.setdefault

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.ExpControl.ExpControlBatchProperties.update

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.ExpControl.ExpControlBatchProperties.values

```{autodoc2-docstring} altdss.ExpControl.ExpControlBatchProperties.values
```

````

`````

`````{py:class} ExpControlProperties()
:canonical: altdss.ExpControl.ExpControlProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.ExpControl.ExpControlProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.BaseFreq
```

````

````{py:attribute} DERList
:canonical: altdss.ExpControl.ExpControlProperties.DERList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.DERList
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.ExpControl.ExpControlProperties.DeltaQ_Factor
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.DeltaQ_Factor
```

````

````{py:attribute} Enabled
:canonical: altdss.ExpControl.ExpControlProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.ExpControl.ExpControlProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.EventLog
```

````

````{py:attribute} Like
:canonical: altdss.ExpControl.ExpControlProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.Like
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ExpControl.ExpControlProperties.PVSystemList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.PVSystemList
```

````

````{py:attribute} PreferQ
:canonical: altdss.ExpControl.ExpControlProperties.PreferQ
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.PreferQ
```

````

````{py:attribute} QBias
:canonical: altdss.ExpControl.ExpControlProperties.QBias
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.QBias
```

````

````{py:attribute} QMaxLag
:canonical: altdss.ExpControl.ExpControlProperties.QMaxLag
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.QMaxLag
```

````

````{py:attribute} QMaxLead
:canonical: altdss.ExpControl.ExpControlProperties.QMaxLead
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.QMaxLead
```

````

````{py:attribute} Slope
:canonical: altdss.ExpControl.ExpControlProperties.Slope
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.Slope
```

````

````{py:attribute} TResponse
:canonical: altdss.ExpControl.ExpControlProperties.TResponse
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.TResponse
```

````

````{py:attribute} VReg
:canonical: altdss.ExpControl.ExpControlProperties.VReg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.VReg
```

````

````{py:attribute} VRegMax
:canonical: altdss.ExpControl.ExpControlProperties.VRegMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.VRegMax
```

````

````{py:attribute} VRegMin
:canonical: altdss.ExpControl.ExpControlProperties.VRegMin
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.VRegMin
```

````

````{py:attribute} VRegTau
:canonical: altdss.ExpControl.ExpControlProperties.VRegTau
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.VRegTau
```

````

````{py:method} __contains__()
:canonical: altdss.ExpControl.ExpControlProperties.__contains__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.ExpControl.ExpControlProperties.__delattr__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.ExpControl.ExpControlProperties.__delitem__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.ExpControl.ExpControlProperties.__dir__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.ExpControl.ExpControlProperties.__format__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.ExpControl.ExpControlProperties.__ge__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.ExpControl.ExpControlProperties.__getattribute__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.ExpControl.ExpControlProperties.__getitem__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.ExpControl.ExpControlProperties.__getstate__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.ExpControl.ExpControlProperties.__gt__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.ExpControl.ExpControlProperties.__init__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.ExpControl.ExpControlProperties.__ior__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.ExpControl.ExpControlProperties.__iter__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.ExpControl.ExpControlProperties.__le__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.ExpControl.ExpControlProperties.__len__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.ExpControl.ExpControlProperties.__lt__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.ExpControl.ExpControlProperties.__ne__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.ExpControl.ExpControlProperties.__new__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.ExpControl.ExpControlProperties.__or__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.ExpControl.ExpControlProperties.__reduce__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.ExpControl.ExpControlProperties.__reduce_ex__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.ExpControl.ExpControlProperties.__repr__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.ExpControl.ExpControlProperties.__reversed__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.ExpControl.ExpControlProperties.__ror__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.ExpControl.ExpControlProperties.__setitem__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.ExpControl.ExpControlProperties.__sizeof__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.ExpControl.ExpControlProperties.__str__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.ExpControl.ExpControlProperties.__subclasshook__

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.ExpControl.ExpControlProperties.clear

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.ExpControl.ExpControlProperties.copy

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.copy
```

````

````{py:method} get()
:canonical: altdss.ExpControl.ExpControlProperties.get

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.get
```

````

````{py:method} items()
:canonical: altdss.ExpControl.ExpControlProperties.items

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.items
```

````

````{py:method} keys()
:canonical: altdss.ExpControl.ExpControlProperties.keys

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.ExpControl.ExpControlProperties.pop

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.ExpControl.ExpControlProperties.popitem

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.ExpControl.ExpControlProperties.setdefault

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.ExpControl.ExpControlProperties.update

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.update
```

````

````{py:method} values()
:canonical: altdss.ExpControl.ExpControlProperties.values

```{autodoc2-docstring} altdss.ExpControl.ExpControlProperties.values
```

````

`````

`````{py:class} IExpControl(iobj)
:canonical: altdss.ExpControl.IExpControl

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.ExpControl.ExpControlBatch`

```{autodoc2-docstring} altdss.ExpControl.IExpControl
```

````{py:attribute} BaseFreq
:canonical: altdss.ExpControl.IExpControl.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.IExpControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.ExpControl.IExpControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.IExpControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.ExpControl.IExpControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.IExpControl.Currents

```{autodoc2-docstring} altdss.ExpControl.IExpControl.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.IExpControl.CurrentsMagAng

```{autodoc2-docstring} altdss.ExpControl.IExpControl.CurrentsMagAng
```

````

````{py:attribute} DERList
:canonical: altdss.ExpControl.IExpControl.DERList
:type: typing.List[typing.List[str]]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.DERList
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.ExpControl.IExpControl.DeltaQ_Factor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.DeltaQ_Factor
```

````

````{py:attribute} Enabled
:canonical: altdss.ExpControl.IExpControl.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.ExpControl.IExpControl.EventLog
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.ExpControl.IExpControl.FullName

```{autodoc2-docstring} altdss.ExpControl.IExpControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.ExpControl.IExpControl.GUID

```{autodoc2-docstring} altdss.ExpControl.IExpControl.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.IExpControl.Handle

```{autodoc2-docstring} altdss.ExpControl.IExpControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.ExpControl.IExpControl.HasOCPDevice

```{autodoc2-docstring} altdss.ExpControl.IExpControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.ExpControl.IExpControl.HasSwitchControl

```{autodoc2-docstring} altdss.ExpControl.IExpControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.ExpControl.IExpControl.HasVoltControl

```{autodoc2-docstring} altdss.ExpControl.IExpControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.ExpControl.IExpControl.IsIsolated

```{autodoc2-docstring} altdss.ExpControl.IExpControl.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.ExpControl.IExpControl.Like

```{autodoc2-docstring} altdss.ExpControl.IExpControl.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.IExpControl.Losses

```{autodoc2-docstring} altdss.ExpControl.IExpControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.ExpControl.IExpControl.MaxCurrent

```{autodoc2-docstring} altdss.ExpControl.IExpControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.ExpControl.IExpControl.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.ExpControl.IExpControl.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.IExpControl.NumConductors

```{autodoc2-docstring} altdss.ExpControl.IExpControl.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.IExpControl.NumControllers

```{autodoc2-docstring} altdss.ExpControl.IExpControl.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.IExpControl.NumPhases

```{autodoc2-docstring} altdss.ExpControl.IExpControl.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.IExpControl.NumTerminals

```{autodoc2-docstring} altdss.ExpControl.IExpControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.ExpControl.IExpControl.OCPDevice

```{autodoc2-docstring} altdss.ExpControl.IExpControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.ExpControl.IExpControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.ExpControl.IExpControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.ExpControl.IExpControl.OCPDeviceType

```{autodoc2-docstring} altdss.ExpControl.IExpControl.OCPDeviceType
```

````

````{py:attribute} PVSystemList
:canonical: altdss.ExpControl.IExpControl.PVSystemList
:type: typing.List[typing.List[str]]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.PVSystemList
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.IExpControl.PhaseLosses

```{autodoc2-docstring} altdss.ExpControl.IExpControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.IExpControl.Powers

```{autodoc2-docstring} altdss.ExpControl.IExpControl.Powers
```

````

````{py:attribute} PreferQ
:canonical: altdss.ExpControl.IExpControl.PreferQ
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.PreferQ
```

````

````{py:attribute} QBias
:canonical: altdss.ExpControl.IExpControl.QBias
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.QBias
```

````

````{py:attribute} QMaxLag
:canonical: altdss.ExpControl.IExpControl.QMaxLag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.QMaxLag
```

````

````{py:attribute} QMaxLead
:canonical: altdss.ExpControl.IExpControl.QMaxLead
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.QMaxLead
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.IExpControl.SeqCurrents

```{autodoc2-docstring} altdss.ExpControl.IExpControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.IExpControl.SeqPowers

```{autodoc2-docstring} altdss.ExpControl.IExpControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.IExpControl.SeqVoltages

```{autodoc2-docstring} altdss.ExpControl.IExpControl.SeqVoltages
```

````

````{py:attribute} Slope
:canonical: altdss.ExpControl.IExpControl.Slope
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.Slope
```

````

````{py:attribute} TResponse
:canonical: altdss.ExpControl.IExpControl.TResponse
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.TResponse
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.IExpControl.TotalPowers

```{autodoc2-docstring} altdss.ExpControl.IExpControl.TotalPowers
```

````

````{py:attribute} VReg
:canonical: altdss.ExpControl.IExpControl.VReg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.VReg
```

````

````{py:attribute} VRegMax
:canonical: altdss.ExpControl.IExpControl.VRegMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.VRegMax
```

````

````{py:attribute} VRegMin
:canonical: altdss.ExpControl.IExpControl.VRegMin
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.VRegMin
```

````

````{py:attribute} VRegTau
:canonical: altdss.ExpControl.IExpControl.VRegTau
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.ExpControl.IExpControl.VRegTau
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.ExpControl.IExpControl.Voltages

```{autodoc2-docstring} altdss.ExpControl.IExpControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.ExpControl.IExpControl.VoltagesMagAng

```{autodoc2-docstring} altdss.ExpControl.IExpControl.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.ExpControl.IExpControl.__call__

```{autodoc2-docstring} altdss.ExpControl.IExpControl.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.ExpControl.IExpControl.__contains__

```{autodoc2-docstring} altdss.ExpControl.IExpControl.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.ExpControl.IExpControl.__getitem__

```{autodoc2-docstring} altdss.ExpControl.IExpControl.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.ExpControl.IExpControl.__init__

```{autodoc2-docstring} altdss.ExpControl.IExpControl.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.ExpControl.IExpControl.__iter__

```{autodoc2-docstring} altdss.ExpControl.IExpControl.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.ExpControl.IExpControl.__len__

```{autodoc2-docstring} altdss.ExpControl.IExpControl.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.ExpControl.IExpControl.batch

```{autodoc2-docstring} altdss.ExpControl.IExpControl.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.ExpControl.ExpControlBatchProperties]) -> altdss.ExpControl.ExpControlBatch
:canonical: altdss.ExpControl.IExpControl.batch_new

```{autodoc2-docstring} altdss.ExpControl.IExpControl.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.ExpControl.IExpControl.begin_edit

```{autodoc2-docstring} altdss.ExpControl.IExpControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.ExpControl.IExpControl.end_edit

```{autodoc2-docstring} altdss.ExpControl.IExpControl.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.ExpControl.IExpControl.find

```{autodoc2-docstring} altdss.ExpControl.IExpControl.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.ExpControl.ExpControlProperties]) -> altdss.ExpControl.ExpControl
:canonical: altdss.ExpControl.IExpControl.new

```{autodoc2-docstring} altdss.ExpControl.IExpControl.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.ExpControl.IExpControl.to_json

```{autodoc2-docstring} altdss.ExpControl.IExpControl.to_json
```

````

````{py:method} to_list()
:canonical: altdss.ExpControl.IExpControl.to_list

```{autodoc2-docstring} altdss.ExpControl.IExpControl.to_list
```

````

`````
