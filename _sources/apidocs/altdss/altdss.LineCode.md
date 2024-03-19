# {py:mod}`altdss.LineCode`

```{py:module} altdss.LineCode
```

```{autodoc2-docstring} altdss.LineCode
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ILineCode <altdss.LineCode.ILineCode>`
  - ```{autodoc2-docstring} altdss.LineCode.ILineCode
    :summary:
    ```
* - {py:obj}`LineCode <altdss.LineCode.LineCode>`
  - ```{autodoc2-docstring} altdss.LineCode.LineCode
    :summary:
    ```
* - {py:obj}`LineCodeBatch <altdss.LineCode.LineCodeBatch>`
  - ```{autodoc2-docstring} altdss.LineCode.LineCodeBatch
    :summary:
    ```
* - {py:obj}`LineCodeBatchProperties <altdss.LineCode.LineCodeBatchProperties>`
  - ```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties
    :summary:
    ```
* - {py:obj}`LineCodeProperties <altdss.LineCode.LineCodeProperties>`
  - ```{autodoc2-docstring} altdss.LineCode.LineCodeProperties
    :summary:
    ```
````

### API

`````{py:class} ILineCode(iobj)
:canonical: altdss.LineCode.ILineCode

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.LineCode.LineCodeBatch`

```{autodoc2-docstring} altdss.LineCode.ILineCode
```

````{py:attribute} B0
:canonical: altdss.LineCode.ILineCode.B0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.B0
```

````

````{py:attribute} B1
:canonical: altdss.LineCode.ILineCode.B1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.LineCode.ILineCode.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.BaseFreq
```

````

````{py:attribute} C0
:canonical: altdss.LineCode.ILineCode.C0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.C0
```

````

````{py:attribute} C1
:canonical: altdss.LineCode.ILineCode.C1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.LineCode.ILineCode.CMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.CMatrix
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineCode.ILineCode.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.EmergAmps
```

````

````{py:attribute} FaultRate
:canonical: altdss.LineCode.ILineCode.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.FaultRate
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.LineCode.ILineCode.FullName

```{autodoc2-docstring} altdss.LineCode.ILineCode.FullName
```

````

````{py:method} Kron(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LineCode.ILineCode.Kron

```{autodoc2-docstring} altdss.LineCode.ILineCode.Kron
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LineCode.ILineCode.Like

```{autodoc2-docstring} altdss.LineCode.ILineCode.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineCode.ILineCode.LineType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.LineType
```

````

````{py:attribute} LineType_str
:canonical: altdss.LineCode.ILineCode.LineType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.LineType_str
```

````

````{py:attribute} NPhases
:canonical: altdss.LineCode.ILineCode.NPhases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.NPhases
```

````

````{py:property} Name
:canonical: altdss.LineCode.ILineCode.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.LineCode.ILineCode.Name
```

````

````{py:attribute} Neutral
:canonical: altdss.LineCode.ILineCode.Neutral
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.Neutral
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineCode.ILineCode.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.NormAmps
```

````

````{py:attribute} PctPerm
:canonical: altdss.LineCode.ILineCode.PctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.PctPerm
```

````

````{py:attribute} R0
:canonical: altdss.LineCode.ILineCode.R0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.R0
```

````

````{py:attribute} R1
:canonical: altdss.LineCode.ILineCode.R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.LineCode.ILineCode.RMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.LineCode.ILineCode.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.LineCode.ILineCode.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.Repair
```

````

````{py:attribute} Rg
:canonical: altdss.LineCode.ILineCode.Rg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.LineCode.ILineCode.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.Seasons
```

````

````{py:attribute} Units
:canonical: altdss.LineCode.ILineCode.Units
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.LineCode.ILineCode.Units_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.Units_str
```

````

````{py:attribute} X0
:canonical: altdss.LineCode.ILineCode.X0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.X0
```

````

````{py:attribute} X1
:canonical: altdss.LineCode.ILineCode.X1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.LineCode.ILineCode.XMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.LineCode.ILineCode.Xg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.Xg
```

````

````{py:method} __call__()
:canonical: altdss.LineCode.ILineCode.__call__

```{autodoc2-docstring} altdss.LineCode.ILineCode.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.LineCode.ILineCode.__contains__

```{autodoc2-docstring} altdss.LineCode.ILineCode.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.LineCode.ILineCode.__getitem__

```{autodoc2-docstring} altdss.LineCode.ILineCode.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.LineCode.ILineCode.__init__

```{autodoc2-docstring} altdss.LineCode.ILineCode.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.LineCode.ILineCode.__iter__

```{autodoc2-docstring} altdss.LineCode.ILineCode.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.LineCode.ILineCode.__len__

```{autodoc2-docstring} altdss.LineCode.ILineCode.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.LineCode.ILineCode.batch

```{autodoc2-docstring} altdss.LineCode.ILineCode.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.LineCode.LineCodeBatchProperties]) -> altdss.LineCode.LineCodeBatch
:canonical: altdss.LineCode.ILineCode.batch_new

```{autodoc2-docstring} altdss.LineCode.ILineCode.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LineCode.ILineCode.begin_edit

```{autodoc2-docstring} altdss.LineCode.ILineCode.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.LineCode.LineCodeBatchProperties]) -> altdss.LineCode.LineCodeBatch
:canonical: altdss.LineCode.ILineCode.edit

```{autodoc2-docstring} altdss.LineCode.ILineCode.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LineCode.ILineCode.end_edit

```{autodoc2-docstring} altdss.LineCode.ILineCode.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.LineCode.ILineCode.find

```{autodoc2-docstring} altdss.LineCode.ILineCode.find
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.LineCode.LineCodeProperties]) -> altdss.LineCode.LineCode
:canonical: altdss.LineCode.ILineCode.new

```{autodoc2-docstring} altdss.LineCode.ILineCode.new
```

````

````{py:attribute} rho
:canonical: altdss.LineCode.ILineCode.rho
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.ILineCode.rho
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LineCode.ILineCode.to_json

```{autodoc2-docstring} altdss.LineCode.ILineCode.to_json
```

````

````{py:method} to_list()
:canonical: altdss.LineCode.ILineCode.to_list

```{autodoc2-docstring} altdss.LineCode.ILineCode.to_list
```

````

`````

`````{py:class} LineCode(api_util, ptr)
:canonical: altdss.LineCode.LineCode

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.LineCode.LineCode
```

````{py:attribute} B0
:canonical: altdss.LineCode.LineCode.B0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.B0
```

````

````{py:attribute} B1
:canonical: altdss.LineCode.LineCode.B1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.LineCode.LineCode.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.BaseFreq
```

````

````{py:attribute} C0
:canonical: altdss.LineCode.LineCode.C0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.C0
```

````

````{py:attribute} C1
:canonical: altdss.LineCode.LineCode.C1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.LineCode.LineCode.CMatrix
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.CMatrix
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineCode.LineCode.EmergAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.EmergAmps
```

````

````{py:attribute} FaultRate
:canonical: altdss.LineCode.LineCode.FaultRate
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.FaultRate
```

````

````{py:method} FullName() -> str
:canonical: altdss.LineCode.LineCode.FullName

```{autodoc2-docstring} altdss.LineCode.LineCode.FullName
```

````

````{py:method} Kron(value: bool = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LineCode.LineCode.Kron

```{autodoc2-docstring} altdss.LineCode.LineCode.Kron
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.LineCode.LineCode.Like

```{autodoc2-docstring} altdss.LineCode.LineCode.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineCode.LineCode.LineType
:type: altdss.enums.LineType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.LineType
```

````

````{py:attribute} LineType_str
:canonical: altdss.LineCode.LineCode.LineType_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.LineType_str
```

````

````{py:attribute} NPhases
:canonical: altdss.LineCode.LineCode.NPhases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.NPhases
```

````

````{py:property} Name
:canonical: altdss.LineCode.LineCode.Name
:type: str

```{autodoc2-docstring} altdss.LineCode.LineCode.Name
```

````

````{py:attribute} Neutral
:canonical: altdss.LineCode.LineCode.Neutral
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.Neutral
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineCode.LineCode.NormAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.NormAmps
```

````

````{py:attribute} PctPerm
:canonical: altdss.LineCode.LineCode.PctPerm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.PctPerm
```

````

````{py:attribute} R0
:canonical: altdss.LineCode.LineCode.R0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.R0
```

````

````{py:attribute} R1
:canonical: altdss.LineCode.LineCode.R1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.LineCode.LineCode.RMatrix
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.LineCode.LineCode.Ratings
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.LineCode.LineCode.Repair
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.Repair
```

````

````{py:attribute} Rg
:canonical: altdss.LineCode.LineCode.Rg
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.LineCode.LineCode.Seasons
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.Seasons
```

````

````{py:attribute} Units
:canonical: altdss.LineCode.LineCode.Units
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.LineCode.LineCode.Units_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.Units_str
```

````

````{py:attribute} X0
:canonical: altdss.LineCode.LineCode.X0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.X0
```

````

````{py:attribute} X1
:canonical: altdss.LineCode.LineCode.X1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.LineCode.LineCode.XMatrix
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.LineCode.LineCode.Xg
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.Xg
```

````

````{py:method} __hash__()
:canonical: altdss.LineCode.LineCode.__hash__

```{autodoc2-docstring} altdss.LineCode.LineCode.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.LineCode.LineCode.__init__

```{autodoc2-docstring} altdss.LineCode.LineCode.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.LineCode.LineCode.__ne__

```{autodoc2-docstring} altdss.LineCode.LineCode.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.LineCode.LineCode.__repr__

```{autodoc2-docstring} altdss.LineCode.LineCode.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LineCode.LineCode.begin_edit

```{autodoc2-docstring} altdss.LineCode.LineCode.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.LineCode.LineCodeProperties]) -> altdss.LineCode.LineCode
:canonical: altdss.LineCode.LineCode.edit

```{autodoc2-docstring} altdss.LineCode.LineCode.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LineCode.LineCode.end_edit

```{autodoc2-docstring} altdss.LineCode.LineCode.end_edit
```

````

````{py:attribute} rho
:canonical: altdss.LineCode.LineCode.rho
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCode.rho
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LineCode.LineCode.to_json

```{autodoc2-docstring} altdss.LineCode.LineCode.to_json
```

````

`````

`````{py:class} LineCodeBatch(api_util, **kwargs)
:canonical: altdss.LineCode.LineCodeBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch
```

````{py:attribute} B0
:canonical: altdss.LineCode.LineCodeBatch.B0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.B0
```

````

````{py:attribute} B1
:canonical: altdss.LineCode.LineCodeBatch.B1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.LineCode.LineCodeBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.BaseFreq
```

````

````{py:attribute} C0
:canonical: altdss.LineCode.LineCodeBatch.C0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.C0
```

````

````{py:attribute} C1
:canonical: altdss.LineCode.LineCodeBatch.C1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.LineCode.LineCodeBatch.CMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.CMatrix
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineCode.LineCodeBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.EmergAmps
```

````

````{py:attribute} FaultRate
:canonical: altdss.LineCode.LineCodeBatch.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.FaultRate
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.LineCode.LineCodeBatch.FullName

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.FullName
```

````

````{py:method} Kron(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LineCode.LineCodeBatch.Kron

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Kron
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LineCode.LineCodeBatch.Like

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineCode.LineCodeBatch.LineType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.LineType
```

````

````{py:attribute} LineType_str
:canonical: altdss.LineCode.LineCodeBatch.LineType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.LineType_str
```

````

````{py:attribute} NPhases
:canonical: altdss.LineCode.LineCodeBatch.NPhases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.NPhases
```

````

````{py:property} Name
:canonical: altdss.LineCode.LineCodeBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Name
```

````

````{py:attribute} Neutral
:canonical: altdss.LineCode.LineCodeBatch.Neutral
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Neutral
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineCode.LineCodeBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.NormAmps
```

````

````{py:attribute} PctPerm
:canonical: altdss.LineCode.LineCodeBatch.PctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.PctPerm
```

````

````{py:attribute} R0
:canonical: altdss.LineCode.LineCodeBatch.R0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.R0
```

````

````{py:attribute} R1
:canonical: altdss.LineCode.LineCodeBatch.R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.LineCode.LineCodeBatch.RMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.LineCode.LineCodeBatch.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.LineCode.LineCodeBatch.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Repair
```

````

````{py:attribute} Rg
:canonical: altdss.LineCode.LineCodeBatch.Rg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.LineCode.LineCodeBatch.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Seasons
```

````

````{py:attribute} Units
:canonical: altdss.LineCode.LineCodeBatch.Units
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.LineCode.LineCodeBatch.Units_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Units_str
```

````

````{py:attribute} X0
:canonical: altdss.LineCode.LineCodeBatch.X0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.X0
```

````

````{py:attribute} X1
:canonical: altdss.LineCode.LineCodeBatch.X1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.LineCode.LineCodeBatch.XMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.LineCode.LineCodeBatch.Xg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.Xg
```

````

````{py:method} __call__()
:canonical: altdss.LineCode.LineCodeBatch.__call__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.LineCode.LineCodeBatch.__getitem__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.LineCode.LineCodeBatch.__init__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.LineCode.LineCodeBatch.__iter__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.LineCode.LineCodeBatch.__len__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.LineCode.LineCodeBatch.batch

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LineCode.LineCodeBatch.begin_edit

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.LineCode.LineCodeBatchProperties]) -> altdss.LineCode.LineCodeBatch
:canonical: altdss.LineCode.LineCodeBatch.edit

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LineCode.LineCodeBatch.end_edit

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.end_edit
```

````

````{py:attribute} rho
:canonical: altdss.LineCode.LineCodeBatch.rho
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.rho
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LineCode.LineCodeBatch.to_json

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.LineCode.LineCodeBatch.to_list

```{autodoc2-docstring} altdss.LineCode.LineCodeBatch.to_list
```

````

`````

`````{py:class} LineCodeBatchProperties()
:canonical: altdss.LineCode.LineCodeBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties
```

````{py:attribute} B0
:canonical: altdss.LineCode.LineCodeBatchProperties.B0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.B0
```

````

````{py:attribute} B1
:canonical: altdss.LineCode.LineCodeBatchProperties.B1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.LineCode.LineCodeBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.BaseFreq
```

````

````{py:attribute} C0
:canonical: altdss.LineCode.LineCodeBatchProperties.C0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.C0
```

````

````{py:attribute} C1
:canonical: altdss.LineCode.LineCodeBatchProperties.C1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.LineCode.LineCodeBatchProperties.CMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.CMatrix
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineCode.LineCodeBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.EmergAmps
```

````

````{py:attribute} FaultRate
:canonical: altdss.LineCode.LineCodeBatchProperties.FaultRate
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.FaultRate
```

````

````{py:attribute} Kron
:canonical: altdss.LineCode.LineCodeBatchProperties.Kron
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.Kron
```

````

````{py:attribute} Like
:canonical: altdss.LineCode.LineCodeBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineCode.LineCodeBatchProperties.LineType
:type: typing.Union[typing.AnyStr, int, altdss.enums.LineType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LineType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.LineType
```

````

````{py:attribute} NPhases
:canonical: altdss.LineCode.LineCodeBatchProperties.NPhases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.NPhases
```

````

````{py:attribute} Neutral
:canonical: altdss.LineCode.LineCodeBatchProperties.Neutral
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.Neutral
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineCode.LineCodeBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.NormAmps
```

````

````{py:attribute} PctPerm
:canonical: altdss.LineCode.LineCodeBatchProperties.PctPerm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.PctPerm
```

````

````{py:attribute} R0
:canonical: altdss.LineCode.LineCodeBatchProperties.R0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.R0
```

````

````{py:attribute} R1
:canonical: altdss.LineCode.LineCodeBatchProperties.R1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.LineCode.LineCodeBatchProperties.RMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.LineCode.LineCodeBatchProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.LineCode.LineCodeBatchProperties.Repair
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.Repair
```

````

````{py:attribute} Rg
:canonical: altdss.LineCode.LineCodeBatchProperties.Rg
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.LineCode.LineCodeBatchProperties.Seasons
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.Seasons
```

````

````{py:attribute} Units
:canonical: altdss.LineCode.LineCodeBatchProperties.Units
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.Units
```

````

````{py:attribute} X0
:canonical: altdss.LineCode.LineCodeBatchProperties.X0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.X0
```

````

````{py:attribute} X1
:canonical: altdss.LineCode.LineCodeBatchProperties.X1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.LineCode.LineCodeBatchProperties.XMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.LineCode.LineCodeBatchProperties.Xg
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.Xg
```

````

````{py:method} __contains__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__contains__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__delattr__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__delitem__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__dir__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__format__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__ge__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__getitem__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__getstate__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__gt__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__init__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__ior__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__iter__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__le__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__len__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__lt__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__ne__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__new__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__or__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__reduce__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__repr__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__reversed__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__ror__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__setitem__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__str__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.LineCode.LineCodeBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.LineCode.LineCodeBatchProperties.clear

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.LineCode.LineCodeBatchProperties.copy

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.LineCode.LineCodeBatchProperties.get

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.LineCode.LineCodeBatchProperties.items

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.LineCode.LineCodeBatchProperties.keys

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.LineCode.LineCodeBatchProperties.pop

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.LineCode.LineCodeBatchProperties.popitem

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.popitem
```

````

````{py:attribute} rho
:canonical: altdss.LineCode.LineCodeBatchProperties.rho
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.rho
```

````

````{py:method} setdefault()
:canonical: altdss.LineCode.LineCodeBatchProperties.setdefault

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.LineCode.LineCodeBatchProperties.update

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.LineCode.LineCodeBatchProperties.values

```{autodoc2-docstring} altdss.LineCode.LineCodeBatchProperties.values
```

````

`````

`````{py:class} LineCodeProperties()
:canonical: altdss.LineCode.LineCodeProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties
```

````{py:attribute} B0
:canonical: altdss.LineCode.LineCodeProperties.B0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.B0
```

````

````{py:attribute} B1
:canonical: altdss.LineCode.LineCodeProperties.B1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.LineCode.LineCodeProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.BaseFreq
```

````

````{py:attribute} C0
:canonical: altdss.LineCode.LineCodeProperties.C0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.C0
```

````

````{py:attribute} C1
:canonical: altdss.LineCode.LineCodeProperties.C1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.LineCode.LineCodeProperties.CMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.CMatrix
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineCode.LineCodeProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.EmergAmps
```

````

````{py:attribute} FaultRate
:canonical: altdss.LineCode.LineCodeProperties.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.FaultRate
```

````

````{py:attribute} Kron
:canonical: altdss.LineCode.LineCodeProperties.Kron
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.Kron
```

````

````{py:attribute} Like
:canonical: altdss.LineCode.LineCodeProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineCode.LineCodeProperties.LineType
:type: typing.Union[typing.AnyStr, int, altdss.enums.LineType]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.LineType
```

````

````{py:attribute} NPhases
:canonical: altdss.LineCode.LineCodeProperties.NPhases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.NPhases
```

````

````{py:attribute} Neutral
:canonical: altdss.LineCode.LineCodeProperties.Neutral
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.Neutral
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineCode.LineCodeProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.NormAmps
```

````

````{py:attribute} PctPerm
:canonical: altdss.LineCode.LineCodeProperties.PctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.PctPerm
```

````

````{py:attribute} R0
:canonical: altdss.LineCode.LineCodeProperties.R0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.R0
```

````

````{py:attribute} R1
:canonical: altdss.LineCode.LineCodeProperties.R1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.LineCode.LineCodeProperties.RMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.LineCode.LineCodeProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.LineCode.LineCodeProperties.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.Repair
```

````

````{py:attribute} Rg
:canonical: altdss.LineCode.LineCodeProperties.Rg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.LineCode.LineCodeProperties.Seasons
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.Seasons
```

````

````{py:attribute} Units
:canonical: altdss.LineCode.LineCodeProperties.Units
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.Units
```

````

````{py:attribute} X0
:canonical: altdss.LineCode.LineCodeProperties.X0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.X0
```

````

````{py:attribute} X1
:canonical: altdss.LineCode.LineCodeProperties.X1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.LineCode.LineCodeProperties.XMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.LineCode.LineCodeProperties.Xg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.Xg
```

````

````{py:method} __contains__()
:canonical: altdss.LineCode.LineCodeProperties.__contains__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.LineCode.LineCodeProperties.__delattr__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.LineCode.LineCodeProperties.__delitem__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.LineCode.LineCodeProperties.__dir__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.LineCode.LineCodeProperties.__format__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.LineCode.LineCodeProperties.__ge__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.LineCode.LineCodeProperties.__getattribute__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.LineCode.LineCodeProperties.__getitem__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.LineCode.LineCodeProperties.__getstate__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.LineCode.LineCodeProperties.__gt__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.LineCode.LineCodeProperties.__init__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.LineCode.LineCodeProperties.__ior__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.LineCode.LineCodeProperties.__iter__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.LineCode.LineCodeProperties.__le__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.LineCode.LineCodeProperties.__len__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.LineCode.LineCodeProperties.__lt__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.LineCode.LineCodeProperties.__ne__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.LineCode.LineCodeProperties.__new__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.LineCode.LineCodeProperties.__or__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.LineCode.LineCodeProperties.__reduce__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.LineCode.LineCodeProperties.__reduce_ex__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.LineCode.LineCodeProperties.__repr__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.LineCode.LineCodeProperties.__reversed__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.LineCode.LineCodeProperties.__ror__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.LineCode.LineCodeProperties.__setitem__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.LineCode.LineCodeProperties.__sizeof__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.LineCode.LineCodeProperties.__str__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.LineCode.LineCodeProperties.__subclasshook__

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.LineCode.LineCodeProperties.clear

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.LineCode.LineCodeProperties.copy

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.copy
```

````

````{py:method} get()
:canonical: altdss.LineCode.LineCodeProperties.get

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.get
```

````

````{py:method} items()
:canonical: altdss.LineCode.LineCodeProperties.items

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.items
```

````

````{py:method} keys()
:canonical: altdss.LineCode.LineCodeProperties.keys

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.LineCode.LineCodeProperties.pop

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.LineCode.LineCodeProperties.popitem

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.popitem
```

````

````{py:attribute} rho
:canonical: altdss.LineCode.LineCodeProperties.rho
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.rho
```

````

````{py:method} setdefault()
:canonical: altdss.LineCode.LineCodeProperties.setdefault

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.LineCode.LineCodeProperties.update

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.update
```

````

````{py:method} values()
:canonical: altdss.LineCode.LineCodeProperties.values

```{autodoc2-docstring} altdss.LineCode.LineCodeProperties.values
```

````

`````
