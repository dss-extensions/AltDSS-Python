# {py:mod}`altdss.Load`

```{py:module} altdss.Load
```

```{autodoc2-docstring} altdss.Load
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ILoad <altdss.Load.ILoad>`
  - ```{autodoc2-docstring} altdss.Load.ILoad
    :summary:
    ```
* - {py:obj}`Load <altdss.Load.Load>`
  - ```{autodoc2-docstring} altdss.Load.Load
    :summary:
    ```
* - {py:obj}`LoadBatch <altdss.Load.LoadBatch>`
  - ```{autodoc2-docstring} altdss.Load.LoadBatch
    :summary:
    ```
* - {py:obj}`LoadBatchProperties <altdss.Load.LoadBatchProperties>`
  - ```{autodoc2-docstring} altdss.Load.LoadBatchProperties
    :summary:
    ```
* - {py:obj}`LoadProperties <altdss.Load.LoadProperties>`
  - ```{autodoc2-docstring} altdss.Load.LoadProperties
    :summary:
    ```
````

### API

`````{py:class} ILoad(iobj)
:canonical: altdss.Load.ILoad

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Load.LoadBatch`

```{autodoc2-docstring} altdss.Load.ILoad
```

````{py:attribute} AllocationFactor
:canonical: altdss.Load.ILoad.AllocationFactor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.AllocationFactor
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Load.ILoad.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Load.ILoad.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Bus1
```

````

````{py:attribute} CFactor
:canonical: altdss.Load.ILoad.CFactor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.CFactor
```

````

````{py:attribute} CVRCurve
:canonical: altdss.Load.ILoad.CVRCurve
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.CVRCurve
```

````

````{py:attribute} CVRCurve_str
:canonical: altdss.Load.ILoad.CVRCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.CVRCurve_str
```

````

````{py:attribute} CVRVars
:canonical: altdss.Load.ILoad.CVRVars
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.CVRVars
```

````

````{py:attribute} CVRWatts
:canonical: altdss.Load.ILoad.CVRWatts
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.CVRWatts
```

````

````{py:attribute} Class
:canonical: altdss.Load.ILoad.Class
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Class
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Load.ILoad.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Load.ILoad.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Load.ILoad.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Load.ILoad.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Load.ILoad.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Load.ILoad.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Load.ILoad.Currents

```{autodoc2-docstring} altdss.Load.ILoad.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Load.ILoad.CurrentsMagAng

```{autodoc2-docstring} altdss.Load.ILoad.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.Load.ILoad.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Load.ILoad.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Daily_str
```

````

````{py:attribute} Duty
:canonical: altdss.Load.ILoad.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Load.ILoad.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Load.ILoad.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Load.ILoad.EnergyMeter

```{autodoc2-docstring} altdss.Load.ILoad.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Load.ILoad.EnergyMeterName

```{autodoc2-docstring} altdss.Load.ILoad.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Load.ILoad.FullName

```{autodoc2-docstring} altdss.Load.ILoad.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Load.ILoad.GUID

```{autodoc2-docstring} altdss.Load.ILoad.GUID
```

````

````{py:attribute} Growth
:canonical: altdss.Load.ILoad.Growth
:type: typing.List[altdss.GrowthShape.GrowthShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Growth
```

````

````{py:attribute} Growth_str
:canonical: altdss.Load.ILoad.Growth_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Growth_str
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Load.ILoad.Handle

```{autodoc2-docstring} altdss.Load.ILoad.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Load.ILoad.HasOCPDevice

```{autodoc2-docstring} altdss.Load.ILoad.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Load.ILoad.HasSwitchControl

```{autodoc2-docstring} altdss.Load.ILoad.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Load.ILoad.HasVoltControl

```{autodoc2-docstring} altdss.Load.ILoad.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Load.ILoad.IsIsolated

```{autodoc2-docstring} altdss.Load.ILoad.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Load.ILoad.Like

```{autodoc2-docstring} altdss.Load.ILoad.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Load.ILoad.Losses

```{autodoc2-docstring} altdss.Load.ILoad.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Load.ILoad.MaxCurrent

```{autodoc2-docstring} altdss.Load.ILoad.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Load.ILoad.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Model
```

````

````{py:property} Name
:canonical: altdss.Load.ILoad.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Load.ILoad.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Load.ILoad.NumConductors

```{autodoc2-docstring} altdss.Load.ILoad.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Load.ILoad.NumControllers

```{autodoc2-docstring} altdss.Load.ILoad.NumControllers
```

````

````{py:attribute} NumCust
:canonical: altdss.Load.ILoad.NumCust
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.NumCust
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Load.ILoad.NumPhases

```{autodoc2-docstring} altdss.Load.ILoad.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Load.ILoad.NumTerminals

```{autodoc2-docstring} altdss.Load.ILoad.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Load.ILoad.OCPDevice

```{autodoc2-docstring} altdss.Load.ILoad.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Load.ILoad.OCPDeviceIndex

```{autodoc2-docstring} altdss.Load.ILoad.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Load.ILoad.OCPDeviceType

```{autodoc2-docstring} altdss.Load.ILoad.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.Load.ILoad.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.PF
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Load.ILoad.PhaseLosses

```{autodoc2-docstring} altdss.Load.ILoad.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Load.ILoad.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Load.ILoad.Powers

```{autodoc2-docstring} altdss.Load.ILoad.Powers
```

````

````{py:attribute} RNeut
:canonical: altdss.Load.ILoad.RNeut
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.RNeut
```

````

````{py:attribute} RelWeight
:canonical: altdss.Load.ILoad.RelWeight
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.RelWeight
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Load.ILoad.SeqCurrents

```{autodoc2-docstring} altdss.Load.ILoad.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Load.ILoad.SeqPowers

```{autodoc2-docstring} altdss.Load.ILoad.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Load.ILoad.SeqVoltages

```{autodoc2-docstring} altdss.Load.ILoad.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.Load.ILoad.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Load.ILoad.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Spectrum_str
```

````

````{py:attribute} Status
:canonical: altdss.Load.ILoad.Status
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Status
```

````

````{py:attribute} Status_str
:canonical: altdss.Load.ILoad.Status_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Status_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Load.ILoad.TotalPowers

```{autodoc2-docstring} altdss.Load.ILoad.TotalPowers
```

````

````{py:attribute} VLowpu
:canonical: altdss.Load.ILoad.VLowpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.VLowpu
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Load.ILoad.VMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.VMaxpu
```

````

````{py:attribute} VMinEmerg
:canonical: altdss.Load.ILoad.VMinEmerg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.VMinEmerg
```

````

````{py:attribute} VMinNorm
:canonical: altdss.Load.ILoad.VMinNorm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.VMinNorm
```

````

````{py:attribute} VMinpu
:canonical: altdss.Load.ILoad.VMinpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.VMinpu
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Load.ILoad.Voltages

```{autodoc2-docstring} altdss.Load.ILoad.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Load.ILoad.VoltagesMagAng

```{autodoc2-docstring} altdss.Load.ILoad.VoltagesMagAng
```

````

````{py:attribute} XNeut
:canonical: altdss.Load.ILoad.XNeut
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.XNeut
```

````

````{py:attribute} XRHarm
:canonical: altdss.Load.ILoad.XRHarm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.XRHarm
```

````

````{py:attribute} XfkVA
:canonical: altdss.Load.ILoad.XfkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.XfkVA
```

````

````{py:attribute} Yearly
:canonical: altdss.Load.ILoad.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Load.ILoad.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.Yearly_str
```

````

````{py:attribute} ZIPV
:canonical: altdss.Load.ILoad.ZIPV
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.ZIPV
```

````

````{py:method} __call__()
:canonical: altdss.Load.ILoad.__call__

```{autodoc2-docstring} altdss.Load.ILoad.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Load.ILoad.__contains__

```{autodoc2-docstring} altdss.Load.ILoad.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Load.ILoad.__getitem__

```{autodoc2-docstring} altdss.Load.ILoad.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Load.ILoad.__init__

```{autodoc2-docstring} altdss.Load.ILoad.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Load.ILoad.__iter__

```{autodoc2-docstring} altdss.Load.ILoad.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Load.ILoad.__len__

```{autodoc2-docstring} altdss.Load.ILoad.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Load.ILoad.batch

```{autodoc2-docstring} altdss.Load.ILoad.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.Load.LoadBatchProperties]) -> altdss.Load.LoadBatch
:canonical: altdss.Load.ILoad.batch_new

```{autodoc2-docstring} altdss.Load.ILoad.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Load.ILoad.begin_edit

```{autodoc2-docstring} altdss.Load.ILoad.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Load.LoadBatchProperties]) -> altdss.Load.LoadBatch
:canonical: altdss.Load.ILoad.edit

```{autodoc2-docstring} altdss.Load.ILoad.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Load.ILoad.end_edit

```{autodoc2-docstring} altdss.Load.ILoad.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Load.ILoad.find

```{autodoc2-docstring} altdss.Load.ILoad.find
```

````

````{py:attribute} kV
:canonical: altdss.Load.ILoad.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Load.ILoad.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Load.ILoad.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.kW
```

````

````{py:attribute} kWh
:canonical: altdss.Load.ILoad.kWh
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.kWh
```

````

````{py:attribute} kWhDays
:canonical: altdss.Load.ILoad.kWhDays
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.kWhDays
```

````

````{py:attribute} kvar
:canonical: altdss.Load.ILoad.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.kvar
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.Load.LoadProperties]) -> altdss.Load.Load
:canonical: altdss.Load.ILoad.new

```{autodoc2-docstring} altdss.Load.ILoad.new
```

````

````{py:attribute} pctMean
:canonical: altdss.Load.ILoad.pctMean
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.pctMean
```

````

````{py:attribute} pctSeriesRL
:canonical: altdss.Load.ILoad.pctSeriesRL
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.pctSeriesRL
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Load.ILoad.pctStdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.pctStdDev
```

````

````{py:attribute} puXHarm
:canonical: altdss.Load.ILoad.puXHarm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.ILoad.puXHarm
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Load.ILoad.to_json

```{autodoc2-docstring} altdss.Load.ILoad.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Load.ILoad.to_list

```{autodoc2-docstring} altdss.Load.ILoad.to_list
```

````

`````

`````{py:class} Load(api_util, ptr)
:canonical: altdss.Load.Load

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`

```{autodoc2-docstring} altdss.Load.Load
```

````{py:attribute} AllocationFactor
:canonical: altdss.Load.Load.AllocationFactor
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.AllocationFactor
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Load.Load.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Load.Load.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Bus1
```

````

````{py:attribute} CFactor
:canonical: altdss.Load.Load.CFactor
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.CFactor
```

````

````{py:attribute} CVRCurve
:canonical: altdss.Load.Load.CVRCurve
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.CVRCurve
```

````

````{py:attribute} CVRCurve_str
:canonical: altdss.Load.Load.CVRCurve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.CVRCurve_str
```

````

````{py:attribute} CVRVars
:canonical: altdss.Load.Load.CVRVars
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.CVRVars
```

````

````{py:attribute} CVRWatts
:canonical: altdss.Load.Load.CVRWatts
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.CVRWatts
```

````

````{py:attribute} Class
:canonical: altdss.Load.Load.Class
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Class
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Load.Load.Close

```{autodoc2-docstring} altdss.Load.Load.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Load.Load.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Load.Load.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Load.Load.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Load.Load.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Load.Load.Conn
:type: altdss.enums.Connection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Load.Load.Conn_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Load.Load.Currents

```{autodoc2-docstring} altdss.Load.Load.Currents
```

````

````{py:attribute} Daily
:canonical: altdss.Load.Load.Daily
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Load.Load.Daily_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Daily_str
```

````

````{py:attribute} DisplayName
:canonical: altdss.Load.Load.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.DisplayName
```

````

````{py:attribute} Duty
:canonical: altdss.Load.Load.Duty
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Load.Load.Duty_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Load.Load.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.Load.Load.EnergyMeter

```{autodoc2-docstring} altdss.Load.Load.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Load.Load.EnergyMeterName

```{autodoc2-docstring} altdss.Load.Load.EnergyMeterName
```

````

````{py:method} FullName() -> str
:canonical: altdss.Load.Load.FullName

```{autodoc2-docstring} altdss.Load.Load.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Load.Load.GUID

```{autodoc2-docstring} altdss.Load.Load.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.Load.Load.GetVariableValue

```{autodoc2-docstring} altdss.Load.Load.GetVariableValue
```

````

````{py:attribute} Growth
:canonical: altdss.Load.Load.Growth
:type: altdss.GrowthShape.GrowthShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Growth
```

````

````{py:attribute} Growth_str
:canonical: altdss.Load.Load.Growth_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Growth_str
```

````

````{py:method} Handle() -> int
:canonical: altdss.Load.Load.Handle

```{autodoc2-docstring} altdss.Load.Load.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Load.Load.HasOCPDevice

```{autodoc2-docstring} altdss.Load.Load.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Load.Load.HasSwitchControl

```{autodoc2-docstring} altdss.Load.Load.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Load.Load.HasVoltControl

```{autodoc2-docstring} altdss.Load.Load.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Load.Load.IsIsolated

```{autodoc2-docstring} altdss.Load.Load.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Load.Load.IsOpen

```{autodoc2-docstring} altdss.Load.Load.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Load.Load.Like

```{autodoc2-docstring} altdss.Load.Load.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Load.Load.Losses

```{autodoc2-docstring} altdss.Load.Load.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Load.Load.MaxCurrent

```{autodoc2-docstring} altdss.Load.Load.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Load.Load.Model
:type: altdss.enums.LoadModel
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Model
```

````

````{py:property} Name
:canonical: altdss.Load.Load.Name
:type: str

```{autodoc2-docstring} altdss.Load.Load.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Load.Load.NodeOrder

```{autodoc2-docstring} altdss.Load.Load.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Load.Load.NodeRef

```{autodoc2-docstring} altdss.Load.Load.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Load.Load.NumConductors

```{autodoc2-docstring} altdss.Load.Load.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Load.Load.NumControllers

```{autodoc2-docstring} altdss.Load.Load.NumControllers
```

````

````{py:attribute} NumCust
:canonical: altdss.Load.Load.NumCust
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.NumCust
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Load.Load.NumPhases

```{autodoc2-docstring} altdss.Load.Load.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Load.Load.NumTerminals

```{autodoc2-docstring} altdss.Load.Load.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Load.Load.OCPDevice

```{autodoc2-docstring} altdss.Load.Load.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Load.Load.OCPDeviceIndex

```{autodoc2-docstring} altdss.Load.Load.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Load.Load.OCPDeviceType

```{autodoc2-docstring} altdss.Load.Load.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Load.Load.Open

```{autodoc2-docstring} altdss.Load.Load.Open
```

````

````{py:attribute} PF
:canonical: altdss.Load.Load.PF
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.PF
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Load.Load.PhaseLosses

```{autodoc2-docstring} altdss.Load.Load.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Load.Load.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Load.Load.Powers

```{autodoc2-docstring} altdss.Load.Load.Powers
```

````

````{py:attribute} RNeut
:canonical: altdss.Load.Load.RNeut
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.RNeut
```

````

````{py:attribute} RelWeight
:canonical: altdss.Load.Load.RelWeight
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.RelWeight
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Load.Load.Residuals

```{autodoc2-docstring} altdss.Load.Load.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Load.Load.SeqCurrents

```{autodoc2-docstring} altdss.Load.Load.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Load.Load.SeqPowers

```{autodoc2-docstring} altdss.Load.Load.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Load.Load.SeqVoltages

```{autodoc2-docstring} altdss.Load.Load.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.Load.Load.SetVariableValue

```{autodoc2-docstring} altdss.Load.Load.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.Load.Load.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Load.Load.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Spectrum_str
```

````

````{py:attribute} Status
:canonical: altdss.Load.Load.Status
:type: altdss.enums.LoadStatus
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Status
```

````

````{py:attribute} Status_str
:canonical: altdss.Load.Load.Status_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Status_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Load.Load.TotalPowers

```{autodoc2-docstring} altdss.Load.Load.TotalPowers
```

````

````{py:attribute} VLowpu
:canonical: altdss.Load.Load.VLowpu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.VLowpu
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Load.Load.VMaxpu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.VMaxpu
```

````

````{py:attribute} VMinEmerg
:canonical: altdss.Load.Load.VMinEmerg
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.VMinEmerg
```

````

````{py:attribute} VMinNorm
:canonical: altdss.Load.Load.VMinNorm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.VMinNorm
```

````

````{py:attribute} VMinpu
:canonical: altdss.Load.Load.VMinpu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.VMinpu
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.Load.Load.VariableNames

```{autodoc2-docstring} altdss.Load.Load.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.Load.Load.VariableValues

```{autodoc2-docstring} altdss.Load.Load.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.Load.Load.VariablesDict

```{autodoc2-docstring} altdss.Load.Load.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Load.Load.Voltages

```{autodoc2-docstring} altdss.Load.Load.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Load.Load.VoltagesMagAng

```{autodoc2-docstring} altdss.Load.Load.VoltagesMagAng
```

````

````{py:attribute} XNeut
:canonical: altdss.Load.Load.XNeut
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.XNeut
```

````

````{py:attribute} XRHarm
:canonical: altdss.Load.Load.XRHarm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.XRHarm
```

````

````{py:attribute} XfkVA
:canonical: altdss.Load.Load.XfkVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.XfkVA
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Load.Load.YPrim

```{autodoc2-docstring} altdss.Load.Load.YPrim
```

````

````{py:attribute} Yearly
:canonical: altdss.Load.Load.Yearly
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Load.Load.Yearly_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.Yearly_str
```

````

````{py:attribute} ZIPV
:canonical: altdss.Load.Load.ZIPV
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.ZIPV
```

````

````{py:method} __hash__()
:canonical: altdss.Load.Load.__hash__

```{autodoc2-docstring} altdss.Load.Load.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Load.Load.__init__

```{autodoc2-docstring} altdss.Load.Load.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Load.Load.__ne__

```{autodoc2-docstring} altdss.Load.Load.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Load.Load.__repr__

```{autodoc2-docstring} altdss.Load.Load.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Load.Load.begin_edit

```{autodoc2-docstring} altdss.Load.Load.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Load.LoadProperties]) -> altdss.Load.Load
:canonical: altdss.Load.Load.edit

```{autodoc2-docstring} altdss.Load.Load.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Load.Load.end_edit

```{autodoc2-docstring} altdss.Load.Load.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Load.Load.kV
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Load.Load.kVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Load.Load.kW
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.kW
```

````

````{py:attribute} kWh
:canonical: altdss.Load.Load.kWh
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.kWh
```

````

````{py:attribute} kWhDays
:canonical: altdss.Load.Load.kWhDays
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.kWhDays
```

````

````{py:attribute} kvar
:canonical: altdss.Load.Load.kvar
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.kvar
```

````

````{py:attribute} pctMean
:canonical: altdss.Load.Load.pctMean
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.pctMean
```

````

````{py:attribute} pctSeriesRL
:canonical: altdss.Load.Load.pctSeriesRL
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.pctSeriesRL
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Load.Load.pctStdDev
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.pctStdDev
```

````

````{py:attribute} puXHarm
:canonical: altdss.Load.Load.puXHarm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.Load.puXHarm
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Load.Load.to_json

```{autodoc2-docstring} altdss.Load.Load.to_json
```

````

`````

`````{py:class} LoadBatch(api_util, **kwargs)
:canonical: altdss.Load.LoadBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.Load.LoadBatch
```

````{py:attribute} AllocationFactor
:canonical: altdss.Load.LoadBatch.AllocationFactor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.AllocationFactor
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Load.LoadBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Load.LoadBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Bus1
```

````

````{py:attribute} CFactor
:canonical: altdss.Load.LoadBatch.CFactor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.CFactor
```

````

````{py:attribute} CVRCurve
:canonical: altdss.Load.LoadBatch.CVRCurve
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.CVRCurve
```

````

````{py:attribute} CVRCurve_str
:canonical: altdss.Load.LoadBatch.CVRCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.CVRCurve_str
```

````

````{py:attribute} CVRVars
:canonical: altdss.Load.LoadBatch.CVRVars
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.CVRVars
```

````

````{py:attribute} CVRWatts
:canonical: altdss.Load.LoadBatch.CVRWatts
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.CVRWatts
```

````

````{py:attribute} Class
:canonical: altdss.Load.LoadBatch.Class
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Class
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Load.LoadBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Load.LoadBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Load.LoadBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Load.LoadBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Load.LoadBatch.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Load.LoadBatch.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Load.LoadBatch.Currents

```{autodoc2-docstring} altdss.Load.LoadBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Load.LoadBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Load.LoadBatch.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.Load.LoadBatch.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Load.LoadBatch.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Daily_str
```

````

````{py:attribute} Duty
:canonical: altdss.Load.LoadBatch.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Load.LoadBatch.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Duty_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Load.LoadBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Load.LoadBatch.EnergyMeter

```{autodoc2-docstring} altdss.Load.LoadBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Load.LoadBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Load.LoadBatch.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Load.LoadBatch.FullName

```{autodoc2-docstring} altdss.Load.LoadBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Load.LoadBatch.GUID

```{autodoc2-docstring} altdss.Load.LoadBatch.GUID
```

````

````{py:attribute} Growth
:canonical: altdss.Load.LoadBatch.Growth
:type: typing.List[altdss.GrowthShape.GrowthShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Growth
```

````

````{py:attribute} Growth_str
:canonical: altdss.Load.LoadBatch.Growth_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Growth_str
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Load.LoadBatch.Handle

```{autodoc2-docstring} altdss.Load.LoadBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Load.LoadBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Load.LoadBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Load.LoadBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Load.LoadBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Load.LoadBatch.HasVoltControl

```{autodoc2-docstring} altdss.Load.LoadBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Load.LoadBatch.IsIsolated

```{autodoc2-docstring} altdss.Load.LoadBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Load.LoadBatch.Like

```{autodoc2-docstring} altdss.Load.LoadBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Load.LoadBatch.Losses

```{autodoc2-docstring} altdss.Load.LoadBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Load.LoadBatch.MaxCurrent

```{autodoc2-docstring} altdss.Load.LoadBatch.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Load.LoadBatch.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Model
```

````

````{py:property} Name
:canonical: altdss.Load.LoadBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Load.LoadBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Load.LoadBatch.NumConductors

```{autodoc2-docstring} altdss.Load.LoadBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Load.LoadBatch.NumControllers

```{autodoc2-docstring} altdss.Load.LoadBatch.NumControllers
```

````

````{py:attribute} NumCust
:canonical: altdss.Load.LoadBatch.NumCust
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.NumCust
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Load.LoadBatch.NumPhases

```{autodoc2-docstring} altdss.Load.LoadBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Load.LoadBatch.NumTerminals

```{autodoc2-docstring} altdss.Load.LoadBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Load.LoadBatch.OCPDevice

```{autodoc2-docstring} altdss.Load.LoadBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Load.LoadBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Load.LoadBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Load.LoadBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Load.LoadBatch.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.Load.LoadBatch.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.PF
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Load.LoadBatch.PhaseLosses

```{autodoc2-docstring} altdss.Load.LoadBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Load.LoadBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Load.LoadBatch.Powers

```{autodoc2-docstring} altdss.Load.LoadBatch.Powers
```

````

````{py:attribute} RNeut
:canonical: altdss.Load.LoadBatch.RNeut
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.RNeut
```

````

````{py:attribute} RelWeight
:canonical: altdss.Load.LoadBatch.RelWeight
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.RelWeight
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Load.LoadBatch.SeqCurrents

```{autodoc2-docstring} altdss.Load.LoadBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Load.LoadBatch.SeqPowers

```{autodoc2-docstring} altdss.Load.LoadBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Load.LoadBatch.SeqVoltages

```{autodoc2-docstring} altdss.Load.LoadBatch.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.Load.LoadBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Load.LoadBatch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Spectrum_str
```

````

````{py:attribute} Status
:canonical: altdss.Load.LoadBatch.Status
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Status
```

````

````{py:attribute} Status_str
:canonical: altdss.Load.LoadBatch.Status_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Status_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Load.LoadBatch.TotalPowers

```{autodoc2-docstring} altdss.Load.LoadBatch.TotalPowers
```

````

````{py:attribute} VLowpu
:canonical: altdss.Load.LoadBatch.VLowpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.VLowpu
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Load.LoadBatch.VMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.VMaxpu
```

````

````{py:attribute} VMinEmerg
:canonical: altdss.Load.LoadBatch.VMinEmerg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.VMinEmerg
```

````

````{py:attribute} VMinNorm
:canonical: altdss.Load.LoadBatch.VMinNorm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.VMinNorm
```

````

````{py:attribute} VMinpu
:canonical: altdss.Load.LoadBatch.VMinpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.VMinpu
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Load.LoadBatch.Voltages

```{autodoc2-docstring} altdss.Load.LoadBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Load.LoadBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Load.LoadBatch.VoltagesMagAng
```

````

````{py:attribute} XNeut
:canonical: altdss.Load.LoadBatch.XNeut
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.XNeut
```

````

````{py:attribute} XRHarm
:canonical: altdss.Load.LoadBatch.XRHarm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.XRHarm
```

````

````{py:attribute} XfkVA
:canonical: altdss.Load.LoadBatch.XfkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.XfkVA
```

````

````{py:attribute} Yearly
:canonical: altdss.Load.LoadBatch.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Load.LoadBatch.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.Yearly_str
```

````

````{py:attribute} ZIPV
:canonical: altdss.Load.LoadBatch.ZIPV
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.ZIPV
```

````

````{py:method} __call__()
:canonical: altdss.Load.LoadBatch.__call__

```{autodoc2-docstring} altdss.Load.LoadBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Load.LoadBatch.__getitem__

```{autodoc2-docstring} altdss.Load.LoadBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Load.LoadBatch.__init__

```{autodoc2-docstring} altdss.Load.LoadBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Load.LoadBatch.__iter__

```{autodoc2-docstring} altdss.Load.LoadBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Load.LoadBatch.__len__

```{autodoc2-docstring} altdss.Load.LoadBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Load.LoadBatch.batch

```{autodoc2-docstring} altdss.Load.LoadBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Load.LoadBatch.begin_edit

```{autodoc2-docstring} altdss.Load.LoadBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Load.LoadBatchProperties]) -> altdss.Load.LoadBatch
:canonical: altdss.Load.LoadBatch.edit

```{autodoc2-docstring} altdss.Load.LoadBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Load.LoadBatch.end_edit

```{autodoc2-docstring} altdss.Load.LoadBatch.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Load.LoadBatch.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Load.LoadBatch.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Load.LoadBatch.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.kW
```

````

````{py:attribute} kWh
:canonical: altdss.Load.LoadBatch.kWh
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.kWh
```

````

````{py:attribute} kWhDays
:canonical: altdss.Load.LoadBatch.kWhDays
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.kWhDays
```

````

````{py:attribute} kvar
:canonical: altdss.Load.LoadBatch.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.kvar
```

````

````{py:attribute} pctMean
:canonical: altdss.Load.LoadBatch.pctMean
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.pctMean
```

````

````{py:attribute} pctSeriesRL
:canonical: altdss.Load.LoadBatch.pctSeriesRL
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.pctSeriesRL
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Load.LoadBatch.pctStdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.pctStdDev
```

````

````{py:attribute} puXHarm
:canonical: altdss.Load.LoadBatch.puXHarm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Load.LoadBatch.puXHarm
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Load.LoadBatch.to_json

```{autodoc2-docstring} altdss.Load.LoadBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Load.LoadBatch.to_list

```{autodoc2-docstring} altdss.Load.LoadBatch.to_list
```

````

`````

`````{py:class} LoadBatchProperties()
:canonical: altdss.Load.LoadBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Load.LoadBatchProperties
```

````{py:attribute} AllocationFactor
:canonical: altdss.Load.LoadBatchProperties.AllocationFactor
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.AllocationFactor
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Load.LoadBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Load.LoadBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Bus1
```

````

````{py:attribute} CFactor
:canonical: altdss.Load.LoadBatchProperties.CFactor
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.CFactor
```

````

````{py:attribute} CVRCurve
:canonical: altdss.Load.LoadBatchProperties.CVRCurve
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.CVRCurve
```

````

````{py:attribute} CVRVars
:canonical: altdss.Load.LoadBatchProperties.CVRVars
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.CVRVars
```

````

````{py:attribute} CVRWatts
:canonical: altdss.Load.LoadBatchProperties.CVRWatts
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.CVRWatts
```

````

````{py:attribute} Class
:canonical: altdss.Load.LoadBatchProperties.Class
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Class
```

````

````{py:attribute} Conn
:canonical: altdss.Load.LoadBatchProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.Connection], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Conn
```

````

````{py:attribute} Daily
:canonical: altdss.Load.LoadBatchProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Daily
```

````

````{py:attribute} Duty
:canonical: altdss.Load.LoadBatchProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Duty
```

````

````{py:attribute} Enabled
:canonical: altdss.Load.LoadBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Enabled
```

````

````{py:attribute} Growth
:canonical: altdss.Load.LoadBatchProperties.Growth
:type: typing.Union[typing.AnyStr, altdss.GrowthShape.GrowthShape, typing.List[typing.AnyStr], typing.List[altdss.GrowthShape.GrowthShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Growth
```

````

````{py:attribute} Like
:canonical: altdss.Load.LoadBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Like
```

````

````{py:attribute} Model
:canonical: altdss.Load.LoadBatchProperties.Model
:type: typing.Union[int, altdss.enums.LoadModel, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Model
```

````

````{py:attribute} NumCust
:canonical: altdss.Load.LoadBatchProperties.NumCust
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.NumCust
```

````

````{py:attribute} PF
:canonical: altdss.Load.LoadBatchProperties.PF
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.PF
```

````

````{py:attribute} Phases
:canonical: altdss.Load.LoadBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Phases
```

````

````{py:attribute} RNeut
:canonical: altdss.Load.LoadBatchProperties.RNeut
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.RNeut
```

````

````{py:attribute} RelWeight
:canonical: altdss.Load.LoadBatchProperties.RelWeight
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.RelWeight
```

````

````{py:attribute} Spectrum
:canonical: altdss.Load.LoadBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Spectrum
```

````

````{py:attribute} Status
:canonical: altdss.Load.LoadBatchProperties.Status
:type: typing.Union[typing.AnyStr, int, altdss.enums.LoadStatus, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LoadStatus], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Status
```

````

````{py:attribute} VLowpu
:canonical: altdss.Load.LoadBatchProperties.VLowpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.VLowpu
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Load.LoadBatchProperties.VMaxpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.VMaxpu
```

````

````{py:attribute} VMinEmerg
:canonical: altdss.Load.LoadBatchProperties.VMinEmerg
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.VMinEmerg
```

````

````{py:attribute} VMinNorm
:canonical: altdss.Load.LoadBatchProperties.VMinNorm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.VMinNorm
```

````

````{py:attribute} VMinpu
:canonical: altdss.Load.LoadBatchProperties.VMinpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.VMinpu
```

````

````{py:attribute} XNeut
:canonical: altdss.Load.LoadBatchProperties.XNeut
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.XNeut
```

````

````{py:attribute} XRHarm
:canonical: altdss.Load.LoadBatchProperties.XRHarm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.XRHarm
```

````

````{py:attribute} XfkVA
:canonical: altdss.Load.LoadBatchProperties.XfkVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.XfkVA
```

````

````{py:attribute} Yearly
:canonical: altdss.Load.LoadBatchProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.Yearly
```

````

````{py:attribute} ZIPV
:canonical: altdss.Load.LoadBatchProperties.ZIPV
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.ZIPV
```

````

````{py:method} __contains__()
:canonical: altdss.Load.LoadBatchProperties.__contains__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Load.LoadBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Load.LoadBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Load.LoadBatchProperties.__dir__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Load.LoadBatchProperties.__format__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Load.LoadBatchProperties.__ge__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Load.LoadBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Load.LoadBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Load.LoadBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Load.LoadBatchProperties.__gt__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Load.LoadBatchProperties.__init__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Load.LoadBatchProperties.__ior__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Load.LoadBatchProperties.__iter__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Load.LoadBatchProperties.__le__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Load.LoadBatchProperties.__len__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Load.LoadBatchProperties.__lt__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Load.LoadBatchProperties.__ne__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Load.LoadBatchProperties.__new__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Load.LoadBatchProperties.__or__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Load.LoadBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Load.LoadBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Load.LoadBatchProperties.__repr__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Load.LoadBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Load.LoadBatchProperties.__ror__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Load.LoadBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Load.LoadBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Load.LoadBatchProperties.__str__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Load.LoadBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Load.LoadBatchProperties.clear

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Load.LoadBatchProperties.copy

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Load.LoadBatchProperties.get

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Load.LoadBatchProperties.items

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Load.LoadBatchProperties.kV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Load.LoadBatchProperties.kVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Load.LoadBatchProperties.kW
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.kW
```

````

````{py:attribute} kWh
:canonical: altdss.Load.LoadBatchProperties.kWh
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.kWh
```

````

````{py:attribute} kWhDays
:canonical: altdss.Load.LoadBatchProperties.kWhDays
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.kWhDays
```

````

````{py:method} keys()
:canonical: altdss.Load.LoadBatchProperties.keys

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Load.LoadBatchProperties.kvar
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.kvar
```

````

````{py:attribute} pctMean
:canonical: altdss.Load.LoadBatchProperties.pctMean
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.pctMean
```

````

````{py:attribute} pctSeriesRL
:canonical: altdss.Load.LoadBatchProperties.pctSeriesRL
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.pctSeriesRL
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Load.LoadBatchProperties.pctStdDev
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.pctStdDev
```

````

````{py:method} pop()
:canonical: altdss.Load.LoadBatchProperties.pop

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Load.LoadBatchProperties.popitem

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.popitem
```

````

````{py:attribute} puXHarm
:canonical: altdss.Load.LoadBatchProperties.puXHarm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.puXHarm
```

````

````{py:method} setdefault()
:canonical: altdss.Load.LoadBatchProperties.setdefault

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Load.LoadBatchProperties.update

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Load.LoadBatchProperties.values

```{autodoc2-docstring} altdss.Load.LoadBatchProperties.values
```

````

`````

`````{py:class} LoadProperties()
:canonical: altdss.Load.LoadProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Load.LoadProperties
```

````{py:attribute} AllocationFactor
:canonical: altdss.Load.LoadProperties.AllocationFactor
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.AllocationFactor
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Load.LoadProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Load.LoadProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Bus1
```

````

````{py:attribute} CFactor
:canonical: altdss.Load.LoadProperties.CFactor
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.CFactor
```

````

````{py:attribute} CVRCurve
:canonical: altdss.Load.LoadProperties.CVRCurve
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.CVRCurve
```

````

````{py:attribute} CVRVars
:canonical: altdss.Load.LoadProperties.CVRVars
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.CVRVars
```

````

````{py:attribute} CVRWatts
:canonical: altdss.Load.LoadProperties.CVRWatts
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.CVRWatts
```

````

````{py:attribute} Class
:canonical: altdss.Load.LoadProperties.Class
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Class
```

````

````{py:attribute} Conn
:canonical: altdss.Load.LoadProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Conn
```

````

````{py:attribute} Daily
:canonical: altdss.Load.LoadProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Daily
```

````

````{py:attribute} Duty
:canonical: altdss.Load.LoadProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Duty
```

````

````{py:attribute} Enabled
:canonical: altdss.Load.LoadProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Enabled
```

````

````{py:attribute} Growth
:canonical: altdss.Load.LoadProperties.Growth
:type: typing.Union[typing.AnyStr, altdss.GrowthShape.GrowthShape]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Growth
```

````

````{py:attribute} Like
:canonical: altdss.Load.LoadProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Like
```

````

````{py:attribute} Model
:canonical: altdss.Load.LoadProperties.Model
:type: typing.Union[int, altdss.enums.LoadModel]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Model
```

````

````{py:attribute} NumCust
:canonical: altdss.Load.LoadProperties.NumCust
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.NumCust
```

````

````{py:attribute} PF
:canonical: altdss.Load.LoadProperties.PF
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.PF
```

````

````{py:attribute} Phases
:canonical: altdss.Load.LoadProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Phases
```

````

````{py:attribute} RNeut
:canonical: altdss.Load.LoadProperties.RNeut
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.RNeut
```

````

````{py:attribute} RelWeight
:canonical: altdss.Load.LoadProperties.RelWeight
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.RelWeight
```

````

````{py:attribute} Spectrum
:canonical: altdss.Load.LoadProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Spectrum
```

````

````{py:attribute} Status
:canonical: altdss.Load.LoadProperties.Status
:type: typing.Union[typing.AnyStr, int, altdss.enums.LoadStatus]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Status
```

````

````{py:attribute} VLowpu
:canonical: altdss.Load.LoadProperties.VLowpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.VLowpu
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Load.LoadProperties.VMaxpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.VMaxpu
```

````

````{py:attribute} VMinEmerg
:canonical: altdss.Load.LoadProperties.VMinEmerg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.VMinEmerg
```

````

````{py:attribute} VMinNorm
:canonical: altdss.Load.LoadProperties.VMinNorm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.VMinNorm
```

````

````{py:attribute} VMinpu
:canonical: altdss.Load.LoadProperties.VMinpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.VMinpu
```

````

````{py:attribute} XNeut
:canonical: altdss.Load.LoadProperties.XNeut
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.XNeut
```

````

````{py:attribute} XRHarm
:canonical: altdss.Load.LoadProperties.XRHarm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.XRHarm
```

````

````{py:attribute} XfkVA
:canonical: altdss.Load.LoadProperties.XfkVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.XfkVA
```

````

````{py:attribute} Yearly
:canonical: altdss.Load.LoadProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.Yearly
```

````

````{py:attribute} ZIPV
:canonical: altdss.Load.LoadProperties.ZIPV
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.ZIPV
```

````

````{py:method} __contains__()
:canonical: altdss.Load.LoadProperties.__contains__

```{autodoc2-docstring} altdss.Load.LoadProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Load.LoadProperties.__delattr__

```{autodoc2-docstring} altdss.Load.LoadProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Load.LoadProperties.__delitem__

```{autodoc2-docstring} altdss.Load.LoadProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Load.LoadProperties.__dir__

```{autodoc2-docstring} altdss.Load.LoadProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Load.LoadProperties.__format__

```{autodoc2-docstring} altdss.Load.LoadProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Load.LoadProperties.__ge__

```{autodoc2-docstring} altdss.Load.LoadProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Load.LoadProperties.__getattribute__

```{autodoc2-docstring} altdss.Load.LoadProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Load.LoadProperties.__getitem__

```{autodoc2-docstring} altdss.Load.LoadProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Load.LoadProperties.__getstate__

```{autodoc2-docstring} altdss.Load.LoadProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Load.LoadProperties.__gt__

```{autodoc2-docstring} altdss.Load.LoadProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Load.LoadProperties.__init__

```{autodoc2-docstring} altdss.Load.LoadProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Load.LoadProperties.__ior__

```{autodoc2-docstring} altdss.Load.LoadProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Load.LoadProperties.__iter__

```{autodoc2-docstring} altdss.Load.LoadProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Load.LoadProperties.__le__

```{autodoc2-docstring} altdss.Load.LoadProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Load.LoadProperties.__len__

```{autodoc2-docstring} altdss.Load.LoadProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Load.LoadProperties.__lt__

```{autodoc2-docstring} altdss.Load.LoadProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Load.LoadProperties.__ne__

```{autodoc2-docstring} altdss.Load.LoadProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Load.LoadProperties.__new__

```{autodoc2-docstring} altdss.Load.LoadProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Load.LoadProperties.__or__

```{autodoc2-docstring} altdss.Load.LoadProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Load.LoadProperties.__reduce__

```{autodoc2-docstring} altdss.Load.LoadProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Load.LoadProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Load.LoadProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Load.LoadProperties.__repr__

```{autodoc2-docstring} altdss.Load.LoadProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Load.LoadProperties.__reversed__

```{autodoc2-docstring} altdss.Load.LoadProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Load.LoadProperties.__ror__

```{autodoc2-docstring} altdss.Load.LoadProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Load.LoadProperties.__setitem__

```{autodoc2-docstring} altdss.Load.LoadProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Load.LoadProperties.__sizeof__

```{autodoc2-docstring} altdss.Load.LoadProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Load.LoadProperties.__str__

```{autodoc2-docstring} altdss.Load.LoadProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Load.LoadProperties.__subclasshook__

```{autodoc2-docstring} altdss.Load.LoadProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Load.LoadProperties.clear

```{autodoc2-docstring} altdss.Load.LoadProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Load.LoadProperties.copy

```{autodoc2-docstring} altdss.Load.LoadProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Load.LoadProperties.get

```{autodoc2-docstring} altdss.Load.LoadProperties.get
```

````

````{py:method} items()
:canonical: altdss.Load.LoadProperties.items

```{autodoc2-docstring} altdss.Load.LoadProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Load.LoadProperties.kV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Load.LoadProperties.kVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.kVA
```

````

````{py:attribute} kW
:canonical: altdss.Load.LoadProperties.kW
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.kW
```

````

````{py:attribute} kWh
:canonical: altdss.Load.LoadProperties.kWh
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.kWh
```

````

````{py:attribute} kWhDays
:canonical: altdss.Load.LoadProperties.kWhDays
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.kWhDays
```

````

````{py:method} keys()
:canonical: altdss.Load.LoadProperties.keys

```{autodoc2-docstring} altdss.Load.LoadProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Load.LoadProperties.kvar
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.kvar
```

````

````{py:attribute} pctMean
:canonical: altdss.Load.LoadProperties.pctMean
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.pctMean
```

````

````{py:attribute} pctSeriesRL
:canonical: altdss.Load.LoadProperties.pctSeriesRL
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.pctSeriesRL
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Load.LoadProperties.pctStdDev
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.pctStdDev
```

````

````{py:method} pop()
:canonical: altdss.Load.LoadProperties.pop

```{autodoc2-docstring} altdss.Load.LoadProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Load.LoadProperties.popitem

```{autodoc2-docstring} altdss.Load.LoadProperties.popitem
```

````

````{py:attribute} puXHarm
:canonical: altdss.Load.LoadProperties.puXHarm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Load.LoadProperties.puXHarm
```

````

````{py:method} setdefault()
:canonical: altdss.Load.LoadProperties.setdefault

```{autodoc2-docstring} altdss.Load.LoadProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Load.LoadProperties.update

```{autodoc2-docstring} altdss.Load.LoadProperties.update
```

````

````{py:method} values()
:canonical: altdss.Load.LoadProperties.values

```{autodoc2-docstring} altdss.Load.LoadProperties.values
```

````

`````
