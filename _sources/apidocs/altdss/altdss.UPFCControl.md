# {py:mod}`altdss.UPFCControl`

```{py:module} altdss.UPFCControl
```

```{autodoc2-docstring} altdss.UPFCControl
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IUPFCControl <altdss.UPFCControl.IUPFCControl>`
  - ```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl
    :summary:
    ```
* - {py:obj}`UPFCControl <altdss.UPFCControl.UPFCControl>`
  - ```{autodoc2-docstring} altdss.UPFCControl.UPFCControl
    :summary:
    ```
* - {py:obj}`UPFCControlBatch <altdss.UPFCControl.UPFCControlBatch>`
  - ```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch
    :summary:
    ```
* - {py:obj}`UPFCControlBatchProperties <altdss.UPFCControl.UPFCControlBatchProperties>`
  - ```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties
    :summary:
    ```
* - {py:obj}`UPFCControlProperties <altdss.UPFCControl.UPFCControlProperties>`
  - ```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties
    :summary:
    ```
````

### API

`````{py:class} IUPFCControl(iobj)
:canonical: altdss.UPFCControl.IUPFCControl

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.UPFCControl.UPFCControlBatch`

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFCControl.IUPFCControl.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.IUPFCControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.IUPFCControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.IUPFCControl.Currents

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.IUPFCControl.CurrentsMagAng

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.CurrentsMagAng
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFCControl.IUPFCControl.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.UPFCControl.IUPFCControl.FullName

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.UPFCControl.IUPFCControl.GUID

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.IUPFCControl.Handle

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.UPFCControl.IUPFCControl.HasOCPDevice

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.UPFCControl.IUPFCControl.HasSwitchControl

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.UPFCControl.IUPFCControl.HasVoltControl

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.UPFCControl.IUPFCControl.IsIsolated

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.UPFCControl.IUPFCControl.Like

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.IUPFCControl.Losses

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.IUPFCControl.MaxCurrent

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.UPFCControl.IUPFCControl.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.IUPFCControl.NumConductors

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.IUPFCControl.NumControllers

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.IUPFCControl.NumPhases

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.IUPFCControl.NumTerminals

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.UPFCControl.IUPFCControl.OCPDevice

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.IUPFCControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.UPFCControl.IUPFCControl.OCPDeviceType

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.IUPFCControl.PhaseLosses

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.IUPFCControl.Powers

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.IUPFCControl.SeqCurrents

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.IUPFCControl.SeqPowers

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.IUPFCControl.SeqVoltages

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.IUPFCControl.TotalPowers

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.TotalPowers
```

````

````{py:attribute} UPFCList
:canonical: altdss.UPFCControl.IUPFCControl.UPFCList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.UPFCList
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.IUPFCControl.Voltages

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.IUPFCControl.VoltagesMagAng

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.UPFCControl.IUPFCControl.__call__

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.UPFCControl.IUPFCControl.__contains__

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.UPFCControl.IUPFCControl.__getitem__

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.UPFCControl.IUPFCControl.__init__

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.UPFCControl.IUPFCControl.__iter__

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.UPFCControl.IUPFCControl.__len__

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.UPFCControl.IUPFCControl.batch

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.UPFCControl.UPFCControlBatchProperties]) -> altdss.UPFCControl.UPFCControlBatch
:canonical: altdss.UPFCControl.IUPFCControl.batch_new

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.UPFCControl.IUPFCControl.begin_edit

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.UPFCControl.UPFCControlBatchProperties]) -> altdss.UPFCControl.UPFCControlBatch
:canonical: altdss.UPFCControl.IUPFCControl.edit

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.UPFCControl.IUPFCControl.end_edit

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.UPFCControl.IUPFCControl.find

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.find
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.UPFCControl.UPFCControlProperties]) -> altdss.UPFCControl.UPFCControl
:canonical: altdss.UPFCControl.IUPFCControl.new

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.UPFCControl.IUPFCControl.to_json

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.to_json
```

````

````{py:method} to_list()
:canonical: altdss.UPFCControl.IUPFCControl.to_list

```{autodoc2-docstring} altdss.UPFCControl.IUPFCControl.to_list
```

````

`````

`````{py:class} UPFCControl(api_util, ptr)
:canonical: altdss.UPFCControl.UPFCControl

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFCControl.UPFCControl.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.UPFCControl.UPFCControl.Close

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControl.Currents

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.UPFCControl.UPFCControl.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.DisplayName
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFCControl.UPFCControl.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Enabled
```

````

````{py:method} FullName() -> str
:canonical: altdss.UPFCControl.UPFCControl.FullName

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.UPFCControl.UPFCControl.GUID

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.UPFCControl.UPFCControl.Handle

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.UPFCControl.UPFCControl.HasOCPDevice

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.UPFCControl.UPFCControl.HasSwitchControl

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.UPFCControl.UPFCControl.HasVoltControl

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.UPFCControl.UPFCControl.IsIsolated

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.UPFCControl.UPFCControl.IsOpen

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.UPFCControl.UPFCControl.Like

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.UPFCControl.UPFCControl.Losses

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.UPFCControl.UPFCControl.MaxCurrent

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.UPFCControl.UPFCControl.Name
:type: str

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.UPFCControl.NodeOrder

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.UPFCControl.NodeRef

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.UPFCControl.UPFCControl.NumConductors

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.UPFCControl.UPFCControl.NumControllers

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.UPFCControl.UPFCControl.NumPhases

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.UPFCControl.UPFCControl.NumTerminals

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.UPFCControl.UPFCControl.OCPDevice

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.UPFCControl.UPFCControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.UPFCControl.UPFCControl.OCPDeviceType

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.UPFCControl.UPFCControl.Open

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControl.PhaseLosses

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControl.Powers

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Powers
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.UPFCControl.Residuals

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.UPFCControl.SeqCurrents

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControl.SeqPowers

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.UPFCControl.SeqVoltages

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControl.TotalPowers

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.TotalPowers
```

````

````{py:attribute} UPFCList
:canonical: altdss.UPFCControl.UPFCControl.UPFCList
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.UPFCList
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControl.Voltages

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.UPFCControl.VoltagesMagAng

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControl.YPrim

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.UPFCControl.UPFCControl.__hash__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.UPFCControl.UPFCControl.__init__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.UPFCControl.UPFCControl.__ne__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.UPFCControl.UPFCControl.__repr__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.UPFCControl.UPFCControl.begin_edit

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.UPFCControl.UPFCControlProperties]) -> altdss.UPFCControl.UPFCControl
:canonical: altdss.UPFCControl.UPFCControl.edit

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.UPFCControl.UPFCControl.end_edit

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.UPFCControl.UPFCControl.to_json

```{autodoc2-docstring} altdss.UPFCControl.UPFCControl.to_json
```

````

`````

`````{py:class} UPFCControlBatch(api_util, **kwargs)
:canonical: altdss.UPFCControl.UPFCControlBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFCControl.UPFCControlBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControlBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControlBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControlBatch.Currents

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.UPFCControlBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.CurrentsMagAng
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFCControl.UPFCControlBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.UPFCControl.UPFCControlBatch.FullName

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.UPFCControl.UPFCControlBatch.GUID

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.UPFCControlBatch.Handle

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.UPFCControl.UPFCControlBatch.HasOCPDevice

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.UPFCControl.UPFCControlBatch.HasSwitchControl

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.UPFCControl.UPFCControlBatch.HasVoltControl

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.UPFCControl.UPFCControlBatch.IsIsolated

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.UPFCControl.UPFCControlBatch.Like

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControlBatch.Losses

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.UPFCControlBatch.MaxCurrent

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.UPFCControl.UPFCControlBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.UPFCControlBatch.NumConductors

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.UPFCControlBatch.NumControllers

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.UPFCControlBatch.NumPhases

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.UPFCControlBatch.NumTerminals

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.UPFCControl.UPFCControlBatch.OCPDevice

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.UPFCControl.UPFCControlBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.UPFCControl.UPFCControlBatch.OCPDeviceType

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControlBatch.PhaseLosses

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControlBatch.Powers

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.UPFCControlBatch.SeqCurrents

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControlBatch.SeqPowers

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.UPFCControlBatch.SeqVoltages

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControlBatch.TotalPowers

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.TotalPowers
```

````

````{py:attribute} UPFCList
:canonical: altdss.UPFCControl.UPFCControlBatch.UPFCList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.UPFCList
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFCControl.UPFCControlBatch.Voltages

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFCControl.UPFCControlBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.UPFCControl.UPFCControlBatch.__call__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.UPFCControl.UPFCControlBatch.__getitem__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.UPFCControl.UPFCControlBatch.__init__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.UPFCControl.UPFCControlBatch.__iter__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.UPFCControl.UPFCControlBatch.__len__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.UPFCControl.UPFCControlBatch.batch

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.UPFCControl.UPFCControlBatch.begin_edit

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.UPFCControl.UPFCControlBatchProperties]) -> altdss.UPFCControl.UPFCControlBatch
:canonical: altdss.UPFCControl.UPFCControlBatch.edit

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.UPFCControl.UPFCControlBatch.end_edit

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.UPFCControl.UPFCControlBatch.to_json

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.UPFCControl.UPFCControlBatch.to_list

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatch.to_list
```

````

`````

`````{py:class} UPFCControlBatchProperties()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.BaseFreq
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.Like
```

````

````{py:attribute} UPFCList
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.UPFCList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.UPFCList
```

````

````{py:method} __contains__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__contains__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__delattr__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__delitem__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__dir__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__format__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__ge__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__getitem__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__getstate__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__gt__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__init__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__ior__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__iter__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__le__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__len__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__lt__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__ne__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__new__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__or__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__reduce__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__repr__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__reversed__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__ror__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__setitem__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__str__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.clear

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.copy

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.get

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.items

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.keys

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.pop

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.popitem

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.setdefault

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.update

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.UPFCControl.UPFCControlBatchProperties.values

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlBatchProperties.values
```

````

`````

`````{py:class} UPFCControlProperties()
:canonical: altdss.UPFCControl.UPFCControlProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFCControl.UPFCControlProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.BaseFreq
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFCControl.UPFCControlProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.UPFCControl.UPFCControlProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.Like
```

````

````{py:attribute} UPFCList
:canonical: altdss.UPFCControl.UPFCControlProperties.UPFCList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.UPFCList
```

````

````{py:method} __contains__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__contains__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__delattr__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__delitem__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__dir__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__format__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__ge__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__getattribute__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__getitem__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__getstate__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__gt__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__init__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__ior__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__iter__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__le__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__len__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__lt__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__ne__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__new__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__or__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__reduce__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__reduce_ex__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__repr__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__reversed__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__ror__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__setitem__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__sizeof__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__str__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.UPFCControl.UPFCControlProperties.__subclasshook__

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.UPFCControl.UPFCControlProperties.clear

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.UPFCControl.UPFCControlProperties.copy

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.copy
```

````

````{py:method} get()
:canonical: altdss.UPFCControl.UPFCControlProperties.get

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.get
```

````

````{py:method} items()
:canonical: altdss.UPFCControl.UPFCControlProperties.items

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.items
```

````

````{py:method} keys()
:canonical: altdss.UPFCControl.UPFCControlProperties.keys

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.UPFCControl.UPFCControlProperties.pop

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.UPFCControl.UPFCControlProperties.popitem

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.UPFCControl.UPFCControlProperties.setdefault

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.UPFCControl.UPFCControlProperties.update

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.update
```

````

````{py:method} values()
:canonical: altdss.UPFCControl.UPFCControlProperties.values

```{autodoc2-docstring} altdss.UPFCControl.UPFCControlProperties.values
```

````

`````
