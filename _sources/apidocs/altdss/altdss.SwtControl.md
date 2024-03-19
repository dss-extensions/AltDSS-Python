# {py:mod}`altdss.SwtControl`

```{py:module} altdss.SwtControl
```

```{autodoc2-docstring} altdss.SwtControl
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ISwtControl <altdss.SwtControl.ISwtControl>`
  - ```{autodoc2-docstring} altdss.SwtControl.ISwtControl
    :summary:
    ```
* - {py:obj}`SwtControl <altdss.SwtControl.SwtControl>`
  - ```{autodoc2-docstring} altdss.SwtControl.SwtControl
    :summary:
    ```
* - {py:obj}`SwtControlBatch <altdss.SwtControl.SwtControlBatch>`
  - ```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch
    :summary:
    ```
* - {py:obj}`SwtControlBatchProperties <altdss.SwtControl.SwtControlBatchProperties>`
  - ```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties
    :summary:
    ```
* - {py:obj}`SwtControlProperties <altdss.SwtControl.SwtControlProperties>`
  - ```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties
    :summary:
    ```
````

### API

`````{py:class} ISwtControl(iobj)
:canonical: altdss.SwtControl.ISwtControl

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.SwtControl.SwtControlBatch`

```{autodoc2-docstring} altdss.SwtControl.ISwtControl
```

````{py:attribute} BaseFreq
:canonical: altdss.SwtControl.ISwtControl.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.ISwtControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.ISwtControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.ISwtControl.Currents

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.ISwtControl.CurrentsMagAng

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.CurrentsMagAng
```

````

````{py:attribute} Delay
:canonical: altdss.SwtControl.ISwtControl.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.SwtControl.ISwtControl.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.SwtControl.ISwtControl.FullName

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.SwtControl.ISwtControl.GUID

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.ISwtControl.Handle

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.SwtControl.ISwtControl.HasOCPDevice

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.SwtControl.ISwtControl.HasSwitchControl

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.SwtControl.ISwtControl.HasVoltControl

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.SwtControl.ISwtControl.IsIsolated

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.SwtControl.ISwtControl.Like

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Like
```

````

````{py:attribute} Lock
:canonical: altdss.SwtControl.ISwtControl.Lock
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Lock
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.ISwtControl.Losses

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.SwtControl.ISwtControl.MaxCurrent

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.SwtControl.ISwtControl.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Name
```

````

````{py:attribute} Normal
:canonical: altdss.SwtControl.ISwtControl.Normal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.SwtControl.ISwtControl.Normal_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Normal_str
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.ISwtControl.NumConductors

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.ISwtControl.NumControllers

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.ISwtControl.NumPhases

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.ISwtControl.NumTerminals

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.SwtControl.ISwtControl.OCPDevice

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.ISwtControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.SwtControl.ISwtControl.OCPDeviceType

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.ISwtControl.PhaseLosses

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.ISwtControl.Powers

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Powers
```

````

````{py:method} Reset(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.SwtControl.ISwtControl.Reset

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Reset
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.ISwtControl.SeqCurrents

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.ISwtControl.SeqPowers

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.ISwtControl.SeqVoltages

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.SeqVoltages
```

````

````{py:attribute} State
:canonical: altdss.SwtControl.ISwtControl.State
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.State
```

````

````{py:attribute} State_str
:canonical: altdss.SwtControl.ISwtControl.State_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.SwtControl.ISwtControl.SwitchedObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.SwtControl.ISwtControl.SwitchedObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.SwtControl.ISwtControl.SwitchedTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.SwitchedTerm
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.ISwtControl.TotalPowers

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.ISwtControl.Voltages

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.ISwtControl.VoltagesMagAng

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.SwtControl.ISwtControl.__call__

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.SwtControl.ISwtControl.__contains__

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.SwtControl.ISwtControl.__getitem__

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.SwtControl.ISwtControl.__init__

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.SwtControl.ISwtControl.__iter__

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.SwtControl.ISwtControl.__len__

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.SwtControl.ISwtControl.batch

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.SwtControl.SwtControlBatchProperties]) -> altdss.SwtControl.SwtControlBatch
:canonical: altdss.SwtControl.ISwtControl.batch_new

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.SwtControl.ISwtControl.begin_edit

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.SwtControl.SwtControlBatchProperties]) -> altdss.SwtControl.SwtControlBatch
:canonical: altdss.SwtControl.ISwtControl.edit

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.SwtControl.ISwtControl.end_edit

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.SwtControl.ISwtControl.find

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.find
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.SwtControl.SwtControlProperties]) -> altdss.SwtControl.SwtControl
:canonical: altdss.SwtControl.ISwtControl.new

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.SwtControl.ISwtControl.to_json

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.to_json
```

````

````{py:method} to_list()
:canonical: altdss.SwtControl.ISwtControl.to_list

```{autodoc2-docstring} altdss.SwtControl.ISwtControl.to_list
```

````

`````

`````{py:class} SwtControl(api_util, ptr)
:canonical: altdss.SwtControl.SwtControl

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.SwtControl.SwtControl
```

````{py:attribute} BaseFreq
:canonical: altdss.SwtControl.SwtControl.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.SwtControl.SwtControl.Close

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.SwtControl.SwtControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.SwtControl.SwtControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControl.Currents

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Currents
```

````

````{py:attribute} Delay
:canonical: altdss.SwtControl.SwtControl.Delay
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Delay
```

````

````{py:attribute} DisplayName
:canonical: altdss.SwtControl.SwtControl.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.DisplayName
```

````

````{py:attribute} Enabled
:canonical: altdss.SwtControl.SwtControl.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Enabled
```

````

````{py:method} FullName() -> str
:canonical: altdss.SwtControl.SwtControl.FullName

```{autodoc2-docstring} altdss.SwtControl.SwtControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.SwtControl.SwtControl.GUID

```{autodoc2-docstring} altdss.SwtControl.SwtControl.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.SwtControl.SwtControl.Handle

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.SwtControl.SwtControl.HasOCPDevice

```{autodoc2-docstring} altdss.SwtControl.SwtControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.SwtControl.SwtControl.HasSwitchControl

```{autodoc2-docstring} altdss.SwtControl.SwtControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.SwtControl.SwtControl.HasVoltControl

```{autodoc2-docstring} altdss.SwtControl.SwtControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.SwtControl.SwtControl.IsIsolated

```{autodoc2-docstring} altdss.SwtControl.SwtControl.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.SwtControl.SwtControl.IsOpen

```{autodoc2-docstring} altdss.SwtControl.SwtControl.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.SwtControl.SwtControl.Like

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Like
```

````

````{py:attribute} Lock
:canonical: altdss.SwtControl.SwtControl.Lock
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Lock
```

````

````{py:method} Losses() -> complex
:canonical: altdss.SwtControl.SwtControl.Losses

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.SwtControl.SwtControl.MaxCurrent

```{autodoc2-docstring} altdss.SwtControl.SwtControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.SwtControl.SwtControl.Name
:type: str

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.SwtControl.NodeOrder

```{autodoc2-docstring} altdss.SwtControl.SwtControl.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.SwtControl.NodeRef

```{autodoc2-docstring} altdss.SwtControl.SwtControl.NodeRef
```

````

````{py:attribute} Normal
:canonical: altdss.SwtControl.SwtControl.Normal
:type: altdss.enums.SwtControlState
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.SwtControl.SwtControl.Normal_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Normal_str
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.SwtControl.SwtControl.NumConductors

```{autodoc2-docstring} altdss.SwtControl.SwtControl.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.SwtControl.SwtControl.NumControllers

```{autodoc2-docstring} altdss.SwtControl.SwtControl.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.SwtControl.SwtControl.NumPhases

```{autodoc2-docstring} altdss.SwtControl.SwtControl.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.SwtControl.SwtControl.NumTerminals

```{autodoc2-docstring} altdss.SwtControl.SwtControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.SwtControl.SwtControl.OCPDevice

```{autodoc2-docstring} altdss.SwtControl.SwtControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.SwtControl.SwtControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.SwtControl.SwtControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.SwtControl.SwtControl.OCPDeviceType

```{autodoc2-docstring} altdss.SwtControl.SwtControl.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.SwtControl.SwtControl.Open

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControl.PhaseLosses

```{autodoc2-docstring} altdss.SwtControl.SwtControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControl.Powers

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Powers
```

````

````{py:method} Reset(value: bool = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.SwtControl.SwtControl.Reset

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Reset
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.SwtControl.Residuals

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.SwtControl.SeqCurrents

```{autodoc2-docstring} altdss.SwtControl.SwtControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControl.SeqPowers

```{autodoc2-docstring} altdss.SwtControl.SwtControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.SwtControl.SeqVoltages

```{autodoc2-docstring} altdss.SwtControl.SwtControl.SeqVoltages
```

````

````{py:attribute} State
:canonical: altdss.SwtControl.SwtControl.State
:type: altdss.enums.SwtControlState
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.State
```

````

````{py:attribute} State_str
:canonical: altdss.SwtControl.SwtControl.State_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.SwtControl.SwtControl.SwitchedObj
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.SwtControl.SwtControl.SwitchedObj_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.SwtControl.SwtControl.SwitchedTerm
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControl.SwitchedTerm
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControl.TotalPowers

```{autodoc2-docstring} altdss.SwtControl.SwtControl.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControl.Voltages

```{autodoc2-docstring} altdss.SwtControl.SwtControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.SwtControl.VoltagesMagAng

```{autodoc2-docstring} altdss.SwtControl.SwtControl.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControl.YPrim

```{autodoc2-docstring} altdss.SwtControl.SwtControl.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.SwtControl.SwtControl.__hash__

```{autodoc2-docstring} altdss.SwtControl.SwtControl.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.SwtControl.SwtControl.__init__

```{autodoc2-docstring} altdss.SwtControl.SwtControl.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.SwtControl.SwtControl.__ne__

```{autodoc2-docstring} altdss.SwtControl.SwtControl.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.SwtControl.SwtControl.__repr__

```{autodoc2-docstring} altdss.SwtControl.SwtControl.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.SwtControl.SwtControl.begin_edit

```{autodoc2-docstring} altdss.SwtControl.SwtControl.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.SwtControl.SwtControlProperties]) -> altdss.SwtControl.SwtControl
:canonical: altdss.SwtControl.SwtControl.edit

```{autodoc2-docstring} altdss.SwtControl.SwtControl.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.SwtControl.SwtControl.end_edit

```{autodoc2-docstring} altdss.SwtControl.SwtControl.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.SwtControl.SwtControl.to_json

```{autodoc2-docstring} altdss.SwtControl.SwtControl.to_json
```

````

`````

`````{py:class} SwtControlBatch(api_util, **kwargs)
:canonical: altdss.SwtControl.SwtControlBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.SwtControl.SwtControlBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControlBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControlBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControlBatch.Currents

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.SwtControlBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.CurrentsMagAng
```

````

````{py:attribute} Delay
:canonical: altdss.SwtControl.SwtControlBatch.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.SwtControl.SwtControlBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.SwtControl.SwtControlBatch.FullName

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.SwtControl.SwtControlBatch.GUID

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.SwtControlBatch.Handle

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.SwtControl.SwtControlBatch.HasOCPDevice

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.SwtControl.SwtControlBatch.HasSwitchControl

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.SwtControl.SwtControlBatch.HasVoltControl

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.SwtControl.SwtControlBatch.IsIsolated

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.SwtControl.SwtControlBatch.Like

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Like
```

````

````{py:attribute} Lock
:canonical: altdss.SwtControl.SwtControlBatch.Lock
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Lock
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControlBatch.Losses

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.SwtControl.SwtControlBatch.MaxCurrent

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.SwtControl.SwtControlBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Name
```

````

````{py:attribute} Normal
:canonical: altdss.SwtControl.SwtControlBatch.Normal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.SwtControl.SwtControlBatch.Normal_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Normal_str
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.SwtControlBatch.NumConductors

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.SwtControlBatch.NumControllers

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.SwtControlBatch.NumPhases

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.SwtControlBatch.NumTerminals

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.SwtControl.SwtControlBatch.OCPDevice

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.SwtControl.SwtControlBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.SwtControl.SwtControlBatch.OCPDeviceType

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControlBatch.PhaseLosses

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControlBatch.Powers

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Powers
```

````

````{py:method} Reset(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.SwtControl.SwtControlBatch.Reset

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Reset
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.SwtControlBatch.SeqCurrents

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControlBatch.SeqPowers

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.SwtControlBatch.SeqVoltages

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.SeqVoltages
```

````

````{py:attribute} State
:canonical: altdss.SwtControl.SwtControlBatch.State
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.State
```

````

````{py:attribute} State_str
:canonical: altdss.SwtControl.SwtControlBatch.State_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.SwtControl.SwtControlBatch.SwitchedObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.SwtControl.SwtControlBatch.SwitchedObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.SwtControl.SwtControlBatch.SwitchedTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.SwitchedTerm
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControlBatch.TotalPowers

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.SwtControl.SwtControlBatch.Voltages

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.SwtControl.SwtControlBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.SwtControl.SwtControlBatch.__call__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.SwtControl.SwtControlBatch.__getitem__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.SwtControl.SwtControlBatch.__init__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.SwtControl.SwtControlBatch.__iter__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.SwtControl.SwtControlBatch.__len__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.SwtControl.SwtControlBatch.batch

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.SwtControl.SwtControlBatch.begin_edit

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.SwtControl.SwtControlBatchProperties]) -> altdss.SwtControl.SwtControlBatch
:canonical: altdss.SwtControl.SwtControlBatch.edit

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.SwtControl.SwtControlBatch.end_edit

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.SwtControl.SwtControlBatch.to_json

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.SwtControl.SwtControlBatch.to_list

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatch.to_list
```

````

`````

`````{py:class} SwtControlBatchProperties()
:canonical: altdss.SwtControl.SwtControlBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.SwtControl.SwtControlBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.BaseFreq
```

````

````{py:attribute} Delay
:canonical: altdss.SwtControl.SwtControlBatchProperties.Delay
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.SwtControl.SwtControlBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.SwtControl.SwtControlBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.Like
```

````

````{py:attribute} Lock
:canonical: altdss.SwtControl.SwtControlBatchProperties.Lock
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.Lock
```

````

````{py:attribute} Normal
:canonical: altdss.SwtControl.SwtControlBatchProperties.Normal
:type: typing.Union[typing.AnyStr, int, altdss.enums.SwtControlState, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.SwtControlState], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.Normal
```

````

````{py:attribute} Reset
:canonical: altdss.SwtControl.SwtControlBatchProperties.Reset
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.Reset
```

````

````{py:attribute} State
:canonical: altdss.SwtControl.SwtControlBatchProperties.State
:type: typing.Union[typing.AnyStr, int, altdss.enums.SwtControlState, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.SwtControlState], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.State
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.SwtControl.SwtControlBatchProperties.SwitchedObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.SwitchedObj
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.SwtControl.SwtControlBatchProperties.SwitchedTerm
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.SwitchedTerm
```

````

````{py:method} __contains__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__contains__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__delattr__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__delitem__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__dir__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__format__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__ge__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__getitem__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__getstate__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__gt__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__init__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__ior__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__iter__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__le__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__len__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__lt__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__ne__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__new__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__or__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__reduce__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__repr__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__reversed__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__ror__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__setitem__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__str__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.SwtControl.SwtControlBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.SwtControl.SwtControlBatchProperties.clear

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.SwtControl.SwtControlBatchProperties.copy

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.SwtControl.SwtControlBatchProperties.get

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.SwtControl.SwtControlBatchProperties.items

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.SwtControl.SwtControlBatchProperties.keys

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.SwtControl.SwtControlBatchProperties.pop

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.SwtControl.SwtControlBatchProperties.popitem

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.SwtControl.SwtControlBatchProperties.setdefault

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.SwtControl.SwtControlBatchProperties.update

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.SwtControl.SwtControlBatchProperties.values

```{autodoc2-docstring} altdss.SwtControl.SwtControlBatchProperties.values
```

````

`````

`````{py:class} SwtControlProperties()
:canonical: altdss.SwtControl.SwtControlProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.SwtControl.SwtControlProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.BaseFreq
```

````

````{py:attribute} Delay
:canonical: altdss.SwtControl.SwtControlProperties.Delay
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.SwtControl.SwtControlProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.SwtControl.SwtControlProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.Like
```

````

````{py:attribute} Lock
:canonical: altdss.SwtControl.SwtControlProperties.Lock
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.Lock
```

````

````{py:attribute} Normal
:canonical: altdss.SwtControl.SwtControlProperties.Normal
:type: typing.Union[typing.AnyStr, int, altdss.enums.SwtControlState]
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.Normal
```

````

````{py:attribute} Reset
:canonical: altdss.SwtControl.SwtControlProperties.Reset
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.Reset
```

````

````{py:attribute} State
:canonical: altdss.SwtControl.SwtControlProperties.State
:type: typing.Union[typing.AnyStr, int, altdss.enums.SwtControlState]
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.State
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.SwtControl.SwtControlProperties.SwitchedObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.SwitchedObj
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.SwtControl.SwtControlProperties.SwitchedTerm
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.SwitchedTerm
```

````

````{py:method} __contains__()
:canonical: altdss.SwtControl.SwtControlProperties.__contains__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.SwtControl.SwtControlProperties.__delattr__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.SwtControl.SwtControlProperties.__delitem__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.SwtControl.SwtControlProperties.__dir__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.SwtControl.SwtControlProperties.__format__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.SwtControl.SwtControlProperties.__ge__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.SwtControl.SwtControlProperties.__getattribute__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.SwtControl.SwtControlProperties.__getitem__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.SwtControl.SwtControlProperties.__getstate__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.SwtControl.SwtControlProperties.__gt__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.SwtControl.SwtControlProperties.__init__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.SwtControl.SwtControlProperties.__ior__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.SwtControl.SwtControlProperties.__iter__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.SwtControl.SwtControlProperties.__le__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.SwtControl.SwtControlProperties.__len__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.SwtControl.SwtControlProperties.__lt__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.SwtControl.SwtControlProperties.__ne__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.SwtControl.SwtControlProperties.__new__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.SwtControl.SwtControlProperties.__or__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.SwtControl.SwtControlProperties.__reduce__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.SwtControl.SwtControlProperties.__reduce_ex__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.SwtControl.SwtControlProperties.__repr__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.SwtControl.SwtControlProperties.__reversed__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.SwtControl.SwtControlProperties.__ror__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.SwtControl.SwtControlProperties.__setitem__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.SwtControl.SwtControlProperties.__sizeof__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.SwtControl.SwtControlProperties.__str__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.SwtControl.SwtControlProperties.__subclasshook__

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.SwtControl.SwtControlProperties.clear

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.SwtControl.SwtControlProperties.copy

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.copy
```

````

````{py:method} get()
:canonical: altdss.SwtControl.SwtControlProperties.get

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.get
```

````

````{py:method} items()
:canonical: altdss.SwtControl.SwtControlProperties.items

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.items
```

````

````{py:method} keys()
:canonical: altdss.SwtControl.SwtControlProperties.keys

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.SwtControl.SwtControlProperties.pop

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.SwtControl.SwtControlProperties.popitem

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.SwtControl.SwtControlProperties.setdefault

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.SwtControl.SwtControlProperties.update

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.update
```

````

````{py:method} values()
:canonical: altdss.SwtControl.SwtControlProperties.values

```{autodoc2-docstring} altdss.SwtControl.SwtControlProperties.values
```

````

`````
