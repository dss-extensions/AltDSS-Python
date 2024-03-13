# {py:mod}`altdss.Bus`

```{py:module} altdss.Bus
```

```{autodoc2-docstring} altdss.Bus
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Bus <altdss.Bus.Bus>`
  - ```{autodoc2-docstring} altdss.Bus.Bus
    :summary:
    ```
* - {py:obj}`BusBatch <altdss.Bus.BusBatch>`
  - ```{autodoc2-docstring} altdss.Bus.BusBatch
    :summary:
    ```
* - {py:obj}`IBuses <altdss.Bus.IBuses>`
  - ```{autodoc2-docstring} altdss.Bus.IBuses
    :summary:
    ```
````

### API

`````{py:class} Bus(api_util, ptr)
:canonical: altdss.Bus.Bus

```{autodoc2-docstring} altdss.Bus.Bus
```

````{py:property} ComplexSeqVoltages
:canonical: altdss.Bus.Bus.ComplexSeqVoltages
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.ComplexSeqVoltages
```

````

````{py:property} CoordDefined
:canonical: altdss.Bus.Bus.CoordDefined
:type: bool

```{autodoc2-docstring} altdss.Bus.Bus.CoordDefined
```

````

````{py:property} CustDuration
:canonical: altdss.Bus.Bus.CustDuration
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.CustDuration
```

````

````{py:property} CustInterrupts
:canonical: altdss.Bus.Bus.CustInterrupts
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.CustInterrupts
```

````

````{py:property} Distance
:canonical: altdss.Bus.Bus.Distance
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.Distance
```

````

````{py:method} GetUniqueNodeNumber(startNumber: int) -> int
:canonical: altdss.Bus.Bus.GetUniqueNodeNumber

```{autodoc2-docstring} altdss.Bus.Bus.GetUniqueNodeNumber
```

````

````{py:property} ISC
:canonical: altdss.Bus.Bus.ISC
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.ISC
```

````

````{py:property} IntDuration
:canonical: altdss.Bus.Bus.IntDuration
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.IntDuration
```

````

````{py:property} Lambda
:canonical: altdss.Bus.Bus.Lambda
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.Lambda
```

````

````{py:method} Lines() -> altdss.Line.LineBatch
:canonical: altdss.Bus.Bus.Lines

```{autodoc2-docstring} altdss.Bus.Bus.Lines
```

````

````{py:method} Loads() -> altdss.Load.LoadBatch
:canonical: altdss.Bus.Bus.Loads

```{autodoc2-docstring} altdss.Bus.Bus.Loads
```

````

````{py:property} Name
:canonical: altdss.Bus.Bus.Name
:type: str

```{autodoc2-docstring} altdss.Bus.Bus.Name
```

````

````{py:property} Nodes
:canonical: altdss.Bus.Bus.Nodes
:type: altdss.types.Int32Array

```{autodoc2-docstring} altdss.Bus.Bus.Nodes
```

````

````{py:property} NumCustomers
:canonical: altdss.Bus.Bus.NumCustomers
:type: int

```{autodoc2-docstring} altdss.Bus.Bus.NumCustomers
```

````

````{py:property} NumInterrupts
:canonical: altdss.Bus.Bus.NumInterrupts
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.NumInterrupts
```

````

````{py:property} NumNodes
:canonical: altdss.Bus.Bus.NumNodes
:type: int

```{autodoc2-docstring} altdss.Bus.Bus.NumNodes
```

````

````{py:method} PCElements() -> altdss.PCElement.PCElementBatch
:canonical: altdss.Bus.Bus.PCElements

```{autodoc2-docstring} altdss.Bus.Bus.PCElements
```

````

````{py:method} PDElements() -> altdss.PDElement.PDElementBatch
:canonical: altdss.Bus.Bus.PDElements

```{autodoc2-docstring} altdss.Bus.Bus.PDElements
```

````

````{py:property} SectionID
:canonical: altdss.Bus.Bus.SectionID
:type: int

```{autodoc2-docstring} altdss.Bus.Bus.SectionID
```

````

````{py:property} SeqVoltages
:canonical: altdss.Bus.Bus.SeqVoltages
:type: altdss.types.Float64Array

```{autodoc2-docstring} altdss.Bus.Bus.SeqVoltages
```

````

````{py:property} TotalKilometers
:canonical: altdss.Bus.Bus.TotalKilometers
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.TotalKilometers
```

````

````{py:property} TotalMiles
:canonical: altdss.Bus.Bus.TotalMiles
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.TotalMiles
```

````

````{py:property} VLL
:canonical: altdss.Bus.Bus.VLL
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.VLL
```

````

````{py:property} VMagAngle
:canonical: altdss.Bus.Bus.VMagAngle
:type: altdss.types.Float64Array

```{autodoc2-docstring} altdss.Bus.Bus.VMagAngle
```

````

````{py:property} VOC
:canonical: altdss.Bus.Bus.VOC
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.VOC
```

````

````{py:property} Voltages
:canonical: altdss.Bus.Bus.Voltages
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.Voltages
```

````

````{py:property} X
:canonical: altdss.Bus.Bus.X
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.X
```

````

````{py:property} Y
:canonical: altdss.Bus.Bus.Y
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.Y
```

````

````{py:property} YSC
:canonical: altdss.Bus.Bus.YSC
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.YSC
```

````

````{py:property} ZSC
:canonical: altdss.Bus.Bus.ZSC
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.ZSC
```

````

````{py:property} ZSC0
:canonical: altdss.Bus.Bus.ZSC0
:type: complex

```{autodoc2-docstring} altdss.Bus.Bus.ZSC0
```

````

````{py:property} ZSC012
:canonical: altdss.Bus.Bus.ZSC012
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.ZSC012
```

````

````{py:property} ZSC1
:canonical: altdss.Bus.Bus.ZSC1
:type: complex

```{autodoc2-docstring} altdss.Bus.Bus.ZSC1
```

````

````{py:method} ZSCRefresh() -> bool
:canonical: altdss.Bus.Bus.ZSCRefresh

```{autodoc2-docstring} altdss.Bus.Bus.ZSCRefresh
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Bus.Bus.__init__

```{autodoc2-docstring} altdss.Bus.Bus.__init__
```

````

````{py:method} __repr__()
:canonical: altdss.Bus.Bus.__repr__

```{autodoc2-docstring} altdss.Bus.Bus.__repr__
```

````

````{py:property} kVBase
:canonical: altdss.Bus.Bus.kVBase
:type: float

```{autodoc2-docstring} altdss.Bus.Bus.kVBase
```

````

````{py:property} puVLL
:canonical: altdss.Bus.Bus.puVLL
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.puVLL
```

````

````{py:property} puVMagAngle
:canonical: altdss.Bus.Bus.puVMagAngle
:type: altdss.types.Float64Array

```{autodoc2-docstring} altdss.Bus.Bus.puVMagAngle
```

````

````{py:property} puVoltages
:canonical: altdss.Bus.Bus.puVoltages
:type: altdss.types.ComplexArray

```{autodoc2-docstring} altdss.Bus.Bus.puVoltages
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Bus.Bus.to_json

```{autodoc2-docstring} altdss.Bus.Bus.to_json
```

````

`````

`````{py:class} BusBatch(api_util, prefer_lists=False)
:canonical: altdss.Bus.BusBatch

Bases: {py:obj}`altdss.common.Base`

```{autodoc2-docstring} altdss.Bus.BusBatch
```

````{py:method} CustDuration() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.CustDuration

```{autodoc2-docstring} altdss.Bus.BusBatch.CustDuration
```

````

````{py:method} CustInterrupts() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.CustInterrupts

```{autodoc2-docstring} altdss.Bus.BusBatch.CustInterrupts
```

````

````{py:method} Distance() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.Distance

```{autodoc2-docstring} altdss.Bus.BusBatch.Distance
```

````

````{py:method} IntDuration() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.IntDuration

```{autodoc2-docstring} altdss.Bus.BusBatch.IntDuration
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.Lambda

```{autodoc2-docstring} altdss.Bus.BusBatch.Lambda
```

````

````{py:method} Name() -> typing.List[str]
:canonical: altdss.Bus.BusBatch.Name

```{autodoc2-docstring} altdss.Bus.BusBatch.Name
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Bus.BusBatch.NumCustomers

```{autodoc2-docstring} altdss.Bus.BusBatch.NumCustomers
```

````

````{py:method} NumInterrupts() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.NumInterrupts

```{autodoc2-docstring} altdss.Bus.BusBatch.NumInterrupts
```

````

````{py:method} NumNodes() -> altdss.types.Int32Array
:canonical: altdss.Bus.BusBatch.NumNodes

```{autodoc2-docstring} altdss.Bus.BusBatch.NumNodes
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Bus.BusBatch.SectionID

```{autodoc2-docstring} altdss.Bus.BusBatch.SectionID
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.TotalKilometers

```{autodoc2-docstring} altdss.Bus.BusBatch.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.TotalMiles

```{autodoc2-docstring} altdss.Bus.BusBatch.TotalMiles
```

````

````{py:method} X() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.X

```{autodoc2-docstring} altdss.Bus.BusBatch.X
```

````

````{py:method} Y() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.Y

```{autodoc2-docstring} altdss.Bus.BusBatch.Y
```

````

````{py:method} ZSCRefresh() -> bool
:canonical: altdss.Bus.BusBatch.ZSCRefresh

```{autodoc2-docstring} altdss.Bus.BusBatch.ZSCRefresh
```

````

````{py:method} __call__(index: typing.Union[int, str]) -> altdss.Bus.Bus
:canonical: altdss.Bus.BusBatch.__call__

```{autodoc2-docstring} altdss.Bus.BusBatch.__call__
```

````

````{py:method} __getitem__(index: int) -> altdss.Bus.Bus
:canonical: altdss.Bus.BusBatch.__getitem__

```{autodoc2-docstring} altdss.Bus.BusBatch.__getitem__
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: altdss.Bus.BusBatch.__init__

```{autodoc2-docstring} altdss.Bus.BusBatch.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[altdss.Bus.Bus]
:canonical: altdss.Bus.BusBatch.__iter__

```{autodoc2-docstring} altdss.Bus.BusBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Bus.BusBatch.__len__

```{autodoc2-docstring} altdss.Bus.BusBatch.__len__
```

````

````{py:method} kVBase() -> altdss.types.Float64Array
:canonical: altdss.Bus.BusBatch.kVBase

```{autodoc2-docstring} altdss.Bus.BusBatch.kVBase
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Bus.BusBatch.to_json

```{autodoc2-docstring} altdss.Bus.BusBatch.to_json
```

````

`````

`````{py:class} IBuses(api_util, prefer_lists=False)
:canonical: altdss.Bus.IBuses

Bases: {py:obj}`altdss.Bus.BusBatch`

```{autodoc2-docstring} altdss.Bus.IBuses
```

````{py:method} CustDuration() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.CustDuration

```{autodoc2-docstring} altdss.Bus.IBuses.CustDuration
```

````

````{py:method} CustInterrupts() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.CustInterrupts

```{autodoc2-docstring} altdss.Bus.IBuses.CustInterrupts
```

````

````{py:method} Distance() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.Distance

```{autodoc2-docstring} altdss.Bus.IBuses.Distance
```

````

````{py:method} IntDuration() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.IntDuration

```{autodoc2-docstring} altdss.Bus.IBuses.IntDuration
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.Lambda

```{autodoc2-docstring} altdss.Bus.IBuses.Lambda
```

````

````{py:method} Name() -> typing.List[str]
:canonical: altdss.Bus.IBuses.Name

```{autodoc2-docstring} altdss.Bus.IBuses.Name
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Bus.IBuses.NumCustomers

```{autodoc2-docstring} altdss.Bus.IBuses.NumCustomers
```

````

````{py:method} NumInterrupts() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.NumInterrupts

```{autodoc2-docstring} altdss.Bus.IBuses.NumInterrupts
```

````

````{py:method} NumNodes() -> altdss.types.Int32Array
:canonical: altdss.Bus.IBuses.NumNodes

```{autodoc2-docstring} altdss.Bus.IBuses.NumNodes
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Bus.IBuses.SectionID

```{autodoc2-docstring} altdss.Bus.IBuses.SectionID
```

````

````{py:method} TotalKilometers() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.TotalKilometers

```{autodoc2-docstring} altdss.Bus.IBuses.TotalKilometers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.TotalMiles

```{autodoc2-docstring} altdss.Bus.IBuses.TotalMiles
```

````

````{py:method} X() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.X

```{autodoc2-docstring} altdss.Bus.IBuses.X
```

````

````{py:method} Y() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.Y

```{autodoc2-docstring} altdss.Bus.IBuses.Y
```

````

````{py:method} ZSCRefresh() -> bool
:canonical: altdss.Bus.IBuses.ZSCRefresh

```{autodoc2-docstring} altdss.Bus.IBuses.ZSCRefresh
```

````

````{py:method} __call__(index: typing.Union[int, str]) -> altdss.Bus.Bus
:canonical: altdss.Bus.IBuses.__call__

```{autodoc2-docstring} altdss.Bus.IBuses.__call__
```

````

````{py:method} __getitem__(index: typing.Union[int, str]) -> altdss.Bus.Bus
:canonical: altdss.Bus.IBuses.__getitem__

```{autodoc2-docstring} altdss.Bus.IBuses.__getitem__
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: altdss.Bus.IBuses.__init__

```{autodoc2-docstring} altdss.Bus.IBuses.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[altdss.Bus.Bus]
:canonical: altdss.Bus.IBuses.__iter__

```{autodoc2-docstring} altdss.Bus.IBuses.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Bus.IBuses.__len__

```{autodoc2-docstring} altdss.Bus.IBuses.__len__
```

````

````{py:method} find(index_or_name: typing.Union[int, str]) -> altdss.Bus.Bus
:canonical: altdss.Bus.IBuses.find

```{autodoc2-docstring} altdss.Bus.IBuses.find
```

````

````{py:method} kVBase() -> altdss.types.Float64Array
:canonical: altdss.Bus.IBuses.kVBase

```{autodoc2-docstring} altdss.Bus.IBuses.kVBase
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Bus.IBuses.to_json

```{autodoc2-docstring} altdss.Bus.IBuses.to_json
```

````

`````
