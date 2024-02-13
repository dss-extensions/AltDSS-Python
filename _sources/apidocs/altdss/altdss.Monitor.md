# {py:mod}`altdss.Monitor`

```{py:module} altdss.Monitor
```

```{autodoc2-docstring} altdss.Monitor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IMonitor <altdss.Monitor.IMonitor>`
  - ```{autodoc2-docstring} altdss.Monitor.IMonitor
    :summary:
    ```
* - {py:obj}`Monitor <altdss.Monitor.Monitor>`
  - ```{autodoc2-docstring} altdss.Monitor.Monitor
    :summary:
    ```
* - {py:obj}`MonitorBatch <altdss.Monitor.MonitorBatch>`
  - ```{autodoc2-docstring} altdss.Monitor.MonitorBatch
    :summary:
    ```
* - {py:obj}`MonitorBatchProperties <altdss.Monitor.MonitorBatchProperties>`
  - ```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties
    :summary:
    ```
* - {py:obj}`MonitorProperties <altdss.Monitor.MonitorProperties>`
  - ```{autodoc2-docstring} altdss.Monitor.MonitorProperties
    :summary:
    ```
````

### API

`````{py:class} IMonitor(iobj)
:canonical: altdss.Monitor.IMonitor

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Monitor.MonitorBatch`

```{autodoc2-docstring} altdss.Monitor.IMonitor
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.MonitorAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.IMonitor.Action

```{autodoc2-docstring} altdss.Monitor.IMonitor.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Monitor.IMonitor.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.IMonitor.BaseFreq
```

````

````{py:method} Clear(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.IMonitor.Clear

```{autodoc2-docstring} altdss.Monitor.IMonitor.Clear
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.IMonitor.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Monitor.IMonitor.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.IMonitor.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Monitor.IMonitor.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.IMonitor.Currents

```{autodoc2-docstring} altdss.Monitor.IMonitor.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Monitor.IMonitor.CurrentsMagAng

```{autodoc2-docstring} altdss.Monitor.IMonitor.CurrentsMagAng
```

````

````{py:attribute} Element
:canonical: altdss.Monitor.IMonitor.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.IMonitor.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.Monitor.IMonitor.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.IMonitor.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Monitor.IMonitor.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.IMonitor.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Monitor.IMonitor.FullName

```{autodoc2-docstring} altdss.Monitor.IMonitor.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Monitor.IMonitor.GUID

```{autodoc2-docstring} altdss.Monitor.IMonitor.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Monitor.IMonitor.Handle

```{autodoc2-docstring} altdss.Monitor.IMonitor.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Monitor.IMonitor.HasOCPDevice

```{autodoc2-docstring} altdss.Monitor.IMonitor.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Monitor.IMonitor.HasSwitchControl

```{autodoc2-docstring} altdss.Monitor.IMonitor.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Monitor.IMonitor.HasVoltControl

```{autodoc2-docstring} altdss.Monitor.IMonitor.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Monitor.IMonitor.IsIsolated

```{autodoc2-docstring} altdss.Monitor.IMonitor.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.IMonitor.Like

```{autodoc2-docstring} altdss.Monitor.IMonitor.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.IMonitor.Losses

```{autodoc2-docstring} altdss.Monitor.IMonitor.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Monitor.IMonitor.MaxCurrent

```{autodoc2-docstring} altdss.Monitor.IMonitor.MaxCurrent
```

````

````{py:attribute} Mode
:canonical: altdss.Monitor.IMonitor.Mode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.IMonitor.Mode
```

````

````{py:property} Name
:canonical: altdss.Monitor.IMonitor.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Monitor.IMonitor.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Monitor.IMonitor.NumConductors

```{autodoc2-docstring} altdss.Monitor.IMonitor.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Monitor.IMonitor.NumControllers

```{autodoc2-docstring} altdss.Monitor.IMonitor.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Monitor.IMonitor.NumPhases

```{autodoc2-docstring} altdss.Monitor.IMonitor.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Monitor.IMonitor.NumTerminals

```{autodoc2-docstring} altdss.Monitor.IMonitor.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Monitor.IMonitor.OCPDevice

```{autodoc2-docstring} altdss.Monitor.IMonitor.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Monitor.IMonitor.OCPDeviceIndex

```{autodoc2-docstring} altdss.Monitor.IMonitor.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Monitor.IMonitor.OCPDeviceType

```{autodoc2-docstring} altdss.Monitor.IMonitor.OCPDeviceType
```

````

````{py:attribute} PPolar
:canonical: altdss.Monitor.IMonitor.PPolar
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.IMonitor.PPolar
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.IMonitor.PhaseLosses

```{autodoc2-docstring} altdss.Monitor.IMonitor.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.IMonitor.Powers

```{autodoc2-docstring} altdss.Monitor.IMonitor.Powers
```

````

````{py:method} Process(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.IMonitor.Process

```{autodoc2-docstring} altdss.Monitor.IMonitor.Process
```

````

````{py:method} Reset(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.IMonitor.Reset

```{autodoc2-docstring} altdss.Monitor.IMonitor.Reset
```

````

````{py:attribute} Residual
:canonical: altdss.Monitor.IMonitor.Residual
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.IMonitor.Residual
```

````

````{py:method} Save(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.IMonitor.Save

```{autodoc2-docstring} altdss.Monitor.IMonitor.Save
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Monitor.IMonitor.SeqCurrents

```{autodoc2-docstring} altdss.Monitor.IMonitor.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.IMonitor.SeqPowers

```{autodoc2-docstring} altdss.Monitor.IMonitor.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Monitor.IMonitor.SeqVoltages

```{autodoc2-docstring} altdss.Monitor.IMonitor.SeqVoltages
```

````

````{py:method} TakeSample(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.IMonitor.TakeSample

```{autodoc2-docstring} altdss.Monitor.IMonitor.TakeSample
```

````

````{py:attribute} Terminal
:canonical: altdss.Monitor.IMonitor.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.IMonitor.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.IMonitor.TotalPowers

```{autodoc2-docstring} altdss.Monitor.IMonitor.TotalPowers
```

````

````{py:attribute} VIPolar
:canonical: altdss.Monitor.IMonitor.VIPolar
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.IMonitor.VIPolar
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.IMonitor.Voltages

```{autodoc2-docstring} altdss.Monitor.IMonitor.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Monitor.IMonitor.VoltagesMagAng

```{autodoc2-docstring} altdss.Monitor.IMonitor.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.Monitor.IMonitor.__call__

```{autodoc2-docstring} altdss.Monitor.IMonitor.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Monitor.IMonitor.__contains__

```{autodoc2-docstring} altdss.Monitor.IMonitor.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Monitor.IMonitor.__getitem__

```{autodoc2-docstring} altdss.Monitor.IMonitor.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Monitor.IMonitor.__init__

```{autodoc2-docstring} altdss.Monitor.IMonitor.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Monitor.IMonitor.__iter__

```{autodoc2-docstring} altdss.Monitor.IMonitor.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Monitor.IMonitor.__len__

```{autodoc2-docstring} altdss.Monitor.IMonitor.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Monitor.IMonitor.batch

```{autodoc2-docstring} altdss.Monitor.IMonitor.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Monitor.MonitorBatchProperties]) -> altdss.Monitor.MonitorBatch
:canonical: altdss.Monitor.IMonitor.batch_new

```{autodoc2-docstring} altdss.Monitor.IMonitor.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Monitor.IMonitor.begin_edit

```{autodoc2-docstring} altdss.Monitor.IMonitor.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Monitor.IMonitor.end_edit

```{autodoc2-docstring} altdss.Monitor.IMonitor.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Monitor.IMonitor.find

```{autodoc2-docstring} altdss.Monitor.IMonitor.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Monitor.MonitorProperties]) -> altdss.Monitor.Monitor
:canonical: altdss.Monitor.IMonitor.new

```{autodoc2-docstring} altdss.Monitor.IMonitor.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Monitor.IMonitor.to_json

```{autodoc2-docstring} altdss.Monitor.IMonitor.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Monitor.IMonitor.to_list

```{autodoc2-docstring} altdss.Monitor.IMonitor.to_list
```

````

`````

`````{py:class} Monitor(api_util, ptr)
:canonical: altdss.Monitor.Monitor

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.MonitorExtras.MonitorObjMixin`

```{autodoc2-docstring} altdss.Monitor.Monitor
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.MonitorAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.Monitor.Action

```{autodoc2-docstring} altdss.Monitor.Monitor.Action
```

````

````{py:method} AsMatrix() -> altdss.types.Float64Array
:canonical: altdss.Monitor.Monitor.AsMatrix

```{autodoc2-docstring} altdss.Monitor.Monitor.AsMatrix
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Monitor.Monitor.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.BaseFreq
```

````

````{py:method} ByteStream() -> altdss.types.Int8Array
:canonical: altdss.Monitor.Monitor.ByteStream

```{autodoc2-docstring} altdss.Monitor.Monitor.ByteStream
```

````

````{py:method} Channel(index: int) -> altdss.types.Float32Array
:canonical: altdss.Monitor.Monitor.Channel

```{autodoc2-docstring} altdss.Monitor.Monitor.Channel
```

````

````{py:method} Clear(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.Monitor.Clear

```{autodoc2-docstring} altdss.Monitor.Monitor.Clear
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Monitor.Monitor.Close

```{autodoc2-docstring} altdss.Monitor.Monitor.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.Monitor.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Monitor.Monitor.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.Monitor.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Monitor.Monitor.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.Monitor.Currents

```{autodoc2-docstring} altdss.Monitor.Monitor.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.Monitor.Monitor.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.DisplayName
```

````

````{py:attribute} Element
:canonical: altdss.Monitor.Monitor.Element
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.Monitor.Monitor.Element_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Monitor.Monitor.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.Enabled
```

````

````{py:method} FileName() -> str
:canonical: altdss.Monitor.Monitor.FileName

```{autodoc2-docstring} altdss.Monitor.Monitor.FileName
```

````

````{py:method} FullName() -> str
:canonical: altdss.Monitor.Monitor.FullName

```{autodoc2-docstring} altdss.Monitor.Monitor.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Monitor.Monitor.GUID

```{autodoc2-docstring} altdss.Monitor.Monitor.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.Monitor.Monitor.Handle

```{autodoc2-docstring} altdss.Monitor.Monitor.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Monitor.Monitor.HasOCPDevice

```{autodoc2-docstring} altdss.Monitor.Monitor.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Monitor.Monitor.HasSwitchControl

```{autodoc2-docstring} altdss.Monitor.Monitor.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Monitor.Monitor.HasVoltControl

```{autodoc2-docstring} altdss.Monitor.Monitor.HasVoltControl
```

````

````{py:method} Header() -> typing.List[str]
:canonical: altdss.Monitor.Monitor.Header

```{autodoc2-docstring} altdss.Monitor.Monitor.Header
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Monitor.Monitor.IsIsolated

```{autodoc2-docstring} altdss.Monitor.Monitor.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Monitor.Monitor.IsOpen

```{autodoc2-docstring} altdss.Monitor.Monitor.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Monitor.Monitor.Like

```{autodoc2-docstring} altdss.Monitor.Monitor.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Monitor.Monitor.Losses

```{autodoc2-docstring} altdss.Monitor.Monitor.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Monitor.Monitor.MaxCurrent

```{autodoc2-docstring} altdss.Monitor.Monitor.MaxCurrent
```

````

````{py:attribute} Mode
:canonical: altdss.Monitor.Monitor.Mode
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.Mode
```

````

````{py:property} Name
:canonical: altdss.Monitor.Monitor.Name
:type: str

```{autodoc2-docstring} altdss.Monitor.Monitor.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Monitor.Monitor.NodeOrder

```{autodoc2-docstring} altdss.Monitor.Monitor.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Monitor.Monitor.NodeRef

```{autodoc2-docstring} altdss.Monitor.Monitor.NodeRef
```

````

````{py:method} NumChannels() -> int
:canonical: altdss.Monitor.Monitor.NumChannels

```{autodoc2-docstring} altdss.Monitor.Monitor.NumChannels
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Monitor.Monitor.NumConductors

```{autodoc2-docstring} altdss.Monitor.Monitor.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Monitor.Monitor.NumControllers

```{autodoc2-docstring} altdss.Monitor.Monitor.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Monitor.Monitor.NumPhases

```{autodoc2-docstring} altdss.Monitor.Monitor.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Monitor.Monitor.NumTerminals

```{autodoc2-docstring} altdss.Monitor.Monitor.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Monitor.Monitor.OCPDevice

```{autodoc2-docstring} altdss.Monitor.Monitor.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Monitor.Monitor.OCPDeviceIndex

```{autodoc2-docstring} altdss.Monitor.Monitor.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Monitor.Monitor.OCPDeviceType

```{autodoc2-docstring} altdss.Monitor.Monitor.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Monitor.Monitor.Open

```{autodoc2-docstring} altdss.Monitor.Monitor.Open
```

````

````{py:attribute} PPolar
:canonical: altdss.Monitor.Monitor.PPolar
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.PPolar
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.Monitor.PhaseLosses

```{autodoc2-docstring} altdss.Monitor.Monitor.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.Monitor.Powers

```{autodoc2-docstring} altdss.Monitor.Monitor.Powers
```

````

````{py:method} Process(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.Monitor.Process

```{autodoc2-docstring} altdss.Monitor.Monitor.Process
```

````

````{py:method} RecordSize() -> int
:canonical: altdss.Monitor.Monitor.RecordSize

```{autodoc2-docstring} altdss.Monitor.Monitor.RecordSize
```

````

````{py:method} Reset(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.Monitor.Reset

```{autodoc2-docstring} altdss.Monitor.Monitor.Reset
```

````

````{py:attribute} Residual
:canonical: altdss.Monitor.Monitor.Residual
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.Residual
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Monitor.Monitor.Residuals

```{autodoc2-docstring} altdss.Monitor.Monitor.Residuals
```

````

````{py:method} SampleCount() -> int
:canonical: altdss.Monitor.Monitor.SampleCount

```{autodoc2-docstring} altdss.Monitor.Monitor.SampleCount
```

````

````{py:method} Save(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.Monitor.Save

```{autodoc2-docstring} altdss.Monitor.Monitor.Save
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Monitor.Monitor.SeqCurrents

```{autodoc2-docstring} altdss.Monitor.Monitor.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.Monitor.SeqPowers

```{autodoc2-docstring} altdss.Monitor.Monitor.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Monitor.Monitor.SeqVoltages

```{autodoc2-docstring} altdss.Monitor.Monitor.SeqVoltages
```

````

````{py:method} Show()
:canonical: altdss.Monitor.Monitor.Show

```{autodoc2-docstring} altdss.Monitor.Monitor.Show
```

````

````{py:method} TakeSample(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.Monitor.TakeSample

```{autodoc2-docstring} altdss.Monitor.Monitor.TakeSample
```

````

````{py:attribute} Terminal
:canonical: altdss.Monitor.Monitor.Terminal
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.Terminal
```

````

````{py:method} ToDataFrame()
:canonical: altdss.Monitor.Monitor.ToDataFrame

```{autodoc2-docstring} altdss.Monitor.Monitor.ToDataFrame
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.Monitor.TotalPowers

```{autodoc2-docstring} altdss.Monitor.Monitor.TotalPowers
```

````

````{py:attribute} VIPolar
:canonical: altdss.Monitor.Monitor.VIPolar
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.Monitor.VIPolar
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.Monitor.Voltages

```{autodoc2-docstring} altdss.Monitor.Monitor.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Monitor.Monitor.VoltagesMagAng

```{autodoc2-docstring} altdss.Monitor.Monitor.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.Monitor.YPrim

```{autodoc2-docstring} altdss.Monitor.Monitor.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.Monitor.Monitor.__hash__

```{autodoc2-docstring} altdss.Monitor.Monitor.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Monitor.Monitor.__init__

```{autodoc2-docstring} altdss.Monitor.Monitor.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Monitor.Monitor.__ne__

```{autodoc2-docstring} altdss.Monitor.Monitor.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Monitor.Monitor.__repr__

```{autodoc2-docstring} altdss.Monitor.Monitor.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Monitor.Monitor.begin_edit

```{autodoc2-docstring} altdss.Monitor.Monitor.begin_edit
```

````

````{py:method} dblFreq() -> altdss.types.Float64Array
:canonical: altdss.Monitor.Monitor.dblFreq

```{autodoc2-docstring} altdss.Monitor.Monitor.dblFreq
```

````

````{py:method} dblHour() -> altdss.types.Float64Array
:canonical: altdss.Monitor.Monitor.dblHour

```{autodoc2-docstring} altdss.Monitor.Monitor.dblHour
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Monitor.Monitor.end_edit

```{autodoc2-docstring} altdss.Monitor.Monitor.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Monitor.Monitor.to_json

```{autodoc2-docstring} altdss.Monitor.Monitor.to_json
```

````

`````

`````{py:class} MonitorBatch(api_util, **kwargs)
:canonical: altdss.Monitor.MonitorBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.Monitor.MonitorBatch
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.MonitorAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.MonitorBatch.Action

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Monitor.MonitorBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.BaseFreq
```

````

````{py:method} Clear(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.MonitorBatch.Clear

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Clear
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.MonitorBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.MonitorBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.MonitorBatch.Currents

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Monitor.MonitorBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.CurrentsMagAng
```

````

````{py:attribute} Element
:canonical: altdss.Monitor.MonitorBatch.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.Monitor.MonitorBatch.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Monitor.MonitorBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Monitor.MonitorBatch.FullName

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Monitor.MonitorBatch.GUID

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Monitor.MonitorBatch.Handle

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Monitor.MonitorBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Monitor.MonitorBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Monitor.MonitorBatch.HasVoltControl

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Monitor.MonitorBatch.IsIsolated

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.MonitorBatch.Like

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.MonitorBatch.Losses

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Monitor.MonitorBatch.MaxCurrent

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.MaxCurrent
```

````

````{py:attribute} Mode
:canonical: altdss.Monitor.MonitorBatch.Mode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Mode
```

````

````{py:property} Name
:canonical: altdss.Monitor.MonitorBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Monitor.MonitorBatch.NumConductors

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Monitor.MonitorBatch.NumControllers

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Monitor.MonitorBatch.NumPhases

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Monitor.MonitorBatch.NumTerminals

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Monitor.MonitorBatch.OCPDevice

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Monitor.MonitorBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Monitor.MonitorBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.OCPDeviceType
```

````

````{py:attribute} PPolar
:canonical: altdss.Monitor.MonitorBatch.PPolar
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.PPolar
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.MonitorBatch.PhaseLosses

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.MonitorBatch.Powers

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Powers
```

````

````{py:method} Process(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.MonitorBatch.Process

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Process
```

````

````{py:method} Reset(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.MonitorBatch.Reset

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Reset
```

````

````{py:attribute} Residual
:canonical: altdss.Monitor.MonitorBatch.Residual
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Residual
```

````

````{py:method} Save(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.MonitorBatch.Save

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Save
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Monitor.MonitorBatch.SeqCurrents

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.MonitorBatch.SeqPowers

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Monitor.MonitorBatch.SeqVoltages

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.SeqVoltages
```

````

````{py:method} TakeSample(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Monitor.MonitorBatch.TakeSample

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.TakeSample
```

````

````{py:attribute} Terminal
:canonical: altdss.Monitor.MonitorBatch.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.MonitorBatch.TotalPowers

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.TotalPowers
```

````

````{py:attribute} VIPolar
:canonical: altdss.Monitor.MonitorBatch.VIPolar
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.VIPolar
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Monitor.MonitorBatch.Voltages

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Monitor.MonitorBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.Monitor.MonitorBatch.__call__

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Monitor.MonitorBatch.__getitem__

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Monitor.MonitorBatch.__init__

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Monitor.MonitorBatch.__iter__

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Monitor.MonitorBatch.__len__

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Monitor.MonitorBatch.begin_edit

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Monitor.MonitorBatch.end_edit

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Monitor.MonitorBatch.to_json

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Monitor.MonitorBatch.to_list

```{autodoc2-docstring} altdss.Monitor.MonitorBatch.to_list
```

````

`````

`````{py:class} MonitorBatchProperties()
:canonical: altdss.Monitor.MonitorBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties
```

````{py:attribute} Action
:canonical: altdss.Monitor.MonitorBatchProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitorAction]
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Monitor.MonitorBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.BaseFreq
```

````

````{py:attribute} Element
:canonical: altdss.Monitor.MonitorBatchProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.Monitor.MonitorBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.Monitor.MonitorBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.Like
```

````

````{py:attribute} Mode
:canonical: altdss.Monitor.MonitorBatchProperties.Mode
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.Mode
```

````

````{py:attribute} PPolar
:canonical: altdss.Monitor.MonitorBatchProperties.PPolar
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.PPolar
```

````

````{py:attribute} Residual
:canonical: altdss.Monitor.MonitorBatchProperties.Residual
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.Residual
```

````

````{py:attribute} Terminal
:canonical: altdss.Monitor.MonitorBatchProperties.Terminal
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.Terminal
```

````

````{py:attribute} VIPolar
:canonical: altdss.Monitor.MonitorBatchProperties.VIPolar
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.VIPolar
```

````

````{py:method} __contains__()
:canonical: altdss.Monitor.MonitorBatchProperties.__contains__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Monitor.MonitorBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Monitor.MonitorBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Monitor.MonitorBatchProperties.__dir__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Monitor.MonitorBatchProperties.__format__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Monitor.MonitorBatchProperties.__ge__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Monitor.MonitorBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Monitor.MonitorBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Monitor.MonitorBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Monitor.MonitorBatchProperties.__gt__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Monitor.MonitorBatchProperties.__init__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Monitor.MonitorBatchProperties.__ior__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Monitor.MonitorBatchProperties.__iter__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Monitor.MonitorBatchProperties.__le__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Monitor.MonitorBatchProperties.__len__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Monitor.MonitorBatchProperties.__lt__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Monitor.MonitorBatchProperties.__ne__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Monitor.MonitorBatchProperties.__new__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Monitor.MonitorBatchProperties.__or__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Monitor.MonitorBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Monitor.MonitorBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Monitor.MonitorBatchProperties.__repr__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Monitor.MonitorBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Monitor.MonitorBatchProperties.__ror__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Monitor.MonitorBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Monitor.MonitorBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Monitor.MonitorBatchProperties.__str__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Monitor.MonitorBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Monitor.MonitorBatchProperties.clear

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Monitor.MonitorBatchProperties.copy

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Monitor.MonitorBatchProperties.get

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Monitor.MonitorBatchProperties.items

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Monitor.MonitorBatchProperties.keys

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Monitor.MonitorBatchProperties.pop

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Monitor.MonitorBatchProperties.popitem

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Monitor.MonitorBatchProperties.setdefault

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Monitor.MonitorBatchProperties.update

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Monitor.MonitorBatchProperties.values

```{autodoc2-docstring} altdss.Monitor.MonitorBatchProperties.values
```

````

`````

`````{py:class} MonitorProperties()
:canonical: altdss.Monitor.MonitorProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Monitor.MonitorProperties
```

````{py:attribute} Action
:canonical: altdss.Monitor.MonitorProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitorAction]
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Monitor.MonitorProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.BaseFreq
```

````

````{py:attribute} Element
:canonical: altdss.Monitor.MonitorProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.Monitor.MonitorProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.Monitor.MonitorProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.Like
```

````

````{py:attribute} Mode
:canonical: altdss.Monitor.MonitorProperties.Mode
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.Mode
```

````

````{py:attribute} PPolar
:canonical: altdss.Monitor.MonitorProperties.PPolar
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.PPolar
```

````

````{py:attribute} Residual
:canonical: altdss.Monitor.MonitorProperties.Residual
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.Residual
```

````

````{py:attribute} Terminal
:canonical: altdss.Monitor.MonitorProperties.Terminal
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.Terminal
```

````

````{py:attribute} VIPolar
:canonical: altdss.Monitor.MonitorProperties.VIPolar
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.VIPolar
```

````

````{py:method} __contains__()
:canonical: altdss.Monitor.MonitorProperties.__contains__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Monitor.MonitorProperties.__delattr__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Monitor.MonitorProperties.__delitem__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Monitor.MonitorProperties.__dir__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Monitor.MonitorProperties.__format__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Monitor.MonitorProperties.__ge__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Monitor.MonitorProperties.__getattribute__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Monitor.MonitorProperties.__getitem__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Monitor.MonitorProperties.__getstate__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Monitor.MonitorProperties.__gt__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Monitor.MonitorProperties.__init__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Monitor.MonitorProperties.__ior__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Monitor.MonitorProperties.__iter__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Monitor.MonitorProperties.__le__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Monitor.MonitorProperties.__len__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Monitor.MonitorProperties.__lt__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Monitor.MonitorProperties.__ne__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Monitor.MonitorProperties.__new__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Monitor.MonitorProperties.__or__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Monitor.MonitorProperties.__reduce__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Monitor.MonitorProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Monitor.MonitorProperties.__repr__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Monitor.MonitorProperties.__reversed__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Monitor.MonitorProperties.__ror__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Monitor.MonitorProperties.__setitem__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Monitor.MonitorProperties.__sizeof__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Monitor.MonitorProperties.__str__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Monitor.MonitorProperties.__subclasshook__

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Monitor.MonitorProperties.clear

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Monitor.MonitorProperties.copy

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Monitor.MonitorProperties.get

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.get
```

````

````{py:method} items()
:canonical: altdss.Monitor.MonitorProperties.items

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Monitor.MonitorProperties.keys

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Monitor.MonitorProperties.pop

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Monitor.MonitorProperties.popitem

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Monitor.MonitorProperties.setdefault

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Monitor.MonitorProperties.update

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.update
```

````

````{py:method} values()
:canonical: altdss.Monitor.MonitorProperties.values

```{autodoc2-docstring} altdss.Monitor.MonitorProperties.values
```

````

`````
