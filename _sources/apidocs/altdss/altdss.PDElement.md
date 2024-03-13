# {py:mod}`altdss.PDElement`

```{py:module} altdss.PDElement
```

```{autodoc2-docstring} altdss.PDElement
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PDElementBatch <altdss.PDElement.PDElementBatch>`
  - ```{autodoc2-docstring} altdss.PDElement.PDElementBatch
    :summary:
    ```
* - {py:obj}`PDElementBatchMixin <altdss.PDElement.PDElementBatchMixin>`
  - ```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin
    :summary:
    ```
* - {py:obj}`PDElementMixin <altdss.PDElement.PDElementMixin>`
  - ```{autodoc2-docstring} altdss.PDElement.PDElementMixin
    :summary:
    ```
````

### API

`````{py:class} PDElementBatch(func, parent, sync_cls_idx=ExtraClassIDs.PDElements, copy_safe=False)
:canonical: altdss.PDElement.PDElementBatch

Bases: {py:obj}`altdss.CircuitElement.CircuitElementBatch`, {py:obj}`altdss.PDElement.PDElementBatchMixin`

```{autodoc2-docstring} altdss.PDElement.PDElementBatch
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.AccumulatedL

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.AccumulatedL
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.PDElement.PDElementBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.PDElement.PDElementBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.PDElement.PDElementBatch.Currents

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.CurrentsMagAng
```

````

````{py:method} EnergyMeter() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.PDElement.PDElementBatch.EnergyMeter

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.PDElement.PDElementBatch.EnergyMeterName

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.EnergyMeterName
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.FromTerminal

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.PDElement.PDElementBatch.FullName

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.PDElement.PDElementBatch.GUID

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.Handle

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.PDElement.PDElementBatch.HasOCPDevice

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.PDElement.PDElementBatch.HasSwitchControl

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.PDElement.PDElementBatch.HasVoltControl

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.PDElement.PDElementBatch.IsIsolated

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.PDElement.PDElementBatch.IsShunt

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.Lambda

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.Lambda
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.PDElement.PDElementBatch.Losses

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.MaxCurrent

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.PDElement.PDElementBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.NumConductors

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.NumControllers

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.NumCustomers

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.NumPhases

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.NumTerminals

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.PDElement.PDElementBatch.OCPDevice

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.PDElement.PDElementBatch.OCPDeviceType

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.PDElement.PDElementBatch.ParentPDElement

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.PDElement.PDElementBatch.PhaseLosses

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.PDElement.PDElementBatch.Powers

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.Powers
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.SectionID

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.SeqCurrents

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.PDElement.PDElementBatch.SeqPowers

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.SeqVoltages

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.SeqVoltages
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatch.TotalCustomers

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.TotalCustomers
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.TotalKilometers

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.TotalMiles

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.PDElement.PDElementBatch.TotalPowers

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.PDElement.PDElementBatch.Voltages

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.PDElement.PDElementBatch.__call__

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.__call__
```

````

````{py:method} __getitem__(idx: int) -> altdss.DSSObj.DSSObj
:canonical: altdss.PDElement.PDElementBatch.__getitem__

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.__getitem__
```

````

````{py:method} __init__(func, parent, sync_cls_idx=ExtraClassIDs.PDElements, copy_safe=False)
:canonical: altdss.PDElement.PDElementBatch.__init__

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[altdss.DSSObj.DSSObj]
:canonical: altdss.PDElement.PDElementBatch.__iter__

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.PDElement.PDElementBatch.__len__

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.__len__
```

````

````{py:method} pctEmergency(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.pctEmergency

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.pctEmergency
```

````

````{py:method} pctNormal(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatch.pctNormal

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.pctNormal
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.PDElement.PDElementBatch.to_json

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.PDElement.PDElementBatch.to_list

```{autodoc2-docstring} altdss.PDElement.PDElementBatch.to_list
```

````

`````

`````{py:class} PDElementBatchMixin
:canonical: altdss.PDElement.PDElementBatchMixin

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatchMixin.AccumulatedL

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.AccumulatedL
```

````

````{py:method} EnergyMeter() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.PDElement.PDElementBatchMixin.EnergyMeter

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.PDElement.PDElementBatchMixin.EnergyMeterName

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.EnergyMeterName
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatchMixin.FromTerminal

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.FromTerminal
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.PDElement.PDElementBatchMixin.IsShunt

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatchMixin.Lambda

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.Lambda
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatchMixin.NumCustomers

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.NumCustomers
```

````

````{py:method} ParentPDElement() -> typing.List[typing.Optional[altdss.DSSObj.DSSObj]]
:canonical: altdss.PDElement.PDElementBatchMixin.ParentPDElement

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.ParentPDElement
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatchMixin.SectionID

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.SectionID
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.PDElement.PDElementBatchMixin.TotalCustomers

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.TotalCustomers
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatchMixin.TotalKilometers

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatchMixin.TotalMiles

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.TotalMiles
```

````

````{py:method} pctEmergency(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatchMixin.pctEmergency

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.pctEmergency
```

````

````{py:method} pctNormal(allNodes=False) -> altdss.types.Float64Array
:canonical: altdss.PDElement.PDElementBatchMixin.pctNormal

```{autodoc2-docstring} altdss.PDElement.PDElementBatchMixin.pctNormal
```

````

`````

`````{py:class} PDElementMixin
:canonical: altdss.PDElement.PDElementMixin

```{autodoc2-docstring} altdss.PDElement.PDElementMixin
```

````{py:method} AccumulatedL() -> float
:canonical: altdss.PDElement.PDElementMixin.AccumulatedL

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.AccumulatedL
```

````

````{py:method} EnergyMeter() -> typing.Optional[altdss.DSSObj.DSSObj]
:canonical: altdss.PDElement.PDElementMixin.EnergyMeter

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.PDElement.PDElementMixin.EnergyMeterName

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.EnergyMeterName
```

````

````{py:method} FromTerminal() -> int
:canonical: altdss.PDElement.PDElementMixin.FromTerminal

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.FromTerminal
```

````

````{py:method} IsShunt() -> bool
:canonical: altdss.PDElement.PDElementMixin.IsShunt

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.IsShunt
```

````

````{py:method} Lambda() -> float
:canonical: altdss.PDElement.PDElementMixin.Lambda

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.Lambda
```

````

````{py:method} NumCustomers() -> int
:canonical: altdss.PDElement.PDElementMixin.NumCustomers

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.NumCustomers
```

````

````{py:method} ParentPDElement() -> typing.Optional[altdss.DSSObj.DSSObj]
:canonical: altdss.PDElement.PDElementMixin.ParentPDElement

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.ParentPDElement
```

````

````{py:method} SectionID() -> int
:canonical: altdss.PDElement.PDElementMixin.SectionID

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.SectionID
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.PDElement.PDElementMixin.TotalCustomers

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.TotalCustomers
```

````

````{py:method} TotalKilometers() -> float
:canonical: altdss.PDElement.PDElementMixin.TotalKilometers

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.TotalKilometers
```

````

````{py:method} TotalMiles() -> float
:canonical: altdss.PDElement.PDElementMixin.TotalMiles

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.TotalMiles
```

````

````{py:method} pctEmergency(allNodes=False) -> float
:canonical: altdss.PDElement.PDElementMixin.pctEmergency

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.pctEmergency
```

````

````{py:method} pctNormal(allNodes=False) -> float
:canonical: altdss.PDElement.PDElementMixin.pctNormal

```{autodoc2-docstring} altdss.PDElement.PDElementMixin.pctNormal
```

````

`````
