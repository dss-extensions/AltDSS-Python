# {py:mod}`altdss.GICTransformer`

```{py:module} altdss.GICTransformer
```

```{autodoc2-docstring} altdss.GICTransformer
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GICTransformer <altdss.GICTransformer.GICTransformer>`
  - ```{autodoc2-docstring} altdss.GICTransformer.GICTransformer
    :summary:
    ```
* - {py:obj}`GICTransformerBatch <altdss.GICTransformer.GICTransformerBatch>`
  - ```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch
    :summary:
    ```
* - {py:obj}`GICTransformerBatchProperties <altdss.GICTransformer.GICTransformerBatchProperties>`
  - ```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties
    :summary:
    ```
* - {py:obj}`GICTransformerProperties <altdss.GICTransformer.GICTransformerProperties>`
  - ```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties
    :summary:
    ```
* - {py:obj}`IGICTransformer <altdss.GICTransformer.IGICTransformer>`
  - ```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer
    :summary:
    ```
````

### API

`````{py:class} GICTransformer(api_util, ptr)
:canonical: altdss.GICTransformer.GICTransformer

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PDElement.PDElementMixin`

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer
```

````{py:method} AccumulatedL() -> float
:canonical: altdss.GICTransformer.GICTransformer.AccumulatedL

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICTransformer.GICTransformer.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.BaseFreq
```

````

````{py:attribute} BusH
:canonical: altdss.GICTransformer.GICTransformer.BusH
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.BusH
```

````

````{py:attribute} BusNH
:canonical: altdss.GICTransformer.GICTransformer.BusNH
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.BusNH
```

````

````{py:attribute} BusNX
:canonical: altdss.GICTransformer.GICTransformer.BusNX
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.BusNX
```

````

````{py:attribute} BusX
:canonical: altdss.GICTransformer.GICTransformer.BusX
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.BusX
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.GICTransformer.GICTransformer.Close

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformer.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformer.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformer.Currents

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.GICTransformer.GICTransformer.DisplayName
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.DisplayName
```

````

````{py:attribute} EmergAmps
:canonical: altdss.GICTransformer.GICTransformer.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.GICTransformer.GICTransformer.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.GICTransformer.GICTransformer.EnergyMeter

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.GICTransformer.GICTransformer.EnergyMeterName

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.GICTransformer.GICTransformer.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.FaultRate
```

````

````{py:method} FromTerminal() -> int
:canonical: altdss.GICTransformer.GICTransformer.FromTerminal

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.FromTerminal
```

````

````{py:method} FullName() -> str
:canonical: altdss.GICTransformer.GICTransformer.FullName

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GICTransformer.GICTransformer.GUID

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.GICTransformer.GICTransformer.Handle

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GICTransformer.GICTransformer.HasOCPDevice

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GICTransformer.GICTransformer.HasSwitchControl

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GICTransformer.GICTransformer.HasVoltControl

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.GICTransformer.GICTransformer.IsIsolated

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.GICTransformer.GICTransformer.IsOpen

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.IsOpen
```

````

````{py:method} IsShunt() -> bool
:canonical: altdss.GICTransformer.GICTransformer.IsShunt

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.IsShunt
```

````

````{py:attribute} K
:canonical: altdss.GICTransformer.GICTransformer.K
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.K
```

````

````{py:method} Lambda() -> float
:canonical: altdss.GICTransformer.GICTransformer.Lambda

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Lambda
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.GICTransformer.GICTransformer.Like

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.GICTransformer.GICTransformer.Losses

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Losses
```

````

````{py:attribute} MVA
:canonical: altdss.GICTransformer.GICTransformer.MVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.MVA
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GICTransformer.GICTransformer.MaxCurrent

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GICTransformer.GICTransformer.Name
:type: str

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformer.NodeOrder

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformer.NodeRef

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.NodeRef
```

````

````{py:attribute} NormAmps
:canonical: altdss.GICTransformer.GICTransformer.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.NormAmps
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.GICTransformer.GICTransformer.NumConductors

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.GICTransformer.GICTransformer.NumControllers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.NumControllers
```

````

````{py:method} NumCustomers() -> int
:canonical: altdss.GICTransformer.GICTransformer.NumCustomers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.NumCustomers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.GICTransformer.GICTransformer.NumPhases

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.GICTransformer.GICTransformer.NumTerminals

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.GICTransformer.GICTransformer.OCPDevice

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.GICTransformer.GICTransformer.OCPDeviceIndex

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GICTransformer.GICTransformer.OCPDeviceType

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.GICTransformer.GICTransformer.Open

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Open
```

````

````{py:method} ParentPDElement() -> altdss.DSSObj.DSSObj
:canonical: altdss.GICTransformer.GICTransformer.ParentPDElement

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformer.PhaseLosses

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.GICTransformer.GICTransformer.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformer.Powers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Powers
```

````

````{py:attribute} R1
:canonical: altdss.GICTransformer.GICTransformer.R1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.R1
```

````

````{py:attribute} R2
:canonical: altdss.GICTransformer.GICTransformer.R2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.R2
```

````

````{py:attribute} Repair
:canonical: altdss.GICTransformer.GICTransformer.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Repair
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformer.Residuals

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Residuals
```

````

````{py:method} SectionID() -> int
:canonical: altdss.GICTransformer.GICTransformer.SectionID

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformer.SeqCurrents

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformer.SeqPowers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformer.SeqVoltages

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.SeqVoltages
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.GICTransformer.GICTransformer.TotalCustomers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.TotalCustomers
```

````

````{py:method} TotalMiles() -> float
:canonical: altdss.GICTransformer.GICTransformer.TotalMiles

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformer.TotalPowers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.GICTransformer.GICTransformer.Type
:type: altdss.enums.GICTransformerType
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.GICTransformer.GICTransformer.Type_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Type_str
```

````

````{py:attribute} VarCurve
:canonical: altdss.GICTransformer.GICTransformer.VarCurve
:type: altdss.XYcurve.XYcurve
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.VarCurve
```

````

````{py:attribute} VarCurve_str
:canonical: altdss.GICTransformer.GICTransformer.VarCurve_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.VarCurve_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformer.Voltages

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformer.VoltagesMagAng

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformer.YPrim

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.GICTransformer.GICTransformer.__hash__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.GICTransformer.GICTransformer.__init__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.GICTransformer.GICTransformer.__ne__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.GICTransformer.GICTransformer.__repr__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GICTransformer.GICTransformer.begin_edit

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GICTransformer.GICTransformer.end_edit

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.end_edit
```

````

````{py:attribute} kVLL1
:canonical: altdss.GICTransformer.GICTransformer.kVLL1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.kVLL1
```

````

````{py:attribute} kVLL2
:canonical: altdss.GICTransformer.GICTransformer.kVLL2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.kVLL2
```

````

````{py:method} pctEmerg(allNodes=False) -> float
:canonical: altdss.GICTransformer.GICTransformer.pctEmerg

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.pctEmerg
```

````

````{py:method} pctNorm(allNodes=False) -> float
:canonical: altdss.GICTransformer.GICTransformer.pctNorm

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.pctNorm
```

````

````{py:attribute} pctPerm
:canonical: altdss.GICTransformer.GICTransformer.pctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.pctPerm
```

````

````{py:attribute} pctR1
:canonical: altdss.GICTransformer.GICTransformer.pctR1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.pctR1
```

````

````{py:attribute} pctR2
:canonical: altdss.GICTransformer.GICTransformer.pctR2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.pctR2
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GICTransformer.GICTransformer.to_json

```{autodoc2-docstring} altdss.GICTransformer.GICTransformer.to_json
```

````

`````

`````{py:class} GICTransformerBatch(api_util, **kwargs)
:canonical: altdss.GICTransformer.GICTransformerBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PDElement.PDElementBatchMixin`

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformerBatch.AccumulatedL

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICTransformer.GICTransformerBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.BaseFreq
```

````

````{py:attribute} BusH
:canonical: altdss.GICTransformer.GICTransformerBatch.BusH
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.BusH
```

````

````{py:attribute} BusNH
:canonical: altdss.GICTransformer.GICTransformerBatch.BusNH
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.BusNH
```

````

````{py:attribute} BusNX
:canonical: altdss.GICTransformer.GICTransformerBatch.BusNX
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.BusNX
```

````

````{py:attribute} BusX
:canonical: altdss.GICTransformer.GICTransformerBatch.BusX
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.BusX
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformerBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformerBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformerBatch.Currents

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformerBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.GICTransformer.GICTransformerBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.GICTransformer.GICTransformerBatch.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.GICTransformer.GICTransformerBatch.EnergyMeter

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.GICTransformer.GICTransformerBatch.EnergyMeterName

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.GICTransformer.GICTransformerBatch.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.FromTerminal

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GICTransformer.GICTransformerBatch.FullName

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GICTransformer.GICTransformerBatch.GUID

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.Handle

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GICTransformer.GICTransformerBatch.HasOCPDevice

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GICTransformer.GICTransformerBatch.HasSwitchControl

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GICTransformer.GICTransformerBatch.HasVoltControl

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.GICTransformer.GICTransformerBatch.IsIsolated

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.GICTransformer.GICTransformerBatch.IsShunt

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.IsShunt
```

````

````{py:attribute} K
:canonical: altdss.GICTransformer.GICTransformerBatch.K
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.K
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformerBatch.Lambda

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Lambda
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GICTransformer.GICTransformerBatch.Like

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformerBatch.Losses

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Losses
```

````

````{py:attribute} MVA
:canonical: altdss.GICTransformer.GICTransformerBatch.MVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.MVA
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GICTransformer.GICTransformerBatch.MaxCurrent

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GICTransformer.GICTransformerBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.GICTransformer.GICTransformerBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.NumConductors

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.NumControllers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.NumCustomers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.NumPhases

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.NumTerminals

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.GICTransformer.GICTransformerBatch.OCPDevice

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GICTransformer.GICTransformerBatch.OCPDeviceType

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.GICTransformer.GICTransformerBatch.ParentPDElement

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformerBatch.PhaseLosses

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.GICTransformer.GICTransformerBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformerBatch.Powers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Powers
```

````

````{py:attribute} R1
:canonical: altdss.GICTransformer.GICTransformerBatch.R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.R1
```

````

````{py:attribute} R2
:canonical: altdss.GICTransformer.GICTransformerBatch.R2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.R2
```

````

````{py:attribute} Repair
:canonical: altdss.GICTransformer.GICTransformerBatch.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Repair
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.SectionID

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformerBatch.SeqCurrents

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformerBatch.SeqPowers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformerBatch.SeqVoltages

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.SeqVoltages
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.GICTransformerBatch.TotalCustomers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.TotalCustomers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformerBatch.TotalMiles

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformerBatch.TotalPowers

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.GICTransformer.GICTransformerBatch.Type
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.GICTransformer.GICTransformerBatch.Type_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Type_str
```

````

````{py:attribute} VarCurve
:canonical: altdss.GICTransformer.GICTransformerBatch.VarCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.VarCurve
```

````

````{py:attribute} VarCurve_str
:canonical: altdss.GICTransformer.GICTransformerBatch.VarCurve_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.VarCurve_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.GICTransformerBatch.Voltages

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.GICTransformerBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.GICTransformer.GICTransformerBatch.__call__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.GICTransformer.GICTransformerBatch.__getitem__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.GICTransformer.GICTransformerBatch.__init__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GICTransformer.GICTransformerBatch.__iter__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GICTransformer.GICTransformerBatch.__len__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GICTransformer.GICTransformerBatch.begin_edit

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GICTransformer.GICTransformerBatch.end_edit

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.end_edit
```

````

````{py:attribute} kVLL1
:canonical: altdss.GICTransformer.GICTransformerBatch.kVLL1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.kVLL1
```

````

````{py:attribute} kVLL2
:canonical: altdss.GICTransformer.GICTransformerBatch.kVLL2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.kVLL2
```

````

````{py:attribute} pctPerm
:canonical: altdss.GICTransformer.GICTransformerBatch.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.pctPerm
```

````

````{py:attribute} pctR1
:canonical: altdss.GICTransformer.GICTransformerBatch.pctR1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.pctR1
```

````

````{py:attribute} pctR2
:canonical: altdss.GICTransformer.GICTransformerBatch.pctR2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.pctR2
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GICTransformer.GICTransformerBatch.to_json

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GICTransformer.GICTransformerBatch.to_list

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatch.to_list
```

````

`````

`````{py:class} GICTransformerBatchProperties()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.BaseFreq
```

````

````{py:attribute} BusH
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.BusH
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.BusH
```

````

````{py:attribute} BusNH
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.BusNH
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.BusNH
```

````

````{py:attribute} BusNX
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.BusNX
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.BusNX
```

````

````{py:attribute} BusX
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.BusX
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.BusX
```

````

````{py:attribute} EmergAmps
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.FaultRate
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.FaultRate
```

````

````{py:attribute} K
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.K
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.K
```

````

````{py:attribute} Like
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.Like
```

````

````{py:attribute} MVA
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.MVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.MVA
```

````

````{py:attribute} NormAmps
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.NormAmps
```

````

````{py:attribute} Phases
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.Phases
```

````

````{py:attribute} R1
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.R1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.R1
```

````

````{py:attribute} R2
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.R2
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.R2
```

````

````{py:attribute} Repair
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.Repair
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.Repair
```

````

````{py:attribute} Type
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.Type
:type: typing.Union[typing.AnyStr, int, altdss.enums.GICTransformerType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.GICTransformerType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.Type
```

````

````{py:attribute} VarCurve
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.VarCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.VarCurve
```

````

````{py:method} __contains__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__contains__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__delattr__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__delitem__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__dir__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__format__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__ge__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__getitem__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__getstate__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__gt__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__init__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__ior__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__iter__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__le__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__len__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__lt__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__ne__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__new__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__or__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__reduce__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__repr__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__reversed__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__ror__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__setitem__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__str__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.clear

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.copy

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.get

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.items

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.items
```

````

````{py:attribute} kVLL1
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.kVLL1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.kVLL1
```

````

````{py:attribute} kVLL2
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.kVLL2
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.kVLL2
```

````

````{py:method} keys()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.keys

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.keys
```

````

````{py:attribute} pctPerm
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.pctPerm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.pctPerm
```

````

````{py:attribute} pctR1
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.pctR1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.pctR1
```

````

````{py:attribute} pctR2
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.pctR2
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.pctR2
```

````

````{py:method} pop()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.pop

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.popitem

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.setdefault

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.update

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.GICTransformer.GICTransformerBatchProperties.values

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerBatchProperties.values
```

````

`````

`````{py:class} GICTransformerProperties()
:canonical: altdss.GICTransformer.GICTransformerProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.GICTransformer.GICTransformerProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.BaseFreq
```

````

````{py:attribute} BusH
:canonical: altdss.GICTransformer.GICTransformerProperties.BusH
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.BusH
```

````

````{py:attribute} BusNH
:canonical: altdss.GICTransformer.GICTransformerProperties.BusNH
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.BusNH
```

````

````{py:attribute} BusNX
:canonical: altdss.GICTransformer.GICTransformerProperties.BusNX
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.BusNX
```

````

````{py:attribute} BusX
:canonical: altdss.GICTransformer.GICTransformerProperties.BusX
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.BusX
```

````

````{py:attribute} EmergAmps
:canonical: altdss.GICTransformer.GICTransformerProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.GICTransformer.GICTransformerProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.GICTransformer.GICTransformerProperties.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.FaultRate
```

````

````{py:attribute} K
:canonical: altdss.GICTransformer.GICTransformerProperties.K
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.K
```

````

````{py:attribute} Like
:canonical: altdss.GICTransformer.GICTransformerProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.Like
```

````

````{py:attribute} MVA
:canonical: altdss.GICTransformer.GICTransformerProperties.MVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.MVA
```

````

````{py:attribute} NormAmps
:canonical: altdss.GICTransformer.GICTransformerProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.NormAmps
```

````

````{py:attribute} Phases
:canonical: altdss.GICTransformer.GICTransformerProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.Phases
```

````

````{py:attribute} R1
:canonical: altdss.GICTransformer.GICTransformerProperties.R1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.R1
```

````

````{py:attribute} R2
:canonical: altdss.GICTransformer.GICTransformerProperties.R2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.R2
```

````

````{py:attribute} Repair
:canonical: altdss.GICTransformer.GICTransformerProperties.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.Repair
```

````

````{py:attribute} Type
:canonical: altdss.GICTransformer.GICTransformerProperties.Type
:type: typing.Union[typing.AnyStr, int, altdss.enums.GICTransformerType]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.Type
```

````

````{py:attribute} VarCurve
:canonical: altdss.GICTransformer.GICTransformerProperties.VarCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.VarCurve
```

````

````{py:method} __contains__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__contains__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__delattr__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__delitem__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__dir__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__format__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__ge__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__getattribute__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__getitem__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__getstate__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__gt__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__init__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__ior__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__iter__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__le__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__len__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__lt__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__ne__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__new__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__or__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__reduce__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__repr__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__reversed__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__ror__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__setitem__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__sizeof__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__str__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GICTransformer.GICTransformerProperties.__subclasshook__

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GICTransformer.GICTransformerProperties.clear

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GICTransformer.GICTransformerProperties.copy

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GICTransformer.GICTransformerProperties.get

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.get
```

````

````{py:method} items()
:canonical: altdss.GICTransformer.GICTransformerProperties.items

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.items
```

````

````{py:attribute} kVLL1
:canonical: altdss.GICTransformer.GICTransformerProperties.kVLL1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.kVLL1
```

````

````{py:attribute} kVLL2
:canonical: altdss.GICTransformer.GICTransformerProperties.kVLL2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.kVLL2
```

````

````{py:method} keys()
:canonical: altdss.GICTransformer.GICTransformerProperties.keys

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.keys
```

````

````{py:attribute} pctPerm
:canonical: altdss.GICTransformer.GICTransformerProperties.pctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.pctPerm
```

````

````{py:attribute} pctR1
:canonical: altdss.GICTransformer.GICTransformerProperties.pctR1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.pctR1
```

````

````{py:attribute} pctR2
:canonical: altdss.GICTransformer.GICTransformerProperties.pctR2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.pctR2
```

````

````{py:method} pop()
:canonical: altdss.GICTransformer.GICTransformerProperties.pop

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GICTransformer.GICTransformerProperties.popitem

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GICTransformer.GICTransformerProperties.setdefault

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GICTransformer.GICTransformerProperties.update

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.update
```

````

````{py:method} values()
:canonical: altdss.GICTransformer.GICTransformerProperties.values

```{autodoc2-docstring} altdss.GICTransformer.GICTransformerProperties.values
```

````

`````

`````{py:class} IGICTransformer(iobj)
:canonical: altdss.GICTransformer.IGICTransformer

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.GICTransformer.GICTransformerBatch`

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.IGICTransformer.AccumulatedL

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.GICTransformer.IGICTransformer.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.BaseFreq
```

````

````{py:attribute} BusH
:canonical: altdss.GICTransformer.IGICTransformer.BusH
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.BusH
```

````

````{py:attribute} BusNH
:canonical: altdss.GICTransformer.IGICTransformer.BusNH
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.BusNH
```

````

````{py:attribute} BusNX
:canonical: altdss.GICTransformer.IGICTransformer.BusNX
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.BusNX
```

````

````{py:attribute} BusX
:canonical: altdss.GICTransformer.IGICTransformer.BusX
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.BusX
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.IGICTransformer.ComplexSeqCurrents

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.IGICTransformer.ComplexSeqVoltages

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.IGICTransformer.Currents

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.IGICTransformer.CurrentsMagAng

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.GICTransformer.IGICTransformer.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.GICTransformer.IGICTransformer.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.GICTransformer.IGICTransformer.EnergyMeter

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.GICTransformer.IGICTransformer.EnergyMeterName

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.GICTransformer.IGICTransformer.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.FromTerminal

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GICTransformer.IGICTransformer.FullName

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.GICTransformer.IGICTransformer.GUID

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.Handle

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.GICTransformer.IGICTransformer.HasOCPDevice

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.GICTransformer.IGICTransformer.HasSwitchControl

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.GICTransformer.IGICTransformer.HasVoltControl

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.GICTransformer.IGICTransformer.IsIsolated

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.GICTransformer.IGICTransformer.IsShunt

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.IsShunt
```

````

````{py:attribute} K
:canonical: altdss.GICTransformer.IGICTransformer.K
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.K
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.IGICTransformer.Lambda

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Lambda
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GICTransformer.IGICTransformer.Like

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.IGICTransformer.Losses

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Losses
```

````

````{py:attribute} MVA
:canonical: altdss.GICTransformer.IGICTransformer.MVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.MVA
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.GICTransformer.IGICTransformer.MaxCurrent

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.GICTransformer.IGICTransformer.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.GICTransformer.IGICTransformer.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.NumConductors

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.NumControllers

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.NumCustomers

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.NumPhases

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.NumTerminals

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.GICTransformer.IGICTransformer.OCPDevice

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.OCPDeviceIndex

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.GICTransformer.IGICTransformer.OCPDeviceType

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.GICTransformer.IGICTransformer.ParentPDElement

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.IGICTransformer.PhaseLosses

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.GICTransformer.IGICTransformer.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.IGICTransformer.Powers

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Powers
```

````

````{py:attribute} R1
:canonical: altdss.GICTransformer.IGICTransformer.R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.R1
```

````

````{py:attribute} R2
:canonical: altdss.GICTransformer.IGICTransformer.R2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.R2
```

````

````{py:attribute} Repair
:canonical: altdss.GICTransformer.IGICTransformer.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Repair
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.SectionID

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.IGICTransformer.SeqCurrents

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.IGICTransformer.SeqPowers

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.IGICTransformer.SeqVoltages

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.SeqVoltages
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.GICTransformer.IGICTransformer.TotalCustomers

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.TotalCustomers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.IGICTransformer.TotalMiles

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.IGICTransformer.TotalPowers

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.GICTransformer.IGICTransformer.Type
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.GICTransformer.IGICTransformer.Type_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Type_str
```

````

````{py:attribute} VarCurve
:canonical: altdss.GICTransformer.IGICTransformer.VarCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.VarCurve
```

````

````{py:attribute} VarCurve_str
:canonical: altdss.GICTransformer.IGICTransformer.VarCurve_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.VarCurve_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.GICTransformer.IGICTransformer.Voltages

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.GICTransformer.IGICTransformer.VoltagesMagAng

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.GICTransformer.IGICTransformer.__call__

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.GICTransformer.IGICTransformer.__contains__

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.GICTransformer.IGICTransformer.__getitem__

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.GICTransformer.IGICTransformer.__init__

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GICTransformer.IGICTransformer.__iter__

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GICTransformer.IGICTransformer.__len__

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.GICTransformer.IGICTransformer.batch

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.GICTransformer.GICTransformerBatchProperties]) -> altdss.GICTransformer.GICTransformerBatch
:canonical: altdss.GICTransformer.IGICTransformer.batch_new

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GICTransformer.IGICTransformer.begin_edit

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GICTransformer.IGICTransformer.end_edit

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.GICTransformer.IGICTransformer.find

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.find
```

````

````{py:attribute} kVLL1
:canonical: altdss.GICTransformer.IGICTransformer.kVLL1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.kVLL1
```

````

````{py:attribute} kVLL2
:canonical: altdss.GICTransformer.IGICTransformer.kVLL2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.kVLL2
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.GICTransformer.GICTransformerProperties]) -> altdss.GICTransformer.GICTransformer
:canonical: altdss.GICTransformer.IGICTransformer.new

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.new
```

````

````{py:attribute} pctPerm
:canonical: altdss.GICTransformer.IGICTransformer.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.pctPerm
```

````

````{py:attribute} pctR1
:canonical: altdss.GICTransformer.IGICTransformer.pctR1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.pctR1
```

````

````{py:attribute} pctR2
:canonical: altdss.GICTransformer.IGICTransformer.pctR2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.pctR2
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GICTransformer.IGICTransformer.to_json

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GICTransformer.IGICTransformer.to_list

```{autodoc2-docstring} altdss.GICTransformer.IGICTransformer.to_list
```

````

`````
