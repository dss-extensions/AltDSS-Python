# {py:mod}`altdss.Reactor`

```{py:module} altdss.Reactor
```

```{autodoc2-docstring} altdss.Reactor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IReactor <altdss.Reactor.IReactor>`
  - ```{autodoc2-docstring} altdss.Reactor.IReactor
    :summary:
    ```
* - {py:obj}`Reactor <altdss.Reactor.Reactor>`
  - ```{autodoc2-docstring} altdss.Reactor.Reactor
    :summary:
    ```
* - {py:obj}`ReactorBatch <altdss.Reactor.ReactorBatch>`
  - ```{autodoc2-docstring} altdss.Reactor.ReactorBatch
    :summary:
    ```
* - {py:obj}`ReactorBatchProperties <altdss.Reactor.ReactorBatchProperties>`
  - ```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties
    :summary:
    ```
* - {py:obj}`ReactorProperties <altdss.Reactor.ReactorProperties>`
  - ```{autodoc2-docstring} altdss.Reactor.ReactorProperties
    :summary:
    ```
````

### API

`````{py:class} IReactor(iobj)
:canonical: altdss.Reactor.IReactor

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Reactor.ReactorBatch`

```{autodoc2-docstring} altdss.Reactor.IReactor
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.AccumulatedL

```{autodoc2-docstring} altdss.Reactor.IReactor.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Reactor.IReactor.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Reactor.IReactor.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Reactor.IReactor.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Bus2
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.IReactor.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Reactor.IReactor.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.IReactor.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Reactor.IReactor.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Reactor.IReactor.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Reactor.IReactor.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.IReactor.Currents

```{autodoc2-docstring} altdss.Reactor.IReactor.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.CurrentsMagAng

```{autodoc2-docstring} altdss.Reactor.IReactor.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Reactor.IReactor.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Reactor.IReactor.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.Reactor.IReactor.EnergyMeter

```{autodoc2-docstring} altdss.Reactor.IReactor.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Reactor.IReactor.EnergyMeterName

```{autodoc2-docstring} altdss.Reactor.IReactor.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Reactor.IReactor.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.FromTerminal

```{autodoc2-docstring} altdss.Reactor.IReactor.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Reactor.IReactor.FullName

```{autodoc2-docstring} altdss.Reactor.IReactor.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Reactor.IReactor.GUID

```{autodoc2-docstring} altdss.Reactor.IReactor.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.Handle

```{autodoc2-docstring} altdss.Reactor.IReactor.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Reactor.IReactor.HasOCPDevice

```{autodoc2-docstring} altdss.Reactor.IReactor.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Reactor.IReactor.HasSwitchControl

```{autodoc2-docstring} altdss.Reactor.IReactor.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Reactor.IReactor.HasVoltControl

```{autodoc2-docstring} altdss.Reactor.IReactor.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Reactor.IReactor.IsIsolated

```{autodoc2-docstring} altdss.Reactor.IReactor.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Reactor.IReactor.IsShunt

```{autodoc2-docstring} altdss.Reactor.IReactor.IsShunt
```

````

````{py:attribute} LCurve
:canonical: altdss.Reactor.IReactor.LCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.LCurve
```

````

````{py:attribute} LCurve_str
:canonical: altdss.Reactor.IReactor.LCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.LCurve_str
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.Lambda

```{autodoc2-docstring} altdss.Reactor.IReactor.Lambda
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Reactor.IReactor.Like

```{autodoc2-docstring} altdss.Reactor.IReactor.Like
```

````

````{py:attribute} LmH
:canonical: altdss.Reactor.IReactor.LmH
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.LmH
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.IReactor.Losses

```{autodoc2-docstring} altdss.Reactor.IReactor.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.MaxCurrent

```{autodoc2-docstring} altdss.Reactor.IReactor.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Reactor.IReactor.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Reactor.IReactor.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Reactor.IReactor.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.NumConductors

```{autodoc2-docstring} altdss.Reactor.IReactor.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.NumControllers

```{autodoc2-docstring} altdss.Reactor.IReactor.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.NumCustomers

```{autodoc2-docstring} altdss.Reactor.IReactor.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.NumPhases

```{autodoc2-docstring} altdss.Reactor.IReactor.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.NumTerminals

```{autodoc2-docstring} altdss.Reactor.IReactor.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Reactor.IReactor.OCPDevice

```{autodoc2-docstring} altdss.Reactor.IReactor.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.OCPDeviceIndex

```{autodoc2-docstring} altdss.Reactor.IReactor.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Reactor.IReactor.OCPDeviceType

```{autodoc2-docstring} altdss.Reactor.IReactor.OCPDeviceType
```

````

````{py:attribute} Parallel
:canonical: altdss.Reactor.IReactor.Parallel
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Parallel
```

````

````{py:method} ParentPDElement() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.Reactor.IReactor.ParentPDElement

```{autodoc2-docstring} altdss.Reactor.IReactor.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.IReactor.PhaseLosses

```{autodoc2-docstring} altdss.Reactor.IReactor.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Reactor.IReactor.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.IReactor.Powers

```{autodoc2-docstring} altdss.Reactor.IReactor.Powers
```

````

````{py:attribute} R
:canonical: altdss.Reactor.IReactor.R
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.R
```

````

````{py:attribute} RCurve
:canonical: altdss.Reactor.IReactor.RCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.RCurve
```

````

````{py:attribute} RCurve_str
:canonical: altdss.Reactor.IReactor.RCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.RCurve_str
```

````

````{py:attribute} RMatrix
:canonical: altdss.Reactor.IReactor.RMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.RMatrix
```

````

````{py:attribute} Repair
:canonical: altdss.Reactor.IReactor.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Repair
```

````

````{py:attribute} Rp
:canonical: altdss.Reactor.IReactor.Rp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Rp
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.SectionID

```{autodoc2-docstring} altdss.Reactor.IReactor.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.SeqCurrents

```{autodoc2-docstring} altdss.Reactor.IReactor.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.IReactor.SeqPowers

```{autodoc2-docstring} altdss.Reactor.IReactor.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.SeqVoltages

```{autodoc2-docstring} altdss.Reactor.IReactor.SeqVoltages
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Reactor.IReactor.TotalCustomers

```{autodoc2-docstring} altdss.Reactor.IReactor.TotalCustomers
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.TotalKilometers

```{autodoc2-docstring} altdss.Reactor.IReactor.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.TotalMiles

```{autodoc2-docstring} altdss.Reactor.IReactor.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.IReactor.TotalPowers

```{autodoc2-docstring} altdss.Reactor.IReactor.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.IReactor.Voltages

```{autodoc2-docstring} altdss.Reactor.IReactor.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.VoltagesMagAng

```{autodoc2-docstring} altdss.Reactor.IReactor.VoltagesMagAng
```

````

````{py:attribute} X
:canonical: altdss.Reactor.IReactor.X
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.X
```

````

````{py:attribute} XMatrix
:canonical: altdss.Reactor.IReactor.XMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.XMatrix
```

````

````{py:attribute} Z0
:canonical: altdss.Reactor.IReactor.Z0
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Z0
```

````

````{py:attribute} Z1
:canonical: altdss.Reactor.IReactor.Z1
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Z1
```

````

````{py:attribute} Z2
:canonical: altdss.Reactor.IReactor.Z2
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.Z2
```

````

````{py:method} __call__()
:canonical: altdss.Reactor.IReactor.__call__

```{autodoc2-docstring} altdss.Reactor.IReactor.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Reactor.IReactor.__contains__

```{autodoc2-docstring} altdss.Reactor.IReactor.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Reactor.IReactor.__getitem__

```{autodoc2-docstring} altdss.Reactor.IReactor.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Reactor.IReactor.__init__

```{autodoc2-docstring} altdss.Reactor.IReactor.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Reactor.IReactor.__iter__

```{autodoc2-docstring} altdss.Reactor.IReactor.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Reactor.IReactor.__len__

```{autodoc2-docstring} altdss.Reactor.IReactor.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Reactor.IReactor.batch

```{autodoc2-docstring} altdss.Reactor.IReactor.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.Reactor.ReactorBatchProperties]) -> altdss.Reactor.ReactorBatch
:canonical: altdss.Reactor.IReactor.batch_new

```{autodoc2-docstring} altdss.Reactor.IReactor.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Reactor.IReactor.begin_edit

```{autodoc2-docstring} altdss.Reactor.IReactor.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Reactor.ReactorBatchProperties]) -> altdss.Reactor.ReactorBatch
:canonical: altdss.Reactor.IReactor.edit

```{autodoc2-docstring} altdss.Reactor.IReactor.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Reactor.IReactor.end_edit

```{autodoc2-docstring} altdss.Reactor.IReactor.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Reactor.IReactor.find

```{autodoc2-docstring} altdss.Reactor.IReactor.find
```

````

````{py:attribute} kV
:canonical: altdss.Reactor.IReactor.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.kV
```

````

````{py:attribute} kvar
:canonical: altdss.Reactor.IReactor.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.kvar
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.Reactor.ReactorProperties]) -> altdss.Reactor.Reactor
:canonical: altdss.Reactor.IReactor.new

```{autodoc2-docstring} altdss.Reactor.IReactor.new
```

````

````{py:method} pctEmergency(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.pctEmergency

```{autodoc2-docstring} altdss.Reactor.IReactor.pctEmergency
```

````

````{py:method} pctNormal(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.Reactor.IReactor.pctNormal

```{autodoc2-docstring} altdss.Reactor.IReactor.pctNormal
```

````

````{py:attribute} pctPerm
:canonical: altdss.Reactor.IReactor.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.IReactor.pctPerm
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Reactor.IReactor.to_json

```{autodoc2-docstring} altdss.Reactor.IReactor.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Reactor.IReactor.to_list

```{autodoc2-docstring} altdss.Reactor.IReactor.to_list
```

````

`````

`````{py:class} Reactor(api_util, ptr)
:canonical: altdss.Reactor.Reactor

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PDElement.PDElementMixin`

```{autodoc2-docstring} altdss.Reactor.Reactor
```

````{py:method} AccumulatedL() -> float
:canonical: altdss.Reactor.Reactor.AccumulatedL

```{autodoc2-docstring} altdss.Reactor.Reactor.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Reactor.Reactor.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Reactor.Reactor.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Reactor.Reactor.Bus2
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Bus2
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Reactor.Reactor.Close

```{autodoc2-docstring} altdss.Reactor.Reactor.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.Reactor.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Reactor.Reactor.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.Reactor.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Reactor.Reactor.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Reactor.Reactor.Conn
:type: altdss.enums.Connection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Reactor.Reactor.Conn_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.Reactor.Currents

```{autodoc2-docstring} altdss.Reactor.Reactor.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.Reactor.Reactor.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.DisplayName
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Reactor.Reactor.EmergAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Reactor.Reactor.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Enabled
```

````

````{py:method} EnergyMeter() -> typing.Optional[altdss.DSSObj.DSSObj]
:canonical: altdss.Reactor.Reactor.EnergyMeter

```{autodoc2-docstring} altdss.Reactor.Reactor.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Reactor.Reactor.EnergyMeterName

```{autodoc2-docstring} altdss.Reactor.Reactor.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Reactor.Reactor.FaultRate
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.FaultRate
```

````

````{py:method} FromTerminal() -> int
:canonical: altdss.Reactor.Reactor.FromTerminal

```{autodoc2-docstring} altdss.Reactor.Reactor.FromTerminal
```

````

````{py:method} FullName() -> str
:canonical: altdss.Reactor.Reactor.FullName

```{autodoc2-docstring} altdss.Reactor.Reactor.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Reactor.Reactor.GUID

```{autodoc2-docstring} altdss.Reactor.Reactor.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.Reactor.Reactor.Handle

```{autodoc2-docstring} altdss.Reactor.Reactor.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Reactor.Reactor.HasOCPDevice

```{autodoc2-docstring} altdss.Reactor.Reactor.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Reactor.Reactor.HasSwitchControl

```{autodoc2-docstring} altdss.Reactor.Reactor.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Reactor.Reactor.HasVoltControl

```{autodoc2-docstring} altdss.Reactor.Reactor.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Reactor.Reactor.IsIsolated

```{autodoc2-docstring} altdss.Reactor.Reactor.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Reactor.Reactor.IsOpen

```{autodoc2-docstring} altdss.Reactor.Reactor.IsOpen
```

````

````{py:method} IsShunt() -> bool
:canonical: altdss.Reactor.Reactor.IsShunt

```{autodoc2-docstring} altdss.Reactor.Reactor.IsShunt
```

````

````{py:attribute} LCurve
:canonical: altdss.Reactor.Reactor.LCurve
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.LCurve
```

````

````{py:attribute} LCurve_str
:canonical: altdss.Reactor.Reactor.LCurve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.LCurve_str
```

````

````{py:method} Lambda() -> float
:canonical: altdss.Reactor.Reactor.Lambda

```{autodoc2-docstring} altdss.Reactor.Reactor.Lambda
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Reactor.Reactor.Like

```{autodoc2-docstring} altdss.Reactor.Reactor.Like
```

````

````{py:attribute} LmH
:canonical: altdss.Reactor.Reactor.LmH
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.LmH
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Reactor.Reactor.Losses

```{autodoc2-docstring} altdss.Reactor.Reactor.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Reactor.Reactor.MaxCurrent

```{autodoc2-docstring} altdss.Reactor.Reactor.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Reactor.Reactor.Name
:type: str

```{autodoc2-docstring} altdss.Reactor.Reactor.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Reactor.Reactor.NodeOrder

```{autodoc2-docstring} altdss.Reactor.Reactor.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Reactor.Reactor.NodeRef

```{autodoc2-docstring} altdss.Reactor.Reactor.NodeRef
```

````

````{py:attribute} NormAmps
:canonical: altdss.Reactor.Reactor.NormAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.NormAmps
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Reactor.Reactor.NumConductors

```{autodoc2-docstring} altdss.Reactor.Reactor.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Reactor.Reactor.NumControllers

```{autodoc2-docstring} altdss.Reactor.Reactor.NumControllers
```

````

````{py:method} NumCustomers() -> int
:canonical: altdss.Reactor.Reactor.NumCustomers

```{autodoc2-docstring} altdss.Reactor.Reactor.NumCustomers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Reactor.Reactor.NumPhases

```{autodoc2-docstring} altdss.Reactor.Reactor.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Reactor.Reactor.NumTerminals

```{autodoc2-docstring} altdss.Reactor.Reactor.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Reactor.Reactor.OCPDevice

```{autodoc2-docstring} altdss.Reactor.Reactor.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Reactor.Reactor.OCPDeviceIndex

```{autodoc2-docstring} altdss.Reactor.Reactor.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Reactor.Reactor.OCPDeviceType

```{autodoc2-docstring} altdss.Reactor.Reactor.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Reactor.Reactor.Open

```{autodoc2-docstring} altdss.Reactor.Reactor.Open
```

````

````{py:attribute} Parallel
:canonical: altdss.Reactor.Reactor.Parallel
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Parallel
```

````

````{py:method} ParentPDElement() -> typing.Optional[altdss.DSSObj.DSSObj]
:canonical: altdss.Reactor.Reactor.ParentPDElement

```{autodoc2-docstring} altdss.Reactor.Reactor.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.Reactor.PhaseLosses

```{autodoc2-docstring} altdss.Reactor.Reactor.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Reactor.Reactor.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.Reactor.Powers

```{autodoc2-docstring} altdss.Reactor.Reactor.Powers
```

````

````{py:attribute} R
:canonical: altdss.Reactor.Reactor.R
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.R
```

````

````{py:attribute} RCurve
:canonical: altdss.Reactor.Reactor.RCurve
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.RCurve
```

````

````{py:attribute} RCurve_str
:canonical: altdss.Reactor.Reactor.RCurve_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.RCurve_str
```

````

````{py:attribute} RMatrix
:canonical: altdss.Reactor.Reactor.RMatrix
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.RMatrix
```

````

````{py:attribute} Repair
:canonical: altdss.Reactor.Reactor.Repair
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Repair
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Reactor.Reactor.Residuals

```{autodoc2-docstring} altdss.Reactor.Reactor.Residuals
```

````

````{py:attribute} Rp
:canonical: altdss.Reactor.Reactor.Rp
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Rp
```

````

````{py:method} SectionID() -> int
:canonical: altdss.Reactor.Reactor.SectionID

```{autodoc2-docstring} altdss.Reactor.Reactor.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Reactor.Reactor.SeqCurrents

```{autodoc2-docstring} altdss.Reactor.Reactor.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.Reactor.SeqPowers

```{autodoc2-docstring} altdss.Reactor.Reactor.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Reactor.Reactor.SeqVoltages

```{autodoc2-docstring} altdss.Reactor.Reactor.SeqVoltages
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.Reactor.Reactor.TotalCustomers

```{autodoc2-docstring} altdss.Reactor.Reactor.TotalCustomers
```

````

````{py:method} TotalKilometers() -> float
:canonical: altdss.Reactor.Reactor.TotalKilometers

```{autodoc2-docstring} altdss.Reactor.Reactor.TotalKilometers
```

````

````{py:method} TotalMiles() -> float
:canonical: altdss.Reactor.Reactor.TotalMiles

```{autodoc2-docstring} altdss.Reactor.Reactor.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.Reactor.TotalPowers

```{autodoc2-docstring} altdss.Reactor.Reactor.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.Reactor.Voltages

```{autodoc2-docstring} altdss.Reactor.Reactor.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Reactor.Reactor.VoltagesMagAng

```{autodoc2-docstring} altdss.Reactor.Reactor.VoltagesMagAng
```

````

````{py:attribute} X
:canonical: altdss.Reactor.Reactor.X
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.X
```

````

````{py:attribute} XMatrix
:canonical: altdss.Reactor.Reactor.XMatrix
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.XMatrix
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.Reactor.YPrim

```{autodoc2-docstring} altdss.Reactor.Reactor.YPrim
```

````

````{py:attribute} Z0
:canonical: altdss.Reactor.Reactor.Z0
:type: complex
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Z0
```

````

````{py:attribute} Z1
:canonical: altdss.Reactor.Reactor.Z1
:type: complex
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Z1
```

````

````{py:attribute} Z2
:canonical: altdss.Reactor.Reactor.Z2
:type: complex
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.Z2
```

````

````{py:method} __hash__()
:canonical: altdss.Reactor.Reactor.__hash__

```{autodoc2-docstring} altdss.Reactor.Reactor.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Reactor.Reactor.__init__

```{autodoc2-docstring} altdss.Reactor.Reactor.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Reactor.Reactor.__ne__

```{autodoc2-docstring} altdss.Reactor.Reactor.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Reactor.Reactor.__repr__

```{autodoc2-docstring} altdss.Reactor.Reactor.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Reactor.Reactor.begin_edit

```{autodoc2-docstring} altdss.Reactor.Reactor.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Reactor.ReactorProperties]) -> altdss.Reactor.Reactor
:canonical: altdss.Reactor.Reactor.edit

```{autodoc2-docstring} altdss.Reactor.Reactor.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Reactor.Reactor.end_edit

```{autodoc2-docstring} altdss.Reactor.Reactor.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Reactor.Reactor.kV
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.kV
```

````

````{py:attribute} kvar
:canonical: altdss.Reactor.Reactor.kvar
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.kvar
```

````

````{py:method} pctEmergency(allNodes=False) -> float
:canonical: altdss.Reactor.Reactor.pctEmergency

```{autodoc2-docstring} altdss.Reactor.Reactor.pctEmergency
```

````

````{py:method} pctNormal(allNodes=False) -> float
:canonical: altdss.Reactor.Reactor.pctNormal

```{autodoc2-docstring} altdss.Reactor.Reactor.pctNormal
```

````

````{py:attribute} pctPerm
:canonical: altdss.Reactor.Reactor.pctPerm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.Reactor.pctPerm
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Reactor.Reactor.to_json

```{autodoc2-docstring} altdss.Reactor.Reactor.to_json
```

````

`````

`````{py:class} ReactorBatch(api_util, **kwargs)
:canonical: altdss.Reactor.ReactorBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PDElement.PDElementBatchMixin`

```{autodoc2-docstring} altdss.Reactor.ReactorBatch
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.AccumulatedL

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Reactor.ReactorBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Reactor.ReactorBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Reactor.ReactorBatch.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Bus2
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.ReactorBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.ReactorBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Reactor.ReactorBatch.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Reactor.ReactorBatch.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Conn_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.ReactorBatch.Currents

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Reactor.ReactorBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Reactor.ReactorBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.Reactor.ReactorBatch.EnergyMeter

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Reactor.ReactorBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Reactor.ReactorBatch.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.FromTerminal

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Reactor.ReactorBatch.FullName

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Reactor.ReactorBatch.GUID

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.Handle

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Reactor.ReactorBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Reactor.ReactorBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Reactor.ReactorBatch.HasVoltControl

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Reactor.ReactorBatch.IsIsolated

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Reactor.ReactorBatch.IsShunt

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.IsShunt
```

````

````{py:attribute} LCurve
:canonical: altdss.Reactor.ReactorBatch.LCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.LCurve
```

````

````{py:attribute} LCurve_str
:canonical: altdss.Reactor.ReactorBatch.LCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.LCurve_str
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.Lambda

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Lambda
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Reactor.ReactorBatch.Like

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Like
```

````

````{py:attribute} LmH
:canonical: altdss.Reactor.ReactorBatch.LmH
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.LmH
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.ReactorBatch.Losses

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.MaxCurrent

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Reactor.ReactorBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Reactor.ReactorBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.NumConductors

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.NumControllers

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.NumCustomers

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.NumPhases

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.NumTerminals

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Reactor.ReactorBatch.OCPDevice

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Reactor.ReactorBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.OCPDeviceType
```

````

````{py:attribute} Parallel
:canonical: altdss.Reactor.ReactorBatch.Parallel
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Parallel
```

````

````{py:method} ParentPDElement() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.Reactor.ReactorBatch.ParentPDElement

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.ReactorBatch.PhaseLosses

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Reactor.ReactorBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.ReactorBatch.Powers

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Powers
```

````

````{py:attribute} R
:canonical: altdss.Reactor.ReactorBatch.R
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.R
```

````

````{py:attribute} RCurve
:canonical: altdss.Reactor.ReactorBatch.RCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.RCurve
```

````

````{py:attribute} RCurve_str
:canonical: altdss.Reactor.ReactorBatch.RCurve_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.RCurve_str
```

````

````{py:attribute} RMatrix
:canonical: altdss.Reactor.ReactorBatch.RMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.RMatrix
```

````

````{py:attribute} Repair
:canonical: altdss.Reactor.ReactorBatch.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Repair
```

````

````{py:attribute} Rp
:canonical: altdss.Reactor.ReactorBatch.Rp
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Rp
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.SectionID

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.SeqCurrents

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.ReactorBatch.SeqPowers

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.SeqVoltages

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.SeqVoltages
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Reactor.ReactorBatch.TotalCustomers

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.TotalCustomers
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.TotalKilometers

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.TotalMiles

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.ReactorBatch.TotalPowers

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Reactor.ReactorBatch.Voltages

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.VoltagesMagAng
```

````

````{py:attribute} X
:canonical: altdss.Reactor.ReactorBatch.X
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.X
```

````

````{py:attribute} XMatrix
:canonical: altdss.Reactor.ReactorBatch.XMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.XMatrix
```

````

````{py:attribute} Z0
:canonical: altdss.Reactor.ReactorBatch.Z0
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Z0
```

````

````{py:attribute} Z1
:canonical: altdss.Reactor.ReactorBatch.Z1
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Z1
```

````

````{py:attribute} Z2
:canonical: altdss.Reactor.ReactorBatch.Z2
:type: typing.List[complex]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.Z2
```

````

````{py:method} __call__()
:canonical: altdss.Reactor.ReactorBatch.__call__

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Reactor.ReactorBatch.__getitem__

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Reactor.ReactorBatch.__init__

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Reactor.ReactorBatch.__iter__

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Reactor.ReactorBatch.__len__

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Reactor.ReactorBatch.batch

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Reactor.ReactorBatch.begin_edit

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Reactor.ReactorBatchProperties]) -> altdss.Reactor.ReactorBatch
:canonical: altdss.Reactor.ReactorBatch.edit

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Reactor.ReactorBatch.end_edit

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Reactor.ReactorBatch.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.kV
```

````

````{py:attribute} kvar
:canonical: altdss.Reactor.ReactorBatch.kvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.kvar
```

````

````{py:method} pctEmergency(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.pctEmergency

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.pctEmergency
```

````

````{py:method} pctNormal(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.Reactor.ReactorBatch.pctNormal

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.pctNormal
```

````

````{py:attribute} pctPerm
:canonical: altdss.Reactor.ReactorBatch.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.pctPerm
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Reactor.ReactorBatch.to_json

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Reactor.ReactorBatch.to_list

```{autodoc2-docstring} altdss.Reactor.ReactorBatch.to_list
```

````

`````

`````{py:class} ReactorBatchProperties()
:canonical: altdss.Reactor.ReactorBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Reactor.ReactorBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Reactor.ReactorBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Reactor.ReactorBatchProperties.Bus2
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Bus2
```

````

````{py:attribute} Conn
:canonical: altdss.Reactor.ReactorBatchProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.Connection], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Conn
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Reactor.ReactorBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Reactor.ReactorBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.Reactor.ReactorBatchProperties.FaultRate
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.FaultRate
```

````

````{py:attribute} LCurve
:canonical: altdss.Reactor.ReactorBatchProperties.LCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.LCurve
```

````

````{py:attribute} Like
:canonical: altdss.Reactor.ReactorBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Like
```

````

````{py:attribute} LmH
:canonical: altdss.Reactor.ReactorBatchProperties.LmH
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.LmH
```

````

````{py:attribute} NormAmps
:canonical: altdss.Reactor.ReactorBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.NormAmps
```

````

````{py:attribute} Parallel
:canonical: altdss.Reactor.ReactorBatchProperties.Parallel
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Parallel
```

````

````{py:attribute} Phases
:canonical: altdss.Reactor.ReactorBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Phases
```

````

````{py:attribute} R
:canonical: altdss.Reactor.ReactorBatchProperties.R
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.R
```

````

````{py:attribute} RCurve
:canonical: altdss.Reactor.ReactorBatchProperties.RCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.RCurve
```

````

````{py:attribute} RMatrix
:canonical: altdss.Reactor.ReactorBatchProperties.RMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.RMatrix
```

````

````{py:attribute} Repair
:canonical: altdss.Reactor.ReactorBatchProperties.Repair
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Repair
```

````

````{py:attribute} Rp
:canonical: altdss.Reactor.ReactorBatchProperties.Rp
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Rp
```

````

````{py:attribute} X
:canonical: altdss.Reactor.ReactorBatchProperties.X
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.X
```

````

````{py:attribute} XMatrix
:canonical: altdss.Reactor.ReactorBatchProperties.XMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.XMatrix
```

````

````{py:attribute} Z0
:canonical: altdss.Reactor.ReactorBatchProperties.Z0
:type: typing.Union[complex, typing.List[complex]]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Z0
```

````

````{py:attribute} Z1
:canonical: altdss.Reactor.ReactorBatchProperties.Z1
:type: typing.Union[complex, typing.List[complex]]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Z1
```

````

````{py:attribute} Z2
:canonical: altdss.Reactor.ReactorBatchProperties.Z2
:type: typing.Union[complex, typing.List[complex]]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.Z2
```

````

````{py:method} __contains__()
:canonical: altdss.Reactor.ReactorBatchProperties.__contains__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Reactor.ReactorBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Reactor.ReactorBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Reactor.ReactorBatchProperties.__dir__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Reactor.ReactorBatchProperties.__format__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Reactor.ReactorBatchProperties.__ge__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Reactor.ReactorBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Reactor.ReactorBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Reactor.ReactorBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Reactor.ReactorBatchProperties.__gt__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Reactor.ReactorBatchProperties.__init__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Reactor.ReactorBatchProperties.__ior__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Reactor.ReactorBatchProperties.__iter__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Reactor.ReactorBatchProperties.__le__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Reactor.ReactorBatchProperties.__len__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Reactor.ReactorBatchProperties.__lt__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Reactor.ReactorBatchProperties.__ne__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Reactor.ReactorBatchProperties.__new__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Reactor.ReactorBatchProperties.__or__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Reactor.ReactorBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Reactor.ReactorBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Reactor.ReactorBatchProperties.__repr__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Reactor.ReactorBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Reactor.ReactorBatchProperties.__ror__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Reactor.ReactorBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Reactor.ReactorBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Reactor.ReactorBatchProperties.__str__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Reactor.ReactorBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Reactor.ReactorBatchProperties.clear

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Reactor.ReactorBatchProperties.copy

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Reactor.ReactorBatchProperties.get

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Reactor.ReactorBatchProperties.items

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Reactor.ReactorBatchProperties.kV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.kV
```

````

````{py:method} keys()
:canonical: altdss.Reactor.ReactorBatchProperties.keys

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Reactor.ReactorBatchProperties.kvar
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.kvar
```

````

````{py:attribute} pctPerm
:canonical: altdss.Reactor.ReactorBatchProperties.pctPerm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.pctPerm
```

````

````{py:method} pop()
:canonical: altdss.Reactor.ReactorBatchProperties.pop

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Reactor.ReactorBatchProperties.popitem

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Reactor.ReactorBatchProperties.setdefault

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Reactor.ReactorBatchProperties.update

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Reactor.ReactorBatchProperties.values

```{autodoc2-docstring} altdss.Reactor.ReactorBatchProperties.values
```

````

`````

`````{py:class} ReactorProperties()
:canonical: altdss.Reactor.ReactorProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Reactor.ReactorProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Reactor.ReactorProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Reactor.ReactorProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Reactor.ReactorProperties.Bus2
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Bus2
```

````

````{py:attribute} Conn
:canonical: altdss.Reactor.ReactorProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Conn
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Reactor.ReactorProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Reactor.ReactorProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.Reactor.ReactorProperties.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.FaultRate
```

````

````{py:attribute} LCurve
:canonical: altdss.Reactor.ReactorProperties.LCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.LCurve
```

````

````{py:attribute} Like
:canonical: altdss.Reactor.ReactorProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Like
```

````

````{py:attribute} LmH
:canonical: altdss.Reactor.ReactorProperties.LmH
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.LmH
```

````

````{py:attribute} NormAmps
:canonical: altdss.Reactor.ReactorProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.NormAmps
```

````

````{py:attribute} Parallel
:canonical: altdss.Reactor.ReactorProperties.Parallel
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Parallel
```

````

````{py:attribute} Phases
:canonical: altdss.Reactor.ReactorProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Phases
```

````

````{py:attribute} R
:canonical: altdss.Reactor.ReactorProperties.R
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.R
```

````

````{py:attribute} RCurve
:canonical: altdss.Reactor.ReactorProperties.RCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.RCurve
```

````

````{py:attribute} RMatrix
:canonical: altdss.Reactor.ReactorProperties.RMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.RMatrix
```

````

````{py:attribute} Repair
:canonical: altdss.Reactor.ReactorProperties.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Repair
```

````

````{py:attribute} Rp
:canonical: altdss.Reactor.ReactorProperties.Rp
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Rp
```

````

````{py:attribute} X
:canonical: altdss.Reactor.ReactorProperties.X
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.X
```

````

````{py:attribute} XMatrix
:canonical: altdss.Reactor.ReactorProperties.XMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.XMatrix
```

````

````{py:attribute} Z0
:canonical: altdss.Reactor.ReactorProperties.Z0
:type: complex
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Z0
```

````

````{py:attribute} Z1
:canonical: altdss.Reactor.ReactorProperties.Z1
:type: complex
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Z1
```

````

````{py:attribute} Z2
:canonical: altdss.Reactor.ReactorProperties.Z2
:type: complex
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.Z2
```

````

````{py:method} __contains__()
:canonical: altdss.Reactor.ReactorProperties.__contains__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Reactor.ReactorProperties.__delattr__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Reactor.ReactorProperties.__delitem__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Reactor.ReactorProperties.__dir__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Reactor.ReactorProperties.__format__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Reactor.ReactorProperties.__ge__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Reactor.ReactorProperties.__getattribute__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Reactor.ReactorProperties.__getitem__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Reactor.ReactorProperties.__getstate__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Reactor.ReactorProperties.__gt__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Reactor.ReactorProperties.__init__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Reactor.ReactorProperties.__ior__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Reactor.ReactorProperties.__iter__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Reactor.ReactorProperties.__le__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Reactor.ReactorProperties.__len__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Reactor.ReactorProperties.__lt__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Reactor.ReactorProperties.__ne__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Reactor.ReactorProperties.__new__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Reactor.ReactorProperties.__or__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Reactor.ReactorProperties.__reduce__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Reactor.ReactorProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Reactor.ReactorProperties.__repr__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Reactor.ReactorProperties.__reversed__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Reactor.ReactorProperties.__ror__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Reactor.ReactorProperties.__setitem__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Reactor.ReactorProperties.__sizeof__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Reactor.ReactorProperties.__str__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Reactor.ReactorProperties.__subclasshook__

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Reactor.ReactorProperties.clear

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Reactor.ReactorProperties.copy

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Reactor.ReactorProperties.get

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.get
```

````

````{py:method} items()
:canonical: altdss.Reactor.ReactorProperties.items

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Reactor.ReactorProperties.kV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.kV
```

````

````{py:method} keys()
:canonical: altdss.Reactor.ReactorProperties.keys

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Reactor.ReactorProperties.kvar
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.kvar
```

````

````{py:attribute} pctPerm
:canonical: altdss.Reactor.ReactorProperties.pctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.pctPerm
```

````

````{py:method} pop()
:canonical: altdss.Reactor.ReactorProperties.pop

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Reactor.ReactorProperties.popitem

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Reactor.ReactorProperties.setdefault

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Reactor.ReactorProperties.update

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.update
```

````

````{py:method} values()
:canonical: altdss.Reactor.ReactorProperties.values

```{autodoc2-docstring} altdss.Reactor.ReactorProperties.values
```

````

`````
