# {py:mod}`altdss.InvControl`

```{py:module} altdss.InvControl
```

```{autodoc2-docstring} altdss.InvControl
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IInvControl <altdss.InvControl.IInvControl>`
  - ```{autodoc2-docstring} altdss.InvControl.IInvControl
    :summary:
    ```
* - {py:obj}`InvControl <altdss.InvControl.InvControl>`
  - ```{autodoc2-docstring} altdss.InvControl.InvControl
    :summary:
    ```
* - {py:obj}`InvControlBatch <altdss.InvControl.InvControlBatch>`
  - ```{autodoc2-docstring} altdss.InvControl.InvControlBatch
    :summary:
    ```
* - {py:obj}`InvControlBatchProperties <altdss.InvControl.InvControlBatchProperties>`
  - ```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties
    :summary:
    ```
* - {py:obj}`InvControlProperties <altdss.InvControl.InvControlProperties>`
  - ```{autodoc2-docstring} altdss.InvControl.InvControlProperties
    :summary:
    ```
````

### API

`````{py:class} IInvControl(iobj)
:canonical: altdss.InvControl.IInvControl

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.InvControl.InvControlBatch`

```{autodoc2-docstring} altdss.InvControl.IInvControl
```

````{py:attribute} ActivePChangeTolerance
:canonical: altdss.InvControl.IInvControl.ActivePChangeTolerance
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.ActivePChangeTolerance
```

````

````{py:attribute} ArGraHiV
:canonical: altdss.InvControl.IInvControl.ArGraHiV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.ArGraHiV
```

````

````{py:attribute} ArGraLowV
:canonical: altdss.InvControl.IInvControl.ArGraLowV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.ArGraLowV
```

````

````{py:attribute} AvgWindowLen
:canonical: altdss.InvControl.IInvControl.AvgWindowLen
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.AvgWindowLen
```

````

````{py:attribute} BaseFreq
:canonical: altdss.InvControl.IInvControl.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.BaseFreq
```

````

````{py:attribute} CombiMode
:canonical: altdss.InvControl.IInvControl.CombiMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.CombiMode
```

````

````{py:attribute} CombiMode_str
:canonical: altdss.InvControl.IInvControl.CombiMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.CombiMode_str
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.IInvControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.InvControl.IInvControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.IInvControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.InvControl.IInvControl.ComplexSeqVoltages
```

````

````{py:attribute} ControlModel
:canonical: altdss.InvControl.IInvControl.ControlModel
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.ControlModel
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.IInvControl.Currents

```{autodoc2-docstring} altdss.InvControl.IInvControl.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.InvControl.IInvControl.CurrentsMagAng

```{autodoc2-docstring} altdss.InvControl.IInvControl.CurrentsMagAng
```

````

````{py:attribute} DERList
:canonical: altdss.InvControl.IInvControl.DERList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.DERList
```

````

````{py:attribute} DbVMax
:canonical: altdss.InvControl.IInvControl.DbVMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.DbVMax
```

````

````{py:attribute} DbVMin
:canonical: altdss.InvControl.IInvControl.DbVMin
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.DbVMin
```

````

````{py:attribute} DeltaP_Factor
:canonical: altdss.InvControl.IInvControl.DeltaP_Factor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.DeltaP_Factor
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.InvControl.IInvControl.DeltaQ_Factor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.DeltaQ_Factor
```

````

````{py:attribute} DynReacAvgWindowLen
:canonical: altdss.InvControl.IInvControl.DynReacAvgWindowLen
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.DynReacAvgWindowLen
```

````

````{py:attribute} Enabled
:canonical: altdss.InvControl.IInvControl.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.InvControl.IInvControl.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.InvControl.IInvControl.FullName

```{autodoc2-docstring} altdss.InvControl.IInvControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.InvControl.IInvControl.GUID

```{autodoc2-docstring} altdss.InvControl.IInvControl.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.InvControl.IInvControl.Handle

```{autodoc2-docstring} altdss.InvControl.IInvControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.InvControl.IInvControl.HasOCPDevice

```{autodoc2-docstring} altdss.InvControl.IInvControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.InvControl.IInvControl.HasSwitchControl

```{autodoc2-docstring} altdss.InvControl.IInvControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.InvControl.IInvControl.HasVoltControl

```{autodoc2-docstring} altdss.InvControl.IInvControl.HasVoltControl
```

````

````{py:attribute} Hysteresis_Offset
:canonical: altdss.InvControl.IInvControl.Hysteresis_Offset
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.Hysteresis_Offset
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.InvControl.IInvControl.IsIsolated

```{autodoc2-docstring} altdss.InvControl.IInvControl.IsIsolated
```

````

````{py:attribute} LPFTau
:canonical: altdss.InvControl.IInvControl.LPFTau
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.LPFTau
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.InvControl.IInvControl.Like

```{autodoc2-docstring} altdss.InvControl.IInvControl.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.IInvControl.Losses

```{autodoc2-docstring} altdss.InvControl.IInvControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.InvControl.IInvControl.MaxCurrent

```{autodoc2-docstring} altdss.InvControl.IInvControl.MaxCurrent
```

````

````{py:attribute} Mode
:canonical: altdss.InvControl.IInvControl.Mode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.Mode
```

````

````{py:attribute} Mode_str
:canonical: altdss.InvControl.IInvControl.Mode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.Mode_str
```

````

````{py:attribute} MonBus
:canonical: altdss.InvControl.IInvControl.MonBus
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.MonBus
```

````

````{py:attribute} MonBusesVBase
:canonical: altdss.InvControl.IInvControl.MonBusesVBase
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.MonBusesVBase
```

````

````{py:attribute} MonVoltageCalc
:canonical: altdss.InvControl.IInvControl.MonVoltageCalc
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.MonVoltageCalc
```

````

````{py:attribute} MonVoltageCalc_str
:canonical: altdss.InvControl.IInvControl.MonVoltageCalc_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.MonVoltageCalc_str
```

````

````{py:property} Name
:canonical: altdss.InvControl.IInvControl.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.InvControl.IInvControl.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.InvControl.IInvControl.NumConductors

```{autodoc2-docstring} altdss.InvControl.IInvControl.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.InvControl.IInvControl.NumControllers

```{autodoc2-docstring} altdss.InvControl.IInvControl.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.InvControl.IInvControl.NumPhases

```{autodoc2-docstring} altdss.InvControl.IInvControl.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.InvControl.IInvControl.NumTerminals

```{autodoc2-docstring} altdss.InvControl.IInvControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.InvControl.IInvControl.OCPDevice

```{autodoc2-docstring} altdss.InvControl.IInvControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.InvControl.IInvControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.InvControl.IInvControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.InvControl.IInvControl.OCPDeviceType

```{autodoc2-docstring} altdss.InvControl.IInvControl.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.IInvControl.PhaseLosses

```{autodoc2-docstring} altdss.InvControl.IInvControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.IInvControl.Powers

```{autodoc2-docstring} altdss.InvControl.IInvControl.Powers
```

````

````{py:attribute} RateOfChangeMode
:canonical: altdss.InvControl.IInvControl.RateOfChangeMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.RateOfChangeMode
```

````

````{py:attribute} RateOfChangeMode_str
:canonical: altdss.InvControl.IInvControl.RateOfChangeMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.RateOfChangeMode_str
```

````

````{py:attribute} RefReactivePower
:canonical: altdss.InvControl.IInvControl.RefReactivePower
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.RefReactivePower
```

````

````{py:attribute} RefReactivePower_str
:canonical: altdss.InvControl.IInvControl.RefReactivePower_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.RefReactivePower_str
```

````

````{py:attribute} RiseFallLimit
:canonical: altdss.InvControl.IInvControl.RiseFallLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.RiseFallLimit
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.InvControl.IInvControl.SeqCurrents

```{autodoc2-docstring} altdss.InvControl.IInvControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.IInvControl.SeqPowers

```{autodoc2-docstring} altdss.InvControl.IInvControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.InvControl.IInvControl.SeqVoltages

```{autodoc2-docstring} altdss.InvControl.IInvControl.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.IInvControl.TotalPowers

```{autodoc2-docstring} altdss.InvControl.IInvControl.TotalPowers
```

````

````{py:attribute} VSetPoint
:canonical: altdss.InvControl.IInvControl.VSetPoint
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VSetPoint
```

````

````{py:attribute} VVC_Curve1
:canonical: altdss.InvControl.IInvControl.VVC_Curve1
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VVC_Curve1
```

````

````{py:attribute} VVC_Curve1_str
:canonical: altdss.InvControl.IInvControl.VVC_Curve1_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VVC_Curve1_str
```

````

````{py:attribute} VarChangeTolerance
:canonical: altdss.InvControl.IInvControl.VarChangeTolerance
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VarChangeTolerance
```

````

````{py:attribute} VoltWattCH_Curve
:canonical: altdss.InvControl.IInvControl.VoltWattCH_Curve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VoltWattCH_Curve
```

````

````{py:attribute} VoltWattCH_Curve_str
:canonical: altdss.InvControl.IInvControl.VoltWattCH_Curve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VoltWattCH_Curve_str
```

````

````{py:attribute} VoltWattYAxis
:canonical: altdss.InvControl.IInvControl.VoltWattYAxis
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VoltWattYAxis
```

````

````{py:attribute} VoltWattYAxis_str
:canonical: altdss.InvControl.IInvControl.VoltWattYAxis_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VoltWattYAxis_str
```

````

````{py:attribute} VoltWatt_Curve
:canonical: altdss.InvControl.IInvControl.VoltWatt_Curve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VoltWatt_Curve
```

````

````{py:attribute} VoltWatt_Curve_str
:canonical: altdss.InvControl.IInvControl.VoltWatt_Curve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VoltWatt_Curve_str
```

````

````{py:attribute} VoltageChangeTolerance
:canonical: altdss.InvControl.IInvControl.VoltageChangeTolerance
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.VoltageChangeTolerance
```

````

````{py:attribute} Voltage_CurveX_Ref
:canonical: altdss.InvControl.IInvControl.Voltage_CurveX_Ref
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.Voltage_CurveX_Ref
```

````

````{py:attribute} Voltage_CurveX_Ref_str
:canonical: altdss.InvControl.IInvControl.Voltage_CurveX_Ref_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.Voltage_CurveX_Ref_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.IInvControl.Voltages

```{autodoc2-docstring} altdss.InvControl.IInvControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.InvControl.IInvControl.VoltagesMagAng

```{autodoc2-docstring} altdss.InvControl.IInvControl.VoltagesMagAng
```

````

````{py:attribute} WattPF_Curve
:canonical: altdss.InvControl.IInvControl.WattPF_Curve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.WattPF_Curve
```

````

````{py:attribute} WattPF_Curve_str
:canonical: altdss.InvControl.IInvControl.WattPF_Curve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.WattPF_Curve_str
```

````

````{py:attribute} WattVar_Curve
:canonical: altdss.InvControl.IInvControl.WattVar_Curve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.WattVar_Curve
```

````

````{py:attribute} WattVar_Curve_str
:canonical: altdss.InvControl.IInvControl.WattVar_Curve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.IInvControl.WattVar_Curve_str
```

````

````{py:method} __call__()
:canonical: altdss.InvControl.IInvControl.__call__

```{autodoc2-docstring} altdss.InvControl.IInvControl.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.InvControl.IInvControl.__contains__

```{autodoc2-docstring} altdss.InvControl.IInvControl.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.InvControl.IInvControl.__getitem__

```{autodoc2-docstring} altdss.InvControl.IInvControl.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.InvControl.IInvControl.__init__

```{autodoc2-docstring} altdss.InvControl.IInvControl.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.InvControl.IInvControl.__iter__

```{autodoc2-docstring} altdss.InvControl.IInvControl.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.InvControl.IInvControl.__len__

```{autodoc2-docstring} altdss.InvControl.IInvControl.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.InvControl.IInvControl.batch

```{autodoc2-docstring} altdss.InvControl.IInvControl.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.InvControl.InvControlBatchProperties]) -> altdss.InvControl.InvControlBatch
:canonical: altdss.InvControl.IInvControl.batch_new

```{autodoc2-docstring} altdss.InvControl.IInvControl.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.InvControl.IInvControl.begin_edit

```{autodoc2-docstring} altdss.InvControl.IInvControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.InvControl.IInvControl.end_edit

```{autodoc2-docstring} altdss.InvControl.IInvControl.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.InvControl.IInvControl.find

```{autodoc2-docstring} altdss.InvControl.IInvControl.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.InvControl.InvControlProperties]) -> altdss.InvControl.InvControl
:canonical: altdss.InvControl.IInvControl.new

```{autodoc2-docstring} altdss.InvControl.IInvControl.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.InvControl.IInvControl.to_json

```{autodoc2-docstring} altdss.InvControl.IInvControl.to_json
```

````

````{py:method} to_list()
:canonical: altdss.InvControl.IInvControl.to_list

```{autodoc2-docstring} altdss.InvControl.IInvControl.to_list
```

````

`````

`````{py:class} InvControl(api_util, ptr)
:canonical: altdss.InvControl.InvControl

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.InvControl.InvControl
```

````{py:attribute} ActivePChangeTolerance
:canonical: altdss.InvControl.InvControl.ActivePChangeTolerance
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.ActivePChangeTolerance
```

````

````{py:attribute} ArGraHiV
:canonical: altdss.InvControl.InvControl.ArGraHiV
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.ArGraHiV
```

````

````{py:attribute} ArGraLowV
:canonical: altdss.InvControl.InvControl.ArGraLowV
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.ArGraLowV
```

````

````{py:attribute} AvgWindowLen
:canonical: altdss.InvControl.InvControl.AvgWindowLen
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.AvgWindowLen
```

````

````{py:attribute} BaseFreq
:canonical: altdss.InvControl.InvControl.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.BaseFreq
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.InvControl.InvControl.Close

```{autodoc2-docstring} altdss.InvControl.InvControl.Close
```

````

````{py:attribute} CombiMode
:canonical: altdss.InvControl.InvControl.CombiMode
:type: altdss.enums.InvControlCombiMode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.CombiMode
```

````

````{py:attribute} CombiMode_str
:canonical: altdss.InvControl.InvControl.CombiMode_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.CombiMode_str
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.InvControl.InvControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.InvControl.InvControl.ComplexSeqVoltages
```

````

````{py:attribute} ControlModel
:canonical: altdss.InvControl.InvControl.ControlModel
:type: altdss.enums.InvControlControlModel
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.ControlModel
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControl.Currents

```{autodoc2-docstring} altdss.InvControl.InvControl.Currents
```

````

````{py:attribute} DERList
:canonical: altdss.InvControl.InvControl.DERList
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.DERList
```

````

````{py:attribute} DbVMax
:canonical: altdss.InvControl.InvControl.DbVMax
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.DbVMax
```

````

````{py:attribute} DbVMin
:canonical: altdss.InvControl.InvControl.DbVMin
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.DbVMin
```

````

````{py:attribute} DeltaP_Factor
:canonical: altdss.InvControl.InvControl.DeltaP_Factor
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.DeltaP_Factor
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.InvControl.InvControl.DeltaQ_Factor
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.DeltaQ_Factor
```

````

````{py:attribute} DisplayName
:canonical: altdss.InvControl.InvControl.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.DisplayName
```

````

````{py:attribute} DynReacAvgWindowLen
:canonical: altdss.InvControl.InvControl.DynReacAvgWindowLen
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.DynReacAvgWindowLen
```

````

````{py:attribute} Enabled
:canonical: altdss.InvControl.InvControl.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.InvControl.InvControl.EventLog
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.EventLog
```

````

````{py:method} FullName() -> str
:canonical: altdss.InvControl.InvControl.FullName

```{autodoc2-docstring} altdss.InvControl.InvControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.InvControl.InvControl.GUID

```{autodoc2-docstring} altdss.InvControl.InvControl.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.InvControl.InvControl.Handle

```{autodoc2-docstring} altdss.InvControl.InvControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.InvControl.InvControl.HasOCPDevice

```{autodoc2-docstring} altdss.InvControl.InvControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.InvControl.InvControl.HasSwitchControl

```{autodoc2-docstring} altdss.InvControl.InvControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.InvControl.InvControl.HasVoltControl

```{autodoc2-docstring} altdss.InvControl.InvControl.HasVoltControl
```

````

````{py:attribute} Hysteresis_Offset
:canonical: altdss.InvControl.InvControl.Hysteresis_Offset
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.Hysteresis_Offset
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.InvControl.InvControl.IsIsolated

```{autodoc2-docstring} altdss.InvControl.InvControl.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.InvControl.InvControl.IsOpen

```{autodoc2-docstring} altdss.InvControl.InvControl.IsOpen
```

````

````{py:attribute} LPFTau
:canonical: altdss.InvControl.InvControl.LPFTau
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.LPFTau
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.InvControl.InvControl.Like

```{autodoc2-docstring} altdss.InvControl.InvControl.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.InvControl.InvControl.Losses

```{autodoc2-docstring} altdss.InvControl.InvControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.InvControl.InvControl.MaxCurrent

```{autodoc2-docstring} altdss.InvControl.InvControl.MaxCurrent
```

````

````{py:attribute} Mode
:canonical: altdss.InvControl.InvControl.Mode
:type: altdss.enums.InvControlControlMode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.Mode
```

````

````{py:attribute} Mode_str
:canonical: altdss.InvControl.InvControl.Mode_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.Mode_str
```

````

````{py:attribute} MonBus
:canonical: altdss.InvControl.InvControl.MonBus
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.MonBus
```

````

````{py:attribute} MonBusesVBase
:canonical: altdss.InvControl.InvControl.MonBusesVBase
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.MonBusesVBase
```

````

````{py:attribute} MonVoltageCalc
:canonical: altdss.InvControl.InvControl.MonVoltageCalc
:type: altdss.enums.MonitoredPhase
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.MonVoltageCalc
```

````

````{py:attribute} MonVoltageCalc_str
:canonical: altdss.InvControl.InvControl.MonVoltageCalc_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.MonVoltageCalc_str
```

````

````{py:property} Name
:canonical: altdss.InvControl.InvControl.Name
:type: str

```{autodoc2-docstring} altdss.InvControl.InvControl.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.InvControl.InvControl.NodeOrder

```{autodoc2-docstring} altdss.InvControl.InvControl.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.InvControl.InvControl.NodeRef

```{autodoc2-docstring} altdss.InvControl.InvControl.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.InvControl.InvControl.NumConductors

```{autodoc2-docstring} altdss.InvControl.InvControl.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.InvControl.InvControl.NumControllers

```{autodoc2-docstring} altdss.InvControl.InvControl.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.InvControl.InvControl.NumPhases

```{autodoc2-docstring} altdss.InvControl.InvControl.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.InvControl.InvControl.NumTerminals

```{autodoc2-docstring} altdss.InvControl.InvControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.InvControl.InvControl.OCPDevice

```{autodoc2-docstring} altdss.InvControl.InvControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.InvControl.InvControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.InvControl.InvControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.InvControl.InvControl.OCPDeviceType

```{autodoc2-docstring} altdss.InvControl.InvControl.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.InvControl.InvControl.Open

```{autodoc2-docstring} altdss.InvControl.InvControl.Open
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControl.PhaseLosses

```{autodoc2-docstring} altdss.InvControl.InvControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControl.Powers

```{autodoc2-docstring} altdss.InvControl.InvControl.Powers
```

````

````{py:attribute} RateOfChangeMode
:canonical: altdss.InvControl.InvControl.RateOfChangeMode
:type: altdss.enums.InvControlRateOfChangeMode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.RateOfChangeMode
```

````

````{py:attribute} RateOfChangeMode_str
:canonical: altdss.InvControl.InvControl.RateOfChangeMode_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.RateOfChangeMode_str
```

````

````{py:attribute} RefReactivePower
:canonical: altdss.InvControl.InvControl.RefReactivePower
:type: altdss.enums.InvControlReactivePowerReference
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.RefReactivePower
```

````

````{py:attribute} RefReactivePower_str
:canonical: altdss.InvControl.InvControl.RefReactivePower_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.RefReactivePower_str
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.InvControl.InvControl.Residuals

```{autodoc2-docstring} altdss.InvControl.InvControl.Residuals
```

````

````{py:attribute} RiseFallLimit
:canonical: altdss.InvControl.InvControl.RiseFallLimit
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.RiseFallLimit
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.InvControl.InvControl.SeqCurrents

```{autodoc2-docstring} altdss.InvControl.InvControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControl.SeqPowers

```{autodoc2-docstring} altdss.InvControl.InvControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.InvControl.InvControl.SeqVoltages

```{autodoc2-docstring} altdss.InvControl.InvControl.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControl.TotalPowers

```{autodoc2-docstring} altdss.InvControl.InvControl.TotalPowers
```

````

````{py:attribute} VSetPoint
:canonical: altdss.InvControl.InvControl.VSetPoint
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VSetPoint
```

````

````{py:attribute} VVC_Curve1
:canonical: altdss.InvControl.InvControl.VVC_Curve1
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VVC_Curve1
```

````

````{py:attribute} VVC_Curve1_str
:canonical: altdss.InvControl.InvControl.VVC_Curve1_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VVC_Curve1_str
```

````

````{py:attribute} VarChangeTolerance
:canonical: altdss.InvControl.InvControl.VarChangeTolerance
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VarChangeTolerance
```

````

````{py:attribute} VoltWattCH_Curve
:canonical: altdss.InvControl.InvControl.VoltWattCH_Curve
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VoltWattCH_Curve
```

````

````{py:attribute} VoltWattCH_Curve_str
:canonical: altdss.InvControl.InvControl.VoltWattCH_Curve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VoltWattCH_Curve_str
```

````

````{py:attribute} VoltWattYAxis
:canonical: altdss.InvControl.InvControl.VoltWattYAxis
:type: altdss.enums.InvControlVoltWattYAxis
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VoltWattYAxis
```

````

````{py:attribute} VoltWattYAxis_str
:canonical: altdss.InvControl.InvControl.VoltWattYAxis_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VoltWattYAxis_str
```

````

````{py:attribute} VoltWatt_Curve
:canonical: altdss.InvControl.InvControl.VoltWatt_Curve
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VoltWatt_Curve
```

````

````{py:attribute} VoltWatt_Curve_str
:canonical: altdss.InvControl.InvControl.VoltWatt_Curve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VoltWatt_Curve_str
```

````

````{py:attribute} VoltageChangeTolerance
:canonical: altdss.InvControl.InvControl.VoltageChangeTolerance
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.VoltageChangeTolerance
```

````

````{py:attribute} Voltage_CurveX_Ref
:canonical: altdss.InvControl.InvControl.Voltage_CurveX_Ref
:type: altdss.enums.InvControlVoltageCurveXRef
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.Voltage_CurveX_Ref
```

````

````{py:attribute} Voltage_CurveX_Ref_str
:canonical: altdss.InvControl.InvControl.Voltage_CurveX_Ref_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.Voltage_CurveX_Ref_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControl.Voltages

```{autodoc2-docstring} altdss.InvControl.InvControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.InvControl.InvControl.VoltagesMagAng

```{autodoc2-docstring} altdss.InvControl.InvControl.VoltagesMagAng
```

````

````{py:attribute} WattPF_Curve
:canonical: altdss.InvControl.InvControl.WattPF_Curve
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.WattPF_Curve
```

````

````{py:attribute} WattPF_Curve_str
:canonical: altdss.InvControl.InvControl.WattPF_Curve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.WattPF_Curve_str
```

````

````{py:attribute} WattVar_Curve
:canonical: altdss.InvControl.InvControl.WattVar_Curve
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.WattVar_Curve
```

````

````{py:attribute} WattVar_Curve_str
:canonical: altdss.InvControl.InvControl.WattVar_Curve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControl.WattVar_Curve_str
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControl.YPrim

```{autodoc2-docstring} altdss.InvControl.InvControl.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.InvControl.InvControl.__hash__

```{autodoc2-docstring} altdss.InvControl.InvControl.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.InvControl.InvControl.__init__

```{autodoc2-docstring} altdss.InvControl.InvControl.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.InvControl.InvControl.__ne__

```{autodoc2-docstring} altdss.InvControl.InvControl.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.InvControl.InvControl.__repr__

```{autodoc2-docstring} altdss.InvControl.InvControl.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.InvControl.InvControl.begin_edit

```{autodoc2-docstring} altdss.InvControl.InvControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.InvControl.InvControl.end_edit

```{autodoc2-docstring} altdss.InvControl.InvControl.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.InvControl.InvControl.to_json

```{autodoc2-docstring} altdss.InvControl.InvControl.to_json
```

````

`````

`````{py:class} InvControlBatch(api_util, **kwargs)
:canonical: altdss.InvControl.InvControlBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.InvControl.InvControlBatch
```

````{py:attribute} ActivePChangeTolerance
:canonical: altdss.InvControl.InvControlBatch.ActivePChangeTolerance
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.ActivePChangeTolerance
```

````

````{py:attribute} ArGraHiV
:canonical: altdss.InvControl.InvControlBatch.ArGraHiV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.ArGraHiV
```

````

````{py:attribute} ArGraLowV
:canonical: altdss.InvControl.InvControlBatch.ArGraLowV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.ArGraLowV
```

````

````{py:attribute} AvgWindowLen
:canonical: altdss.InvControl.InvControlBatch.AvgWindowLen
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.AvgWindowLen
```

````

````{py:attribute} BaseFreq
:canonical: altdss.InvControl.InvControlBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.BaseFreq
```

````

````{py:attribute} CombiMode
:canonical: altdss.InvControl.InvControlBatch.CombiMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.CombiMode
```

````

````{py:attribute} CombiMode_str
:canonical: altdss.InvControl.InvControlBatch.CombiMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.CombiMode_str
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControlBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControlBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.ComplexSeqVoltages
```

````

````{py:attribute} ControlModel
:canonical: altdss.InvControl.InvControlBatch.ControlModel
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.ControlModel
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControlBatch.Currents

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.InvControl.InvControlBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.CurrentsMagAng
```

````

````{py:attribute} DERList
:canonical: altdss.InvControl.InvControlBatch.DERList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.DERList
```

````

````{py:attribute} DbVMax
:canonical: altdss.InvControl.InvControlBatch.DbVMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.DbVMax
```

````

````{py:attribute} DbVMin
:canonical: altdss.InvControl.InvControlBatch.DbVMin
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.DbVMin
```

````

````{py:attribute} DeltaP_Factor
:canonical: altdss.InvControl.InvControlBatch.DeltaP_Factor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.DeltaP_Factor
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.InvControl.InvControlBatch.DeltaQ_Factor
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.DeltaQ_Factor
```

````

````{py:attribute} DynReacAvgWindowLen
:canonical: altdss.InvControl.InvControlBatch.DynReacAvgWindowLen
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.DynReacAvgWindowLen
```

````

````{py:attribute} Enabled
:canonical: altdss.InvControl.InvControlBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.InvControl.InvControlBatch.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.InvControl.InvControlBatch.FullName

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.InvControl.InvControlBatch.GUID

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.InvControl.InvControlBatch.Handle

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.InvControl.InvControlBatch.HasOCPDevice

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.InvControl.InvControlBatch.HasSwitchControl

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.InvControl.InvControlBatch.HasVoltControl

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.HasVoltControl
```

````

````{py:attribute} Hysteresis_Offset
:canonical: altdss.InvControl.InvControlBatch.Hysteresis_Offset
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Hysteresis_Offset
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.InvControl.InvControlBatch.IsIsolated

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.IsIsolated
```

````

````{py:attribute} LPFTau
:canonical: altdss.InvControl.InvControlBatch.LPFTau
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.LPFTau
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.InvControl.InvControlBatch.Like

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControlBatch.Losses

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.InvControl.InvControlBatch.MaxCurrent

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.MaxCurrent
```

````

````{py:attribute} Mode
:canonical: altdss.InvControl.InvControlBatch.Mode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Mode
```

````

````{py:attribute} Mode_str
:canonical: altdss.InvControl.InvControlBatch.Mode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Mode_str
```

````

````{py:attribute} MonBus
:canonical: altdss.InvControl.InvControlBatch.MonBus
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.MonBus
```

````

````{py:attribute} MonBusesVBase
:canonical: altdss.InvControl.InvControlBatch.MonBusesVBase
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.MonBusesVBase
```

````

````{py:attribute} MonVoltageCalc
:canonical: altdss.InvControl.InvControlBatch.MonVoltageCalc
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.MonVoltageCalc
```

````

````{py:attribute} MonVoltageCalc_str
:canonical: altdss.InvControl.InvControlBatch.MonVoltageCalc_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.MonVoltageCalc_str
```

````

````{py:property} Name
:canonical: altdss.InvControl.InvControlBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.InvControl.InvControlBatch.NumConductors

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.InvControl.InvControlBatch.NumControllers

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.InvControl.InvControlBatch.NumPhases

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.InvControl.InvControlBatch.NumTerminals

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.InvControl.InvControlBatch.OCPDevice

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.InvControl.InvControlBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.InvControl.InvControlBatch.OCPDeviceType

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControlBatch.PhaseLosses

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControlBatch.Powers

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Powers
```

````

````{py:attribute} RateOfChangeMode
:canonical: altdss.InvControl.InvControlBatch.RateOfChangeMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.RateOfChangeMode
```

````

````{py:attribute} RateOfChangeMode_str
:canonical: altdss.InvControl.InvControlBatch.RateOfChangeMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.RateOfChangeMode_str
```

````

````{py:attribute} RefReactivePower
:canonical: altdss.InvControl.InvControlBatch.RefReactivePower
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.RefReactivePower
```

````

````{py:attribute} RefReactivePower_str
:canonical: altdss.InvControl.InvControlBatch.RefReactivePower_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.RefReactivePower_str
```

````

````{py:attribute} RiseFallLimit
:canonical: altdss.InvControl.InvControlBatch.RiseFallLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.RiseFallLimit
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.InvControl.InvControlBatch.SeqCurrents

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControlBatch.SeqPowers

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.InvControl.InvControlBatch.SeqVoltages

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControlBatch.TotalPowers

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.TotalPowers
```

````

````{py:attribute} VSetPoint
:canonical: altdss.InvControl.InvControlBatch.VSetPoint
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VSetPoint
```

````

````{py:attribute} VVC_Curve1
:canonical: altdss.InvControl.InvControlBatch.VVC_Curve1
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VVC_Curve1
```

````

````{py:attribute} VVC_Curve1_str
:canonical: altdss.InvControl.InvControlBatch.VVC_Curve1_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VVC_Curve1_str
```

````

````{py:attribute} VarChangeTolerance
:canonical: altdss.InvControl.InvControlBatch.VarChangeTolerance
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VarChangeTolerance
```

````

````{py:attribute} VoltWattCH_Curve
:canonical: altdss.InvControl.InvControlBatch.VoltWattCH_Curve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VoltWattCH_Curve
```

````

````{py:attribute} VoltWattCH_Curve_str
:canonical: altdss.InvControl.InvControlBatch.VoltWattCH_Curve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VoltWattCH_Curve_str
```

````

````{py:attribute} VoltWattYAxis
:canonical: altdss.InvControl.InvControlBatch.VoltWattYAxis
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VoltWattYAxis
```

````

````{py:attribute} VoltWattYAxis_str
:canonical: altdss.InvControl.InvControlBatch.VoltWattYAxis_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VoltWattYAxis_str
```

````

````{py:attribute} VoltWatt_Curve
:canonical: altdss.InvControl.InvControlBatch.VoltWatt_Curve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VoltWatt_Curve
```

````

````{py:attribute} VoltWatt_Curve_str
:canonical: altdss.InvControl.InvControlBatch.VoltWatt_Curve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VoltWatt_Curve_str
```

````

````{py:attribute} VoltageChangeTolerance
:canonical: altdss.InvControl.InvControlBatch.VoltageChangeTolerance
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VoltageChangeTolerance
```

````

````{py:attribute} Voltage_CurveX_Ref
:canonical: altdss.InvControl.InvControlBatch.Voltage_CurveX_Ref
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Voltage_CurveX_Ref
```

````

````{py:attribute} Voltage_CurveX_Ref_str
:canonical: altdss.InvControl.InvControlBatch.Voltage_CurveX_Ref_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Voltage_CurveX_Ref_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.InvControl.InvControlBatch.Voltages

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.InvControl.InvControlBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.VoltagesMagAng
```

````

````{py:attribute} WattPF_Curve
:canonical: altdss.InvControl.InvControlBatch.WattPF_Curve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.WattPF_Curve
```

````

````{py:attribute} WattPF_Curve_str
:canonical: altdss.InvControl.InvControlBatch.WattPF_Curve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.WattPF_Curve_str
```

````

````{py:attribute} WattVar_Curve
:canonical: altdss.InvControl.InvControlBatch.WattVar_Curve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.WattVar_Curve
```

````

````{py:attribute} WattVar_Curve_str
:canonical: altdss.InvControl.InvControlBatch.WattVar_Curve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.WattVar_Curve_str
```

````

````{py:method} __call__()
:canonical: altdss.InvControl.InvControlBatch.__call__

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.InvControl.InvControlBatch.__getitem__

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.InvControl.InvControlBatch.__init__

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.InvControl.InvControlBatch.__iter__

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.InvControl.InvControlBatch.__len__

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.InvControl.InvControlBatch.begin_edit

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.InvControl.InvControlBatch.end_edit

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.InvControl.InvControlBatch.to_json

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.InvControl.InvControlBatch.to_list

```{autodoc2-docstring} altdss.InvControl.InvControlBatch.to_list
```

````

`````

`````{py:class} InvControlBatchProperties()
:canonical: altdss.InvControl.InvControlBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties
```

````{py:attribute} ActivePChangeTolerance
:canonical: altdss.InvControl.InvControlBatchProperties.ActivePChangeTolerance
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.ActivePChangeTolerance
```

````

````{py:attribute} ArGraHiV
:canonical: altdss.InvControl.InvControlBatchProperties.ArGraHiV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.ArGraHiV
```

````

````{py:attribute} ArGraLowV
:canonical: altdss.InvControl.InvControlBatchProperties.ArGraLowV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.ArGraLowV
```

````

````{py:attribute} AvgWindowLen
:canonical: altdss.InvControl.InvControlBatchProperties.AvgWindowLen
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.AvgWindowLen
```

````

````{py:attribute} BaseFreq
:canonical: altdss.InvControl.InvControlBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.BaseFreq
```

````

````{py:attribute} CombiMode
:canonical: altdss.InvControl.InvControlBatchProperties.CombiMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlCombiMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.InvControlCombiMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.CombiMode
```

````

````{py:attribute} ControlModel
:canonical: altdss.InvControl.InvControlBatchProperties.ControlModel
:type: typing.Union[int, altdss.enums.InvControlControlModel, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.ControlModel
```

````

````{py:attribute} DERList
:canonical: altdss.InvControl.InvControlBatchProperties.DERList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.DERList
```

````

````{py:attribute} DbVMax
:canonical: altdss.InvControl.InvControlBatchProperties.DbVMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.DbVMax
```

````

````{py:attribute} DbVMin
:canonical: altdss.InvControl.InvControlBatchProperties.DbVMin
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.DbVMin
```

````

````{py:attribute} DeltaP_Factor
:canonical: altdss.InvControl.InvControlBatchProperties.DeltaP_Factor
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.DeltaP_Factor
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.InvControl.InvControlBatchProperties.DeltaQ_Factor
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.DeltaQ_Factor
```

````

````{py:attribute} DynReacAvgWindowLen
:canonical: altdss.InvControl.InvControlBatchProperties.DynReacAvgWindowLen
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.DynReacAvgWindowLen
```

````

````{py:attribute} Enabled
:canonical: altdss.InvControl.InvControlBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.InvControl.InvControlBatchProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.EventLog
```

````

````{py:attribute} Hysteresis_Offset
:canonical: altdss.InvControl.InvControlBatchProperties.Hysteresis_Offset
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.Hysteresis_Offset
```

````

````{py:attribute} LPFTau
:canonical: altdss.InvControl.InvControlBatchProperties.LPFTau
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.LPFTau
```

````

````{py:attribute} Like
:canonical: altdss.InvControl.InvControlBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.Like
```

````

````{py:attribute} Mode
:canonical: altdss.InvControl.InvControlBatchProperties.Mode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlControlMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.InvControlControlMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.Mode
```

````

````{py:attribute} MonBus
:canonical: altdss.InvControl.InvControlBatchProperties.MonBus
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.MonBus
```

````

````{py:attribute} MonBusesVBase
:canonical: altdss.InvControl.InvControlBatchProperties.MonBusesVBase
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.MonBusesVBase
```

````

````{py:attribute} MonVoltageCalc
:canonical: altdss.InvControl.InvControlBatchProperties.MonVoltageCalc
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitoredPhase, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.MonitoredPhase], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.MonVoltageCalc
```

````

````{py:attribute} RateOfChangeMode
:canonical: altdss.InvControl.InvControlBatchProperties.RateOfChangeMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlRateOfChangeMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.InvControlRateOfChangeMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.RateOfChangeMode
```

````

````{py:attribute} RefReactivePower
:canonical: altdss.InvControl.InvControlBatchProperties.RefReactivePower
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlReactivePowerReference, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.InvControlReactivePowerReference], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.RefReactivePower
```

````

````{py:attribute} RiseFallLimit
:canonical: altdss.InvControl.InvControlBatchProperties.RiseFallLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.RiseFallLimit
```

````

````{py:attribute} VSetPoint
:canonical: altdss.InvControl.InvControlBatchProperties.VSetPoint
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.VSetPoint
```

````

````{py:attribute} VVC_Curve1
:canonical: altdss.InvControl.InvControlBatchProperties.VVC_Curve1
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.VVC_Curve1
```

````

````{py:attribute} VarChangeTolerance
:canonical: altdss.InvControl.InvControlBatchProperties.VarChangeTolerance
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.VarChangeTolerance
```

````

````{py:attribute} VoltWattCH_Curve
:canonical: altdss.InvControl.InvControlBatchProperties.VoltWattCH_Curve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.VoltWattCH_Curve
```

````

````{py:attribute} VoltWattYAxis
:canonical: altdss.InvControl.InvControlBatchProperties.VoltWattYAxis
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlVoltWattYAxis, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.InvControlVoltWattYAxis], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.VoltWattYAxis
```

````

````{py:attribute} VoltWatt_Curve
:canonical: altdss.InvControl.InvControlBatchProperties.VoltWatt_Curve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.VoltWatt_Curve
```

````

````{py:attribute} VoltageChangeTolerance
:canonical: altdss.InvControl.InvControlBatchProperties.VoltageChangeTolerance
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.VoltageChangeTolerance
```

````

````{py:attribute} Voltage_CurveX_Ref
:canonical: altdss.InvControl.InvControlBatchProperties.Voltage_CurveX_Ref
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlVoltageCurveXRef, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.InvControlVoltageCurveXRef], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.Voltage_CurveX_Ref
```

````

````{py:attribute} WattPF_Curve
:canonical: altdss.InvControl.InvControlBatchProperties.WattPF_Curve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.WattPF_Curve
```

````

````{py:attribute} WattVar_Curve
:canonical: altdss.InvControl.InvControlBatchProperties.WattVar_Curve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.WattVar_Curve
```

````

````{py:method} __contains__()
:canonical: altdss.InvControl.InvControlBatchProperties.__contains__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.InvControl.InvControlBatchProperties.__delattr__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.InvControl.InvControlBatchProperties.__delitem__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.InvControl.InvControlBatchProperties.__dir__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.InvControl.InvControlBatchProperties.__format__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.InvControl.InvControlBatchProperties.__ge__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.InvControl.InvControlBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.InvControl.InvControlBatchProperties.__getitem__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.InvControl.InvControlBatchProperties.__getstate__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.InvControl.InvControlBatchProperties.__gt__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.InvControl.InvControlBatchProperties.__init__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.InvControl.InvControlBatchProperties.__ior__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.InvControl.InvControlBatchProperties.__iter__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.InvControl.InvControlBatchProperties.__le__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.InvControl.InvControlBatchProperties.__len__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.InvControl.InvControlBatchProperties.__lt__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.InvControl.InvControlBatchProperties.__ne__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.InvControl.InvControlBatchProperties.__new__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.InvControl.InvControlBatchProperties.__or__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.InvControl.InvControlBatchProperties.__reduce__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.InvControl.InvControlBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.InvControl.InvControlBatchProperties.__repr__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.InvControl.InvControlBatchProperties.__reversed__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.InvControl.InvControlBatchProperties.__ror__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.InvControl.InvControlBatchProperties.__setitem__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.InvControl.InvControlBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.InvControl.InvControlBatchProperties.__str__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.InvControl.InvControlBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.InvControl.InvControlBatchProperties.clear

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.InvControl.InvControlBatchProperties.copy

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.InvControl.InvControlBatchProperties.get

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.InvControl.InvControlBatchProperties.items

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.InvControl.InvControlBatchProperties.keys

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.InvControl.InvControlBatchProperties.pop

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.InvControl.InvControlBatchProperties.popitem

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.InvControl.InvControlBatchProperties.setdefault

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.InvControl.InvControlBatchProperties.update

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.InvControl.InvControlBatchProperties.values

```{autodoc2-docstring} altdss.InvControl.InvControlBatchProperties.values
```

````

`````

`````{py:class} InvControlProperties()
:canonical: altdss.InvControl.InvControlProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.InvControl.InvControlProperties
```

````{py:attribute} ActivePChangeTolerance
:canonical: altdss.InvControl.InvControlProperties.ActivePChangeTolerance
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.ActivePChangeTolerance
```

````

````{py:attribute} ArGraHiV
:canonical: altdss.InvControl.InvControlProperties.ArGraHiV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.ArGraHiV
```

````

````{py:attribute} ArGraLowV
:canonical: altdss.InvControl.InvControlProperties.ArGraLowV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.ArGraLowV
```

````

````{py:attribute} AvgWindowLen
:canonical: altdss.InvControl.InvControlProperties.AvgWindowLen
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.AvgWindowLen
```

````

````{py:attribute} BaseFreq
:canonical: altdss.InvControl.InvControlProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.BaseFreq
```

````

````{py:attribute} CombiMode
:canonical: altdss.InvControl.InvControlProperties.CombiMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlCombiMode]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.CombiMode
```

````

````{py:attribute} ControlModel
:canonical: altdss.InvControl.InvControlProperties.ControlModel
:type: typing.Union[int, altdss.enums.InvControlControlModel]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.ControlModel
```

````

````{py:attribute} DERList
:canonical: altdss.InvControl.InvControlProperties.DERList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.DERList
```

````

````{py:attribute} DbVMax
:canonical: altdss.InvControl.InvControlProperties.DbVMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.DbVMax
```

````

````{py:attribute} DbVMin
:canonical: altdss.InvControl.InvControlProperties.DbVMin
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.DbVMin
```

````

````{py:attribute} DeltaP_Factor
:canonical: altdss.InvControl.InvControlProperties.DeltaP_Factor
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.DeltaP_Factor
```

````

````{py:attribute} DeltaQ_Factor
:canonical: altdss.InvControl.InvControlProperties.DeltaQ_Factor
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.DeltaQ_Factor
```

````

````{py:attribute} DynReacAvgWindowLen
:canonical: altdss.InvControl.InvControlProperties.DynReacAvgWindowLen
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.DynReacAvgWindowLen
```

````

````{py:attribute} Enabled
:canonical: altdss.InvControl.InvControlProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.InvControl.InvControlProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.EventLog
```

````

````{py:attribute} Hysteresis_Offset
:canonical: altdss.InvControl.InvControlProperties.Hysteresis_Offset
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.Hysteresis_Offset
```

````

````{py:attribute} LPFTau
:canonical: altdss.InvControl.InvControlProperties.LPFTau
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.LPFTau
```

````

````{py:attribute} Like
:canonical: altdss.InvControl.InvControlProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.Like
```

````

````{py:attribute} Mode
:canonical: altdss.InvControl.InvControlProperties.Mode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlControlMode]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.Mode
```

````

````{py:attribute} MonBus
:canonical: altdss.InvControl.InvControlProperties.MonBus
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.MonBus
```

````

````{py:attribute} MonBusesVBase
:canonical: altdss.InvControl.InvControlProperties.MonBusesVBase
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.MonBusesVBase
```

````

````{py:attribute} MonVoltageCalc
:canonical: altdss.InvControl.InvControlProperties.MonVoltageCalc
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitoredPhase]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.MonVoltageCalc
```

````

````{py:attribute} RateOfChangeMode
:canonical: altdss.InvControl.InvControlProperties.RateOfChangeMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlRateOfChangeMode]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.RateOfChangeMode
```

````

````{py:attribute} RefReactivePower
:canonical: altdss.InvControl.InvControlProperties.RefReactivePower
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlReactivePowerReference]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.RefReactivePower
```

````

````{py:attribute} RiseFallLimit
:canonical: altdss.InvControl.InvControlProperties.RiseFallLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.RiseFallLimit
```

````

````{py:attribute} VSetPoint
:canonical: altdss.InvControl.InvControlProperties.VSetPoint
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.VSetPoint
```

````

````{py:attribute} VVC_Curve1
:canonical: altdss.InvControl.InvControlProperties.VVC_Curve1
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.VVC_Curve1
```

````

````{py:attribute} VarChangeTolerance
:canonical: altdss.InvControl.InvControlProperties.VarChangeTolerance
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.VarChangeTolerance
```

````

````{py:attribute} VoltWattCH_Curve
:canonical: altdss.InvControl.InvControlProperties.VoltWattCH_Curve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.VoltWattCH_Curve
```

````

````{py:attribute} VoltWattYAxis
:canonical: altdss.InvControl.InvControlProperties.VoltWattYAxis
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlVoltWattYAxis]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.VoltWattYAxis
```

````

````{py:attribute} VoltWatt_Curve
:canonical: altdss.InvControl.InvControlProperties.VoltWatt_Curve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.VoltWatt_Curve
```

````

````{py:attribute} VoltageChangeTolerance
:canonical: altdss.InvControl.InvControlProperties.VoltageChangeTolerance
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.VoltageChangeTolerance
```

````

````{py:attribute} Voltage_CurveX_Ref
:canonical: altdss.InvControl.InvControlProperties.Voltage_CurveX_Ref
:type: typing.Union[typing.AnyStr, int, altdss.enums.InvControlVoltageCurveXRef]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.Voltage_CurveX_Ref
```

````

````{py:attribute} WattPF_Curve
:canonical: altdss.InvControl.InvControlProperties.WattPF_Curve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.WattPF_Curve
```

````

````{py:attribute} WattVar_Curve
:canonical: altdss.InvControl.InvControlProperties.WattVar_Curve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.WattVar_Curve
```

````

````{py:method} __contains__()
:canonical: altdss.InvControl.InvControlProperties.__contains__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.InvControl.InvControlProperties.__delattr__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.InvControl.InvControlProperties.__delitem__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.InvControl.InvControlProperties.__dir__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.InvControl.InvControlProperties.__format__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.InvControl.InvControlProperties.__ge__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.InvControl.InvControlProperties.__getattribute__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.InvControl.InvControlProperties.__getitem__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.InvControl.InvControlProperties.__getstate__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.InvControl.InvControlProperties.__gt__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.InvControl.InvControlProperties.__init__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.InvControl.InvControlProperties.__ior__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.InvControl.InvControlProperties.__iter__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.InvControl.InvControlProperties.__le__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.InvControl.InvControlProperties.__len__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.InvControl.InvControlProperties.__lt__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.InvControl.InvControlProperties.__ne__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.InvControl.InvControlProperties.__new__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.InvControl.InvControlProperties.__or__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.InvControl.InvControlProperties.__reduce__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.InvControl.InvControlProperties.__reduce_ex__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.InvControl.InvControlProperties.__repr__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.InvControl.InvControlProperties.__reversed__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.InvControl.InvControlProperties.__ror__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.InvControl.InvControlProperties.__setitem__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.InvControl.InvControlProperties.__sizeof__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.InvControl.InvControlProperties.__str__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.InvControl.InvControlProperties.__subclasshook__

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.InvControl.InvControlProperties.clear

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.InvControl.InvControlProperties.copy

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.copy
```

````

````{py:method} get()
:canonical: altdss.InvControl.InvControlProperties.get

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.get
```

````

````{py:method} items()
:canonical: altdss.InvControl.InvControlProperties.items

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.items
```

````

````{py:method} keys()
:canonical: altdss.InvControl.InvControlProperties.keys

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.InvControl.InvControlProperties.pop

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.InvControl.InvControlProperties.popitem

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.InvControl.InvControlProperties.setdefault

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.InvControl.InvControlProperties.update

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.update
```

````

````{py:method} values()
:canonical: altdss.InvControl.InvControlProperties.values

```{autodoc2-docstring} altdss.InvControl.InvControlProperties.values
```

````

`````
