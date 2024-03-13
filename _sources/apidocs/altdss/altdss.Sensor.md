# {py:mod}`altdss.Sensor`

```{py:module} altdss.Sensor
```

```{autodoc2-docstring} altdss.Sensor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ISensor <altdss.Sensor.ISensor>`
  - ```{autodoc2-docstring} altdss.Sensor.ISensor
    :summary:
    ```
* - {py:obj}`Sensor <altdss.Sensor.Sensor>`
  - ```{autodoc2-docstring} altdss.Sensor.Sensor
    :summary:
    ```
* - {py:obj}`SensorBatch <altdss.Sensor.SensorBatch>`
  - ```{autodoc2-docstring} altdss.Sensor.SensorBatch
    :summary:
    ```
* - {py:obj}`SensorBatchProperties <altdss.Sensor.SensorBatchProperties>`
  - ```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties
    :summary:
    ```
* - {py:obj}`SensorProperties <altdss.Sensor.SensorProperties>`
  - ```{autodoc2-docstring} altdss.Sensor.SensorProperties
    :summary:
    ```
````

### API

`````{py:class} ISensor(iobj)
:canonical: altdss.Sensor.ISensor

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Sensor.SensorBatch`

```{autodoc2-docstring} altdss.Sensor.ISensor
```

````{py:attribute} BaseFreq
:canonical: altdss.Sensor.ISensor.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.BaseFreq
```

````

````{py:method} Clear(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Sensor.ISensor.Clear

```{autodoc2-docstring} altdss.Sensor.ISensor.Clear
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.ISensor.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Sensor.ISensor.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.ISensor.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Sensor.ISensor.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Sensor.ISensor.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Sensor.ISensor.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.Conn_str
```

````

````{py:attribute} Currents
:canonical: altdss.Sensor.ISensor.Currents
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Sensor.ISensor.CurrentsMagAng

```{autodoc2-docstring} altdss.Sensor.ISensor.CurrentsMagAng
```

````

````{py:attribute} DeltaDirection
:canonical: altdss.Sensor.ISensor.DeltaDirection
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.DeltaDirection
```

````

````{py:attribute} Element
:canonical: altdss.Sensor.ISensor.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.Sensor.ISensor.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Sensor.ISensor.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Sensor.ISensor.FullName

```{autodoc2-docstring} altdss.Sensor.ISensor.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Sensor.ISensor.GUID

```{autodoc2-docstring} altdss.Sensor.ISensor.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Sensor.ISensor.Handle

```{autodoc2-docstring} altdss.Sensor.ISensor.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Sensor.ISensor.HasOCPDevice

```{autodoc2-docstring} altdss.Sensor.ISensor.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Sensor.ISensor.HasSwitchControl

```{autodoc2-docstring} altdss.Sensor.ISensor.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Sensor.ISensor.HasVoltControl

```{autodoc2-docstring} altdss.Sensor.ISensor.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Sensor.ISensor.IsIsolated

```{autodoc2-docstring} altdss.Sensor.ISensor.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Sensor.ISensor.Like

```{autodoc2-docstring} altdss.Sensor.ISensor.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.ISensor.Losses

```{autodoc2-docstring} altdss.Sensor.ISensor.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Sensor.ISensor.MaxCurrent

```{autodoc2-docstring} altdss.Sensor.ISensor.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Sensor.ISensor.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Sensor.ISensor.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Sensor.ISensor.NumConductors

```{autodoc2-docstring} altdss.Sensor.ISensor.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Sensor.ISensor.NumControllers

```{autodoc2-docstring} altdss.Sensor.ISensor.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Sensor.ISensor.NumPhases

```{autodoc2-docstring} altdss.Sensor.ISensor.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Sensor.ISensor.NumTerminals

```{autodoc2-docstring} altdss.Sensor.ISensor.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Sensor.ISensor.OCPDevice

```{autodoc2-docstring} altdss.Sensor.ISensor.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Sensor.ISensor.OCPDeviceIndex

```{autodoc2-docstring} altdss.Sensor.ISensor.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Sensor.ISensor.OCPDeviceType

```{autodoc2-docstring} altdss.Sensor.ISensor.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.ISensor.PhaseLosses

```{autodoc2-docstring} altdss.Sensor.ISensor.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.ISensor.Powers

```{autodoc2-docstring} altdss.Sensor.ISensor.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Sensor.ISensor.SeqCurrents

```{autodoc2-docstring} altdss.Sensor.ISensor.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.ISensor.SeqPowers

```{autodoc2-docstring} altdss.Sensor.ISensor.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Sensor.ISensor.SeqVoltages

```{autodoc2-docstring} altdss.Sensor.ISensor.SeqVoltages
```

````

````{py:attribute} Terminal
:canonical: altdss.Sensor.ISensor.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.ISensor.TotalPowers

```{autodoc2-docstring} altdss.Sensor.ISensor.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.ISensor.Voltages

```{autodoc2-docstring} altdss.Sensor.ISensor.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Sensor.ISensor.VoltagesMagAng

```{autodoc2-docstring} altdss.Sensor.ISensor.VoltagesMagAng
```

````

````{py:attribute} Weight
:canonical: altdss.Sensor.ISensor.Weight
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.Weight
```

````

````{py:method} __call__()
:canonical: altdss.Sensor.ISensor.__call__

```{autodoc2-docstring} altdss.Sensor.ISensor.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Sensor.ISensor.__contains__

```{autodoc2-docstring} altdss.Sensor.ISensor.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Sensor.ISensor.__getitem__

```{autodoc2-docstring} altdss.Sensor.ISensor.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Sensor.ISensor.__init__

```{autodoc2-docstring} altdss.Sensor.ISensor.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Sensor.ISensor.__iter__

```{autodoc2-docstring} altdss.Sensor.ISensor.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Sensor.ISensor.__len__

```{autodoc2-docstring} altdss.Sensor.ISensor.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Sensor.ISensor.batch

```{autodoc2-docstring} altdss.Sensor.ISensor.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Sensor.SensorBatchProperties]) -> altdss.Sensor.SensorBatch
:canonical: altdss.Sensor.ISensor.batch_new

```{autodoc2-docstring} altdss.Sensor.ISensor.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Sensor.ISensor.begin_edit

```{autodoc2-docstring} altdss.Sensor.ISensor.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Sensor.ISensor.end_edit

```{autodoc2-docstring} altdss.Sensor.ISensor.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Sensor.ISensor.find

```{autodoc2-docstring} altdss.Sensor.ISensor.find
```

````

````{py:attribute} kVBase
:canonical: altdss.Sensor.ISensor.kVBase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.kVBase
```

````

````{py:attribute} kVs
:canonical: altdss.Sensor.ISensor.kVs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.kVs
```

````

````{py:attribute} kWs
:canonical: altdss.Sensor.ISensor.kWs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.kWs
```

````

````{py:attribute} kvars
:canonical: altdss.Sensor.ISensor.kvars
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.kvars
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Sensor.SensorProperties]) -> altdss.Sensor.Sensor
:canonical: altdss.Sensor.ISensor.new

```{autodoc2-docstring} altdss.Sensor.ISensor.new
```

````

````{py:attribute} pctError
:canonical: altdss.Sensor.ISensor.pctError
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.ISensor.pctError
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Sensor.ISensor.to_json

```{autodoc2-docstring} altdss.Sensor.ISensor.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Sensor.ISensor.to_list

```{autodoc2-docstring} altdss.Sensor.ISensor.to_list
```

````

`````

`````{py:class} Sensor(api_util, ptr)
:canonical: altdss.Sensor.Sensor

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.Sensor.Sensor
```

````{py:attribute} BaseFreq
:canonical: altdss.Sensor.Sensor.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.BaseFreq
```

````

````{py:method} Clear(value: bool = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Sensor.Sensor.Clear

```{autodoc2-docstring} altdss.Sensor.Sensor.Clear
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Sensor.Sensor.Close

```{autodoc2-docstring} altdss.Sensor.Sensor.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.Sensor.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Sensor.Sensor.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.Sensor.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Sensor.Sensor.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Sensor.Sensor.Conn
:type: altdss.enums.Connection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Sensor.Sensor.Conn_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.Conn_str
```

````

````{py:attribute} Currents
:canonical: altdss.Sensor.Sensor.Currents
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.Currents
```

````

````{py:attribute} DeltaDirection
:canonical: altdss.Sensor.Sensor.DeltaDirection
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.DeltaDirection
```

````

````{py:attribute} DisplayName
:canonical: altdss.Sensor.Sensor.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.DisplayName
```

````

````{py:attribute} Element
:canonical: altdss.Sensor.Sensor.Element
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.Sensor.Sensor.Element_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Sensor.Sensor.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.Enabled
```

````

````{py:method} FullName() -> str
:canonical: altdss.Sensor.Sensor.FullName

```{autodoc2-docstring} altdss.Sensor.Sensor.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Sensor.Sensor.GUID

```{autodoc2-docstring} altdss.Sensor.Sensor.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.Sensor.Sensor.Handle

```{autodoc2-docstring} altdss.Sensor.Sensor.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Sensor.Sensor.HasOCPDevice

```{autodoc2-docstring} altdss.Sensor.Sensor.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Sensor.Sensor.HasSwitchControl

```{autodoc2-docstring} altdss.Sensor.Sensor.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Sensor.Sensor.HasVoltControl

```{autodoc2-docstring} altdss.Sensor.Sensor.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Sensor.Sensor.IsIsolated

```{autodoc2-docstring} altdss.Sensor.Sensor.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Sensor.Sensor.IsOpen

```{autodoc2-docstring} altdss.Sensor.Sensor.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Sensor.Sensor.Like

```{autodoc2-docstring} altdss.Sensor.Sensor.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Sensor.Sensor.Losses

```{autodoc2-docstring} altdss.Sensor.Sensor.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Sensor.Sensor.MaxCurrent

```{autodoc2-docstring} altdss.Sensor.Sensor.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Sensor.Sensor.Name
:type: str

```{autodoc2-docstring} altdss.Sensor.Sensor.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Sensor.Sensor.NodeOrder

```{autodoc2-docstring} altdss.Sensor.Sensor.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Sensor.Sensor.NodeRef

```{autodoc2-docstring} altdss.Sensor.Sensor.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Sensor.Sensor.NumConductors

```{autodoc2-docstring} altdss.Sensor.Sensor.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Sensor.Sensor.NumControllers

```{autodoc2-docstring} altdss.Sensor.Sensor.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Sensor.Sensor.NumPhases

```{autodoc2-docstring} altdss.Sensor.Sensor.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Sensor.Sensor.NumTerminals

```{autodoc2-docstring} altdss.Sensor.Sensor.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Sensor.Sensor.OCPDevice

```{autodoc2-docstring} altdss.Sensor.Sensor.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Sensor.Sensor.OCPDeviceIndex

```{autodoc2-docstring} altdss.Sensor.Sensor.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Sensor.Sensor.OCPDeviceType

```{autodoc2-docstring} altdss.Sensor.Sensor.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Sensor.Sensor.Open

```{autodoc2-docstring} altdss.Sensor.Sensor.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.Sensor.PhaseLosses

```{autodoc2-docstring} altdss.Sensor.Sensor.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.Sensor.Powers

```{autodoc2-docstring} altdss.Sensor.Sensor.Powers
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Sensor.Sensor.Residuals

```{autodoc2-docstring} altdss.Sensor.Sensor.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Sensor.Sensor.SeqCurrents

```{autodoc2-docstring} altdss.Sensor.Sensor.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.Sensor.SeqPowers

```{autodoc2-docstring} altdss.Sensor.Sensor.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Sensor.Sensor.SeqVoltages

```{autodoc2-docstring} altdss.Sensor.Sensor.SeqVoltages
```

````

````{py:attribute} Terminal
:canonical: altdss.Sensor.Sensor.Terminal
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.Sensor.TotalPowers

```{autodoc2-docstring} altdss.Sensor.Sensor.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.Sensor.Voltages

```{autodoc2-docstring} altdss.Sensor.Sensor.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Sensor.Sensor.VoltagesMagAng

```{autodoc2-docstring} altdss.Sensor.Sensor.VoltagesMagAng
```

````

````{py:attribute} Weight
:canonical: altdss.Sensor.Sensor.Weight
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.Weight
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.Sensor.YPrim

```{autodoc2-docstring} altdss.Sensor.Sensor.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.Sensor.Sensor.__hash__

```{autodoc2-docstring} altdss.Sensor.Sensor.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Sensor.Sensor.__init__

```{autodoc2-docstring} altdss.Sensor.Sensor.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Sensor.Sensor.__ne__

```{autodoc2-docstring} altdss.Sensor.Sensor.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Sensor.Sensor.__repr__

```{autodoc2-docstring} altdss.Sensor.Sensor.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Sensor.Sensor.begin_edit

```{autodoc2-docstring} altdss.Sensor.Sensor.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Sensor.Sensor.end_edit

```{autodoc2-docstring} altdss.Sensor.Sensor.end_edit
```

````

````{py:attribute} kVBase
:canonical: altdss.Sensor.Sensor.kVBase
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.kVBase
```

````

````{py:attribute} kVs
:canonical: altdss.Sensor.Sensor.kVs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.kVs
```

````

````{py:attribute} kWs
:canonical: altdss.Sensor.Sensor.kWs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.kWs
```

````

````{py:attribute} kvars
:canonical: altdss.Sensor.Sensor.kvars
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.kvars
```

````

````{py:attribute} pctError
:canonical: altdss.Sensor.Sensor.pctError
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.Sensor.pctError
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Sensor.Sensor.to_json

```{autodoc2-docstring} altdss.Sensor.Sensor.to_json
```

````

`````

`````{py:class} SensorBatch(api_util, **kwargs)
:canonical: altdss.Sensor.SensorBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.Sensor.SensorBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.Sensor.SensorBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.BaseFreq
```

````

````{py:method} Clear(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Sensor.SensorBatch.Clear

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Clear
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.SensorBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Sensor.SensorBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.SensorBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Sensor.SensorBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Sensor.SensorBatch.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Sensor.SensorBatch.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Conn_str
```

````

````{py:attribute} Currents
:canonical: altdss.Sensor.SensorBatch.Currents
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Sensor.SensorBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Sensor.SensorBatch.CurrentsMagAng
```

````

````{py:attribute} DeltaDirection
:canonical: altdss.Sensor.SensorBatch.DeltaDirection
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.DeltaDirection
```

````

````{py:attribute} Element
:canonical: altdss.Sensor.SensorBatch.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.Sensor.SensorBatch.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Sensor.SensorBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Sensor.SensorBatch.FullName

```{autodoc2-docstring} altdss.Sensor.SensorBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Sensor.SensorBatch.GUID

```{autodoc2-docstring} altdss.Sensor.SensorBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Sensor.SensorBatch.Handle

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Sensor.SensorBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Sensor.SensorBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Sensor.SensorBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Sensor.SensorBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Sensor.SensorBatch.HasVoltControl

```{autodoc2-docstring} altdss.Sensor.SensorBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Sensor.SensorBatch.IsIsolated

```{autodoc2-docstring} altdss.Sensor.SensorBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Sensor.SensorBatch.Like

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.SensorBatch.Losses

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Sensor.SensorBatch.MaxCurrent

```{autodoc2-docstring} altdss.Sensor.SensorBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Sensor.SensorBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Sensor.SensorBatch.NumConductors

```{autodoc2-docstring} altdss.Sensor.SensorBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Sensor.SensorBatch.NumControllers

```{autodoc2-docstring} altdss.Sensor.SensorBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Sensor.SensorBatch.NumPhases

```{autodoc2-docstring} altdss.Sensor.SensorBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Sensor.SensorBatch.NumTerminals

```{autodoc2-docstring} altdss.Sensor.SensorBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Sensor.SensorBatch.OCPDevice

```{autodoc2-docstring} altdss.Sensor.SensorBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Sensor.SensorBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Sensor.SensorBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Sensor.SensorBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Sensor.SensorBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.SensorBatch.PhaseLosses

```{autodoc2-docstring} altdss.Sensor.SensorBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.SensorBatch.Powers

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Sensor.SensorBatch.SeqCurrents

```{autodoc2-docstring} altdss.Sensor.SensorBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.SensorBatch.SeqPowers

```{autodoc2-docstring} altdss.Sensor.SensorBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Sensor.SensorBatch.SeqVoltages

```{autodoc2-docstring} altdss.Sensor.SensorBatch.SeqVoltages
```

````

````{py:attribute} Terminal
:canonical: altdss.Sensor.SensorBatch.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.SensorBatch.TotalPowers

```{autodoc2-docstring} altdss.Sensor.SensorBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Sensor.SensorBatch.Voltages

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Sensor.SensorBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Sensor.SensorBatch.VoltagesMagAng
```

````

````{py:attribute} Weight
:canonical: altdss.Sensor.SensorBatch.Weight
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.Weight
```

````

````{py:method} __call__()
:canonical: altdss.Sensor.SensorBatch.__call__

```{autodoc2-docstring} altdss.Sensor.SensorBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Sensor.SensorBatch.__getitem__

```{autodoc2-docstring} altdss.Sensor.SensorBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Sensor.SensorBatch.__init__

```{autodoc2-docstring} altdss.Sensor.SensorBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Sensor.SensorBatch.__iter__

```{autodoc2-docstring} altdss.Sensor.SensorBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Sensor.SensorBatch.__len__

```{autodoc2-docstring} altdss.Sensor.SensorBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Sensor.SensorBatch.batch

```{autodoc2-docstring} altdss.Sensor.SensorBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Sensor.SensorBatch.begin_edit

```{autodoc2-docstring} altdss.Sensor.SensorBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Sensor.SensorBatch.end_edit

```{autodoc2-docstring} altdss.Sensor.SensorBatch.end_edit
```

````

````{py:attribute} kVBase
:canonical: altdss.Sensor.SensorBatch.kVBase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.kVBase
```

````

````{py:attribute} kVs
:canonical: altdss.Sensor.SensorBatch.kVs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.kVs
```

````

````{py:attribute} kWs
:canonical: altdss.Sensor.SensorBatch.kWs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.kWs
```

````

````{py:attribute} kvars
:canonical: altdss.Sensor.SensorBatch.kvars
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.kvars
```

````

````{py:attribute} pctError
:canonical: altdss.Sensor.SensorBatch.pctError
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Sensor.SensorBatch.pctError
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Sensor.SensorBatch.to_json

```{autodoc2-docstring} altdss.Sensor.SensorBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Sensor.SensorBatch.to_list

```{autodoc2-docstring} altdss.Sensor.SensorBatch.to_list
```

````

`````

`````{py:class} SensorBatchProperties()
:canonical: altdss.Sensor.SensorBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Sensor.SensorBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.BaseFreq
```

````

````{py:attribute} Clear
:canonical: altdss.Sensor.SensorBatchProperties.Clear
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.Clear
```

````

````{py:attribute} Conn
:canonical: altdss.Sensor.SensorBatchProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.Connection], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.Conn
```

````

````{py:attribute} Currents
:canonical: altdss.Sensor.SensorBatchProperties.Currents
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.Currents
```

````

````{py:attribute} DeltaDirection
:canonical: altdss.Sensor.SensorBatchProperties.DeltaDirection
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.DeltaDirection
```

````

````{py:attribute} Element
:canonical: altdss.Sensor.SensorBatchProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.Sensor.SensorBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.Sensor.SensorBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.Like
```

````

````{py:attribute} Terminal
:canonical: altdss.Sensor.SensorBatchProperties.Terminal
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.Terminal
```

````

````{py:attribute} Weight
:canonical: altdss.Sensor.SensorBatchProperties.Weight
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.Weight
```

````

````{py:method} __contains__()
:canonical: altdss.Sensor.SensorBatchProperties.__contains__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Sensor.SensorBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Sensor.SensorBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Sensor.SensorBatchProperties.__dir__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Sensor.SensorBatchProperties.__format__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Sensor.SensorBatchProperties.__ge__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Sensor.SensorBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Sensor.SensorBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Sensor.SensorBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Sensor.SensorBatchProperties.__gt__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Sensor.SensorBatchProperties.__init__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Sensor.SensorBatchProperties.__ior__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Sensor.SensorBatchProperties.__iter__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Sensor.SensorBatchProperties.__le__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Sensor.SensorBatchProperties.__len__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Sensor.SensorBatchProperties.__lt__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Sensor.SensorBatchProperties.__ne__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Sensor.SensorBatchProperties.__new__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Sensor.SensorBatchProperties.__or__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Sensor.SensorBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Sensor.SensorBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Sensor.SensorBatchProperties.__repr__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Sensor.SensorBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Sensor.SensorBatchProperties.__ror__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Sensor.SensorBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Sensor.SensorBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Sensor.SensorBatchProperties.__str__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Sensor.SensorBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Sensor.SensorBatchProperties.clear

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Sensor.SensorBatchProperties.copy

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Sensor.SensorBatchProperties.get

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Sensor.SensorBatchProperties.items

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.items
```

````

````{py:attribute} kVBase
:canonical: altdss.Sensor.SensorBatchProperties.kVBase
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.kVBase
```

````

````{py:attribute} kVs
:canonical: altdss.Sensor.SensorBatchProperties.kVs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.kVs
```

````

````{py:attribute} kWs
:canonical: altdss.Sensor.SensorBatchProperties.kWs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.kWs
```

````

````{py:method} keys()
:canonical: altdss.Sensor.SensorBatchProperties.keys

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.keys
```

````

````{py:attribute} kvars
:canonical: altdss.Sensor.SensorBatchProperties.kvars
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.kvars
```

````

````{py:attribute} pctError
:canonical: altdss.Sensor.SensorBatchProperties.pctError
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.pctError
```

````

````{py:method} pop()
:canonical: altdss.Sensor.SensorBatchProperties.pop

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Sensor.SensorBatchProperties.popitem

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Sensor.SensorBatchProperties.setdefault

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Sensor.SensorBatchProperties.update

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Sensor.SensorBatchProperties.values

```{autodoc2-docstring} altdss.Sensor.SensorBatchProperties.values
```

````

`````

`````{py:class} SensorProperties()
:canonical: altdss.Sensor.SensorProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Sensor.SensorProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Sensor.SensorProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.BaseFreq
```

````

````{py:attribute} Clear
:canonical: altdss.Sensor.SensorProperties.Clear
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.Clear
```

````

````{py:attribute} Conn
:canonical: altdss.Sensor.SensorProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.Conn
```

````

````{py:attribute} Currents
:canonical: altdss.Sensor.SensorProperties.Currents
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.Currents
```

````

````{py:attribute} DeltaDirection
:canonical: altdss.Sensor.SensorProperties.DeltaDirection
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.DeltaDirection
```

````

````{py:attribute} Element
:canonical: altdss.Sensor.SensorProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.Sensor.SensorProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.Enabled
```

````

````{py:attribute} Like
:canonical: altdss.Sensor.SensorProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.Like
```

````

````{py:attribute} Terminal
:canonical: altdss.Sensor.SensorProperties.Terminal
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.Terminal
```

````

````{py:attribute} Weight
:canonical: altdss.Sensor.SensorProperties.Weight
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.Weight
```

````

````{py:method} __contains__()
:canonical: altdss.Sensor.SensorProperties.__contains__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Sensor.SensorProperties.__delattr__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Sensor.SensorProperties.__delitem__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Sensor.SensorProperties.__dir__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Sensor.SensorProperties.__format__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Sensor.SensorProperties.__ge__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Sensor.SensorProperties.__getattribute__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Sensor.SensorProperties.__getitem__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Sensor.SensorProperties.__getstate__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Sensor.SensorProperties.__gt__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Sensor.SensorProperties.__init__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Sensor.SensorProperties.__ior__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Sensor.SensorProperties.__iter__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Sensor.SensorProperties.__le__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Sensor.SensorProperties.__len__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Sensor.SensorProperties.__lt__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Sensor.SensorProperties.__ne__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Sensor.SensorProperties.__new__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Sensor.SensorProperties.__or__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Sensor.SensorProperties.__reduce__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Sensor.SensorProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Sensor.SensorProperties.__repr__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Sensor.SensorProperties.__reversed__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Sensor.SensorProperties.__ror__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Sensor.SensorProperties.__setitem__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Sensor.SensorProperties.__sizeof__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Sensor.SensorProperties.__str__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Sensor.SensorProperties.__subclasshook__

```{autodoc2-docstring} altdss.Sensor.SensorProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Sensor.SensorProperties.clear

```{autodoc2-docstring} altdss.Sensor.SensorProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Sensor.SensorProperties.copy

```{autodoc2-docstring} altdss.Sensor.SensorProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Sensor.SensorProperties.get

```{autodoc2-docstring} altdss.Sensor.SensorProperties.get
```

````

````{py:method} items()
:canonical: altdss.Sensor.SensorProperties.items

```{autodoc2-docstring} altdss.Sensor.SensorProperties.items
```

````

````{py:attribute} kVBase
:canonical: altdss.Sensor.SensorProperties.kVBase
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.kVBase
```

````

````{py:attribute} kVs
:canonical: altdss.Sensor.SensorProperties.kVs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.kVs
```

````

````{py:attribute} kWs
:canonical: altdss.Sensor.SensorProperties.kWs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.kWs
```

````

````{py:method} keys()
:canonical: altdss.Sensor.SensorProperties.keys

```{autodoc2-docstring} altdss.Sensor.SensorProperties.keys
```

````

````{py:attribute} kvars
:canonical: altdss.Sensor.SensorProperties.kvars
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.kvars
```

````

````{py:attribute} pctError
:canonical: altdss.Sensor.SensorProperties.pctError
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Sensor.SensorProperties.pctError
```

````

````{py:method} pop()
:canonical: altdss.Sensor.SensorProperties.pop

```{autodoc2-docstring} altdss.Sensor.SensorProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Sensor.SensorProperties.popitem

```{autodoc2-docstring} altdss.Sensor.SensorProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Sensor.SensorProperties.setdefault

```{autodoc2-docstring} altdss.Sensor.SensorProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Sensor.SensorProperties.update

```{autodoc2-docstring} altdss.Sensor.SensorProperties.update
```

````

````{py:method} values()
:canonical: altdss.Sensor.SensorProperties.values

```{autodoc2-docstring} altdss.Sensor.SensorProperties.values
```

````

`````
