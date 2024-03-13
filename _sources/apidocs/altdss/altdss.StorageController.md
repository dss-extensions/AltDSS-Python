# {py:mod}`altdss.StorageController`

```{py:module} altdss.StorageController
```

```{autodoc2-docstring} altdss.StorageController
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IStorageController <altdss.StorageController.IStorageController>`
  - ```{autodoc2-docstring} altdss.StorageController.IStorageController
    :summary:
    ```
* - {py:obj}`StorageController <altdss.StorageController.StorageController>`
  - ```{autodoc2-docstring} altdss.StorageController.StorageController
    :summary:
    ```
* - {py:obj}`StorageControllerBatch <altdss.StorageController.StorageControllerBatch>`
  - ```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch
    :summary:
    ```
* - {py:obj}`StorageControllerBatchProperties <altdss.StorageController.StorageControllerBatchProperties>`
  - ```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties
    :summary:
    ```
* - {py:obj}`StorageControllerProperties <altdss.StorageController.StorageControllerProperties>`
  - ```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties
    :summary:
    ```
````

### API

`````{py:class} IStorageController(iobj)
:canonical: altdss.StorageController.IStorageController

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.StorageController.StorageControllerBatch`

```{autodoc2-docstring} altdss.StorageController.IStorageController
```

````{py:attribute} BaseFreq
:canonical: altdss.StorageController.IStorageController.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.IStorageController.ComplexSeqCurrents

```{autodoc2-docstring} altdss.StorageController.IStorageController.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.IStorageController.ComplexSeqVoltages

```{autodoc2-docstring} altdss.StorageController.IStorageController.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.IStorageController.Currents

```{autodoc2-docstring} altdss.StorageController.IStorageController.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.StorageController.IStorageController.CurrentsMagAng

```{autodoc2-docstring} altdss.StorageController.IStorageController.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.StorageController.IStorageController.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.StorageController.IStorageController.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Daily_str
```

````

````{py:attribute} DispFactor
:canonical: altdss.StorageController.IStorageController.DispFactor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.DispFactor
```

````

````{py:attribute} Duty
:canonical: altdss.StorageController.IStorageController.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.StorageController.IStorageController.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Duty_str
```

````

````{py:attribute} Element
:canonical: altdss.StorageController.IStorageController.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Element
```

````

````{py:attribute} ElementList
:canonical: altdss.StorageController.IStorageController.ElementList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.ElementList
```

````

````{py:attribute} Element_str
:canonical: altdss.StorageController.IStorageController.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.StorageController.IStorageController.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.StorageController.IStorageController.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.StorageController.IStorageController.FullName

```{autodoc2-docstring} altdss.StorageController.IStorageController.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.StorageController.IStorageController.GUID

```{autodoc2-docstring} altdss.StorageController.IStorageController.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.StorageController.IStorageController.Handle

```{autodoc2-docstring} altdss.StorageController.IStorageController.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.StorageController.IStorageController.HasOCPDevice

```{autodoc2-docstring} altdss.StorageController.IStorageController.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.StorageController.IStorageController.HasSwitchControl

```{autodoc2-docstring} altdss.StorageController.IStorageController.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.StorageController.IStorageController.HasVoltControl

```{autodoc2-docstring} altdss.StorageController.IStorageController.HasVoltControl
```

````

````{py:attribute} InhibitTime
:canonical: altdss.StorageController.IStorageController.InhibitTime
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.InhibitTime
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.StorageController.IStorageController.IsIsolated

```{autodoc2-docstring} altdss.StorageController.IStorageController.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.StorageController.IStorageController.Like

```{autodoc2-docstring} altdss.StorageController.IStorageController.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.IStorageController.Losses

```{autodoc2-docstring} altdss.StorageController.IStorageController.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.StorageController.IStorageController.MaxCurrent

```{autodoc2-docstring} altdss.StorageController.IStorageController.MaxCurrent
```

````

````{py:attribute} ModeCharge
:canonical: altdss.StorageController.IStorageController.ModeCharge
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.ModeCharge
```

````

````{py:attribute} ModeCharge_str
:canonical: altdss.StorageController.IStorageController.ModeCharge_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.ModeCharge_str
```

````

````{py:attribute} ModeDischarge
:canonical: altdss.StorageController.IStorageController.ModeDischarge
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.ModeDischarge
```

````

````{py:attribute} ModeDischarge_str
:canonical: altdss.StorageController.IStorageController.ModeDischarge_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.ModeDischarge_str
```

````

````{py:attribute} MonPhase
:canonical: altdss.StorageController.IStorageController.MonPhase
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.MonPhase
```

````

````{py:attribute} MonPhase_str
:canonical: altdss.StorageController.IStorageController.MonPhase_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.MonPhase_str
```

````

````{py:property} Name
:canonical: altdss.StorageController.IStorageController.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.StorageController.IStorageController.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.StorageController.IStorageController.NumConductors

```{autodoc2-docstring} altdss.StorageController.IStorageController.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.StorageController.IStorageController.NumControllers

```{autodoc2-docstring} altdss.StorageController.IStorageController.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.StorageController.IStorageController.NumPhases

```{autodoc2-docstring} altdss.StorageController.IStorageController.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.StorageController.IStorageController.NumTerminals

```{autodoc2-docstring} altdss.StorageController.IStorageController.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.StorageController.IStorageController.OCPDevice

```{autodoc2-docstring} altdss.StorageController.IStorageController.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.StorageController.IStorageController.OCPDeviceIndex

```{autodoc2-docstring} altdss.StorageController.IStorageController.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.StorageController.IStorageController.OCPDeviceType

```{autodoc2-docstring} altdss.StorageController.IStorageController.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.IStorageController.PhaseLosses

```{autodoc2-docstring} altdss.StorageController.IStorageController.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.IStorageController.Powers

```{autodoc2-docstring} altdss.StorageController.IStorageController.Powers
```

````

````{py:attribute} ResetLevel
:canonical: altdss.StorageController.IStorageController.ResetLevel
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.ResetLevel
```

````

````{py:attribute} SeasonTargets
:canonical: altdss.StorageController.IStorageController.SeasonTargets
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.SeasonTargets
```

````

````{py:attribute} SeasonTargetsLow
:canonical: altdss.StorageController.IStorageController.SeasonTargetsLow
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.SeasonTargetsLow
```

````

````{py:attribute} Seasons
:canonical: altdss.StorageController.IStorageController.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Seasons
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.StorageController.IStorageController.SeqCurrents

```{autodoc2-docstring} altdss.StorageController.IStorageController.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.IStorageController.SeqPowers

```{autodoc2-docstring} altdss.StorageController.IStorageController.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.StorageController.IStorageController.SeqVoltages

```{autodoc2-docstring} altdss.StorageController.IStorageController.SeqVoltages
```

````

````{py:attribute} TDn
:canonical: altdss.StorageController.IStorageController.TDn
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.TDn
```

````

````{py:attribute} TFlat
:canonical: altdss.StorageController.IStorageController.TFlat
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.TFlat
```

````

````{py:attribute} TUp
:canonical: altdss.StorageController.IStorageController.TUp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.TUp
```

````

````{py:attribute} Terminal
:canonical: altdss.StorageController.IStorageController.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Terminal
```

````

````{py:attribute} TimeChargeTrigger
:canonical: altdss.StorageController.IStorageController.TimeChargeTrigger
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.TimeChargeTrigger
```

````

````{py:attribute} TimeDischargeTrigger
:canonical: altdss.StorageController.IStorageController.TimeDischargeTrigger
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.TimeDischargeTrigger
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.IStorageController.TotalPowers

```{autodoc2-docstring} altdss.StorageController.IStorageController.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.IStorageController.Voltages

```{autodoc2-docstring} altdss.StorageController.IStorageController.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.StorageController.IStorageController.VoltagesMagAng

```{autodoc2-docstring} altdss.StorageController.IStorageController.VoltagesMagAng
```

````

````{py:attribute} Weights
:canonical: altdss.StorageController.IStorageController.Weights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Weights
```

````

````{py:attribute} Yearly
:canonical: altdss.StorageController.IStorageController.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.StorageController.IStorageController.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.StorageController.IStorageController.__call__

```{autodoc2-docstring} altdss.StorageController.IStorageController.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.StorageController.IStorageController.__contains__

```{autodoc2-docstring} altdss.StorageController.IStorageController.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.StorageController.IStorageController.__getitem__

```{autodoc2-docstring} altdss.StorageController.IStorageController.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.StorageController.IStorageController.__init__

```{autodoc2-docstring} altdss.StorageController.IStorageController.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.StorageController.IStorageController.__iter__

```{autodoc2-docstring} altdss.StorageController.IStorageController.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.StorageController.IStorageController.__len__

```{autodoc2-docstring} altdss.StorageController.IStorageController.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.StorageController.IStorageController.batch

```{autodoc2-docstring} altdss.StorageController.IStorageController.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.StorageController.StorageControllerBatchProperties]) -> altdss.StorageController.StorageControllerBatch
:canonical: altdss.StorageController.IStorageController.batch_new

```{autodoc2-docstring} altdss.StorageController.IStorageController.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.StorageController.IStorageController.begin_edit

```{autodoc2-docstring} altdss.StorageController.IStorageController.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.StorageController.IStorageController.end_edit

```{autodoc2-docstring} altdss.StorageController.IStorageController.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.StorageController.IStorageController.find

```{autodoc2-docstring} altdss.StorageController.IStorageController.find
```

````

````{py:attribute} kWActual
:canonical: altdss.StorageController.IStorageController.kWActual
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWActual
```

````

````{py:attribute} kWBand
:canonical: altdss.StorageController.IStorageController.kWBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWBand
```

````

````{py:attribute} kWBandLow
:canonical: altdss.StorageController.IStorageController.kWBandLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWBandLow
```

````

````{py:attribute} kWNeed
:canonical: altdss.StorageController.IStorageController.kWNeed
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWNeed
```

````

````{py:attribute} kWTarget
:canonical: altdss.StorageController.IStorageController.kWTarget
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWTarget
```

````

````{py:attribute} kWTargetLow
:canonical: altdss.StorageController.IStorageController.kWTargetLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWTargetLow
```

````

````{py:attribute} kWThreshold
:canonical: altdss.StorageController.IStorageController.kWThreshold
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWThreshold
```

````

````{py:attribute} kWTotal
:canonical: altdss.StorageController.IStorageController.kWTotal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWTotal
```

````

````{py:attribute} kWhActual
:canonical: altdss.StorageController.IStorageController.kWhActual
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWhActual
```

````

````{py:attribute} kWhTotal
:canonical: altdss.StorageController.IStorageController.kWhTotal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.kWhTotal
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.StorageController.StorageControllerProperties]) -> altdss.StorageController.StorageController
:canonical: altdss.StorageController.IStorageController.new

```{autodoc2-docstring} altdss.StorageController.IStorageController.new
```

````

````{py:attribute} pctRateCharge
:canonical: altdss.StorageController.IStorageController.pctRateCharge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.pctRateCharge
```

````

````{py:attribute} pctRatekW
:canonical: altdss.StorageController.IStorageController.pctRatekW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.pctRatekW
```

````

````{py:attribute} pctReserve
:canonical: altdss.StorageController.IStorageController.pctReserve
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.pctReserve
```

````

````{py:attribute} pctkWBand
:canonical: altdss.StorageController.IStorageController.pctkWBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.pctkWBand
```

````

````{py:attribute} pctkWBandLow
:canonical: altdss.StorageController.IStorageController.pctkWBandLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.IStorageController.pctkWBandLow
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.StorageController.IStorageController.to_json

```{autodoc2-docstring} altdss.StorageController.IStorageController.to_json
```

````

````{py:method} to_list()
:canonical: altdss.StorageController.IStorageController.to_list

```{autodoc2-docstring} altdss.StorageController.IStorageController.to_list
```

````

`````

`````{py:class} StorageController(api_util, ptr)
:canonical: altdss.StorageController.StorageController

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.StorageController.StorageController
```

````{py:attribute} BaseFreq
:canonical: altdss.StorageController.StorageController.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.StorageController.StorageController.Close

```{autodoc2-docstring} altdss.StorageController.StorageController.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageController.ComplexSeqCurrents

```{autodoc2-docstring} altdss.StorageController.StorageController.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageController.ComplexSeqVoltages

```{autodoc2-docstring} altdss.StorageController.StorageController.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageController.Currents

```{autodoc2-docstring} altdss.StorageController.StorageController.Currents
```

````

````{py:attribute} Daily
:canonical: altdss.StorageController.StorageController.Daily
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.StorageController.StorageController.Daily_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Daily_str
```

````

````{py:attribute} DispFactor
:canonical: altdss.StorageController.StorageController.DispFactor
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.DispFactor
```

````

````{py:attribute} DisplayName
:canonical: altdss.StorageController.StorageController.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.DisplayName
```

````

````{py:attribute} Duty
:canonical: altdss.StorageController.StorageController.Duty
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.StorageController.StorageController.Duty_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Duty_str
```

````

````{py:attribute} Element
:canonical: altdss.StorageController.StorageController.Element
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Element
```

````

````{py:attribute} ElementList
:canonical: altdss.StorageController.StorageController.ElementList
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.ElementList
```

````

````{py:attribute} Element_str
:canonical: altdss.StorageController.StorageController.Element_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.StorageController.StorageController.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.StorageController.StorageController.EventLog
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.EventLog
```

````

````{py:method} FullName() -> str
:canonical: altdss.StorageController.StorageController.FullName

```{autodoc2-docstring} altdss.StorageController.StorageController.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.StorageController.StorageController.GUID

```{autodoc2-docstring} altdss.StorageController.StorageController.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.StorageController.StorageController.Handle

```{autodoc2-docstring} altdss.StorageController.StorageController.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.StorageController.StorageController.HasOCPDevice

```{autodoc2-docstring} altdss.StorageController.StorageController.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.StorageController.StorageController.HasSwitchControl

```{autodoc2-docstring} altdss.StorageController.StorageController.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.StorageController.StorageController.HasVoltControl

```{autodoc2-docstring} altdss.StorageController.StorageController.HasVoltControl
```

````

````{py:attribute} InhibitTime
:canonical: altdss.StorageController.StorageController.InhibitTime
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.InhibitTime
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.StorageController.StorageController.IsIsolated

```{autodoc2-docstring} altdss.StorageController.StorageController.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.StorageController.StorageController.IsOpen

```{autodoc2-docstring} altdss.StorageController.StorageController.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.StorageController.StorageController.Like

```{autodoc2-docstring} altdss.StorageController.StorageController.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.StorageController.StorageController.Losses

```{autodoc2-docstring} altdss.StorageController.StorageController.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.StorageController.StorageController.MaxCurrent

```{autodoc2-docstring} altdss.StorageController.StorageController.MaxCurrent
```

````

````{py:attribute} ModeCharge
:canonical: altdss.StorageController.StorageController.ModeCharge
:type: altdss.enums.StorageControllerChargeMode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.ModeCharge
```

````

````{py:attribute} ModeCharge_str
:canonical: altdss.StorageController.StorageController.ModeCharge_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.ModeCharge_str
```

````

````{py:attribute} ModeDischarge
:canonical: altdss.StorageController.StorageController.ModeDischarge
:type: altdss.enums.StorageControllerDischargeMode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.ModeDischarge
```

````

````{py:attribute} ModeDischarge_str
:canonical: altdss.StorageController.StorageController.ModeDischarge_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.ModeDischarge_str
```

````

````{py:attribute} MonPhase
:canonical: altdss.StorageController.StorageController.MonPhase
:type: altdss.enums.MonitoredPhase
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.MonPhase
```

````

````{py:attribute} MonPhase_str
:canonical: altdss.StorageController.StorageController.MonPhase_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.MonPhase_str
```

````

````{py:property} Name
:canonical: altdss.StorageController.StorageController.Name
:type: str

```{autodoc2-docstring} altdss.StorageController.StorageController.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.StorageController.StorageController.NodeOrder

```{autodoc2-docstring} altdss.StorageController.StorageController.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.StorageController.StorageController.NodeRef

```{autodoc2-docstring} altdss.StorageController.StorageController.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.StorageController.StorageController.NumConductors

```{autodoc2-docstring} altdss.StorageController.StorageController.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.StorageController.StorageController.NumControllers

```{autodoc2-docstring} altdss.StorageController.StorageController.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.StorageController.StorageController.NumPhases

```{autodoc2-docstring} altdss.StorageController.StorageController.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.StorageController.StorageController.NumTerminals

```{autodoc2-docstring} altdss.StorageController.StorageController.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.StorageController.StorageController.OCPDevice

```{autodoc2-docstring} altdss.StorageController.StorageController.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.StorageController.StorageController.OCPDeviceIndex

```{autodoc2-docstring} altdss.StorageController.StorageController.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.StorageController.StorageController.OCPDeviceType

```{autodoc2-docstring} altdss.StorageController.StorageController.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.StorageController.StorageController.Open

```{autodoc2-docstring} altdss.StorageController.StorageController.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageController.PhaseLosses

```{autodoc2-docstring} altdss.StorageController.StorageController.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageController.Powers

```{autodoc2-docstring} altdss.StorageController.StorageController.Powers
```

````

````{py:attribute} ResetLevel
:canonical: altdss.StorageController.StorageController.ResetLevel
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.ResetLevel
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.StorageController.StorageController.Residuals

```{autodoc2-docstring} altdss.StorageController.StorageController.Residuals
```

````

````{py:attribute} SeasonTargets
:canonical: altdss.StorageController.StorageController.SeasonTargets
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.SeasonTargets
```

````

````{py:attribute} SeasonTargetsLow
:canonical: altdss.StorageController.StorageController.SeasonTargetsLow
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.SeasonTargetsLow
```

````

````{py:attribute} Seasons
:canonical: altdss.StorageController.StorageController.Seasons
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Seasons
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.StorageController.StorageController.SeqCurrents

```{autodoc2-docstring} altdss.StorageController.StorageController.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageController.SeqPowers

```{autodoc2-docstring} altdss.StorageController.StorageController.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.StorageController.StorageController.SeqVoltages

```{autodoc2-docstring} altdss.StorageController.StorageController.SeqVoltages
```

````

````{py:attribute} TDn
:canonical: altdss.StorageController.StorageController.TDn
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.TDn
```

````

````{py:attribute} TFlat
:canonical: altdss.StorageController.StorageController.TFlat
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.TFlat
```

````

````{py:attribute} TUp
:canonical: altdss.StorageController.StorageController.TUp
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.TUp
```

````

````{py:attribute} Terminal
:canonical: altdss.StorageController.StorageController.Terminal
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Terminal
```

````

````{py:attribute} TimeChargeTrigger
:canonical: altdss.StorageController.StorageController.TimeChargeTrigger
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.TimeChargeTrigger
```

````

````{py:attribute} TimeDischargeTrigger
:canonical: altdss.StorageController.StorageController.TimeDischargeTrigger
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.TimeDischargeTrigger
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageController.TotalPowers

```{autodoc2-docstring} altdss.StorageController.StorageController.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageController.Voltages

```{autodoc2-docstring} altdss.StorageController.StorageController.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.StorageController.StorageController.VoltagesMagAng

```{autodoc2-docstring} altdss.StorageController.StorageController.VoltagesMagAng
```

````

````{py:attribute} Weights
:canonical: altdss.StorageController.StorageController.Weights
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Weights
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageController.YPrim

```{autodoc2-docstring} altdss.StorageController.StorageController.YPrim
```

````

````{py:attribute} Yearly
:canonical: altdss.StorageController.StorageController.Yearly
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.StorageController.StorageController.Yearly_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.Yearly_str
```

````

````{py:method} __hash__()
:canonical: altdss.StorageController.StorageController.__hash__

```{autodoc2-docstring} altdss.StorageController.StorageController.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.StorageController.StorageController.__init__

```{autodoc2-docstring} altdss.StorageController.StorageController.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.StorageController.StorageController.__ne__

```{autodoc2-docstring} altdss.StorageController.StorageController.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.StorageController.StorageController.__repr__

```{autodoc2-docstring} altdss.StorageController.StorageController.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.StorageController.StorageController.begin_edit

```{autodoc2-docstring} altdss.StorageController.StorageController.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.StorageController.StorageController.end_edit

```{autodoc2-docstring} altdss.StorageController.StorageController.end_edit
```

````

````{py:attribute} kWActual
:canonical: altdss.StorageController.StorageController.kWActual
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWActual
```

````

````{py:attribute} kWBand
:canonical: altdss.StorageController.StorageController.kWBand
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWBand
```

````

````{py:attribute} kWBandLow
:canonical: altdss.StorageController.StorageController.kWBandLow
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWBandLow
```

````

````{py:attribute} kWNeed
:canonical: altdss.StorageController.StorageController.kWNeed
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWNeed
```

````

````{py:attribute} kWTarget
:canonical: altdss.StorageController.StorageController.kWTarget
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWTarget
```

````

````{py:attribute} kWTargetLow
:canonical: altdss.StorageController.StorageController.kWTargetLow
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWTargetLow
```

````

````{py:attribute} kWThreshold
:canonical: altdss.StorageController.StorageController.kWThreshold
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWThreshold
```

````

````{py:attribute} kWTotal
:canonical: altdss.StorageController.StorageController.kWTotal
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWTotal
```

````

````{py:attribute} kWhActual
:canonical: altdss.StorageController.StorageController.kWhActual
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWhActual
```

````

````{py:attribute} kWhTotal
:canonical: altdss.StorageController.StorageController.kWhTotal
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.kWhTotal
```

````

````{py:attribute} pctRateCharge
:canonical: altdss.StorageController.StorageController.pctRateCharge
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.pctRateCharge
```

````

````{py:attribute} pctRatekW
:canonical: altdss.StorageController.StorageController.pctRatekW
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.pctRatekW
```

````

````{py:attribute} pctReserve
:canonical: altdss.StorageController.StorageController.pctReserve
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.pctReserve
```

````

````{py:attribute} pctkWBand
:canonical: altdss.StorageController.StorageController.pctkWBand
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.pctkWBand
```

````

````{py:attribute} pctkWBandLow
:canonical: altdss.StorageController.StorageController.pctkWBandLow
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageController.pctkWBandLow
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.StorageController.StorageController.to_json

```{autodoc2-docstring} altdss.StorageController.StorageController.to_json
```

````

`````

`````{py:class} StorageControllerBatch(api_util, **kwargs)
:canonical: altdss.StorageController.StorageControllerBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.StorageController.StorageControllerBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.BaseFreq
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageControllerBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageControllerBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageControllerBatch.Currents

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.StorageController.StorageControllerBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.StorageController.StorageControllerBatch.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.StorageController.StorageControllerBatch.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Daily_str
```

````

````{py:attribute} DispFactor
:canonical: altdss.StorageController.StorageControllerBatch.DispFactor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.DispFactor
```

````

````{py:attribute} Duty
:canonical: altdss.StorageController.StorageControllerBatch.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.StorageController.StorageControllerBatch.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Duty_str
```

````

````{py:attribute} Element
:canonical: altdss.StorageController.StorageControllerBatch.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Element
```

````

````{py:attribute} ElementList
:canonical: altdss.StorageController.StorageControllerBatch.ElementList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.ElementList
```

````

````{py:attribute} Element_str
:canonical: altdss.StorageController.StorageControllerBatch.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.StorageController.StorageControllerBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.StorageController.StorageControllerBatch.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.StorageController.StorageControllerBatch.FullName

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.StorageController.StorageControllerBatch.GUID

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.StorageController.StorageControllerBatch.Handle

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.StorageController.StorageControllerBatch.HasOCPDevice

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.StorageController.StorageControllerBatch.HasSwitchControl

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.StorageController.StorageControllerBatch.HasVoltControl

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.HasVoltControl
```

````

````{py:attribute} InhibitTime
:canonical: altdss.StorageController.StorageControllerBatch.InhibitTime
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.InhibitTime
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.StorageController.StorageControllerBatch.IsIsolated

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.StorageController.StorageControllerBatch.Like

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageControllerBatch.Losses

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.StorageController.StorageControllerBatch.MaxCurrent

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.MaxCurrent
```

````

````{py:attribute} ModeCharge
:canonical: altdss.StorageController.StorageControllerBatch.ModeCharge
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.ModeCharge
```

````

````{py:attribute} ModeCharge_str
:canonical: altdss.StorageController.StorageControllerBatch.ModeCharge_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.ModeCharge_str
```

````

````{py:attribute} ModeDischarge
:canonical: altdss.StorageController.StorageControllerBatch.ModeDischarge
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.ModeDischarge
```

````

````{py:attribute} ModeDischarge_str
:canonical: altdss.StorageController.StorageControllerBatch.ModeDischarge_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.ModeDischarge_str
```

````

````{py:attribute} MonPhase
:canonical: altdss.StorageController.StorageControllerBatch.MonPhase
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.MonPhase
```

````

````{py:attribute} MonPhase_str
:canonical: altdss.StorageController.StorageControllerBatch.MonPhase_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.MonPhase_str
```

````

````{py:property} Name
:canonical: altdss.StorageController.StorageControllerBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.StorageController.StorageControllerBatch.NumConductors

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.StorageController.StorageControllerBatch.NumControllers

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.StorageController.StorageControllerBatch.NumPhases

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.StorageController.StorageControllerBatch.NumTerminals

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.StorageController.StorageControllerBatch.OCPDevice

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.StorageController.StorageControllerBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.StorageController.StorageControllerBatch.OCPDeviceType

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageControllerBatch.PhaseLosses

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageControllerBatch.Powers

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Powers
```

````

````{py:attribute} ResetLevel
:canonical: altdss.StorageController.StorageControllerBatch.ResetLevel
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.ResetLevel
```

````

````{py:attribute} SeasonTargets
:canonical: altdss.StorageController.StorageControllerBatch.SeasonTargets
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.SeasonTargets
```

````

````{py:attribute} SeasonTargetsLow
:canonical: altdss.StorageController.StorageControllerBatch.SeasonTargetsLow
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.SeasonTargetsLow
```

````

````{py:attribute} Seasons
:canonical: altdss.StorageController.StorageControllerBatch.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Seasons
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.StorageController.StorageControllerBatch.SeqCurrents

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageControllerBatch.SeqPowers

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.StorageController.StorageControllerBatch.SeqVoltages

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.SeqVoltages
```

````

````{py:attribute} TDn
:canonical: altdss.StorageController.StorageControllerBatch.TDn
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.TDn
```

````

````{py:attribute} TFlat
:canonical: altdss.StorageController.StorageControllerBatch.TFlat
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.TFlat
```

````

````{py:attribute} TUp
:canonical: altdss.StorageController.StorageControllerBatch.TUp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.TUp
```

````

````{py:attribute} Terminal
:canonical: altdss.StorageController.StorageControllerBatch.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Terminal
```

````

````{py:attribute} TimeChargeTrigger
:canonical: altdss.StorageController.StorageControllerBatch.TimeChargeTrigger
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.TimeChargeTrigger
```

````

````{py:attribute} TimeDischargeTrigger
:canonical: altdss.StorageController.StorageControllerBatch.TimeDischargeTrigger
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.TimeDischargeTrigger
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageControllerBatch.TotalPowers

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.StorageController.StorageControllerBatch.Voltages

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.StorageController.StorageControllerBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.VoltagesMagAng
```

````

````{py:attribute} Weights
:canonical: altdss.StorageController.StorageControllerBatch.Weights
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Weights
```

````

````{py:attribute} Yearly
:canonical: altdss.StorageController.StorageControllerBatch.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.StorageController.StorageControllerBatch.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.StorageController.StorageControllerBatch.__call__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.StorageController.StorageControllerBatch.__getitem__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.StorageController.StorageControllerBatch.__init__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.StorageController.StorageControllerBatch.__iter__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.StorageController.StorageControllerBatch.__len__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.StorageController.StorageControllerBatch.batch

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.StorageController.StorageControllerBatch.begin_edit

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.StorageController.StorageControllerBatch.end_edit

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.end_edit
```

````

````{py:attribute} kWActual
:canonical: altdss.StorageController.StorageControllerBatch.kWActual
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWActual
```

````

````{py:attribute} kWBand
:canonical: altdss.StorageController.StorageControllerBatch.kWBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWBand
```

````

````{py:attribute} kWBandLow
:canonical: altdss.StorageController.StorageControllerBatch.kWBandLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWBandLow
```

````

````{py:attribute} kWNeed
:canonical: altdss.StorageController.StorageControllerBatch.kWNeed
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWNeed
```

````

````{py:attribute} kWTarget
:canonical: altdss.StorageController.StorageControllerBatch.kWTarget
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWTarget
```

````

````{py:attribute} kWTargetLow
:canonical: altdss.StorageController.StorageControllerBatch.kWTargetLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWTargetLow
```

````

````{py:attribute} kWThreshold
:canonical: altdss.StorageController.StorageControllerBatch.kWThreshold
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWThreshold
```

````

````{py:attribute} kWTotal
:canonical: altdss.StorageController.StorageControllerBatch.kWTotal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWTotal
```

````

````{py:attribute} kWhActual
:canonical: altdss.StorageController.StorageControllerBatch.kWhActual
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWhActual
```

````

````{py:attribute} kWhTotal
:canonical: altdss.StorageController.StorageControllerBatch.kWhTotal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.kWhTotal
```

````

````{py:attribute} pctRateCharge
:canonical: altdss.StorageController.StorageControllerBatch.pctRateCharge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.pctRateCharge
```

````

````{py:attribute} pctRatekW
:canonical: altdss.StorageController.StorageControllerBatch.pctRatekW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.pctRatekW
```

````

````{py:attribute} pctReserve
:canonical: altdss.StorageController.StorageControllerBatch.pctReserve
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.pctReserve
```

````

````{py:attribute} pctkWBand
:canonical: altdss.StorageController.StorageControllerBatch.pctkWBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.pctkWBand
```

````

````{py:attribute} pctkWBandLow
:canonical: altdss.StorageController.StorageControllerBatch.pctkWBandLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.pctkWBandLow
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.StorageController.StorageControllerBatch.to_json

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.StorageController.StorageControllerBatch.to_list

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatch.to_list
```

````

`````

`````{py:class} StorageControllerBatchProperties()
:canonical: altdss.StorageController.StorageControllerBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.StorageController.StorageControllerBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.BaseFreq
```

````

````{py:attribute} Daily
:canonical: altdss.StorageController.StorageControllerBatchProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.Daily
```

````

````{py:attribute} DispFactor
:canonical: altdss.StorageController.StorageControllerBatchProperties.DispFactor
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.DispFactor
```

````

````{py:attribute} Duty
:canonical: altdss.StorageController.StorageControllerBatchProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.Duty
```

````

````{py:attribute} Element
:canonical: altdss.StorageController.StorageControllerBatchProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.Element
```

````

````{py:attribute} ElementList
:canonical: altdss.StorageController.StorageControllerBatchProperties.ElementList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.ElementList
```

````

````{py:attribute} Enabled
:canonical: altdss.StorageController.StorageControllerBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.StorageController.StorageControllerBatchProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.EventLog
```

````

````{py:attribute} InhibitTime
:canonical: altdss.StorageController.StorageControllerBatchProperties.InhibitTime
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.InhibitTime
```

````

````{py:attribute} Like
:canonical: altdss.StorageController.StorageControllerBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.Like
```

````

````{py:attribute} ModeCharge
:canonical: altdss.StorageController.StorageControllerBatchProperties.ModeCharge
:type: typing.Union[typing.AnyStr, int, altdss.enums.StorageControllerChargeMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.StorageControllerChargeMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.ModeCharge
```

````

````{py:attribute} ModeDischarge
:canonical: altdss.StorageController.StorageControllerBatchProperties.ModeDischarge
:type: typing.Union[typing.AnyStr, int, altdss.enums.StorageControllerDischargeMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.StorageControllerDischargeMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.ModeDischarge
```

````

````{py:attribute} MonPhase
:canonical: altdss.StorageController.StorageControllerBatchProperties.MonPhase
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitoredPhase, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.MonitoredPhase], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.MonPhase
```

````

````{py:attribute} ResetLevel
:canonical: altdss.StorageController.StorageControllerBatchProperties.ResetLevel
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.ResetLevel
```

````

````{py:attribute} SeasonTargets
:canonical: altdss.StorageController.StorageControllerBatchProperties.SeasonTargets
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.SeasonTargets
```

````

````{py:attribute} SeasonTargetsLow
:canonical: altdss.StorageController.StorageControllerBatchProperties.SeasonTargetsLow
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.SeasonTargetsLow
```

````

````{py:attribute} Seasons
:canonical: altdss.StorageController.StorageControllerBatchProperties.Seasons
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.Seasons
```

````

````{py:attribute} TDn
:canonical: altdss.StorageController.StorageControllerBatchProperties.TDn
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.TDn
```

````

````{py:attribute} TFlat
:canonical: altdss.StorageController.StorageControllerBatchProperties.TFlat
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.TFlat
```

````

````{py:attribute} TUp
:canonical: altdss.StorageController.StorageControllerBatchProperties.TUp
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.TUp
```

````

````{py:attribute} Terminal
:canonical: altdss.StorageController.StorageControllerBatchProperties.Terminal
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.Terminal
```

````

````{py:attribute} TimeChargeTrigger
:canonical: altdss.StorageController.StorageControllerBatchProperties.TimeChargeTrigger
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.TimeChargeTrigger
```

````

````{py:attribute} TimeDischargeTrigger
:canonical: altdss.StorageController.StorageControllerBatchProperties.TimeDischargeTrigger
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.TimeDischargeTrigger
```

````

````{py:attribute} Weights
:canonical: altdss.StorageController.StorageControllerBatchProperties.Weights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.Weights
```

````

````{py:attribute} Yearly
:canonical: altdss.StorageController.StorageControllerBatchProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__contains__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__delattr__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__delitem__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__dir__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__format__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__ge__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__getitem__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__getstate__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__gt__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__init__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__ior__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__iter__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__le__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__len__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__lt__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__ne__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__new__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__or__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__reduce__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__repr__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__reversed__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__ror__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__setitem__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__str__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.StorageController.StorageControllerBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.StorageController.StorageControllerBatchProperties.clear

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.StorageController.StorageControllerBatchProperties.copy

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.StorageController.StorageControllerBatchProperties.get

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.StorageController.StorageControllerBatchProperties.items

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.items
```

````

````{py:attribute} kWActual
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWActual
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWActual
```

````

````{py:attribute} kWBand
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWBand
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWBand
```

````

````{py:attribute} kWBandLow
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWBandLow
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWBandLow
```

````

````{py:attribute} kWNeed
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWNeed
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWNeed
```

````

````{py:attribute} kWTarget
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWTarget
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWTarget
```

````

````{py:attribute} kWTargetLow
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWTargetLow
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWTargetLow
```

````

````{py:attribute} kWThreshold
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWThreshold
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWThreshold
```

````

````{py:attribute} kWTotal
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWTotal
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWTotal
```

````

````{py:attribute} kWhActual
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWhActual
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWhActual
```

````

````{py:attribute} kWhTotal
:canonical: altdss.StorageController.StorageControllerBatchProperties.kWhTotal
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.kWhTotal
```

````

````{py:method} keys()
:canonical: altdss.StorageController.StorageControllerBatchProperties.keys

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.keys
```

````

````{py:attribute} pctRateCharge
:canonical: altdss.StorageController.StorageControllerBatchProperties.pctRateCharge
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.pctRateCharge
```

````

````{py:attribute} pctRatekW
:canonical: altdss.StorageController.StorageControllerBatchProperties.pctRatekW
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.pctRatekW
```

````

````{py:attribute} pctReserve
:canonical: altdss.StorageController.StorageControllerBatchProperties.pctReserve
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.pctReserve
```

````

````{py:attribute} pctkWBand
:canonical: altdss.StorageController.StorageControllerBatchProperties.pctkWBand
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.pctkWBand
```

````

````{py:attribute} pctkWBandLow
:canonical: altdss.StorageController.StorageControllerBatchProperties.pctkWBandLow
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.pctkWBandLow
```

````

````{py:method} pop()
:canonical: altdss.StorageController.StorageControllerBatchProperties.pop

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.StorageController.StorageControllerBatchProperties.popitem

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.StorageController.StorageControllerBatchProperties.setdefault

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.StorageController.StorageControllerBatchProperties.update

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.StorageController.StorageControllerBatchProperties.values

```{autodoc2-docstring} altdss.StorageController.StorageControllerBatchProperties.values
```

````

`````

`````{py:class} StorageControllerProperties()
:canonical: altdss.StorageController.StorageControllerProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.StorageController.StorageControllerProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.BaseFreq
```

````

````{py:attribute} Daily
:canonical: altdss.StorageController.StorageControllerProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.Daily
```

````

````{py:attribute} DispFactor
:canonical: altdss.StorageController.StorageControllerProperties.DispFactor
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.DispFactor
```

````

````{py:attribute} Duty
:canonical: altdss.StorageController.StorageControllerProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.Duty
```

````

````{py:attribute} Element
:canonical: altdss.StorageController.StorageControllerProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.Element
```

````

````{py:attribute} ElementList
:canonical: altdss.StorageController.StorageControllerProperties.ElementList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.ElementList
```

````

````{py:attribute} Enabled
:canonical: altdss.StorageController.StorageControllerProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.StorageController.StorageControllerProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.EventLog
```

````

````{py:attribute} InhibitTime
:canonical: altdss.StorageController.StorageControllerProperties.InhibitTime
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.InhibitTime
```

````

````{py:attribute} Like
:canonical: altdss.StorageController.StorageControllerProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.Like
```

````

````{py:attribute} ModeCharge
:canonical: altdss.StorageController.StorageControllerProperties.ModeCharge
:type: typing.Union[typing.AnyStr, int, altdss.enums.StorageControllerChargeMode]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.ModeCharge
```

````

````{py:attribute} ModeDischarge
:canonical: altdss.StorageController.StorageControllerProperties.ModeDischarge
:type: typing.Union[typing.AnyStr, int, altdss.enums.StorageControllerDischargeMode]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.ModeDischarge
```

````

````{py:attribute} MonPhase
:canonical: altdss.StorageController.StorageControllerProperties.MonPhase
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitoredPhase]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.MonPhase
```

````

````{py:attribute} ResetLevel
:canonical: altdss.StorageController.StorageControllerProperties.ResetLevel
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.ResetLevel
```

````

````{py:attribute} SeasonTargets
:canonical: altdss.StorageController.StorageControllerProperties.SeasonTargets
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.SeasonTargets
```

````

````{py:attribute} SeasonTargetsLow
:canonical: altdss.StorageController.StorageControllerProperties.SeasonTargetsLow
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.SeasonTargetsLow
```

````

````{py:attribute} Seasons
:canonical: altdss.StorageController.StorageControllerProperties.Seasons
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.Seasons
```

````

````{py:attribute} TDn
:canonical: altdss.StorageController.StorageControllerProperties.TDn
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.TDn
```

````

````{py:attribute} TFlat
:canonical: altdss.StorageController.StorageControllerProperties.TFlat
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.TFlat
```

````

````{py:attribute} TUp
:canonical: altdss.StorageController.StorageControllerProperties.TUp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.TUp
```

````

````{py:attribute} Terminal
:canonical: altdss.StorageController.StorageControllerProperties.Terminal
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.Terminal
```

````

````{py:attribute} TimeChargeTrigger
:canonical: altdss.StorageController.StorageControllerProperties.TimeChargeTrigger
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.TimeChargeTrigger
```

````

````{py:attribute} TimeDischargeTrigger
:canonical: altdss.StorageController.StorageControllerProperties.TimeDischargeTrigger
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.TimeDischargeTrigger
```

````

````{py:attribute} Weights
:canonical: altdss.StorageController.StorageControllerProperties.Weights
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.Weights
```

````

````{py:attribute} Yearly
:canonical: altdss.StorageController.StorageControllerProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.StorageController.StorageControllerProperties.__contains__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.StorageController.StorageControllerProperties.__delattr__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.StorageController.StorageControllerProperties.__delitem__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.StorageController.StorageControllerProperties.__dir__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.StorageController.StorageControllerProperties.__format__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.StorageController.StorageControllerProperties.__ge__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.StorageController.StorageControllerProperties.__getattribute__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.StorageController.StorageControllerProperties.__getitem__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.StorageController.StorageControllerProperties.__getstate__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.StorageController.StorageControllerProperties.__gt__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.StorageController.StorageControllerProperties.__init__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.StorageController.StorageControllerProperties.__ior__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.StorageController.StorageControllerProperties.__iter__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.StorageController.StorageControllerProperties.__le__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.StorageController.StorageControllerProperties.__len__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.StorageController.StorageControllerProperties.__lt__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.StorageController.StorageControllerProperties.__ne__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.StorageController.StorageControllerProperties.__new__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.StorageController.StorageControllerProperties.__or__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.StorageController.StorageControllerProperties.__reduce__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.StorageController.StorageControllerProperties.__reduce_ex__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.StorageController.StorageControllerProperties.__repr__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.StorageController.StorageControllerProperties.__reversed__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.StorageController.StorageControllerProperties.__ror__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.StorageController.StorageControllerProperties.__setitem__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.StorageController.StorageControllerProperties.__sizeof__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.StorageController.StorageControllerProperties.__str__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.StorageController.StorageControllerProperties.__subclasshook__

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.StorageController.StorageControllerProperties.clear

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.StorageController.StorageControllerProperties.copy

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.copy
```

````

````{py:method} get()
:canonical: altdss.StorageController.StorageControllerProperties.get

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.get
```

````

````{py:method} items()
:canonical: altdss.StorageController.StorageControllerProperties.items

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.items
```

````

````{py:attribute} kWActual
:canonical: altdss.StorageController.StorageControllerProperties.kWActual
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWActual
```

````

````{py:attribute} kWBand
:canonical: altdss.StorageController.StorageControllerProperties.kWBand
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWBand
```

````

````{py:attribute} kWBandLow
:canonical: altdss.StorageController.StorageControllerProperties.kWBandLow
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWBandLow
```

````

````{py:attribute} kWNeed
:canonical: altdss.StorageController.StorageControllerProperties.kWNeed
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWNeed
```

````

````{py:attribute} kWTarget
:canonical: altdss.StorageController.StorageControllerProperties.kWTarget
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWTarget
```

````

````{py:attribute} kWTargetLow
:canonical: altdss.StorageController.StorageControllerProperties.kWTargetLow
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWTargetLow
```

````

````{py:attribute} kWThreshold
:canonical: altdss.StorageController.StorageControllerProperties.kWThreshold
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWThreshold
```

````

````{py:attribute} kWTotal
:canonical: altdss.StorageController.StorageControllerProperties.kWTotal
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWTotal
```

````

````{py:attribute} kWhActual
:canonical: altdss.StorageController.StorageControllerProperties.kWhActual
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWhActual
```

````

````{py:attribute} kWhTotal
:canonical: altdss.StorageController.StorageControllerProperties.kWhTotal
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.kWhTotal
```

````

````{py:method} keys()
:canonical: altdss.StorageController.StorageControllerProperties.keys

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.keys
```

````

````{py:attribute} pctRateCharge
:canonical: altdss.StorageController.StorageControllerProperties.pctRateCharge
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.pctRateCharge
```

````

````{py:attribute} pctRatekW
:canonical: altdss.StorageController.StorageControllerProperties.pctRatekW
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.pctRatekW
```

````

````{py:attribute} pctReserve
:canonical: altdss.StorageController.StorageControllerProperties.pctReserve
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.pctReserve
```

````

````{py:attribute} pctkWBand
:canonical: altdss.StorageController.StorageControllerProperties.pctkWBand
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.pctkWBand
```

````

````{py:attribute} pctkWBandLow
:canonical: altdss.StorageController.StorageControllerProperties.pctkWBandLow
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.pctkWBandLow
```

````

````{py:method} pop()
:canonical: altdss.StorageController.StorageControllerProperties.pop

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.StorageController.StorageControllerProperties.popitem

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.StorageController.StorageControllerProperties.setdefault

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.StorageController.StorageControllerProperties.update

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.update
```

````

````{py:method} values()
:canonical: altdss.StorageController.StorageControllerProperties.values

```{autodoc2-docstring} altdss.StorageController.StorageControllerProperties.values
```

````

`````
