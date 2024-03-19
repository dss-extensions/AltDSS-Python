# {py:mod}`altdss.EnergyMeter`

```{py:module} altdss.EnergyMeter
```

```{autodoc2-docstring} altdss.EnergyMeter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EnergyMeter <altdss.EnergyMeter.EnergyMeter>`
  - ```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter
    :summary:
    ```
* - {py:obj}`EnergyMeterBatch <altdss.EnergyMeter.EnergyMeterBatch>`
  - ```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch
    :summary:
    ```
* - {py:obj}`EnergyMeterBatchProperties <altdss.EnergyMeter.EnergyMeterBatchProperties>`
  - ```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties
    :summary:
    ```
* - {py:obj}`EnergyMeterProperties <altdss.EnergyMeter.EnergyMeterProperties>`
  - ```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties
    :summary:
    ```
* - {py:obj}`IEnergyMeter <altdss.EnergyMeter.IEnergyMeter>`
  - ```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter
    :summary:
    ```
````

### API

`````{py:class} EnergyMeter(api_util, ptr)
:canonical: altdss.EnergyMeter.EnergyMeter

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.EnergyMeterExtras.EnergyMeterObjMixin`, {py:obj}`altdss.PCElement.ElementHasRegistersMixin`

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.EnergyMeterAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeter.Action

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Action
```

````

````{py:property} AllocFactors
:canonical: altdss.EnergyMeter.EnergyMeter.AllocFactors
:type: altdss.types.Float64Array

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.AllocFactors
```

````

````{py:method} Allocate(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeter.Allocate

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Allocate
```

````

````{py:attribute} BaseFreq
:canonical: altdss.EnergyMeter.EnergyMeter.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.BaseFreq
```

````

````{py:attribute} Branches
:canonical: altdss.EnergyMeter.EnergyMeter.Branches
:type: altdss.PDElement.PDElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Branches
```

````

````{py:attribute} CAIDI
:canonical: altdss.EnergyMeter.EnergyMeter.CAIDI
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.CAIDI
```

````

````{py:property} CalcCurrent
:canonical: altdss.EnergyMeter.EnergyMeter.CalcCurrent
:type: altdss.types.Float64Array

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.CalcCurrent
```

````

````{py:method} Clear(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeter.Clear

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Clear
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.EnergyMeter.EnergyMeter.Close

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeter.ComplexSeqCurrents

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeter.ComplexSeqVoltages

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeter.Currents

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Currents
```

````

````{py:attribute} CustInterrupts
:canonical: altdss.EnergyMeter.EnergyMeter.CustInterrupts
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.CustInterrupts
```

````

````{py:attribute} DisplayName
:canonical: altdss.EnergyMeter.EnergyMeter.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.DisplayName
```

````

````{py:method} DoReliabilityCalc(assumeRestoration: bool) -> None
:canonical: altdss.EnergyMeter.EnergyMeter.DoReliabilityCalc

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.DoReliabilityCalc
```

````

````{py:attribute} Element
:canonical: altdss.EnergyMeter.EnergyMeter.Element
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.EnergyMeter.EnergyMeter.Element_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.EnergyMeter.EnergyMeter.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Enabled
```

````

````{py:attribute} EndElements
:canonical: altdss.EnergyMeter.EnergyMeter.EndElements
:type: altdss.CircuitElement.CircuitElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.EndElements
```

````

````{py:method} FullName() -> str
:canonical: altdss.EnergyMeter.EnergyMeter.FullName

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.EnergyMeter.EnergyMeter.GUID

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.EnergyMeter.EnergyMeter.Handle

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.EnergyMeter.EnergyMeter.HasOCPDevice

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.EnergyMeter.EnergyMeter.HasSwitchControl

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.EnergyMeter.EnergyMeter.HasVoltControl

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.HasVoltControl
```

````

````{py:attribute} Int_Duration
:canonical: altdss.EnergyMeter.EnergyMeter.Int_Duration
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Int_Duration
```

````

````{py:attribute} Int_Rate
:canonical: altdss.EnergyMeter.EnergyMeter.Int_Rate
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Int_Rate
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.EnergyMeter.EnergyMeter.IsIsolated

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.EnergyMeter.EnergyMeter.IsOpen

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.EnergyMeter.EnergyMeter.Like

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Like
```

````

````{py:attribute} LineLosses
:canonical: altdss.EnergyMeter.EnergyMeter.LineLosses
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.LineLosses
```

````

````{py:method} Loads() -> altdss.Load.LoadBatch
:canonical: altdss.EnergyMeter.EnergyMeter.Loads

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Loads
```

````

````{py:attribute} LocalOnly
:canonical: altdss.EnergyMeter.EnergyMeter.LocalOnly
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.LocalOnly
```

````

````{py:attribute} Losses
:canonical: altdss.EnergyMeter.EnergyMeter.Losses
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Losses
```

````

````{py:attribute} Mask
:canonical: altdss.EnergyMeter.EnergyMeter.Mask
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Mask
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.EnergyMeter.EnergyMeter.MaxCurrent

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.EnergyMeter.EnergyMeter.Name
:type: str

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeter.NodeOrder

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeter.NodeRef

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.EnergyMeter.EnergyMeter.NumConductors

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.EnergyMeter.EnergyMeter.NumControllers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.NumControllers
```

````

````{py:method} NumEndElements() -> int
:canonical: altdss.EnergyMeter.EnergyMeter.NumEndElements

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.NumEndElements
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.EnergyMeter.EnergyMeter.NumPhases

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.NumPhases
```

````

````{py:method} NumSections() -> int
:canonical: altdss.EnergyMeter.EnergyMeter.NumSections

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.NumSections
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.EnergyMeter.EnergyMeter.NumTerminals

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.EnergyMeter.EnergyMeter.OCPDevice

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.EnergyMeter.EnergyMeter.OCPDeviceIndex

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.EnergyMeter.EnergyMeter.OCPDeviceType

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.EnergyMeter.EnergyMeter.Open

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Open
```

````

````{py:attribute} Option
:canonical: altdss.EnergyMeter.EnergyMeter.Option
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Option
```

````

````{py:attribute} PeakCurrent
:canonical: altdss.EnergyMeter.EnergyMeter.PeakCurrent
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.PeakCurrent
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeter.PhaseLosses

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.PhaseLosses
```

````

````{py:attribute} PhaseVoltageReport
:canonical: altdss.EnergyMeter.EnergyMeter.PhaseVoltageReport
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.PhaseVoltageReport
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeter.Powers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Powers
```

````

````{py:method} Reduce(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeter.Reduce

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Reduce
```

````

````{py:method} RegisterNames() -> typing.List[str]
:canonical: altdss.EnergyMeter.EnergyMeter.RegisterNames

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.RegisterNames
```

````

````{py:method} RegisterValues() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeter.RegisterValues

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.RegisterValues
```

````

````{py:method} RegistersDict() -> typing.Dict[str, float]
:canonical: altdss.EnergyMeter.EnergyMeter.RegistersDict

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.RegistersDict
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeter.Residuals

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Residuals
```

````

````{py:attribute} SAIDI
:canonical: altdss.EnergyMeter.EnergyMeter.SAIDI
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.SAIDI
```

````

````{py:attribute} SAIFI
:canonical: altdss.EnergyMeter.EnergyMeter.SAIFI
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.SAIFI
```

````

````{py:attribute} SAIFIkW
:canonical: altdss.EnergyMeter.EnergyMeter.SAIFIkW
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.SAIFIkW
```

````

````{py:method} Save(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeter.Save

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Save
```

````

````{py:method} Section(idx: int) -> altdss.EnergyMeterExtras.MeterSection
:canonical: altdss.EnergyMeter.EnergyMeter.Section

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Section
```

````

````{py:method} Sections() -> altdss.EnergyMeterExtras.MeterSections
:canonical: altdss.EnergyMeter.EnergyMeter.Sections

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Sections
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeter.SeqCurrents

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.SeqCurrents
```

````

````{py:attribute} SeqLosses
:canonical: altdss.EnergyMeter.EnergyMeter.SeqLosses
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.SeqLosses
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeter.SeqPowers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeter.SeqVoltages

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.SeqVoltages
```

````

````{py:attribute} Sequence
:canonical: altdss.EnergyMeter.EnergyMeter.Sequence
:type: altdss.CircuitElement.CircuitElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Sequence
```

````

````{py:method} TakeSample(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeter.TakeSample

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.TakeSample
```

````

````{py:attribute} Terminal
:canonical: altdss.EnergyMeter.EnergyMeter.Terminal
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Terminal
```

````

````{py:attribute} ThreePhaseLosses
:canonical: altdss.EnergyMeter.EnergyMeter.ThreePhaseLosses
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.ThreePhaseLosses
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.EnergyMeter.EnergyMeter.TotalCustomers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.TotalCustomers
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeter.TotalPowers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.TotalPowers
```

````

````{py:attribute} VBaseLosses
:canonical: altdss.EnergyMeter.EnergyMeter.VBaseLosses
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.VBaseLosses
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeter.Voltages

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeter.VoltagesMagAng

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.VoltagesMagAng
```

````

````{py:attribute} XfmrLosses
:canonical: altdss.EnergyMeter.EnergyMeter.XfmrLosses
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.XfmrLosses
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeter.YPrim

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.YPrim
```

````

````{py:method} ZoneDump(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeter.ZoneDump

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.ZoneDump
```

````

````{py:attribute} ZoneList
:canonical: altdss.EnergyMeter.EnergyMeter.ZoneList
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.ZoneList
```

````

````{py:attribute} ZonePCEs
:canonical: altdss.EnergyMeter.EnergyMeter.ZonePCEs
:type: altdss.PCElement.PCElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.ZonePCEs
```

````

````{py:method} __hash__()
:canonical: altdss.EnergyMeter.EnergyMeter.__hash__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.EnergyMeter.EnergyMeter.__init__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.EnergyMeter.EnergyMeter.__ne__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.EnergyMeter.EnergyMeter.__repr__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.EnergyMeter.EnergyMeter.begin_edit

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.EnergyMeter.EnergyMeterProperties]) -> altdss.EnergyMeter.EnergyMeter
:canonical: altdss.EnergyMeter.EnergyMeter.edit

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.EnergyMeter.EnergyMeter.end_edit

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.end_edit
```

````

````{py:attribute} kVAEmerg
:canonical: altdss.EnergyMeter.EnergyMeter.kVAEmerg
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.kVAEmerg
```

````

````{py:attribute} kVANormal
:canonical: altdss.EnergyMeter.EnergyMeter.kVANormal
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.kVANormal
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.EnergyMeter.EnergyMeter.to_json

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeter.to_json
```

````

`````

`````{py:class} EnergyMeterBatch(api_util, **kwargs)
:canonical: altdss.EnergyMeter.EnergyMeterBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.EnergyMeterExtras.EnergyMeterBatchMixin`

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.EnergyMeterAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Action

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Action
```

````

````{py:method} Allocate(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Allocate

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Allocate
```

````

````{py:attribute} BaseFreq
:canonical: altdss.EnergyMeter.EnergyMeterBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.BaseFreq
```

````

````{py:attribute} CAIDI
:canonical: altdss.EnergyMeter.EnergyMeterBatch.CAIDI
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.CAIDI
```

````

````{py:method} Clear(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Clear

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Clear
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Currents

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.CurrentsMagAng
```

````

````{py:attribute} CustInterrupts
:canonical: altdss.EnergyMeter.EnergyMeterBatch.CustInterrupts
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.CustInterrupts
```

````

````{py:method} DoReliabilityCalc(assumeRestoration: bool) -> None
:canonical: altdss.EnergyMeter.EnergyMeterBatch.DoReliabilityCalc

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.DoReliabilityCalc
```

````

````{py:attribute} Element
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.EnergyMeter.EnergyMeterBatch.FullName

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.EnergyMeter.EnergyMeterBatch.GUID

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Handle

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.HasOCPDevice

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.HasSwitchControl

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.HasVoltControl

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.HasVoltControl
```

````

````{py:attribute} Int_Duration
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Int_Duration
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Int_Duration
```

````

````{py:attribute} Int_Rate
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Int_Rate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Int_Rate
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.IsIsolated

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Like

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Like
```

````

````{py:attribute} LineLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatch.LineLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.LineLosses
```

````

````{py:attribute} LocalOnly
:canonical: altdss.EnergyMeter.EnergyMeterBatch.LocalOnly
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.LocalOnly
```

````

````{py:attribute} Losses
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Losses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Losses
```

````

````{py:attribute} Mask
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Mask
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Mask
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.MaxCurrent

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.NumConductors

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.NumControllers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.NumControllers
```

````

````{py:method} NumEndElements() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.NumEndElements

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.NumEndElements
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.NumPhases

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.NumPhases
```

````

````{py:method} NumSections() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.NumSections

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.NumSections
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.NumTerminals

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.EnergyMeter.EnergyMeterBatch.OCPDevice

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.EnergyMeter.EnergyMeterBatch.OCPDeviceType

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.OCPDeviceType
```

````

````{py:attribute} Option
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Option
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Option
```

````

````{py:attribute} PeakCurrent
:canonical: altdss.EnergyMeter.EnergyMeterBatch.PeakCurrent
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.PeakCurrent
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.PhaseLosses

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.PhaseLosses
```

````

````{py:attribute} PhaseVoltageReport
:canonical: altdss.EnergyMeter.EnergyMeterBatch.PhaseVoltageReport
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.PhaseVoltageReport
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Powers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Powers
```

````

````{py:method} Reduce(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Reduce

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Reduce
```

````

````{py:attribute} SAIDI
:canonical: altdss.EnergyMeter.EnergyMeterBatch.SAIDI
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.SAIDI
```

````

````{py:attribute} SAIFI
:canonical: altdss.EnergyMeter.EnergyMeterBatch.SAIFI
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.SAIFI
```

````

````{py:attribute} SAIFIkW
:canonical: altdss.EnergyMeter.EnergyMeterBatch.SAIFIkW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.SAIFIkW
```

````

````{py:method} Save(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Save

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Save
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.SeqCurrents

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.SeqCurrents
```

````

````{py:attribute} SeqLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatch.SeqLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.SeqLosses
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.SeqPowers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.SeqVoltages

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.SeqVoltages
```

````

````{py:method} TakeSample(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.TakeSample

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.TakeSample
```

````

````{py:attribute} Terminal
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Terminal
```

````

````{py:attribute} ThreePhaseLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatch.ThreePhaseLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.ThreePhaseLosses
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.TotalCustomers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.TotalCustomers
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.TotalPowers

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.TotalPowers
```

````

````{py:attribute} VBaseLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatch.VBaseLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.VBaseLosses
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.EnergyMeterBatch.Voltages

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.EnergyMeterBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.VoltagesMagAng
```

````

````{py:attribute} XfmrLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatch.XfmrLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.XfmrLosses
```

````

````{py:method} ZoneDump(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.ZoneDump

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.ZoneDump
```

````

````{py:attribute} ZoneList
:canonical: altdss.EnergyMeter.EnergyMeterBatch.ZoneList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.ZoneList
```

````

````{py:method} __call__()
:canonical: altdss.EnergyMeter.EnergyMeterBatch.__call__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.EnergyMeter.EnergyMeterBatch.__getitem__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.__init__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.EnergyMeter.EnergyMeterBatch.__iter__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.EnergyMeter.EnergyMeterBatch.__len__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.EnergyMeter.EnergyMeterBatch.batch

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.EnergyMeter.EnergyMeterBatch.begin_edit

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.EnergyMeter.EnergyMeterBatchProperties]) -> altdss.EnergyMeter.EnergyMeterBatch
:canonical: altdss.EnergyMeter.EnergyMeterBatch.edit

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.EnergyMeter.EnergyMeterBatch.end_edit

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.end_edit
```

````

````{py:attribute} kVAEmerg
:canonical: altdss.EnergyMeter.EnergyMeterBatch.kVAEmerg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.kVAEmerg
```

````

````{py:attribute} kVANormal
:canonical: altdss.EnergyMeter.EnergyMeterBatch.kVANormal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.kVANormal
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.EnergyMeter.EnergyMeterBatch.to_json

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.EnergyMeter.EnergyMeterBatch.to_list

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatch.to_list
```

````

`````

`````{py:class} EnergyMeterBatchProperties()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties
```

````{py:attribute} Action
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.EnergyMeterAction]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.BaseFreq
```

````

````{py:attribute} CAIDI
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.CAIDI
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.CAIDI
```

````

````{py:attribute} CustInterrupts
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.CustInterrupts
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.CustInterrupts
```

````

````{py:attribute} Element
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Enabled
```

````

````{py:attribute} Int_Duration
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Int_Duration
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Int_Duration
```

````

````{py:attribute} Int_Rate
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Int_Rate
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Int_Rate
```

````

````{py:attribute} Like
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Like
```

````

````{py:attribute} LineLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.LineLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.LineLosses
```

````

````{py:attribute} LocalOnly
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.LocalOnly
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.LocalOnly
```

````

````{py:attribute} Losses
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Losses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Losses
```

````

````{py:attribute} Mask
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Mask
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Mask
```

````

````{py:attribute} Option
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Option
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Option
```

````

````{py:attribute} PeakCurrent
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.PeakCurrent
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.PeakCurrent
```

````

````{py:attribute} PhaseVoltageReport
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.PhaseVoltageReport
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.PhaseVoltageReport
```

````

````{py:attribute} SAIDI
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.SAIDI
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.SAIDI
```

````

````{py:attribute} SAIFI
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.SAIFI
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.SAIFI
```

````

````{py:attribute} SAIFIkW
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.SAIFIkW
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.SAIFIkW
```

````

````{py:attribute} SeqLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.SeqLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.SeqLosses
```

````

````{py:attribute} Terminal
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.Terminal
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.Terminal
```

````

````{py:attribute} ThreePhaseLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.ThreePhaseLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.ThreePhaseLosses
```

````

````{py:attribute} VBaseLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.VBaseLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.VBaseLosses
```

````

````{py:attribute} XfmrLosses
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.XfmrLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.XfmrLosses
```

````

````{py:attribute} ZoneList
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.ZoneList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.ZoneList
```

````

````{py:method} __contains__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__contains__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__delattr__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__delitem__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__dir__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__format__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__ge__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__getitem__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__getstate__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__gt__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__init__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__ior__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__iter__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__le__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__len__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__lt__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__ne__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__new__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__or__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__reduce__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__repr__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__reversed__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__ror__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__setitem__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__str__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.clear

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.copy

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.get

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.items

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.items
```

````

````{py:attribute} kVAEmerg
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.kVAEmerg
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.kVAEmerg
```

````

````{py:attribute} kVANormal
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.kVANormal
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.kVANormal
```

````

````{py:method} keys()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.keys

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.pop

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.popitem

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.setdefault

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.update

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.EnergyMeter.EnergyMeterBatchProperties.values

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterBatchProperties.values
```

````

`````

`````{py:class} EnergyMeterProperties()
:canonical: altdss.EnergyMeter.EnergyMeterProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties
```

````{py:attribute} Action
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.EnergyMeterAction]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Action
```

````

````{py:attribute} BaseFreq
:canonical: altdss.EnergyMeter.EnergyMeterProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.BaseFreq
```

````

````{py:attribute} CAIDI
:canonical: altdss.EnergyMeter.EnergyMeterProperties.CAIDI
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.CAIDI
```

````

````{py:attribute} CustInterrupts
:canonical: altdss.EnergyMeter.EnergyMeterProperties.CustInterrupts
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.CustInterrupts
```

````

````{py:attribute} Element
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Enabled
```

````

````{py:attribute} Int_Duration
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Int_Duration
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Int_Duration
```

````

````{py:attribute} Int_Rate
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Int_Rate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Int_Rate
```

````

````{py:attribute} Like
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Like
```

````

````{py:attribute} LineLosses
:canonical: altdss.EnergyMeter.EnergyMeterProperties.LineLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.LineLosses
```

````

````{py:attribute} LocalOnly
:canonical: altdss.EnergyMeter.EnergyMeterProperties.LocalOnly
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.LocalOnly
```

````

````{py:attribute} Losses
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Losses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Losses
```

````

````{py:attribute} Mask
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Mask
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Mask
```

````

````{py:attribute} Option
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Option
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Option
```

````

````{py:attribute} PeakCurrent
:canonical: altdss.EnergyMeter.EnergyMeterProperties.PeakCurrent
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.PeakCurrent
```

````

````{py:attribute} PhaseVoltageReport
:canonical: altdss.EnergyMeter.EnergyMeterProperties.PhaseVoltageReport
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.PhaseVoltageReport
```

````

````{py:attribute} SAIDI
:canonical: altdss.EnergyMeter.EnergyMeterProperties.SAIDI
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.SAIDI
```

````

````{py:attribute} SAIFI
:canonical: altdss.EnergyMeter.EnergyMeterProperties.SAIFI
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.SAIFI
```

````

````{py:attribute} SAIFIkW
:canonical: altdss.EnergyMeter.EnergyMeterProperties.SAIFIkW
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.SAIFIkW
```

````

````{py:attribute} SeqLosses
:canonical: altdss.EnergyMeter.EnergyMeterProperties.SeqLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.SeqLosses
```

````

````{py:attribute} Terminal
:canonical: altdss.EnergyMeter.EnergyMeterProperties.Terminal
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.Terminal
```

````

````{py:attribute} ThreePhaseLosses
:canonical: altdss.EnergyMeter.EnergyMeterProperties.ThreePhaseLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.ThreePhaseLosses
```

````

````{py:attribute} VBaseLosses
:canonical: altdss.EnergyMeter.EnergyMeterProperties.VBaseLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.VBaseLosses
```

````

````{py:attribute} XfmrLosses
:canonical: altdss.EnergyMeter.EnergyMeterProperties.XfmrLosses
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.XfmrLosses
```

````

````{py:attribute} ZoneList
:canonical: altdss.EnergyMeter.EnergyMeterProperties.ZoneList
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.ZoneList
```

````

````{py:method} __contains__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__contains__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__delattr__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__delitem__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__dir__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__format__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__ge__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__getattribute__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__getitem__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__getstate__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__gt__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__init__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__ior__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__iter__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__le__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__len__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__lt__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__ne__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__new__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__or__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__reduce__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__reduce_ex__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__repr__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__reversed__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__ror__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__setitem__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__sizeof__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__str__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.__subclasshook__

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.clear

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.copy

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.copy
```

````

````{py:method} get()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.get

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.get
```

````

````{py:method} items()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.items

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.items
```

````

````{py:attribute} kVAEmerg
:canonical: altdss.EnergyMeter.EnergyMeterProperties.kVAEmerg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.kVAEmerg
```

````

````{py:attribute} kVANormal
:canonical: altdss.EnergyMeter.EnergyMeterProperties.kVANormal
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.kVANormal
```

````

````{py:method} keys()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.keys

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.pop

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.popitem

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.setdefault

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.update

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.update
```

````

````{py:method} values()
:canonical: altdss.EnergyMeter.EnergyMeterProperties.values

```{autodoc2-docstring} altdss.EnergyMeter.EnergyMeterProperties.values
```

````

`````

`````{py:class} IEnergyMeter(iobj)
:canonical: altdss.EnergyMeter.IEnergyMeter

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.EnergyMeter.EnergyMeterBatch`, {py:obj}`altdss.EnergyMeterExtras.IEnergyMeterMixin`

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.EnergyMeterAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.IEnergyMeter.Action

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Action
```

````

````{py:method} Allocate(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.IEnergyMeter.Allocate

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Allocate
```

````

````{py:attribute} BaseFreq
:canonical: altdss.EnergyMeter.IEnergyMeter.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.BaseFreq
```

````

````{py:attribute} CAIDI
:canonical: altdss.EnergyMeter.IEnergyMeter.CAIDI
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.CAIDI
```

````

````{py:method} Clear(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.IEnergyMeter.Clear

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Clear
```

````

````{py:method} CloseDIFiles()
:canonical: altdss.EnergyMeter.IEnergyMeter.CloseDIFiles

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.CloseDIFiles
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.IEnergyMeter.ComplexSeqCurrents

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.IEnergyMeter.ComplexSeqVoltages

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.IEnergyMeter.Currents

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.IEnergyMeter.CurrentsMagAng

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.CurrentsMagAng
```

````

````{py:attribute} CustInterrupts
:canonical: altdss.EnergyMeter.IEnergyMeter.CustInterrupts
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.CustInterrupts
```

````

````{py:method} DIFilesAreOpen() -> bool
:canonical: altdss.EnergyMeter.IEnergyMeter.DIFilesAreOpen

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.DIFilesAreOpen
```

````

````{py:method} DoReliabilityCalc(assumeRestoration: bool) -> None
:canonical: altdss.EnergyMeter.IEnergyMeter.DoReliabilityCalc

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.DoReliabilityCalc
```

````

````{py:attribute} Element
:canonical: altdss.EnergyMeter.IEnergyMeter.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.EnergyMeter.IEnergyMeter.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.EnergyMeter.IEnergyMeter.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Enabled
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.EnergyMeter.IEnergyMeter.FullName

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.EnergyMeter.IEnergyMeter.GUID

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.IEnergyMeter.Handle

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.EnergyMeter.IEnergyMeter.HasOCPDevice

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.EnergyMeter.IEnergyMeter.HasSwitchControl

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.EnergyMeter.IEnergyMeter.HasVoltControl

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.HasVoltControl
```

````

````{py:attribute} Int_Duration
:canonical: altdss.EnergyMeter.IEnergyMeter.Int_Duration
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Int_Duration
```

````

````{py:attribute} Int_Rate
:canonical: altdss.EnergyMeter.IEnergyMeter.Int_Rate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Int_Rate
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.EnergyMeter.IEnergyMeter.IsIsolated

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.IEnergyMeter.Like

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Like
```

````

````{py:attribute} LineLosses
:canonical: altdss.EnergyMeter.IEnergyMeter.LineLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.LineLosses
```

````

````{py:attribute} LocalOnly
:canonical: altdss.EnergyMeter.IEnergyMeter.LocalOnly
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.LocalOnly
```

````

````{py:attribute} Losses
:canonical: altdss.EnergyMeter.IEnergyMeter.Losses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Losses
```

````

````{py:attribute} Mask
:canonical: altdss.EnergyMeter.IEnergyMeter.Mask
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Mask
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.IEnergyMeter.MaxCurrent

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.EnergyMeter.IEnergyMeter.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.IEnergyMeter.NumConductors

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.IEnergyMeter.NumControllers

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.NumControllers
```

````

````{py:method} NumEndElements() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.IEnergyMeter.NumEndElements

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.NumEndElements
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.IEnergyMeter.NumPhases

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.NumPhases
```

````

````{py:method} NumSections() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.IEnergyMeter.NumSections

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.NumSections
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.IEnergyMeter.NumTerminals

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.EnergyMeter.IEnergyMeter.OCPDevice

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.IEnergyMeter.OCPDeviceIndex

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.EnergyMeter.IEnergyMeter.OCPDeviceType

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.OCPDeviceType
```

````

````{py:method} OpenDIFiles()
:canonical: altdss.EnergyMeter.IEnergyMeter.OpenDIFiles

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.OpenDIFiles
```

````

````{py:attribute} Option
:canonical: altdss.EnergyMeter.IEnergyMeter.Option
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Option
```

````

````{py:attribute} PeakCurrent
:canonical: altdss.EnergyMeter.IEnergyMeter.PeakCurrent
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.PeakCurrent
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.IEnergyMeter.PhaseLosses

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.PhaseLosses
```

````

````{py:attribute} PhaseVoltageReport
:canonical: altdss.EnergyMeter.IEnergyMeter.PhaseVoltageReport
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.PhaseVoltageReport
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.IEnergyMeter.Powers

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Powers
```

````

````{py:method} Reduce(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.IEnergyMeter.Reduce

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Reduce
```

````

````{py:attribute} SAIDI
:canonical: altdss.EnergyMeter.IEnergyMeter.SAIDI
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.SAIDI
```

````

````{py:attribute} SAIFI
:canonical: altdss.EnergyMeter.IEnergyMeter.SAIFI
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.SAIFI
```

````

````{py:attribute} SAIFIkW
:canonical: altdss.EnergyMeter.IEnergyMeter.SAIFIkW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.SAIFIkW
```

````

````{py:method} Save(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.IEnergyMeter.Save

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Save
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.IEnergyMeter.SeqCurrents

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.SeqCurrents
```

````

````{py:attribute} SeqLosses
:canonical: altdss.EnergyMeter.IEnergyMeter.SeqLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.SeqLosses
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.IEnergyMeter.SeqPowers

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.IEnergyMeter.SeqVoltages

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.SeqVoltages
```

````

````{py:method} TakeSample(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.IEnergyMeter.TakeSample

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.TakeSample
```

````

````{py:attribute} Terminal
:canonical: altdss.EnergyMeter.IEnergyMeter.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Terminal
```

````

````{py:attribute} ThreePhaseLosses
:canonical: altdss.EnergyMeter.IEnergyMeter.ThreePhaseLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.ThreePhaseLosses
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeter.IEnergyMeter.TotalCustomers

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.TotalCustomers
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.IEnergyMeter.TotalPowers

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.TotalPowers
```

````

````{py:method} Totals() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.IEnergyMeter.Totals

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Totals
```

````

````{py:attribute} VBaseLosses
:canonical: altdss.EnergyMeter.IEnergyMeter.VBaseLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.VBaseLosses
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.EnergyMeter.IEnergyMeter.Voltages

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeter.IEnergyMeter.VoltagesMagAng

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.VoltagesMagAng
```

````

````{py:attribute} XfmrLosses
:canonical: altdss.EnergyMeter.IEnergyMeter.XfmrLosses
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.XfmrLosses
```

````

````{py:method} ZoneDump(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.EnergyMeter.IEnergyMeter.ZoneDump

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.ZoneDump
```

````

````{py:attribute} ZoneList
:canonical: altdss.EnergyMeter.IEnergyMeter.ZoneList
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.ZoneList
```

````

````{py:method} __call__()
:canonical: altdss.EnergyMeter.IEnergyMeter.__call__

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.EnergyMeter.IEnergyMeter.__contains__

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.EnergyMeter.IEnergyMeter.__getitem__

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.EnergyMeter.IEnergyMeter.__init__

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.EnergyMeter.IEnergyMeter.__iter__

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.EnergyMeter.IEnergyMeter.__len__

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.EnergyMeter.IEnergyMeter.batch

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.EnergyMeter.EnergyMeterBatchProperties]) -> altdss.EnergyMeter.EnergyMeterBatch
:canonical: altdss.EnergyMeter.IEnergyMeter.batch_new

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.EnergyMeter.IEnergyMeter.begin_edit

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.EnergyMeter.EnergyMeterBatchProperties]) -> altdss.EnergyMeter.EnergyMeterBatch
:canonical: altdss.EnergyMeter.IEnergyMeter.edit

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.EnergyMeter.IEnergyMeter.end_edit

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.EnergyMeter.IEnergyMeter.find

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.find
```

````

````{py:attribute} kVAEmerg
:canonical: altdss.EnergyMeter.IEnergyMeter.kVAEmerg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.kVAEmerg
```

````

````{py:attribute} kVANormal
:canonical: altdss.EnergyMeter.IEnergyMeter.kVANormal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.kVANormal
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.EnergyMeter.EnergyMeterProperties]) -> altdss.EnergyMeter.EnergyMeter
:canonical: altdss.EnergyMeter.IEnergyMeter.new

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.EnergyMeter.IEnergyMeter.to_json

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.to_json
```

````

````{py:method} to_list()
:canonical: altdss.EnergyMeter.IEnergyMeter.to_list

```{autodoc2-docstring} altdss.EnergyMeter.IEnergyMeter.to_list
```

````

`````
