# {py:mod}`altdss.Fault`

```{py:module} altdss.Fault
```

```{autodoc2-docstring} altdss.Fault
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Fault <altdss.Fault.Fault>`
  - ```{autodoc2-docstring} altdss.Fault.Fault
    :summary:
    ```
* - {py:obj}`FaultBatch <altdss.Fault.FaultBatch>`
  - ```{autodoc2-docstring} altdss.Fault.FaultBatch
    :summary:
    ```
* - {py:obj}`FaultBatchProperties <altdss.Fault.FaultBatchProperties>`
  - ```{autodoc2-docstring} altdss.Fault.FaultBatchProperties
    :summary:
    ```
* - {py:obj}`FaultProperties <altdss.Fault.FaultProperties>`
  - ```{autodoc2-docstring} altdss.Fault.FaultProperties
    :summary:
    ```
* - {py:obj}`IFault <altdss.Fault.IFault>`
  - ```{autodoc2-docstring} altdss.Fault.IFault
    :summary:
    ```
````

### API

`````{py:class} Fault(api_util, ptr)
:canonical: altdss.Fault.Fault

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PDElement.PDElementMixin`

```{autodoc2-docstring} altdss.Fault.Fault
```

````{py:method} AccumulatedL() -> float
:canonical: altdss.Fault.Fault.AccumulatedL

```{autodoc2-docstring} altdss.Fault.Fault.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Fault.Fault.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Fault.Fault.Bus1
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Fault.Fault.Bus2
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.Bus2
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Fault.Fault.Close

```{autodoc2-docstring} altdss.Fault.Fault.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Fault.Fault.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Fault.Fault.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Fault.Fault.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Fault.Fault.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Fault.Fault.Currents

```{autodoc2-docstring} altdss.Fault.Fault.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.Fault.Fault.DisplayName
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.DisplayName
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Fault.Fault.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Fault.Fault.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.Fault.Fault.EnergyMeter

```{autodoc2-docstring} altdss.Fault.Fault.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Fault.Fault.EnergyMeterName

```{autodoc2-docstring} altdss.Fault.Fault.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Fault.Fault.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.FaultRate
```

````

````{py:method} FromTerminal() -> int
:canonical: altdss.Fault.Fault.FromTerminal

```{autodoc2-docstring} altdss.Fault.Fault.FromTerminal
```

````

````{py:method} FullName() -> str
:canonical: altdss.Fault.Fault.FullName

```{autodoc2-docstring} altdss.Fault.Fault.FullName
```

````

````{py:attribute} GMatrix
:canonical: altdss.Fault.Fault.GMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.GMatrix
```

````

````{py:method} GUID() -> str
:canonical: altdss.Fault.Fault.GUID

```{autodoc2-docstring} altdss.Fault.Fault.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.Fault.Fault.Handle

```{autodoc2-docstring} altdss.Fault.Fault.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Fault.Fault.HasOCPDevice

```{autodoc2-docstring} altdss.Fault.Fault.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Fault.Fault.HasSwitchControl

```{autodoc2-docstring} altdss.Fault.Fault.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Fault.Fault.HasVoltControl

```{autodoc2-docstring} altdss.Fault.Fault.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Fault.Fault.IsIsolated

```{autodoc2-docstring} altdss.Fault.Fault.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Fault.Fault.IsOpen

```{autodoc2-docstring} altdss.Fault.Fault.IsOpen
```

````

````{py:method} IsShunt() -> bool
:canonical: altdss.Fault.Fault.IsShunt

```{autodoc2-docstring} altdss.Fault.Fault.IsShunt
```

````

````{py:method} Lambda() -> float
:canonical: altdss.Fault.Fault.Lambda

```{autodoc2-docstring} altdss.Fault.Fault.Lambda
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Fault.Fault.Like

```{autodoc2-docstring} altdss.Fault.Fault.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Fault.Fault.Losses

```{autodoc2-docstring} altdss.Fault.Fault.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Fault.Fault.MaxCurrent

```{autodoc2-docstring} altdss.Fault.Fault.MaxCurrent
```

````

````{py:attribute} MinAmps
:canonical: altdss.Fault.Fault.MinAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.MinAmps
```

````

````{py:property} Name
:canonical: altdss.Fault.Fault.Name
:type: str

```{autodoc2-docstring} altdss.Fault.Fault.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Fault.Fault.NodeOrder

```{autodoc2-docstring} altdss.Fault.Fault.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Fault.Fault.NodeRef

```{autodoc2-docstring} altdss.Fault.Fault.NodeRef
```

````

````{py:attribute} NormAmps
:canonical: altdss.Fault.Fault.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.NormAmps
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Fault.Fault.NumConductors

```{autodoc2-docstring} altdss.Fault.Fault.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Fault.Fault.NumControllers

```{autodoc2-docstring} altdss.Fault.Fault.NumControllers
```

````

````{py:method} NumCustomers() -> int
:canonical: altdss.Fault.Fault.NumCustomers

```{autodoc2-docstring} altdss.Fault.Fault.NumCustomers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Fault.Fault.NumPhases

```{autodoc2-docstring} altdss.Fault.Fault.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Fault.Fault.NumTerminals

```{autodoc2-docstring} altdss.Fault.Fault.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Fault.Fault.OCPDevice

```{autodoc2-docstring} altdss.Fault.Fault.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Fault.Fault.OCPDeviceIndex

```{autodoc2-docstring} altdss.Fault.Fault.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Fault.Fault.OCPDeviceType

```{autodoc2-docstring} altdss.Fault.Fault.OCPDeviceType
```

````

````{py:attribute} OnTime
:canonical: altdss.Fault.Fault.OnTime
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.OnTime
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Fault.Fault.Open

```{autodoc2-docstring} altdss.Fault.Fault.Open
```

````

````{py:method} ParentPDElement() -> altdss.DSSObj.DSSObj
:canonical: altdss.Fault.Fault.ParentPDElement

```{autodoc2-docstring} altdss.Fault.Fault.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Fault.Fault.PhaseLosses

```{autodoc2-docstring} altdss.Fault.Fault.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Fault.Fault.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Fault.Fault.Powers

```{autodoc2-docstring} altdss.Fault.Fault.Powers
```

````

````{py:attribute} R
:canonical: altdss.Fault.Fault.R
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.R
```

````

````{py:attribute} Repair
:canonical: altdss.Fault.Fault.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.Repair
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Fault.Fault.Residuals

```{autodoc2-docstring} altdss.Fault.Fault.Residuals
```

````

````{py:method} SectionID() -> int
:canonical: altdss.Fault.Fault.SectionID

```{autodoc2-docstring} altdss.Fault.Fault.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Fault.Fault.SeqCurrents

```{autodoc2-docstring} altdss.Fault.Fault.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fault.Fault.SeqPowers

```{autodoc2-docstring} altdss.Fault.Fault.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Fault.Fault.SeqVoltages

```{autodoc2-docstring} altdss.Fault.Fault.SeqVoltages
```

````

````{py:attribute} Temporary
:canonical: altdss.Fault.Fault.Temporary
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.Temporary
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.Fault.Fault.TotalCustomers

```{autodoc2-docstring} altdss.Fault.Fault.TotalCustomers
```

````

````{py:method} TotalMiles() -> float
:canonical: altdss.Fault.Fault.TotalMiles

```{autodoc2-docstring} altdss.Fault.Fault.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fault.Fault.TotalPowers

```{autodoc2-docstring} altdss.Fault.Fault.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Fault.Fault.Voltages

```{autodoc2-docstring} altdss.Fault.Fault.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fault.Fault.VoltagesMagAng

```{autodoc2-docstring} altdss.Fault.Fault.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Fault.Fault.YPrim

```{autodoc2-docstring} altdss.Fault.Fault.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.Fault.Fault.__hash__

```{autodoc2-docstring} altdss.Fault.Fault.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Fault.Fault.__init__

```{autodoc2-docstring} altdss.Fault.Fault.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Fault.Fault.__ne__

```{autodoc2-docstring} altdss.Fault.Fault.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Fault.Fault.__repr__

```{autodoc2-docstring} altdss.Fault.Fault.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Fault.Fault.begin_edit

```{autodoc2-docstring} altdss.Fault.Fault.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Fault.Fault.end_edit

```{autodoc2-docstring} altdss.Fault.Fault.end_edit
```

````

````{py:method} pctEmerg(allNodes=False) -> float
:canonical: altdss.Fault.Fault.pctEmerg

```{autodoc2-docstring} altdss.Fault.Fault.pctEmerg
```

````

````{py:method} pctNorm(allNodes=False) -> float
:canonical: altdss.Fault.Fault.pctNorm

```{autodoc2-docstring} altdss.Fault.Fault.pctNorm
```

````

````{py:attribute} pctPerm
:canonical: altdss.Fault.Fault.pctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.pctPerm
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Fault.Fault.pctStdDev
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.Fault.pctStdDev
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Fault.Fault.to_json

```{autodoc2-docstring} altdss.Fault.Fault.to_json
```

````

`````

`````{py:class} FaultBatch(api_util, **kwargs)
:canonical: altdss.Fault.FaultBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PDElement.PDElementBatchMixin`

```{autodoc2-docstring} altdss.Fault.FaultBatch
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Fault.FaultBatch.AccumulatedL

```{autodoc2-docstring} altdss.Fault.FaultBatch.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Fault.FaultBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Fault.FaultBatch.Bus1
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Fault.FaultBatch.Bus2
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.Bus2
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Fault.FaultBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Fault.FaultBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Fault.FaultBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Fault.FaultBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Fault.FaultBatch.Currents

```{autodoc2-docstring} altdss.Fault.FaultBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fault.FaultBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Fault.FaultBatch.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Fault.FaultBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Fault.FaultBatch.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Fault.FaultBatch.EnergyMeter

```{autodoc2-docstring} altdss.Fault.FaultBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Fault.FaultBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Fault.FaultBatch.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Fault.FaultBatch.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.FromTerminal

```{autodoc2-docstring} altdss.Fault.FaultBatch.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Fault.FaultBatch.FullName

```{autodoc2-docstring} altdss.Fault.FaultBatch.FullName
```

````

````{py:attribute} GMatrix
:canonical: altdss.Fault.FaultBatch.GMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.GMatrix
```

````

````{py:method} GUID() -> str
:canonical: altdss.Fault.FaultBatch.GUID

```{autodoc2-docstring} altdss.Fault.FaultBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.Handle

```{autodoc2-docstring} altdss.Fault.FaultBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Fault.FaultBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Fault.FaultBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Fault.FaultBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Fault.FaultBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Fault.FaultBatch.HasVoltControl

```{autodoc2-docstring} altdss.Fault.FaultBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Fault.FaultBatch.IsIsolated

```{autodoc2-docstring} altdss.Fault.FaultBatch.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Fault.FaultBatch.IsShunt

```{autodoc2-docstring} altdss.Fault.FaultBatch.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Fault.FaultBatch.Lambda

```{autodoc2-docstring} altdss.Fault.FaultBatch.Lambda
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fault.FaultBatch.Like

```{autodoc2-docstring} altdss.Fault.FaultBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Fault.FaultBatch.Losses

```{autodoc2-docstring} altdss.Fault.FaultBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Fault.FaultBatch.MaxCurrent

```{autodoc2-docstring} altdss.Fault.FaultBatch.MaxCurrent
```

````

````{py:attribute} MinAmps
:canonical: altdss.Fault.FaultBatch.MinAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.MinAmps
```

````

````{py:property} Name
:canonical: altdss.Fault.FaultBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Fault.FaultBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Fault.FaultBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.NumConductors

```{autodoc2-docstring} altdss.Fault.FaultBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.NumControllers

```{autodoc2-docstring} altdss.Fault.FaultBatch.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.NumCustomers

```{autodoc2-docstring} altdss.Fault.FaultBatch.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.NumPhases

```{autodoc2-docstring} altdss.Fault.FaultBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.NumTerminals

```{autodoc2-docstring} altdss.Fault.FaultBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Fault.FaultBatch.OCPDevice

```{autodoc2-docstring} altdss.Fault.FaultBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Fault.FaultBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Fault.FaultBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Fault.FaultBatch.OCPDeviceType
```

````

````{py:attribute} OnTime
:canonical: altdss.Fault.FaultBatch.OnTime
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.OnTime
```

````

````{py:method} ParentPDElement() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Fault.FaultBatch.ParentPDElement

```{autodoc2-docstring} altdss.Fault.FaultBatch.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Fault.FaultBatch.PhaseLosses

```{autodoc2-docstring} altdss.Fault.FaultBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Fault.FaultBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Fault.FaultBatch.Powers

```{autodoc2-docstring} altdss.Fault.FaultBatch.Powers
```

````

````{py:attribute} R
:canonical: altdss.Fault.FaultBatch.R
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.R
```

````

````{py:attribute} Repair
:canonical: altdss.Fault.FaultBatch.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.Repair
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.SectionID

```{autodoc2-docstring} altdss.Fault.FaultBatch.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Fault.FaultBatch.SeqCurrents

```{autodoc2-docstring} altdss.Fault.FaultBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fault.FaultBatch.SeqPowers

```{autodoc2-docstring} altdss.Fault.FaultBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Fault.FaultBatch.SeqVoltages

```{autodoc2-docstring} altdss.Fault.FaultBatch.SeqVoltages
```

````

````{py:attribute} Temporary
:canonical: altdss.Fault.FaultBatch.Temporary
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.Temporary
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Fault.FaultBatch.TotalCustomers

```{autodoc2-docstring} altdss.Fault.FaultBatch.TotalCustomers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Fault.FaultBatch.TotalMiles

```{autodoc2-docstring} altdss.Fault.FaultBatch.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fault.FaultBatch.TotalPowers

```{autodoc2-docstring} altdss.Fault.FaultBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Fault.FaultBatch.Voltages

```{autodoc2-docstring} altdss.Fault.FaultBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fault.FaultBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Fault.FaultBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.Fault.FaultBatch.__call__

```{autodoc2-docstring} altdss.Fault.FaultBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Fault.FaultBatch.__getitem__

```{autodoc2-docstring} altdss.Fault.FaultBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Fault.FaultBatch.__init__

```{autodoc2-docstring} altdss.Fault.FaultBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Fault.FaultBatch.__iter__

```{autodoc2-docstring} altdss.Fault.FaultBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Fault.FaultBatch.__len__

```{autodoc2-docstring} altdss.Fault.FaultBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Fault.FaultBatch.begin_edit

```{autodoc2-docstring} altdss.Fault.FaultBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Fault.FaultBatch.end_edit

```{autodoc2-docstring} altdss.Fault.FaultBatch.end_edit
```

````

````{py:attribute} pctPerm
:canonical: altdss.Fault.FaultBatch.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.pctPerm
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Fault.FaultBatch.pctStdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatch.pctStdDev
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Fault.FaultBatch.to_json

```{autodoc2-docstring} altdss.Fault.FaultBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Fault.FaultBatch.to_list

```{autodoc2-docstring} altdss.Fault.FaultBatch.to_list
```

````

`````

`````{py:class} FaultBatchProperties()
:canonical: altdss.Fault.FaultBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Fault.FaultBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Fault.FaultBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Fault.FaultBatchProperties.Bus2
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.Bus2
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Fault.FaultBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Fault.FaultBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.Fault.FaultBatchProperties.FaultRate
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.FaultRate
```

````

````{py:attribute} GMatrix
:canonical: altdss.Fault.FaultBatchProperties.GMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.GMatrix
```

````

````{py:attribute} Like
:canonical: altdss.Fault.FaultBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.Like
```

````

````{py:attribute} MinAmps
:canonical: altdss.Fault.FaultBatchProperties.MinAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.MinAmps
```

````

````{py:attribute} NormAmps
:canonical: altdss.Fault.FaultBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.NormAmps
```

````

````{py:attribute} OnTime
:canonical: altdss.Fault.FaultBatchProperties.OnTime
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.OnTime
```

````

````{py:attribute} Phases
:canonical: altdss.Fault.FaultBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.Phases
```

````

````{py:attribute} R
:canonical: altdss.Fault.FaultBatchProperties.R
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.R
```

````

````{py:attribute} Repair
:canonical: altdss.Fault.FaultBatchProperties.Repair
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.Repair
```

````

````{py:attribute} Temporary
:canonical: altdss.Fault.FaultBatchProperties.Temporary
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.Temporary
```

````

````{py:method} __contains__()
:canonical: altdss.Fault.FaultBatchProperties.__contains__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Fault.FaultBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Fault.FaultBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Fault.FaultBatchProperties.__dir__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Fault.FaultBatchProperties.__format__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Fault.FaultBatchProperties.__ge__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Fault.FaultBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Fault.FaultBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Fault.FaultBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Fault.FaultBatchProperties.__gt__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Fault.FaultBatchProperties.__init__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Fault.FaultBatchProperties.__ior__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Fault.FaultBatchProperties.__iter__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Fault.FaultBatchProperties.__le__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Fault.FaultBatchProperties.__len__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Fault.FaultBatchProperties.__lt__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Fault.FaultBatchProperties.__ne__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Fault.FaultBatchProperties.__new__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Fault.FaultBatchProperties.__or__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Fault.FaultBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Fault.FaultBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Fault.FaultBatchProperties.__repr__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Fault.FaultBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Fault.FaultBatchProperties.__ror__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Fault.FaultBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Fault.FaultBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Fault.FaultBatchProperties.__str__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Fault.FaultBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Fault.FaultBatchProperties.clear

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Fault.FaultBatchProperties.copy

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Fault.FaultBatchProperties.get

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Fault.FaultBatchProperties.items

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Fault.FaultBatchProperties.keys

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.keys
```

````

````{py:attribute} pctPerm
:canonical: altdss.Fault.FaultBatchProperties.pctPerm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.pctPerm
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Fault.FaultBatchProperties.pctStdDev
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.pctStdDev
```

````

````{py:method} pop()
:canonical: altdss.Fault.FaultBatchProperties.pop

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Fault.FaultBatchProperties.popitem

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Fault.FaultBatchProperties.setdefault

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Fault.FaultBatchProperties.update

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Fault.FaultBatchProperties.values

```{autodoc2-docstring} altdss.Fault.FaultBatchProperties.values
```

````

`````

`````{py:class} FaultProperties()
:canonical: altdss.Fault.FaultProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Fault.FaultProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.Fault.FaultProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Fault.FaultProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Fault.FaultProperties.Bus2
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.Bus2
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Fault.FaultProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Fault.FaultProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.Fault.FaultProperties.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.FaultRate
```

````

````{py:attribute} GMatrix
:canonical: altdss.Fault.FaultProperties.GMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.GMatrix
```

````

````{py:attribute} Like
:canonical: altdss.Fault.FaultProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.Like
```

````

````{py:attribute} MinAmps
:canonical: altdss.Fault.FaultProperties.MinAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.MinAmps
```

````

````{py:attribute} NormAmps
:canonical: altdss.Fault.FaultProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.NormAmps
```

````

````{py:attribute} OnTime
:canonical: altdss.Fault.FaultProperties.OnTime
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.OnTime
```

````

````{py:attribute} Phases
:canonical: altdss.Fault.FaultProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.Phases
```

````

````{py:attribute} R
:canonical: altdss.Fault.FaultProperties.R
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.R
```

````

````{py:attribute} Repair
:canonical: altdss.Fault.FaultProperties.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.Repair
```

````

````{py:attribute} Temporary
:canonical: altdss.Fault.FaultProperties.Temporary
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.Temporary
```

````

````{py:method} __contains__()
:canonical: altdss.Fault.FaultProperties.__contains__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Fault.FaultProperties.__delattr__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Fault.FaultProperties.__delitem__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Fault.FaultProperties.__dir__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Fault.FaultProperties.__format__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Fault.FaultProperties.__ge__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Fault.FaultProperties.__getattribute__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Fault.FaultProperties.__getitem__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Fault.FaultProperties.__getstate__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Fault.FaultProperties.__gt__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Fault.FaultProperties.__init__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Fault.FaultProperties.__ior__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Fault.FaultProperties.__iter__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Fault.FaultProperties.__le__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Fault.FaultProperties.__len__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Fault.FaultProperties.__lt__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Fault.FaultProperties.__ne__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Fault.FaultProperties.__new__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Fault.FaultProperties.__or__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Fault.FaultProperties.__reduce__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Fault.FaultProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Fault.FaultProperties.__repr__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Fault.FaultProperties.__reversed__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Fault.FaultProperties.__ror__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Fault.FaultProperties.__setitem__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Fault.FaultProperties.__sizeof__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Fault.FaultProperties.__str__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Fault.FaultProperties.__subclasshook__

```{autodoc2-docstring} altdss.Fault.FaultProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Fault.FaultProperties.clear

```{autodoc2-docstring} altdss.Fault.FaultProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Fault.FaultProperties.copy

```{autodoc2-docstring} altdss.Fault.FaultProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Fault.FaultProperties.get

```{autodoc2-docstring} altdss.Fault.FaultProperties.get
```

````

````{py:method} items()
:canonical: altdss.Fault.FaultProperties.items

```{autodoc2-docstring} altdss.Fault.FaultProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Fault.FaultProperties.keys

```{autodoc2-docstring} altdss.Fault.FaultProperties.keys
```

````

````{py:attribute} pctPerm
:canonical: altdss.Fault.FaultProperties.pctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.pctPerm
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Fault.FaultProperties.pctStdDev
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Fault.FaultProperties.pctStdDev
```

````

````{py:method} pop()
:canonical: altdss.Fault.FaultProperties.pop

```{autodoc2-docstring} altdss.Fault.FaultProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Fault.FaultProperties.popitem

```{autodoc2-docstring} altdss.Fault.FaultProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Fault.FaultProperties.setdefault

```{autodoc2-docstring} altdss.Fault.FaultProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Fault.FaultProperties.update

```{autodoc2-docstring} altdss.Fault.FaultProperties.update
```

````

````{py:method} values()
:canonical: altdss.Fault.FaultProperties.values

```{autodoc2-docstring} altdss.Fault.FaultProperties.values
```

````

`````

`````{py:class} IFault(iobj)
:canonical: altdss.Fault.IFault

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Fault.FaultBatch`

```{autodoc2-docstring} altdss.Fault.IFault
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Fault.IFault.AccumulatedL

```{autodoc2-docstring} altdss.Fault.IFault.AccumulatedL
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Fault.IFault.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Fault.IFault.Bus1
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Fault.IFault.Bus2
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.Bus2
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Fault.IFault.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Fault.IFault.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Fault.IFault.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Fault.IFault.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Fault.IFault.Currents

```{autodoc2-docstring} altdss.Fault.IFault.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fault.IFault.CurrentsMagAng

```{autodoc2-docstring} altdss.Fault.IFault.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Fault.IFault.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Fault.IFault.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Fault.IFault.EnergyMeter

```{autodoc2-docstring} altdss.Fault.IFault.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Fault.IFault.EnergyMeterName

```{autodoc2-docstring} altdss.Fault.IFault.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Fault.IFault.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.FromTerminal

```{autodoc2-docstring} altdss.Fault.IFault.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Fault.IFault.FullName

```{autodoc2-docstring} altdss.Fault.IFault.FullName
```

````

````{py:attribute} GMatrix
:canonical: altdss.Fault.IFault.GMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.GMatrix
```

````

````{py:method} GUID() -> str
:canonical: altdss.Fault.IFault.GUID

```{autodoc2-docstring} altdss.Fault.IFault.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.Handle

```{autodoc2-docstring} altdss.Fault.IFault.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Fault.IFault.HasOCPDevice

```{autodoc2-docstring} altdss.Fault.IFault.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Fault.IFault.HasSwitchControl

```{autodoc2-docstring} altdss.Fault.IFault.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Fault.IFault.HasVoltControl

```{autodoc2-docstring} altdss.Fault.IFault.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Fault.IFault.IsIsolated

```{autodoc2-docstring} altdss.Fault.IFault.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Fault.IFault.IsShunt

```{autodoc2-docstring} altdss.Fault.IFault.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Fault.IFault.Lambda

```{autodoc2-docstring} altdss.Fault.IFault.Lambda
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Fault.IFault.Like

```{autodoc2-docstring} altdss.Fault.IFault.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Fault.IFault.Losses

```{autodoc2-docstring} altdss.Fault.IFault.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Fault.IFault.MaxCurrent

```{autodoc2-docstring} altdss.Fault.IFault.MaxCurrent
```

````

````{py:attribute} MinAmps
:canonical: altdss.Fault.IFault.MinAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.MinAmps
```

````

````{py:property} Name
:canonical: altdss.Fault.IFault.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Fault.IFault.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Fault.IFault.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.NumConductors

```{autodoc2-docstring} altdss.Fault.IFault.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.NumControllers

```{autodoc2-docstring} altdss.Fault.IFault.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.NumCustomers

```{autodoc2-docstring} altdss.Fault.IFault.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.NumPhases

```{autodoc2-docstring} altdss.Fault.IFault.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.NumTerminals

```{autodoc2-docstring} altdss.Fault.IFault.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Fault.IFault.OCPDevice

```{autodoc2-docstring} altdss.Fault.IFault.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.OCPDeviceIndex

```{autodoc2-docstring} altdss.Fault.IFault.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Fault.IFault.OCPDeviceType

```{autodoc2-docstring} altdss.Fault.IFault.OCPDeviceType
```

````

````{py:attribute} OnTime
:canonical: altdss.Fault.IFault.OnTime
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.OnTime
```

````

````{py:method} ParentPDElement() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Fault.IFault.ParentPDElement

```{autodoc2-docstring} altdss.Fault.IFault.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Fault.IFault.PhaseLosses

```{autodoc2-docstring} altdss.Fault.IFault.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Fault.IFault.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Fault.IFault.Powers

```{autodoc2-docstring} altdss.Fault.IFault.Powers
```

````

````{py:attribute} R
:canonical: altdss.Fault.IFault.R
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.R
```

````

````{py:attribute} Repair
:canonical: altdss.Fault.IFault.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.Repair
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.SectionID

```{autodoc2-docstring} altdss.Fault.IFault.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Fault.IFault.SeqCurrents

```{autodoc2-docstring} altdss.Fault.IFault.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fault.IFault.SeqPowers

```{autodoc2-docstring} altdss.Fault.IFault.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Fault.IFault.SeqVoltages

```{autodoc2-docstring} altdss.Fault.IFault.SeqVoltages
```

````

````{py:attribute} Temporary
:canonical: altdss.Fault.IFault.Temporary
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.Temporary
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Fault.IFault.TotalCustomers

```{autodoc2-docstring} altdss.Fault.IFault.TotalCustomers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Fault.IFault.TotalMiles

```{autodoc2-docstring} altdss.Fault.IFault.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Fault.IFault.TotalPowers

```{autodoc2-docstring} altdss.Fault.IFault.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Fault.IFault.Voltages

```{autodoc2-docstring} altdss.Fault.IFault.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Fault.IFault.VoltagesMagAng

```{autodoc2-docstring} altdss.Fault.IFault.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.Fault.IFault.__call__

```{autodoc2-docstring} altdss.Fault.IFault.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Fault.IFault.__contains__

```{autodoc2-docstring} altdss.Fault.IFault.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Fault.IFault.__getitem__

```{autodoc2-docstring} altdss.Fault.IFault.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Fault.IFault.__init__

```{autodoc2-docstring} altdss.Fault.IFault.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Fault.IFault.__iter__

```{autodoc2-docstring} altdss.Fault.IFault.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Fault.IFault.__len__

```{autodoc2-docstring} altdss.Fault.IFault.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Fault.IFault.batch

```{autodoc2-docstring} altdss.Fault.IFault.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Fault.FaultBatchProperties]) -> altdss.Fault.FaultBatch
:canonical: altdss.Fault.IFault.batch_new

```{autodoc2-docstring} altdss.Fault.IFault.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Fault.IFault.begin_edit

```{autodoc2-docstring} altdss.Fault.IFault.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Fault.IFault.end_edit

```{autodoc2-docstring} altdss.Fault.IFault.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Fault.IFault.find

```{autodoc2-docstring} altdss.Fault.IFault.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Fault.FaultProperties]) -> altdss.Fault.Fault
:canonical: altdss.Fault.IFault.new

```{autodoc2-docstring} altdss.Fault.IFault.new
```

````

````{py:attribute} pctPerm
:canonical: altdss.Fault.IFault.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.pctPerm
```

````

````{py:attribute} pctStdDev
:canonical: altdss.Fault.IFault.pctStdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.Fault.IFault.pctStdDev
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Fault.IFault.to_json

```{autodoc2-docstring} altdss.Fault.IFault.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Fault.IFault.to_list

```{autodoc2-docstring} altdss.Fault.IFault.to_list
```

````

`````
