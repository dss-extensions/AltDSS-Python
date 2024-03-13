# {py:mod}`altdss.Vsource`

```{py:module} altdss.Vsource
```

```{autodoc2-docstring} altdss.Vsource
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IVsource <altdss.Vsource.IVsource>`
  - ```{autodoc2-docstring} altdss.Vsource.IVsource
    :summary:
    ```
* - {py:obj}`Vsource <altdss.Vsource.Vsource>`
  - ```{autodoc2-docstring} altdss.Vsource.Vsource
    :summary:
    ```
* - {py:obj}`VsourceBatch <altdss.Vsource.VsourceBatch>`
  - ```{autodoc2-docstring} altdss.Vsource.VsourceBatch
    :summary:
    ```
* - {py:obj}`VsourceBatchProperties <altdss.Vsource.VsourceBatchProperties>`
  - ```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties
    :summary:
    ```
* - {py:obj}`VsourceProperties <altdss.Vsource.VsourceProperties>`
  - ```{autodoc2-docstring} altdss.Vsource.VsourceProperties
    :summary:
    ```
````

### API

`````{py:class} IVsource(iobj)
:canonical: altdss.Vsource.IVsource

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Vsource.VsourceBatch`

```{autodoc2-docstring} altdss.Vsource.IVsource
```

````{py:attribute} Angle
:canonical: altdss.Vsource.IVsource.Angle
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Vsource.IVsource.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.BaseFreq
```

````

````{py:attribute} BaseMVA
:canonical: altdss.Vsource.IVsource.BaseMVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.BaseMVA
```

````

````{py:attribute} BasekV
:canonical: altdss.Vsource.IVsource.BasekV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.BasekV
```

````

````{py:attribute} Bus1
:canonical: altdss.Vsource.IVsource.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Vsource.IVsource.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Bus2
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.IVsource.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Vsource.IVsource.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.IVsource.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Vsource.IVsource.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.IVsource.Currents

```{autodoc2-docstring} altdss.Vsource.IVsource.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Vsource.IVsource.CurrentsMagAng

```{autodoc2-docstring} altdss.Vsource.IVsource.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.Vsource.IVsource.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Vsource.IVsource.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Daily_str
```

````

````{py:attribute} Duty
:canonical: altdss.Vsource.IVsource.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Vsource.IVsource.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Vsource.IVsource.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Vsource.IVsource.EnergyMeter

```{autodoc2-docstring} altdss.Vsource.IVsource.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Vsource.IVsource.EnergyMeterName

```{autodoc2-docstring} altdss.Vsource.IVsource.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.Vsource.IVsource.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Vsource.IVsource.FullName

```{autodoc2-docstring} altdss.Vsource.IVsource.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Vsource.IVsource.GUID

```{autodoc2-docstring} altdss.Vsource.IVsource.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Vsource.IVsource.Handle

```{autodoc2-docstring} altdss.Vsource.IVsource.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Vsource.IVsource.HasOCPDevice

```{autodoc2-docstring} altdss.Vsource.IVsource.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Vsource.IVsource.HasSwitchControl

```{autodoc2-docstring} altdss.Vsource.IVsource.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Vsource.IVsource.HasVoltControl

```{autodoc2-docstring} altdss.Vsource.IVsource.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Vsource.IVsource.IsIsolated

```{autodoc2-docstring} altdss.Vsource.IVsource.IsIsolated
```

````

````{py:attribute} Isc1
:canonical: altdss.Vsource.IVsource.Isc1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Isc1
```

````

````{py:attribute} Isc3
:canonical: altdss.Vsource.IVsource.Isc3
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Isc3
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Vsource.IVsource.Like

```{autodoc2-docstring} altdss.Vsource.IVsource.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.IVsource.Losses

```{autodoc2-docstring} altdss.Vsource.IVsource.Losses
```

````

````{py:attribute} MVASC1
:canonical: altdss.Vsource.IVsource.MVASC1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.MVASC1
```

````

````{py:attribute} MVASC3
:canonical: altdss.Vsource.IVsource.MVASC3
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.MVASC3
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Vsource.IVsource.MaxCurrent

```{autodoc2-docstring} altdss.Vsource.IVsource.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Vsource.IVsource.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Model
```

````

````{py:attribute} Model_str
:canonical: altdss.Vsource.IVsource.Model_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Model_str
```

````

````{py:property} Name
:canonical: altdss.Vsource.IVsource.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Vsource.IVsource.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Vsource.IVsource.NumConductors

```{autodoc2-docstring} altdss.Vsource.IVsource.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Vsource.IVsource.NumControllers

```{autodoc2-docstring} altdss.Vsource.IVsource.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Vsource.IVsource.NumPhases

```{autodoc2-docstring} altdss.Vsource.IVsource.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Vsource.IVsource.NumTerminals

```{autodoc2-docstring} altdss.Vsource.IVsource.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Vsource.IVsource.OCPDevice

```{autodoc2-docstring} altdss.Vsource.IVsource.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Vsource.IVsource.OCPDeviceIndex

```{autodoc2-docstring} altdss.Vsource.IVsource.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Vsource.IVsource.OCPDeviceType

```{autodoc2-docstring} altdss.Vsource.IVsource.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.IVsource.PhaseLosses

```{autodoc2-docstring} altdss.Vsource.IVsource.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Vsource.IVsource.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.IVsource.Powers

```{autodoc2-docstring} altdss.Vsource.IVsource.Powers
```

````

````{py:attribute} R0
:canonical: altdss.Vsource.IVsource.R0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.R0
```

````

````{py:attribute} R1
:canonical: altdss.Vsource.IVsource.R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.R1
```

````

````{py:attribute} ScanType
:canonical: altdss.Vsource.IVsource.ScanType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.ScanType
```

````

````{py:attribute} ScanType_str
:canonical: altdss.Vsource.IVsource.ScanType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.ScanType_str
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Vsource.IVsource.SeqCurrents

```{autodoc2-docstring} altdss.Vsource.IVsource.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.IVsource.SeqPowers

```{autodoc2-docstring} altdss.Vsource.IVsource.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Vsource.IVsource.SeqVoltages

```{autodoc2-docstring} altdss.Vsource.IVsource.SeqVoltages
```

````

````{py:attribute} Sequence
:canonical: altdss.Vsource.IVsource.Sequence
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Sequence
```

````

````{py:attribute} Sequence_str
:canonical: altdss.Vsource.IVsource.Sequence_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Sequence_str
```

````

````{py:attribute} Spectrum
:canonical: altdss.Vsource.IVsource.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Vsource.IVsource.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.IVsource.TotalPowers

```{autodoc2-docstring} altdss.Vsource.IVsource.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.IVsource.Voltages

```{autodoc2-docstring} altdss.Vsource.IVsource.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Vsource.IVsource.VoltagesMagAng

```{autodoc2-docstring} altdss.Vsource.IVsource.VoltagesMagAng
```

````

````{py:attribute} X0
:canonical: altdss.Vsource.IVsource.X0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.X0
```

````

````{py:attribute} X0R0
:canonical: altdss.Vsource.IVsource.X0R0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.X0R0
```

````

````{py:attribute} X1
:canonical: altdss.Vsource.IVsource.X1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.X1
```

````

````{py:attribute} X1R1
:canonical: altdss.Vsource.IVsource.X1R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.X1R1
```

````

````{py:attribute} Yearly
:canonical: altdss.Vsource.IVsource.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Vsource.IVsource.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Yearly_str
```

````

````{py:attribute} Z2
:canonical: altdss.Vsource.IVsource.Z2
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.Z2
```

````

````{py:method} __call__()
:canonical: altdss.Vsource.IVsource.__call__

```{autodoc2-docstring} altdss.Vsource.IVsource.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Vsource.IVsource.__contains__

```{autodoc2-docstring} altdss.Vsource.IVsource.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Vsource.IVsource.__getitem__

```{autodoc2-docstring} altdss.Vsource.IVsource.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Vsource.IVsource.__init__

```{autodoc2-docstring} altdss.Vsource.IVsource.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Vsource.IVsource.__iter__

```{autodoc2-docstring} altdss.Vsource.IVsource.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Vsource.IVsource.__len__

```{autodoc2-docstring} altdss.Vsource.IVsource.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Vsource.IVsource.batch

```{autodoc2-docstring} altdss.Vsource.IVsource.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Vsource.VsourceBatchProperties]) -> altdss.Vsource.VsourceBatch
:canonical: altdss.Vsource.IVsource.batch_new

```{autodoc2-docstring} altdss.Vsource.IVsource.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Vsource.IVsource.begin_edit

```{autodoc2-docstring} altdss.Vsource.IVsource.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Vsource.IVsource.end_edit

```{autodoc2-docstring} altdss.Vsource.IVsource.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Vsource.IVsource.find

```{autodoc2-docstring} altdss.Vsource.IVsource.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Vsource.VsourceProperties]) -> altdss.Vsource.Vsource
:canonical: altdss.Vsource.IVsource.new

```{autodoc2-docstring} altdss.Vsource.IVsource.new
```

````

````{py:attribute} pu
:canonical: altdss.Vsource.IVsource.pu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.pu
```

````

````{py:attribute} puZ0
:canonical: altdss.Vsource.IVsource.puZ0
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.puZ0
```

````

````{py:attribute} puZ1
:canonical: altdss.Vsource.IVsource.puZ1
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.puZ1
```

````

````{py:attribute} puZ2
:canonical: altdss.Vsource.IVsource.puZ2
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.puZ2
```

````

````{py:attribute} puZIdeal
:canonical: altdss.Vsource.IVsource.puZIdeal
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.IVsource.puZIdeal
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Vsource.IVsource.to_json

```{autodoc2-docstring} altdss.Vsource.IVsource.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Vsource.IVsource.to_list

```{autodoc2-docstring} altdss.Vsource.IVsource.to_list
```

````

`````

`````{py:class} Vsource(api_util, ptr)
:canonical: altdss.Vsource.Vsource

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`

```{autodoc2-docstring} altdss.Vsource.Vsource
```

````{py:attribute} Angle
:canonical: altdss.Vsource.Vsource.Angle
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Vsource.Vsource.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.BaseFreq
```

````

````{py:attribute} BaseMVA
:canonical: altdss.Vsource.Vsource.BaseMVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.BaseMVA
```

````

````{py:attribute} BasekV
:canonical: altdss.Vsource.Vsource.BasekV
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.BasekV
```

````

````{py:attribute} Bus1
:canonical: altdss.Vsource.Vsource.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Vsource.Vsource.Bus2
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Bus2
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Vsource.Vsource.Close

```{autodoc2-docstring} altdss.Vsource.Vsource.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.Vsource.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Vsource.Vsource.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.Vsource.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Vsource.Vsource.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.Vsource.Currents

```{autodoc2-docstring} altdss.Vsource.Vsource.Currents
```

````

````{py:attribute} Daily
:canonical: altdss.Vsource.Vsource.Daily
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Vsource.Vsource.Daily_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Daily_str
```

````

````{py:attribute} DisplayName
:canonical: altdss.Vsource.Vsource.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.DisplayName
```

````

````{py:attribute} Duty
:canonical: altdss.Vsource.Vsource.Duty
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Vsource.Vsource.Duty_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Vsource.Vsource.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.Vsource.Vsource.EnergyMeter

```{autodoc2-docstring} altdss.Vsource.Vsource.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Vsource.Vsource.EnergyMeterName

```{autodoc2-docstring} altdss.Vsource.Vsource.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.Vsource.Vsource.Frequency
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Frequency
```

````

````{py:method} FullName() -> str
:canonical: altdss.Vsource.Vsource.FullName

```{autodoc2-docstring} altdss.Vsource.Vsource.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Vsource.Vsource.GUID

```{autodoc2-docstring} altdss.Vsource.Vsource.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.Vsource.Vsource.GetVariableValue

```{autodoc2-docstring} altdss.Vsource.Vsource.GetVariableValue
```

````

````{py:method} Handle() -> int
:canonical: altdss.Vsource.Vsource.Handle

```{autodoc2-docstring} altdss.Vsource.Vsource.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Vsource.Vsource.HasOCPDevice

```{autodoc2-docstring} altdss.Vsource.Vsource.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Vsource.Vsource.HasSwitchControl

```{autodoc2-docstring} altdss.Vsource.Vsource.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Vsource.Vsource.HasVoltControl

```{autodoc2-docstring} altdss.Vsource.Vsource.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Vsource.Vsource.IsIsolated

```{autodoc2-docstring} altdss.Vsource.Vsource.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Vsource.Vsource.IsOpen

```{autodoc2-docstring} altdss.Vsource.Vsource.IsOpen
```

````

````{py:attribute} Isc1
:canonical: altdss.Vsource.Vsource.Isc1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Isc1
```

````

````{py:attribute} Isc3
:canonical: altdss.Vsource.Vsource.Isc3
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Isc3
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Vsource.Vsource.Like

```{autodoc2-docstring} altdss.Vsource.Vsource.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Vsource.Vsource.Losses

```{autodoc2-docstring} altdss.Vsource.Vsource.Losses
```

````

````{py:attribute} MVASC1
:canonical: altdss.Vsource.Vsource.MVASC1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.MVASC1
```

````

````{py:attribute} MVASC3
:canonical: altdss.Vsource.Vsource.MVASC3
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.MVASC3
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Vsource.Vsource.MaxCurrent

```{autodoc2-docstring} altdss.Vsource.Vsource.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Vsource.Vsource.Model
:type: altdss.enums.VSourceModel
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Model
```

````

````{py:attribute} Model_str
:canonical: altdss.Vsource.Vsource.Model_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Model_str
```

````

````{py:property} Name
:canonical: altdss.Vsource.Vsource.Name
:type: str

```{autodoc2-docstring} altdss.Vsource.Vsource.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Vsource.Vsource.NodeOrder

```{autodoc2-docstring} altdss.Vsource.Vsource.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Vsource.Vsource.NodeRef

```{autodoc2-docstring} altdss.Vsource.Vsource.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Vsource.Vsource.NumConductors

```{autodoc2-docstring} altdss.Vsource.Vsource.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Vsource.Vsource.NumControllers

```{autodoc2-docstring} altdss.Vsource.Vsource.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Vsource.Vsource.NumPhases

```{autodoc2-docstring} altdss.Vsource.Vsource.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Vsource.Vsource.NumTerminals

```{autodoc2-docstring} altdss.Vsource.Vsource.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Vsource.Vsource.OCPDevice

```{autodoc2-docstring} altdss.Vsource.Vsource.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Vsource.Vsource.OCPDeviceIndex

```{autodoc2-docstring} altdss.Vsource.Vsource.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Vsource.Vsource.OCPDeviceType

```{autodoc2-docstring} altdss.Vsource.Vsource.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Vsource.Vsource.Open

```{autodoc2-docstring} altdss.Vsource.Vsource.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.Vsource.PhaseLosses

```{autodoc2-docstring} altdss.Vsource.Vsource.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Vsource.Vsource.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.Vsource.Powers

```{autodoc2-docstring} altdss.Vsource.Vsource.Powers
```

````

````{py:attribute} R0
:canonical: altdss.Vsource.Vsource.R0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.R0
```

````

````{py:attribute} R1
:canonical: altdss.Vsource.Vsource.R1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.R1
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Vsource.Vsource.Residuals

```{autodoc2-docstring} altdss.Vsource.Vsource.Residuals
```

````

````{py:attribute} ScanType
:canonical: altdss.Vsource.Vsource.ScanType
:type: altdss.enums.ScanType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.ScanType
```

````

````{py:attribute} ScanType_str
:canonical: altdss.Vsource.Vsource.ScanType_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.ScanType_str
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Vsource.Vsource.SeqCurrents

```{autodoc2-docstring} altdss.Vsource.Vsource.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.Vsource.SeqPowers

```{autodoc2-docstring} altdss.Vsource.Vsource.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Vsource.Vsource.SeqVoltages

```{autodoc2-docstring} altdss.Vsource.Vsource.SeqVoltages
```

````

````{py:attribute} Sequence
:canonical: altdss.Vsource.Vsource.Sequence
:type: altdss.enums.SequenceType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Sequence
```

````

````{py:attribute} Sequence_str
:canonical: altdss.Vsource.Vsource.Sequence_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Sequence_str
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.Vsource.Vsource.SetVariableValue

```{autodoc2-docstring} altdss.Vsource.Vsource.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.Vsource.Vsource.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Vsource.Vsource.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.Vsource.TotalPowers

```{autodoc2-docstring} altdss.Vsource.Vsource.TotalPowers
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.Vsource.Vsource.VariableNames

```{autodoc2-docstring} altdss.Vsource.Vsource.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.Vsource.Vsource.VariableValues

```{autodoc2-docstring} altdss.Vsource.Vsource.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.Vsource.Vsource.VariablesDict

```{autodoc2-docstring} altdss.Vsource.Vsource.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.Vsource.Voltages

```{autodoc2-docstring} altdss.Vsource.Vsource.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Vsource.Vsource.VoltagesMagAng

```{autodoc2-docstring} altdss.Vsource.Vsource.VoltagesMagAng
```

````

````{py:attribute} X0
:canonical: altdss.Vsource.Vsource.X0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.X0
```

````

````{py:attribute} X0R0
:canonical: altdss.Vsource.Vsource.X0R0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.X0R0
```

````

````{py:attribute} X1
:canonical: altdss.Vsource.Vsource.X1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.X1
```

````

````{py:attribute} X1R1
:canonical: altdss.Vsource.Vsource.X1R1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.X1R1
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.Vsource.YPrim

```{autodoc2-docstring} altdss.Vsource.Vsource.YPrim
```

````

````{py:attribute} Yearly
:canonical: altdss.Vsource.Vsource.Yearly
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Vsource.Vsource.Yearly_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Yearly_str
```

````

````{py:attribute} Z2
:canonical: altdss.Vsource.Vsource.Z2
:type: complex
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.Z2
```

````

````{py:method} __hash__()
:canonical: altdss.Vsource.Vsource.__hash__

```{autodoc2-docstring} altdss.Vsource.Vsource.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Vsource.Vsource.__init__

```{autodoc2-docstring} altdss.Vsource.Vsource.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Vsource.Vsource.__ne__

```{autodoc2-docstring} altdss.Vsource.Vsource.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Vsource.Vsource.__repr__

```{autodoc2-docstring} altdss.Vsource.Vsource.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Vsource.Vsource.begin_edit

```{autodoc2-docstring} altdss.Vsource.Vsource.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Vsource.Vsource.end_edit

```{autodoc2-docstring} altdss.Vsource.Vsource.end_edit
```

````

````{py:attribute} pu
:canonical: altdss.Vsource.Vsource.pu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.pu
```

````

````{py:attribute} puZ0
:canonical: altdss.Vsource.Vsource.puZ0
:type: complex
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.puZ0
```

````

````{py:attribute} puZ1
:canonical: altdss.Vsource.Vsource.puZ1
:type: complex
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.puZ1
```

````

````{py:attribute} puZ2
:canonical: altdss.Vsource.Vsource.puZ2
:type: complex
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.puZ2
```

````

````{py:attribute} puZIdeal
:canonical: altdss.Vsource.Vsource.puZIdeal
:type: complex
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.Vsource.puZIdeal
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Vsource.Vsource.to_json

```{autodoc2-docstring} altdss.Vsource.Vsource.to_json
```

````

`````

`````{py:class} VsourceBatch(api_util, **kwargs)
:canonical: altdss.Vsource.VsourceBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.Vsource.VsourceBatch
```

````{py:attribute} Angle
:canonical: altdss.Vsource.VsourceBatch.Angle
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Vsource.VsourceBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.BaseFreq
```

````

````{py:attribute} BaseMVA
:canonical: altdss.Vsource.VsourceBatch.BaseMVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.BaseMVA
```

````

````{py:attribute} BasekV
:canonical: altdss.Vsource.VsourceBatch.BasekV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.BasekV
```

````

````{py:attribute} Bus1
:canonical: altdss.Vsource.VsourceBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Vsource.VsourceBatch.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Bus2
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.VsourceBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.VsourceBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.VsourceBatch.Currents

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Vsource.VsourceBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.Vsource.VsourceBatch.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Vsource.VsourceBatch.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Daily_str
```

````

````{py:attribute} Duty
:canonical: altdss.Vsource.VsourceBatch.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Vsource.VsourceBatch.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Vsource.VsourceBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Vsource.VsourceBatch.EnergyMeter

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Vsource.VsourceBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.Vsource.VsourceBatch.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Vsource.VsourceBatch.FullName

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Vsource.VsourceBatch.GUID

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Vsource.VsourceBatch.Handle

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Vsource.VsourceBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Vsource.VsourceBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Vsource.VsourceBatch.HasVoltControl

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Vsource.VsourceBatch.IsIsolated

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.IsIsolated
```

````

````{py:attribute} Isc1
:canonical: altdss.Vsource.VsourceBatch.Isc1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Isc1
```

````

````{py:attribute} Isc3
:canonical: altdss.Vsource.VsourceBatch.Isc3
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Isc3
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Vsource.VsourceBatch.Like

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.VsourceBatch.Losses

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Losses
```

````

````{py:attribute} MVASC1
:canonical: altdss.Vsource.VsourceBatch.MVASC1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.MVASC1
```

````

````{py:attribute} MVASC3
:canonical: altdss.Vsource.VsourceBatch.MVASC3
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.MVASC3
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Vsource.VsourceBatch.MaxCurrent

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Vsource.VsourceBatch.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Model
```

````

````{py:attribute} Model_str
:canonical: altdss.Vsource.VsourceBatch.Model_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Model_str
```

````

````{py:property} Name
:canonical: altdss.Vsource.VsourceBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Vsource.VsourceBatch.NumConductors

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Vsource.VsourceBatch.NumControllers

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Vsource.VsourceBatch.NumPhases

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Vsource.VsourceBatch.NumTerminals

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Vsource.VsourceBatch.OCPDevice

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Vsource.VsourceBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Vsource.VsourceBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.VsourceBatch.PhaseLosses

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Vsource.VsourceBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.VsourceBatch.Powers

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Powers
```

````

````{py:attribute} R0
:canonical: altdss.Vsource.VsourceBatch.R0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.R0
```

````

````{py:attribute} R1
:canonical: altdss.Vsource.VsourceBatch.R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.R1
```

````

````{py:attribute} ScanType
:canonical: altdss.Vsource.VsourceBatch.ScanType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.ScanType
```

````

````{py:attribute} ScanType_str
:canonical: altdss.Vsource.VsourceBatch.ScanType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.ScanType_str
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Vsource.VsourceBatch.SeqCurrents

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.VsourceBatch.SeqPowers

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Vsource.VsourceBatch.SeqVoltages

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.SeqVoltages
```

````

````{py:attribute} Sequence
:canonical: altdss.Vsource.VsourceBatch.Sequence
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Sequence
```

````

````{py:attribute} Sequence_str
:canonical: altdss.Vsource.VsourceBatch.Sequence_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Sequence_str
```

````

````{py:attribute} Spectrum
:canonical: altdss.Vsource.VsourceBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Vsource.VsourceBatch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.VsourceBatch.TotalPowers

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Vsource.VsourceBatch.Voltages

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Vsource.VsourceBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.VoltagesMagAng
```

````

````{py:attribute} X0
:canonical: altdss.Vsource.VsourceBatch.X0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.X0
```

````

````{py:attribute} X0R0
:canonical: altdss.Vsource.VsourceBatch.X0R0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.X0R0
```

````

````{py:attribute} X1
:canonical: altdss.Vsource.VsourceBatch.X1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.X1
```

````

````{py:attribute} X1R1
:canonical: altdss.Vsource.VsourceBatch.X1R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.X1R1
```

````

````{py:attribute} Yearly
:canonical: altdss.Vsource.VsourceBatch.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Vsource.VsourceBatch.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Yearly_str
```

````

````{py:attribute} Z2
:canonical: altdss.Vsource.VsourceBatch.Z2
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.Z2
```

````

````{py:method} __call__()
:canonical: altdss.Vsource.VsourceBatch.__call__

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Vsource.VsourceBatch.__getitem__

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Vsource.VsourceBatch.__init__

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Vsource.VsourceBatch.__iter__

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Vsource.VsourceBatch.__len__

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Vsource.VsourceBatch.batch

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Vsource.VsourceBatch.begin_edit

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Vsource.VsourceBatch.end_edit

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.end_edit
```

````

````{py:attribute} pu
:canonical: altdss.Vsource.VsourceBatch.pu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.pu
```

````

````{py:attribute} puZ0
:canonical: altdss.Vsource.VsourceBatch.puZ0
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.puZ0
```

````

````{py:attribute} puZ1
:canonical: altdss.Vsource.VsourceBatch.puZ1
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.puZ1
```

````

````{py:attribute} puZ2
:canonical: altdss.Vsource.VsourceBatch.puZ2
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.puZ2
```

````

````{py:attribute} puZIdeal
:canonical: altdss.Vsource.VsourceBatch.puZIdeal
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.puZIdeal
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Vsource.VsourceBatch.to_json

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Vsource.VsourceBatch.to_list

```{autodoc2-docstring} altdss.Vsource.VsourceBatch.to_list
```

````

`````

`````{py:class} VsourceBatchProperties()
:canonical: altdss.Vsource.VsourceBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties
```

````{py:attribute} Angle
:canonical: altdss.Vsource.VsourceBatchProperties.Angle
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Vsource.VsourceBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.BaseFreq
```

````

````{py:attribute} BaseMVA
:canonical: altdss.Vsource.VsourceBatchProperties.BaseMVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.BaseMVA
```

````

````{py:attribute} BasekV
:canonical: altdss.Vsource.VsourceBatchProperties.BasekV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.BasekV
```

````

````{py:attribute} Bus1
:canonical: altdss.Vsource.VsourceBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Vsource.VsourceBatchProperties.Bus2
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Bus2
```

````

````{py:attribute} Daily
:canonical: altdss.Vsource.VsourceBatchProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Daily
```

````

````{py:attribute} Duty
:canonical: altdss.Vsource.VsourceBatchProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Duty
```

````

````{py:attribute} Enabled
:canonical: altdss.Vsource.VsourceBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.Vsource.VsourceBatchProperties.Frequency
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Frequency
```

````

````{py:attribute} Isc1
:canonical: altdss.Vsource.VsourceBatchProperties.Isc1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Isc1
```

````

````{py:attribute} Isc3
:canonical: altdss.Vsource.VsourceBatchProperties.Isc3
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Isc3
```

````

````{py:attribute} Like
:canonical: altdss.Vsource.VsourceBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Like
```

````

````{py:attribute} MVASC1
:canonical: altdss.Vsource.VsourceBatchProperties.MVASC1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.MVASC1
```

````

````{py:attribute} MVASC3
:canonical: altdss.Vsource.VsourceBatchProperties.MVASC3
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.MVASC3
```

````

````{py:attribute} Model
:canonical: altdss.Vsource.VsourceBatchProperties.Model
:type: typing.Union[typing.AnyStr, int, altdss.enums.VSourceModel, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.VSourceModel], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Model
```

````

````{py:attribute} Phases
:canonical: altdss.Vsource.VsourceBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Phases
```

````

````{py:attribute} R0
:canonical: altdss.Vsource.VsourceBatchProperties.R0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.R0
```

````

````{py:attribute} R1
:canonical: altdss.Vsource.VsourceBatchProperties.R1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.R1
```

````

````{py:attribute} ScanType
:canonical: altdss.Vsource.VsourceBatchProperties.ScanType
:type: typing.Union[typing.AnyStr, int, altdss.enums.ScanType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.ScanType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.ScanType
```

````

````{py:attribute} Sequence
:canonical: altdss.Vsource.VsourceBatchProperties.Sequence
:type: typing.Union[typing.AnyStr, int, altdss.enums.SequenceType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.SequenceType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Sequence
```

````

````{py:attribute} Spectrum
:canonical: altdss.Vsource.VsourceBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Spectrum
```

````

````{py:attribute} X0
:canonical: altdss.Vsource.VsourceBatchProperties.X0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.X0
```

````

````{py:attribute} X0R0
:canonical: altdss.Vsource.VsourceBatchProperties.X0R0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.X0R0
```

````

````{py:attribute} X1
:canonical: altdss.Vsource.VsourceBatchProperties.X1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.X1
```

````

````{py:attribute} X1R1
:canonical: altdss.Vsource.VsourceBatchProperties.X1R1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.X1R1
```

````

````{py:attribute} Yearly
:canonical: altdss.Vsource.VsourceBatchProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Yearly
```

````

````{py:attribute} Z2
:canonical: altdss.Vsource.VsourceBatchProperties.Z2
:type: typing.Union[complex, typing.List[complex]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.Z2
```

````

````{py:method} __contains__()
:canonical: altdss.Vsource.VsourceBatchProperties.__contains__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Vsource.VsourceBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Vsource.VsourceBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Vsource.VsourceBatchProperties.__dir__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Vsource.VsourceBatchProperties.__format__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Vsource.VsourceBatchProperties.__ge__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Vsource.VsourceBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Vsource.VsourceBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Vsource.VsourceBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Vsource.VsourceBatchProperties.__gt__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Vsource.VsourceBatchProperties.__init__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Vsource.VsourceBatchProperties.__ior__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Vsource.VsourceBatchProperties.__iter__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Vsource.VsourceBatchProperties.__le__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Vsource.VsourceBatchProperties.__len__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Vsource.VsourceBatchProperties.__lt__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Vsource.VsourceBatchProperties.__ne__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Vsource.VsourceBatchProperties.__new__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Vsource.VsourceBatchProperties.__or__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Vsource.VsourceBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Vsource.VsourceBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Vsource.VsourceBatchProperties.__repr__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Vsource.VsourceBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Vsource.VsourceBatchProperties.__ror__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Vsource.VsourceBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Vsource.VsourceBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Vsource.VsourceBatchProperties.__str__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Vsource.VsourceBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Vsource.VsourceBatchProperties.clear

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Vsource.VsourceBatchProperties.copy

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Vsource.VsourceBatchProperties.get

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Vsource.VsourceBatchProperties.items

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Vsource.VsourceBatchProperties.keys

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Vsource.VsourceBatchProperties.pop

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Vsource.VsourceBatchProperties.popitem

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.popitem
```

````

````{py:attribute} pu
:canonical: altdss.Vsource.VsourceBatchProperties.pu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.pu
```

````

````{py:attribute} puZ0
:canonical: altdss.Vsource.VsourceBatchProperties.puZ0
:type: typing.Union[complex, typing.List[complex]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.puZ0
```

````

````{py:attribute} puZ1
:canonical: altdss.Vsource.VsourceBatchProperties.puZ1
:type: typing.Union[complex, typing.List[complex]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.puZ1
```

````

````{py:attribute} puZ2
:canonical: altdss.Vsource.VsourceBatchProperties.puZ2
:type: typing.Union[complex, typing.List[complex]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.puZ2
```

````

````{py:attribute} puZIdeal
:canonical: altdss.Vsource.VsourceBatchProperties.puZIdeal
:type: typing.Union[complex, typing.List[complex]]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.puZIdeal
```

````

````{py:method} setdefault()
:canonical: altdss.Vsource.VsourceBatchProperties.setdefault

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Vsource.VsourceBatchProperties.update

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Vsource.VsourceBatchProperties.values

```{autodoc2-docstring} altdss.Vsource.VsourceBatchProperties.values
```

````

`````

`````{py:class} VsourceProperties()
:canonical: altdss.Vsource.VsourceProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Vsource.VsourceProperties
```

````{py:attribute} Angle
:canonical: altdss.Vsource.VsourceProperties.Angle
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Angle
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Vsource.VsourceProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.BaseFreq
```

````

````{py:attribute} BaseMVA
:canonical: altdss.Vsource.VsourceProperties.BaseMVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.BaseMVA
```

````

````{py:attribute} BasekV
:canonical: altdss.Vsource.VsourceProperties.BasekV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.BasekV
```

````

````{py:attribute} Bus1
:canonical: altdss.Vsource.VsourceProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Vsource.VsourceProperties.Bus2
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Bus2
```

````

````{py:attribute} Daily
:canonical: altdss.Vsource.VsourceProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Daily
```

````

````{py:attribute} Duty
:canonical: altdss.Vsource.VsourceProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Duty
```

````

````{py:attribute} Enabled
:canonical: altdss.Vsource.VsourceProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.Vsource.VsourceProperties.Frequency
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Frequency
```

````

````{py:attribute} Isc1
:canonical: altdss.Vsource.VsourceProperties.Isc1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Isc1
```

````

````{py:attribute} Isc3
:canonical: altdss.Vsource.VsourceProperties.Isc3
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Isc3
```

````

````{py:attribute} Like
:canonical: altdss.Vsource.VsourceProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Like
```

````

````{py:attribute} MVASC1
:canonical: altdss.Vsource.VsourceProperties.MVASC1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.MVASC1
```

````

````{py:attribute} MVASC3
:canonical: altdss.Vsource.VsourceProperties.MVASC3
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.MVASC3
```

````

````{py:attribute} Model
:canonical: altdss.Vsource.VsourceProperties.Model
:type: typing.Union[typing.AnyStr, int, altdss.enums.VSourceModel]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Model
```

````

````{py:attribute} Phases
:canonical: altdss.Vsource.VsourceProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Phases
```

````

````{py:attribute} R0
:canonical: altdss.Vsource.VsourceProperties.R0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.R0
```

````

````{py:attribute} R1
:canonical: altdss.Vsource.VsourceProperties.R1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.R1
```

````

````{py:attribute} ScanType
:canonical: altdss.Vsource.VsourceProperties.ScanType
:type: typing.Union[typing.AnyStr, int, altdss.enums.ScanType]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.ScanType
```

````

````{py:attribute} Sequence
:canonical: altdss.Vsource.VsourceProperties.Sequence
:type: typing.Union[typing.AnyStr, int, altdss.enums.SequenceType]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Sequence
```

````

````{py:attribute} Spectrum
:canonical: altdss.Vsource.VsourceProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Spectrum
```

````

````{py:attribute} X0
:canonical: altdss.Vsource.VsourceProperties.X0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.X0
```

````

````{py:attribute} X0R0
:canonical: altdss.Vsource.VsourceProperties.X0R0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.X0R0
```

````

````{py:attribute} X1
:canonical: altdss.Vsource.VsourceProperties.X1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.X1
```

````

````{py:attribute} X1R1
:canonical: altdss.Vsource.VsourceProperties.X1R1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.X1R1
```

````

````{py:attribute} Yearly
:canonical: altdss.Vsource.VsourceProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Yearly
```

````

````{py:attribute} Z2
:canonical: altdss.Vsource.VsourceProperties.Z2
:type: complex
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.Z2
```

````

````{py:method} __contains__()
:canonical: altdss.Vsource.VsourceProperties.__contains__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Vsource.VsourceProperties.__delattr__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Vsource.VsourceProperties.__delitem__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Vsource.VsourceProperties.__dir__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Vsource.VsourceProperties.__format__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Vsource.VsourceProperties.__ge__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Vsource.VsourceProperties.__getattribute__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Vsource.VsourceProperties.__getitem__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Vsource.VsourceProperties.__getstate__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Vsource.VsourceProperties.__gt__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Vsource.VsourceProperties.__init__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Vsource.VsourceProperties.__ior__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Vsource.VsourceProperties.__iter__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Vsource.VsourceProperties.__le__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Vsource.VsourceProperties.__len__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Vsource.VsourceProperties.__lt__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Vsource.VsourceProperties.__ne__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Vsource.VsourceProperties.__new__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Vsource.VsourceProperties.__or__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Vsource.VsourceProperties.__reduce__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Vsource.VsourceProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Vsource.VsourceProperties.__repr__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Vsource.VsourceProperties.__reversed__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Vsource.VsourceProperties.__ror__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Vsource.VsourceProperties.__setitem__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Vsource.VsourceProperties.__sizeof__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Vsource.VsourceProperties.__str__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Vsource.VsourceProperties.__subclasshook__

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Vsource.VsourceProperties.clear

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Vsource.VsourceProperties.copy

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Vsource.VsourceProperties.get

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.get
```

````

````{py:method} items()
:canonical: altdss.Vsource.VsourceProperties.items

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Vsource.VsourceProperties.keys

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Vsource.VsourceProperties.pop

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Vsource.VsourceProperties.popitem

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.popitem
```

````

````{py:attribute} pu
:canonical: altdss.Vsource.VsourceProperties.pu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.pu
```

````

````{py:attribute} puZ0
:canonical: altdss.Vsource.VsourceProperties.puZ0
:type: complex
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.puZ0
```

````

````{py:attribute} puZ1
:canonical: altdss.Vsource.VsourceProperties.puZ1
:type: complex
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.puZ1
```

````

````{py:attribute} puZ2
:canonical: altdss.Vsource.VsourceProperties.puZ2
:type: complex
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.puZ2
```

````

````{py:attribute} puZIdeal
:canonical: altdss.Vsource.VsourceProperties.puZIdeal
:type: complex
:value: >
   None

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.puZIdeal
```

````

````{py:method} setdefault()
:canonical: altdss.Vsource.VsourceProperties.setdefault

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Vsource.VsourceProperties.update

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.update
```

````

````{py:method} values()
:canonical: altdss.Vsource.VsourceProperties.values

```{autodoc2-docstring} altdss.Vsource.VsourceProperties.values
```

````

`````
