# {py:mod}`altdss.EnergyMeterExtras`

```{py:module} altdss.EnergyMeterExtras
```

```{autodoc2-docstring} altdss.EnergyMeterExtras
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EnergyMeterBatchMixin <altdss.EnergyMeterExtras.EnergyMeterBatchMixin>`
  - ```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterBatchMixin
    :summary:
    ```
* - {py:obj}`EnergyMeterObjMixin <altdss.EnergyMeterExtras.EnergyMeterObjMixin>`
  - ```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin
    :summary:
    ```
* - {py:obj}`IEnergyMeterMixin <altdss.EnergyMeterExtras.IEnergyMeterMixin>`
  - ```{autodoc2-docstring} altdss.EnergyMeterExtras.IEnergyMeterMixin
    :summary:
    ```
* - {py:obj}`MeterSection <altdss.EnergyMeterExtras.MeterSection>`
  - ```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection
    :summary:
    ```
* - {py:obj}`MeterSections <altdss.EnergyMeterExtras.MeterSections>`
  - ```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSections
    :summary:
    ```
````

### API

`````{py:class} EnergyMeterBatchMixin
:canonical: altdss.EnergyMeterExtras.EnergyMeterBatchMixin

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterBatchMixin
```

````{py:method} DoReliabilityCalc(assumeRestoration: bool) -> None
:canonical: altdss.EnergyMeterExtras.EnergyMeterBatchMixin.DoReliabilityCalc

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterBatchMixin.DoReliabilityCalc
```

````

````{py:method} NumEndElements() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeterExtras.EnergyMeterBatchMixin.NumEndElements

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterBatchMixin.NumEndElements
```

````

````{py:method} NumSections() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeterExtras.EnergyMeterBatchMixin.NumSections

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterBatchMixin.NumSections
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.EnergyMeterExtras.EnergyMeterBatchMixin.TotalCustomers

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterBatchMixin.TotalCustomers
```

````

`````

`````{py:class} EnergyMeterObjMixin()
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin
```

````{py:property} AllocFactors
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.AllocFactors
:type: altdss.types.Float64Array

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.AllocFactors
```

````

````{py:attribute} Branches
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.Branches
:type: altdss.PDElement.PDElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.Branches
```

````

````{py:property} CalcCurrent
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.CalcCurrent
:type: altdss.types.Float64Array

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.CalcCurrent
```

````

````{py:method} DoReliabilityCalc(assumeRestoration: bool) -> None
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.DoReliabilityCalc

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.DoReliabilityCalc
```

````

````{py:attribute} EndElements
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.EndElements
:type: altdss.CircuitElement.CircuitElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.EndElements
```

````

````{py:method} Loads() -> altdss.Load.LoadBatch
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.Loads

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.Loads
```

````

````{py:method} NumEndElements() -> int
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.NumEndElements

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.NumEndElements
```

````

````{py:method} NumSections() -> int
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.NumSections

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.NumSections
```

````

````{py:method} Section(idx: int) -> altdss.EnergyMeterExtras.MeterSection
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.Section

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.Section
```

````

````{py:method} Sections() -> altdss.EnergyMeterExtras.MeterSections
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.Sections

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.Sections
```

````

````{py:attribute} Sequence
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.Sequence
:type: altdss.CircuitElement.CircuitElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.Sequence
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.TotalCustomers

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.TotalCustomers
```

````

````{py:attribute} ZonePCEs
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.ZonePCEs
:type: altdss.PCElement.PCElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.ZonePCEs
```

````

````{py:method} __init__()
:canonical: altdss.EnergyMeterExtras.EnergyMeterObjMixin.__init__

```{autodoc2-docstring} altdss.EnergyMeterExtras.EnergyMeterObjMixin.__init__
```

````

`````

`````{py:class} IEnergyMeterMixin
:canonical: altdss.EnergyMeterExtras.IEnergyMeterMixin

```{autodoc2-docstring} altdss.EnergyMeterExtras.IEnergyMeterMixin
```

````{py:method} CloseDIFiles()
:canonical: altdss.EnergyMeterExtras.IEnergyMeterMixin.CloseDIFiles

```{autodoc2-docstring} altdss.EnergyMeterExtras.IEnergyMeterMixin.CloseDIFiles
```

````

````{py:method} DIFilesAreOpen() -> bool
:canonical: altdss.EnergyMeterExtras.IEnergyMeterMixin.DIFilesAreOpen

```{autodoc2-docstring} altdss.EnergyMeterExtras.IEnergyMeterMixin.DIFilesAreOpen
```

````

````{py:method} OpenDIFiles()
:canonical: altdss.EnergyMeterExtras.IEnergyMeterMixin.OpenDIFiles

```{autodoc2-docstring} altdss.EnergyMeterExtras.IEnergyMeterMixin.OpenDIFiles
```

````

````{py:method} Totals() -> altdss.types.Float64Array
:canonical: altdss.EnergyMeterExtras.IEnergyMeterMixin.Totals

```{autodoc2-docstring} altdss.EnergyMeterExtras.IEnergyMeterMixin.Totals
```

````

`````

`````{py:class} MeterSection(meter, idx)
:canonical: altdss.EnergyMeterExtras.MeterSection

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection
```

````{py:method} AvgRepairTime() -> float
:canonical: altdss.EnergyMeterExtras.MeterSection.AvgRepairTime

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.AvgRepairTime
```

````

````{py:method} FaultRateXRepairHours() -> float
:canonical: altdss.EnergyMeterExtras.MeterSection.FaultRateXRepairHours

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.FaultRateXRepairHours
```

````

````{py:method} Index() -> int
:canonical: altdss.EnergyMeterExtras.MeterSection.Index

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.Index
```

````

````{py:method} NumBranches() -> int
:canonical: altdss.EnergyMeterExtras.MeterSection.NumBranches

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.NumBranches
```

````

````{py:method} NumCustomers() -> int
:canonical: altdss.EnergyMeterExtras.MeterSection.NumCustomers

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.NumCustomers
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.EnergyMeterExtras.MeterSection.OCPDeviceType

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.OCPDeviceType
```

````

````{py:method} SequenceIndex() -> int
:canonical: altdss.EnergyMeterExtras.MeterSection.SequenceIndex

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.SequenceIndex
```

````

````{py:method} SumBranchFaultRates() -> float
:canonical: altdss.EnergyMeterExtras.MeterSection.SumBranchFaultRates

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.SumBranchFaultRates
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.EnergyMeterExtras.MeterSection.TotalCustomers

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.TotalCustomers
```

````

````{py:method} __init__(meter, idx)
:canonical: altdss.EnergyMeterExtras.MeterSection.__init__

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.__init__
```

````

````{py:method} as_dict()
:canonical: altdss.EnergyMeterExtras.MeterSection.as_dict

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSection.as_dict
```

````

`````

`````{py:class} MeterSections(meter)
:canonical: altdss.EnergyMeterExtras.MeterSections

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSections
```

````{py:method} __call__(idx: int) -> altdss.EnergyMeterExtras.MeterSection
:canonical: altdss.EnergyMeterExtras.MeterSections.__call__

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSections.__call__
```

````

````{py:attribute} __getitem__
:canonical: altdss.EnergyMeterExtras.MeterSections.__getitem__
:value: >
   None

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSections.__getitem__
```

````

````{py:method} __init__(meter)
:canonical: altdss.EnergyMeterExtras.MeterSections.__init__

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSections.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[altdss.EnergyMeterExtras.MeterSection]
:canonical: altdss.EnergyMeterExtras.MeterSections.__iter__

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSections.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.EnergyMeterExtras.MeterSections.__len__

```{autodoc2-docstring} altdss.EnergyMeterExtras.MeterSections.__len__
```

````

`````
