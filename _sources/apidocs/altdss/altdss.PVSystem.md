# {py:mod}`altdss.PVSystem`

```{py:module} altdss.PVSystem
```

```{autodoc2-docstring} altdss.PVSystem
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IPVSystem <altdss.PVSystem.IPVSystem>`
  - ```{autodoc2-docstring} altdss.PVSystem.IPVSystem
    :summary:
    ```
* - {py:obj}`PVSystem <altdss.PVSystem.PVSystem>`
  - ```{autodoc2-docstring} altdss.PVSystem.PVSystem
    :summary:
    ```
* - {py:obj}`PVSystemBatch <altdss.PVSystem.PVSystemBatch>`
  - ```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch
    :summary:
    ```
* - {py:obj}`PVSystemBatchProperties <altdss.PVSystem.PVSystemBatchProperties>`
  - ```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties
    :summary:
    ```
* - {py:obj}`PVSystemProperties <altdss.PVSystem.PVSystemProperties>`
  - ```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties
    :summary:
    ```
````

### API

`````{py:class} IPVSystem(iobj)
:canonical: altdss.PVSystem.IPVSystem

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.PVSystem.PVSystemBatch`

```{autodoc2-docstring} altdss.PVSystem.IPVSystem
```

````{py:attribute} AmpLimit
:canonical: altdss.PVSystem.IPVSystem.AmpLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.PVSystem.IPVSystem.AmpLimitGain
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.PVSystem.IPVSystem.Balanced
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.PVSystem.IPVSystem.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.PVSystem.IPVSystem.Bus1
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.PVSystem.IPVSystem.Class
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Class
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.IPVSystem.ComplexSeqCurrents

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.IPVSystem.ComplexSeqVoltages

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.PVSystem.IPVSystem.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.PVSystem.IPVSystem.Conn_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Conn_str
```

````

````{py:attribute} ControlMode
:canonical: altdss.PVSystem.IPVSystem.ControlMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.ControlMode
```

````

````{py:attribute} ControlMode_str
:canonical: altdss.PVSystem.IPVSystem.ControlMode_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.ControlMode_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.IPVSystem.Currents

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.IPVSystem.CurrentsMagAng

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.PVSystem.IPVSystem.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.PVSystem.IPVSystem.Daily_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.PVSystem.IPVSystem.DebugTrace
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.DebugTrace
```

````

````{py:attribute} Duty
:canonical: altdss.PVSystem.IPVSystem.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.PVSystem.IPVSystem.DutyStart
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.DutyStart
```

````

````{py:attribute} Duty_str
:canonical: altdss.PVSystem.IPVSystem.Duty_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Duty_str
```

````

````{py:attribute} DynOut
:canonical: altdss.PVSystem.IPVSystem.DynOut
:type: typing.List[typing.List[str]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.PVSystem.IPVSystem.DynamicEq
:type: typing.List[altdss.DynamicExp.DynamicExp]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.DynamicEq
```

````

````{py:attribute} DynamicEq_str
:canonical: altdss.PVSystem.IPVSystem.DynamicEq_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.DynamicEq_str
```

````

````{py:attribute} EffCurve
:canonical: altdss.PVSystem.IPVSystem.EffCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.EffCurve
```

````

````{py:attribute} EffCurve_str
:canonical: altdss.PVSystem.IPVSystem.EffCurve_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.EffCurve_str
```

````

````{py:attribute} Enabled
:canonical: altdss.PVSystem.IPVSystem.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.PVSystem.IPVSystem.EnergyMeter

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.PVSystem.IPVSystem.EnergyMeterName

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.PVSystem.IPVSystem.FullName

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.PVSystem.IPVSystem.GUID

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.IPVSystem.Handle

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.PVSystem.IPVSystem.HasOCPDevice

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.PVSystem.IPVSystem.HasSwitchControl

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.PVSystem.IPVSystem.HasVoltControl

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.HasVoltControl
```

````

````{py:attribute} Irradiance
:canonical: altdss.PVSystem.IPVSystem.Irradiance
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Irradiance
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.PVSystem.IPVSystem.IsIsolated

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.IsIsolated
```

````

````{py:attribute} Kp
:canonical: altdss.PVSystem.IPVSystem.Kp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Kp
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PVSystem.IPVSystem.Like

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.PVSystem.IPVSystem.LimitCurrent
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.LimitCurrent
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.IPVSystem.Losses

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.PVSystem.IPVSystem.MaxCurrent

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.PVSystem.IPVSystem.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Model
```

````

````{py:property} Name
:canonical: altdss.PVSystem.IPVSystem.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.IPVSystem.NumConductors

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.IPVSystem.NumControllers

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.IPVSystem.NumPhases

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.IPVSystem.NumTerminals

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.PVSystem.IPVSystem.OCPDevice

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.IPVSystem.OCPDeviceIndex

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.PVSystem.IPVSystem.OCPDeviceType

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.PVSystem.IPVSystem.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.PVSystem.IPVSystem.PFPriority
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.PVSystem.IPVSystem.PITol
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.PITol
```

````

````{py:attribute} PTCurve
:canonical: altdss.PVSystem.IPVSystem.PTCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.PTCurve
```

````

````{py:attribute} PTCurve_str
:canonical: altdss.PVSystem.IPVSystem.PTCurve_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.PTCurve_str
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.IPVSystem.PhaseLosses

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.PVSystem.IPVSystem.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Phases
```

````

````{py:attribute} Pmpp
:canonical: altdss.PVSystem.IPVSystem.Pmpp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Pmpp
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.IPVSystem.Powers

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Powers
```

````

````{py:attribute} SafeMode
:canonical: altdss.PVSystem.IPVSystem.SafeMode
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.PVSystem.IPVSystem.SafeVoltage
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.SafeVoltage
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.IPVSystem.SeqCurrents

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.IPVSystem.SeqPowers

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.IPVSystem.SeqVoltages

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.PVSystem.IPVSystem.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.PVSystem.IPVSystem.Spectrum_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Spectrum_str
```

````

````{py:attribute} TDaily
:canonical: altdss.PVSystem.IPVSystem.TDaily
:type: typing.List[altdss.TShape.TShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.TDaily
```

````

````{py:attribute} TDaily_str
:canonical: altdss.PVSystem.IPVSystem.TDaily_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.TDaily_str
```

````

````{py:attribute} TDuty
:canonical: altdss.PVSystem.IPVSystem.TDuty
:type: typing.List[altdss.TShape.TShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.TDuty
```

````

````{py:attribute} TDuty_str
:canonical: altdss.PVSystem.IPVSystem.TDuty_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.TDuty_str
```

````

````{py:attribute} TYearly
:canonical: altdss.PVSystem.IPVSystem.TYearly
:type: typing.List[altdss.TShape.TShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.TYearly
```

````

````{py:attribute} TYearly_str
:canonical: altdss.PVSystem.IPVSystem.TYearly_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.TYearly_str
```

````

````{py:attribute} Temperature
:canonical: altdss.PVSystem.IPVSystem.Temperature
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Temperature
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.IPVSystem.TotalPowers

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.TotalPowers
```

````

````{py:attribute} UserData
:canonical: altdss.PVSystem.IPVSystem.UserData
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.PVSystem.IPVSystem.UserModel
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.PVSystem.IPVSystem.VMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.PVSystem.IPVSystem.VMinpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.PVSystem.IPVSystem.VarFollowInverter
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.VarFollowInverter
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.IPVSystem.Voltages

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.IPVSystem.VoltagesMagAng

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.VoltagesMagAng
```

````

````{py:attribute} WattPriority
:canonical: altdss.PVSystem.IPVSystem.WattPriority
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.WattPriority
```

````

````{py:attribute} Yearly
:canonical: altdss.PVSystem.IPVSystem.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.PVSystem.IPVSystem.Yearly_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.PVSystem.IPVSystem.__call__

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.PVSystem.IPVSystem.__contains__

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.PVSystem.IPVSystem.__getitem__

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.PVSystem.IPVSystem.__init__

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.PVSystem.IPVSystem.__iter__

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.PVSystem.IPVSystem.__len__

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.PVSystem.IPVSystem.batch

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.PVSystem.PVSystemBatchProperties]) -> altdss.PVSystem.PVSystemBatch
:canonical: altdss.PVSystem.IPVSystem.batch_new

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.PVSystem.IPVSystem.begin_edit

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.PVSystem.IPVSystem.end_edit

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.PVSystem.IPVSystem.find

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.find
```

````

````{py:attribute} kV
:canonical: altdss.PVSystem.IPVSystem.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.kV
```

````

````{py:attribute} kVA
:canonical: altdss.PVSystem.IPVSystem.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.PVSystem.IPVSystem.kVDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.kVDC
```

````

````{py:attribute} kvar
:canonical: altdss.PVSystem.IPVSystem.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.PVSystem.IPVSystem.kvarMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.PVSystem.IPVSystem.kvarMaxAbs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.kvarMaxAbs
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.PVSystem.PVSystemProperties]) -> altdss.PVSystem.PVSystem
:canonical: altdss.PVSystem.IPVSystem.new

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.new
```

````

````{py:attribute} pctCutIn
:canonical: altdss.PVSystem.IPVSystem.pctCutIn
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.PVSystem.IPVSystem.pctCutOut
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.pctCutOut
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.PVSystem.IPVSystem.pctPMinNoVars
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.PVSystem.IPVSystem.pctPMinkvarMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.pctPMinkvarMax
```

````

````{py:attribute} pctPmpp
:canonical: altdss.PVSystem.IPVSystem.pctPmpp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.pctPmpp
```

````

````{py:attribute} pctR
:canonical: altdss.PVSystem.IPVSystem.pctR
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.pctR
```

````

````{py:attribute} pctX
:canonical: altdss.PVSystem.IPVSystem.pctX
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.pctX
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.PVSystem.IPVSystem.to_json

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.to_json
```

````

````{py:method} to_list()
:canonical: altdss.PVSystem.IPVSystem.to_list

```{autodoc2-docstring} altdss.PVSystem.IPVSystem.to_list
```

````

`````

`````{py:class} PVSystem(api_util, ptr)
:canonical: altdss.PVSystem.PVSystem

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`, {py:obj}`altdss.PCElement.ElementHasRegistersMixin`

```{autodoc2-docstring} altdss.PVSystem.PVSystem
```

````{py:attribute} AmpLimit
:canonical: altdss.PVSystem.PVSystem.AmpLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.PVSystem.PVSystem.AmpLimitGain
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.PVSystem.PVSystem.Balanced
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.PVSystem.PVSystem.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.PVSystem.PVSystem.Bus1
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.PVSystem.PVSystem.Class
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Class
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.PVSystem.PVSystem.Close

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystem.ComplexSeqCurrents

```{autodoc2-docstring} altdss.PVSystem.PVSystem.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystem.ComplexSeqVoltages

```{autodoc2-docstring} altdss.PVSystem.PVSystem.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.PVSystem.PVSystem.Conn
:type: altdss.enums.Connection
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.PVSystem.PVSystem.Conn_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Conn_str
```

````

````{py:attribute} ControlMode
:canonical: altdss.PVSystem.PVSystem.ControlMode
:type: altdss.enums.InverterControlMode
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.ControlMode
```

````

````{py:attribute} ControlMode_str
:canonical: altdss.PVSystem.PVSystem.ControlMode_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.ControlMode_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystem.Currents

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Currents
```

````

````{py:attribute} Daily
:canonical: altdss.PVSystem.PVSystem.Daily
:type: altdss.LoadShape.LoadShape
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.PVSystem.PVSystem.Daily_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.PVSystem.PVSystem.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.DebugTrace
```

````

````{py:attribute} DisplayName
:canonical: altdss.PVSystem.PVSystem.DisplayName
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.DisplayName
```

````

````{py:attribute} Duty
:canonical: altdss.PVSystem.PVSystem.Duty
:type: altdss.LoadShape.LoadShape
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.PVSystem.PVSystem.DutyStart
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.DutyStart
```

````

````{py:attribute} Duty_str
:canonical: altdss.PVSystem.PVSystem.Duty_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Duty_str
```

````

````{py:attribute} DynOut
:canonical: altdss.PVSystem.PVSystem.DynOut
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.PVSystem.PVSystem.DynamicEq
:type: altdss.DynamicExp.DynamicExp
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.DynamicEq
```

````

````{py:attribute} DynamicEq_str
:canonical: altdss.PVSystem.PVSystem.DynamicEq_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.DynamicEq_str
```

````

````{py:attribute} EffCurve
:canonical: altdss.PVSystem.PVSystem.EffCurve
:type: altdss.XYcurve.XYcurve
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.EffCurve
```

````

````{py:attribute} EffCurve_str
:canonical: altdss.PVSystem.PVSystem.EffCurve_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.EffCurve_str
```

````

````{py:attribute} Enabled
:canonical: altdss.PVSystem.PVSystem.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.PVSystem.PVSystem.EnergyMeter

```{autodoc2-docstring} altdss.PVSystem.PVSystem.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.PVSystem.PVSystem.EnergyMeterName

```{autodoc2-docstring} altdss.PVSystem.PVSystem.EnergyMeterName
```

````

````{py:method} FullName() -> str
:canonical: altdss.PVSystem.PVSystem.FullName

```{autodoc2-docstring} altdss.PVSystem.PVSystem.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.PVSystem.PVSystem.GUID

```{autodoc2-docstring} altdss.PVSystem.PVSystem.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.PVSystem.PVSystem.GetVariableValue

```{autodoc2-docstring} altdss.PVSystem.PVSystem.GetVariableValue
```

````

````{py:method} Handle() -> int
:canonical: altdss.PVSystem.PVSystem.Handle

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.PVSystem.PVSystem.HasOCPDevice

```{autodoc2-docstring} altdss.PVSystem.PVSystem.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.PVSystem.PVSystem.HasSwitchControl

```{autodoc2-docstring} altdss.PVSystem.PVSystem.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.PVSystem.PVSystem.HasVoltControl

```{autodoc2-docstring} altdss.PVSystem.PVSystem.HasVoltControl
```

````

````{py:attribute} Irradiance
:canonical: altdss.PVSystem.PVSystem.Irradiance
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Irradiance
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.PVSystem.PVSystem.IsIsolated

```{autodoc2-docstring} altdss.PVSystem.PVSystem.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.PVSystem.PVSystem.IsOpen

```{autodoc2-docstring} altdss.PVSystem.PVSystem.IsOpen
```

````

````{py:attribute} Kp
:canonical: altdss.PVSystem.PVSystem.Kp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Kp
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.PVSystem.PVSystem.Like

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.PVSystem.PVSystem.LimitCurrent
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.LimitCurrent
```

````

````{py:method} Losses() -> complex
:canonical: altdss.PVSystem.PVSystem.Losses

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.PVSystem.PVSystem.MaxCurrent

```{autodoc2-docstring} altdss.PVSystem.PVSystem.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.PVSystem.PVSystem.Model
:type: altdss.enums.PVSystemModel
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Model
```

````

````{py:property} Name
:canonical: altdss.PVSystem.PVSystem.Name
:type: str

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.PVSystem.NodeOrder

```{autodoc2-docstring} altdss.PVSystem.PVSystem.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.PVSystem.NodeRef

```{autodoc2-docstring} altdss.PVSystem.PVSystem.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.PVSystem.PVSystem.NumConductors

```{autodoc2-docstring} altdss.PVSystem.PVSystem.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.PVSystem.PVSystem.NumControllers

```{autodoc2-docstring} altdss.PVSystem.PVSystem.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.PVSystem.PVSystem.NumPhases

```{autodoc2-docstring} altdss.PVSystem.PVSystem.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.PVSystem.PVSystem.NumTerminals

```{autodoc2-docstring} altdss.PVSystem.PVSystem.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.PVSystem.PVSystem.OCPDevice

```{autodoc2-docstring} altdss.PVSystem.PVSystem.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.PVSystem.PVSystem.OCPDeviceIndex

```{autodoc2-docstring} altdss.PVSystem.PVSystem.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.PVSystem.PVSystem.OCPDeviceType

```{autodoc2-docstring} altdss.PVSystem.PVSystem.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.PVSystem.PVSystem.Open

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Open
```

````

````{py:attribute} PF
:canonical: altdss.PVSystem.PVSystem.PF
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.PVSystem.PVSystem.PFPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.PVSystem.PVSystem.PITol
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.PITol
```

````

````{py:attribute} PTCurve
:canonical: altdss.PVSystem.PVSystem.PTCurve
:type: altdss.XYcurve.XYcurve
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.PTCurve
```

````

````{py:attribute} PTCurve_str
:canonical: altdss.PVSystem.PVSystem.PTCurve_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.PTCurve_str
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystem.PhaseLosses

```{autodoc2-docstring} altdss.PVSystem.PVSystem.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.PVSystem.PVSystem.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Phases
```

````

````{py:attribute} Pmpp
:canonical: altdss.PVSystem.PVSystem.Pmpp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Pmpp
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystem.Powers

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Powers
```

````

````{py:method} RegisterNames() -> typing.List[str]
:canonical: altdss.PVSystem.PVSystem.RegisterNames

```{autodoc2-docstring} altdss.PVSystem.PVSystem.RegisterNames
```

````

````{py:method} RegisterValues() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystem.RegisterValues

```{autodoc2-docstring} altdss.PVSystem.PVSystem.RegisterValues
```

````

````{py:method} RegistersDict() -> typing.Dict[str, float]
:canonical: altdss.PVSystem.PVSystem.RegistersDict

```{autodoc2-docstring} altdss.PVSystem.PVSystem.RegistersDict
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystem.Residuals

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Residuals
```

````

````{py:attribute} SafeMode
:canonical: altdss.PVSystem.PVSystem.SafeMode
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.PVSystem.PVSystem.SafeVoltage
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.SafeVoltage
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystem.SeqCurrents

```{autodoc2-docstring} altdss.PVSystem.PVSystem.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystem.SeqPowers

```{autodoc2-docstring} altdss.PVSystem.PVSystem.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystem.SeqVoltages

```{autodoc2-docstring} altdss.PVSystem.PVSystem.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.PVSystem.PVSystem.SetVariableValue

```{autodoc2-docstring} altdss.PVSystem.PVSystem.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.PVSystem.PVSystem.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.PVSystem.PVSystem.Spectrum_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Spectrum_str
```

````

````{py:attribute} TDaily
:canonical: altdss.PVSystem.PVSystem.TDaily
:type: altdss.TShape.TShape
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.TDaily
```

````

````{py:attribute} TDaily_str
:canonical: altdss.PVSystem.PVSystem.TDaily_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.TDaily_str
```

````

````{py:attribute} TDuty
:canonical: altdss.PVSystem.PVSystem.TDuty
:type: altdss.TShape.TShape
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.TDuty
```

````

````{py:attribute} TDuty_str
:canonical: altdss.PVSystem.PVSystem.TDuty_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.TDuty_str
```

````

````{py:attribute} TYearly
:canonical: altdss.PVSystem.PVSystem.TYearly
:type: altdss.TShape.TShape
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.TYearly
```

````

````{py:attribute} TYearly_str
:canonical: altdss.PVSystem.PVSystem.TYearly_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.TYearly_str
```

````

````{py:attribute} Temperature
:canonical: altdss.PVSystem.PVSystem.Temperature
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Temperature
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystem.TotalPowers

```{autodoc2-docstring} altdss.PVSystem.PVSystem.TotalPowers
```

````

````{py:attribute} UserData
:canonical: altdss.PVSystem.PVSystem.UserData
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.PVSystem.PVSystem.UserModel
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.PVSystem.PVSystem.VMaxpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.PVSystem.PVSystem.VMinpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.PVSystem.PVSystem.VarFollowInverter
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.VarFollowInverter
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.PVSystem.PVSystem.VariableNames

```{autodoc2-docstring} altdss.PVSystem.PVSystem.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystem.VariableValues

```{autodoc2-docstring} altdss.PVSystem.PVSystem.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.PVSystem.PVSystem.VariablesDict

```{autodoc2-docstring} altdss.PVSystem.PVSystem.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystem.Voltages

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystem.VoltagesMagAng

```{autodoc2-docstring} altdss.PVSystem.PVSystem.VoltagesMagAng
```

````

````{py:attribute} WattPriority
:canonical: altdss.PVSystem.PVSystem.WattPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.WattPriority
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystem.YPrim

```{autodoc2-docstring} altdss.PVSystem.PVSystem.YPrim
```

````

````{py:attribute} Yearly
:canonical: altdss.PVSystem.PVSystem.Yearly
:type: altdss.LoadShape.LoadShape
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.PVSystem.PVSystem.Yearly_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.Yearly_str
```

````

````{py:method} __hash__()
:canonical: altdss.PVSystem.PVSystem.__hash__

```{autodoc2-docstring} altdss.PVSystem.PVSystem.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.PVSystem.PVSystem.__init__

```{autodoc2-docstring} altdss.PVSystem.PVSystem.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.PVSystem.PVSystem.__ne__

```{autodoc2-docstring} altdss.PVSystem.PVSystem.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.PVSystem.PVSystem.__repr__

```{autodoc2-docstring} altdss.PVSystem.PVSystem.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.PVSystem.PVSystem.begin_edit

```{autodoc2-docstring} altdss.PVSystem.PVSystem.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.PVSystem.PVSystem.end_edit

```{autodoc2-docstring} altdss.PVSystem.PVSystem.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.PVSystem.PVSystem.kV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.kV
```

````

````{py:attribute} kVA
:canonical: altdss.PVSystem.PVSystem.kVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.PVSystem.PVSystem.kVDC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.kVDC
```

````

````{py:attribute} kvar
:canonical: altdss.PVSystem.PVSystem.kvar
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.PVSystem.PVSystem.kvarMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.PVSystem.PVSystem.kvarMaxAbs
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.kvarMaxAbs
```

````

````{py:attribute} pctCutIn
:canonical: altdss.PVSystem.PVSystem.pctCutIn
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.PVSystem.PVSystem.pctCutOut
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.pctCutOut
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.PVSystem.PVSystem.pctPMinNoVars
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.PVSystem.PVSystem.pctPMinkvarMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.pctPMinkvarMax
```

````

````{py:attribute} pctPmpp
:canonical: altdss.PVSystem.PVSystem.pctPmpp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.pctPmpp
```

````

````{py:attribute} pctR
:canonical: altdss.PVSystem.PVSystem.pctR
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.pctR
```

````

````{py:attribute} pctX
:canonical: altdss.PVSystem.PVSystem.pctX
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystem.pctX
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.PVSystem.PVSystem.to_json

```{autodoc2-docstring} altdss.PVSystem.PVSystem.to_json
```

````

`````

`````{py:class} PVSystemBatch(api_util, **kwargs)
:canonical: altdss.PVSystem.PVSystemBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch
```

````{py:attribute} AmpLimit
:canonical: altdss.PVSystem.PVSystemBatch.AmpLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.PVSystem.PVSystemBatch.AmpLimitGain
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.PVSystem.PVSystemBatch.Balanced
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.PVSystem.PVSystemBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.PVSystem.PVSystemBatch.Bus1
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.PVSystem.PVSystemBatch.Class
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Class
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystemBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystemBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.PVSystem.PVSystemBatch.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.PVSystem.PVSystemBatch.Conn_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Conn_str
```

````

````{py:attribute} ControlMode
:canonical: altdss.PVSystem.PVSystemBatch.ControlMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.ControlMode
```

````

````{py:attribute} ControlMode_str
:canonical: altdss.PVSystem.PVSystemBatch.ControlMode_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.ControlMode_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystemBatch.Currents

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystemBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.CurrentsMagAng
```

````

````{py:attribute} Daily
:canonical: altdss.PVSystem.PVSystemBatch.Daily
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Daily
```

````

````{py:attribute} Daily_str
:canonical: altdss.PVSystem.PVSystemBatch.Daily_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Daily_str
```

````

````{py:attribute} DebugTrace
:canonical: altdss.PVSystem.PVSystemBatch.DebugTrace
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.DebugTrace
```

````

````{py:attribute} Duty
:canonical: altdss.PVSystem.PVSystemBatch.Duty
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.PVSystem.PVSystemBatch.DutyStart
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.DutyStart
```

````

````{py:attribute} Duty_str
:canonical: altdss.PVSystem.PVSystemBatch.Duty_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Duty_str
```

````

````{py:attribute} DynOut
:canonical: altdss.PVSystem.PVSystemBatch.DynOut
:type: typing.List[typing.List[str]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.PVSystem.PVSystemBatch.DynamicEq
:type: typing.List[altdss.DynamicExp.DynamicExp]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.DynamicEq
```

````

````{py:attribute} DynamicEq_str
:canonical: altdss.PVSystem.PVSystemBatch.DynamicEq_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.DynamicEq_str
```

````

````{py:attribute} EffCurve
:canonical: altdss.PVSystem.PVSystemBatch.EffCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.EffCurve
```

````

````{py:attribute} EffCurve_str
:canonical: altdss.PVSystem.PVSystemBatch.EffCurve_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.EffCurve_str
```

````

````{py:attribute} Enabled
:canonical: altdss.PVSystem.PVSystemBatch.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.PVSystem.PVSystemBatch.EnergyMeter

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.PVSystem.PVSystemBatch.EnergyMeterName

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.PVSystem.PVSystemBatch.FullName

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.PVSystem.PVSystemBatch.GUID

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.PVSystemBatch.Handle

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.PVSystem.PVSystemBatch.HasOCPDevice

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.PVSystem.PVSystemBatch.HasSwitchControl

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.PVSystem.PVSystemBatch.HasVoltControl

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.HasVoltControl
```

````

````{py:attribute} Irradiance
:canonical: altdss.PVSystem.PVSystemBatch.Irradiance
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Irradiance
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.PVSystem.PVSystemBatch.IsIsolated

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.IsIsolated
```

````

````{py:attribute} Kp
:canonical: altdss.PVSystem.PVSystemBatch.Kp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Kp
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PVSystem.PVSystemBatch.Like

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.PVSystem.PVSystemBatch.LimitCurrent
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.LimitCurrent
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystemBatch.Losses

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.PVSystem.PVSystemBatch.MaxCurrent

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.MaxCurrent
```

````

````{py:attribute} Model
:canonical: altdss.PVSystem.PVSystemBatch.Model
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Model
```

````

````{py:property} Name
:canonical: altdss.PVSystem.PVSystemBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.PVSystemBatch.NumConductors

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.PVSystemBatch.NumControllers

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.PVSystemBatch.NumPhases

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.PVSystemBatch.NumTerminals

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.PVSystem.PVSystemBatch.OCPDevice

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.PVSystem.PVSystemBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.PVSystem.PVSystemBatch.OCPDeviceType

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.PVSystem.PVSystemBatch.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.PVSystem.PVSystemBatch.PFPriority
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.PVSystem.PVSystemBatch.PITol
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.PITol
```

````

````{py:attribute} PTCurve
:canonical: altdss.PVSystem.PVSystemBatch.PTCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.PTCurve
```

````

````{py:attribute} PTCurve_str
:canonical: altdss.PVSystem.PVSystemBatch.PTCurve_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.PTCurve_str
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystemBatch.PhaseLosses

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.PVSystem.PVSystemBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Phases
```

````

````{py:attribute} Pmpp
:canonical: altdss.PVSystem.PVSystemBatch.Pmpp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Pmpp
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystemBatch.Powers

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Powers
```

````

````{py:attribute} SafeMode
:canonical: altdss.PVSystem.PVSystemBatch.SafeMode
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.PVSystem.PVSystemBatch.SafeVoltage
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.SafeVoltage
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystemBatch.SeqCurrents

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystemBatch.SeqPowers

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystemBatch.SeqVoltages

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.PVSystem.PVSystemBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.PVSystem.PVSystemBatch.Spectrum_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Spectrum_str
```

````

````{py:attribute} TDaily
:canonical: altdss.PVSystem.PVSystemBatch.TDaily
:type: typing.List[altdss.TShape.TShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.TDaily
```

````

````{py:attribute} TDaily_str
:canonical: altdss.PVSystem.PVSystemBatch.TDaily_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.TDaily_str
```

````

````{py:attribute} TDuty
:canonical: altdss.PVSystem.PVSystemBatch.TDuty
:type: typing.List[altdss.TShape.TShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.TDuty
```

````

````{py:attribute} TDuty_str
:canonical: altdss.PVSystem.PVSystemBatch.TDuty_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.TDuty_str
```

````

````{py:attribute} TYearly
:canonical: altdss.PVSystem.PVSystemBatch.TYearly
:type: typing.List[altdss.TShape.TShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.TYearly
```

````

````{py:attribute} TYearly_str
:canonical: altdss.PVSystem.PVSystemBatch.TYearly_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.TYearly_str
```

````

````{py:attribute} Temperature
:canonical: altdss.PVSystem.PVSystemBatch.Temperature
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Temperature
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystemBatch.TotalPowers

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.TotalPowers
```

````

````{py:attribute} UserData
:canonical: altdss.PVSystem.PVSystemBatch.UserData
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.PVSystem.PVSystemBatch.UserModel
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.PVSystem.PVSystemBatch.VMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.PVSystem.PVSystemBatch.VMinpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.PVSystem.PVSystemBatch.VarFollowInverter
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.VarFollowInverter
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.PVSystem.PVSystemBatch.Voltages

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.PVSystem.PVSystemBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.VoltagesMagAng
```

````

````{py:attribute} WattPriority
:canonical: altdss.PVSystem.PVSystemBatch.WattPriority
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.WattPriority
```

````

````{py:attribute} Yearly
:canonical: altdss.PVSystem.PVSystemBatch.Yearly
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Yearly
```

````

````{py:attribute} Yearly_str
:canonical: altdss.PVSystem.PVSystemBatch.Yearly_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.Yearly_str
```

````

````{py:method} __call__()
:canonical: altdss.PVSystem.PVSystemBatch.__call__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.PVSystem.PVSystemBatch.__getitem__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.PVSystem.PVSystemBatch.__init__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.PVSystem.PVSystemBatch.__iter__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.PVSystem.PVSystemBatch.__len__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.PVSystem.PVSystemBatch.begin_edit

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.PVSystem.PVSystemBatch.end_edit

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.PVSystem.PVSystemBatch.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.kV
```

````

````{py:attribute} kVA
:canonical: altdss.PVSystem.PVSystemBatch.kVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.PVSystem.PVSystemBatch.kVDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.kVDC
```

````

````{py:attribute} kvar
:canonical: altdss.PVSystem.PVSystemBatch.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.PVSystem.PVSystemBatch.kvarMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.PVSystem.PVSystemBatch.kvarMaxAbs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.kvarMaxAbs
```

````

````{py:attribute} pctCutIn
:canonical: altdss.PVSystem.PVSystemBatch.pctCutIn
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.PVSystem.PVSystemBatch.pctCutOut
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.pctCutOut
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.PVSystem.PVSystemBatch.pctPMinNoVars
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.PVSystem.PVSystemBatch.pctPMinkvarMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.pctPMinkvarMax
```

````

````{py:attribute} pctPmpp
:canonical: altdss.PVSystem.PVSystemBatch.pctPmpp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.pctPmpp
```

````

````{py:attribute} pctR
:canonical: altdss.PVSystem.PVSystemBatch.pctR
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.pctR
```

````

````{py:attribute} pctX
:canonical: altdss.PVSystem.PVSystemBatch.pctX
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.pctX
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.PVSystem.PVSystemBatch.to_json

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.PVSystem.PVSystemBatch.to_list

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatch.to_list
```

````

`````

`````{py:class} PVSystemBatchProperties()
:canonical: altdss.PVSystem.PVSystemBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties
```

````{py:attribute} AmpLimit
:canonical: altdss.PVSystem.PVSystemBatchProperties.AmpLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.PVSystem.PVSystemBatchProperties.AmpLimitGain
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.PVSystem.PVSystemBatchProperties.Balanced
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.PVSystem.PVSystemBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.PVSystem.PVSystemBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.PVSystem.PVSystemBatchProperties.Class
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Class
```

````

````{py:attribute} Conn
:canonical: altdss.PVSystem.PVSystemBatchProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.Connection], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Conn
```

````

````{py:attribute} ControlMode
:canonical: altdss.PVSystem.PVSystemBatchProperties.ControlMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InverterControlMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.InverterControlMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.ControlMode
```

````

````{py:attribute} Daily
:canonical: altdss.PVSystem.PVSystemBatchProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Daily
```

````

````{py:attribute} DebugTrace
:canonical: altdss.PVSystem.PVSystemBatchProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.DebugTrace
```

````

````{py:attribute} Duty
:canonical: altdss.PVSystem.PVSystemBatchProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.PVSystem.PVSystemBatchProperties.DutyStart
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.DutyStart
```

````

````{py:attribute} DynOut
:canonical: altdss.PVSystem.PVSystemBatchProperties.DynOut
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.PVSystem.PVSystemBatchProperties.DynamicEq
:type: typing.Union[typing.AnyStr, altdss.DynamicExp.DynamicExp, typing.List[typing.AnyStr], typing.List[altdss.DynamicExp.DynamicExp]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.DynamicEq
```

````

````{py:attribute} EffCurve
:canonical: altdss.PVSystem.PVSystemBatchProperties.EffCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.EffCurve
```

````

````{py:attribute} Enabled
:canonical: altdss.PVSystem.PVSystemBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Enabled
```

````

````{py:attribute} Irradiance
:canonical: altdss.PVSystem.PVSystemBatchProperties.Irradiance
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Irradiance
```

````

````{py:attribute} Kp
:canonical: altdss.PVSystem.PVSystemBatchProperties.Kp
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Kp
```

````

````{py:attribute} Like
:canonical: altdss.PVSystem.PVSystemBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.PVSystem.PVSystemBatchProperties.LimitCurrent
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.LimitCurrent
```

````

````{py:attribute} Model
:canonical: altdss.PVSystem.PVSystemBatchProperties.Model
:type: typing.Union[int, altdss.enums.PVSystemModel, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Model
```

````

````{py:attribute} PF
:canonical: altdss.PVSystem.PVSystemBatchProperties.PF
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.PVSystem.PVSystemBatchProperties.PFPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.PVSystem.PVSystemBatchProperties.PITol
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.PITol
```

````

````{py:attribute} PTCurve
:canonical: altdss.PVSystem.PVSystemBatchProperties.PTCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.PTCurve
```

````

````{py:attribute} Phases
:canonical: altdss.PVSystem.PVSystemBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Phases
```

````

````{py:attribute} Pmpp
:canonical: altdss.PVSystem.PVSystemBatchProperties.Pmpp
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Pmpp
```

````

````{py:attribute} SafeMode
:canonical: altdss.PVSystem.PVSystemBatchProperties.SafeMode
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.PVSystem.PVSystemBatchProperties.SafeVoltage
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.SafeVoltage
```

````

````{py:attribute} Spectrum
:canonical: altdss.PVSystem.PVSystemBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Spectrum
```

````

````{py:attribute} TDaily
:canonical: altdss.PVSystem.PVSystemBatchProperties.TDaily
:type: typing.Union[typing.AnyStr, altdss.TShape.TShape, typing.List[typing.AnyStr], typing.List[altdss.TShape.TShape]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.TDaily
```

````

````{py:attribute} TDuty
:canonical: altdss.PVSystem.PVSystemBatchProperties.TDuty
:type: typing.Union[typing.AnyStr, altdss.TShape.TShape, typing.List[typing.AnyStr], typing.List[altdss.TShape.TShape]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.TDuty
```

````

````{py:attribute} TYearly
:canonical: altdss.PVSystem.PVSystemBatchProperties.TYearly
:type: typing.Union[typing.AnyStr, altdss.TShape.TShape, typing.List[typing.AnyStr], typing.List[altdss.TShape.TShape]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.TYearly
```

````

````{py:attribute} Temperature
:canonical: altdss.PVSystem.PVSystemBatchProperties.Temperature
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Temperature
```

````

````{py:attribute} UserData
:canonical: altdss.PVSystem.PVSystemBatchProperties.UserData
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.PVSystem.PVSystemBatchProperties.UserModel
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.PVSystem.PVSystemBatchProperties.VMaxpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.PVSystem.PVSystemBatchProperties.VMinpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.PVSystem.PVSystemBatchProperties.VarFollowInverter
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.VarFollowInverter
```

````

````{py:attribute} WattPriority
:canonical: altdss.PVSystem.PVSystemBatchProperties.WattPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.WattPriority
```

````

````{py:attribute} Yearly
:canonical: altdss.PVSystem.PVSystemBatchProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__contains__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__delattr__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__delitem__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__dir__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__format__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__ge__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__getitem__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__getstate__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__gt__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__init__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__ior__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__iter__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__le__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__len__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__lt__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__ne__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__new__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__or__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__reduce__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__repr__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__reversed__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__ror__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__setitem__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__str__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.PVSystem.PVSystemBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.PVSystem.PVSystemBatchProperties.clear

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.PVSystem.PVSystemBatchProperties.copy

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.PVSystem.PVSystemBatchProperties.get

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.PVSystem.PVSystemBatchProperties.items

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.PVSystem.PVSystemBatchProperties.kV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.PVSystem.PVSystemBatchProperties.kVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.PVSystem.PVSystemBatchProperties.kVDC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.kVDC
```

````

````{py:method} keys()
:canonical: altdss.PVSystem.PVSystemBatchProperties.keys

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.PVSystem.PVSystemBatchProperties.kvar
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.PVSystem.PVSystemBatchProperties.kvarMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.PVSystem.PVSystemBatchProperties.kvarMaxAbs
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.kvarMaxAbs
```

````

````{py:attribute} pctCutIn
:canonical: altdss.PVSystem.PVSystemBatchProperties.pctCutIn
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.PVSystem.PVSystemBatchProperties.pctCutOut
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.pctCutOut
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.PVSystem.PVSystemBatchProperties.pctPMinNoVars
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.PVSystem.PVSystemBatchProperties.pctPMinkvarMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.pctPMinkvarMax
```

````

````{py:attribute} pctPmpp
:canonical: altdss.PVSystem.PVSystemBatchProperties.pctPmpp
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.pctPmpp
```

````

````{py:attribute} pctR
:canonical: altdss.PVSystem.PVSystemBatchProperties.pctR
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.pctR
```

````

````{py:attribute} pctX
:canonical: altdss.PVSystem.PVSystemBatchProperties.pctX
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.pctX
```

````

````{py:method} pop()
:canonical: altdss.PVSystem.PVSystemBatchProperties.pop

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.PVSystem.PVSystemBatchProperties.popitem

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.PVSystem.PVSystemBatchProperties.setdefault

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.PVSystem.PVSystemBatchProperties.update

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.PVSystem.PVSystemBatchProperties.values

```{autodoc2-docstring} altdss.PVSystem.PVSystemBatchProperties.values
```

````

`````

`````{py:class} PVSystemProperties()
:canonical: altdss.PVSystem.PVSystemProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties
```

````{py:attribute} AmpLimit
:canonical: altdss.PVSystem.PVSystemProperties.AmpLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.AmpLimit
```

````

````{py:attribute} AmpLimitGain
:canonical: altdss.PVSystem.PVSystemProperties.AmpLimitGain
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.AmpLimitGain
```

````

````{py:attribute} Balanced
:canonical: altdss.PVSystem.PVSystemProperties.Balanced
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Balanced
```

````

````{py:attribute} BaseFreq
:canonical: altdss.PVSystem.PVSystemProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.PVSystem.PVSystemProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Bus1
```

````

````{py:attribute} Class
:canonical: altdss.PVSystem.PVSystemProperties.Class
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Class
```

````

````{py:attribute} Conn
:canonical: altdss.PVSystem.PVSystemProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Conn
```

````

````{py:attribute} ControlMode
:canonical: altdss.PVSystem.PVSystemProperties.ControlMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InverterControlMode]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.ControlMode
```

````

````{py:attribute} Daily
:canonical: altdss.PVSystem.PVSystemProperties.Daily
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Daily
```

````

````{py:attribute} DebugTrace
:canonical: altdss.PVSystem.PVSystemProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.DebugTrace
```

````

````{py:attribute} Duty
:canonical: altdss.PVSystem.PVSystemProperties.Duty
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Duty
```

````

````{py:attribute} DutyStart
:canonical: altdss.PVSystem.PVSystemProperties.DutyStart
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.DutyStart
```

````

````{py:attribute} DynOut
:canonical: altdss.PVSystem.PVSystemProperties.DynOut
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.DynOut
```

````

````{py:attribute} DynamicEq
:canonical: altdss.PVSystem.PVSystemProperties.DynamicEq
:type: typing.Union[typing.AnyStr, altdss.DynamicExp.DynamicExp]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.DynamicEq
```

````

````{py:attribute} EffCurve
:canonical: altdss.PVSystem.PVSystemProperties.EffCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.EffCurve
```

````

````{py:attribute} Enabled
:canonical: altdss.PVSystem.PVSystemProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Enabled
```

````

````{py:attribute} Irradiance
:canonical: altdss.PVSystem.PVSystemProperties.Irradiance
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Irradiance
```

````

````{py:attribute} Kp
:canonical: altdss.PVSystem.PVSystemProperties.Kp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Kp
```

````

````{py:attribute} Like
:canonical: altdss.PVSystem.PVSystemProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Like
```

````

````{py:attribute} LimitCurrent
:canonical: altdss.PVSystem.PVSystemProperties.LimitCurrent
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.LimitCurrent
```

````

````{py:attribute} Model
:canonical: altdss.PVSystem.PVSystemProperties.Model
:type: typing.Union[int, altdss.enums.PVSystemModel]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Model
```

````

````{py:attribute} PF
:canonical: altdss.PVSystem.PVSystemProperties.PF
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.PF
```

````

````{py:attribute} PFPriority
:canonical: altdss.PVSystem.PVSystemProperties.PFPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.PFPriority
```

````

````{py:attribute} PITol
:canonical: altdss.PVSystem.PVSystemProperties.PITol
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.PITol
```

````

````{py:attribute} PTCurve
:canonical: altdss.PVSystem.PVSystemProperties.PTCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.PTCurve
```

````

````{py:attribute} Phases
:canonical: altdss.PVSystem.PVSystemProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Phases
```

````

````{py:attribute} Pmpp
:canonical: altdss.PVSystem.PVSystemProperties.Pmpp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Pmpp
```

````

````{py:attribute} SafeMode
:canonical: altdss.PVSystem.PVSystemProperties.SafeMode
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.SafeMode
```

````

````{py:attribute} SafeVoltage
:canonical: altdss.PVSystem.PVSystemProperties.SafeVoltage
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.SafeVoltage
```

````

````{py:attribute} Spectrum
:canonical: altdss.PVSystem.PVSystemProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Spectrum
```

````

````{py:attribute} TDaily
:canonical: altdss.PVSystem.PVSystemProperties.TDaily
:type: typing.Union[typing.AnyStr, altdss.TShape.TShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.TDaily
```

````

````{py:attribute} TDuty
:canonical: altdss.PVSystem.PVSystemProperties.TDuty
:type: typing.Union[typing.AnyStr, altdss.TShape.TShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.TDuty
```

````

````{py:attribute} TYearly
:canonical: altdss.PVSystem.PVSystemProperties.TYearly
:type: typing.Union[typing.AnyStr, altdss.TShape.TShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.TYearly
```

````

````{py:attribute} Temperature
:canonical: altdss.PVSystem.PVSystemProperties.Temperature
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Temperature
```

````

````{py:attribute} UserData
:canonical: altdss.PVSystem.PVSystemProperties.UserData
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.PVSystem.PVSystemProperties.UserModel
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.UserModel
```

````

````{py:attribute} VMaxpu
:canonical: altdss.PVSystem.PVSystemProperties.VMaxpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.VMaxpu
```

````

````{py:attribute} VMinpu
:canonical: altdss.PVSystem.PVSystemProperties.VMinpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.VMinpu
```

````

````{py:attribute} VarFollowInverter
:canonical: altdss.PVSystem.PVSystemProperties.VarFollowInverter
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.VarFollowInverter
```

````

````{py:attribute} WattPriority
:canonical: altdss.PVSystem.PVSystemProperties.WattPriority
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.WattPriority
```

````

````{py:attribute} Yearly
:canonical: altdss.PVSystem.PVSystemProperties.Yearly
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.Yearly
```

````

````{py:method} __contains__()
:canonical: altdss.PVSystem.PVSystemProperties.__contains__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.PVSystem.PVSystemProperties.__delattr__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.PVSystem.PVSystemProperties.__delitem__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.PVSystem.PVSystemProperties.__dir__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.PVSystem.PVSystemProperties.__format__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.PVSystem.PVSystemProperties.__ge__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.PVSystem.PVSystemProperties.__getattribute__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.PVSystem.PVSystemProperties.__getitem__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.PVSystem.PVSystemProperties.__getstate__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.PVSystem.PVSystemProperties.__gt__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.PVSystem.PVSystemProperties.__init__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.PVSystem.PVSystemProperties.__ior__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.PVSystem.PVSystemProperties.__iter__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.PVSystem.PVSystemProperties.__le__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.PVSystem.PVSystemProperties.__len__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.PVSystem.PVSystemProperties.__lt__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.PVSystem.PVSystemProperties.__ne__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.PVSystem.PVSystemProperties.__new__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.PVSystem.PVSystemProperties.__or__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.PVSystem.PVSystemProperties.__reduce__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.PVSystem.PVSystemProperties.__reduce_ex__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.PVSystem.PVSystemProperties.__repr__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.PVSystem.PVSystemProperties.__reversed__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.PVSystem.PVSystemProperties.__ror__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.PVSystem.PVSystemProperties.__setitem__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.PVSystem.PVSystemProperties.__sizeof__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.PVSystem.PVSystemProperties.__str__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.PVSystem.PVSystemProperties.__subclasshook__

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.PVSystem.PVSystemProperties.clear

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.PVSystem.PVSystemProperties.copy

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.copy
```

````

````{py:method} get()
:canonical: altdss.PVSystem.PVSystemProperties.get

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.get
```

````

````{py:method} items()
:canonical: altdss.PVSystem.PVSystemProperties.items

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.PVSystem.PVSystemProperties.kV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.kV
```

````

````{py:attribute} kVA
:canonical: altdss.PVSystem.PVSystemProperties.kVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.kVA
```

````

````{py:attribute} kVDC
:canonical: altdss.PVSystem.PVSystemProperties.kVDC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.kVDC
```

````

````{py:method} keys()
:canonical: altdss.PVSystem.PVSystemProperties.keys

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.PVSystem.PVSystemProperties.kvar
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.kvar
```

````

````{py:attribute} kvarMax
:canonical: altdss.PVSystem.PVSystemProperties.kvarMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.kvarMax
```

````

````{py:attribute} kvarMaxAbs
:canonical: altdss.PVSystem.PVSystemProperties.kvarMaxAbs
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.kvarMaxAbs
```

````

````{py:attribute} pctCutIn
:canonical: altdss.PVSystem.PVSystemProperties.pctCutIn
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.pctCutIn
```

````

````{py:attribute} pctCutOut
:canonical: altdss.PVSystem.PVSystemProperties.pctCutOut
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.pctCutOut
```

````

````{py:attribute} pctPMinNoVars
:canonical: altdss.PVSystem.PVSystemProperties.pctPMinNoVars
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.pctPMinNoVars
```

````

````{py:attribute} pctPMinkvarMax
:canonical: altdss.PVSystem.PVSystemProperties.pctPMinkvarMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.pctPMinkvarMax
```

````

````{py:attribute} pctPmpp
:canonical: altdss.PVSystem.PVSystemProperties.pctPmpp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.pctPmpp
```

````

````{py:attribute} pctR
:canonical: altdss.PVSystem.PVSystemProperties.pctR
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.pctR
```

````

````{py:attribute} pctX
:canonical: altdss.PVSystem.PVSystemProperties.pctX
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.pctX
```

````

````{py:method} pop()
:canonical: altdss.PVSystem.PVSystemProperties.pop

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.PVSystem.PVSystemProperties.popitem

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.PVSystem.PVSystemProperties.setdefault

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.PVSystem.PVSystemProperties.update

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.update
```

````

````{py:method} values()
:canonical: altdss.PVSystem.PVSystemProperties.values

```{autodoc2-docstring} altdss.PVSystem.PVSystemProperties.values
```

````

`````
