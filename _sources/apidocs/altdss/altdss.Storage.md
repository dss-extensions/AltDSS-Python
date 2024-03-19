# {py:mod}`altdss.Storage`

```{py:module} altdss.Storage
```

```{autodoc2-docstring} altdss.Storage
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IStorage <altdss.Storage.IStorage>`
  - ```{autodoc2-docstring} altdss.Storage.IStorage
    :summary:
    ```
* - {py:obj}`Storage <altdss.Storage.Storage>`
  - ```{autodoc2-docstring} altdss.Storage.Storage
    :summary:
    ```
* - {py:obj}`StorageBatch <altdss.Storage.StorageBatch>`
  - ```{autodoc2-docstring} altdss.Storage.StorageBatch
    :summary:
    ```
* - {py:obj}`StorageBatchProperties <altdss.Storage.StorageBatchProperties>`
  - ```{autodoc2-docstring} altdss.Storage.StorageBatchProperties
    :summary:
    ```
* - {py:obj}`StorageProperties <altdss.Storage.StorageProperties>`
  - ```{autodoc2-docstring} altdss.Storage.StorageProperties
    :summary:
    ```
````

### API

`````{py:class} IStorage(iobj)
:canonical: altdss.Storage.IStorage

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Storage.StorageBatch`

```{autodoc2-docstring} altdss.Storage.IStorage
```

````{py:attribute} AmpLimit
:canonical: altdss.Storage.IStorage.AmpLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.Storage.IStorage.AmpLimitGain
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.Storage.IStorage.Balanced
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Storage.IStorage.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Storage.IStorage.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Bus1
```

````

````{py:attribute} ChargeTrigger
:canonical: altdss.Storage.IStorage.ChargeTrigger
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.ChargeTrigger
```

````

````{py:attribute} Class
:canonical: altdss.Storage.IStorage.Class
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Class
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Storage.IStorage.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Storage.IStorage.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Storage.IStorage.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Storage.IStorage.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Storage.IStorage.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Storage.IStorage.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Conn_str
```

````

````{py:attribute} ControlMode
:canonical: altdss.Storage.IStorage.ControlMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.ControlMode
```

````

````{py:attribute} ControlMode_str
:canonical: altdss.Storage.IStorage.ControlMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.ControlMode_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Storage.IStorage.Currents

```{autodoc2-docstring} altdss.Storage.IStorage.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Storage.IStorage.CurrentsMagAng

```{autodoc2-docstring} altdss.Storage.IStorage.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.Storage.IStorage.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Storage.IStorage.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Storage.IStorage.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.DebugTrace
```

````

````{py:attribute} DischargeTrigger
:canonical: altdss.Storage.IStorage.DischargeTrigger
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.DischargeTrigger
```

````

````{py:attribute} DispMode
:canonical: altdss.Storage.IStorage.DispMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.DispMode
```

````

````{py:attribute} DispMode_str
:canonical: altdss.Storage.IStorage.DispMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.DispMode_str
```

````

````{py:attribute} Duty
:canonical: altdss.Storage.IStorage.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Storage.IStorage.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Duty_str
```

````

````{py:attribute} DynOut
:canonical: altdss.Storage.IStorage.DynOut
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.DynOut
```

````

````{py:attribute} DynaDLL
:canonical: altdss.Storage.IStorage.DynaDLL
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.DynaDLL
```

````

````{py:attribute} DynaData
:canonical: altdss.Storage.IStorage.DynaData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.DynaData
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Storage.IStorage.DynamicEq
:type: typing.List[altdss.DynamicExp.DynamicExp]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.DynamicEq
```

````

````{py:attribute} DynamicEq_str
:canonical: altdss.Storage.IStorage.DynamicEq_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.DynamicEq_str
```

````

````{py:attribute} EffCurve
:canonical: altdss.Storage.IStorage.EffCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.EffCurve
```

````

````{py:attribute} EffCurve_str
:canonical: altdss.Storage.IStorage.EffCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.EffCurve_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Storage.IStorage.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Storage.IStorage.EnergyMeter

```{autodoc2-docstring} altdss.Storage.IStorage.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Storage.IStorage.EnergyMeterName

```{autodoc2-docstring} altdss.Storage.IStorage.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Storage.IStorage.FullName

```{autodoc2-docstring} altdss.Storage.IStorage.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Storage.IStorage.GUID

```{autodoc2-docstring} altdss.Storage.IStorage.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Storage.IStorage.Handle

```{autodoc2-docstring} altdss.Storage.IStorage.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Storage.IStorage.HasOCPDevice

```{autodoc2-docstring} altdss.Storage.IStorage.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Storage.IStorage.HasSwitchControl

```{autodoc2-docstring} altdss.Storage.IStorage.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Storage.IStorage.HasVoltControl

```{autodoc2-docstring} altdss.Storage.IStorage.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Storage.IStorage.IsIsolated

```{autodoc2-docstring} altdss.Storage.IStorage.IsIsolated
```

````

````{py:attribute} Kp
:canonical: altdss.Storage.IStorage.Kp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Kp
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Storage.IStorage.Like

```{autodoc2-docstring} altdss.Storage.IStorage.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.Storage.IStorage.LimitCurrent
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.LimitCurrent
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Storage.IStorage.Losses

```{autodoc2-docstring} altdss.Storage.IStorage.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Storage.IStorage.MaxCurrent

```{autodoc2-docstring} altdss.Storage.IStorage.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Storage.IStorage.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Model
```

````

````{py:property} Name
:canonical: altdss.Storage.IStorage.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Storage.IStorage.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Storage.IStorage.NumConductors

```{autodoc2-docstring} altdss.Storage.IStorage.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Storage.IStorage.NumControllers

```{autodoc2-docstring} altdss.Storage.IStorage.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Storage.IStorage.NumPhases

```{autodoc2-docstring} altdss.Storage.IStorage.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Storage.IStorage.NumTerminals

```{autodoc2-docstring} altdss.Storage.IStorage.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Storage.IStorage.OCPDevice

```{autodoc2-docstring} altdss.Storage.IStorage.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Storage.IStorage.OCPDeviceIndex

```{autodoc2-docstring} altdss.Storage.IStorage.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Storage.IStorage.OCPDeviceType

```{autodoc2-docstring} altdss.Storage.IStorage.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.Storage.IStorage.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.Storage.IStorage.PFPriority
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.Storage.IStorage.PITol
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.PITol
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Storage.IStorage.PhaseLosses

```{autodoc2-docstring} altdss.Storage.IStorage.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Storage.IStorage.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Storage.IStorage.Powers

```{autodoc2-docstring} altdss.Storage.IStorage.Powers
```

````

````{py:attribute} SafeMode
:canonical: altdss.Storage.IStorage.SafeMode
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.Storage.IStorage.SafeVoltage
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.SafeVoltage
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Storage.IStorage.SeqCurrents

```{autodoc2-docstring} altdss.Storage.IStorage.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Storage.IStorage.SeqPowers

```{autodoc2-docstring} altdss.Storage.IStorage.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Storage.IStorage.SeqVoltages

```{autodoc2-docstring} altdss.Storage.IStorage.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.Storage.IStorage.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Storage.IStorage.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Spectrum_str
```

````

````{py:attribute} State
:canonical: altdss.Storage.IStorage.State
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.State
```

````

````{py:attribute} State_str
:canonical: altdss.Storage.IStorage.State_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.State_str
```

````

````{py:attribute} TimeChargeTrig
:canonical: altdss.Storage.IStorage.TimeChargeTrig
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.TimeChargeTrig
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Storage.IStorage.TotalPowers

```{autodoc2-docstring} altdss.Storage.IStorage.TotalPowers
```

````

````{py:attribute} UserData
:canonical: altdss.Storage.IStorage.UserData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Storage.IStorage.UserModel
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Storage.IStorage.VMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Storage.IStorage.VMinpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.Storage.IStorage.VarFollowInverter
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.VarFollowInverter
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Storage.IStorage.Voltages

```{autodoc2-docstring} altdss.Storage.IStorage.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Storage.IStorage.VoltagesMagAng

```{autodoc2-docstring} altdss.Storage.IStorage.VoltagesMagAng
```

````

````{py:attribute} WattPriority
:canonical: altdss.Storage.IStorage.WattPriority
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.WattPriority
```

````

````{py:attribute} Yearly
:canonical: altdss.Storage.IStorage.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Storage.IStorage.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.Storage.IStorage.__call__

```{autodoc2-docstring} altdss.Storage.IStorage.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Storage.IStorage.__contains__

```{autodoc2-docstring} altdss.Storage.IStorage.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Storage.IStorage.__getitem__

```{autodoc2-docstring} altdss.Storage.IStorage.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Storage.IStorage.__init__

```{autodoc2-docstring} altdss.Storage.IStorage.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Storage.IStorage.__iter__

```{autodoc2-docstring} altdss.Storage.IStorage.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Storage.IStorage.__len__

```{autodoc2-docstring} altdss.Storage.IStorage.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Storage.IStorage.batch

```{autodoc2-docstring} altdss.Storage.IStorage.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.Storage.StorageBatchProperties]) -> altdss.Storage.StorageBatch
:canonical: altdss.Storage.IStorage.batch_new

```{autodoc2-docstring} altdss.Storage.IStorage.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Storage.IStorage.begin_edit

```{autodoc2-docstring} altdss.Storage.IStorage.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Storage.StorageBatchProperties]) -> altdss.Storage.StorageBatch
:canonical: altdss.Storage.IStorage.edit

```{autodoc2-docstring} altdss.Storage.IStorage.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Storage.IStorage.end_edit

```{autodoc2-docstring} altdss.Storage.IStorage.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Storage.IStorage.find

```{autodoc2-docstring} altdss.Storage.IStorage.find
```

````

````{py:attribute} kV
:canonical: altdss.Storage.IStorage.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Storage.IStorage.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.Storage.IStorage.kVDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.Storage.IStorage.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kW
```

````

````{py:attribute} kWRated
:canonical: altdss.Storage.IStorage.kWRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kWRated
```

````

````{py:attribute} kWhRated
:canonical: altdss.Storage.IStorage.kWhRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kWhRated
```

````

````{py:attribute} kWhStored
:canonical: altdss.Storage.IStorage.kWhStored
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kWhStored
```

````

````{py:attribute} kvar
:canonical: altdss.Storage.IStorage.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.Storage.IStorage.kvarMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.Storage.IStorage.kvarMaxAbs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.kvarMaxAbs
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.Storage.StorageProperties]) -> altdss.Storage.Storage
:canonical: altdss.Storage.IStorage.new

```{autodoc2-docstring} altdss.Storage.IStorage.new
```

````

````{py:attribute} pctCharge
:canonical: altdss.Storage.IStorage.pctCharge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctCharge
```

````

````{py:attribute} pctCutIn
:canonical: altdss.Storage.IStorage.pctCutIn
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.Storage.IStorage.pctCutOut
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctCutOut
```

````

````{py:attribute} pctDischarge
:canonical: altdss.Storage.IStorage.pctDischarge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctDischarge
```

````

````{py:attribute} pctEffCharge
:canonical: altdss.Storage.IStorage.pctEffCharge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctEffCharge
```

````

````{py:attribute} pctEffDischarge
:canonical: altdss.Storage.IStorage.pctEffDischarge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctEffDischarge
```

````

````{py:attribute} pctIdlingkW
:canonical: altdss.Storage.IStorage.pctIdlingkW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctIdlingkW
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.Storage.IStorage.pctPMinNoVars
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.Storage.IStorage.pctPMinkvarMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctPMinkvarMax
```

````

````{py:attribute} pctR
:canonical: altdss.Storage.IStorage.pctR
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctR
```

````

````{py:attribute} pctReserve
:canonical: altdss.Storage.IStorage.pctReserve
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctReserve
```

````

````{py:attribute} pctStored
:canonical: altdss.Storage.IStorage.pctStored
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctStored
```

````

````{py:attribute} pctX
:canonical: altdss.Storage.IStorage.pctX
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctX
```

````

````{py:attribute} pctkWRated
:canonical: altdss.Storage.IStorage.pctkWRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.IStorage.pctkWRated
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Storage.IStorage.to_json

```{autodoc2-docstring} altdss.Storage.IStorage.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Storage.IStorage.to_list

```{autodoc2-docstring} altdss.Storage.IStorage.to_list
```

````

`````

`````{py:class} Storage(api_util, ptr)
:canonical: altdss.Storage.Storage

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`, {py:obj}`altdss.PCElement.ElementHasRegistersMixin`

```{autodoc2-docstring} altdss.Storage.Storage
```

````{py:attribute} AmpLimit
:canonical: altdss.Storage.Storage.AmpLimit
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.Storage.Storage.AmpLimitGain
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.Storage.Storage.Balanced
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Storage.Storage.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Storage.Storage.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Bus1
```

````

````{py:attribute} ChargeTrigger
:canonical: altdss.Storage.Storage.ChargeTrigger
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.ChargeTrigger
```

````

````{py:attribute} Class
:canonical: altdss.Storage.Storage.Class
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Class
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Storage.Storage.Close

```{autodoc2-docstring} altdss.Storage.Storage.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Storage.Storage.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Storage.Storage.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Storage.Storage.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Storage.Storage.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Storage.Storage.Conn
:type: altdss.enums.Connection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Storage.Storage.Conn_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Conn_str
```

````

````{py:attribute} ControlMode
:canonical: altdss.Storage.Storage.ControlMode
:type: altdss.enums.InverterControlMode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.ControlMode
```

````

````{py:attribute} ControlMode_str
:canonical: altdss.Storage.Storage.ControlMode_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.ControlMode_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Storage.Storage.Currents

```{autodoc2-docstring} altdss.Storage.Storage.Currents
```

````

````{py:attribute} Daily
:canonical: altdss.Storage.Storage.Daily
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Storage.Storage.Daily_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Storage.Storage.DebugTrace
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DebugTrace
```

````

````{py:attribute} DischargeTrigger
:canonical: altdss.Storage.Storage.DischargeTrigger
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DischargeTrigger
```

````

````{py:attribute} DispMode
:canonical: altdss.Storage.Storage.DispMode
:type: altdss.enums.StorageDispatchMode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DispMode
```

````

````{py:attribute} DispMode_str
:canonical: altdss.Storage.Storage.DispMode_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DispMode_str
```

````

````{py:attribute} DisplayName
:canonical: altdss.Storage.Storage.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DisplayName
```

````

````{py:attribute} Duty
:canonical: altdss.Storage.Storage.Duty
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Storage.Storage.Duty_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Duty_str
```

````

````{py:attribute} DynOut
:canonical: altdss.Storage.Storage.DynOut
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DynOut
```

````

````{py:attribute} DynaDLL
:canonical: altdss.Storage.Storage.DynaDLL
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DynaDLL
```

````

````{py:attribute} DynaData
:canonical: altdss.Storage.Storage.DynaData
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DynaData
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Storage.Storage.DynamicEq
:type: altdss.DynamicExp.DynamicExp
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DynamicEq
```

````

````{py:attribute} DynamicEq_str
:canonical: altdss.Storage.Storage.DynamicEq_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.DynamicEq_str
```

````

````{py:attribute} EffCurve
:canonical: altdss.Storage.Storage.EffCurve
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.EffCurve
```

````

````{py:attribute} EffCurve_str
:canonical: altdss.Storage.Storage.EffCurve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.EffCurve_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Storage.Storage.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.Storage.Storage.EnergyMeter

```{autodoc2-docstring} altdss.Storage.Storage.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Storage.Storage.EnergyMeterName

```{autodoc2-docstring} altdss.Storage.Storage.EnergyMeterName
```

````

````{py:method} FullName() -> str
:canonical: altdss.Storage.Storage.FullName

```{autodoc2-docstring} altdss.Storage.Storage.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Storage.Storage.GUID

```{autodoc2-docstring} altdss.Storage.Storage.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.Storage.Storage.GetVariableValue

```{autodoc2-docstring} altdss.Storage.Storage.GetVariableValue
```

````

````{py:method} Handle() -> int
:canonical: altdss.Storage.Storage.Handle

```{autodoc2-docstring} altdss.Storage.Storage.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Storage.Storage.HasOCPDevice

```{autodoc2-docstring} altdss.Storage.Storage.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Storage.Storage.HasSwitchControl

```{autodoc2-docstring} altdss.Storage.Storage.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Storage.Storage.HasVoltControl

```{autodoc2-docstring} altdss.Storage.Storage.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Storage.Storage.IsIsolated

```{autodoc2-docstring} altdss.Storage.Storage.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Storage.Storage.IsOpen

```{autodoc2-docstring} altdss.Storage.Storage.IsOpen
```

````

````{py:attribute} Kp
:canonical: altdss.Storage.Storage.Kp
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Kp
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Storage.Storage.Like

```{autodoc2-docstring} altdss.Storage.Storage.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.Storage.Storage.LimitCurrent
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.LimitCurrent
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Storage.Storage.Losses

```{autodoc2-docstring} altdss.Storage.Storage.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Storage.Storage.MaxCurrent

```{autodoc2-docstring} altdss.Storage.Storage.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Storage.Storage.Model
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Model
```

````

````{py:property} Name
:canonical: altdss.Storage.Storage.Name
:type: str

```{autodoc2-docstring} altdss.Storage.Storage.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Storage.Storage.NodeOrder

```{autodoc2-docstring} altdss.Storage.Storage.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Storage.Storage.NodeRef

```{autodoc2-docstring} altdss.Storage.Storage.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Storage.Storage.NumConductors

```{autodoc2-docstring} altdss.Storage.Storage.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Storage.Storage.NumControllers

```{autodoc2-docstring} altdss.Storage.Storage.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Storage.Storage.NumPhases

```{autodoc2-docstring} altdss.Storage.Storage.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Storage.Storage.NumTerminals

```{autodoc2-docstring} altdss.Storage.Storage.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Storage.Storage.OCPDevice

```{autodoc2-docstring} altdss.Storage.Storage.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Storage.Storage.OCPDeviceIndex

```{autodoc2-docstring} altdss.Storage.Storage.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Storage.Storage.OCPDeviceType

```{autodoc2-docstring} altdss.Storage.Storage.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Storage.Storage.Open

```{autodoc2-docstring} altdss.Storage.Storage.Open
```

````

````{py:attribute} PF
:canonical: altdss.Storage.Storage.PF
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.Storage.Storage.PFPriority
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.Storage.Storage.PITol
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.PITol
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Storage.Storage.PhaseLosses

```{autodoc2-docstring} altdss.Storage.Storage.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Storage.Storage.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Storage.Storage.Powers

```{autodoc2-docstring} altdss.Storage.Storage.Powers
```

````

````{py:method} RegisterNames() -> typing.List[str]
:canonical: altdss.Storage.Storage.RegisterNames

```{autodoc2-docstring} altdss.Storage.Storage.RegisterNames
```

````

````{py:method} RegisterValues() -> altdss.types.Float64Array
:canonical: altdss.Storage.Storage.RegisterValues

```{autodoc2-docstring} altdss.Storage.Storage.RegisterValues
```

````

````{py:method} RegistersDict() -> typing.Dict[str, float]
:canonical: altdss.Storage.Storage.RegistersDict

```{autodoc2-docstring} altdss.Storage.Storage.RegistersDict
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Storage.Storage.Residuals

```{autodoc2-docstring} altdss.Storage.Storage.Residuals
```

````

````{py:attribute} SafeMode
:canonical: altdss.Storage.Storage.SafeMode
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.Storage.Storage.SafeVoltage
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.SafeVoltage
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Storage.Storage.SeqCurrents

```{autodoc2-docstring} altdss.Storage.Storage.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Storage.Storage.SeqPowers

```{autodoc2-docstring} altdss.Storage.Storage.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Storage.Storage.SeqVoltages

```{autodoc2-docstring} altdss.Storage.Storage.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.Storage.Storage.SetVariableValue

```{autodoc2-docstring} altdss.Storage.Storage.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.Storage.Storage.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Storage.Storage.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Spectrum_str
```

````

````{py:attribute} State
:canonical: altdss.Storage.Storage.State
:type: altdss.enums.StorageState
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.State
```

````

````{py:attribute} State_str
:canonical: altdss.Storage.Storage.State_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.State_str
```

````

````{py:attribute} TimeChargeTrig
:canonical: altdss.Storage.Storage.TimeChargeTrig
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.TimeChargeTrig
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Storage.Storage.TotalPowers

```{autodoc2-docstring} altdss.Storage.Storage.TotalPowers
```

````

````{py:attribute} UserData
:canonical: altdss.Storage.Storage.UserData
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Storage.Storage.UserModel
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Storage.Storage.VMaxpu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Storage.Storage.VMinpu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.Storage.Storage.VarFollowInverter
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.VarFollowInverter
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.Storage.Storage.VariableNames

```{autodoc2-docstring} altdss.Storage.Storage.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.Storage.Storage.VariableValues

```{autodoc2-docstring} altdss.Storage.Storage.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.Storage.Storage.VariablesDict

```{autodoc2-docstring} altdss.Storage.Storage.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Storage.Storage.Voltages

```{autodoc2-docstring} altdss.Storage.Storage.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Storage.Storage.VoltagesMagAng

```{autodoc2-docstring} altdss.Storage.Storage.VoltagesMagAng
```

````

````{py:attribute} WattPriority
:canonical: altdss.Storage.Storage.WattPriority
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.WattPriority
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Storage.Storage.YPrim

```{autodoc2-docstring} altdss.Storage.Storage.YPrim
```

````

````{py:attribute} Yearly
:canonical: altdss.Storage.Storage.Yearly
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Storage.Storage.Yearly_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.Yearly_str
```

````

````{py:method} __hash__()
:canonical: altdss.Storage.Storage.__hash__

```{autodoc2-docstring} altdss.Storage.Storage.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Storage.Storage.__init__

```{autodoc2-docstring} altdss.Storage.Storage.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Storage.Storage.__ne__

```{autodoc2-docstring} altdss.Storage.Storage.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Storage.Storage.__repr__

```{autodoc2-docstring} altdss.Storage.Storage.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Storage.Storage.begin_edit

```{autodoc2-docstring} altdss.Storage.Storage.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Storage.StorageProperties]) -> altdss.Storage.Storage
:canonical: altdss.Storage.Storage.edit

```{autodoc2-docstring} altdss.Storage.Storage.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Storage.Storage.end_edit

```{autodoc2-docstring} altdss.Storage.Storage.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Storage.Storage.kV
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Storage.Storage.kVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.Storage.Storage.kVDC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.Storage.Storage.kW
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kW
```

````

````{py:attribute} kWRated
:canonical: altdss.Storage.Storage.kWRated
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kWRated
```

````

````{py:attribute} kWhRated
:canonical: altdss.Storage.Storage.kWhRated
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kWhRated
```

````

````{py:attribute} kWhStored
:canonical: altdss.Storage.Storage.kWhStored
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kWhStored
```

````

````{py:attribute} kvar
:canonical: altdss.Storage.Storage.kvar
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.Storage.Storage.kvarMax
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.Storage.Storage.kvarMaxAbs
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.kvarMaxAbs
```

````

````{py:attribute} pctCharge
:canonical: altdss.Storage.Storage.pctCharge
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctCharge
```

````

````{py:attribute} pctCutIn
:canonical: altdss.Storage.Storage.pctCutIn
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.Storage.Storage.pctCutOut
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctCutOut
```

````

````{py:attribute} pctDischarge
:canonical: altdss.Storage.Storage.pctDischarge
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctDischarge
```

````

````{py:attribute} pctEffCharge
:canonical: altdss.Storage.Storage.pctEffCharge
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctEffCharge
```

````

````{py:attribute} pctEffDischarge
:canonical: altdss.Storage.Storage.pctEffDischarge
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctEffDischarge
```

````

````{py:attribute} pctIdlingkW
:canonical: altdss.Storage.Storage.pctIdlingkW
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctIdlingkW
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.Storage.Storage.pctPMinNoVars
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.Storage.Storage.pctPMinkvarMax
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctPMinkvarMax
```

````

````{py:attribute} pctR
:canonical: altdss.Storage.Storage.pctR
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctR
```

````

````{py:attribute} pctReserve
:canonical: altdss.Storage.Storage.pctReserve
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctReserve
```

````

````{py:attribute} pctStored
:canonical: altdss.Storage.Storage.pctStored
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctStored
```

````

````{py:attribute} pctX
:canonical: altdss.Storage.Storage.pctX
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctX
```

````

````{py:attribute} pctkWRated
:canonical: altdss.Storage.Storage.pctkWRated
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.Storage.pctkWRated
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Storage.Storage.to_json

```{autodoc2-docstring} altdss.Storage.Storage.to_json
```

````

`````

`````{py:class} StorageBatch(api_util, **kwargs)
:canonical: altdss.Storage.StorageBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.Storage.StorageBatch
```

````{py:attribute} AmpLimit
:canonical: altdss.Storage.StorageBatch.AmpLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.Storage.StorageBatch.AmpLimitGain
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.Storage.StorageBatch.Balanced
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Storage.StorageBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Storage.StorageBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Bus1
```

````

````{py:attribute} ChargeTrigger
:canonical: altdss.Storage.StorageBatch.ChargeTrigger
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.ChargeTrigger
```

````

````{py:attribute} Class
:canonical: altdss.Storage.StorageBatch.Class
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Class
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Storage.StorageBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Storage.StorageBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Storage.StorageBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Storage.StorageBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Storage.StorageBatch.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Storage.StorageBatch.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Conn_str
```

````

````{py:attribute} ControlMode
:canonical: altdss.Storage.StorageBatch.ControlMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.ControlMode
```

````

````{py:attribute} ControlMode_str
:canonical: altdss.Storage.StorageBatch.ControlMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.ControlMode_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Storage.StorageBatch.Currents

```{autodoc2-docstring} altdss.Storage.StorageBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Storage.StorageBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Storage.StorageBatch.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.Storage.StorageBatch.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.Storage.StorageBatch.Daily_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Storage.StorageBatch.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.DebugTrace
```

````

````{py:attribute} DischargeTrigger
:canonical: altdss.Storage.StorageBatch.DischargeTrigger
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.DischargeTrigger
```

````

````{py:attribute} DispMode
:canonical: altdss.Storage.StorageBatch.DispMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.DispMode
```

````

````{py:attribute} DispMode_str
:canonical: altdss.Storage.StorageBatch.DispMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.DispMode_str
```

````

````{py:attribute} Duty
:canonical: altdss.Storage.StorageBatch.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Duty
```

````

````{py:attribute} Duty_str
:canonical: altdss.Storage.StorageBatch.Duty_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Duty_str
```

````

````{py:attribute} DynOut
:canonical: altdss.Storage.StorageBatch.DynOut
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.DynOut
```

````

````{py:attribute} DynaDLL
:canonical: altdss.Storage.StorageBatch.DynaDLL
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.DynaDLL
```

````

````{py:attribute} DynaData
:canonical: altdss.Storage.StorageBatch.DynaData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.DynaData
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Storage.StorageBatch.DynamicEq
:type: typing.List[altdss.DynamicExp.DynamicExp]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.DynamicEq
```

````

````{py:attribute} DynamicEq_str
:canonical: altdss.Storage.StorageBatch.DynamicEq_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.DynamicEq_str
```

````

````{py:attribute} EffCurve
:canonical: altdss.Storage.StorageBatch.EffCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.EffCurve
```

````

````{py:attribute} EffCurve_str
:canonical: altdss.Storage.StorageBatch.EffCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.EffCurve_str
```

````

````{py:attribute} Enabled
:canonical: altdss.Storage.StorageBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Storage.StorageBatch.EnergyMeter

```{autodoc2-docstring} altdss.Storage.StorageBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Storage.StorageBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Storage.StorageBatch.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Storage.StorageBatch.FullName

```{autodoc2-docstring} altdss.Storage.StorageBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Storage.StorageBatch.GUID

```{autodoc2-docstring} altdss.Storage.StorageBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Storage.StorageBatch.Handle

```{autodoc2-docstring} altdss.Storage.StorageBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Storage.StorageBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Storage.StorageBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Storage.StorageBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Storage.StorageBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Storage.StorageBatch.HasVoltControl

```{autodoc2-docstring} altdss.Storage.StorageBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Storage.StorageBatch.IsIsolated

```{autodoc2-docstring} altdss.Storage.StorageBatch.IsIsolated
```

````

````{py:attribute} Kp
:canonical: altdss.Storage.StorageBatch.Kp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Kp
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Storage.StorageBatch.Like

```{autodoc2-docstring} altdss.Storage.StorageBatch.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.Storage.StorageBatch.LimitCurrent
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.LimitCurrent
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Storage.StorageBatch.Losses

```{autodoc2-docstring} altdss.Storage.StorageBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Storage.StorageBatch.MaxCurrent

```{autodoc2-docstring} altdss.Storage.StorageBatch.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Storage.StorageBatch.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Model
```

````

````{py:property} Name
:canonical: altdss.Storage.StorageBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Storage.StorageBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Storage.StorageBatch.NumConductors

```{autodoc2-docstring} altdss.Storage.StorageBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Storage.StorageBatch.NumControllers

```{autodoc2-docstring} altdss.Storage.StorageBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Storage.StorageBatch.NumPhases

```{autodoc2-docstring} altdss.Storage.StorageBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Storage.StorageBatch.NumTerminals

```{autodoc2-docstring} altdss.Storage.StorageBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Storage.StorageBatch.OCPDevice

```{autodoc2-docstring} altdss.Storage.StorageBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Storage.StorageBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Storage.StorageBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Storage.StorageBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Storage.StorageBatch.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.Storage.StorageBatch.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.Storage.StorageBatch.PFPriority
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.Storage.StorageBatch.PITol
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.PITol
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Storage.StorageBatch.PhaseLosses

```{autodoc2-docstring} altdss.Storage.StorageBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Storage.StorageBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Storage.StorageBatch.Powers

```{autodoc2-docstring} altdss.Storage.StorageBatch.Powers
```

````

````{py:attribute} SafeMode
:canonical: altdss.Storage.StorageBatch.SafeMode
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.Storage.StorageBatch.SafeVoltage
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.SafeVoltage
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Storage.StorageBatch.SeqCurrents

```{autodoc2-docstring} altdss.Storage.StorageBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Storage.StorageBatch.SeqPowers

```{autodoc2-docstring} altdss.Storage.StorageBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Storage.StorageBatch.SeqVoltages

```{autodoc2-docstring} altdss.Storage.StorageBatch.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.Storage.StorageBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.Storage.StorageBatch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Spectrum_str
```

````

````{py:attribute} State
:canonical: altdss.Storage.StorageBatch.State
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.State
```

````

````{py:attribute} State_str
:canonical: altdss.Storage.StorageBatch.State_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.State_str
```

````

````{py:attribute} TimeChargeTrig
:canonical: altdss.Storage.StorageBatch.TimeChargeTrig
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.TimeChargeTrig
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Storage.StorageBatch.TotalPowers

```{autodoc2-docstring} altdss.Storage.StorageBatch.TotalPowers
```

````

````{py:attribute} UserData
:canonical: altdss.Storage.StorageBatch.UserData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Storage.StorageBatch.UserModel
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Storage.StorageBatch.VMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Storage.StorageBatch.VMinpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.Storage.StorageBatch.VarFollowInverter
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.VarFollowInverter
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Storage.StorageBatch.Voltages

```{autodoc2-docstring} altdss.Storage.StorageBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Storage.StorageBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Storage.StorageBatch.VoltagesMagAng
```

````

````{py:attribute} WattPriority
:canonical: altdss.Storage.StorageBatch.WattPriority
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.WattPriority
```

````

````{py:attribute} Yearly
:canonical: altdss.Storage.StorageBatch.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.Storage.StorageBatch.Yearly_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.Storage.StorageBatch.__call__

```{autodoc2-docstring} altdss.Storage.StorageBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Storage.StorageBatch.__getitem__

```{autodoc2-docstring} altdss.Storage.StorageBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Storage.StorageBatch.__init__

```{autodoc2-docstring} altdss.Storage.StorageBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Storage.StorageBatch.__iter__

```{autodoc2-docstring} altdss.Storage.StorageBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Storage.StorageBatch.__len__

```{autodoc2-docstring} altdss.Storage.StorageBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Storage.StorageBatch.batch

```{autodoc2-docstring} altdss.Storage.StorageBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Storage.StorageBatch.begin_edit

```{autodoc2-docstring} altdss.Storage.StorageBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Storage.StorageBatchProperties]) -> altdss.Storage.StorageBatch
:canonical: altdss.Storage.StorageBatch.edit

```{autodoc2-docstring} altdss.Storage.StorageBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Storage.StorageBatch.end_edit

```{autodoc2-docstring} altdss.Storage.StorageBatch.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Storage.StorageBatch.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Storage.StorageBatch.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.Storage.StorageBatch.kVDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.Storage.StorageBatch.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kW
```

````

````{py:attribute} kWRated
:canonical: altdss.Storage.StorageBatch.kWRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kWRated
```

````

````{py:attribute} kWhRated
:canonical: altdss.Storage.StorageBatch.kWhRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kWhRated
```

````

````{py:attribute} kWhStored
:canonical: altdss.Storage.StorageBatch.kWhStored
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kWhStored
```

````

````{py:attribute} kvar
:canonical: altdss.Storage.StorageBatch.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.Storage.StorageBatch.kvarMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.Storage.StorageBatch.kvarMaxAbs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.kvarMaxAbs
```

````

````{py:attribute} pctCharge
:canonical: altdss.Storage.StorageBatch.pctCharge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctCharge
```

````

````{py:attribute} pctCutIn
:canonical: altdss.Storage.StorageBatch.pctCutIn
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.Storage.StorageBatch.pctCutOut
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctCutOut
```

````

````{py:attribute} pctDischarge
:canonical: altdss.Storage.StorageBatch.pctDischarge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctDischarge
```

````

````{py:attribute} pctEffCharge
:canonical: altdss.Storage.StorageBatch.pctEffCharge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctEffCharge
```

````

````{py:attribute} pctEffDischarge
:canonical: altdss.Storage.StorageBatch.pctEffDischarge
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctEffDischarge
```

````

````{py:attribute} pctIdlingkW
:canonical: altdss.Storage.StorageBatch.pctIdlingkW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctIdlingkW
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.Storage.StorageBatch.pctPMinNoVars
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.Storage.StorageBatch.pctPMinkvarMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctPMinkvarMax
```

````

````{py:attribute} pctR
:canonical: altdss.Storage.StorageBatch.pctR
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctR
```

````

````{py:attribute} pctReserve
:canonical: altdss.Storage.StorageBatch.pctReserve
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctReserve
```

````

````{py:attribute} pctStored
:canonical: altdss.Storage.StorageBatch.pctStored
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctStored
```

````

````{py:attribute} pctX
:canonical: altdss.Storage.StorageBatch.pctX
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctX
```

````

````{py:attribute} pctkWRated
:canonical: altdss.Storage.StorageBatch.pctkWRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Storage.StorageBatch.pctkWRated
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Storage.StorageBatch.to_json

```{autodoc2-docstring} altdss.Storage.StorageBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Storage.StorageBatch.to_list

```{autodoc2-docstring} altdss.Storage.StorageBatch.to_list
```

````

`````

`````{py:class} StorageBatchProperties()
:canonical: altdss.Storage.StorageBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties
```

````{py:attribute} AmpLimit
:canonical: altdss.Storage.StorageBatchProperties.AmpLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.Storage.StorageBatchProperties.AmpLimitGain
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.Storage.StorageBatchProperties.Balanced
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Storage.StorageBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Storage.StorageBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Bus1
```

````

````{py:attribute} ChargeTrigger
:canonical: altdss.Storage.StorageBatchProperties.ChargeTrigger
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.ChargeTrigger
```

````

````{py:attribute} Class
:canonical: altdss.Storage.StorageBatchProperties.Class
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Class
```

````

````{py:attribute} Conn
:canonical: altdss.Storage.StorageBatchProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.Connection], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Conn
```

````

````{py:attribute} ControlMode
:canonical: altdss.Storage.StorageBatchProperties.ControlMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InverterControlMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.InverterControlMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.ControlMode
```

````

````{py:attribute} Daily
:canonical: altdss.Storage.StorageBatchProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Daily
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Storage.StorageBatchProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.DebugTrace
```

````

````{py:attribute} DischargeTrigger
:canonical: altdss.Storage.StorageBatchProperties.DischargeTrigger
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.DischargeTrigger
```

````

````{py:attribute} DispMode
:canonical: altdss.Storage.StorageBatchProperties.DispMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.StorageDispatchMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.StorageDispatchMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.DispMode
```

````

````{py:attribute} Duty
:canonical: altdss.Storage.StorageBatchProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Duty
```

````

````{py:attribute} DynOut
:canonical: altdss.Storage.StorageBatchProperties.DynOut
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.DynOut
```

````

````{py:attribute} DynaDLL
:canonical: altdss.Storage.StorageBatchProperties.DynaDLL
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.DynaDLL
```

````

````{py:attribute} DynaData
:canonical: altdss.Storage.StorageBatchProperties.DynaData
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.DynaData
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Storage.StorageBatchProperties.DynamicEq
:type: typing.Union[typing.AnyStr, altdss.DynamicExp.DynamicExp, typing.List[typing.AnyStr], typing.List[altdss.DynamicExp.DynamicExp]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.DynamicEq
```

````

````{py:attribute} EffCurve
:canonical: altdss.Storage.StorageBatchProperties.EffCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.EffCurve
```

````

````{py:attribute} Enabled
:canonical: altdss.Storage.StorageBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Enabled
```

````

````{py:attribute} Kp
:canonical: altdss.Storage.StorageBatchProperties.Kp
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Kp
```

````

````{py:attribute} Like
:canonical: altdss.Storage.StorageBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.Storage.StorageBatchProperties.LimitCurrent
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.LimitCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Storage.StorageBatchProperties.Model
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Model
```

````

````{py:attribute} PF
:canonical: altdss.Storage.StorageBatchProperties.PF
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.Storage.StorageBatchProperties.PFPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.Storage.StorageBatchProperties.PITol
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.PITol
```

````

````{py:attribute} Phases
:canonical: altdss.Storage.StorageBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Phases
```

````

````{py:attribute} SafeMode
:canonical: altdss.Storage.StorageBatchProperties.SafeMode
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.Storage.StorageBatchProperties.SafeVoltage
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.SafeVoltage
```

````

````{py:attribute} Spectrum
:canonical: altdss.Storage.StorageBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Spectrum
```

````

````{py:attribute} State
:canonical: altdss.Storage.StorageBatchProperties.State
:type: typing.Union[typing.AnyStr, int, altdss.enums.StorageState, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.StorageState], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.State
```

````

````{py:attribute} TimeChargeTrig
:canonical: altdss.Storage.StorageBatchProperties.TimeChargeTrig
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.TimeChargeTrig
```

````

````{py:attribute} UserData
:canonical: altdss.Storage.StorageBatchProperties.UserData
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Storage.StorageBatchProperties.UserModel
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Storage.StorageBatchProperties.VMaxpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Storage.StorageBatchProperties.VMinpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.Storage.StorageBatchProperties.VarFollowInverter
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.VarFollowInverter
```

````

````{py:attribute} WattPriority
:canonical: altdss.Storage.StorageBatchProperties.WattPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.WattPriority
```

````

````{py:attribute} Yearly
:canonical: altdss.Storage.StorageBatchProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.Storage.StorageBatchProperties.__contains__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Storage.StorageBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Storage.StorageBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Storage.StorageBatchProperties.__dir__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Storage.StorageBatchProperties.__format__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Storage.StorageBatchProperties.__ge__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Storage.StorageBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Storage.StorageBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Storage.StorageBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Storage.StorageBatchProperties.__gt__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Storage.StorageBatchProperties.__init__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Storage.StorageBatchProperties.__ior__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Storage.StorageBatchProperties.__iter__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Storage.StorageBatchProperties.__le__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Storage.StorageBatchProperties.__len__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Storage.StorageBatchProperties.__lt__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Storage.StorageBatchProperties.__ne__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Storage.StorageBatchProperties.__new__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Storage.StorageBatchProperties.__or__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Storage.StorageBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Storage.StorageBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Storage.StorageBatchProperties.__repr__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Storage.StorageBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Storage.StorageBatchProperties.__ror__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Storage.StorageBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Storage.StorageBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Storage.StorageBatchProperties.__str__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Storage.StorageBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Storage.StorageBatchProperties.clear

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Storage.StorageBatchProperties.copy

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Storage.StorageBatchProperties.get

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Storage.StorageBatchProperties.items

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Storage.StorageBatchProperties.kV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Storage.StorageBatchProperties.kVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.Storage.StorageBatchProperties.kVDC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.Storage.StorageBatchProperties.kW
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kW
```

````

````{py:attribute} kWRated
:canonical: altdss.Storage.StorageBatchProperties.kWRated
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kWRated
```

````

````{py:attribute} kWhRated
:canonical: altdss.Storage.StorageBatchProperties.kWhRated
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kWhRated
```

````

````{py:attribute} kWhStored
:canonical: altdss.Storage.StorageBatchProperties.kWhStored
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kWhStored
```

````

````{py:method} keys()
:canonical: altdss.Storage.StorageBatchProperties.keys

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Storage.StorageBatchProperties.kvar
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.Storage.StorageBatchProperties.kvarMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.Storage.StorageBatchProperties.kvarMaxAbs
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.kvarMaxAbs
```

````

````{py:attribute} pctCharge
:canonical: altdss.Storage.StorageBatchProperties.pctCharge
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctCharge
```

````

````{py:attribute} pctCutIn
:canonical: altdss.Storage.StorageBatchProperties.pctCutIn
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.Storage.StorageBatchProperties.pctCutOut
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctCutOut
```

````

````{py:attribute} pctDischarge
:canonical: altdss.Storage.StorageBatchProperties.pctDischarge
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctDischarge
```

````

````{py:attribute} pctEffCharge
:canonical: altdss.Storage.StorageBatchProperties.pctEffCharge
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctEffCharge
```

````

````{py:attribute} pctEffDischarge
:canonical: altdss.Storage.StorageBatchProperties.pctEffDischarge
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctEffDischarge
```

````

````{py:attribute} pctIdlingkW
:canonical: altdss.Storage.StorageBatchProperties.pctIdlingkW
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctIdlingkW
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.Storage.StorageBatchProperties.pctPMinNoVars
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.Storage.StorageBatchProperties.pctPMinkvarMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctPMinkvarMax
```

````

````{py:attribute} pctR
:canonical: altdss.Storage.StorageBatchProperties.pctR
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctR
```

````

````{py:attribute} pctReserve
:canonical: altdss.Storage.StorageBatchProperties.pctReserve
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctReserve
```

````

````{py:attribute} pctStored
:canonical: altdss.Storage.StorageBatchProperties.pctStored
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctStored
```

````

````{py:attribute} pctX
:canonical: altdss.Storage.StorageBatchProperties.pctX
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctX
```

````

````{py:attribute} pctkWRated
:canonical: altdss.Storage.StorageBatchProperties.pctkWRated
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pctkWRated
```

````

````{py:method} pop()
:canonical: altdss.Storage.StorageBatchProperties.pop

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Storage.StorageBatchProperties.popitem

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Storage.StorageBatchProperties.setdefault

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Storage.StorageBatchProperties.update

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Storage.StorageBatchProperties.values

```{autodoc2-docstring} altdss.Storage.StorageBatchProperties.values
```

````

`````

`````{py:class} StorageProperties()
:canonical: altdss.Storage.StorageProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Storage.StorageProperties
```

````{py:attribute} AmpLimit
:canonical: altdss.Storage.StorageProperties.AmpLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.Storage.StorageProperties.AmpLimitGain
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.Storage.StorageProperties.Balanced
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Storage.StorageProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Storage.StorageProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Bus1
```

````

````{py:attribute} ChargeTrigger
:canonical: altdss.Storage.StorageProperties.ChargeTrigger
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.ChargeTrigger
```

````

````{py:attribute} Class
:canonical: altdss.Storage.StorageProperties.Class
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Class
```

````

````{py:attribute} Conn
:canonical: altdss.Storage.StorageProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Conn
```

````

````{py:attribute} ControlMode
:canonical: altdss.Storage.StorageProperties.ControlMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InverterControlMode]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.ControlMode
```

````

````{py:attribute} Daily
:canonical: altdss.Storage.StorageProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Daily
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Storage.StorageProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.DebugTrace
```

````

````{py:attribute} DischargeTrigger
:canonical: altdss.Storage.StorageProperties.DischargeTrigger
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.DischargeTrigger
```

````

````{py:attribute} DispMode
:canonical: altdss.Storage.StorageProperties.DispMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.StorageDispatchMode]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.DispMode
```

````

````{py:attribute} Duty
:canonical: altdss.Storage.StorageProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Duty
```

````

````{py:attribute} DynOut
:canonical: altdss.Storage.StorageProperties.DynOut
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.DynOut
```

````

````{py:attribute} DynaDLL
:canonical: altdss.Storage.StorageProperties.DynaDLL
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.DynaDLL
```

````

````{py:attribute} DynaData
:canonical: altdss.Storage.StorageProperties.DynaData
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.DynaData
```

````

````{py:attribute} DynamicEq
:canonical: altdss.Storage.StorageProperties.DynamicEq
:type: typing.Union[typing.AnyStr, altdss.DynamicExp.DynamicExp]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.DynamicEq
```

````

````{py:attribute} EffCurve
:canonical: altdss.Storage.StorageProperties.EffCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.EffCurve
```

````

````{py:attribute} Enabled
:canonical: altdss.Storage.StorageProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Enabled
```

````

````{py:attribute} Kp
:canonical: altdss.Storage.StorageProperties.Kp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Kp
```

````

````{py:attribute} Like
:canonical: altdss.Storage.StorageProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.Storage.StorageProperties.LimitCurrent
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.LimitCurrent
```

````

````{py:attribute} Model
:canonical: altdss.Storage.StorageProperties.Model
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Model
```

````

````{py:attribute} PF
:canonical: altdss.Storage.StorageProperties.PF
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.Storage.StorageProperties.PFPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.Storage.StorageProperties.PITol
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.PITol
```

````

````{py:attribute} Phases
:canonical: altdss.Storage.StorageProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Phases
```

````

````{py:attribute} SafeMode
:canonical: altdss.Storage.StorageProperties.SafeMode
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.Storage.StorageProperties.SafeVoltage
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.SafeVoltage
```

````

````{py:attribute} Spectrum
:canonical: altdss.Storage.StorageProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Spectrum
```

````

````{py:attribute} State
:canonical: altdss.Storage.StorageProperties.State
:type: typing.Union[typing.AnyStr, int, altdss.enums.StorageState]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.State
```

````

````{py:attribute} TimeChargeTrig
:canonical: altdss.Storage.StorageProperties.TimeChargeTrig
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.TimeChargeTrig
```

````

````{py:attribute} UserData
:canonical: altdss.Storage.StorageProperties.UserData
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.Storage.StorageProperties.UserModel
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.Storage.StorageProperties.VMaxpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.Storage.StorageProperties.VMinpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.Storage.StorageProperties.VarFollowInverter
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.VarFollowInverter
```

````

````{py:attribute} WattPriority
:canonical: altdss.Storage.StorageProperties.WattPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.WattPriority
```

````

````{py:attribute} Yearly
:canonical: altdss.Storage.StorageProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.Storage.StorageProperties.__contains__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Storage.StorageProperties.__delattr__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Storage.StorageProperties.__delitem__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Storage.StorageProperties.__dir__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Storage.StorageProperties.__format__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Storage.StorageProperties.__ge__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Storage.StorageProperties.__getattribute__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Storage.StorageProperties.__getitem__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Storage.StorageProperties.__getstate__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Storage.StorageProperties.__gt__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Storage.StorageProperties.__init__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Storage.StorageProperties.__ior__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Storage.StorageProperties.__iter__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Storage.StorageProperties.__le__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Storage.StorageProperties.__len__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Storage.StorageProperties.__lt__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Storage.StorageProperties.__ne__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Storage.StorageProperties.__new__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Storage.StorageProperties.__or__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Storage.StorageProperties.__reduce__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Storage.StorageProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Storage.StorageProperties.__repr__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Storage.StorageProperties.__reversed__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Storage.StorageProperties.__ror__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Storage.StorageProperties.__setitem__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Storage.StorageProperties.__sizeof__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Storage.StorageProperties.__str__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Storage.StorageProperties.__subclasshook__

```{autodoc2-docstring} altdss.Storage.StorageProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Storage.StorageProperties.clear

```{autodoc2-docstring} altdss.Storage.StorageProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Storage.StorageProperties.copy

```{autodoc2-docstring} altdss.Storage.StorageProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Storage.StorageProperties.get

```{autodoc2-docstring} altdss.Storage.StorageProperties.get
```

````

````{py:method} items()
:canonical: altdss.Storage.StorageProperties.items

```{autodoc2-docstring} altdss.Storage.StorageProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Storage.StorageProperties.kV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.Storage.StorageProperties.kVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.Storage.StorageProperties.kVDC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.Storage.StorageProperties.kW
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kW
```

````

````{py:attribute} kWRated
:canonical: altdss.Storage.StorageProperties.kWRated
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kWRated
```

````

````{py:attribute} kWhRated
:canonical: altdss.Storage.StorageProperties.kWhRated
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kWhRated
```

````

````{py:attribute} kWhStored
:canonical: altdss.Storage.StorageProperties.kWhStored
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kWhStored
```

````

````{py:method} keys()
:canonical: altdss.Storage.StorageProperties.keys

```{autodoc2-docstring} altdss.Storage.StorageProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Storage.StorageProperties.kvar
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.Storage.StorageProperties.kvarMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.Storage.StorageProperties.kvarMaxAbs
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.kvarMaxAbs
```

````

````{py:attribute} pctCharge
:canonical: altdss.Storage.StorageProperties.pctCharge
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctCharge
```

````

````{py:attribute} pctCutIn
:canonical: altdss.Storage.StorageProperties.pctCutIn
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.Storage.StorageProperties.pctCutOut
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctCutOut
```

````

````{py:attribute} pctDischarge
:canonical: altdss.Storage.StorageProperties.pctDischarge
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctDischarge
```

````

````{py:attribute} pctEffCharge
:canonical: altdss.Storage.StorageProperties.pctEffCharge
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctEffCharge
```

````

````{py:attribute} pctEffDischarge
:canonical: altdss.Storage.StorageProperties.pctEffDischarge
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctEffDischarge
```

````

````{py:attribute} pctIdlingkW
:canonical: altdss.Storage.StorageProperties.pctIdlingkW
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctIdlingkW
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.Storage.StorageProperties.pctPMinNoVars
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.Storage.StorageProperties.pctPMinkvarMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctPMinkvarMax
```

````

````{py:attribute} pctR
:canonical: altdss.Storage.StorageProperties.pctR
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctR
```

````

````{py:attribute} pctReserve
:canonical: altdss.Storage.StorageProperties.pctReserve
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctReserve
```

````

````{py:attribute} pctStored
:canonical: altdss.Storage.StorageProperties.pctStored
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctStored
```

````

````{py:attribute} pctX
:canonical: altdss.Storage.StorageProperties.pctX
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctX
```

````

````{py:attribute} pctkWRated
:canonical: altdss.Storage.StorageProperties.pctkWRated
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Storage.StorageProperties.pctkWRated
```

````

````{py:method} pop()
:canonical: altdss.Storage.StorageProperties.pop

```{autodoc2-docstring} altdss.Storage.StorageProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Storage.StorageProperties.popitem

```{autodoc2-docstring} altdss.Storage.StorageProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Storage.StorageProperties.setdefault

```{autodoc2-docstring} altdss.Storage.StorageProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Storage.StorageProperties.update

```{autodoc2-docstring} altdss.Storage.StorageProperties.update
```

````

````{py:method} values()
:canonical: altdss.Storage.StorageProperties.values

```{autodoc2-docstring} altdss.Storage.StorageProperties.values
```

````

`````
