# {py:mod}`altdss.Isource`

```{py:module} altdss.Isource
```

```{autodoc2-docstring} altdss.Isource
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IIsource <altdss.Isource.IIsource>`
  - ```{autodoc2-docstring} altdss.Isource.IIsource
    :summary:
    ```
* - {py:obj}`Isource <altdss.Isource.Isource>`
  - ```{autodoc2-docstring} altdss.Isource.Isource
    :summary:
    ```
* - {py:obj}`IsourceBatch <altdss.Isource.IsourceBatch>`
  - ```{autodoc2-docstring} altdss.Isource.IsourceBatch
    :summary:
    ```
* - {py:obj}`IsourceBatchProperties <altdss.Isource.IsourceBatchProperties>`
  - ```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties
    :summary:
    ```
* - {py:obj}`IsourceProperties <altdss.Isource.IsourceProperties>`
  - ```{autodoc2-docstring} altdss.Isource.IsourceProperties
    :summary:
    ```
````

### API

`````{py:class} IIsource(iobj)
:canonical: altdss.Isource.IIsource

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Isource.IsourceBatch`

```{autodoc2-docstring} altdss.Isource.IIsource
```

````{py:attribute} Amps
:canonical: altdss.Isource.IIsource.Amps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Amps
```

````

````{py:attribute} Angle
:canonical: altdss.Isource.IIsource.Angle
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Isource.IIsource.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Isource.IIsource.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Isource.IIsource.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Bus2
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IIsource.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Isource.IIsource.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IIsource.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Isource.IIsource.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IIsource.Currents

```{autodoc2-docstring} altdss.Isource.IIsource.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Isource.IIsource.CurrentsMagAng

```{autodoc2-docstring} altdss.Isource.IIsource.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.Isource.IIsource.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Isource.IIsource.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Daily_str
```

````

````{py:attribute} Duty
:canonical: altdss.Isource.IIsource.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Isource.IIsource.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Isource.IIsource.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Isource.IIsource.EnergyMeter

```{autodoc2-docstring} altdss.Isource.IIsource.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Isource.IIsource.EnergyMeterName

```{autodoc2-docstring} altdss.Isource.IIsource.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.Isource.IIsource.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Isource.IIsource.FullName

```{autodoc2-docstring} altdss.Isource.IIsource.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Isource.IIsource.GUID

```{autodoc2-docstring} altdss.Isource.IIsource.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Isource.IIsource.Handle

```{autodoc2-docstring} altdss.Isource.IIsource.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Isource.IIsource.HasOCPDevice

```{autodoc2-docstring} altdss.Isource.IIsource.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Isource.IIsource.HasSwitchControl

```{autodoc2-docstring} altdss.Isource.IIsource.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Isource.IIsource.HasVoltControl

```{autodoc2-docstring} altdss.Isource.IIsource.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Isource.IIsource.IsIsolated

```{autodoc2-docstring} altdss.Isource.IIsource.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Isource.IIsource.Like

```{autodoc2-docstring} altdss.Isource.IIsource.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IIsource.Losses

```{autodoc2-docstring} altdss.Isource.IIsource.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Isource.IIsource.MaxCurrent

```{autodoc2-docstring} altdss.Isource.IIsource.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Isource.IIsource.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Isource.IIsource.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Isource.IIsource.NumConductors

```{autodoc2-docstring} altdss.Isource.IIsource.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Isource.IIsource.NumControllers

```{autodoc2-docstring} altdss.Isource.IIsource.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Isource.IIsource.NumPhases

```{autodoc2-docstring} altdss.Isource.IIsource.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Isource.IIsource.NumTerminals

```{autodoc2-docstring} altdss.Isource.IIsource.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Isource.IIsource.OCPDevice

```{autodoc2-docstring} altdss.Isource.IIsource.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Isource.IIsource.OCPDeviceIndex

```{autodoc2-docstring} altdss.Isource.IIsource.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Isource.IIsource.OCPDeviceType

```{autodoc2-docstring} altdss.Isource.IIsource.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IIsource.PhaseLosses

```{autodoc2-docstring} altdss.Isource.IIsource.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Isource.IIsource.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IIsource.Powers

```{autodoc2-docstring} altdss.Isource.IIsource.Powers
```

````

````{py:attribute} ScanType
:canonical: altdss.Isource.IIsource.ScanType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.ScanType
```

````

````{py:attribute} ScanType_str
:canonical: altdss.Isource.IIsource.ScanType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.ScanType_str
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Isource.IIsource.SeqCurrents

```{autodoc2-docstring} altdss.Isource.IIsource.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IIsource.SeqPowers

```{autodoc2-docstring} altdss.Isource.IIsource.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Isource.IIsource.SeqVoltages

```{autodoc2-docstring} altdss.Isource.IIsource.SeqVoltages
```

````

````{py:attribute} Sequence
:canonical: altdss.Isource.IIsource.Sequence
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Sequence
```

````

````{py:attribute} Sequence_str
:canonical: altdss.Isource.IIsource.Sequence_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Sequence_str
```

````

````{py:attribute} Spectrum
:canonical: altdss.Isource.IIsource.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Isource.IIsource.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IIsource.TotalPowers

```{autodoc2-docstring} altdss.Isource.IIsource.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IIsource.Voltages

```{autodoc2-docstring} altdss.Isource.IIsource.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Isource.IIsource.VoltagesMagAng

```{autodoc2-docstring} altdss.Isource.IIsource.VoltagesMagAng
```

````

````{py:attribute} Yearly
:canonical: altdss.Isource.IIsource.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Isource.IIsource.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IIsource.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.Isource.IIsource.__call__

```{autodoc2-docstring} altdss.Isource.IIsource.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Isource.IIsource.__contains__

```{autodoc2-docstring} altdss.Isource.IIsource.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Isource.IIsource.__getitem__

```{autodoc2-docstring} altdss.Isource.IIsource.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Isource.IIsource.__init__

```{autodoc2-docstring} altdss.Isource.IIsource.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Isource.IIsource.__iter__

```{autodoc2-docstring} altdss.Isource.IIsource.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Isource.IIsource.__len__

```{autodoc2-docstring} altdss.Isource.IIsource.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Isource.IIsource.batch

```{autodoc2-docstring} altdss.Isource.IIsource.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Isource.IsourceBatchProperties]) -> altdss.Isource.IsourceBatch
:canonical: altdss.Isource.IIsource.batch_new

```{autodoc2-docstring} altdss.Isource.IIsource.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Isource.IIsource.begin_edit

```{autodoc2-docstring} altdss.Isource.IIsource.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Isource.IIsource.end_edit

```{autodoc2-docstring} altdss.Isource.IIsource.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Isource.IIsource.find

```{autodoc2-docstring} altdss.Isource.IIsource.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Isource.IsourceProperties]) -> altdss.Isource.Isource
:canonical: altdss.Isource.IIsource.new

```{autodoc2-docstring} altdss.Isource.IIsource.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Isource.IIsource.to_json

```{autodoc2-docstring} altdss.Isource.IIsource.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Isource.IIsource.to_list

```{autodoc2-docstring} altdss.Isource.IIsource.to_list
```

````

`````

`````{py:class} Isource(api_util, ptr)
:canonical: altdss.Isource.Isource

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`

```{autodoc2-docstring} altdss.Isource.Isource
```

````{py:attribute} Amps
:canonical: altdss.Isource.Isource.Amps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Amps
```

````

````{py:attribute} Angle
:canonical: altdss.Isource.Isource.Angle
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Isource.Isource.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Isource.Isource.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Isource.Isource.Bus2
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Bus2
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Isource.Isource.Close

```{autodoc2-docstring} altdss.Isource.Isource.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Isource.Isource.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Isource.Isource.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Isource.Isource.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Isource.Isource.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Isource.Isource.Currents

```{autodoc2-docstring} altdss.Isource.Isource.Currents
```

````

````{py:attribute} Daily
:canonical: altdss.Isource.Isource.Daily
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Isource.Isource.Daily_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Daily_str
```

````

````{py:attribute} DisplayName
:canonical: altdss.Isource.Isource.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.DisplayName
```

````

````{py:attribute} Duty
:canonical: altdss.Isource.Isource.Duty
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Isource.Isource.Duty_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Isource.Isource.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.Isource.Isource.EnergyMeter

```{autodoc2-docstring} altdss.Isource.Isource.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Isource.Isource.EnergyMeterName

```{autodoc2-docstring} altdss.Isource.Isource.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.Isource.Isource.Frequency
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Frequency
```

````

````{py:method} FullName() -> str
:canonical: altdss.Isource.Isource.FullName

```{autodoc2-docstring} altdss.Isource.Isource.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Isource.Isource.GUID

```{autodoc2-docstring} altdss.Isource.Isource.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.Isource.Isource.GetVariableValue

```{autodoc2-docstring} altdss.Isource.Isource.GetVariableValue
```

````

````{py:method} Handle() -> int
:canonical: altdss.Isource.Isource.Handle

```{autodoc2-docstring} altdss.Isource.Isource.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Isource.Isource.HasOCPDevice

```{autodoc2-docstring} altdss.Isource.Isource.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Isource.Isource.HasSwitchControl

```{autodoc2-docstring} altdss.Isource.Isource.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Isource.Isource.HasVoltControl

```{autodoc2-docstring} altdss.Isource.Isource.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Isource.Isource.IsIsolated

```{autodoc2-docstring} altdss.Isource.Isource.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Isource.Isource.IsOpen

```{autodoc2-docstring} altdss.Isource.Isource.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Isource.Isource.Like

```{autodoc2-docstring} altdss.Isource.Isource.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Isource.Isource.Losses

```{autodoc2-docstring} altdss.Isource.Isource.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Isource.Isource.MaxCurrent

```{autodoc2-docstring} altdss.Isource.Isource.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Isource.Isource.Name
:type: str

```{autodoc2-docstring} altdss.Isource.Isource.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Isource.Isource.NodeOrder

```{autodoc2-docstring} altdss.Isource.Isource.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Isource.Isource.NodeRef

```{autodoc2-docstring} altdss.Isource.Isource.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Isource.Isource.NumConductors

```{autodoc2-docstring} altdss.Isource.Isource.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Isource.Isource.NumControllers

```{autodoc2-docstring} altdss.Isource.Isource.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Isource.Isource.NumPhases

```{autodoc2-docstring} altdss.Isource.Isource.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Isource.Isource.NumTerminals

```{autodoc2-docstring} altdss.Isource.Isource.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Isource.Isource.OCPDevice

```{autodoc2-docstring} altdss.Isource.Isource.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Isource.Isource.OCPDeviceIndex

```{autodoc2-docstring} altdss.Isource.Isource.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Isource.Isource.OCPDeviceType

```{autodoc2-docstring} altdss.Isource.Isource.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Isource.Isource.Open

```{autodoc2-docstring} altdss.Isource.Isource.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Isource.Isource.PhaseLosses

```{autodoc2-docstring} altdss.Isource.Isource.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Isource.Isource.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Isource.Isource.Powers

```{autodoc2-docstring} altdss.Isource.Isource.Powers
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Isource.Isource.Residuals

```{autodoc2-docstring} altdss.Isource.Isource.Residuals
```

````

````{py:attribute} ScanType
:canonical: altdss.Isource.Isource.ScanType
:type: altdss.enums.ScanType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.ScanType
```

````

````{py:attribute} ScanType_str
:canonical: altdss.Isource.Isource.ScanType_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.ScanType_str
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Isource.Isource.SeqCurrents

```{autodoc2-docstring} altdss.Isource.Isource.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Isource.Isource.SeqPowers

```{autodoc2-docstring} altdss.Isource.Isource.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Isource.Isource.SeqVoltages

```{autodoc2-docstring} altdss.Isource.Isource.SeqVoltages
```

````

````{py:attribute} Sequence
:canonical: altdss.Isource.Isource.Sequence
:type: altdss.enums.SequenceType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Sequence
```

````

````{py:attribute} Sequence_str
:canonical: altdss.Isource.Isource.Sequence_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Sequence_str
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.Isource.Isource.SetVariableValue

```{autodoc2-docstring} altdss.Isource.Isource.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.Isource.Isource.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Isource.Isource.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Isource.Isource.TotalPowers

```{autodoc2-docstring} altdss.Isource.Isource.TotalPowers
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.Isource.Isource.VariableNames

```{autodoc2-docstring} altdss.Isource.Isource.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.Isource.Isource.VariableValues

```{autodoc2-docstring} altdss.Isource.Isource.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.Isource.Isource.VariablesDict

```{autodoc2-docstring} altdss.Isource.Isource.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Isource.Isource.Voltages

```{autodoc2-docstring} altdss.Isource.Isource.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Isource.Isource.VoltagesMagAng

```{autodoc2-docstring} altdss.Isource.Isource.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Isource.Isource.YPrim

```{autodoc2-docstring} altdss.Isource.Isource.YPrim
```

````

````{py:attribute} Yearly
:canonical: altdss.Isource.Isource.Yearly
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Isource.Isource.Yearly_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.Isource.Yearly_str
```

````

````{py:method} __hash__()
:canonical: altdss.Isource.Isource.__hash__

```{autodoc2-docstring} altdss.Isource.Isource.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Isource.Isource.__init__

```{autodoc2-docstring} altdss.Isource.Isource.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Isource.Isource.__ne__

```{autodoc2-docstring} altdss.Isource.Isource.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Isource.Isource.__repr__

```{autodoc2-docstring} altdss.Isource.Isource.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Isource.Isource.begin_edit

```{autodoc2-docstring} altdss.Isource.Isource.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Isource.Isource.end_edit

```{autodoc2-docstring} altdss.Isource.Isource.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Isource.Isource.to_json

```{autodoc2-docstring} altdss.Isource.Isource.to_json
```

````

`````

`````{py:class} IsourceBatch(api_util, **kwargs)
:canonical: altdss.Isource.IsourceBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.Isource.IsourceBatch
```

````{py:attribute} Amps
:canonical: altdss.Isource.IsourceBatch.Amps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Amps
```

````

````{py:attribute} Angle
:canonical: altdss.Isource.IsourceBatch.Angle
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Isource.IsourceBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Isource.IsourceBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Isource.IsourceBatch.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Bus2
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IsourceBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Isource.IsourceBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IsourceBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Isource.IsourceBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IsourceBatch.Currents

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Isource.IsourceBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Isource.IsourceBatch.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.Isource.IsourceBatch.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Isource.IsourceBatch.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Daily_str
```

````

````{py:attribute} Duty
:canonical: altdss.Isource.IsourceBatch.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Isource.IsourceBatch.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Isource.IsourceBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Isource.IsourceBatch.EnergyMeter

```{autodoc2-docstring} altdss.Isource.IsourceBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Isource.IsourceBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Isource.IsourceBatch.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.Isource.IsourceBatch.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Isource.IsourceBatch.FullName

```{autodoc2-docstring} altdss.Isource.IsourceBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Isource.IsourceBatch.GUID

```{autodoc2-docstring} altdss.Isource.IsourceBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Isource.IsourceBatch.Handle

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Isource.IsourceBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Isource.IsourceBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Isource.IsourceBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Isource.IsourceBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Isource.IsourceBatch.HasVoltControl

```{autodoc2-docstring} altdss.Isource.IsourceBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Isource.IsourceBatch.IsIsolated

```{autodoc2-docstring} altdss.Isource.IsourceBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Isource.IsourceBatch.Like

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IsourceBatch.Losses

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Isource.IsourceBatch.MaxCurrent

```{autodoc2-docstring} altdss.Isource.IsourceBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Isource.IsourceBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Isource.IsourceBatch.NumConductors

```{autodoc2-docstring} altdss.Isource.IsourceBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Isource.IsourceBatch.NumControllers

```{autodoc2-docstring} altdss.Isource.IsourceBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Isource.IsourceBatch.NumPhases

```{autodoc2-docstring} altdss.Isource.IsourceBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Isource.IsourceBatch.NumTerminals

```{autodoc2-docstring} altdss.Isource.IsourceBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Isource.IsourceBatch.OCPDevice

```{autodoc2-docstring} altdss.Isource.IsourceBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Isource.IsourceBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Isource.IsourceBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Isource.IsourceBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Isource.IsourceBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IsourceBatch.PhaseLosses

```{autodoc2-docstring} altdss.Isource.IsourceBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Isource.IsourceBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IsourceBatch.Powers

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Powers
```

````

````{py:attribute} ScanType
:canonical: altdss.Isource.IsourceBatch.ScanType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.ScanType
```

````

````{py:attribute} ScanType_str
:canonical: altdss.Isource.IsourceBatch.ScanType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.ScanType_str
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Isource.IsourceBatch.SeqCurrents

```{autodoc2-docstring} altdss.Isource.IsourceBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IsourceBatch.SeqPowers

```{autodoc2-docstring} altdss.Isource.IsourceBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Isource.IsourceBatch.SeqVoltages

```{autodoc2-docstring} altdss.Isource.IsourceBatch.SeqVoltages
```

````

````{py:attribute} Sequence
:canonical: altdss.Isource.IsourceBatch.Sequence
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Sequence
```

````

````{py:attribute} Sequence_str
:canonical: altdss.Isource.IsourceBatch.Sequence_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Sequence_str
```

````

````{py:attribute} Spectrum
:canonical: altdss.Isource.IsourceBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Isource.IsourceBatch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IsourceBatch.TotalPowers

```{autodoc2-docstring} altdss.Isource.IsourceBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Isource.IsourceBatch.Voltages

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Isource.IsourceBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Isource.IsourceBatch.VoltagesMagAng
```

````

````{py:attribute} Yearly
:canonical: altdss.Isource.IsourceBatch.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Isource.IsourceBatch.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Isource.IsourceBatch.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.Isource.IsourceBatch.__call__

```{autodoc2-docstring} altdss.Isource.IsourceBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Isource.IsourceBatch.__getitem__

```{autodoc2-docstring} altdss.Isource.IsourceBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Isource.IsourceBatch.__init__

```{autodoc2-docstring} altdss.Isource.IsourceBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Isource.IsourceBatch.__iter__

```{autodoc2-docstring} altdss.Isource.IsourceBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Isource.IsourceBatch.__len__

```{autodoc2-docstring} altdss.Isource.IsourceBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Isource.IsourceBatch.batch

```{autodoc2-docstring} altdss.Isource.IsourceBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Isource.IsourceBatch.begin_edit

```{autodoc2-docstring} altdss.Isource.IsourceBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Isource.IsourceBatch.end_edit

```{autodoc2-docstring} altdss.Isource.IsourceBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Isource.IsourceBatch.to_json

```{autodoc2-docstring} altdss.Isource.IsourceBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Isource.IsourceBatch.to_list

```{autodoc2-docstring} altdss.Isource.IsourceBatch.to_list
```

````

`````

`````{py:class} IsourceBatchProperties()
:canonical: altdss.Isource.IsourceBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties
```

````{py:attribute} Amps
:canonical: altdss.Isource.IsourceBatchProperties.Amps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Amps
```

````

````{py:attribute} Angle
:canonical: altdss.Isource.IsourceBatchProperties.Angle
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Isource.IsourceBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Isource.IsourceBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Isource.IsourceBatchProperties.Bus2
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Bus2
```

````

````{py:attribute} Daily
:canonical: altdss.Isource.IsourceBatchProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Daily
```

````

````{py:attribute} Duty
:canonical: altdss.Isource.IsourceBatchProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Duty
```

````

````{py:attribute} Enabled
:canonical: altdss.Isource.IsourceBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.Isource.IsourceBatchProperties.Frequency
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Frequency
```

````

````{py:attribute} Like
:canonical: altdss.Isource.IsourceBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Like
```

````

````{py:attribute} Phases
:canonical: altdss.Isource.IsourceBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Phases
```

````

````{py:attribute} ScanType
:canonical: altdss.Isource.IsourceBatchProperties.ScanType
:type: typing.Union[typing.AnyStr, int, altdss.enums.ScanType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.ScanType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.ScanType
```

````

````{py:attribute} Sequence
:canonical: altdss.Isource.IsourceBatchProperties.Sequence
:type: typing.Union[typing.AnyStr, int, altdss.enums.SequenceType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.SequenceType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Sequence
```

````

````{py:attribute} Spectrum
:canonical: altdss.Isource.IsourceBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Spectrum
```

````

````{py:attribute} Yearly
:canonical: altdss.Isource.IsourceBatchProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.Isource.IsourceBatchProperties.__contains__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Isource.IsourceBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Isource.IsourceBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Isource.IsourceBatchProperties.__dir__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Isource.IsourceBatchProperties.__format__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Isource.IsourceBatchProperties.__ge__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Isource.IsourceBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Isource.IsourceBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Isource.IsourceBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Isource.IsourceBatchProperties.__gt__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Isource.IsourceBatchProperties.__init__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Isource.IsourceBatchProperties.__ior__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Isource.IsourceBatchProperties.__iter__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Isource.IsourceBatchProperties.__le__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Isource.IsourceBatchProperties.__len__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Isource.IsourceBatchProperties.__lt__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Isource.IsourceBatchProperties.__ne__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Isource.IsourceBatchProperties.__new__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Isource.IsourceBatchProperties.__or__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Isource.IsourceBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Isource.IsourceBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Isource.IsourceBatchProperties.__repr__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Isource.IsourceBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Isource.IsourceBatchProperties.__ror__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Isource.IsourceBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Isource.IsourceBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Isource.IsourceBatchProperties.__str__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Isource.IsourceBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Isource.IsourceBatchProperties.clear

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Isource.IsourceBatchProperties.copy

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Isource.IsourceBatchProperties.get

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Isource.IsourceBatchProperties.items

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Isource.IsourceBatchProperties.keys

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Isource.IsourceBatchProperties.pop

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Isource.IsourceBatchProperties.popitem

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Isource.IsourceBatchProperties.setdefault

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Isource.IsourceBatchProperties.update

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Isource.IsourceBatchProperties.values

```{autodoc2-docstring} altdss.Isource.IsourceBatchProperties.values
```

````

`````

`````{py:class} IsourceProperties()
:canonical: altdss.Isource.IsourceProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Isource.IsourceProperties
```

````{py:attribute} Amps
:canonical: altdss.Isource.IsourceProperties.Amps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Amps
```

````

````{py:attribute} Angle
:canonical: altdss.Isource.IsourceProperties.Angle
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Isource.IsourceProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Isource.IsourceProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Isource.IsourceProperties.Bus2
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Bus2
```

````

````{py:attribute} Daily
:canonical: altdss.Isource.IsourceProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Daily
```

````

````{py:attribute} Duty
:canonical: altdss.Isource.IsourceProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Duty
```

````

````{py:attribute} Enabled
:canonical: altdss.Isource.IsourceProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.Isource.IsourceProperties.Frequency
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Frequency
```

````

````{py:attribute} Like
:canonical: altdss.Isource.IsourceProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Like
```

````

````{py:attribute} Phases
:canonical: altdss.Isource.IsourceProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Phases
```

````

````{py:attribute} ScanType
:canonical: altdss.Isource.IsourceProperties.ScanType
:type: typing.Union[typing.AnyStr, int, altdss.enums.ScanType]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.ScanType
```

````

````{py:attribute} Sequence
:canonical: altdss.Isource.IsourceProperties.Sequence
:type: typing.Union[typing.AnyStr, int, altdss.enums.SequenceType]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Sequence
```

````

````{py:attribute} Spectrum
:canonical: altdss.Isource.IsourceProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Spectrum
```

````

````{py:attribute} Yearly
:canonical: altdss.Isource.IsourceProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Isource.IsourceProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.Isource.IsourceProperties.__contains__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Isource.IsourceProperties.__delattr__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Isource.IsourceProperties.__delitem__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Isource.IsourceProperties.__dir__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Isource.IsourceProperties.__format__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Isource.IsourceProperties.__ge__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Isource.IsourceProperties.__getattribute__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Isource.IsourceProperties.__getitem__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Isource.IsourceProperties.__getstate__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Isource.IsourceProperties.__gt__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Isource.IsourceProperties.__init__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Isource.IsourceProperties.__ior__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Isource.IsourceProperties.__iter__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Isource.IsourceProperties.__le__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Isource.IsourceProperties.__len__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Isource.IsourceProperties.__lt__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Isource.IsourceProperties.__ne__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Isource.IsourceProperties.__new__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Isource.IsourceProperties.__or__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Isource.IsourceProperties.__reduce__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Isource.IsourceProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Isource.IsourceProperties.__repr__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Isource.IsourceProperties.__reversed__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Isource.IsourceProperties.__ror__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Isource.IsourceProperties.__setitem__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Isource.IsourceProperties.__sizeof__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Isource.IsourceProperties.__str__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Isource.IsourceProperties.__subclasshook__

```{autodoc2-docstring} altdss.Isource.IsourceProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Isource.IsourceProperties.clear

```{autodoc2-docstring} altdss.Isource.IsourceProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Isource.IsourceProperties.copy

```{autodoc2-docstring} altdss.Isource.IsourceProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Isource.IsourceProperties.get

```{autodoc2-docstring} altdss.Isource.IsourceProperties.get
```

````

````{py:method} items()
:canonical: altdss.Isource.IsourceProperties.items

```{autodoc2-docstring} altdss.Isource.IsourceProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Isource.IsourceProperties.keys

```{autodoc2-docstring} altdss.Isource.IsourceProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Isource.IsourceProperties.pop

```{autodoc2-docstring} altdss.Isource.IsourceProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Isource.IsourceProperties.popitem

```{autodoc2-docstring} altdss.Isource.IsourceProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Isource.IsourceProperties.setdefault

```{autodoc2-docstring} altdss.Isource.IsourceProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Isource.IsourceProperties.update

```{autodoc2-docstring} altdss.Isource.IsourceProperties.update
```

````

````{py:method} values()
:canonical: altdss.Isource.IsourceProperties.values

```{autodoc2-docstring} altdss.Isource.IsourceProperties.values
```

````

`````
