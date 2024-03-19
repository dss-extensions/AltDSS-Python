# {py:mod}`altdss.Recloser`

```{py:module} altdss.Recloser
```

```{autodoc2-docstring} altdss.Recloser
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IRecloser <altdss.Recloser.IRecloser>`
  - ```{autodoc2-docstring} altdss.Recloser.IRecloser
    :summary:
    ```
* - {py:obj}`Recloser <altdss.Recloser.Recloser>`
  - ```{autodoc2-docstring} altdss.Recloser.Recloser
    :summary:
    ```
* - {py:obj}`RecloserBatch <altdss.Recloser.RecloserBatch>`
  - ```{autodoc2-docstring} altdss.Recloser.RecloserBatch
    :summary:
    ```
* - {py:obj}`RecloserBatchProperties <altdss.Recloser.RecloserBatchProperties>`
  - ```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties
    :summary:
    ```
* - {py:obj}`RecloserProperties <altdss.Recloser.RecloserProperties>`
  - ```{autodoc2-docstring} altdss.Recloser.RecloserProperties
    :summary:
    ```
````

### API

`````{py:class} IRecloser(iobj)
:canonical: altdss.Recloser.IRecloser

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Recloser.RecloserBatch`

```{autodoc2-docstring} altdss.Recloser.IRecloser
```

````{py:attribute} BaseFreq
:canonical: altdss.Recloser.IRecloser.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.IRecloser.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Recloser.IRecloser.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.IRecloser.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Recloser.IRecloser.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.IRecloser.Currents

```{autodoc2-docstring} altdss.Recloser.IRecloser.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Recloser.IRecloser.CurrentsMagAng

```{autodoc2-docstring} altdss.Recloser.IRecloser.CurrentsMagAng
```

````

````{py:attribute} Delay
:canonical: altdss.Recloser.IRecloser.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.Recloser.IRecloser.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Recloser.IRecloser.FullName

```{autodoc2-docstring} altdss.Recloser.IRecloser.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Recloser.IRecloser.GUID

```{autodoc2-docstring} altdss.Recloser.IRecloser.GUID
```

````

````{py:attribute} GroundDelayed
:canonical: altdss.Recloser.IRecloser.GroundDelayed
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.GroundDelayed
```

````

````{py:attribute} GroundDelayed_str
:canonical: altdss.Recloser.IRecloser.GroundDelayed_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.GroundDelayed_str
```

````

````{py:attribute} GroundFast
:canonical: altdss.Recloser.IRecloser.GroundFast
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.GroundFast
```

````

````{py:attribute} GroundFast_str
:canonical: altdss.Recloser.IRecloser.GroundFast_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.GroundFast_str
```

````

````{py:attribute} GroundInst
:canonical: altdss.Recloser.IRecloser.GroundInst
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Recloser.IRecloser.GroundTrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.GroundTrip
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Recloser.IRecloser.Handle

```{autodoc2-docstring} altdss.Recloser.IRecloser.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Recloser.IRecloser.HasOCPDevice

```{autodoc2-docstring} altdss.Recloser.IRecloser.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Recloser.IRecloser.HasSwitchControl

```{autodoc2-docstring} altdss.Recloser.IRecloser.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Recloser.IRecloser.HasVoltControl

```{autodoc2-docstring} altdss.Recloser.IRecloser.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Recloser.IRecloser.IsIsolated

```{autodoc2-docstring} altdss.Recloser.IRecloser.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Recloser.IRecloser.Like

```{autodoc2-docstring} altdss.Recloser.IRecloser.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.IRecloser.Losses

```{autodoc2-docstring} altdss.Recloser.IRecloser.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Recloser.IRecloser.MaxCurrent

```{autodoc2-docstring} altdss.Recloser.IRecloser.MaxCurrent
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Recloser.IRecloser.MonitoredObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.MonitoredObj
```

````

````{py:attribute} MonitoredObj_str
:canonical: altdss.Recloser.IRecloser.MonitoredObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.MonitoredObj_str
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Recloser.IRecloser.MonitoredTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.MonitoredTerm
```

````

````{py:property} Name
:canonical: altdss.Recloser.IRecloser.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Recloser.IRecloser.Name
```

````

````{py:attribute} Normal
:canonical: altdss.Recloser.IRecloser.Normal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.Recloser.IRecloser.Normal_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.Normal_str
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Recloser.IRecloser.NumConductors

```{autodoc2-docstring} altdss.Recloser.IRecloser.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Recloser.IRecloser.NumControllers

```{autodoc2-docstring} altdss.Recloser.IRecloser.NumControllers
```

````

````{py:attribute} NumFast
:canonical: altdss.Recloser.IRecloser.NumFast
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.NumFast
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Recloser.IRecloser.NumPhases

```{autodoc2-docstring} altdss.Recloser.IRecloser.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Recloser.IRecloser.NumTerminals

```{autodoc2-docstring} altdss.Recloser.IRecloser.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Recloser.IRecloser.OCPDevice

```{autodoc2-docstring} altdss.Recloser.IRecloser.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Recloser.IRecloser.OCPDeviceIndex

```{autodoc2-docstring} altdss.Recloser.IRecloser.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Recloser.IRecloser.OCPDeviceType

```{autodoc2-docstring} altdss.Recloser.IRecloser.OCPDeviceType
```

````

````{py:attribute} PhaseDelayed
:canonical: altdss.Recloser.IRecloser.PhaseDelayed
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.PhaseDelayed
```

````

````{py:attribute} PhaseDelayed_str
:canonical: altdss.Recloser.IRecloser.PhaseDelayed_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.PhaseDelayed_str
```

````

````{py:attribute} PhaseFast
:canonical: altdss.Recloser.IRecloser.PhaseFast
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.PhaseFast
```

````

````{py:attribute} PhaseFast_str
:canonical: altdss.Recloser.IRecloser.PhaseFast_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.PhaseFast_str
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Recloser.IRecloser.PhaseInst
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.PhaseInst
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.IRecloser.PhaseLosses

```{autodoc2-docstring} altdss.Recloser.IRecloser.PhaseLosses
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Recloser.IRecloser.PhaseTrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.PhaseTrip
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.IRecloser.Powers

```{autodoc2-docstring} altdss.Recloser.IRecloser.Powers
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Recloser.IRecloser.RecloseIntervals
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Recloser.IRecloser.Reset
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.Reset
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Recloser.IRecloser.SeqCurrents

```{autodoc2-docstring} altdss.Recloser.IRecloser.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.IRecloser.SeqPowers

```{autodoc2-docstring} altdss.Recloser.IRecloser.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Recloser.IRecloser.SeqVoltages

```{autodoc2-docstring} altdss.Recloser.IRecloser.SeqVoltages
```

````

````{py:attribute} Shots
:canonical: altdss.Recloser.IRecloser.Shots
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.Shots
```

````

````{py:attribute} State
:canonical: altdss.Recloser.IRecloser.State
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.State
```

````

````{py:attribute} State_str
:canonical: altdss.Recloser.IRecloser.State_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Recloser.IRecloser.SwitchedObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.Recloser.IRecloser.SwitchedObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Recloser.IRecloser.SwitchedTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.SwitchedTerm
```

````

````{py:attribute} TDGrDelayed
:canonical: altdss.Recloser.IRecloser.TDGrDelayed
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.TDGrDelayed
```

````

````{py:attribute} TDGrFast
:canonical: altdss.Recloser.IRecloser.TDGrFast
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.TDGrFast
```

````

````{py:attribute} TDPhDelayed
:canonical: altdss.Recloser.IRecloser.TDPhDelayed
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.TDPhDelayed
```

````

````{py:attribute} TDPhFast
:canonical: altdss.Recloser.IRecloser.TDPhFast
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.IRecloser.TDPhFast
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.IRecloser.TotalPowers

```{autodoc2-docstring} altdss.Recloser.IRecloser.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.IRecloser.Voltages

```{autodoc2-docstring} altdss.Recloser.IRecloser.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Recloser.IRecloser.VoltagesMagAng

```{autodoc2-docstring} altdss.Recloser.IRecloser.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.Recloser.IRecloser.__call__

```{autodoc2-docstring} altdss.Recloser.IRecloser.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Recloser.IRecloser.__contains__

```{autodoc2-docstring} altdss.Recloser.IRecloser.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Recloser.IRecloser.__getitem__

```{autodoc2-docstring} altdss.Recloser.IRecloser.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Recloser.IRecloser.__init__

```{autodoc2-docstring} altdss.Recloser.IRecloser.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Recloser.IRecloser.__iter__

```{autodoc2-docstring} altdss.Recloser.IRecloser.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Recloser.IRecloser.__len__

```{autodoc2-docstring} altdss.Recloser.IRecloser.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Recloser.IRecloser.batch

```{autodoc2-docstring} altdss.Recloser.IRecloser.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.Recloser.RecloserBatchProperties]) -> altdss.Recloser.RecloserBatch
:canonical: altdss.Recloser.IRecloser.batch_new

```{autodoc2-docstring} altdss.Recloser.IRecloser.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Recloser.IRecloser.begin_edit

```{autodoc2-docstring} altdss.Recloser.IRecloser.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Recloser.RecloserBatchProperties]) -> altdss.Recloser.RecloserBatch
:canonical: altdss.Recloser.IRecloser.edit

```{autodoc2-docstring} altdss.Recloser.IRecloser.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Recloser.IRecloser.end_edit

```{autodoc2-docstring} altdss.Recloser.IRecloser.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Recloser.IRecloser.find

```{autodoc2-docstring} altdss.Recloser.IRecloser.find
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.Recloser.RecloserProperties]) -> altdss.Recloser.Recloser
:canonical: altdss.Recloser.IRecloser.new

```{autodoc2-docstring} altdss.Recloser.IRecloser.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Recloser.IRecloser.to_json

```{autodoc2-docstring} altdss.Recloser.IRecloser.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Recloser.IRecloser.to_list

```{autodoc2-docstring} altdss.Recloser.IRecloser.to_list
```

````

`````

`````{py:class} Recloser(api_util, ptr)
:canonical: altdss.Recloser.Recloser

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.Recloser.Recloser
```

````{py:attribute} BaseFreq
:canonical: altdss.Recloser.Recloser.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Recloser.Recloser.Close

```{autodoc2-docstring} altdss.Recloser.Recloser.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.Recloser.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Recloser.Recloser.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.Recloser.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Recloser.Recloser.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.Recloser.Currents

```{autodoc2-docstring} altdss.Recloser.Recloser.Currents
```

````

````{py:attribute} Delay
:canonical: altdss.Recloser.Recloser.Delay
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.Delay
```

````

````{py:attribute} DisplayName
:canonical: altdss.Recloser.Recloser.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.DisplayName
```

````

````{py:attribute} Enabled
:canonical: altdss.Recloser.Recloser.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.Enabled
```

````

````{py:method} FullName() -> str
:canonical: altdss.Recloser.Recloser.FullName

```{autodoc2-docstring} altdss.Recloser.Recloser.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Recloser.Recloser.GUID

```{autodoc2-docstring} altdss.Recloser.Recloser.GUID
```

````

````{py:attribute} GroundDelayed
:canonical: altdss.Recloser.Recloser.GroundDelayed
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.GroundDelayed
```

````

````{py:attribute} GroundDelayed_str
:canonical: altdss.Recloser.Recloser.GroundDelayed_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.GroundDelayed_str
```

````

````{py:attribute} GroundFast
:canonical: altdss.Recloser.Recloser.GroundFast
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.GroundFast
```

````

````{py:attribute} GroundFast_str
:canonical: altdss.Recloser.Recloser.GroundFast_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.GroundFast_str
```

````

````{py:attribute} GroundInst
:canonical: altdss.Recloser.Recloser.GroundInst
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Recloser.Recloser.GroundTrip
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.GroundTrip
```

````

````{py:method} Handle() -> int
:canonical: altdss.Recloser.Recloser.Handle

```{autodoc2-docstring} altdss.Recloser.Recloser.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Recloser.Recloser.HasOCPDevice

```{autodoc2-docstring} altdss.Recloser.Recloser.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Recloser.Recloser.HasSwitchControl

```{autodoc2-docstring} altdss.Recloser.Recloser.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Recloser.Recloser.HasVoltControl

```{autodoc2-docstring} altdss.Recloser.Recloser.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Recloser.Recloser.IsIsolated

```{autodoc2-docstring} altdss.Recloser.Recloser.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Recloser.Recloser.IsOpen

```{autodoc2-docstring} altdss.Recloser.Recloser.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Recloser.Recloser.Like

```{autodoc2-docstring} altdss.Recloser.Recloser.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Recloser.Recloser.Losses

```{autodoc2-docstring} altdss.Recloser.Recloser.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Recloser.Recloser.MaxCurrent

```{autodoc2-docstring} altdss.Recloser.Recloser.MaxCurrent
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Recloser.Recloser.MonitoredObj
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.MonitoredObj
```

````

````{py:attribute} MonitoredObj_str
:canonical: altdss.Recloser.Recloser.MonitoredObj_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.MonitoredObj_str
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Recloser.Recloser.MonitoredTerm
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.MonitoredTerm
```

````

````{py:property} Name
:canonical: altdss.Recloser.Recloser.Name
:type: str

```{autodoc2-docstring} altdss.Recloser.Recloser.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Recloser.Recloser.NodeOrder

```{autodoc2-docstring} altdss.Recloser.Recloser.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Recloser.Recloser.NodeRef

```{autodoc2-docstring} altdss.Recloser.Recloser.NodeRef
```

````

````{py:attribute} Normal
:canonical: altdss.Recloser.Recloser.Normal
:type: altdss.enums.RecloserState
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.Recloser.Recloser.Normal_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.Normal_str
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Recloser.Recloser.NumConductors

```{autodoc2-docstring} altdss.Recloser.Recloser.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Recloser.Recloser.NumControllers

```{autodoc2-docstring} altdss.Recloser.Recloser.NumControllers
```

````

````{py:attribute} NumFast
:canonical: altdss.Recloser.Recloser.NumFast
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.NumFast
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Recloser.Recloser.NumPhases

```{autodoc2-docstring} altdss.Recloser.Recloser.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Recloser.Recloser.NumTerminals

```{autodoc2-docstring} altdss.Recloser.Recloser.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Recloser.Recloser.OCPDevice

```{autodoc2-docstring} altdss.Recloser.Recloser.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Recloser.Recloser.OCPDeviceIndex

```{autodoc2-docstring} altdss.Recloser.Recloser.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Recloser.Recloser.OCPDeviceType

```{autodoc2-docstring} altdss.Recloser.Recloser.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Recloser.Recloser.Open

```{autodoc2-docstring} altdss.Recloser.Recloser.Open
```

````

````{py:attribute} PhaseDelayed
:canonical: altdss.Recloser.Recloser.PhaseDelayed
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.PhaseDelayed
```

````

````{py:attribute} PhaseDelayed_str
:canonical: altdss.Recloser.Recloser.PhaseDelayed_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.PhaseDelayed_str
```

````

````{py:attribute} PhaseFast
:canonical: altdss.Recloser.Recloser.PhaseFast
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.PhaseFast
```

````

````{py:attribute} PhaseFast_str
:canonical: altdss.Recloser.Recloser.PhaseFast_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.PhaseFast_str
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Recloser.Recloser.PhaseInst
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.PhaseInst
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.Recloser.PhaseLosses

```{autodoc2-docstring} altdss.Recloser.Recloser.PhaseLosses
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Recloser.Recloser.PhaseTrip
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.PhaseTrip
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.Recloser.Powers

```{autodoc2-docstring} altdss.Recloser.Recloser.Powers
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Recloser.Recloser.RecloseIntervals
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Recloser.Recloser.Reset
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.Reset
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Recloser.Recloser.Residuals

```{autodoc2-docstring} altdss.Recloser.Recloser.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Recloser.Recloser.SeqCurrents

```{autodoc2-docstring} altdss.Recloser.Recloser.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.Recloser.SeqPowers

```{autodoc2-docstring} altdss.Recloser.Recloser.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Recloser.Recloser.SeqVoltages

```{autodoc2-docstring} altdss.Recloser.Recloser.SeqVoltages
```

````

````{py:attribute} Shots
:canonical: altdss.Recloser.Recloser.Shots
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.Shots
```

````

````{py:attribute} State
:canonical: altdss.Recloser.Recloser.State
:type: altdss.enums.RecloserState
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.State
```

````

````{py:attribute} State_str
:canonical: altdss.Recloser.Recloser.State_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Recloser.Recloser.SwitchedObj
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.Recloser.Recloser.SwitchedObj_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Recloser.Recloser.SwitchedTerm
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.SwitchedTerm
```

````

````{py:attribute} TDGrDelayed
:canonical: altdss.Recloser.Recloser.TDGrDelayed
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.TDGrDelayed
```

````

````{py:attribute} TDGrFast
:canonical: altdss.Recloser.Recloser.TDGrFast
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.TDGrFast
```

````

````{py:attribute} TDPhDelayed
:canonical: altdss.Recloser.Recloser.TDPhDelayed
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.TDPhDelayed
```

````

````{py:attribute} TDPhFast
:canonical: altdss.Recloser.Recloser.TDPhFast
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.Recloser.TDPhFast
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.Recloser.TotalPowers

```{autodoc2-docstring} altdss.Recloser.Recloser.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.Recloser.Voltages

```{autodoc2-docstring} altdss.Recloser.Recloser.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Recloser.Recloser.VoltagesMagAng

```{autodoc2-docstring} altdss.Recloser.Recloser.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.Recloser.YPrim

```{autodoc2-docstring} altdss.Recloser.Recloser.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.Recloser.Recloser.__hash__

```{autodoc2-docstring} altdss.Recloser.Recloser.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Recloser.Recloser.__init__

```{autodoc2-docstring} altdss.Recloser.Recloser.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Recloser.Recloser.__ne__

```{autodoc2-docstring} altdss.Recloser.Recloser.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Recloser.Recloser.__repr__

```{autodoc2-docstring} altdss.Recloser.Recloser.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Recloser.Recloser.begin_edit

```{autodoc2-docstring} altdss.Recloser.Recloser.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Recloser.RecloserProperties]) -> altdss.Recloser.Recloser
:canonical: altdss.Recloser.Recloser.edit

```{autodoc2-docstring} altdss.Recloser.Recloser.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Recloser.Recloser.end_edit

```{autodoc2-docstring} altdss.Recloser.Recloser.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Recloser.Recloser.to_json

```{autodoc2-docstring} altdss.Recloser.Recloser.to_json
```

````

`````

`````{py:class} RecloserBatch(api_util, **kwargs)
:canonical: altdss.Recloser.RecloserBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.Recloser.RecloserBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.Recloser.RecloserBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.RecloserBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.RecloserBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.RecloserBatch.Currents

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Recloser.RecloserBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.CurrentsMagAng
```

````

````{py:attribute} Delay
:canonical: altdss.Recloser.RecloserBatch.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.Recloser.RecloserBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Recloser.RecloserBatch.FullName

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Recloser.RecloserBatch.GUID

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.GUID
```

````

````{py:attribute} GroundDelayed
:canonical: altdss.Recloser.RecloserBatch.GroundDelayed
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.GroundDelayed
```

````

````{py:attribute} GroundDelayed_str
:canonical: altdss.Recloser.RecloserBatch.GroundDelayed_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.GroundDelayed_str
```

````

````{py:attribute} GroundFast
:canonical: altdss.Recloser.RecloserBatch.GroundFast
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.GroundFast
```

````

````{py:attribute} GroundFast_str
:canonical: altdss.Recloser.RecloserBatch.GroundFast_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.GroundFast_str
```

````

````{py:attribute} GroundInst
:canonical: altdss.Recloser.RecloserBatch.GroundInst
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Recloser.RecloserBatch.GroundTrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.GroundTrip
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Recloser.RecloserBatch.Handle

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Recloser.RecloserBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Recloser.RecloserBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Recloser.RecloserBatch.HasVoltControl

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Recloser.RecloserBatch.IsIsolated

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Recloser.RecloserBatch.Like

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.RecloserBatch.Losses

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Recloser.RecloserBatch.MaxCurrent

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.MaxCurrent
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Recloser.RecloserBatch.MonitoredObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.MonitoredObj
```

````

````{py:attribute} MonitoredObj_str
:canonical: altdss.Recloser.RecloserBatch.MonitoredObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.MonitoredObj_str
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Recloser.RecloserBatch.MonitoredTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.MonitoredTerm
```

````

````{py:property} Name
:canonical: altdss.Recloser.RecloserBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Name
```

````

````{py:attribute} Normal
:canonical: altdss.Recloser.RecloserBatch.Normal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.Recloser.RecloserBatch.Normal_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Normal_str
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Recloser.RecloserBatch.NumConductors

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Recloser.RecloserBatch.NumControllers

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.NumControllers
```

````

````{py:attribute} NumFast
:canonical: altdss.Recloser.RecloserBatch.NumFast
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.NumFast
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Recloser.RecloserBatch.NumPhases

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Recloser.RecloserBatch.NumTerminals

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Recloser.RecloserBatch.OCPDevice

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Recloser.RecloserBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Recloser.RecloserBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.OCPDeviceType
```

````

````{py:attribute} PhaseDelayed
:canonical: altdss.Recloser.RecloserBatch.PhaseDelayed
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.PhaseDelayed
```

````

````{py:attribute} PhaseDelayed_str
:canonical: altdss.Recloser.RecloserBatch.PhaseDelayed_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.PhaseDelayed_str
```

````

````{py:attribute} PhaseFast
:canonical: altdss.Recloser.RecloserBatch.PhaseFast
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.PhaseFast
```

````

````{py:attribute} PhaseFast_str
:canonical: altdss.Recloser.RecloserBatch.PhaseFast_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.PhaseFast_str
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Recloser.RecloserBatch.PhaseInst
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.PhaseInst
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.RecloserBatch.PhaseLosses

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.PhaseLosses
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Recloser.RecloserBatch.PhaseTrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.PhaseTrip
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.RecloserBatch.Powers

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Powers
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Recloser.RecloserBatch.RecloseIntervals
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Recloser.RecloserBatch.Reset
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Reset
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Recloser.RecloserBatch.SeqCurrents

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.RecloserBatch.SeqPowers

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Recloser.RecloserBatch.SeqVoltages

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.SeqVoltages
```

````

````{py:attribute} Shots
:canonical: altdss.Recloser.RecloserBatch.Shots
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Shots
```

````

````{py:attribute} State
:canonical: altdss.Recloser.RecloserBatch.State
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.State
```

````

````{py:attribute} State_str
:canonical: altdss.Recloser.RecloserBatch.State_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Recloser.RecloserBatch.SwitchedObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.Recloser.RecloserBatch.SwitchedObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Recloser.RecloserBatch.SwitchedTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.SwitchedTerm
```

````

````{py:attribute} TDGrDelayed
:canonical: altdss.Recloser.RecloserBatch.TDGrDelayed
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.TDGrDelayed
```

````

````{py:attribute} TDGrFast
:canonical: altdss.Recloser.RecloserBatch.TDGrFast
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.TDGrFast
```

````

````{py:attribute} TDPhDelayed
:canonical: altdss.Recloser.RecloserBatch.TDPhDelayed
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.TDPhDelayed
```

````

````{py:attribute} TDPhFast
:canonical: altdss.Recloser.RecloserBatch.TDPhFast
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.TDPhFast
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.RecloserBatch.TotalPowers

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Recloser.RecloserBatch.Voltages

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Recloser.RecloserBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.Recloser.RecloserBatch.__call__

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Recloser.RecloserBatch.__getitem__

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Recloser.RecloserBatch.__init__

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Recloser.RecloserBatch.__iter__

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Recloser.RecloserBatch.__len__

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Recloser.RecloserBatch.batch

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Recloser.RecloserBatch.begin_edit

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Recloser.RecloserBatchProperties]) -> altdss.Recloser.RecloserBatch
:canonical: altdss.Recloser.RecloserBatch.edit

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Recloser.RecloserBatch.end_edit

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Recloser.RecloserBatch.to_json

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Recloser.RecloserBatch.to_list

```{autodoc2-docstring} altdss.Recloser.RecloserBatch.to_list
```

````

`````

`````{py:class} RecloserBatchProperties()
:canonical: altdss.Recloser.RecloserBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Recloser.RecloserBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.BaseFreq
```

````

````{py:attribute} Delay
:canonical: altdss.Recloser.RecloserBatchProperties.Delay
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.Recloser.RecloserBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.Enabled
```

````

````{py:attribute} GroundDelayed
:canonical: altdss.Recloser.RecloserBatchProperties.GroundDelayed
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.GroundDelayed
```

````

````{py:attribute} GroundFast
:canonical: altdss.Recloser.RecloserBatchProperties.GroundFast
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.GroundFast
```

````

````{py:attribute} GroundInst
:canonical: altdss.Recloser.RecloserBatchProperties.GroundInst
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Recloser.RecloserBatchProperties.GroundTrip
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.GroundTrip
```

````

````{py:attribute} Like
:canonical: altdss.Recloser.RecloserBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.Like
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Recloser.RecloserBatchProperties.MonitoredObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.MonitoredObj
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Recloser.RecloserBatchProperties.MonitoredTerm
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.MonitoredTerm
```

````

````{py:attribute} Normal
:canonical: altdss.Recloser.RecloserBatchProperties.Normal
:type: typing.Union[typing.AnyStr, int, altdss.enums.RecloserState, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.RecloserState], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.Normal
```

````

````{py:attribute} NumFast
:canonical: altdss.Recloser.RecloserBatchProperties.NumFast
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.NumFast
```

````

````{py:attribute} PhaseDelayed
:canonical: altdss.Recloser.RecloserBatchProperties.PhaseDelayed
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.PhaseDelayed
```

````

````{py:attribute} PhaseFast
:canonical: altdss.Recloser.RecloserBatchProperties.PhaseFast
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.PhaseFast
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Recloser.RecloserBatchProperties.PhaseInst
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.PhaseInst
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Recloser.RecloserBatchProperties.PhaseTrip
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.PhaseTrip
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Recloser.RecloserBatchProperties.RecloseIntervals
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Recloser.RecloserBatchProperties.Reset
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.Reset
```

````

````{py:attribute} Shots
:canonical: altdss.Recloser.RecloserBatchProperties.Shots
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.Shots
```

````

````{py:attribute} State
:canonical: altdss.Recloser.RecloserBatchProperties.State
:type: typing.Union[typing.AnyStr, int, altdss.enums.RecloserState, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.RecloserState], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.State
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Recloser.RecloserBatchProperties.SwitchedObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.SwitchedObj
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Recloser.RecloserBatchProperties.SwitchedTerm
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.SwitchedTerm
```

````

````{py:attribute} TDGrDelayed
:canonical: altdss.Recloser.RecloserBatchProperties.TDGrDelayed
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.TDGrDelayed
```

````

````{py:attribute} TDGrFast
:canonical: altdss.Recloser.RecloserBatchProperties.TDGrFast
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.TDGrFast
```

````

````{py:attribute} TDPhDelayed
:canonical: altdss.Recloser.RecloserBatchProperties.TDPhDelayed
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.TDPhDelayed
```

````

````{py:attribute} TDPhFast
:canonical: altdss.Recloser.RecloserBatchProperties.TDPhFast
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.TDPhFast
```

````

````{py:method} __contains__()
:canonical: altdss.Recloser.RecloserBatchProperties.__contains__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Recloser.RecloserBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Recloser.RecloserBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Recloser.RecloserBatchProperties.__dir__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Recloser.RecloserBatchProperties.__format__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Recloser.RecloserBatchProperties.__ge__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Recloser.RecloserBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Recloser.RecloserBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Recloser.RecloserBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Recloser.RecloserBatchProperties.__gt__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Recloser.RecloserBatchProperties.__init__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Recloser.RecloserBatchProperties.__ior__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Recloser.RecloserBatchProperties.__iter__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Recloser.RecloserBatchProperties.__le__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Recloser.RecloserBatchProperties.__len__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Recloser.RecloserBatchProperties.__lt__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Recloser.RecloserBatchProperties.__ne__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Recloser.RecloserBatchProperties.__new__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Recloser.RecloserBatchProperties.__or__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Recloser.RecloserBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Recloser.RecloserBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Recloser.RecloserBatchProperties.__repr__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Recloser.RecloserBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Recloser.RecloserBatchProperties.__ror__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Recloser.RecloserBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Recloser.RecloserBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Recloser.RecloserBatchProperties.__str__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Recloser.RecloserBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Recloser.RecloserBatchProperties.clear

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Recloser.RecloserBatchProperties.copy

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Recloser.RecloserBatchProperties.get

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Recloser.RecloserBatchProperties.items

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Recloser.RecloserBatchProperties.keys

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Recloser.RecloserBatchProperties.pop

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Recloser.RecloserBatchProperties.popitem

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Recloser.RecloserBatchProperties.setdefault

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Recloser.RecloserBatchProperties.update

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Recloser.RecloserBatchProperties.values

```{autodoc2-docstring} altdss.Recloser.RecloserBatchProperties.values
```

````

`````

`````{py:class} RecloserProperties()
:canonical: altdss.Recloser.RecloserProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Recloser.RecloserProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Recloser.RecloserProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.BaseFreq
```

````

````{py:attribute} Delay
:canonical: altdss.Recloser.RecloserProperties.Delay
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.Recloser.RecloserProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.Enabled
```

````

````{py:attribute} GroundDelayed
:canonical: altdss.Recloser.RecloserProperties.GroundDelayed
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.GroundDelayed
```

````

````{py:attribute} GroundFast
:canonical: altdss.Recloser.RecloserProperties.GroundFast
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.GroundFast
```

````

````{py:attribute} GroundInst
:canonical: altdss.Recloser.RecloserProperties.GroundInst
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Recloser.RecloserProperties.GroundTrip
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.GroundTrip
```

````

````{py:attribute} Like
:canonical: altdss.Recloser.RecloserProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.Like
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Recloser.RecloserProperties.MonitoredObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.MonitoredObj
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Recloser.RecloserProperties.MonitoredTerm
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.MonitoredTerm
```

````

````{py:attribute} Normal
:canonical: altdss.Recloser.RecloserProperties.Normal
:type: typing.Union[typing.AnyStr, int, altdss.enums.RecloserState]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.Normal
```

````

````{py:attribute} NumFast
:canonical: altdss.Recloser.RecloserProperties.NumFast
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.NumFast
```

````

````{py:attribute} PhaseDelayed
:canonical: altdss.Recloser.RecloserProperties.PhaseDelayed
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.PhaseDelayed
```

````

````{py:attribute} PhaseFast
:canonical: altdss.Recloser.RecloserProperties.PhaseFast
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.PhaseFast
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Recloser.RecloserProperties.PhaseInst
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.PhaseInst
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Recloser.RecloserProperties.PhaseTrip
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.PhaseTrip
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Recloser.RecloserProperties.RecloseIntervals
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Recloser.RecloserProperties.Reset
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.Reset
```

````

````{py:attribute} Shots
:canonical: altdss.Recloser.RecloserProperties.Shots
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.Shots
```

````

````{py:attribute} State
:canonical: altdss.Recloser.RecloserProperties.State
:type: typing.Union[typing.AnyStr, int, altdss.enums.RecloserState]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.State
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Recloser.RecloserProperties.SwitchedObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.SwitchedObj
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Recloser.RecloserProperties.SwitchedTerm
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.SwitchedTerm
```

````

````{py:attribute} TDGrDelayed
:canonical: altdss.Recloser.RecloserProperties.TDGrDelayed
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.TDGrDelayed
```

````

````{py:attribute} TDGrFast
:canonical: altdss.Recloser.RecloserProperties.TDGrFast
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.TDGrFast
```

````

````{py:attribute} TDPhDelayed
:canonical: altdss.Recloser.RecloserProperties.TDPhDelayed
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.TDPhDelayed
```

````

````{py:attribute} TDPhFast
:canonical: altdss.Recloser.RecloserProperties.TDPhFast
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.TDPhFast
```

````

````{py:method} __contains__()
:canonical: altdss.Recloser.RecloserProperties.__contains__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Recloser.RecloserProperties.__delattr__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Recloser.RecloserProperties.__delitem__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Recloser.RecloserProperties.__dir__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Recloser.RecloserProperties.__format__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Recloser.RecloserProperties.__ge__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Recloser.RecloserProperties.__getattribute__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Recloser.RecloserProperties.__getitem__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Recloser.RecloserProperties.__getstate__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Recloser.RecloserProperties.__gt__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Recloser.RecloserProperties.__init__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Recloser.RecloserProperties.__ior__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Recloser.RecloserProperties.__iter__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Recloser.RecloserProperties.__le__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Recloser.RecloserProperties.__len__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Recloser.RecloserProperties.__lt__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Recloser.RecloserProperties.__ne__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Recloser.RecloserProperties.__new__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Recloser.RecloserProperties.__or__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Recloser.RecloserProperties.__reduce__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Recloser.RecloserProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Recloser.RecloserProperties.__repr__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Recloser.RecloserProperties.__reversed__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Recloser.RecloserProperties.__ror__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Recloser.RecloserProperties.__setitem__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Recloser.RecloserProperties.__sizeof__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Recloser.RecloserProperties.__str__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Recloser.RecloserProperties.__subclasshook__

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Recloser.RecloserProperties.clear

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Recloser.RecloserProperties.copy

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Recloser.RecloserProperties.get

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.get
```

````

````{py:method} items()
:canonical: altdss.Recloser.RecloserProperties.items

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Recloser.RecloserProperties.keys

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Recloser.RecloserProperties.pop

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Recloser.RecloserProperties.popitem

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Recloser.RecloserProperties.setdefault

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Recloser.RecloserProperties.update

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.update
```

````

````{py:method} values()
:canonical: altdss.Recloser.RecloserProperties.values

```{autodoc2-docstring} altdss.Recloser.RecloserProperties.values
```

````

`````
