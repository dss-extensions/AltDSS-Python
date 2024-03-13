# {py:mod}`altdss.AutoTrans`

```{py:module} altdss.AutoTrans
```

```{autodoc2-docstring} altdss.AutoTrans
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AutoTrans <altdss.AutoTrans.AutoTrans>`
  - ```{autodoc2-docstring} altdss.AutoTrans.AutoTrans
    :summary:
    ```
* - {py:obj}`AutoTransBatch <altdss.AutoTrans.AutoTransBatch>`
  - ```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch
    :summary:
    ```
* - {py:obj}`AutoTransBatchProperties <altdss.AutoTrans.AutoTransBatchProperties>`
  - ```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties
    :summary:
    ```
* - {py:obj}`AutoTransProperties <altdss.AutoTrans.AutoTransProperties>`
  - ```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties
    :summary:
    ```
* - {py:obj}`IAutoTrans <altdss.AutoTrans.IAutoTrans>`
  - ```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans
    :summary:
    ```
````

### API

`````{py:class} AutoTrans(api_util, ptr)
:canonical: altdss.AutoTrans.AutoTrans

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PDElement.PDElementMixin`, {py:obj}`altdss.TransformerExtras.TransformerObjMixin`

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans
```

````{py:method} AccumulatedL() -> float
:canonical: altdss.AutoTrans.AutoTrans.AccumulatedL

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.AccumulatedL
```

````

````{py:attribute} Bank
:canonical: altdss.AutoTrans.AutoTrans.Bank
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.AutoTrans.AutoTrans.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.AutoTrans.AutoTrans.Buses
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Buses
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.AutoTrans.AutoTrans.Close

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.ComplexSeqCurrents

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.ComplexSeqVoltages

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.ComplexSeqVoltages
```

````

````{py:attribute} Conns
:canonical: altdss.AutoTrans.AutoTrans.Conns
:type: altdss.enums.AutoTransConnection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Conns
```

````

````{py:attribute} Conns_str
:canonical: altdss.AutoTrans.AutoTrans.Conns_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Conns_str
```

````

````{py:attribute} Core
:canonical: altdss.AutoTrans.AutoTrans.Core
:type: altdss.enums.CoreType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Core
```

````

````{py:attribute} Core_str
:canonical: altdss.AutoTrans.AutoTrans.Core_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Core_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.Currents

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.AutoTrans.AutoTrans.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.DisplayName
```

````

````{py:attribute} EmergAmps
:canonical: altdss.AutoTrans.AutoTrans.EmergAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.AutoTrans.AutoTrans.EmergHkVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.AutoTrans.AutoTrans.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Enabled
```

````

````{py:method} EnergyMeter() -> typing.Optional[altdss.DSSObj.DSSObj]
:canonical: altdss.AutoTrans.AutoTrans.EnergyMeter

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.AutoTrans.AutoTrans.EnergyMeterName

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.EnergyMeterName
```

````

````{py:attribute} FLRise
:canonical: altdss.AutoTrans.AutoTrans.FLRise
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.AutoTrans.AutoTrans.FaultRate
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.FaultRate
```

````

````{py:method} FromTerminal() -> int
:canonical: altdss.AutoTrans.AutoTrans.FromTerminal

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.FromTerminal
```

````

````{py:method} FullName() -> str
:canonical: altdss.AutoTrans.AutoTrans.FullName

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.AutoTrans.AutoTrans.GUID

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.GUID
```

````

````{py:attribute} HSRise
:canonical: altdss.AutoTrans.AutoTrans.HSRise
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.HSRise
```

````

````{py:method} Handle() -> int
:canonical: altdss.AutoTrans.AutoTrans.Handle

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.AutoTrans.AutoTrans.HasOCPDevice

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.AutoTrans.AutoTrans.HasSwitchControl

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.AutoTrans.AutoTrans.HasVoltControl

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.AutoTrans.AutoTrans.IsIsolated

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.AutoTrans.AutoTrans.IsOpen

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.IsOpen
```

````

````{py:method} IsShunt() -> bool
:canonical: altdss.AutoTrans.AutoTrans.IsShunt

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.IsShunt
```

````

````{py:method} Lambda() -> float
:canonical: altdss.AutoTrans.AutoTrans.Lambda

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Lambda
```

````

````{py:attribute} LeadLag
:canonical: altdss.AutoTrans.AutoTrans.LeadLag
:type: altdss.enums.PhaseSequence
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.LeadLag
```

````

````{py:attribute} LeadLag_str
:canonical: altdss.AutoTrans.AutoTrans.LeadLag_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.LeadLag_str
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.AutoTrans.AutoTrans.Like

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.AutoTrans.AutoTrans.Losses

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Losses
```

````

````{py:method} LossesByType() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.LossesByType

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.LossesByType
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.AutoTrans.AutoTrans.MaxCurrent

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.MaxCurrent
```

````

````{py:attribute} MaxTap
:canonical: altdss.AutoTrans.AutoTrans.MaxTap
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.AutoTrans.AutoTrans.MinTap
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.MinTap
```

````

````{py:property} Name
:canonical: altdss.AutoTrans.AutoTrans.Name
:type: str

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTrans.NodeOrder

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTrans.NodeRef

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NodeRef
```

````

````{py:attribute} NormAmps
:canonical: altdss.AutoTrans.AutoTrans.NormAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.AutoTrans.AutoTrans.NormHkVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NormHkVA
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.AutoTrans.AutoTrans.NumConductors

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.AutoTrans.AutoTrans.NumControllers

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NumControllers
```

````

````{py:method} NumCustomers() -> int
:canonical: altdss.AutoTrans.AutoTrans.NumCustomers

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NumCustomers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.AutoTrans.AutoTrans.NumPhases

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NumPhases
```

````

````{py:attribute} NumTaps
:canonical: altdss.AutoTrans.AutoTrans.NumTaps
:type: altdss.types.Int32Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NumTaps
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.AutoTrans.AutoTrans.NumTerminals

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.AutoTrans.AutoTrans.OCPDevice

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.AutoTrans.AutoTrans.OCPDeviceIndex

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.AutoTrans.AutoTrans.OCPDeviceType

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.AutoTrans.AutoTrans.Open

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Open
```

````

````{py:method} ParentPDElement() -> typing.Optional[altdss.DSSObj.DSSObj]
:canonical: altdss.AutoTrans.AutoTrans.ParentPDElement

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.PhaseLosses

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.AutoTrans.AutoTrans.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.Powers

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Powers
```

````

````{py:attribute} RDCOhms
:canonical: altdss.AutoTrans.AutoTrans.RDCOhms
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.RDCOhms
```

````

````{py:attribute} Repair
:canonical: altdss.AutoTrans.AutoTrans.Repair
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Repair
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTrans.Residuals

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Residuals
```

````

````{py:method} SectionID() -> int
:canonical: altdss.AutoTrans.AutoTrans.SectionID

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTrans.SeqCurrents

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.SeqPowers

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTrans.SeqVoltages

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.SeqVoltages
```

````

````{py:attribute} Sub
:canonical: altdss.AutoTrans.AutoTrans.Sub
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.AutoTrans.AutoTrans.SubName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.AutoTrans.AutoTrans.Taps
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.AutoTrans.AutoTrans.Thermal
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Thermal
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.AutoTrans.AutoTrans.TotalCustomers

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.TotalCustomers
```

````

````{py:method} TotalKilometers() -> float
:canonical: altdss.AutoTrans.AutoTrans.TotalKilometers

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.TotalKilometers
```

````

````{py:method} TotalMiles() -> float
:canonical: altdss.AutoTrans.AutoTrans.TotalMiles

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.TotalPowers

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.Voltages

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTrans.VoltagesMagAng

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.VoltagesMagAng
```

````

````{py:method} WindingCurrents() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.WindingCurrents

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.WindingCurrents
```

````

````{py:method} WindingVoltages(winding: int) -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.WindingVoltages

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.WindingVoltages
```

````

````{py:attribute} Windings
:canonical: altdss.AutoTrans.AutoTrans.Windings
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.Windings
```

````

````{py:attribute} XHT
:canonical: altdss.AutoTrans.AutoTrans.XHT
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.XHT
```

````

````{py:attribute} XHX
:canonical: altdss.AutoTrans.AutoTrans.XHX
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.XHX
```

````

````{py:attribute} XRConst
:canonical: altdss.AutoTrans.AutoTrans.XRConst
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.AutoTrans.AutoTrans.XSCArray
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.XSCArray
```

````

````{py:attribute} XXT
:canonical: altdss.AutoTrans.AutoTrans.XXT
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.XXT
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTrans.YPrim

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.AutoTrans.AutoTrans.__hash__

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.AutoTrans.AutoTrans.__init__

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.AutoTrans.AutoTrans.__ne__

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.AutoTrans.AutoTrans.__repr__

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.AutoTrans.AutoTrans.begin_edit

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.AutoTrans.AutoTrans.end_edit

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.end_edit
```

````

````{py:attribute} kVAs
:canonical: altdss.AutoTrans.AutoTrans.kVAs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.AutoTrans.AutoTrans.kVs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.kVs
```

````

````{py:attribute} m
:canonical: altdss.AutoTrans.AutoTrans.m
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.m
```

````

````{py:attribute} n
:canonical: altdss.AutoTrans.AutoTrans.n
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.n
```

````

````{py:method} pctEmergency(allNodes=False) -> float
:canonical: altdss.AutoTrans.AutoTrans.pctEmergency

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.pctEmergency
```

````

````{py:attribute} pctIMag
:canonical: altdss.AutoTrans.AutoTrans.pctIMag
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.AutoTrans.AutoTrans.pctLoadLoss
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.AutoTrans.AutoTrans.pctNoLoadLoss
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.pctNoLoadLoss
```

````

````{py:method} pctNormal(allNodes=False) -> float
:canonical: altdss.AutoTrans.AutoTrans.pctNormal

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.pctNormal
```

````

````{py:attribute} pctPerm
:canonical: altdss.AutoTrans.AutoTrans.pctPerm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.AutoTrans.AutoTrans.pctR
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.AutoTrans.AutoTrans.pctRs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.pctRs
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.AutoTrans.AutoTrans.ppm_Antifloat
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.ppm_Antifloat
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.AutoTrans.AutoTrans.to_json

```{autodoc2-docstring} altdss.AutoTrans.AutoTrans.to_json
```

````

`````

`````{py:class} AutoTransBatch(api_util, **kwargs)
:canonical: altdss.AutoTrans.AutoTransBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PDElement.PDElementBatchMixin`

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.AccumulatedL

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.AccumulatedL
```

````

````{py:attribute} Bank
:canonical: altdss.AutoTrans.AutoTransBatch.Bank
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.AutoTrans.AutoTransBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.AutoTrans.AutoTransBatch.Buses
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Buses
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTransBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTransBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conns
:canonical: altdss.AutoTrans.AutoTransBatch.Conns
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Conns
```

````

````{py:attribute} Conns_str
:canonical: altdss.AutoTrans.AutoTransBatch.Conns_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Conns_str
```

````

````{py:attribute} Core
:canonical: altdss.AutoTrans.AutoTransBatch.Core
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Core
```

````

````{py:attribute} Core_str
:canonical: altdss.AutoTrans.AutoTransBatch.Core_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Core_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTransBatch.Currents

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.AutoTrans.AutoTransBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.AutoTrans.AutoTransBatch.EmergHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.AutoTrans.AutoTransBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.AutoTrans.AutoTransBatch.EnergyMeter

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.AutoTrans.AutoTransBatch.EnergyMeterName

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.EnergyMeterName
```

````

````{py:attribute} FLRise
:canonical: altdss.AutoTrans.AutoTransBatch.FLRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.AutoTrans.AutoTransBatch.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.FromTerminal

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.AutoTrans.AutoTransBatch.FullName

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.AutoTrans.AutoTransBatch.GUID

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.GUID
```

````

````{py:attribute} HSRise
:canonical: altdss.AutoTrans.AutoTransBatch.HSRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.HSRise
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.Handle

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.AutoTrans.AutoTransBatch.HasOCPDevice

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.AutoTrans.AutoTransBatch.HasSwitchControl

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.AutoTrans.AutoTransBatch.HasVoltControl

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.AutoTrans.AutoTransBatch.IsIsolated

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.AutoTrans.AutoTransBatch.IsShunt

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.Lambda

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Lambda
```

````

````{py:attribute} LeadLag
:canonical: altdss.AutoTrans.AutoTransBatch.LeadLag
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.LeadLag
```

````

````{py:attribute} LeadLag_str
:canonical: altdss.AutoTrans.AutoTransBatch.LeadLag_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.LeadLag_str
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.AutoTrans.AutoTransBatch.Like

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTransBatch.Losses

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.MaxCurrent

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.MaxCurrent
```

````

````{py:attribute} MaxTap
:canonical: altdss.AutoTrans.AutoTransBatch.MaxTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.AutoTrans.AutoTransBatch.MinTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.MinTap
```

````

````{py:property} Name
:canonical: altdss.AutoTrans.AutoTransBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.AutoTrans.AutoTransBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.AutoTrans.AutoTransBatch.NormHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.NormHkVA
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.NumConductors

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.NumControllers

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.NumCustomers

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.NumPhases

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.NumPhases
```

````

````{py:attribute} NumTaps
:canonical: altdss.AutoTrans.AutoTransBatch.NumTaps
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.NumTaps
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.NumTerminals

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.AutoTrans.AutoTransBatch.OCPDevice

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.AutoTrans.AutoTransBatch.OCPDeviceType

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.AutoTrans.AutoTransBatch.ParentPDElement

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTransBatch.PhaseLosses

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.AutoTrans.AutoTransBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTransBatch.Powers

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Powers
```

````

````{py:attribute} RDCOhms
:canonical: altdss.AutoTrans.AutoTransBatch.RDCOhms
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.RDCOhms
```

````

````{py:attribute} Repair
:canonical: altdss.AutoTrans.AutoTransBatch.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Repair
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.SectionID

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.SeqCurrents

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTransBatch.SeqPowers

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.SeqVoltages

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.SeqVoltages
```

````

````{py:attribute} Sub
:canonical: altdss.AutoTrans.AutoTransBatch.Sub
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.AutoTrans.AutoTransBatch.SubName
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.AutoTrans.AutoTransBatch.Taps
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.AutoTrans.AutoTransBatch.Thermal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Thermal
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.AutoTransBatch.TotalCustomers

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.TotalCustomers
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.TotalKilometers

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.TotalMiles

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTransBatch.TotalPowers

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.AutoTransBatch.Voltages

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.VoltagesMagAng
```

````

````{py:attribute} Windings
:canonical: altdss.AutoTrans.AutoTransBatch.Windings
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.Windings
```

````

````{py:attribute} XHT
:canonical: altdss.AutoTrans.AutoTransBatch.XHT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.XHT
```

````

````{py:attribute} XHX
:canonical: altdss.AutoTrans.AutoTransBatch.XHX
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.XHX
```

````

````{py:attribute} XRConst
:canonical: altdss.AutoTrans.AutoTransBatch.XRConst
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.AutoTrans.AutoTransBatch.XSCArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.XSCArray
```

````

````{py:attribute} XXT
:canonical: altdss.AutoTrans.AutoTransBatch.XXT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.XXT
```

````

````{py:method} __call__()
:canonical: altdss.AutoTrans.AutoTransBatch.__call__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.AutoTrans.AutoTransBatch.__getitem__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.AutoTrans.AutoTransBatch.__init__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.AutoTrans.AutoTransBatch.__iter__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.AutoTrans.AutoTransBatch.__len__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.AutoTrans.AutoTransBatch.batch

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.AutoTrans.AutoTransBatch.begin_edit

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.AutoTrans.AutoTransBatch.end_edit

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.end_edit
```

````

````{py:attribute} kVAs
:canonical: altdss.AutoTrans.AutoTransBatch.kVAs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.AutoTrans.AutoTransBatch.kVs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.kVs
```

````

````{py:attribute} m
:canonical: altdss.AutoTrans.AutoTransBatch.m
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.m
```

````

````{py:attribute} n
:canonical: altdss.AutoTrans.AutoTransBatch.n
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.n
```

````

````{py:method} pctEmergency(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.pctEmergency

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.pctEmergency
```

````

````{py:attribute} pctIMag
:canonical: altdss.AutoTrans.AutoTransBatch.pctIMag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.AutoTrans.AutoTransBatch.pctLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.AutoTrans.AutoTransBatch.pctNoLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.pctNoLoadLoss
```

````

````{py:method} pctNormal(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.AutoTransBatch.pctNormal

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.pctNormal
```

````

````{py:attribute} pctPerm
:canonical: altdss.AutoTrans.AutoTransBatch.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.AutoTrans.AutoTransBatch.pctR
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.AutoTrans.AutoTransBatch.pctRs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.pctRs
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.AutoTrans.AutoTransBatch.ppm_Antifloat
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.ppm_Antifloat
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.AutoTrans.AutoTransBatch.to_json

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.AutoTrans.AutoTransBatch.to_list

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatch.to_list
```

````

`````

`````{py:class} AutoTransBatchProperties()
:canonical: altdss.AutoTrans.AutoTransBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties
```

````{py:attribute} Bank
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Bank
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.AutoTrans.AutoTransBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Buses
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Buses
```

````

````{py:attribute} Conns
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Conns
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.AutoTransConnection]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Conns
```

````

````{py:attribute} Core
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Core
:type: typing.Union[typing.AnyStr, int, altdss.enums.CoreType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.CoreType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Core
```

````

````{py:attribute} EmergAmps
:canonical: altdss.AutoTrans.AutoTransBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.AutoTrans.AutoTransBatchProperties.EmergHkVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Enabled
```

````

````{py:attribute} FLRise
:canonical: altdss.AutoTrans.AutoTransBatchProperties.FLRise
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.AutoTrans.AutoTransBatchProperties.FaultRate
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.FaultRate
```

````

````{py:attribute} HSRise
:canonical: altdss.AutoTrans.AutoTransBatchProperties.HSRise
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.HSRise
```

````

````{py:attribute} LeadLag
:canonical: altdss.AutoTrans.AutoTransBatchProperties.LeadLag
:type: typing.Union[typing.AnyStr, int, altdss.enums.PhaseSequence, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.PhaseSequence], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.LeadLag
```

````

````{py:attribute} Like
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Like
```

````

````{py:attribute} MaxTap
:canonical: altdss.AutoTrans.AutoTransBatchProperties.MaxTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.AutoTrans.AutoTransBatchProperties.MinTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.MinTap
```

````

````{py:attribute} NormAmps
:canonical: altdss.AutoTrans.AutoTransBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.AutoTrans.AutoTransBatchProperties.NormHkVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.NormHkVA
```

````

````{py:attribute} NumTaps
:canonical: altdss.AutoTrans.AutoTransBatchProperties.NumTaps
:type: altdss.types.Int32Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.NumTaps
```

````

````{py:attribute} Phases
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Phases
```

````

````{py:attribute} RDCOhms
:canonical: altdss.AutoTrans.AutoTransBatchProperties.RDCOhms
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.RDCOhms
```

````

````{py:attribute} Repair
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Repair
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Repair
```

````

````{py:attribute} Sub
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Sub
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.AutoTrans.AutoTransBatchProperties.SubName
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Taps
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Thermal
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Thermal
```

````

````{py:attribute} Windings
:canonical: altdss.AutoTrans.AutoTransBatchProperties.Windings
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.Windings
```

````

````{py:attribute} XHT
:canonical: altdss.AutoTrans.AutoTransBatchProperties.XHT
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.XHT
```

````

````{py:attribute} XHX
:canonical: altdss.AutoTrans.AutoTransBatchProperties.XHX
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.XHX
```

````

````{py:attribute} XRConst
:canonical: altdss.AutoTrans.AutoTransBatchProperties.XRConst
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.AutoTrans.AutoTransBatchProperties.XSCArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.XSCArray
```

````

````{py:attribute} XXT
:canonical: altdss.AutoTrans.AutoTransBatchProperties.XXT
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.XXT
```

````

````{py:method} __contains__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__contains__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__delattr__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__delitem__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__dir__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__format__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__ge__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__getitem__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__getstate__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__gt__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__init__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__ior__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__iter__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__le__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__len__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__lt__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__ne__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__new__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__or__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__reduce__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__repr__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__reversed__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__ror__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__setitem__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__str__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.clear

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.copy

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.get

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.items

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.items
```

````

````{py:attribute} kVAs
:canonical: altdss.AutoTrans.AutoTransBatchProperties.kVAs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.AutoTrans.AutoTransBatchProperties.kVs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.kVs
```

````

````{py:method} keys()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.keys

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.keys
```

````

````{py:attribute} m
:canonical: altdss.AutoTrans.AutoTransBatchProperties.m
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.m
```

````

````{py:attribute} n
:canonical: altdss.AutoTrans.AutoTransBatchProperties.n
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.n
```

````

````{py:attribute} pctIMag
:canonical: altdss.AutoTrans.AutoTransBatchProperties.pctIMag
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.AutoTrans.AutoTransBatchProperties.pctLoadLoss
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.AutoTrans.AutoTransBatchProperties.pctNoLoadLoss
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.pctNoLoadLoss
```

````

````{py:attribute} pctPerm
:canonical: altdss.AutoTrans.AutoTransBatchProperties.pctPerm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.AutoTrans.AutoTransBatchProperties.pctR
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.AutoTrans.AutoTransBatchProperties.pctRs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.pctRs
```

````

````{py:method} pop()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.pop

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.popitem

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.popitem
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.AutoTrans.AutoTransBatchProperties.ppm_Antifloat
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.ppm_Antifloat
```

````

````{py:method} setdefault()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.setdefault

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.update

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.AutoTrans.AutoTransBatchProperties.values

```{autodoc2-docstring} altdss.AutoTrans.AutoTransBatchProperties.values
```

````

`````

`````{py:class} AutoTransProperties()
:canonical: altdss.AutoTrans.AutoTransProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties
```

````{py:attribute} Bank
:canonical: altdss.AutoTrans.AutoTransProperties.Bank
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.AutoTrans.AutoTransProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.AutoTrans.AutoTransProperties.Buses
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Buses
```

````

````{py:attribute} Conns
:canonical: altdss.AutoTrans.AutoTransProperties.Conns
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.AutoTransConnection]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Conns
```

````

````{py:attribute} Core
:canonical: altdss.AutoTrans.AutoTransProperties.Core
:type: typing.Union[typing.AnyStr, int, altdss.enums.CoreType]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Core
```

````

````{py:attribute} EmergAmps
:canonical: altdss.AutoTrans.AutoTransProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.AutoTrans.AutoTransProperties.EmergHkVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.AutoTrans.AutoTransProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Enabled
```

````

````{py:attribute} FLRise
:canonical: altdss.AutoTrans.AutoTransProperties.FLRise
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.AutoTrans.AutoTransProperties.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.FaultRate
```

````

````{py:attribute} HSRise
:canonical: altdss.AutoTrans.AutoTransProperties.HSRise
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.HSRise
```

````

````{py:attribute} LeadLag
:canonical: altdss.AutoTrans.AutoTransProperties.LeadLag
:type: typing.Union[typing.AnyStr, int, altdss.enums.PhaseSequence]
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.LeadLag
```

````

````{py:attribute} Like
:canonical: altdss.AutoTrans.AutoTransProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Like
```

````

````{py:attribute} MaxTap
:canonical: altdss.AutoTrans.AutoTransProperties.MaxTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.AutoTrans.AutoTransProperties.MinTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.MinTap
```

````

````{py:attribute} NormAmps
:canonical: altdss.AutoTrans.AutoTransProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.AutoTrans.AutoTransProperties.NormHkVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.NormHkVA
```

````

````{py:attribute} NumTaps
:canonical: altdss.AutoTrans.AutoTransProperties.NumTaps
:type: altdss.types.Int32Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.NumTaps
```

````

````{py:attribute} Phases
:canonical: altdss.AutoTrans.AutoTransProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Phases
```

````

````{py:attribute} RDCOhms
:canonical: altdss.AutoTrans.AutoTransProperties.RDCOhms
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.RDCOhms
```

````

````{py:attribute} Repair
:canonical: altdss.AutoTrans.AutoTransProperties.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Repair
```

````

````{py:attribute} Sub
:canonical: altdss.AutoTrans.AutoTransProperties.Sub
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.AutoTrans.AutoTransProperties.SubName
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.AutoTrans.AutoTransProperties.Taps
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.AutoTrans.AutoTransProperties.Thermal
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Thermal
```

````

````{py:attribute} Windings
:canonical: altdss.AutoTrans.AutoTransProperties.Windings
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.Windings
```

````

````{py:attribute} XHT
:canonical: altdss.AutoTrans.AutoTransProperties.XHT
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.XHT
```

````

````{py:attribute} XHX
:canonical: altdss.AutoTrans.AutoTransProperties.XHX
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.XHX
```

````

````{py:attribute} XRConst
:canonical: altdss.AutoTrans.AutoTransProperties.XRConst
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.AutoTrans.AutoTransProperties.XSCArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.XSCArray
```

````

````{py:attribute} XXT
:canonical: altdss.AutoTrans.AutoTransProperties.XXT
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.XXT
```

````

````{py:method} __contains__()
:canonical: altdss.AutoTrans.AutoTransProperties.__contains__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.AutoTrans.AutoTransProperties.__delattr__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.AutoTrans.AutoTransProperties.__delitem__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.AutoTrans.AutoTransProperties.__dir__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.AutoTrans.AutoTransProperties.__format__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.AutoTrans.AutoTransProperties.__ge__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.AutoTrans.AutoTransProperties.__getattribute__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.AutoTrans.AutoTransProperties.__getitem__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.AutoTrans.AutoTransProperties.__getstate__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.AutoTrans.AutoTransProperties.__gt__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.AutoTrans.AutoTransProperties.__init__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.AutoTrans.AutoTransProperties.__ior__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.AutoTrans.AutoTransProperties.__iter__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.AutoTrans.AutoTransProperties.__le__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.AutoTrans.AutoTransProperties.__len__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.AutoTrans.AutoTransProperties.__lt__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.AutoTrans.AutoTransProperties.__ne__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.AutoTrans.AutoTransProperties.__new__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.AutoTrans.AutoTransProperties.__or__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.AutoTrans.AutoTransProperties.__reduce__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.AutoTrans.AutoTransProperties.__reduce_ex__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.AutoTrans.AutoTransProperties.__repr__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.AutoTrans.AutoTransProperties.__reversed__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.AutoTrans.AutoTransProperties.__ror__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.AutoTrans.AutoTransProperties.__setitem__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.AutoTrans.AutoTransProperties.__sizeof__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.AutoTrans.AutoTransProperties.__str__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.AutoTrans.AutoTransProperties.__subclasshook__

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.AutoTrans.AutoTransProperties.clear

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.AutoTrans.AutoTransProperties.copy

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.copy
```

````

````{py:method} get()
:canonical: altdss.AutoTrans.AutoTransProperties.get

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.get
```

````

````{py:method} items()
:canonical: altdss.AutoTrans.AutoTransProperties.items

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.items
```

````

````{py:attribute} kVAs
:canonical: altdss.AutoTrans.AutoTransProperties.kVAs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.AutoTrans.AutoTransProperties.kVs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.kVs
```

````

````{py:method} keys()
:canonical: altdss.AutoTrans.AutoTransProperties.keys

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.keys
```

````

````{py:attribute} m
:canonical: altdss.AutoTrans.AutoTransProperties.m
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.m
```

````

````{py:attribute} n
:canonical: altdss.AutoTrans.AutoTransProperties.n
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.n
```

````

````{py:attribute} pctIMag
:canonical: altdss.AutoTrans.AutoTransProperties.pctIMag
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.AutoTrans.AutoTransProperties.pctLoadLoss
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.AutoTrans.AutoTransProperties.pctNoLoadLoss
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.pctNoLoadLoss
```

````

````{py:attribute} pctPerm
:canonical: altdss.AutoTrans.AutoTransProperties.pctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.AutoTrans.AutoTransProperties.pctR
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.AutoTrans.AutoTransProperties.pctRs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.pctRs
```

````

````{py:method} pop()
:canonical: altdss.AutoTrans.AutoTransProperties.pop

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.AutoTrans.AutoTransProperties.popitem

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.popitem
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.AutoTrans.AutoTransProperties.ppm_Antifloat
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.ppm_Antifloat
```

````

````{py:method} setdefault()
:canonical: altdss.AutoTrans.AutoTransProperties.setdefault

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.AutoTrans.AutoTransProperties.update

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.update
```

````

````{py:method} values()
:canonical: altdss.AutoTrans.AutoTransProperties.values

```{autodoc2-docstring} altdss.AutoTrans.AutoTransProperties.values
```

````

`````

`````{py:class} IAutoTrans(iobj)
:canonical: altdss.AutoTrans.IAutoTrans

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.AutoTrans.AutoTransBatch`

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.AccumulatedL

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.AccumulatedL
```

````

````{py:attribute} Bank
:canonical: altdss.AutoTrans.IAutoTrans.Bank
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.AutoTrans.IAutoTrans.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.AutoTrans.IAutoTrans.Buses
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Buses
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.IAutoTrans.ComplexSeqCurrents

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.IAutoTrans.ComplexSeqVoltages

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.ComplexSeqVoltages
```

````

````{py:attribute} Conns
:canonical: altdss.AutoTrans.IAutoTrans.Conns
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Conns
```

````

````{py:attribute} Conns_str
:canonical: altdss.AutoTrans.IAutoTrans.Conns_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Conns_str
```

````

````{py:attribute} Core
:canonical: altdss.AutoTrans.IAutoTrans.Core
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Core
```

````

````{py:attribute} Core_str
:canonical: altdss.AutoTrans.IAutoTrans.Core_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Core_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.IAutoTrans.Currents

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.CurrentsMagAng

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.AutoTrans.IAutoTrans.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.AutoTrans.IAutoTrans.EmergHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.AutoTrans.IAutoTrans.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.AutoTrans.IAutoTrans.EnergyMeter

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.AutoTrans.IAutoTrans.EnergyMeterName

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.EnergyMeterName
```

````

````{py:attribute} FLRise
:canonical: altdss.AutoTrans.IAutoTrans.FLRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.AutoTrans.IAutoTrans.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.FromTerminal

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.AutoTrans.IAutoTrans.FullName

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.AutoTrans.IAutoTrans.GUID

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.GUID
```

````

````{py:attribute} HSRise
:canonical: altdss.AutoTrans.IAutoTrans.HSRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.HSRise
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.Handle

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.AutoTrans.IAutoTrans.HasOCPDevice

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.AutoTrans.IAutoTrans.HasSwitchControl

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.AutoTrans.IAutoTrans.HasVoltControl

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.AutoTrans.IAutoTrans.IsIsolated

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.AutoTrans.IAutoTrans.IsShunt

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.Lambda

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Lambda
```

````

````{py:attribute} LeadLag
:canonical: altdss.AutoTrans.IAutoTrans.LeadLag
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.LeadLag
```

````

````{py:attribute} LeadLag_str
:canonical: altdss.AutoTrans.IAutoTrans.LeadLag_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.LeadLag_str
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.AutoTrans.IAutoTrans.Like

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.IAutoTrans.Losses

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.MaxCurrent

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.MaxCurrent
```

````

````{py:attribute} MaxTap
:canonical: altdss.AutoTrans.IAutoTrans.MaxTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.AutoTrans.IAutoTrans.MinTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.MinTap
```

````

````{py:property} Name
:canonical: altdss.AutoTrans.IAutoTrans.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.AutoTrans.IAutoTrans.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.AutoTrans.IAutoTrans.NormHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.NormHkVA
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.NumConductors

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.NumControllers

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.NumCustomers

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.NumPhases

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.NumPhases
```

````

````{py:attribute} NumTaps
:canonical: altdss.AutoTrans.IAutoTrans.NumTaps
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.NumTaps
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.NumTerminals

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.AutoTrans.IAutoTrans.OCPDevice

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.OCPDeviceIndex

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.AutoTrans.IAutoTrans.OCPDeviceType

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.AutoTrans.IAutoTrans.ParentPDElement

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.IAutoTrans.PhaseLosses

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.AutoTrans.IAutoTrans.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.IAutoTrans.Powers

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Powers
```

````

````{py:attribute} RDCOhms
:canonical: altdss.AutoTrans.IAutoTrans.RDCOhms
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.RDCOhms
```

````

````{py:attribute} Repair
:canonical: altdss.AutoTrans.IAutoTrans.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Repair
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.SectionID

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.SeqCurrents

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.IAutoTrans.SeqPowers

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.SeqVoltages

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.SeqVoltages
```

````

````{py:attribute} Sub
:canonical: altdss.AutoTrans.IAutoTrans.Sub
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.AutoTrans.IAutoTrans.SubName
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.AutoTrans.IAutoTrans.Taps
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.AutoTrans.IAutoTrans.Thermal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Thermal
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.AutoTrans.IAutoTrans.TotalCustomers

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.TotalCustomers
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.TotalKilometers

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.TotalMiles

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.IAutoTrans.TotalPowers

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.AutoTrans.IAutoTrans.Voltages

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.VoltagesMagAng

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.VoltagesMagAng
```

````

````{py:attribute} Windings
:canonical: altdss.AutoTrans.IAutoTrans.Windings
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.Windings
```

````

````{py:attribute} XHT
:canonical: altdss.AutoTrans.IAutoTrans.XHT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.XHT
```

````

````{py:attribute} XHX
:canonical: altdss.AutoTrans.IAutoTrans.XHX
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.XHX
```

````

````{py:attribute} XRConst
:canonical: altdss.AutoTrans.IAutoTrans.XRConst
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.AutoTrans.IAutoTrans.XSCArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.XSCArray
```

````

````{py:attribute} XXT
:canonical: altdss.AutoTrans.IAutoTrans.XXT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.XXT
```

````

````{py:method} __call__()
:canonical: altdss.AutoTrans.IAutoTrans.__call__

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.AutoTrans.IAutoTrans.__contains__

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.AutoTrans.IAutoTrans.__getitem__

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.AutoTrans.IAutoTrans.__init__

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.AutoTrans.IAutoTrans.__iter__

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.AutoTrans.IAutoTrans.__len__

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.AutoTrans.IAutoTrans.batch

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.AutoTrans.AutoTransBatchProperties]) -> altdss.AutoTrans.AutoTransBatch
:canonical: altdss.AutoTrans.IAutoTrans.batch_new

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.AutoTrans.IAutoTrans.begin_edit

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.AutoTrans.IAutoTrans.end_edit

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.AutoTrans.IAutoTrans.find

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.find
```

````

````{py:attribute} kVAs
:canonical: altdss.AutoTrans.IAutoTrans.kVAs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.AutoTrans.IAutoTrans.kVs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.kVs
```

````

````{py:attribute} m
:canonical: altdss.AutoTrans.IAutoTrans.m
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.m
```

````

````{py:attribute} n
:canonical: altdss.AutoTrans.IAutoTrans.n
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.n
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.AutoTrans.AutoTransProperties]) -> altdss.AutoTrans.AutoTrans
:canonical: altdss.AutoTrans.IAutoTrans.new

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.new
```

````

````{py:method} pctEmergency(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.pctEmergency

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.pctEmergency
```

````

````{py:attribute} pctIMag
:canonical: altdss.AutoTrans.IAutoTrans.pctIMag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.AutoTrans.IAutoTrans.pctLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.AutoTrans.IAutoTrans.pctNoLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.pctNoLoadLoss
```

````

````{py:method} pctNormal(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.AutoTrans.IAutoTrans.pctNormal

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.pctNormal
```

````

````{py:attribute} pctPerm
:canonical: altdss.AutoTrans.IAutoTrans.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.AutoTrans.IAutoTrans.pctR
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.AutoTrans.IAutoTrans.pctRs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.pctRs
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.AutoTrans.IAutoTrans.ppm_Antifloat
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.ppm_Antifloat
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.AutoTrans.IAutoTrans.to_json

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.to_json
```

````

````{py:method} to_list()
:canonical: altdss.AutoTrans.IAutoTrans.to_list

```{autodoc2-docstring} altdss.AutoTrans.IAutoTrans.to_list
```

````

`````
