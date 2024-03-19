# {py:mod}`altdss.Capacitor`

```{py:module} altdss.Capacitor
```

```{autodoc2-docstring} altdss.Capacitor
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Capacitor <altdss.Capacitor.Capacitor>`
  - ```{autodoc2-docstring} altdss.Capacitor.Capacitor
    :summary:
    ```
* - {py:obj}`CapacitorBatch <altdss.Capacitor.CapacitorBatch>`
  - ```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch
    :summary:
    ```
* - {py:obj}`CapacitorBatchProperties <altdss.Capacitor.CapacitorBatchProperties>`
  - ```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties
    :summary:
    ```
* - {py:obj}`CapacitorProperties <altdss.Capacitor.CapacitorProperties>`
  - ```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties
    :summary:
    ```
* - {py:obj}`ICapacitor <altdss.Capacitor.ICapacitor>`
  - ```{autodoc2-docstring} altdss.Capacitor.ICapacitor
    :summary:
    ```
````

### API

`````{py:class} Capacitor(api_util, ptr)
:canonical: altdss.Capacitor.Capacitor

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PDElement.PDElementMixin`

```{autodoc2-docstring} altdss.Capacitor.Capacitor
```

````{py:method} AccumulatedL() -> float
:canonical: altdss.Capacitor.Capacitor.AccumulatedL

```{autodoc2-docstring} altdss.Capacitor.Capacitor.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Capacitor.Capacitor.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Capacitor.Capacitor.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Capacitor.Capacitor.Bus2
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Bus2
```

````

````{py:attribute} CMatrix
:canonical: altdss.Capacitor.Capacitor.CMatrix
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.CMatrix
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Capacitor.Capacitor.Close

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.Capacitor.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Capacitor.Capacitor.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.Capacitor.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Capacitor.Capacitor.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Capacitor.Capacitor.Conn
:type: altdss.enums.Connection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Capacitor.Capacitor.Conn_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Conn_str
```

````

````{py:attribute} Cuf
:canonical: altdss.Capacitor.Capacitor.Cuf
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Cuf
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.Capacitor.Currents

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.Capacitor.Capacitor.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.DisplayName
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Capacitor.Capacitor.EmergAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Capacitor.Capacitor.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Enabled
```

````

````{py:method} EnergyMeter() -> typing.Optional[altdss.DSSObj.DSSObj]
:canonical: altdss.Capacitor.Capacitor.EnergyMeter

```{autodoc2-docstring} altdss.Capacitor.Capacitor.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Capacitor.Capacitor.EnergyMeterName

```{autodoc2-docstring} altdss.Capacitor.Capacitor.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Capacitor.Capacitor.FaultRate
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.FaultRate
```

````

````{py:method} FromTerminal() -> int
:canonical: altdss.Capacitor.Capacitor.FromTerminal

```{autodoc2-docstring} altdss.Capacitor.Capacitor.FromTerminal
```

````

````{py:method} FullName() -> str
:canonical: altdss.Capacitor.Capacitor.FullName

```{autodoc2-docstring} altdss.Capacitor.Capacitor.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Capacitor.Capacitor.GUID

```{autodoc2-docstring} altdss.Capacitor.Capacitor.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.Capacitor.Capacitor.Handle

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Handle
```

````

````{py:attribute} Harm
:canonical: altdss.Capacitor.Capacitor.Harm
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Harm
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Capacitor.Capacitor.HasOCPDevice

```{autodoc2-docstring} altdss.Capacitor.Capacitor.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Capacitor.Capacitor.HasSwitchControl

```{autodoc2-docstring} altdss.Capacitor.Capacitor.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Capacitor.Capacitor.HasVoltControl

```{autodoc2-docstring} altdss.Capacitor.Capacitor.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Capacitor.Capacitor.IsIsolated

```{autodoc2-docstring} altdss.Capacitor.Capacitor.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Capacitor.Capacitor.IsOpen

```{autodoc2-docstring} altdss.Capacitor.Capacitor.IsOpen
```

````

````{py:method} IsShunt() -> bool
:canonical: altdss.Capacitor.Capacitor.IsShunt

```{autodoc2-docstring} altdss.Capacitor.Capacitor.IsShunt
```

````

````{py:method} Lambda() -> float
:canonical: altdss.Capacitor.Capacitor.Lambda

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Lambda
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Capacitor.Capacitor.Like

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Capacitor.Capacitor.Losses

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Capacitor.Capacitor.MaxCurrent

```{autodoc2-docstring} altdss.Capacitor.Capacitor.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Capacitor.Capacitor.Name
:type: str

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.Capacitor.NodeOrder

```{autodoc2-docstring} altdss.Capacitor.Capacitor.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.Capacitor.NodeRef

```{autodoc2-docstring} altdss.Capacitor.Capacitor.NodeRef
```

````

````{py:attribute} NormAmps
:canonical: altdss.Capacitor.Capacitor.NormAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.NormAmps
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Capacitor.Capacitor.NumConductors

```{autodoc2-docstring} altdss.Capacitor.Capacitor.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Capacitor.Capacitor.NumControllers

```{autodoc2-docstring} altdss.Capacitor.Capacitor.NumControllers
```

````

````{py:method} NumCustomers() -> int
:canonical: altdss.Capacitor.Capacitor.NumCustomers

```{autodoc2-docstring} altdss.Capacitor.Capacitor.NumCustomers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Capacitor.Capacitor.NumPhases

```{autodoc2-docstring} altdss.Capacitor.Capacitor.NumPhases
```

````

````{py:attribute} NumSteps
:canonical: altdss.Capacitor.Capacitor.NumSteps
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.NumSteps
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Capacitor.Capacitor.NumTerminals

```{autodoc2-docstring} altdss.Capacitor.Capacitor.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Capacitor.Capacitor.OCPDevice

```{autodoc2-docstring} altdss.Capacitor.Capacitor.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Capacitor.Capacitor.OCPDeviceIndex

```{autodoc2-docstring} altdss.Capacitor.Capacitor.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Capacitor.Capacitor.OCPDeviceType

```{autodoc2-docstring} altdss.Capacitor.Capacitor.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Capacitor.Capacitor.Open

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Open
```

````

````{py:method} ParentPDElement() -> typing.Optional[altdss.DSSObj.DSSObj]
:canonical: altdss.Capacitor.Capacitor.ParentPDElement

```{autodoc2-docstring} altdss.Capacitor.Capacitor.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.Capacitor.PhaseLosses

```{autodoc2-docstring} altdss.Capacitor.Capacitor.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Capacitor.Capacitor.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.Capacitor.Powers

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Powers
```

````

````{py:attribute} R
:canonical: altdss.Capacitor.Capacitor.R
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.R
```

````

````{py:attribute} Repair
:canonical: altdss.Capacitor.Capacitor.Repair
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Repair
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.Capacitor.Residuals

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Residuals
```

````

````{py:method} SectionID() -> int
:canonical: altdss.Capacitor.Capacitor.SectionID

```{autodoc2-docstring} altdss.Capacitor.Capacitor.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.Capacitor.SeqCurrents

```{autodoc2-docstring} altdss.Capacitor.Capacitor.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.Capacitor.SeqPowers

```{autodoc2-docstring} altdss.Capacitor.Capacitor.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.Capacitor.SeqVoltages

```{autodoc2-docstring} altdss.Capacitor.Capacitor.SeqVoltages
```

````

````{py:attribute} States
:canonical: altdss.Capacitor.Capacitor.States
:type: altdss.types.Int32Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.States
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.Capacitor.Capacitor.TotalCustomers

```{autodoc2-docstring} altdss.Capacitor.Capacitor.TotalCustomers
```

````

````{py:method} TotalKilometers() -> float
:canonical: altdss.Capacitor.Capacitor.TotalKilometers

```{autodoc2-docstring} altdss.Capacitor.Capacitor.TotalKilometers
```

````

````{py:method} TotalMiles() -> float
:canonical: altdss.Capacitor.Capacitor.TotalMiles

```{autodoc2-docstring} altdss.Capacitor.Capacitor.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.Capacitor.TotalPowers

```{autodoc2-docstring} altdss.Capacitor.Capacitor.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.Capacitor.Voltages

```{autodoc2-docstring} altdss.Capacitor.Capacitor.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.Capacitor.VoltagesMagAng

```{autodoc2-docstring} altdss.Capacitor.Capacitor.VoltagesMagAng
```

````

````{py:attribute} XL
:canonical: altdss.Capacitor.Capacitor.XL
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.XL
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.Capacitor.YPrim

```{autodoc2-docstring} altdss.Capacitor.Capacitor.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.Capacitor.Capacitor.__hash__

```{autodoc2-docstring} altdss.Capacitor.Capacitor.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Capacitor.Capacitor.__init__

```{autodoc2-docstring} altdss.Capacitor.Capacitor.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Capacitor.Capacitor.__ne__

```{autodoc2-docstring} altdss.Capacitor.Capacitor.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Capacitor.Capacitor.__repr__

```{autodoc2-docstring} altdss.Capacitor.Capacitor.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Capacitor.Capacitor.begin_edit

```{autodoc2-docstring} altdss.Capacitor.Capacitor.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Capacitor.CapacitorProperties]) -> altdss.Capacitor.Capacitor
:canonical: altdss.Capacitor.Capacitor.edit

```{autodoc2-docstring} altdss.Capacitor.Capacitor.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Capacitor.Capacitor.end_edit

```{autodoc2-docstring} altdss.Capacitor.Capacitor.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Capacitor.Capacitor.kV
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.kV
```

````

````{py:attribute} kvar
:canonical: altdss.Capacitor.Capacitor.kvar
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.kvar
```

````

````{py:method} pctEmergency(allNodes=False) -> float
:canonical: altdss.Capacitor.Capacitor.pctEmergency

```{autodoc2-docstring} altdss.Capacitor.Capacitor.pctEmergency
```

````

````{py:method} pctNormal(allNodes=False) -> float
:canonical: altdss.Capacitor.Capacitor.pctNormal

```{autodoc2-docstring} altdss.Capacitor.Capacitor.pctNormal
```

````

````{py:attribute} pctPerm
:canonical: altdss.Capacitor.Capacitor.pctPerm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.Capacitor.pctPerm
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Capacitor.Capacitor.to_json

```{autodoc2-docstring} altdss.Capacitor.Capacitor.to_json
```

````

`````

`````{py:class} CapacitorBatch(api_util, **kwargs)
:canonical: altdss.Capacitor.CapacitorBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PDElement.PDElementBatchMixin`

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.AccumulatedL

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Capacitor.CapacitorBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Capacitor.CapacitorBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Capacitor.CapacitorBatch.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Bus2
```

````

````{py:attribute} CMatrix
:canonical: altdss.Capacitor.CapacitorBatch.CMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.CMatrix
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.CapacitorBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.CapacitorBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Capacitor.CapacitorBatch.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Capacitor.CapacitorBatch.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Conn_str
```

````

````{py:attribute} Cuf
:canonical: altdss.Capacitor.CapacitorBatch.Cuf
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Cuf
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.CapacitorBatch.Currents

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Capacitor.CapacitorBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Capacitor.CapacitorBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.Capacitor.CapacitorBatch.EnergyMeter

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Capacitor.CapacitorBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Capacitor.CapacitorBatch.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.FromTerminal

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Capacitor.CapacitorBatch.FullName

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Capacitor.CapacitorBatch.GUID

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.Handle

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Handle
```

````

````{py:attribute} Harm
:canonical: altdss.Capacitor.CapacitorBatch.Harm
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Harm
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Capacitor.CapacitorBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Capacitor.CapacitorBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Capacitor.CapacitorBatch.HasVoltControl

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Capacitor.CapacitorBatch.IsIsolated

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Capacitor.CapacitorBatch.IsShunt

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.Lambda

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Lambda
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Capacitor.CapacitorBatch.Like

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.CapacitorBatch.Losses

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.MaxCurrent

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Capacitor.CapacitorBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Capacitor.CapacitorBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.NumConductors

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.NumControllers

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.NumCustomers

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.NumPhases

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.NumPhases
```

````

````{py:attribute} NumSteps
:canonical: altdss.Capacitor.CapacitorBatch.NumSteps
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.NumSteps
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.NumTerminals

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Capacitor.CapacitorBatch.OCPDevice

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Capacitor.CapacitorBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.Capacitor.CapacitorBatch.ParentPDElement

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.CapacitorBatch.PhaseLosses

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Capacitor.CapacitorBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.CapacitorBatch.Powers

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Powers
```

````

````{py:attribute} R
:canonical: altdss.Capacitor.CapacitorBatch.R
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.R
```

````

````{py:attribute} Repair
:canonical: altdss.Capacitor.CapacitorBatch.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Repair
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.SectionID

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.SeqCurrents

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.CapacitorBatch.SeqPowers

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.SeqVoltages

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.SeqVoltages
```

````

````{py:attribute} States
:canonical: altdss.Capacitor.CapacitorBatch.States
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.States
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.CapacitorBatch.TotalCustomers

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.TotalCustomers
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.TotalKilometers

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.TotalMiles

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.CapacitorBatch.TotalPowers

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.CapacitorBatch.Voltages

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.VoltagesMagAng
```

````

````{py:attribute} XL
:canonical: altdss.Capacitor.CapacitorBatch.XL
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.XL
```

````

````{py:method} __call__()
:canonical: altdss.Capacitor.CapacitorBatch.__call__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Capacitor.CapacitorBatch.__getitem__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Capacitor.CapacitorBatch.__init__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Capacitor.CapacitorBatch.__iter__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Capacitor.CapacitorBatch.__len__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Capacitor.CapacitorBatch.batch

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Capacitor.CapacitorBatch.begin_edit

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Capacitor.CapacitorBatchProperties]) -> altdss.Capacitor.CapacitorBatch
:canonical: altdss.Capacitor.CapacitorBatch.edit

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Capacitor.CapacitorBatch.end_edit

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.end_edit
```

````

````{py:attribute} kV
:canonical: altdss.Capacitor.CapacitorBatch.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.kV
```

````

````{py:attribute} kvar
:canonical: altdss.Capacitor.CapacitorBatch.kvar
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.kvar
```

````

````{py:method} pctEmergency(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.pctEmergency

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.pctEmergency
```

````

````{py:method} pctNormal(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.Capacitor.CapacitorBatch.pctNormal

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.pctNormal
```

````

````{py:attribute} pctPerm
:canonical: altdss.Capacitor.CapacitorBatch.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.pctPerm
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Capacitor.CapacitorBatch.to_json

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Capacitor.CapacitorBatch.to_list

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatch.to_list
```

````

`````

`````{py:class} CapacitorBatchProperties()
:canonical: altdss.Capacitor.CapacitorBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Capacitor.CapacitorBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Capacitor.CapacitorBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Capacitor.CapacitorBatchProperties.Bus2
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.Bus2
```

````

````{py:attribute} CMatrix
:canonical: altdss.Capacitor.CapacitorBatchProperties.CMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.CMatrix
```

````

````{py:attribute} Conn
:canonical: altdss.Capacitor.CapacitorBatchProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.Connection], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.Conn
```

````

````{py:attribute} Cuf
:canonical: altdss.Capacitor.CapacitorBatchProperties.Cuf
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.Cuf
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Capacitor.CapacitorBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Capacitor.CapacitorBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.Capacitor.CapacitorBatchProperties.FaultRate
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.FaultRate
```

````

````{py:attribute} Harm
:canonical: altdss.Capacitor.CapacitorBatchProperties.Harm
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.Harm
```

````

````{py:attribute} Like
:canonical: altdss.Capacitor.CapacitorBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.Like
```

````

````{py:attribute} NormAmps
:canonical: altdss.Capacitor.CapacitorBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.NormAmps
```

````

````{py:attribute} NumSteps
:canonical: altdss.Capacitor.CapacitorBatchProperties.NumSteps
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.NumSteps
```

````

````{py:attribute} Phases
:canonical: altdss.Capacitor.CapacitorBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.Phases
```

````

````{py:attribute} R
:canonical: altdss.Capacitor.CapacitorBatchProperties.R
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.R
```

````

````{py:attribute} Repair
:canonical: altdss.Capacitor.CapacitorBatchProperties.Repair
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.Repair
```

````

````{py:attribute} States
:canonical: altdss.Capacitor.CapacitorBatchProperties.States
:type: altdss.types.Int32Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.States
```

````

````{py:attribute} XL
:canonical: altdss.Capacitor.CapacitorBatchProperties.XL
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.XL
```

````

````{py:method} __contains__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__contains__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__dir__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__format__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__ge__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__gt__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__init__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__ior__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__iter__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__le__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__len__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__lt__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__ne__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__new__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__or__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__repr__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__ror__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__str__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Capacitor.CapacitorBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Capacitor.CapacitorBatchProperties.clear

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Capacitor.CapacitorBatchProperties.copy

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Capacitor.CapacitorBatchProperties.get

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Capacitor.CapacitorBatchProperties.items

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Capacitor.CapacitorBatchProperties.kV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.kV
```

````

````{py:method} keys()
:canonical: altdss.Capacitor.CapacitorBatchProperties.keys

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Capacitor.CapacitorBatchProperties.kvar
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.kvar
```

````

````{py:attribute} pctPerm
:canonical: altdss.Capacitor.CapacitorBatchProperties.pctPerm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.pctPerm
```

````

````{py:method} pop()
:canonical: altdss.Capacitor.CapacitorBatchProperties.pop

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Capacitor.CapacitorBatchProperties.popitem

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Capacitor.CapacitorBatchProperties.setdefault

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Capacitor.CapacitorBatchProperties.update

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Capacitor.CapacitorBatchProperties.values

```{autodoc2-docstring} altdss.Capacitor.CapacitorBatchProperties.values
```

````

`````

`````{py:class} CapacitorProperties()
:canonical: altdss.Capacitor.CapacitorProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Capacitor.CapacitorProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Capacitor.CapacitorProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Capacitor.CapacitorProperties.Bus2
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.Bus2
```

````

````{py:attribute} CMatrix
:canonical: altdss.Capacitor.CapacitorProperties.CMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.CMatrix
```

````

````{py:attribute} Conn
:canonical: altdss.Capacitor.CapacitorProperties.Conn
:type: typing.Union[typing.AnyStr, int, altdss.enums.Connection]
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.Conn
```

````

````{py:attribute} Cuf
:canonical: altdss.Capacitor.CapacitorProperties.Cuf
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.Cuf
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Capacitor.CapacitorProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Capacitor.CapacitorProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.Capacitor.CapacitorProperties.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.FaultRate
```

````

````{py:attribute} Harm
:canonical: altdss.Capacitor.CapacitorProperties.Harm
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.Harm
```

````

````{py:attribute} Like
:canonical: altdss.Capacitor.CapacitorProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.Like
```

````

````{py:attribute} NormAmps
:canonical: altdss.Capacitor.CapacitorProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.NormAmps
```

````

````{py:attribute} NumSteps
:canonical: altdss.Capacitor.CapacitorProperties.NumSteps
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.NumSteps
```

````

````{py:attribute} Phases
:canonical: altdss.Capacitor.CapacitorProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.Phases
```

````

````{py:attribute} R
:canonical: altdss.Capacitor.CapacitorProperties.R
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.R
```

````

````{py:attribute} Repair
:canonical: altdss.Capacitor.CapacitorProperties.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.Repair
```

````

````{py:attribute} States
:canonical: altdss.Capacitor.CapacitorProperties.States
:type: altdss.types.Int32Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.States
```

````

````{py:attribute} XL
:canonical: altdss.Capacitor.CapacitorProperties.XL
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.XL
```

````

````{py:method} __contains__()
:canonical: altdss.Capacitor.CapacitorProperties.__contains__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Capacitor.CapacitorProperties.__delattr__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Capacitor.CapacitorProperties.__delitem__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Capacitor.CapacitorProperties.__dir__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Capacitor.CapacitorProperties.__format__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Capacitor.CapacitorProperties.__ge__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Capacitor.CapacitorProperties.__getattribute__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Capacitor.CapacitorProperties.__getitem__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Capacitor.CapacitorProperties.__getstate__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Capacitor.CapacitorProperties.__gt__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Capacitor.CapacitorProperties.__init__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Capacitor.CapacitorProperties.__ior__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Capacitor.CapacitorProperties.__iter__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Capacitor.CapacitorProperties.__le__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Capacitor.CapacitorProperties.__len__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Capacitor.CapacitorProperties.__lt__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Capacitor.CapacitorProperties.__ne__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Capacitor.CapacitorProperties.__new__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Capacitor.CapacitorProperties.__or__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Capacitor.CapacitorProperties.__reduce__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Capacitor.CapacitorProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Capacitor.CapacitorProperties.__repr__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Capacitor.CapacitorProperties.__reversed__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Capacitor.CapacitorProperties.__ror__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Capacitor.CapacitorProperties.__setitem__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Capacitor.CapacitorProperties.__sizeof__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Capacitor.CapacitorProperties.__str__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Capacitor.CapacitorProperties.__subclasshook__

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Capacitor.CapacitorProperties.clear

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Capacitor.CapacitorProperties.copy

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Capacitor.CapacitorProperties.get

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.get
```

````

````{py:method} items()
:canonical: altdss.Capacitor.CapacitorProperties.items

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.items
```

````

````{py:attribute} kV
:canonical: altdss.Capacitor.CapacitorProperties.kV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.kV
```

````

````{py:method} keys()
:canonical: altdss.Capacitor.CapacitorProperties.keys

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.keys
```

````

````{py:attribute} kvar
:canonical: altdss.Capacitor.CapacitorProperties.kvar
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.kvar
```

````

````{py:attribute} pctPerm
:canonical: altdss.Capacitor.CapacitorProperties.pctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.pctPerm
```

````

````{py:method} pop()
:canonical: altdss.Capacitor.CapacitorProperties.pop

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Capacitor.CapacitorProperties.popitem

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Capacitor.CapacitorProperties.setdefault

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Capacitor.CapacitorProperties.update

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.update
```

````

````{py:method} values()
:canonical: altdss.Capacitor.CapacitorProperties.values

```{autodoc2-docstring} altdss.Capacitor.CapacitorProperties.values
```

````

`````

`````{py:class} ICapacitor(iobj)
:canonical: altdss.Capacitor.ICapacitor

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Capacitor.CapacitorBatch`

```{autodoc2-docstring} altdss.Capacitor.ICapacitor
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.AccumulatedL

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Capacitor.ICapacitor.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Capacitor.ICapacitor.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Capacitor.ICapacitor.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Bus2
```

````

````{py:attribute} CMatrix
:canonical: altdss.Capacitor.ICapacitor.CMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.CMatrix
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.ICapacitor.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.ICapacitor.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.ComplexSeqVoltages
```

````

````{py:attribute} Conn
:canonical: altdss.Capacitor.ICapacitor.Conn
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Conn
```

````

````{py:attribute} Conn_str
:canonical: altdss.Capacitor.ICapacitor.Conn_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Conn_str
```

````

````{py:attribute} Cuf
:canonical: altdss.Capacitor.ICapacitor.Cuf
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Cuf
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.ICapacitor.Currents

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.CurrentsMagAng

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Capacitor.ICapacitor.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Capacitor.ICapacitor.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.Capacitor.ICapacitor.EnergyMeter

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Capacitor.ICapacitor.EnergyMeterName

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Capacitor.ICapacitor.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.FromTerminal

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Capacitor.ICapacitor.FullName

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.Capacitor.ICapacitor.GUID

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.Handle

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Handle
```

````

````{py:attribute} Harm
:canonical: altdss.Capacitor.ICapacitor.Harm
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Harm
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.Capacitor.ICapacitor.HasOCPDevice

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.Capacitor.ICapacitor.HasSwitchControl

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.Capacitor.ICapacitor.HasVoltControl

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Capacitor.ICapacitor.IsIsolated

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Capacitor.ICapacitor.IsShunt

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.Lambda

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Lambda
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Capacitor.ICapacitor.Like

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.ICapacitor.Losses

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.MaxCurrent

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Capacitor.ICapacitor.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Capacitor.ICapacitor.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.NumConductors

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.NumControllers

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.NumCustomers

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.NumPhases

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.NumPhases
```

````

````{py:attribute} NumSteps
:canonical: altdss.Capacitor.ICapacitor.NumSteps
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.NumSteps
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.NumTerminals

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Capacitor.ICapacitor.OCPDevice

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.OCPDeviceIndex

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.Capacitor.ICapacitor.OCPDeviceType

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.Capacitor.ICapacitor.ParentPDElement

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.ICapacitor.PhaseLosses

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Capacitor.ICapacitor.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.ICapacitor.Powers

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Powers
```

````

````{py:attribute} R
:canonical: altdss.Capacitor.ICapacitor.R
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.R
```

````

````{py:attribute} Repair
:canonical: altdss.Capacitor.ICapacitor.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Repair
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.SectionID

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.SeqCurrents

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.ICapacitor.SeqPowers

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.SeqVoltages

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.SeqVoltages
```

````

````{py:attribute} States
:canonical: altdss.Capacitor.ICapacitor.States
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.States
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Capacitor.ICapacitor.TotalCustomers

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.TotalCustomers
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.TotalKilometers

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.TotalMiles

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.ICapacitor.TotalPowers

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Capacitor.ICapacitor.Voltages

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.VoltagesMagAng

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.VoltagesMagAng
```

````

````{py:attribute} XL
:canonical: altdss.Capacitor.ICapacitor.XL
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.XL
```

````

````{py:method} __call__()
:canonical: altdss.Capacitor.ICapacitor.__call__

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Capacitor.ICapacitor.__contains__

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Capacitor.ICapacitor.__getitem__

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Capacitor.ICapacitor.__init__

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Capacitor.ICapacitor.__iter__

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Capacitor.ICapacitor.__len__

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Capacitor.ICapacitor.batch

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.Capacitor.CapacitorBatchProperties]) -> altdss.Capacitor.CapacitorBatch
:canonical: altdss.Capacitor.ICapacitor.batch_new

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Capacitor.ICapacitor.begin_edit

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.Capacitor.CapacitorBatchProperties]) -> altdss.Capacitor.CapacitorBatch
:canonical: altdss.Capacitor.ICapacitor.edit

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Capacitor.ICapacitor.end_edit

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Capacitor.ICapacitor.find

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.find
```

````

````{py:attribute} kV
:canonical: altdss.Capacitor.ICapacitor.kV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.kV
```

````

````{py:attribute} kvar
:canonical: altdss.Capacitor.ICapacitor.kvar
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.kvar
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.Capacitor.CapacitorProperties]) -> altdss.Capacitor.Capacitor
:canonical: altdss.Capacitor.ICapacitor.new

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.new
```

````

````{py:method} pctEmergency(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.pctEmergency

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.pctEmergency
```

````

````{py:method} pctNormal(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.Capacitor.ICapacitor.pctNormal

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.pctNormal
```

````

````{py:attribute} pctPerm
:canonical: altdss.Capacitor.ICapacitor.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.pctPerm
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Capacitor.ICapacitor.to_json

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Capacitor.ICapacitor.to_list

```{autodoc2-docstring} altdss.Capacitor.ICapacitor.to_list
```

````

`````
