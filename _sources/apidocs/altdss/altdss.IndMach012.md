# {py:mod}`altdss.IndMach012`

```{py:module} altdss.IndMach012
```

```{autodoc2-docstring} altdss.IndMach012
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IIndMach012 <altdss.IndMach012.IIndMach012>`
  - ```{autodoc2-docstring} altdss.IndMach012.IIndMach012
    :summary:
    ```
* - {py:obj}`IndMach012 <altdss.IndMach012.IndMach012>`
  - ```{autodoc2-docstring} altdss.IndMach012.IndMach012
    :summary:
    ```
* - {py:obj}`IndMach012Batch <altdss.IndMach012.IndMach012Batch>`
  - ```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch
    :summary:
    ```
* - {py:obj}`IndMach012BatchProperties <altdss.IndMach012.IndMach012BatchProperties>`
  - ```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties
    :summary:
    ```
* - {py:obj}`IndMach012Properties <altdss.IndMach012.IndMach012Properties>`
  - ```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties
    :summary:
    ```
````

### API

`````{py:class} IIndMach012(iobj)
:canonical: altdss.IndMach012.IIndMach012

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.IndMach012.IndMach012Batch`

```{autodoc2-docstring} altdss.IndMach012.IIndMach012
```

````{py:attribute} BaseFreq
:canonical: altdss.IndMach012.IIndMach012.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.IndMach012.IIndMach012.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Bus1
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IIndMach012.ComplexSeqCurrents

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IIndMach012.ComplexSeqVoltages

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.IndMach012.IIndMach012.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.IndMach012.IIndMach012.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IIndMach012.Currents

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IIndMach012.CurrentsMagAng

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.CurrentsMagAng
```

````

````{py:attribute} D
:canonical: altdss.IndMach012.IIndMach012.D
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.D
```

````

````{py:attribute} Daily
:canonical: altdss.IndMach012.IIndMach012.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.IndMach012.IIndMach012.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.IndMach012.IIndMach012.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.DebugTrace
```

````

````{py:attribute} Duty
:canonical: altdss.IndMach012.IIndMach012.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.IndMach012.IIndMach012.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.IndMach012.IIndMach012.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.IndMach012.IIndMach012.EnergyMeter

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.IndMach012.IIndMach012.EnergyMeterName

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.IndMach012.IIndMach012.FullName

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.IndMach012.IIndMach012.GUID

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.GUID
```

````

````{py:attribute} H
:canonical: altdss.IndMach012.IIndMach012.H
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.H
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IIndMach012.Handle

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.IndMach012.IIndMach012.HasOCPDevice

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.IndMach012.IIndMach012.HasSwitchControl

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.IndMach012.IIndMach012.HasVoltControl

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.IndMach012.IIndMach012.IsIsolated

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.IndMach012.IIndMach012.Like

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IIndMach012.Losses

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IIndMach012.MaxCurrent

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.MaxCurrent
```

````

````{py:attribute} MaxSlip
:canonical: altdss.IndMach012.IIndMach012.MaxSlip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.MaxSlip
```

````

````{py:property} Name
:canonical: altdss.IndMach012.IIndMach012.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IIndMach012.NumConductors

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IIndMach012.NumControllers

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IIndMach012.NumPhases

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IIndMach012.NumTerminals

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.IndMach012.IIndMach012.OCPDevice

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IIndMach012.OCPDeviceIndex

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.IndMach012.IIndMach012.OCPDeviceType

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.IndMach012.IIndMach012.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.PF
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IIndMach012.PhaseLosses

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.IndMach012.IIndMach012.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IIndMach012.Powers

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IIndMach012.SeqCurrents

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IIndMach012.SeqPowers

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IIndMach012.SeqVoltages

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.SeqVoltages
```

````

````{py:attribute} Slip
:canonical: altdss.IndMach012.IIndMach012.Slip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Slip
```

````

````{py:attribute} SlipOption
:canonical: altdss.IndMach012.IIndMach012.SlipOption
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.SlipOption
```

````

````{py:attribute} SlipOption_str
:canonical: altdss.IndMach012.IIndMach012.SlipOption_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.SlipOption_str
```

````

````{py:attribute} Spectrum
:canonical: altdss.IndMach012.IIndMach012.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.IndMach012.IIndMach012.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IIndMach012.TotalPowers

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IIndMach012.Voltages

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IIndMach012.VoltagesMagAng

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.VoltagesMagAng
```

````

````{py:attribute} Yearly
:canonical: altdss.IndMach012.IIndMach012.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.IndMach012.IIndMach012.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.IndMach012.IIndMach012.__call__

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.IndMach012.IIndMach012.__contains__

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.IndMach012.IIndMach012.__getitem__

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.IndMach012.IIndMach012.__init__

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.IndMach012.IIndMach012.__iter__

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.IndMach012.IIndMach012.__len__

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.IndMach012.IIndMach012.batch

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.IndMach012.IndMach012BatchProperties]) -> altdss.IndMach012.IndMach012Batch
:canonical: altdss.IndMach012.IIndMach012.batch_new

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.IndMach012.IIndMach012.begin_edit

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.IndMach012.IndMach012BatchProperties]) -> altdss.IndMach012.IndMach012Batch
:canonical: altdss.IndMach012.IIndMach012.edit

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.IndMach012.IIndMach012.end_edit

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.IndMach012.IIndMach012.find

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.find
```

````

````{py:attribute} kV
:canonical: altdss.IndMach012.IIndMach012.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.kV
```

````

````{py:attribute} kVA
:canonical: altdss.IndMach012.IIndMach012.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.kVA
```

````

````{py:attribute} kW
:canonical: altdss.IndMach012.IIndMach012.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.kW
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.IndMach012.IndMach012Properties]) -> altdss.IndMach012.IndMach012
:canonical: altdss.IndMach012.IIndMach012.new

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.new
```

````

````{py:attribute} puRr
:canonical: altdss.IndMach012.IIndMach012.puRr
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.puRr
```

````

````{py:attribute} puRs
:canonical: altdss.IndMach012.IIndMach012.puRs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.puRs
```

````

````{py:attribute} puXm
:canonical: altdss.IndMach012.IIndMach012.puXm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.puXm
```

````

````{py:attribute} puXr
:canonical: altdss.IndMach012.IIndMach012.puXr
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.puXr
```

````

````{py:attribute} puXs
:canonical: altdss.IndMach012.IIndMach012.puXs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.puXs
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.IndMach012.IIndMach012.to_json

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.to_json
```

````

````{py:method} to_list()
:canonical: altdss.IndMach012.IIndMach012.to_list

```{autodoc2-docstring} altdss.IndMach012.IIndMach012.to_list
```

````

`````

`````{py:class} IndMach012(api_util, ptr)
:canonical: altdss.IndMach012.IndMach012

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`

```{autodoc2-docstring} altdss.IndMach012.IndMach012
```

````{py:attribute} BaseFreq
:canonical: altdss.IndMach012.IndMach012.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.IndMach012.IndMach012.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Bus1
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.IndMach012.IndMach012.Close

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012.ComplexSeqCurrents

```{autodoc2-docstring} altdss.IndMach012.IndMach012.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012.ComplexSeqVoltages

```{autodoc2-docstring} altdss.IndMach012.IndMach012.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.IndMach012.IndMach012.Conn
:type: altdss.enums.Connection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.IndMach012.IndMach012.Conn_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012.Currents

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Currents
```

````

````{py:attribute} D
:canonical: altdss.IndMach012.IndMach012.D
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.D
```

````

````{py:attribute} Daily
:canonical: altdss.IndMach012.IndMach012.Daily
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.IndMach012.IndMach012.Daily_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.IndMach012.IndMach012.DebugTrace
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.DebugTrace
```

````

````{py:attribute} DisplayName
:canonical: altdss.IndMach012.IndMach012.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.DisplayName
```

````

````{py:attribute} Duty
:canonical: altdss.IndMach012.IndMach012.Duty
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.IndMach012.IndMach012.Duty_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.IndMach012.IndMach012.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.IndMach012.IndMach012.EnergyMeter

```{autodoc2-docstring} altdss.IndMach012.IndMach012.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.IndMach012.IndMach012.EnergyMeterName

```{autodoc2-docstring} altdss.IndMach012.IndMach012.EnergyMeterName
```

````

````{py:method} FullName() -> str
:canonical: altdss.IndMach012.IndMach012.FullName

```{autodoc2-docstring} altdss.IndMach012.IndMach012.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.IndMach012.IndMach012.GUID

```{autodoc2-docstring} altdss.IndMach012.IndMach012.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.IndMach012.IndMach012.GetVariableValue

```{autodoc2-docstring} altdss.IndMach012.IndMach012.GetVariableValue
```

````

````{py:attribute} H
:canonical: altdss.IndMach012.IndMach012.H
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.H
```

````

````{py:method} Handle() -> int
:canonical: altdss.IndMach012.IndMach012.Handle

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.IndMach012.IndMach012.HasOCPDevice

```{autodoc2-docstring} altdss.IndMach012.IndMach012.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.IndMach012.IndMach012.HasSwitchControl

```{autodoc2-docstring} altdss.IndMach012.IndMach012.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.IndMach012.IndMach012.HasVoltControl

```{autodoc2-docstring} altdss.IndMach012.IndMach012.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.IndMach012.IndMach012.IsIsolated

```{autodoc2-docstring} altdss.IndMach012.IndMach012.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.IndMach012.IndMach012.IsOpen

```{autodoc2-docstring} altdss.IndMach012.IndMach012.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.IndMach012.IndMach012.Like

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.IndMach012.IndMach012.Losses

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.IndMach012.IndMach012.MaxCurrent

```{autodoc2-docstring} altdss.IndMach012.IndMach012.MaxCurrent
```

````

````{py:attribute} MaxSlip
:canonical: altdss.IndMach012.IndMach012.MaxSlip
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.MaxSlip
```

````

````{py:property} Name
:canonical: altdss.IndMach012.IndMach012.Name
:type: str

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IndMach012.NodeOrder

```{autodoc2-docstring} altdss.IndMach012.IndMach012.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IndMach012.NodeRef

```{autodoc2-docstring} altdss.IndMach012.IndMach012.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.IndMach012.IndMach012.NumConductors

```{autodoc2-docstring} altdss.IndMach012.IndMach012.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.IndMach012.IndMach012.NumControllers

```{autodoc2-docstring} altdss.IndMach012.IndMach012.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.IndMach012.IndMach012.NumPhases

```{autodoc2-docstring} altdss.IndMach012.IndMach012.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.IndMach012.IndMach012.NumTerminals

```{autodoc2-docstring} altdss.IndMach012.IndMach012.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.IndMach012.IndMach012.OCPDevice

```{autodoc2-docstring} altdss.IndMach012.IndMach012.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.IndMach012.IndMach012.OCPDeviceIndex

```{autodoc2-docstring} altdss.IndMach012.IndMach012.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.IndMach012.IndMach012.OCPDeviceType

```{autodoc2-docstring} altdss.IndMach012.IndMach012.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.IndMach012.IndMach012.Open

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Open
```

````

````{py:attribute} PF
:canonical: altdss.IndMach012.IndMach012.PF
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.PF
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012.PhaseLosses

```{autodoc2-docstring} altdss.IndMach012.IndMach012.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.IndMach012.IndMach012.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012.Powers

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Powers
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012.Residuals

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012.SeqCurrents

```{autodoc2-docstring} altdss.IndMach012.IndMach012.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012.SeqPowers

```{autodoc2-docstring} altdss.IndMach012.IndMach012.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012.SeqVoltages

```{autodoc2-docstring} altdss.IndMach012.IndMach012.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.IndMach012.IndMach012.SetVariableValue

```{autodoc2-docstring} altdss.IndMach012.IndMach012.SetVariableValue
```

````

````{py:attribute} Slip
:canonical: altdss.IndMach012.IndMach012.Slip
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Slip
```

````

````{py:attribute} SlipOption
:canonical: altdss.IndMach012.IndMach012.SlipOption
:type: altdss.enums.IndMach012SlipOption
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.SlipOption
```

````

````{py:attribute} SlipOption_str
:canonical: altdss.IndMach012.IndMach012.SlipOption_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.SlipOption_str
```

````

````{py:attribute} Spectrum
:canonical: altdss.IndMach012.IndMach012.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.IndMach012.IndMach012.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012.TotalPowers

```{autodoc2-docstring} altdss.IndMach012.IndMach012.TotalPowers
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.IndMach012.IndMach012.VariableNames

```{autodoc2-docstring} altdss.IndMach012.IndMach012.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012.VariableValues

```{autodoc2-docstring} altdss.IndMach012.IndMach012.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.IndMach012.IndMach012.VariablesDict

```{autodoc2-docstring} altdss.IndMach012.IndMach012.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012.Voltages

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012.VoltagesMagAng

```{autodoc2-docstring} altdss.IndMach012.IndMach012.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012.YPrim

```{autodoc2-docstring} altdss.IndMach012.IndMach012.YPrim
```

````

````{py:attribute} Yearly
:canonical: altdss.IndMach012.IndMach012.Yearly
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.IndMach012.IndMach012.Yearly_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.Yearly_str
```

````

````{py:method} __hash__()
:canonical: altdss.IndMach012.IndMach012.__hash__

```{autodoc2-docstring} altdss.IndMach012.IndMach012.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.IndMach012.IndMach012.__init__

```{autodoc2-docstring} altdss.IndMach012.IndMach012.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.IndMach012.IndMach012.__ne__

```{autodoc2-docstring} altdss.IndMach012.IndMach012.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.IndMach012.IndMach012.__repr__

```{autodoc2-docstring} altdss.IndMach012.IndMach012.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.IndMach012.IndMach012.begin_edit

```{autodoc2-docstring} altdss.IndMach012.IndMach012.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.IndMach012.IndMach012Properties]) -> altdss.IndMach012.IndMach012
:canonical: altdss.IndMach012.IndMach012.edit

```{autodoc2-docstring} altdss.IndMach012.IndMach012.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.IndMach012.IndMach012.end_edit

```{autodoc2-docstring} altdss.IndMach012.IndMach012.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.IndMach012.IndMach012.kV
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.kV
```

````

````{py:attribute} kVA
:canonical: altdss.IndMach012.IndMach012.kVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.kVA
```

````

````{py:attribute} kW
:canonical: altdss.IndMach012.IndMach012.kW
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.kW
```

````

````{py:attribute} puRr
:canonical: altdss.IndMach012.IndMach012.puRr
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.puRr
```

````

````{py:attribute} puRs
:canonical: altdss.IndMach012.IndMach012.puRs
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.puRs
```

````

````{py:attribute} puXm
:canonical: altdss.IndMach012.IndMach012.puXm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.puXm
```

````

````{py:attribute} puXr
:canonical: altdss.IndMach012.IndMach012.puXr
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.puXr
```

````

````{py:attribute} puXs
:canonical: altdss.IndMach012.IndMach012.puXs
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012.puXs
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.IndMach012.IndMach012.to_json

```{autodoc2-docstring} altdss.IndMach012.IndMach012.to_json
```

````

`````

`````{py:class} IndMach012Batch(api_util, **kwargs)
:canonical: altdss.IndMach012.IndMach012Batch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch
```

````{py:attribute} BaseFreq
:canonical: altdss.IndMach012.IndMach012Batch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.IndMach012.IndMach012Batch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Bus1
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012Batch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012Batch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.IndMach012.IndMach012Batch.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.IndMach012.IndMach012Batch.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012Batch.Currents

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012Batch.CurrentsMagAng

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.CurrentsMagAng
```

````

````{py:attribute} D
:canonical: altdss.IndMach012.IndMach012Batch.D
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.D
```

````

````{py:attribute} Daily
:canonical: altdss.IndMach012.IndMach012Batch.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.IndMach012.IndMach012Batch.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.IndMach012.IndMach012Batch.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.DebugTrace
```

````

````{py:attribute} Duty
:canonical: altdss.IndMach012.IndMach012Batch.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.IndMach012.IndMach012Batch.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.IndMach012.IndMach012Batch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.IndMach012.IndMach012Batch.EnergyMeter

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.IndMach012.IndMach012Batch.EnergyMeterName

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.IndMach012.IndMach012Batch.FullName

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.IndMach012.IndMach012Batch.GUID

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.GUID
```

````

````{py:attribute} H
:canonical: altdss.IndMach012.IndMach012Batch.H
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.H
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IndMach012Batch.Handle

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.IndMach012.IndMach012Batch.HasOCPDevice

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.IndMach012.IndMach012Batch.HasSwitchControl

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.IndMach012.IndMach012Batch.HasVoltControl

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.IndMach012.IndMach012Batch.IsIsolated

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.IndMach012.IndMach012Batch.Like

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012Batch.Losses

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012Batch.MaxCurrent

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.MaxCurrent
```

````

````{py:attribute} MaxSlip
:canonical: altdss.IndMach012.IndMach012Batch.MaxSlip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.MaxSlip
```

````

````{py:property} Name
:canonical: altdss.IndMach012.IndMach012Batch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IndMach012Batch.NumConductors

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IndMach012Batch.NumControllers

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IndMach012Batch.NumPhases

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IndMach012Batch.NumTerminals

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.IndMach012.IndMach012Batch.OCPDevice

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.IndMach012.IndMach012Batch.OCPDeviceIndex

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.IndMach012.IndMach012Batch.OCPDeviceType

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.IndMach012.IndMach012Batch.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.PF
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012Batch.PhaseLosses

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.IndMach012.IndMach012Batch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012Batch.Powers

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Powers
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012Batch.SeqCurrents

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012Batch.SeqPowers

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012Batch.SeqVoltages

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.SeqVoltages
```

````

````{py:attribute} Slip
:canonical: altdss.IndMach012.IndMach012Batch.Slip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Slip
```

````

````{py:attribute} SlipOption
:canonical: altdss.IndMach012.IndMach012Batch.SlipOption
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.SlipOption
```

````

````{py:attribute} SlipOption_str
:canonical: altdss.IndMach012.IndMach012Batch.SlipOption_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.SlipOption_str
```

````

````{py:attribute} Spectrum
:canonical: altdss.IndMach012.IndMach012Batch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.IndMach012.IndMach012Batch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012Batch.TotalPowers

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.IndMach012.IndMach012Batch.Voltages

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.IndMach012.IndMach012Batch.VoltagesMagAng

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.VoltagesMagAng
```

````

````{py:attribute} Yearly
:canonical: altdss.IndMach012.IndMach012Batch.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.IndMach012.IndMach012Batch.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.IndMach012.IndMach012Batch.__call__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.IndMach012.IndMach012Batch.__getitem__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.IndMach012.IndMach012Batch.__init__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.IndMach012.IndMach012Batch.__iter__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.IndMach012.IndMach012Batch.__len__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.IndMach012.IndMach012Batch.batch

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.IndMach012.IndMach012Batch.begin_edit

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.IndMach012.IndMach012BatchProperties]) -> altdss.IndMach012.IndMach012Batch
:canonical: altdss.IndMach012.IndMach012Batch.edit

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.IndMach012.IndMach012Batch.end_edit

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.IndMach012.IndMach012Batch.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.kV
```

````

````{py:attribute} kVA
:canonical: altdss.IndMach012.IndMach012Batch.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.kVA
```

````

````{py:attribute} kW
:canonical: altdss.IndMach012.IndMach012Batch.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.kW
```

````

````{py:attribute} puRr
:canonical: altdss.IndMach012.IndMach012Batch.puRr
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.puRr
```

````

````{py:attribute} puRs
:canonical: altdss.IndMach012.IndMach012Batch.puRs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.puRs
```

````

````{py:attribute} puXm
:canonical: altdss.IndMach012.IndMach012Batch.puXm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.puXm
```

````

````{py:attribute} puXr
:canonical: altdss.IndMach012.IndMach012Batch.puXr
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.puXr
```

````

````{py:attribute} puXs
:canonical: altdss.IndMach012.IndMach012Batch.puXs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.puXs
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.IndMach012.IndMach012Batch.to_json

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.IndMach012.IndMach012Batch.to_list

```{autodoc2-docstring} altdss.IndMach012.IndMach012Batch.to_list
```

````

`````

`````{py:class} IndMach012BatchProperties()
:canonical: altdss.IndMach012.IndMach012BatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.IndMach012.IndMach012BatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.IndMach012.IndMach012BatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Bus1
```

````

````{py:attribute} Conn
:canonical: altdss.IndMach012.IndMach012BatchProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.Connection], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Conn
```

````

````{py:attribute} D
:canonical: altdss.IndMach012.IndMach012BatchProperties.D
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.D
```

````

````{py:attribute} Daily
:canonical: altdss.IndMach012.IndMach012BatchProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Daily
```

````

````{py:attribute} DebugTrace
:canonical: altdss.IndMach012.IndMach012BatchProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.DebugTrace
```

````

````{py:attribute} Duty
:canonical: altdss.IndMach012.IndMach012BatchProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Duty
```

````

````{py:attribute} Enabled
:canonical: altdss.IndMach012.IndMach012BatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Enabled
```

````

````{py:attribute} H
:canonical: altdss.IndMach012.IndMach012BatchProperties.H
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.H
```

````

````{py:attribute} Like
:canonical: altdss.IndMach012.IndMach012BatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Like
```

````

````{py:attribute} MaxSlip
:canonical: altdss.IndMach012.IndMach012BatchProperties.MaxSlip
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.MaxSlip
```

````

````{py:attribute} PF
:canonical: altdss.IndMach012.IndMach012BatchProperties.PF
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.PF
```

````

````{py:attribute} Phases
:canonical: altdss.IndMach012.IndMach012BatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Phases
```

````

````{py:attribute} Slip
:canonical: altdss.IndMach012.IndMach012BatchProperties.Slip
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Slip
```

````

````{py:attribute} SlipOption
:canonical: altdss.IndMach012.IndMach012BatchProperties.SlipOption
:type: typing.Union[typing.AnyStr, int, altdss.enums.IndMach012SlipOption, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.IndMach012SlipOption], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.SlipOption
```

````

````{py:attribute} Spectrum
:canonical: altdss.IndMach012.IndMach012BatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Spectrum
```

````

````{py:attribute} Yearly
:canonical: altdss.IndMach012.IndMach012BatchProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__contains__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__delattr__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__delitem__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__dir__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__format__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__ge__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__getattribute__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__getitem__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__getstate__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__gt__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__init__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__ior__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__iter__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__le__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__len__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__lt__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__ne__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__new__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__or__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__reduce__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__repr__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__reversed__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__ror__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__setitem__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__sizeof__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__str__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.IndMach012.IndMach012BatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.IndMach012.IndMach012BatchProperties.clear

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.IndMach012.IndMach012BatchProperties.copy

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.IndMach012.IndMach012BatchProperties.get

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.IndMach012.IndMach012BatchProperties.items

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.IndMach012.IndMach012BatchProperties.kV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.IndMach012.IndMach012BatchProperties.kVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.kVA
```

````

````{py:attribute} kW
:canonical: altdss.IndMach012.IndMach012BatchProperties.kW
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.kW
```

````

````{py:method} keys()
:canonical: altdss.IndMach012.IndMach012BatchProperties.keys

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.IndMach012.IndMach012BatchProperties.pop

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.IndMach012.IndMach012BatchProperties.popitem

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.popitem
```

````

````{py:attribute} puRr
:canonical: altdss.IndMach012.IndMach012BatchProperties.puRr
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.puRr
```

````

````{py:attribute} puRs
:canonical: altdss.IndMach012.IndMach012BatchProperties.puRs
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.puRs
```

````

````{py:attribute} puXm
:canonical: altdss.IndMach012.IndMach012BatchProperties.puXm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.puXm
```

````

````{py:attribute} puXr
:canonical: altdss.IndMach012.IndMach012BatchProperties.puXr
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.puXr
```

````

````{py:attribute} puXs
:canonical: altdss.IndMach012.IndMach012BatchProperties.puXs
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.puXs
```

````

````{py:method} setdefault()
:canonical: altdss.IndMach012.IndMach012BatchProperties.setdefault

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.IndMach012.IndMach012BatchProperties.update

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.IndMach012.IndMach012BatchProperties.values

```{autodoc2-docstring} altdss.IndMach012.IndMach012BatchProperties.values
```

````

`````

`````{py:class} IndMach012Properties()
:canonical: altdss.IndMach012.IndMach012Properties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties
```

````{py:attribute} BaseFreq
:canonical: altdss.IndMach012.IndMach012Properties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.IndMach012.IndMach012Properties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Bus1
```

````

````{py:attribute} Conn
:canonical: altdss.IndMach012.IndMach012Properties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Conn
```

````

````{py:attribute} D
:canonical: altdss.IndMach012.IndMach012Properties.D
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.D
```

````

````{py:attribute} Daily
:canonical: altdss.IndMach012.IndMach012Properties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Daily
```

````

````{py:attribute} DebugTrace
:canonical: altdss.IndMach012.IndMach012Properties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.DebugTrace
```

````

````{py:attribute} Duty
:canonical: altdss.IndMach012.IndMach012Properties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Duty
```

````

````{py:attribute} Enabled
:canonical: altdss.IndMach012.IndMach012Properties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Enabled
```

````

````{py:attribute} H
:canonical: altdss.IndMach012.IndMach012Properties.H
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.H
```

````

````{py:attribute} Like
:canonical: altdss.IndMach012.IndMach012Properties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Like
```

````

````{py:attribute} MaxSlip
:canonical: altdss.IndMach012.IndMach012Properties.MaxSlip
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.MaxSlip
```

````

````{py:attribute} PF
:canonical: altdss.IndMach012.IndMach012Properties.PF
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.PF
```

````

````{py:attribute} Phases
:canonical: altdss.IndMach012.IndMach012Properties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Phases
```

````

````{py:attribute} Slip
:canonical: altdss.IndMach012.IndMach012Properties.Slip
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Slip
```

````

````{py:attribute} SlipOption
:canonical: altdss.IndMach012.IndMach012Properties.SlipOption
:type: typing.Union[typing.AnyStr, int, altdss.enums.IndMach012SlipOption]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.SlipOption
```

````

````{py:attribute} Spectrum
:canonical: altdss.IndMach012.IndMach012Properties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Spectrum
```

````

````{py:attribute} Yearly
:canonical: altdss.IndMach012.IndMach012Properties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.IndMach012.IndMach012Properties.__contains__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.IndMach012.IndMach012Properties.__delattr__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.IndMach012.IndMach012Properties.__delitem__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.IndMach012.IndMach012Properties.__dir__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.IndMach012.IndMach012Properties.__format__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.IndMach012.IndMach012Properties.__ge__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.IndMach012.IndMach012Properties.__getattribute__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.IndMach012.IndMach012Properties.__getitem__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.IndMach012.IndMach012Properties.__getstate__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.IndMach012.IndMach012Properties.__gt__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.IndMach012.IndMach012Properties.__init__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.IndMach012.IndMach012Properties.__ior__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.IndMach012.IndMach012Properties.__iter__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.IndMach012.IndMach012Properties.__le__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.IndMach012.IndMach012Properties.__len__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.IndMach012.IndMach012Properties.__lt__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.IndMach012.IndMach012Properties.__ne__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.IndMach012.IndMach012Properties.__new__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.IndMach012.IndMach012Properties.__or__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.IndMach012.IndMach012Properties.__reduce__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.IndMach012.IndMach012Properties.__reduce_ex__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.IndMach012.IndMach012Properties.__repr__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.IndMach012.IndMach012Properties.__reversed__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.IndMach012.IndMach012Properties.__ror__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.IndMach012.IndMach012Properties.__setitem__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.IndMach012.IndMach012Properties.__sizeof__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.IndMach012.IndMach012Properties.__str__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.IndMach012.IndMach012Properties.__subclasshook__

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.IndMach012.IndMach012Properties.clear

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.clear
```

````

````{py:method} copy()
:canonical: altdss.IndMach012.IndMach012Properties.copy

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.copy
```

````

````{py:method} get()
:canonical: altdss.IndMach012.IndMach012Properties.get

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.get
```

````

````{py:method} items()
:canonical: altdss.IndMach012.IndMach012Properties.items

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.items
```

````

````{py:attribute} kV
:canonical: altdss.IndMach012.IndMach012Properties.kV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.IndMach012.IndMach012Properties.kVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.kVA
```

````

````{py:attribute} kW
:canonical: altdss.IndMach012.IndMach012Properties.kW
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.kW
```

````

````{py:method} keys()
:canonical: altdss.IndMach012.IndMach012Properties.keys

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.keys
```

````

````{py:method} pop()
:canonical: altdss.IndMach012.IndMach012Properties.pop

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.pop
```

````

````{py:method} popitem()
:canonical: altdss.IndMach012.IndMach012Properties.popitem

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.popitem
```

````

````{py:attribute} puRr
:canonical: altdss.IndMach012.IndMach012Properties.puRr
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.puRr
```

````

````{py:attribute} puRs
:canonical: altdss.IndMach012.IndMach012Properties.puRs
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.puRs
```

````

````{py:attribute} puXm
:canonical: altdss.IndMach012.IndMach012Properties.puXm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.puXm
```

````

````{py:attribute} puXr
:canonical: altdss.IndMach012.IndMach012Properties.puXr
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.puXr
```

````

````{py:attribute} puXs
:canonical: altdss.IndMach012.IndMach012Properties.puXs
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.puXs
```

````

````{py:method} setdefault()
:canonical: altdss.IndMach012.IndMach012Properties.setdefault

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.setdefault
```

````

````{py:method} update()
:canonical: altdss.IndMach012.IndMach012Properties.update

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.update
```

````

````{py:method} values()
:canonical: altdss.IndMach012.IndMach012Properties.values

```{autodoc2-docstring} altdss.IndMach012.IndMach012Properties.values
```

````

`````
