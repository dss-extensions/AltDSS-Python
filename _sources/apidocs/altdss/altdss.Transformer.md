# {py:mod}`altdss.Transformer`

```{py:module} altdss.Transformer
```

```{autodoc2-docstring} altdss.Transformer
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ITransformer <altdss.Transformer.ITransformer>`
  - ```{autodoc2-docstring} altdss.Transformer.ITransformer
    :summary:
    ```
* - {py:obj}`Transformer <altdss.Transformer.Transformer>`
  - ```{autodoc2-docstring} altdss.Transformer.Transformer
    :summary:
    ```
* - {py:obj}`TransformerBatch <altdss.Transformer.TransformerBatch>`
  - ```{autodoc2-docstring} altdss.Transformer.TransformerBatch
    :summary:
    ```
* - {py:obj}`TransformerBatchProperties <altdss.Transformer.TransformerBatchProperties>`
  - ```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties
    :summary:
    ```
* - {py:obj}`TransformerProperties <altdss.Transformer.TransformerProperties>`
  - ```{autodoc2-docstring} altdss.Transformer.TransformerProperties
    :summary:
    ```
````

### API

`````{py:class} ITransformer(iobj)
:canonical: altdss.Transformer.ITransformer

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Transformer.TransformerBatch`

```{autodoc2-docstring} altdss.Transformer.ITransformer
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Transformer.ITransformer.AccumulatedL

```{autodoc2-docstring} altdss.Transformer.ITransformer.AccumulatedL
```

````

````{py:attribute} Bank
:canonical: altdss.Transformer.ITransformer.Bank
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Transformer.ITransformer.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.Transformer.ITransformer.Buses
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Buses
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.ITransformer.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Transformer.ITransformer.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.ITransformer.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Transformer.ITransformer.ComplexSeqVoltages
```

````

````{py:attribute} Conns
:canonical: altdss.Transformer.ITransformer.Conns
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Conns
```

````

````{py:attribute} Conns_str
:canonical: altdss.Transformer.ITransformer.Conns_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Conns_str
```

````

````{py:attribute} Core
:canonical: altdss.Transformer.ITransformer.Core
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Core
```

````

````{py:attribute} Core_str
:canonical: altdss.Transformer.ITransformer.Core_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Core_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.ITransformer.Currents

```{autodoc2-docstring} altdss.Transformer.ITransformer.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Transformer.ITransformer.CurrentsMagAng

```{autodoc2-docstring} altdss.Transformer.ITransformer.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Transformer.ITransformer.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.Transformer.ITransformer.EmergHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.Transformer.ITransformer.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Transformer.ITransformer.EnergyMeter

```{autodoc2-docstring} altdss.Transformer.ITransformer.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Transformer.ITransformer.EnergyMeterName

```{autodoc2-docstring} altdss.Transformer.ITransformer.EnergyMeterName
```

````

````{py:attribute} FLRise
:canonical: altdss.Transformer.ITransformer.FLRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.Transformer.ITransformer.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.FromTerminal

```{autodoc2-docstring} altdss.Transformer.ITransformer.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Transformer.ITransformer.FullName

```{autodoc2-docstring} altdss.Transformer.ITransformer.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Transformer.ITransformer.GUID

```{autodoc2-docstring} altdss.Transformer.ITransformer.GUID
```

````

````{py:attribute} HSRise
:canonical: altdss.Transformer.ITransformer.HSRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.HSRise
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.Handle

```{autodoc2-docstring} altdss.Transformer.ITransformer.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Transformer.ITransformer.HasOCPDevice

```{autodoc2-docstring} altdss.Transformer.ITransformer.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Transformer.ITransformer.HasSwitchControl

```{autodoc2-docstring} altdss.Transformer.ITransformer.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Transformer.ITransformer.HasVoltControl

```{autodoc2-docstring} altdss.Transformer.ITransformer.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Transformer.ITransformer.IsIsolated

```{autodoc2-docstring} altdss.Transformer.ITransformer.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Transformer.ITransformer.IsShunt

```{autodoc2-docstring} altdss.Transformer.ITransformer.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Transformer.ITransformer.Lambda

```{autodoc2-docstring} altdss.Transformer.ITransformer.Lambda
```

````

````{py:attribute} LeadLag
:canonical: altdss.Transformer.ITransformer.LeadLag
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.LeadLag
```

````

````{py:attribute} LeadLag_str
:canonical: altdss.Transformer.ITransformer.LeadLag_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.LeadLag_str
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Transformer.ITransformer.Like

```{autodoc2-docstring} altdss.Transformer.ITransformer.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.ITransformer.Losses

```{autodoc2-docstring} altdss.Transformer.ITransformer.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Transformer.ITransformer.MaxCurrent

```{autodoc2-docstring} altdss.Transformer.ITransformer.MaxCurrent
```

````

````{py:attribute} MaxTap
:canonical: altdss.Transformer.ITransformer.MaxTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.Transformer.ITransformer.MinTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.MinTap
```

````

````{py:property} Name
:canonical: altdss.Transformer.ITransformer.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Transformer.ITransformer.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Transformer.ITransformer.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.Transformer.ITransformer.NormHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.NormHkVA
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.NumConductors

```{autodoc2-docstring} altdss.Transformer.ITransformer.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.NumControllers

```{autodoc2-docstring} altdss.Transformer.ITransformer.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.NumCustomers

```{autodoc2-docstring} altdss.Transformer.ITransformer.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.NumPhases

```{autodoc2-docstring} altdss.Transformer.ITransformer.NumPhases
```

````

````{py:attribute} NumTaps
:canonical: altdss.Transformer.ITransformer.NumTaps
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.NumTaps
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.NumTerminals

```{autodoc2-docstring} altdss.Transformer.ITransformer.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Transformer.ITransformer.OCPDevice

```{autodoc2-docstring} altdss.Transformer.ITransformer.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.OCPDeviceIndex

```{autodoc2-docstring} altdss.Transformer.ITransformer.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Transformer.ITransformer.OCPDeviceType

```{autodoc2-docstring} altdss.Transformer.ITransformer.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Transformer.ITransformer.ParentPDElement

```{autodoc2-docstring} altdss.Transformer.ITransformer.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.ITransformer.PhaseLosses

```{autodoc2-docstring} altdss.Transformer.ITransformer.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Transformer.ITransformer.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.ITransformer.Powers

```{autodoc2-docstring} altdss.Transformer.ITransformer.Powers
```

````

````{py:attribute} RDCOhms
:canonical: altdss.Transformer.ITransformer.RDCOhms
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.Transformer.ITransformer.RNeut
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.Transformer.ITransformer.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Transformer.ITransformer.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Repair
```

````

````{py:attribute} Seasons
:canonical: altdss.Transformer.ITransformer.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Seasons
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.SectionID

```{autodoc2-docstring} altdss.Transformer.ITransformer.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Transformer.ITransformer.SeqCurrents

```{autodoc2-docstring} altdss.Transformer.ITransformer.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.ITransformer.SeqPowers

```{autodoc2-docstring} altdss.Transformer.ITransformer.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Transformer.ITransformer.SeqVoltages

```{autodoc2-docstring} altdss.Transformer.ITransformer.SeqVoltages
```

````

````{py:attribute} Sub
:canonical: altdss.Transformer.ITransformer.Sub
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.Transformer.ITransformer.SubName
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.Transformer.ITransformer.Taps
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.Transformer.ITransformer.Thermal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Thermal
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Transformer.ITransformer.TotalCustomers

```{autodoc2-docstring} altdss.Transformer.ITransformer.TotalCustomers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Transformer.ITransformer.TotalMiles

```{autodoc2-docstring} altdss.Transformer.ITransformer.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.ITransformer.TotalPowers

```{autodoc2-docstring} altdss.Transformer.ITransformer.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.ITransformer.Voltages

```{autodoc2-docstring} altdss.Transformer.ITransformer.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Transformer.ITransformer.VoltagesMagAng

```{autodoc2-docstring} altdss.Transformer.ITransformer.VoltagesMagAng
```

````

````{py:attribute} Windings
:canonical: altdss.Transformer.ITransformer.Windings
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.Windings
```

````

````{py:attribute} X12
:canonical: altdss.Transformer.ITransformer.X12
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.X12
```

````

````{py:attribute} X13
:canonical: altdss.Transformer.ITransformer.X13
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.X13
```

````

````{py:attribute} X23
:canonical: altdss.Transformer.ITransformer.X23
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.X23
```

````

````{py:attribute} XHL
:canonical: altdss.Transformer.ITransformer.XHL
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.Transformer.ITransformer.XHT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.Transformer.ITransformer.XLT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.Transformer.ITransformer.XNeut
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.XNeut
```

````

````{py:attribute} XRConst
:canonical: altdss.Transformer.ITransformer.XRConst
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.Transformer.ITransformer.XSCArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.XSCArray
```

````

````{py:attribute} XfmrCode
:canonical: altdss.Transformer.ITransformer.XfmrCode
:type: typing.List[altdss.XfmrCode.XfmrCode]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.XfmrCode
```

````

````{py:attribute} XfmrCode_str
:canonical: altdss.Transformer.ITransformer.XfmrCode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.XfmrCode_str
```

````

````{py:method} __call__()
:canonical: altdss.Transformer.ITransformer.__call__

```{autodoc2-docstring} altdss.Transformer.ITransformer.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Transformer.ITransformer.__contains__

```{autodoc2-docstring} altdss.Transformer.ITransformer.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Transformer.ITransformer.__getitem__

```{autodoc2-docstring} altdss.Transformer.ITransformer.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Transformer.ITransformer.__init__

```{autodoc2-docstring} altdss.Transformer.ITransformer.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Transformer.ITransformer.__iter__

```{autodoc2-docstring} altdss.Transformer.ITransformer.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Transformer.ITransformer.__len__

```{autodoc2-docstring} altdss.Transformer.ITransformer.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Transformer.ITransformer.batch

```{autodoc2-docstring} altdss.Transformer.ITransformer.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Transformer.TransformerBatchProperties]) -> altdss.Transformer.TransformerBatch
:canonical: altdss.Transformer.ITransformer.batch_new

```{autodoc2-docstring} altdss.Transformer.ITransformer.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Transformer.ITransformer.begin_edit

```{autodoc2-docstring} altdss.Transformer.ITransformer.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Transformer.ITransformer.end_edit

```{autodoc2-docstring} altdss.Transformer.ITransformer.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Transformer.ITransformer.find

```{autodoc2-docstring} altdss.Transformer.ITransformer.find
```

````

````{py:attribute} kVAs
:canonical: altdss.Transformer.ITransformer.kVAs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.Transformer.ITransformer.kVs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.kVs
```

````

````{py:attribute} m
:canonical: altdss.Transformer.ITransformer.m
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.m
```

````

````{py:attribute} n
:canonical: altdss.Transformer.ITransformer.n
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.n
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Transformer.TransformerProperties]) -> altdss.Transformer.Transformer
:canonical: altdss.Transformer.ITransformer.new

```{autodoc2-docstring} altdss.Transformer.ITransformer.new
```

````

````{py:attribute} pctIMag
:canonical: altdss.Transformer.ITransformer.pctIMag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.Transformer.ITransformer.pctLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.Transformer.ITransformer.pctNoLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.pctNoLoadLoss
```

````

````{py:attribute} pctPerm
:canonical: altdss.Transformer.ITransformer.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.Transformer.ITransformer.pctR
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.Transformer.ITransformer.pctRs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.pctRs
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.Transformer.ITransformer.ppm_Antifloat
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.ITransformer.ppm_Antifloat
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Transformer.ITransformer.to_json

```{autodoc2-docstring} altdss.Transformer.ITransformer.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Transformer.ITransformer.to_list

```{autodoc2-docstring} altdss.Transformer.ITransformer.to_list
```

````

`````

`````{py:class} Transformer(api_util, ptr)
:canonical: altdss.Transformer.Transformer

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PDElement.PDElementMixin`, {py:obj}`altdss.TransformerExtras.TransformerObjMixin`

```{autodoc2-docstring} altdss.Transformer.Transformer
```

````{py:method} AccumulatedL() -> float
:canonical: altdss.Transformer.Transformer.AccumulatedL

```{autodoc2-docstring} altdss.Transformer.Transformer.AccumulatedL
```

````

````{py:attribute} Bank
:canonical: altdss.Transformer.Transformer.Bank
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Transformer.Transformer.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.Transformer.Transformer.Buses
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Buses
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Transformer.Transformer.Close

```{autodoc2-docstring} altdss.Transformer.Transformer.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Transformer.Transformer.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Transformer.Transformer.ComplexSeqVoltages
```

````

````{py:attribute} Conns
:canonical: altdss.Transformer.Transformer.Conns
:type: altdss.enums.Connection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Conns
```

````

````{py:attribute} Conns_str
:canonical: altdss.Transformer.Transformer.Conns_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Conns_str
```

````

````{py:attribute} Core
:canonical: altdss.Transformer.Transformer.Core
:type: altdss.enums.CoreType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Core
```

````

````{py:attribute} Core_str
:canonical: altdss.Transformer.Transformer.Core_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Core_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.Currents

```{autodoc2-docstring} altdss.Transformer.Transformer.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.Transformer.Transformer.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.DisplayName
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Transformer.Transformer.EmergAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.Transformer.Transformer.EmergHkVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.Transformer.Transformer.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.Transformer.Transformer.EnergyMeter

```{autodoc2-docstring} altdss.Transformer.Transformer.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Transformer.Transformer.EnergyMeterName

```{autodoc2-docstring} altdss.Transformer.Transformer.EnergyMeterName
```

````

````{py:attribute} FLRise
:canonical: altdss.Transformer.Transformer.FLRise
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.Transformer.Transformer.FaultRate
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.FaultRate
```

````

````{py:method} FromTerminal() -> int
:canonical: altdss.Transformer.Transformer.FromTerminal

```{autodoc2-docstring} altdss.Transformer.Transformer.FromTerminal
```

````

````{py:method} FullName() -> str
:canonical: altdss.Transformer.Transformer.FullName

```{autodoc2-docstring} altdss.Transformer.Transformer.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Transformer.Transformer.GUID

```{autodoc2-docstring} altdss.Transformer.Transformer.GUID
```

````

````{py:attribute} HSRise
:canonical: altdss.Transformer.Transformer.HSRise
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.HSRise
```

````

````{py:method} Handle() -> int
:canonical: altdss.Transformer.Transformer.Handle

```{autodoc2-docstring} altdss.Transformer.Transformer.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Transformer.Transformer.HasOCPDevice

```{autodoc2-docstring} altdss.Transformer.Transformer.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Transformer.Transformer.HasSwitchControl

```{autodoc2-docstring} altdss.Transformer.Transformer.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Transformer.Transformer.HasVoltControl

```{autodoc2-docstring} altdss.Transformer.Transformer.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Transformer.Transformer.IsIsolated

```{autodoc2-docstring} altdss.Transformer.Transformer.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Transformer.Transformer.IsOpen

```{autodoc2-docstring} altdss.Transformer.Transformer.IsOpen
```

````

````{py:method} IsShunt() -> bool
:canonical: altdss.Transformer.Transformer.IsShunt

```{autodoc2-docstring} altdss.Transformer.Transformer.IsShunt
```

````

````{py:method} Lambda() -> float
:canonical: altdss.Transformer.Transformer.Lambda

```{autodoc2-docstring} altdss.Transformer.Transformer.Lambda
```

````

````{py:attribute} LeadLag
:canonical: altdss.Transformer.Transformer.LeadLag
:type: altdss.enums.PhaseSequence
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.LeadLag
```

````

````{py:attribute} LeadLag_str
:canonical: altdss.Transformer.Transformer.LeadLag_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.LeadLag_str
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Transformer.Transformer.Like

```{autodoc2-docstring} altdss.Transformer.Transformer.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Transformer.Transformer.Losses

```{autodoc2-docstring} altdss.Transformer.Transformer.Losses
```

````

````{py:method} LossesByType() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.LossesByType

```{autodoc2-docstring} altdss.Transformer.Transformer.LossesByType
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Transformer.Transformer.MaxCurrent

```{autodoc2-docstring} altdss.Transformer.Transformer.MaxCurrent
```

````

````{py:attribute} MaxTap
:canonical: altdss.Transformer.Transformer.MaxTap
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.Transformer.Transformer.MinTap
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.MinTap
```

````

````{py:property} Name
:canonical: altdss.Transformer.Transformer.Name
:type: str

```{autodoc2-docstring} altdss.Transformer.Transformer.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Transformer.Transformer.NodeOrder

```{autodoc2-docstring} altdss.Transformer.Transformer.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Transformer.Transformer.NodeRef

```{autodoc2-docstring} altdss.Transformer.Transformer.NodeRef
```

````

````{py:attribute} NormAmps
:canonical: altdss.Transformer.Transformer.NormAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.Transformer.Transformer.NormHkVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.NormHkVA
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Transformer.Transformer.NumConductors

```{autodoc2-docstring} altdss.Transformer.Transformer.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Transformer.Transformer.NumControllers

```{autodoc2-docstring} altdss.Transformer.Transformer.NumControllers
```

````

````{py:method} NumCustomers() -> int
:canonical: altdss.Transformer.Transformer.NumCustomers

```{autodoc2-docstring} altdss.Transformer.Transformer.NumCustomers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Transformer.Transformer.NumPhases

```{autodoc2-docstring} altdss.Transformer.Transformer.NumPhases
```

````

````{py:attribute} NumTaps
:canonical: altdss.Transformer.Transformer.NumTaps
:type: altdss.types.Int32Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.NumTaps
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Transformer.Transformer.NumTerminals

```{autodoc2-docstring} altdss.Transformer.Transformer.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Transformer.Transformer.OCPDevice

```{autodoc2-docstring} altdss.Transformer.Transformer.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Transformer.Transformer.OCPDeviceIndex

```{autodoc2-docstring} altdss.Transformer.Transformer.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Transformer.Transformer.OCPDeviceType

```{autodoc2-docstring} altdss.Transformer.Transformer.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Transformer.Transformer.Open

```{autodoc2-docstring} altdss.Transformer.Transformer.Open
```

````

````{py:method} ParentPDElement() -> altdss.DSSObj.DSSObj
:canonical: altdss.Transformer.Transformer.ParentPDElement

```{autodoc2-docstring} altdss.Transformer.Transformer.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.PhaseLosses

```{autodoc2-docstring} altdss.Transformer.Transformer.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Transformer.Transformer.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.Powers

```{autodoc2-docstring} altdss.Transformer.Transformer.Powers
```

````

````{py:attribute} RDCOhms
:canonical: altdss.Transformer.Transformer.RDCOhms
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.Transformer.Transformer.RNeut
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.Transformer.Transformer.Ratings
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Transformer.Transformer.Repair
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Repair
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Transformer.Transformer.Residuals

```{autodoc2-docstring} altdss.Transformer.Transformer.Residuals
```

````

````{py:attribute} Seasons
:canonical: altdss.Transformer.Transformer.Seasons
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Seasons
```

````

````{py:method} SectionID() -> int
:canonical: altdss.Transformer.Transformer.SectionID

```{autodoc2-docstring} altdss.Transformer.Transformer.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Transformer.Transformer.SeqCurrents

```{autodoc2-docstring} altdss.Transformer.Transformer.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.SeqPowers

```{autodoc2-docstring} altdss.Transformer.Transformer.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Transformer.Transformer.SeqVoltages

```{autodoc2-docstring} altdss.Transformer.Transformer.SeqVoltages
```

````

````{py:attribute} Sub
:canonical: altdss.Transformer.Transformer.Sub
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.Transformer.Transformer.SubName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.Transformer.Transformer.Taps
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.Transformer.Transformer.Thermal
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Thermal
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.Transformer.Transformer.TotalCustomers

```{autodoc2-docstring} altdss.Transformer.Transformer.TotalCustomers
```

````

````{py:method} TotalMiles() -> float
:canonical: altdss.Transformer.Transformer.TotalMiles

```{autodoc2-docstring} altdss.Transformer.Transformer.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.TotalPowers

```{autodoc2-docstring} altdss.Transformer.Transformer.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.Voltages

```{autodoc2-docstring} altdss.Transformer.Transformer.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Transformer.Transformer.VoltagesMagAng

```{autodoc2-docstring} altdss.Transformer.Transformer.VoltagesMagAng
```

````

````{py:method} WindingCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.WindingCurrents

```{autodoc2-docstring} altdss.Transformer.Transformer.WindingCurrents
```

````

````{py:method} WindingVoltages(winding: int) -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.WindingVoltages

```{autodoc2-docstring} altdss.Transformer.Transformer.WindingVoltages
```

````

````{py:attribute} Windings
:canonical: altdss.Transformer.Transformer.Windings
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.Windings
```

````

````{py:attribute} X12
:canonical: altdss.Transformer.Transformer.X12
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.X12
```

````

````{py:attribute} X13
:canonical: altdss.Transformer.Transformer.X13
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.X13
```

````

````{py:attribute} X23
:canonical: altdss.Transformer.Transformer.X23
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.X23
```

````

````{py:attribute} XHL
:canonical: altdss.Transformer.Transformer.XHL
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.Transformer.Transformer.XHT
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.Transformer.Transformer.XLT
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.Transformer.Transformer.XNeut
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.XNeut
```

````

````{py:attribute} XRConst
:canonical: altdss.Transformer.Transformer.XRConst
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.Transformer.Transformer.XSCArray
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.XSCArray
```

````

````{py:attribute} XfmrCode
:canonical: altdss.Transformer.Transformer.XfmrCode
:type: altdss.XfmrCode.XfmrCode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.XfmrCode
```

````

````{py:attribute} XfmrCode_str
:canonical: altdss.Transformer.Transformer.XfmrCode_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.XfmrCode_str
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.Transformer.YPrim

```{autodoc2-docstring} altdss.Transformer.Transformer.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.Transformer.Transformer.__hash__

```{autodoc2-docstring} altdss.Transformer.Transformer.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Transformer.Transformer.__init__

```{autodoc2-docstring} altdss.Transformer.Transformer.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Transformer.Transformer.__ne__

```{autodoc2-docstring} altdss.Transformer.Transformer.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Transformer.Transformer.__repr__

```{autodoc2-docstring} altdss.Transformer.Transformer.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Transformer.Transformer.begin_edit

```{autodoc2-docstring} altdss.Transformer.Transformer.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Transformer.Transformer.end_edit

```{autodoc2-docstring} altdss.Transformer.Transformer.end_edit
```

````

````{py:attribute} kVAs
:canonical: altdss.Transformer.Transformer.kVAs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.Transformer.Transformer.kVs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.kVs
```

````

````{py:attribute} m
:canonical: altdss.Transformer.Transformer.m
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.m
```

````

````{py:attribute} n
:canonical: altdss.Transformer.Transformer.n
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.n
```

````

````{py:method} pctEmerg(allNodes=False) -> float
:canonical: altdss.Transformer.Transformer.pctEmerg

```{autodoc2-docstring} altdss.Transformer.Transformer.pctEmerg
```

````

````{py:attribute} pctIMag
:canonical: altdss.Transformer.Transformer.pctIMag
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.Transformer.Transformer.pctLoadLoss
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.Transformer.Transformer.pctNoLoadLoss
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.pctNoLoadLoss
```

````

````{py:method} pctNorm(allNodes=False) -> float
:canonical: altdss.Transformer.Transformer.pctNorm

```{autodoc2-docstring} altdss.Transformer.Transformer.pctNorm
```

````

````{py:attribute} pctPerm
:canonical: altdss.Transformer.Transformer.pctPerm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.Transformer.Transformer.pctR
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.Transformer.Transformer.pctRs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.pctRs
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.Transformer.Transformer.ppm_Antifloat
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.Transformer.ppm_Antifloat
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Transformer.Transformer.to_json

```{autodoc2-docstring} altdss.Transformer.Transformer.to_json
```

````

`````

`````{py:class} TransformerBatch(api_util, **kwargs)
:canonical: altdss.Transformer.TransformerBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PDElement.PDElementBatchMixin`

```{autodoc2-docstring} altdss.Transformer.TransformerBatch
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Transformer.TransformerBatch.AccumulatedL

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.AccumulatedL
```

````

````{py:attribute} Bank
:canonical: altdss.Transformer.TransformerBatch.Bank
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Transformer.TransformerBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.Transformer.TransformerBatch.Buses
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Buses
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.TransformerBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.TransformerBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conns
:canonical: altdss.Transformer.TransformerBatch.Conns
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Conns
```

````

````{py:attribute} Conns_str
:canonical: altdss.Transformer.TransformerBatch.Conns_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Conns_str
```

````

````{py:attribute} Core
:canonical: altdss.Transformer.TransformerBatch.Core
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Core
```

````

````{py:attribute} Core_str
:canonical: altdss.Transformer.TransformerBatch.Core_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Core_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.TransformerBatch.Currents

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Transformer.TransformerBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.CurrentsMagAng
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Transformer.TransformerBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.Transformer.TransformerBatch.EmergHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.Transformer.TransformerBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Transformer.TransformerBatch.EnergyMeter

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Transformer.TransformerBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.EnergyMeterName
```

````

````{py:attribute} FLRise
:canonical: altdss.Transformer.TransformerBatch.FLRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.Transformer.TransformerBatch.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.FromTerminal

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Transformer.TransformerBatch.FullName

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Transformer.TransformerBatch.GUID

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.GUID
```

````

````{py:attribute} HSRise
:canonical: altdss.Transformer.TransformerBatch.HSRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.HSRise
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.Handle

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Transformer.TransformerBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Transformer.TransformerBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Transformer.TransformerBatch.HasVoltControl

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Transformer.TransformerBatch.IsIsolated

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Transformer.TransformerBatch.IsShunt

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Transformer.TransformerBatch.Lambda

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Lambda
```

````

````{py:attribute} LeadLag
:canonical: altdss.Transformer.TransformerBatch.LeadLag
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.LeadLag
```

````

````{py:attribute} LeadLag_str
:canonical: altdss.Transformer.TransformerBatch.LeadLag_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.LeadLag_str
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Transformer.TransformerBatch.Like

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.TransformerBatch.Losses

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Transformer.TransformerBatch.MaxCurrent

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.MaxCurrent
```

````

````{py:attribute} MaxTap
:canonical: altdss.Transformer.TransformerBatch.MaxTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.Transformer.TransformerBatch.MinTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.MinTap
```

````

````{py:property} Name
:canonical: altdss.Transformer.TransformerBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Transformer.TransformerBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.Transformer.TransformerBatch.NormHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.NormHkVA
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.NumConductors

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.NumControllers

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.NumCustomers

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.NumPhases

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.NumPhases
```

````

````{py:attribute} NumTaps
:canonical: altdss.Transformer.TransformerBatch.NumTaps
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.NumTaps
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.NumTerminals

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Transformer.TransformerBatch.OCPDevice

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Transformer.TransformerBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Transformer.TransformerBatch.ParentPDElement

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.TransformerBatch.PhaseLosses

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Transformer.TransformerBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.TransformerBatch.Powers

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Powers
```

````

````{py:attribute} RDCOhms
:canonical: altdss.Transformer.TransformerBatch.RDCOhms
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.Transformer.TransformerBatch.RNeut
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.Transformer.TransformerBatch.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Transformer.TransformerBatch.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Repair
```

````

````{py:attribute} Seasons
:canonical: altdss.Transformer.TransformerBatch.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Seasons
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.SectionID

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Transformer.TransformerBatch.SeqCurrents

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.TransformerBatch.SeqPowers

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Transformer.TransformerBatch.SeqVoltages

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.SeqVoltages
```

````

````{py:attribute} Sub
:canonical: altdss.Transformer.TransformerBatch.Sub
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.Transformer.TransformerBatch.SubName
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.Transformer.TransformerBatch.Taps
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.Transformer.TransformerBatch.Thermal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Thermal
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Transformer.TransformerBatch.TotalCustomers

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.TotalCustomers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Transformer.TransformerBatch.TotalMiles

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.TransformerBatch.TotalPowers

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Transformer.TransformerBatch.Voltages

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Transformer.TransformerBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.VoltagesMagAng
```

````

````{py:attribute} Windings
:canonical: altdss.Transformer.TransformerBatch.Windings
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.Windings
```

````

````{py:attribute} X12
:canonical: altdss.Transformer.TransformerBatch.X12
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.X12
```

````

````{py:attribute} X13
:canonical: altdss.Transformer.TransformerBatch.X13
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.X13
```

````

````{py:attribute} X23
:canonical: altdss.Transformer.TransformerBatch.X23
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.X23
```

````

````{py:attribute} XHL
:canonical: altdss.Transformer.TransformerBatch.XHL
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.Transformer.TransformerBatch.XHT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.Transformer.TransformerBatch.XLT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.Transformer.TransformerBatch.XNeut
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.XNeut
```

````

````{py:attribute} XRConst
:canonical: altdss.Transformer.TransformerBatch.XRConst
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.Transformer.TransformerBatch.XSCArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.XSCArray
```

````

````{py:attribute} XfmrCode
:canonical: altdss.Transformer.TransformerBatch.XfmrCode
:type: typing.List[altdss.XfmrCode.XfmrCode]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.XfmrCode
```

````

````{py:attribute} XfmrCode_str
:canonical: altdss.Transformer.TransformerBatch.XfmrCode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.XfmrCode_str
```

````

````{py:method} __call__()
:canonical: altdss.Transformer.TransformerBatch.__call__

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Transformer.TransformerBatch.__getitem__

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Transformer.TransformerBatch.__init__

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Transformer.TransformerBatch.__iter__

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Transformer.TransformerBatch.__len__

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Transformer.TransformerBatch.begin_edit

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Transformer.TransformerBatch.end_edit

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.end_edit
```

````

````{py:attribute} kVAs
:canonical: altdss.Transformer.TransformerBatch.kVAs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.Transformer.TransformerBatch.kVs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.kVs
```

````

````{py:attribute} m
:canonical: altdss.Transformer.TransformerBatch.m
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.m
```

````

````{py:attribute} n
:canonical: altdss.Transformer.TransformerBatch.n
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.n
```

````

````{py:attribute} pctIMag
:canonical: altdss.Transformer.TransformerBatch.pctIMag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.Transformer.TransformerBatch.pctLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.Transformer.TransformerBatch.pctNoLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.pctNoLoadLoss
```

````

````{py:attribute} pctPerm
:canonical: altdss.Transformer.TransformerBatch.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.Transformer.TransformerBatch.pctR
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.Transformer.TransformerBatch.pctRs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.pctRs
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.Transformer.TransformerBatch.ppm_Antifloat
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.ppm_Antifloat
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Transformer.TransformerBatch.to_json

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Transformer.TransformerBatch.to_list

```{autodoc2-docstring} altdss.Transformer.TransformerBatch.to_list
```

````

`````

`````{py:class} TransformerBatchProperties()
:canonical: altdss.Transformer.TransformerBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties
```

````{py:attribute} Bank
:canonical: altdss.Transformer.TransformerBatchProperties.Bank
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Transformer.TransformerBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.Transformer.TransformerBatchProperties.Buses
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Buses
```

````

````{py:attribute} Conns
:canonical: altdss.Transformer.TransformerBatchProperties.Conns
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.Connection]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Conns
```

````

````{py:attribute} Core
:canonical: altdss.Transformer.TransformerBatchProperties.Core
:type: typing.Union[typing.AnyStr, int, altdss.enums.CoreType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.CoreType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Core
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Transformer.TransformerBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.Transformer.TransformerBatchProperties.EmergHkVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.Transformer.TransformerBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Enabled
```

````

````{py:attribute} FLRise
:canonical: altdss.Transformer.TransformerBatchProperties.FLRise
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.Transformer.TransformerBatchProperties.FaultRate
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.FaultRate
```

````

````{py:attribute} HSRise
:canonical: altdss.Transformer.TransformerBatchProperties.HSRise
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.HSRise
```

````

````{py:attribute} LeadLag
:canonical: altdss.Transformer.TransformerBatchProperties.LeadLag
:type: typing.Union[typing.AnyStr, int, altdss.enums.PhaseSequence, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.PhaseSequence], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.LeadLag
```

````

````{py:attribute} Like
:canonical: altdss.Transformer.TransformerBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Like
```

````

````{py:attribute} MaxTap
:canonical: altdss.Transformer.TransformerBatchProperties.MaxTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.Transformer.TransformerBatchProperties.MinTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.MinTap
```

````

````{py:attribute} NormAmps
:canonical: altdss.Transformer.TransformerBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.Transformer.TransformerBatchProperties.NormHkVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.NormHkVA
```

````

````{py:attribute} NumTaps
:canonical: altdss.Transformer.TransformerBatchProperties.NumTaps
:type: altdss.types.Int32Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.NumTaps
```

````

````{py:attribute} Phases
:canonical: altdss.Transformer.TransformerBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Phases
```

````

````{py:attribute} RDCOhms
:canonical: altdss.Transformer.TransformerBatchProperties.RDCOhms
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.Transformer.TransformerBatchProperties.RNeut
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.Transformer.TransformerBatchProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Transformer.TransformerBatchProperties.Repair
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Repair
```

````

````{py:attribute} Seasons
:canonical: altdss.Transformer.TransformerBatchProperties.Seasons
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Seasons
```

````

````{py:attribute} Sub
:canonical: altdss.Transformer.TransformerBatchProperties.Sub
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.Transformer.TransformerBatchProperties.SubName
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.Transformer.TransformerBatchProperties.Taps
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.Transformer.TransformerBatchProperties.Thermal
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Thermal
```

````

````{py:attribute} Windings
:canonical: altdss.Transformer.TransformerBatchProperties.Windings
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.Windings
```

````

````{py:attribute} X12
:canonical: altdss.Transformer.TransformerBatchProperties.X12
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.X12
```

````

````{py:attribute} X13
:canonical: altdss.Transformer.TransformerBatchProperties.X13
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.X13
```

````

````{py:attribute} X23
:canonical: altdss.Transformer.TransformerBatchProperties.X23
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.X23
```

````

````{py:attribute} XHL
:canonical: altdss.Transformer.TransformerBatchProperties.XHL
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.Transformer.TransformerBatchProperties.XHT
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.Transformer.TransformerBatchProperties.XLT
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.Transformer.TransformerBatchProperties.XNeut
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.XNeut
```

````

````{py:attribute} XRConst
:canonical: altdss.Transformer.TransformerBatchProperties.XRConst
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.Transformer.TransformerBatchProperties.XSCArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.XSCArray
```

````

````{py:attribute} XfmrCode
:canonical: altdss.Transformer.TransformerBatchProperties.XfmrCode
:type: typing.Union[typing.AnyStr, altdss.XfmrCode.XfmrCode, typing.List[typing.AnyStr], typing.List[altdss.XfmrCode.XfmrCode]]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.XfmrCode
```

````

````{py:method} __contains__()
:canonical: altdss.Transformer.TransformerBatchProperties.__contains__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Transformer.TransformerBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Transformer.TransformerBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Transformer.TransformerBatchProperties.__dir__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Transformer.TransformerBatchProperties.__format__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Transformer.TransformerBatchProperties.__ge__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Transformer.TransformerBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Transformer.TransformerBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Transformer.TransformerBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Transformer.TransformerBatchProperties.__gt__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Transformer.TransformerBatchProperties.__init__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Transformer.TransformerBatchProperties.__ior__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Transformer.TransformerBatchProperties.__iter__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Transformer.TransformerBatchProperties.__le__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Transformer.TransformerBatchProperties.__len__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Transformer.TransformerBatchProperties.__lt__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Transformer.TransformerBatchProperties.__ne__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Transformer.TransformerBatchProperties.__new__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Transformer.TransformerBatchProperties.__or__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Transformer.TransformerBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Transformer.TransformerBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Transformer.TransformerBatchProperties.__repr__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Transformer.TransformerBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Transformer.TransformerBatchProperties.__ror__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Transformer.TransformerBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Transformer.TransformerBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Transformer.TransformerBatchProperties.__str__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Transformer.TransformerBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Transformer.TransformerBatchProperties.clear

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Transformer.TransformerBatchProperties.copy

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Transformer.TransformerBatchProperties.get

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Transformer.TransformerBatchProperties.items

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.items
```

````

````{py:attribute} kVAs
:canonical: altdss.Transformer.TransformerBatchProperties.kVAs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.Transformer.TransformerBatchProperties.kVs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.kVs
```

````

````{py:method} keys()
:canonical: altdss.Transformer.TransformerBatchProperties.keys

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.keys
```

````

````{py:attribute} m
:canonical: altdss.Transformer.TransformerBatchProperties.m
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.m
```

````

````{py:attribute} n
:canonical: altdss.Transformer.TransformerBatchProperties.n
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.n
```

````

````{py:attribute} pctIMag
:canonical: altdss.Transformer.TransformerBatchProperties.pctIMag
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.Transformer.TransformerBatchProperties.pctLoadLoss
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.Transformer.TransformerBatchProperties.pctNoLoadLoss
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.pctNoLoadLoss
```

````

````{py:attribute} pctPerm
:canonical: altdss.Transformer.TransformerBatchProperties.pctPerm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.Transformer.TransformerBatchProperties.pctR
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.Transformer.TransformerBatchProperties.pctRs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.pctRs
```

````

````{py:method} pop()
:canonical: altdss.Transformer.TransformerBatchProperties.pop

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Transformer.TransformerBatchProperties.popitem

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.popitem
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.Transformer.TransformerBatchProperties.ppm_Antifloat
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.ppm_Antifloat
```

````

````{py:method} setdefault()
:canonical: altdss.Transformer.TransformerBatchProperties.setdefault

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Transformer.TransformerBatchProperties.update

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Transformer.TransformerBatchProperties.values

```{autodoc2-docstring} altdss.Transformer.TransformerBatchProperties.values
```

````

`````

`````{py:class} TransformerProperties()
:canonical: altdss.Transformer.TransformerProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Transformer.TransformerProperties
```

````{py:attribute} Bank
:canonical: altdss.Transformer.TransformerProperties.Bank
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Bank
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Transformer.TransformerProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.BaseFreq
```

````

````{py:attribute} Buses
:canonical: altdss.Transformer.TransformerProperties.Buses
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Buses
```

````

````{py:attribute} Conns
:canonical: altdss.Transformer.TransformerProperties.Conns
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.Connection]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Conns
```

````

````{py:attribute} Core
:canonical: altdss.Transformer.TransformerProperties.Core
:type: typing.Union[typing.AnyStr, int, altdss.enums.CoreType]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Core
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Transformer.TransformerProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.EmergAmps
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.Transformer.TransformerProperties.EmergHkVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.EmergHkVA
```

````

````{py:attribute} Enabled
:canonical: altdss.Transformer.TransformerProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Enabled
```

````

````{py:attribute} FLRise
:canonical: altdss.Transformer.TransformerProperties.FLRise
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.FLRise
```

````

````{py:attribute} FaultRate
:canonical: altdss.Transformer.TransformerProperties.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.FaultRate
```

````

````{py:attribute} HSRise
:canonical: altdss.Transformer.TransformerProperties.HSRise
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.HSRise
```

````

````{py:attribute} LeadLag
:canonical: altdss.Transformer.TransformerProperties.LeadLag
:type: typing.Union[typing.AnyStr, int, altdss.enums.PhaseSequence]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.LeadLag
```

````

````{py:attribute} Like
:canonical: altdss.Transformer.TransformerProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Like
```

````

````{py:attribute} MaxTap
:canonical: altdss.Transformer.TransformerProperties.MaxTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.Transformer.TransformerProperties.MinTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.MinTap
```

````

````{py:attribute} NormAmps
:canonical: altdss.Transformer.TransformerProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.NormAmps
```

````

````{py:attribute} NormHkVA
:canonical: altdss.Transformer.TransformerProperties.NormHkVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.NormHkVA
```

````

````{py:attribute} NumTaps
:canonical: altdss.Transformer.TransformerProperties.NumTaps
:type: altdss.types.Int32Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.NumTaps
```

````

````{py:attribute} Phases
:canonical: altdss.Transformer.TransformerProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Phases
```

````

````{py:attribute} RDCOhms
:canonical: altdss.Transformer.TransformerProperties.RDCOhms
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.Transformer.TransformerProperties.RNeut
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.Transformer.TransformerProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Transformer.TransformerProperties.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Repair
```

````

````{py:attribute} Seasons
:canonical: altdss.Transformer.TransformerProperties.Seasons
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Seasons
```

````

````{py:attribute} Sub
:canonical: altdss.Transformer.TransformerProperties.Sub
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Sub
```

````

````{py:attribute} SubName
:canonical: altdss.Transformer.TransformerProperties.SubName
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.SubName
```

````

````{py:attribute} Taps
:canonical: altdss.Transformer.TransformerProperties.Taps
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.Transformer.TransformerProperties.Thermal
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Thermal
```

````

````{py:attribute} Windings
:canonical: altdss.Transformer.TransformerProperties.Windings
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.Windings
```

````

````{py:attribute} X12
:canonical: altdss.Transformer.TransformerProperties.X12
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.X12
```

````

````{py:attribute} X13
:canonical: altdss.Transformer.TransformerProperties.X13
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.X13
```

````

````{py:attribute} X23
:canonical: altdss.Transformer.TransformerProperties.X23
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.X23
```

````

````{py:attribute} XHL
:canonical: altdss.Transformer.TransformerProperties.XHL
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.Transformer.TransformerProperties.XHT
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.Transformer.TransformerProperties.XLT
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.Transformer.TransformerProperties.XNeut
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.XNeut
```

````

````{py:attribute} XRConst
:canonical: altdss.Transformer.TransformerProperties.XRConst
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.XRConst
```

````

````{py:attribute} XSCArray
:canonical: altdss.Transformer.TransformerProperties.XSCArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.XSCArray
```

````

````{py:attribute} XfmrCode
:canonical: altdss.Transformer.TransformerProperties.XfmrCode
:type: typing.Union[typing.AnyStr, altdss.XfmrCode.XfmrCode]
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.XfmrCode
```

````

````{py:method} __contains__()
:canonical: altdss.Transformer.TransformerProperties.__contains__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Transformer.TransformerProperties.__delattr__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Transformer.TransformerProperties.__delitem__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Transformer.TransformerProperties.__dir__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Transformer.TransformerProperties.__format__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Transformer.TransformerProperties.__ge__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Transformer.TransformerProperties.__getattribute__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Transformer.TransformerProperties.__getitem__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Transformer.TransformerProperties.__getstate__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Transformer.TransformerProperties.__gt__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Transformer.TransformerProperties.__init__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Transformer.TransformerProperties.__ior__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Transformer.TransformerProperties.__iter__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Transformer.TransformerProperties.__le__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Transformer.TransformerProperties.__len__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Transformer.TransformerProperties.__lt__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Transformer.TransformerProperties.__ne__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Transformer.TransformerProperties.__new__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Transformer.TransformerProperties.__or__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Transformer.TransformerProperties.__reduce__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Transformer.TransformerProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Transformer.TransformerProperties.__repr__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Transformer.TransformerProperties.__reversed__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Transformer.TransformerProperties.__ror__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Transformer.TransformerProperties.__setitem__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Transformer.TransformerProperties.__sizeof__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Transformer.TransformerProperties.__str__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Transformer.TransformerProperties.__subclasshook__

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Transformer.TransformerProperties.clear

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Transformer.TransformerProperties.copy

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Transformer.TransformerProperties.get

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.get
```

````

````{py:method} items()
:canonical: altdss.Transformer.TransformerProperties.items

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.items
```

````

````{py:attribute} kVAs
:canonical: altdss.Transformer.TransformerProperties.kVAs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.Transformer.TransformerProperties.kVs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.kVs
```

````

````{py:method} keys()
:canonical: altdss.Transformer.TransformerProperties.keys

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.keys
```

````

````{py:attribute} m
:canonical: altdss.Transformer.TransformerProperties.m
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.m
```

````

````{py:attribute} n
:canonical: altdss.Transformer.TransformerProperties.n
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.n
```

````

````{py:attribute} pctIMag
:canonical: altdss.Transformer.TransformerProperties.pctIMag
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.Transformer.TransformerProperties.pctLoadLoss
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.Transformer.TransformerProperties.pctNoLoadLoss
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.pctNoLoadLoss
```

````

````{py:attribute} pctPerm
:canonical: altdss.Transformer.TransformerProperties.pctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.pctPerm
```

````

````{py:attribute} pctR
:canonical: altdss.Transformer.TransformerProperties.pctR
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.Transformer.TransformerProperties.pctRs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.pctRs
```

````

````{py:method} pop()
:canonical: altdss.Transformer.TransformerProperties.pop

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Transformer.TransformerProperties.popitem

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.popitem
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.Transformer.TransformerProperties.ppm_Antifloat
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.ppm_Antifloat
```

````

````{py:method} setdefault()
:canonical: altdss.Transformer.TransformerProperties.setdefault

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Transformer.TransformerProperties.update

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.update
```

````

````{py:method} values()
:canonical: altdss.Transformer.TransformerProperties.values

```{autodoc2-docstring} altdss.Transformer.TransformerProperties.values
```

````

`````
