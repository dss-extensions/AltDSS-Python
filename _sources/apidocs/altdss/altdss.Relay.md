# {py:mod}`altdss.Relay`

```{py:module} altdss.Relay
```

```{autodoc2-docstring} altdss.Relay
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IRelay <altdss.Relay.IRelay>`
  - ```{autodoc2-docstring} altdss.Relay.IRelay
    :summary:
    ```
* - {py:obj}`Relay <altdss.Relay.Relay>`
  - ```{autodoc2-docstring} altdss.Relay.Relay
    :summary:
    ```
* - {py:obj}`RelayBatch <altdss.Relay.RelayBatch>`
  - ```{autodoc2-docstring} altdss.Relay.RelayBatch
    :summary:
    ```
* - {py:obj}`RelayBatchProperties <altdss.Relay.RelayBatchProperties>`
  - ```{autodoc2-docstring} altdss.Relay.RelayBatchProperties
    :summary:
    ```
* - {py:obj}`RelayProperties <altdss.Relay.RelayProperties>`
  - ```{autodoc2-docstring} altdss.Relay.RelayProperties
    :summary:
    ```
````

### API

`````{py:class} IRelay(iobj)
:canonical: altdss.Relay.IRelay

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Relay.RelayBatch`

```{autodoc2-docstring} altdss.Relay.IRelay
```

````{py:attribute} Action
:canonical: altdss.Relay.IRelay.Action
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Action
```

````

````{py:attribute} Action_str
:canonical: altdss.Relay.IRelay.Action_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Action_str
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Relay.IRelay.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.BaseFreq
```

````

````{py:attribute} BreakerTime
:canonical: altdss.Relay.IRelay.BreakerTime
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.BreakerTime
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Relay.IRelay.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Relay.IRelay.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Relay.IRelay.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Relay.IRelay.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Relay.IRelay.Currents

```{autodoc2-docstring} altdss.Relay.IRelay.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Relay.IRelay.CurrentsMagAng

```{autodoc2-docstring} altdss.Relay.IRelay.CurrentsMagAng
```

````

````{py:attribute} DOC_DelayInner
:canonical: altdss.Relay.IRelay.DOC_DelayInner
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_DelayInner
```

````

````{py:attribute} DOC_P1Blocking
:canonical: altdss.Relay.IRelay.DOC_P1Blocking
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_P1Blocking
```

````

````{py:attribute} DOC_PhaseCurveInner
:canonical: altdss.Relay.IRelay.DOC_PhaseCurveInner
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_PhaseCurveInner
```

````

````{py:attribute} DOC_PhaseCurveInner_str
:canonical: altdss.Relay.IRelay.DOC_PhaseCurveInner_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_PhaseCurveInner_str
```

````

````{py:attribute} DOC_PhaseTripInner
:canonical: altdss.Relay.IRelay.DOC_PhaseTripInner
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_PhaseTripInner
```

````

````{py:attribute} DOC_TDPhaseInner
:canonical: altdss.Relay.IRelay.DOC_TDPhaseInner
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_TDPhaseInner
```

````

````{py:attribute} DOC_TiltAngleHigh
:canonical: altdss.Relay.IRelay.DOC_TiltAngleHigh
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_TiltAngleHigh
```

````

````{py:attribute} DOC_TiltAngleLow
:canonical: altdss.Relay.IRelay.DOC_TiltAngleLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_TiltAngleLow
```

````

````{py:attribute} DOC_TripSettingHigh
:canonical: altdss.Relay.IRelay.DOC_TripSettingHigh
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_TripSettingHigh
```

````

````{py:attribute} DOC_TripSettingLow
:canonical: altdss.Relay.IRelay.DOC_TripSettingLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_TripSettingLow
```

````

````{py:attribute} DOC_TripSettingMag
:canonical: altdss.Relay.IRelay.DOC_TripSettingMag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DOC_TripSettingMag
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Relay.IRelay.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.Relay.IRelay.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Delay
```

````

````{py:attribute} DistReverse
:canonical: altdss.Relay.IRelay.DistReverse
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.DistReverse
```

````

````{py:attribute} Enabled
:canonical: altdss.Relay.IRelay.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.Relay.IRelay.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.EventLog
```

````

````{py:attribute} F46BaseAmps
:canonical: altdss.Relay.IRelay.F46BaseAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.F46BaseAmps
```

````

````{py:attribute} F46isqt
:canonical: altdss.Relay.IRelay.F46isqt
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.F46isqt
```

````

````{py:attribute} F46pctPickup
:canonical: altdss.Relay.IRelay.F46pctPickup
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.F46pctPickup
```

````

````{py:attribute} F47pctPickup
:canonical: altdss.Relay.IRelay.F47pctPickup
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.F47pctPickup
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Relay.IRelay.FullName

```{autodoc2-docstring} altdss.Relay.IRelay.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Relay.IRelay.GUID

```{autodoc2-docstring} altdss.Relay.IRelay.GUID
```

````

````{py:attribute} GroundCurve
:canonical: altdss.Relay.IRelay.GroundCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.GroundCurve
```

````

````{py:attribute} GroundCurve_str
:canonical: altdss.Relay.IRelay.GroundCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.GroundCurve_str
```

````

````{py:attribute} GroundInst
:canonical: altdss.Relay.IRelay.GroundInst
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Relay.IRelay.GroundTrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.GroundTrip
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Relay.IRelay.Handle

```{autodoc2-docstring} altdss.Relay.IRelay.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Relay.IRelay.HasOCPDevice

```{autodoc2-docstring} altdss.Relay.IRelay.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Relay.IRelay.HasSwitchControl

```{autodoc2-docstring} altdss.Relay.IRelay.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Relay.IRelay.HasVoltControl

```{autodoc2-docstring} altdss.Relay.IRelay.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Relay.IRelay.IsIsolated

```{autodoc2-docstring} altdss.Relay.IRelay.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Relay.IRelay.Like

```{autodoc2-docstring} altdss.Relay.IRelay.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Relay.IRelay.Losses

```{autodoc2-docstring} altdss.Relay.IRelay.Losses
```

````

````{py:attribute} MGround
:canonical: altdss.Relay.IRelay.MGround
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.MGround
```

````

````{py:attribute} MPhase
:canonical: altdss.Relay.IRelay.MPhase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.MPhase
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Relay.IRelay.MaxCurrent

```{autodoc2-docstring} altdss.Relay.IRelay.MaxCurrent
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Relay.IRelay.MonitoredObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.MonitoredObj
```

````

````{py:attribute} MonitoredObj_str
:canonical: altdss.Relay.IRelay.MonitoredObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.MonitoredObj_str
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Relay.IRelay.MonitoredTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.MonitoredTerm
```

````

````{py:property} Name
:canonical: altdss.Relay.IRelay.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Relay.IRelay.Name
```

````

````{py:attribute} Normal
:canonical: altdss.Relay.IRelay.Normal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.Relay.IRelay.Normal_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Normal_str
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Relay.IRelay.NumConductors

```{autodoc2-docstring} altdss.Relay.IRelay.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Relay.IRelay.NumControllers

```{autodoc2-docstring} altdss.Relay.IRelay.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Relay.IRelay.NumPhases

```{autodoc2-docstring} altdss.Relay.IRelay.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Relay.IRelay.NumTerminals

```{autodoc2-docstring} altdss.Relay.IRelay.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Relay.IRelay.OCPDevice

```{autodoc2-docstring} altdss.Relay.IRelay.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Relay.IRelay.OCPDeviceIndex

```{autodoc2-docstring} altdss.Relay.IRelay.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Relay.IRelay.OCPDeviceType

```{autodoc2-docstring} altdss.Relay.IRelay.OCPDeviceType
```

````

````{py:attribute} Overtrip
:canonical: altdss.Relay.IRelay.Overtrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Overtrip
```

````

````{py:attribute} OvervoltCurve
:canonical: altdss.Relay.IRelay.OvervoltCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.OvervoltCurve
```

````

````{py:attribute} OvervoltCurve_str
:canonical: altdss.Relay.IRelay.OvervoltCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.OvervoltCurve_str
```

````

````{py:attribute} PhaseCurve
:canonical: altdss.Relay.IRelay.PhaseCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.PhaseCurve
```

````

````{py:attribute} PhaseCurve_str
:canonical: altdss.Relay.IRelay.PhaseCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.PhaseCurve_str
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Relay.IRelay.PhaseInst
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.PhaseInst
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Relay.IRelay.PhaseLosses

```{autodoc2-docstring} altdss.Relay.IRelay.PhaseLosses
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Relay.IRelay.PhaseTrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.PhaseTrip
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Relay.IRelay.Powers

```{autodoc2-docstring} altdss.Relay.IRelay.Powers
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Relay.IRelay.RecloseIntervals
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Relay.IRelay.Reset
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Reset
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Relay.IRelay.SeqCurrents

```{autodoc2-docstring} altdss.Relay.IRelay.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Relay.IRelay.SeqPowers

```{autodoc2-docstring} altdss.Relay.IRelay.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Relay.IRelay.SeqVoltages

```{autodoc2-docstring} altdss.Relay.IRelay.SeqVoltages
```

````

````{py:attribute} Shots
:canonical: altdss.Relay.IRelay.Shots
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Shots
```

````

````{py:attribute} State
:canonical: altdss.Relay.IRelay.State
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.State
```

````

````{py:attribute} State_str
:canonical: altdss.Relay.IRelay.State_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Relay.IRelay.SwitchedObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.Relay.IRelay.SwitchedObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Relay.IRelay.SwitchedTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.SwitchedTerm
```

````

````{py:attribute} TDGround
:canonical: altdss.Relay.IRelay.TDGround
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.TDGround
```

````

````{py:attribute} TDPhase
:canonical: altdss.Relay.IRelay.TDPhase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.TDPhase
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Relay.IRelay.TotalPowers

```{autodoc2-docstring} altdss.Relay.IRelay.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.Relay.IRelay.Type
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.Relay.IRelay.Type_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Type_str
```

````

````{py:attribute} Undertrip
:canonical: altdss.Relay.IRelay.Undertrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Undertrip
```

````

````{py:attribute} UndervoltCurve
:canonical: altdss.Relay.IRelay.UndervoltCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.UndervoltCurve
```

````

````{py:attribute} UndervoltCurve_str
:canonical: altdss.Relay.IRelay.UndervoltCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.UndervoltCurve_str
```

````

````{py:attribute} Variable
:canonical: altdss.Relay.IRelay.Variable
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Variable
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Relay.IRelay.Voltages

```{autodoc2-docstring} altdss.Relay.IRelay.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Relay.IRelay.VoltagesMagAng

```{autodoc2-docstring} altdss.Relay.IRelay.VoltagesMagAng
```

````

````{py:attribute} Z0Ang
:canonical: altdss.Relay.IRelay.Z0Ang
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Z0Ang
```

````

````{py:attribute} Z0Mag
:canonical: altdss.Relay.IRelay.Z0Mag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Z0Mag
```

````

````{py:attribute} Z1Ang
:canonical: altdss.Relay.IRelay.Z1Ang
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Z1Ang
```

````

````{py:attribute} Z1Mag
:canonical: altdss.Relay.IRelay.Z1Mag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.Z1Mag
```

````

````{py:method} __call__()
:canonical: altdss.Relay.IRelay.__call__

```{autodoc2-docstring} altdss.Relay.IRelay.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Relay.IRelay.__contains__

```{autodoc2-docstring} altdss.Relay.IRelay.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Relay.IRelay.__getitem__

```{autodoc2-docstring} altdss.Relay.IRelay.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Relay.IRelay.__init__

```{autodoc2-docstring} altdss.Relay.IRelay.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Relay.IRelay.__iter__

```{autodoc2-docstring} altdss.Relay.IRelay.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Relay.IRelay.__len__

```{autodoc2-docstring} altdss.Relay.IRelay.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Relay.IRelay.batch

```{autodoc2-docstring} altdss.Relay.IRelay.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Relay.RelayBatchProperties]) -> altdss.Relay.RelayBatch
:canonical: altdss.Relay.IRelay.batch_new

```{autodoc2-docstring} altdss.Relay.IRelay.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Relay.IRelay.begin_edit

```{autodoc2-docstring} altdss.Relay.IRelay.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Relay.IRelay.end_edit

```{autodoc2-docstring} altdss.Relay.IRelay.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Relay.IRelay.find

```{autodoc2-docstring} altdss.Relay.IRelay.find
```

````

````{py:attribute} kVBase
:canonical: altdss.Relay.IRelay.kVBase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.IRelay.kVBase
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Relay.RelayProperties]) -> altdss.Relay.Relay
:canonical: altdss.Relay.IRelay.new

```{autodoc2-docstring} altdss.Relay.IRelay.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Relay.IRelay.to_json

```{autodoc2-docstring} altdss.Relay.IRelay.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Relay.IRelay.to_list

```{autodoc2-docstring} altdss.Relay.IRelay.to_list
```

````

`````

`````{py:class} Relay(api_util, ptr)
:canonical: altdss.Relay.Relay

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.Relay.Relay
```

````{py:attribute} Action
:canonical: altdss.Relay.Relay.Action
:type: altdss.enums.RelayAction
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Action
```

````

````{py:attribute} Action_str
:canonical: altdss.Relay.Relay.Action_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Action_str
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Relay.Relay.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.BaseFreq
```

````

````{py:attribute} BreakerTime
:canonical: altdss.Relay.Relay.BreakerTime
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.BreakerTime
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Relay.Relay.Close

```{autodoc2-docstring} altdss.Relay.Relay.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Relay.Relay.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Relay.Relay.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Relay.Relay.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Relay.Relay.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Relay.Relay.Currents

```{autodoc2-docstring} altdss.Relay.Relay.Currents
```

````

````{py:attribute} DOC_DelayInner
:canonical: altdss.Relay.Relay.DOC_DelayInner
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_DelayInner
```

````

````{py:attribute} DOC_P1Blocking
:canonical: altdss.Relay.Relay.DOC_P1Blocking
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_P1Blocking
```

````

````{py:attribute} DOC_PhaseCurveInner
:canonical: altdss.Relay.Relay.DOC_PhaseCurveInner
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_PhaseCurveInner
```

````

````{py:attribute} DOC_PhaseCurveInner_str
:canonical: altdss.Relay.Relay.DOC_PhaseCurveInner_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_PhaseCurveInner_str
```

````

````{py:attribute} DOC_PhaseTripInner
:canonical: altdss.Relay.Relay.DOC_PhaseTripInner
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_PhaseTripInner
```

````

````{py:attribute} DOC_TDPhaseInner
:canonical: altdss.Relay.Relay.DOC_TDPhaseInner
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_TDPhaseInner
```

````

````{py:attribute} DOC_TiltAngleHigh
:canonical: altdss.Relay.Relay.DOC_TiltAngleHigh
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_TiltAngleHigh
```

````

````{py:attribute} DOC_TiltAngleLow
:canonical: altdss.Relay.Relay.DOC_TiltAngleLow
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_TiltAngleLow
```

````

````{py:attribute} DOC_TripSettingHigh
:canonical: altdss.Relay.Relay.DOC_TripSettingHigh
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_TripSettingHigh
```

````

````{py:attribute} DOC_TripSettingLow
:canonical: altdss.Relay.Relay.DOC_TripSettingLow
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_TripSettingLow
```

````

````{py:attribute} DOC_TripSettingMag
:canonical: altdss.Relay.Relay.DOC_TripSettingMag
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DOC_TripSettingMag
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Relay.Relay.DebugTrace
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.Relay.Relay.Delay
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Delay
```

````

````{py:attribute} DisplayName
:canonical: altdss.Relay.Relay.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DisplayName
```

````

````{py:attribute} DistReverse
:canonical: altdss.Relay.Relay.DistReverse
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.DistReverse
```

````

````{py:attribute} Enabled
:canonical: altdss.Relay.Relay.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.Relay.Relay.EventLog
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.EventLog
```

````

````{py:attribute} F46BaseAmps
:canonical: altdss.Relay.Relay.F46BaseAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.F46BaseAmps
```

````

````{py:attribute} F46isqt
:canonical: altdss.Relay.Relay.F46isqt
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.F46isqt
```

````

````{py:attribute} F46pctPickup
:canonical: altdss.Relay.Relay.F46pctPickup
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.F46pctPickup
```

````

````{py:attribute} F47pctPickup
:canonical: altdss.Relay.Relay.F47pctPickup
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.F47pctPickup
```

````

````{py:method} FullName() -> str
:canonical: altdss.Relay.Relay.FullName

```{autodoc2-docstring} altdss.Relay.Relay.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Relay.Relay.GUID

```{autodoc2-docstring} altdss.Relay.Relay.GUID
```

````

````{py:attribute} GroundCurve
:canonical: altdss.Relay.Relay.GroundCurve
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.GroundCurve
```

````

````{py:attribute} GroundCurve_str
:canonical: altdss.Relay.Relay.GroundCurve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.GroundCurve_str
```

````

````{py:attribute} GroundInst
:canonical: altdss.Relay.Relay.GroundInst
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Relay.Relay.GroundTrip
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.GroundTrip
```

````

````{py:method} Handle() -> int
:canonical: altdss.Relay.Relay.Handle

```{autodoc2-docstring} altdss.Relay.Relay.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Relay.Relay.HasOCPDevice

```{autodoc2-docstring} altdss.Relay.Relay.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Relay.Relay.HasSwitchControl

```{autodoc2-docstring} altdss.Relay.Relay.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Relay.Relay.HasVoltControl

```{autodoc2-docstring} altdss.Relay.Relay.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Relay.Relay.IsIsolated

```{autodoc2-docstring} altdss.Relay.Relay.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Relay.Relay.IsOpen

```{autodoc2-docstring} altdss.Relay.Relay.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Relay.Relay.Like

```{autodoc2-docstring} altdss.Relay.Relay.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Relay.Relay.Losses

```{autodoc2-docstring} altdss.Relay.Relay.Losses
```

````

````{py:attribute} MGround
:canonical: altdss.Relay.Relay.MGround
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.MGround
```

````

````{py:attribute} MPhase
:canonical: altdss.Relay.Relay.MPhase
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.MPhase
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Relay.Relay.MaxCurrent

```{autodoc2-docstring} altdss.Relay.Relay.MaxCurrent
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Relay.Relay.MonitoredObj
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.MonitoredObj
```

````

````{py:attribute} MonitoredObj_str
:canonical: altdss.Relay.Relay.MonitoredObj_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.MonitoredObj_str
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Relay.Relay.MonitoredTerm
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.MonitoredTerm
```

````

````{py:property} Name
:canonical: altdss.Relay.Relay.Name
:type: str

```{autodoc2-docstring} altdss.Relay.Relay.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Relay.Relay.NodeOrder

```{autodoc2-docstring} altdss.Relay.Relay.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Relay.Relay.NodeRef

```{autodoc2-docstring} altdss.Relay.Relay.NodeRef
```

````

````{py:attribute} Normal
:canonical: altdss.Relay.Relay.Normal
:type: altdss.enums.RelayState
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.Relay.Relay.Normal_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Normal_str
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Relay.Relay.NumConductors

```{autodoc2-docstring} altdss.Relay.Relay.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Relay.Relay.NumControllers

```{autodoc2-docstring} altdss.Relay.Relay.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Relay.Relay.NumPhases

```{autodoc2-docstring} altdss.Relay.Relay.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Relay.Relay.NumTerminals

```{autodoc2-docstring} altdss.Relay.Relay.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Relay.Relay.OCPDevice

```{autodoc2-docstring} altdss.Relay.Relay.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Relay.Relay.OCPDeviceIndex

```{autodoc2-docstring} altdss.Relay.Relay.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Relay.Relay.OCPDeviceType

```{autodoc2-docstring} altdss.Relay.Relay.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Relay.Relay.Open

```{autodoc2-docstring} altdss.Relay.Relay.Open
```

````

````{py:attribute} Overtrip
:canonical: altdss.Relay.Relay.Overtrip
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Overtrip
```

````

````{py:attribute} OvervoltCurve
:canonical: altdss.Relay.Relay.OvervoltCurve
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.OvervoltCurve
```

````

````{py:attribute} OvervoltCurve_str
:canonical: altdss.Relay.Relay.OvervoltCurve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.OvervoltCurve_str
```

````

````{py:attribute} PhaseCurve
:canonical: altdss.Relay.Relay.PhaseCurve
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.PhaseCurve
```

````

````{py:attribute} PhaseCurve_str
:canonical: altdss.Relay.Relay.PhaseCurve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.PhaseCurve_str
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Relay.Relay.PhaseInst
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.PhaseInst
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Relay.Relay.PhaseLosses

```{autodoc2-docstring} altdss.Relay.Relay.PhaseLosses
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Relay.Relay.PhaseTrip
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.PhaseTrip
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Relay.Relay.Powers

```{autodoc2-docstring} altdss.Relay.Relay.Powers
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Relay.Relay.RecloseIntervals
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Relay.Relay.Reset
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Reset
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Relay.Relay.Residuals

```{autodoc2-docstring} altdss.Relay.Relay.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Relay.Relay.SeqCurrents

```{autodoc2-docstring} altdss.Relay.Relay.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Relay.Relay.SeqPowers

```{autodoc2-docstring} altdss.Relay.Relay.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Relay.Relay.SeqVoltages

```{autodoc2-docstring} altdss.Relay.Relay.SeqVoltages
```

````

````{py:attribute} Shots
:canonical: altdss.Relay.Relay.Shots
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Shots
```

````

````{py:attribute} State
:canonical: altdss.Relay.Relay.State
:type: altdss.enums.RelayState
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.State
```

````

````{py:attribute} State_str
:canonical: altdss.Relay.Relay.State_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Relay.Relay.SwitchedObj
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.Relay.Relay.SwitchedObj_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Relay.Relay.SwitchedTerm
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.SwitchedTerm
```

````

````{py:attribute} TDGround
:canonical: altdss.Relay.Relay.TDGround
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.TDGround
```

````

````{py:attribute} TDPhase
:canonical: altdss.Relay.Relay.TDPhase
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.TDPhase
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Relay.Relay.TotalPowers

```{autodoc2-docstring} altdss.Relay.Relay.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.Relay.Relay.Type
:type: altdss.enums.RelayType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.Relay.Relay.Type_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Type_str
```

````

````{py:attribute} Undertrip
:canonical: altdss.Relay.Relay.Undertrip
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Undertrip
```

````

````{py:attribute} UndervoltCurve
:canonical: altdss.Relay.Relay.UndervoltCurve
:type: altdss.TCC_Curve.TCC_Curve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.UndervoltCurve
```

````

````{py:attribute} UndervoltCurve_str
:canonical: altdss.Relay.Relay.UndervoltCurve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.UndervoltCurve_str
```

````

````{py:attribute} Variable
:canonical: altdss.Relay.Relay.Variable
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Variable
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Relay.Relay.Voltages

```{autodoc2-docstring} altdss.Relay.Relay.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Relay.Relay.VoltagesMagAng

```{autodoc2-docstring} altdss.Relay.Relay.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Relay.Relay.YPrim

```{autodoc2-docstring} altdss.Relay.Relay.YPrim
```

````

````{py:attribute} Z0Ang
:canonical: altdss.Relay.Relay.Z0Ang
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Z0Ang
```

````

````{py:attribute} Z0Mag
:canonical: altdss.Relay.Relay.Z0Mag
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Z0Mag
```

````

````{py:attribute} Z1Ang
:canonical: altdss.Relay.Relay.Z1Ang
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Z1Ang
```

````

````{py:attribute} Z1Mag
:canonical: altdss.Relay.Relay.Z1Mag
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.Z1Mag
```

````

````{py:method} __hash__()
:canonical: altdss.Relay.Relay.__hash__

```{autodoc2-docstring} altdss.Relay.Relay.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Relay.Relay.__init__

```{autodoc2-docstring} altdss.Relay.Relay.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Relay.Relay.__ne__

```{autodoc2-docstring} altdss.Relay.Relay.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Relay.Relay.__repr__

```{autodoc2-docstring} altdss.Relay.Relay.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Relay.Relay.begin_edit

```{autodoc2-docstring} altdss.Relay.Relay.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Relay.Relay.end_edit

```{autodoc2-docstring} altdss.Relay.Relay.end_edit
```

````

````{py:attribute} kVBase
:canonical: altdss.Relay.Relay.kVBase
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.Relay.kVBase
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Relay.Relay.to_json

```{autodoc2-docstring} altdss.Relay.Relay.to_json
```

````

`````

`````{py:class} RelayBatch(api_util, **kwargs)
:canonical: altdss.Relay.RelayBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.Relay.RelayBatch
```

````{py:attribute} Action
:canonical: altdss.Relay.RelayBatch.Action
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Action
```

````

````{py:attribute} Action_str
:canonical: altdss.Relay.RelayBatch.Action_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Action_str
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Relay.RelayBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.BaseFreq
```

````

````{py:attribute} BreakerTime
:canonical: altdss.Relay.RelayBatch.BreakerTime
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.BreakerTime
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Relay.RelayBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Relay.RelayBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Relay.RelayBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Relay.RelayBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Relay.RelayBatch.Currents

```{autodoc2-docstring} altdss.Relay.RelayBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Relay.RelayBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Relay.RelayBatch.CurrentsMagAng
```

````

````{py:attribute} DOC_DelayInner
:canonical: altdss.Relay.RelayBatch.DOC_DelayInner
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_DelayInner
```

````

````{py:attribute} DOC_P1Blocking
:canonical: altdss.Relay.RelayBatch.DOC_P1Blocking
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_P1Blocking
```

````

````{py:attribute} DOC_PhaseCurveInner
:canonical: altdss.Relay.RelayBatch.DOC_PhaseCurveInner
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_PhaseCurveInner
```

````

````{py:attribute} DOC_PhaseCurveInner_str
:canonical: altdss.Relay.RelayBatch.DOC_PhaseCurveInner_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_PhaseCurveInner_str
```

````

````{py:attribute} DOC_PhaseTripInner
:canonical: altdss.Relay.RelayBatch.DOC_PhaseTripInner
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_PhaseTripInner
```

````

````{py:attribute} DOC_TDPhaseInner
:canonical: altdss.Relay.RelayBatch.DOC_TDPhaseInner
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_TDPhaseInner
```

````

````{py:attribute} DOC_TiltAngleHigh
:canonical: altdss.Relay.RelayBatch.DOC_TiltAngleHigh
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_TiltAngleHigh
```

````

````{py:attribute} DOC_TiltAngleLow
:canonical: altdss.Relay.RelayBatch.DOC_TiltAngleLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_TiltAngleLow
```

````

````{py:attribute} DOC_TripSettingHigh
:canonical: altdss.Relay.RelayBatch.DOC_TripSettingHigh
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_TripSettingHigh
```

````

````{py:attribute} DOC_TripSettingLow
:canonical: altdss.Relay.RelayBatch.DOC_TripSettingLow
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_TripSettingLow
```

````

````{py:attribute} DOC_TripSettingMag
:canonical: altdss.Relay.RelayBatch.DOC_TripSettingMag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DOC_TripSettingMag
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Relay.RelayBatch.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.Relay.RelayBatch.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Delay
```

````

````{py:attribute} DistReverse
:canonical: altdss.Relay.RelayBatch.DistReverse
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.DistReverse
```

````

````{py:attribute} Enabled
:canonical: altdss.Relay.RelayBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.Relay.RelayBatch.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.EventLog
```

````

````{py:attribute} F46BaseAmps
:canonical: altdss.Relay.RelayBatch.F46BaseAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.F46BaseAmps
```

````

````{py:attribute} F46isqt
:canonical: altdss.Relay.RelayBatch.F46isqt
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.F46isqt
```

````

````{py:attribute} F46pctPickup
:canonical: altdss.Relay.RelayBatch.F46pctPickup
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.F46pctPickup
```

````

````{py:attribute} F47pctPickup
:canonical: altdss.Relay.RelayBatch.F47pctPickup
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.F47pctPickup
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Relay.RelayBatch.FullName

```{autodoc2-docstring} altdss.Relay.RelayBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Relay.RelayBatch.GUID

```{autodoc2-docstring} altdss.Relay.RelayBatch.GUID
```

````

````{py:attribute} GroundCurve
:canonical: altdss.Relay.RelayBatch.GroundCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.GroundCurve
```

````

````{py:attribute} GroundCurve_str
:canonical: altdss.Relay.RelayBatch.GroundCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.GroundCurve_str
```

````

````{py:attribute} GroundInst
:canonical: altdss.Relay.RelayBatch.GroundInst
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Relay.RelayBatch.GroundTrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.GroundTrip
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Relay.RelayBatch.Handle

```{autodoc2-docstring} altdss.Relay.RelayBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Relay.RelayBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Relay.RelayBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Relay.RelayBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Relay.RelayBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Relay.RelayBatch.HasVoltControl

```{autodoc2-docstring} altdss.Relay.RelayBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Relay.RelayBatch.IsIsolated

```{autodoc2-docstring} altdss.Relay.RelayBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Relay.RelayBatch.Like

```{autodoc2-docstring} altdss.Relay.RelayBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Relay.RelayBatch.Losses

```{autodoc2-docstring} altdss.Relay.RelayBatch.Losses
```

````

````{py:attribute} MGround
:canonical: altdss.Relay.RelayBatch.MGround
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.MGround
```

````

````{py:attribute} MPhase
:canonical: altdss.Relay.RelayBatch.MPhase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.MPhase
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Relay.RelayBatch.MaxCurrent

```{autodoc2-docstring} altdss.Relay.RelayBatch.MaxCurrent
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Relay.RelayBatch.MonitoredObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.MonitoredObj
```

````

````{py:attribute} MonitoredObj_str
:canonical: altdss.Relay.RelayBatch.MonitoredObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.MonitoredObj_str
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Relay.RelayBatch.MonitoredTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.MonitoredTerm
```

````

````{py:property} Name
:canonical: altdss.Relay.RelayBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Relay.RelayBatch.Name
```

````

````{py:attribute} Normal
:canonical: altdss.Relay.RelayBatch.Normal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Normal
```

````

````{py:attribute} Normal_str
:canonical: altdss.Relay.RelayBatch.Normal_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Normal_str
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Relay.RelayBatch.NumConductors

```{autodoc2-docstring} altdss.Relay.RelayBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Relay.RelayBatch.NumControllers

```{autodoc2-docstring} altdss.Relay.RelayBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Relay.RelayBatch.NumPhases

```{autodoc2-docstring} altdss.Relay.RelayBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Relay.RelayBatch.NumTerminals

```{autodoc2-docstring} altdss.Relay.RelayBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Relay.RelayBatch.OCPDevice

```{autodoc2-docstring} altdss.Relay.RelayBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Relay.RelayBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Relay.RelayBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Relay.RelayBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Relay.RelayBatch.OCPDeviceType
```

````

````{py:attribute} Overtrip
:canonical: altdss.Relay.RelayBatch.Overtrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Overtrip
```

````

````{py:attribute} OvervoltCurve
:canonical: altdss.Relay.RelayBatch.OvervoltCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.OvervoltCurve
```

````

````{py:attribute} OvervoltCurve_str
:canonical: altdss.Relay.RelayBatch.OvervoltCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.OvervoltCurve_str
```

````

````{py:attribute} PhaseCurve
:canonical: altdss.Relay.RelayBatch.PhaseCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.PhaseCurve
```

````

````{py:attribute} PhaseCurve_str
:canonical: altdss.Relay.RelayBatch.PhaseCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.PhaseCurve_str
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Relay.RelayBatch.PhaseInst
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.PhaseInst
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Relay.RelayBatch.PhaseLosses

```{autodoc2-docstring} altdss.Relay.RelayBatch.PhaseLosses
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Relay.RelayBatch.PhaseTrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.PhaseTrip
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Relay.RelayBatch.Powers

```{autodoc2-docstring} altdss.Relay.RelayBatch.Powers
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Relay.RelayBatch.RecloseIntervals
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Relay.RelayBatch.Reset
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Reset
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Relay.RelayBatch.SeqCurrents

```{autodoc2-docstring} altdss.Relay.RelayBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Relay.RelayBatch.SeqPowers

```{autodoc2-docstring} altdss.Relay.RelayBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Relay.RelayBatch.SeqVoltages

```{autodoc2-docstring} altdss.Relay.RelayBatch.SeqVoltages
```

````

````{py:attribute} Shots
:canonical: altdss.Relay.RelayBatch.Shots
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Shots
```

````

````{py:attribute} State
:canonical: altdss.Relay.RelayBatch.State
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.State
```

````

````{py:attribute} State_str
:canonical: altdss.Relay.RelayBatch.State_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.State_str
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Relay.RelayBatch.SwitchedObj
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.SwitchedObj
```

````

````{py:attribute} SwitchedObj_str
:canonical: altdss.Relay.RelayBatch.SwitchedObj_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.SwitchedObj_str
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Relay.RelayBatch.SwitchedTerm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.SwitchedTerm
```

````

````{py:attribute} TDGround
:canonical: altdss.Relay.RelayBatch.TDGround
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.TDGround
```

````

````{py:attribute} TDPhase
:canonical: altdss.Relay.RelayBatch.TDPhase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.TDPhase
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Relay.RelayBatch.TotalPowers

```{autodoc2-docstring} altdss.Relay.RelayBatch.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.Relay.RelayBatch.Type
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.Relay.RelayBatch.Type_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Type_str
```

````

````{py:attribute} Undertrip
:canonical: altdss.Relay.RelayBatch.Undertrip
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Undertrip
```

````

````{py:attribute} UndervoltCurve
:canonical: altdss.Relay.RelayBatch.UndervoltCurve
:type: typing.List[altdss.TCC_Curve.TCC_Curve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.UndervoltCurve
```

````

````{py:attribute} UndervoltCurve_str
:canonical: altdss.Relay.RelayBatch.UndervoltCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.UndervoltCurve_str
```

````

````{py:attribute} Variable
:canonical: altdss.Relay.RelayBatch.Variable
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Variable
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Relay.RelayBatch.Voltages

```{autodoc2-docstring} altdss.Relay.RelayBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Relay.RelayBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Relay.RelayBatch.VoltagesMagAng
```

````

````{py:attribute} Z0Ang
:canonical: altdss.Relay.RelayBatch.Z0Ang
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Z0Ang
```

````

````{py:attribute} Z0Mag
:canonical: altdss.Relay.RelayBatch.Z0Mag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Z0Mag
```

````

````{py:attribute} Z1Ang
:canonical: altdss.Relay.RelayBatch.Z1Ang
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Z1Ang
```

````

````{py:attribute} Z1Mag
:canonical: altdss.Relay.RelayBatch.Z1Mag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.Z1Mag
```

````

````{py:method} __call__()
:canonical: altdss.Relay.RelayBatch.__call__

```{autodoc2-docstring} altdss.Relay.RelayBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Relay.RelayBatch.__getitem__

```{autodoc2-docstring} altdss.Relay.RelayBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Relay.RelayBatch.__init__

```{autodoc2-docstring} altdss.Relay.RelayBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Relay.RelayBatch.__iter__

```{autodoc2-docstring} altdss.Relay.RelayBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Relay.RelayBatch.__len__

```{autodoc2-docstring} altdss.Relay.RelayBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Relay.RelayBatch.begin_edit

```{autodoc2-docstring} altdss.Relay.RelayBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Relay.RelayBatch.end_edit

```{autodoc2-docstring} altdss.Relay.RelayBatch.end_edit
```

````

````{py:attribute} kVBase
:canonical: altdss.Relay.RelayBatch.kVBase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Relay.RelayBatch.kVBase
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Relay.RelayBatch.to_json

```{autodoc2-docstring} altdss.Relay.RelayBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Relay.RelayBatch.to_list

```{autodoc2-docstring} altdss.Relay.RelayBatch.to_list
```

````

`````

`````{py:class} RelayBatchProperties()
:canonical: altdss.Relay.RelayBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties
```

````{py:attribute} Action
:canonical: altdss.Relay.RelayBatchProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.RelayAction, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.RelayAction], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Relay.RelayBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.BaseFreq
```

````

````{py:attribute} BreakerTime
:canonical: altdss.Relay.RelayBatchProperties.BreakerTime
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.BreakerTime
```

````

````{py:attribute} DOC_DelayInner
:canonical: altdss.Relay.RelayBatchProperties.DOC_DelayInner
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_DelayInner
```

````

````{py:attribute} DOC_P1Blocking
:canonical: altdss.Relay.RelayBatchProperties.DOC_P1Blocking
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_P1Blocking
```

````

````{py:attribute} DOC_PhaseCurveInner
:canonical: altdss.Relay.RelayBatchProperties.DOC_PhaseCurveInner
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_PhaseCurveInner
```

````

````{py:attribute} DOC_PhaseTripInner
:canonical: altdss.Relay.RelayBatchProperties.DOC_PhaseTripInner
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_PhaseTripInner
```

````

````{py:attribute} DOC_TDPhaseInner
:canonical: altdss.Relay.RelayBatchProperties.DOC_TDPhaseInner
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_TDPhaseInner
```

````

````{py:attribute} DOC_TiltAngleHigh
:canonical: altdss.Relay.RelayBatchProperties.DOC_TiltAngleHigh
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_TiltAngleHigh
```

````

````{py:attribute} DOC_TiltAngleLow
:canonical: altdss.Relay.RelayBatchProperties.DOC_TiltAngleLow
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_TiltAngleLow
```

````

````{py:attribute} DOC_TripSettingHigh
:canonical: altdss.Relay.RelayBatchProperties.DOC_TripSettingHigh
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_TripSettingHigh
```

````

````{py:attribute} DOC_TripSettingLow
:canonical: altdss.Relay.RelayBatchProperties.DOC_TripSettingLow
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_TripSettingLow
```

````

````{py:attribute} DOC_TripSettingMag
:canonical: altdss.Relay.RelayBatchProperties.DOC_TripSettingMag
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DOC_TripSettingMag
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Relay.RelayBatchProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.Relay.RelayBatchProperties.Delay
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Delay
```

````

````{py:attribute} DistReverse
:canonical: altdss.Relay.RelayBatchProperties.DistReverse
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.DistReverse
```

````

````{py:attribute} Enabled
:canonical: altdss.Relay.RelayBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.Relay.RelayBatchProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.EventLog
```

````

````{py:attribute} F46BaseAmps
:canonical: altdss.Relay.RelayBatchProperties.F46BaseAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.F46BaseAmps
```

````

````{py:attribute} F46isqt
:canonical: altdss.Relay.RelayBatchProperties.F46isqt
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.F46isqt
```

````

````{py:attribute} F46pctPickup
:canonical: altdss.Relay.RelayBatchProperties.F46pctPickup
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.F46pctPickup
```

````

````{py:attribute} F47pctPickup
:canonical: altdss.Relay.RelayBatchProperties.F47pctPickup
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.F47pctPickup
```

````

````{py:attribute} GroundCurve
:canonical: altdss.Relay.RelayBatchProperties.GroundCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.GroundCurve
```

````

````{py:attribute} GroundInst
:canonical: altdss.Relay.RelayBatchProperties.GroundInst
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Relay.RelayBatchProperties.GroundTrip
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.GroundTrip
```

````

````{py:attribute} Like
:canonical: altdss.Relay.RelayBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Like
```

````

````{py:attribute} MGround
:canonical: altdss.Relay.RelayBatchProperties.MGround
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.MGround
```

````

````{py:attribute} MPhase
:canonical: altdss.Relay.RelayBatchProperties.MPhase
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.MPhase
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Relay.RelayBatchProperties.MonitoredObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.MonitoredObj
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Relay.RelayBatchProperties.MonitoredTerm
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.MonitoredTerm
```

````

````{py:attribute} Normal
:canonical: altdss.Relay.RelayBatchProperties.Normal
:type: typing.Union[typing.AnyStr, int, altdss.enums.RelayState, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.RelayState], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Normal
```

````

````{py:attribute} Overtrip
:canonical: altdss.Relay.RelayBatchProperties.Overtrip
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Overtrip
```

````

````{py:attribute} OvervoltCurve
:canonical: altdss.Relay.RelayBatchProperties.OvervoltCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.OvervoltCurve
```

````

````{py:attribute} PhaseCurve
:canonical: altdss.Relay.RelayBatchProperties.PhaseCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.PhaseCurve
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Relay.RelayBatchProperties.PhaseInst
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.PhaseInst
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Relay.RelayBatchProperties.PhaseTrip
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.PhaseTrip
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Relay.RelayBatchProperties.RecloseIntervals
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Relay.RelayBatchProperties.Reset
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Reset
```

````

````{py:attribute} Shots
:canonical: altdss.Relay.RelayBatchProperties.Shots
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Shots
```

````

````{py:attribute} State
:canonical: altdss.Relay.RelayBatchProperties.State
:type: typing.Union[typing.AnyStr, int, altdss.enums.RelayState, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.RelayState], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.State
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Relay.RelayBatchProperties.SwitchedObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.SwitchedObj
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Relay.RelayBatchProperties.SwitchedTerm
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.SwitchedTerm
```

````

````{py:attribute} TDGround
:canonical: altdss.Relay.RelayBatchProperties.TDGround
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.TDGround
```

````

````{py:attribute} TDPhase
:canonical: altdss.Relay.RelayBatchProperties.TDPhase
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.TDPhase
```

````

````{py:attribute} Type
:canonical: altdss.Relay.RelayBatchProperties.Type
:type: typing.Union[typing.AnyStr, int, altdss.enums.RelayType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.RelayType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Type
```

````

````{py:attribute} Undertrip
:canonical: altdss.Relay.RelayBatchProperties.Undertrip
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Undertrip
```

````

````{py:attribute} UndervoltCurve
:canonical: altdss.Relay.RelayBatchProperties.UndervoltCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve, typing.List[typing.AnyStr], typing.List[altdss.TCC_Curve.TCC_Curve]]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.UndervoltCurve
```

````

````{py:attribute} Variable
:canonical: altdss.Relay.RelayBatchProperties.Variable
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Variable
```

````

````{py:attribute} Z0Ang
:canonical: altdss.Relay.RelayBatchProperties.Z0Ang
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Z0Ang
```

````

````{py:attribute} Z0Mag
:canonical: altdss.Relay.RelayBatchProperties.Z0Mag
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Z0Mag
```

````

````{py:attribute} Z1Ang
:canonical: altdss.Relay.RelayBatchProperties.Z1Ang
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Z1Ang
```

````

````{py:attribute} Z1Mag
:canonical: altdss.Relay.RelayBatchProperties.Z1Mag
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.Z1Mag
```

````

````{py:method} __contains__()
:canonical: altdss.Relay.RelayBatchProperties.__contains__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Relay.RelayBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Relay.RelayBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Relay.RelayBatchProperties.__dir__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Relay.RelayBatchProperties.__format__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Relay.RelayBatchProperties.__ge__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Relay.RelayBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Relay.RelayBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Relay.RelayBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Relay.RelayBatchProperties.__gt__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Relay.RelayBatchProperties.__init__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Relay.RelayBatchProperties.__ior__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Relay.RelayBatchProperties.__iter__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Relay.RelayBatchProperties.__le__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Relay.RelayBatchProperties.__len__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Relay.RelayBatchProperties.__lt__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Relay.RelayBatchProperties.__ne__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Relay.RelayBatchProperties.__new__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Relay.RelayBatchProperties.__or__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Relay.RelayBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Relay.RelayBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Relay.RelayBatchProperties.__repr__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Relay.RelayBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Relay.RelayBatchProperties.__ror__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Relay.RelayBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Relay.RelayBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Relay.RelayBatchProperties.__str__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Relay.RelayBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Relay.RelayBatchProperties.clear

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Relay.RelayBatchProperties.copy

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Relay.RelayBatchProperties.get

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Relay.RelayBatchProperties.items

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.items
```

````

````{py:attribute} kVBase
:canonical: altdss.Relay.RelayBatchProperties.kVBase
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.kVBase
```

````

````{py:method} keys()
:canonical: altdss.Relay.RelayBatchProperties.keys

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Relay.RelayBatchProperties.pop

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Relay.RelayBatchProperties.popitem

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Relay.RelayBatchProperties.setdefault

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Relay.RelayBatchProperties.update

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Relay.RelayBatchProperties.values

```{autodoc2-docstring} altdss.Relay.RelayBatchProperties.values
```

````

`````

`````{py:class} RelayProperties()
:canonical: altdss.Relay.RelayProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Relay.RelayProperties
```

````{py:attribute} Action
:canonical: altdss.Relay.RelayProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.RelayAction]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Relay.RelayProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.BaseFreq
```

````

````{py:attribute} BreakerTime
:canonical: altdss.Relay.RelayProperties.BreakerTime
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.BreakerTime
```

````

````{py:attribute} DOC_DelayInner
:canonical: altdss.Relay.RelayProperties.DOC_DelayInner
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_DelayInner
```

````

````{py:attribute} DOC_P1Blocking
:canonical: altdss.Relay.RelayProperties.DOC_P1Blocking
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_P1Blocking
```

````

````{py:attribute} DOC_PhaseCurveInner
:canonical: altdss.Relay.RelayProperties.DOC_PhaseCurveInner
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_PhaseCurveInner
```

````

````{py:attribute} DOC_PhaseTripInner
:canonical: altdss.Relay.RelayProperties.DOC_PhaseTripInner
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_PhaseTripInner
```

````

````{py:attribute} DOC_TDPhaseInner
:canonical: altdss.Relay.RelayProperties.DOC_TDPhaseInner
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_TDPhaseInner
```

````

````{py:attribute} DOC_TiltAngleHigh
:canonical: altdss.Relay.RelayProperties.DOC_TiltAngleHigh
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_TiltAngleHigh
```

````

````{py:attribute} DOC_TiltAngleLow
:canonical: altdss.Relay.RelayProperties.DOC_TiltAngleLow
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_TiltAngleLow
```

````

````{py:attribute} DOC_TripSettingHigh
:canonical: altdss.Relay.RelayProperties.DOC_TripSettingHigh
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_TripSettingHigh
```

````

````{py:attribute} DOC_TripSettingLow
:canonical: altdss.Relay.RelayProperties.DOC_TripSettingLow
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_TripSettingLow
```

````

````{py:attribute} DOC_TripSettingMag
:canonical: altdss.Relay.RelayProperties.DOC_TripSettingMag
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DOC_TripSettingMag
```

````

````{py:attribute} DebugTrace
:canonical: altdss.Relay.RelayProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.Relay.RelayProperties.Delay
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Delay
```

````

````{py:attribute} DistReverse
:canonical: altdss.Relay.RelayProperties.DistReverse
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.DistReverse
```

````

````{py:attribute} Enabled
:canonical: altdss.Relay.RelayProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.Relay.RelayProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.EventLog
```

````

````{py:attribute} F46BaseAmps
:canonical: altdss.Relay.RelayProperties.F46BaseAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.F46BaseAmps
```

````

````{py:attribute} F46isqt
:canonical: altdss.Relay.RelayProperties.F46isqt
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.F46isqt
```

````

````{py:attribute} F46pctPickup
:canonical: altdss.Relay.RelayProperties.F46pctPickup
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.F46pctPickup
```

````

````{py:attribute} F47pctPickup
:canonical: altdss.Relay.RelayProperties.F47pctPickup
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.F47pctPickup
```

````

````{py:attribute} GroundCurve
:canonical: altdss.Relay.RelayProperties.GroundCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.GroundCurve
```

````

````{py:attribute} GroundInst
:canonical: altdss.Relay.RelayProperties.GroundInst
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.GroundInst
```

````

````{py:attribute} GroundTrip
:canonical: altdss.Relay.RelayProperties.GroundTrip
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.GroundTrip
```

````

````{py:attribute} Like
:canonical: altdss.Relay.RelayProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Like
```

````

````{py:attribute} MGround
:canonical: altdss.Relay.RelayProperties.MGround
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.MGround
```

````

````{py:attribute} MPhase
:canonical: altdss.Relay.RelayProperties.MPhase
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.MPhase
```

````

````{py:attribute} MonitoredObj
:canonical: altdss.Relay.RelayProperties.MonitoredObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.MonitoredObj
```

````

````{py:attribute} MonitoredTerm
:canonical: altdss.Relay.RelayProperties.MonitoredTerm
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.MonitoredTerm
```

````

````{py:attribute} Normal
:canonical: altdss.Relay.RelayProperties.Normal
:type: typing.Union[typing.AnyStr, int, altdss.enums.RelayState]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Normal
```

````

````{py:attribute} Overtrip
:canonical: altdss.Relay.RelayProperties.Overtrip
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Overtrip
```

````

````{py:attribute} OvervoltCurve
:canonical: altdss.Relay.RelayProperties.OvervoltCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.OvervoltCurve
```

````

````{py:attribute} PhaseCurve
:canonical: altdss.Relay.RelayProperties.PhaseCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.PhaseCurve
```

````

````{py:attribute} PhaseInst
:canonical: altdss.Relay.RelayProperties.PhaseInst
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.PhaseInst
```

````

````{py:attribute} PhaseTrip
:canonical: altdss.Relay.RelayProperties.PhaseTrip
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.PhaseTrip
```

````

````{py:attribute} RecloseIntervals
:canonical: altdss.Relay.RelayProperties.RecloseIntervals
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.RecloseIntervals
```

````

````{py:attribute} Reset
:canonical: altdss.Relay.RelayProperties.Reset
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Reset
```

````

````{py:attribute} Shots
:canonical: altdss.Relay.RelayProperties.Shots
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Shots
```

````

````{py:attribute} State
:canonical: altdss.Relay.RelayProperties.State
:type: typing.Union[typing.AnyStr, int, altdss.enums.RelayState]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.State
```

````

````{py:attribute} SwitchedObj
:canonical: altdss.Relay.RelayProperties.SwitchedObj
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.SwitchedObj
```

````

````{py:attribute} SwitchedTerm
:canonical: altdss.Relay.RelayProperties.SwitchedTerm
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.SwitchedTerm
```

````

````{py:attribute} TDGround
:canonical: altdss.Relay.RelayProperties.TDGround
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.TDGround
```

````

````{py:attribute} TDPhase
:canonical: altdss.Relay.RelayProperties.TDPhase
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.TDPhase
```

````

````{py:attribute} Type
:canonical: altdss.Relay.RelayProperties.Type
:type: typing.Union[typing.AnyStr, int, altdss.enums.RelayType]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Type
```

````

````{py:attribute} Undertrip
:canonical: altdss.Relay.RelayProperties.Undertrip
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Undertrip
```

````

````{py:attribute} UndervoltCurve
:canonical: altdss.Relay.RelayProperties.UndervoltCurve
:type: typing.Union[typing.AnyStr, altdss.TCC_Curve.TCC_Curve]
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.UndervoltCurve
```

````

````{py:attribute} Variable
:canonical: altdss.Relay.RelayProperties.Variable
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Variable
```

````

````{py:attribute} Z0Ang
:canonical: altdss.Relay.RelayProperties.Z0Ang
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Z0Ang
```

````

````{py:attribute} Z0Mag
:canonical: altdss.Relay.RelayProperties.Z0Mag
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Z0Mag
```

````

````{py:attribute} Z1Ang
:canonical: altdss.Relay.RelayProperties.Z1Ang
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Z1Ang
```

````

````{py:attribute} Z1Mag
:canonical: altdss.Relay.RelayProperties.Z1Mag
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.Z1Mag
```

````

````{py:method} __contains__()
:canonical: altdss.Relay.RelayProperties.__contains__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Relay.RelayProperties.__delattr__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Relay.RelayProperties.__delitem__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Relay.RelayProperties.__dir__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Relay.RelayProperties.__format__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Relay.RelayProperties.__ge__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Relay.RelayProperties.__getattribute__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Relay.RelayProperties.__getitem__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Relay.RelayProperties.__getstate__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Relay.RelayProperties.__gt__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Relay.RelayProperties.__init__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Relay.RelayProperties.__ior__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Relay.RelayProperties.__iter__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Relay.RelayProperties.__le__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Relay.RelayProperties.__len__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Relay.RelayProperties.__lt__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Relay.RelayProperties.__ne__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Relay.RelayProperties.__new__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Relay.RelayProperties.__or__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Relay.RelayProperties.__reduce__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Relay.RelayProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Relay.RelayProperties.__repr__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Relay.RelayProperties.__reversed__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Relay.RelayProperties.__ror__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Relay.RelayProperties.__setitem__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Relay.RelayProperties.__sizeof__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Relay.RelayProperties.__str__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Relay.RelayProperties.__subclasshook__

```{autodoc2-docstring} altdss.Relay.RelayProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Relay.RelayProperties.clear

```{autodoc2-docstring} altdss.Relay.RelayProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Relay.RelayProperties.copy

```{autodoc2-docstring} altdss.Relay.RelayProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Relay.RelayProperties.get

```{autodoc2-docstring} altdss.Relay.RelayProperties.get
```

````

````{py:method} items()
:canonical: altdss.Relay.RelayProperties.items

```{autodoc2-docstring} altdss.Relay.RelayProperties.items
```

````

````{py:attribute} kVBase
:canonical: altdss.Relay.RelayProperties.kVBase
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Relay.RelayProperties.kVBase
```

````

````{py:method} keys()
:canonical: altdss.Relay.RelayProperties.keys

```{autodoc2-docstring} altdss.Relay.RelayProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.Relay.RelayProperties.pop

```{autodoc2-docstring} altdss.Relay.RelayProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Relay.RelayProperties.popitem

```{autodoc2-docstring} altdss.Relay.RelayProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Relay.RelayProperties.setdefault

```{autodoc2-docstring} altdss.Relay.RelayProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Relay.RelayProperties.update

```{autodoc2-docstring} altdss.Relay.RelayProperties.update
```

````

````{py:method} values()
:canonical: altdss.Relay.RelayProperties.values

```{autodoc2-docstring} altdss.Relay.RelayProperties.values
```

````

`````
