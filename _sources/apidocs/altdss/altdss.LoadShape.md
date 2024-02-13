# {py:mod}`altdss.LoadShape`

```{py:module} altdss.LoadShape
```

```{autodoc2-docstring} altdss.LoadShape
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ILoadShape <altdss.LoadShape.ILoadShape>`
  - ```{autodoc2-docstring} altdss.LoadShape.ILoadShape
    :summary:
    ```
* - {py:obj}`LoadShape <altdss.LoadShape.LoadShape>`
  - ```{autodoc2-docstring} altdss.LoadShape.LoadShape
    :summary:
    ```
* - {py:obj}`LoadShapeBatch <altdss.LoadShape.LoadShapeBatch>`
  - ```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch
    :summary:
    ```
* - {py:obj}`LoadShapeBatchProperties <altdss.LoadShape.LoadShapeBatchProperties>`
  - ```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties
    :summary:
    ```
* - {py:obj}`LoadShapeProperties <altdss.LoadShape.LoadShapeProperties>`
  - ```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties
    :summary:
    ```
````

### API

`````{py:class} ILoadShape(iobj)
:canonical: altdss.LoadShape.ILoadShape

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.LoadShape.LoadShapeBatch`

```{autodoc2-docstring} altdss.LoadShape.ILoadShape
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.LoadShapeAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.ILoadShape.Action

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.LoadShape.ILoadShape.CSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.LoadShape.ILoadShape.DblFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.DblFile
```

````

````{py:method} DblSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.ILoadShape.DblSave

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.DblSave
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.LoadShape.ILoadShape.FullName

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.FullName
```

````

````{py:attribute} Hour
:canonical: altdss.LoadShape.ILoadShape.Hour
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.Hour
```

````

````{py:attribute} Interpolation
:canonical: altdss.LoadShape.ILoadShape.Interpolation
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.Interpolation
```

````

````{py:attribute} Interpolation_str
:canonical: altdss.LoadShape.ILoadShape.Interpolation_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.Interpolation_str
```

````

````{py:attribute} Interval
:canonical: altdss.LoadShape.ILoadShape.Interval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.Interval
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.ILoadShape.Like

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.LoadShape.ILoadShape.MInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.LoadShape.ILoadShape.Mean
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.Mean
```

````

````{py:attribute} MemoryMapping
:canonical: altdss.LoadShape.ILoadShape.MemoryMapping
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.MemoryMapping
```

````

````{py:attribute} NPts
:canonical: altdss.LoadShape.ILoadShape.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.NPts
```

````

````{py:property} Name
:canonical: altdss.LoadShape.ILoadShape.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.Name
```

````

````{py:method} Normalize(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.ILoadShape.Normalize

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.Normalize
```

````

````{py:attribute} PBase
:canonical: altdss.LoadShape.ILoadShape.PBase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.PBase
```

````

````{py:attribute} PMax
:canonical: altdss.LoadShape.ILoadShape.PMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.PMax
```

````

````{py:attribute} PMult
:canonical: altdss.LoadShape.ILoadShape.PMult
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.PMult
```

````

````{py:attribute} PQCSVFile
:canonical: altdss.LoadShape.ILoadShape.PQCSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.PQCSVFile
```

````

````{py:attribute} QBase
:canonical: altdss.LoadShape.ILoadShape.QBase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.QBase
```

````

````{py:attribute} QMax
:canonical: altdss.LoadShape.ILoadShape.QMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.QMax
```

````

````{py:attribute} QMult
:canonical: altdss.LoadShape.ILoadShape.QMult
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.QMult
```

````

````{py:attribute} SInterval
:canonical: altdss.LoadShape.ILoadShape.SInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.LoadShape.ILoadShape.SngFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.SngFile
```

````

````{py:method} SngSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.ILoadShape.SngSave

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.SngSave
```

````

````{py:attribute} StdDev
:canonical: altdss.LoadShape.ILoadShape.StdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.StdDev
```

````

````{py:attribute} UseActual
:canonical: altdss.LoadShape.ILoadShape.UseActual
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.UseActual
```

````

````{py:method} UseFloat32()
:canonical: altdss.LoadShape.ILoadShape.UseFloat32

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.UseFloat32
```

````

````{py:method} UseFloat64()
:canonical: altdss.LoadShape.ILoadShape.UseFloat64

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.UseFloat64
```

````

````{py:method} __call__()
:canonical: altdss.LoadShape.ILoadShape.__call__

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.LoadShape.ILoadShape.__contains__

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.LoadShape.ILoadShape.__getitem__

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.LoadShape.ILoadShape.__init__

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.LoadShape.ILoadShape.__iter__

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.LoadShape.ILoadShape.__len__

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.LoadShape.ILoadShape.batch

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.LoadShape.LoadShapeBatchProperties]) -> altdss.LoadShape.LoadShapeBatch
:canonical: altdss.LoadShape.ILoadShape.batch_new

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LoadShape.ILoadShape.begin_edit

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LoadShape.ILoadShape.end_edit

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.LoadShape.ILoadShape.find

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.LoadShape.LoadShapeProperties]) -> altdss.LoadShape.LoadShape
:canonical: altdss.LoadShape.ILoadShape.new

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LoadShape.ILoadShape.to_json

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.to_json
```

````

````{py:method} to_list()
:canonical: altdss.LoadShape.ILoadShape.to_list

```{autodoc2-docstring} altdss.LoadShape.ILoadShape.to_list
```

````

`````

`````{py:class} LoadShape(api_util, ptr)
:canonical: altdss.LoadShape.LoadShape

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.LoadShapeExtras.LoadShapeObjMixin`

```{autodoc2-docstring} altdss.LoadShape.LoadShape
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.LoadShapeAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.LoadShape.Action

```{autodoc2-docstring} altdss.LoadShape.LoadShape.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.LoadShape.LoadShape.CSVFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.LoadShape.LoadShape.DblFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.DblFile
```

````

````{py:method} DblSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.LoadShape.DblSave

```{autodoc2-docstring} altdss.LoadShape.LoadShape.DblSave
```

````

````{py:method} FullName() -> str
:canonical: altdss.LoadShape.LoadShape.FullName

```{autodoc2-docstring} altdss.LoadShape.LoadShape.FullName
```

````

````{py:attribute} Hour
:canonical: altdss.LoadShape.LoadShape.Hour
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.Hour
```

````

````{py:attribute} Interpolation
:canonical: altdss.LoadShape.LoadShape.Interpolation
:type: altdss.enums.LoadShapeInterpolation
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.Interpolation
```

````

````{py:attribute} Interpolation_str
:canonical: altdss.LoadShape.LoadShape.Interpolation_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.Interpolation_str
```

````

````{py:attribute} Interval
:canonical: altdss.LoadShape.LoadShape.Interval
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.Interval
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.LoadShape.LoadShape.Like

```{autodoc2-docstring} altdss.LoadShape.LoadShape.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.LoadShape.LoadShape.MInterval
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.LoadShape.LoadShape.Mean
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.Mean
```

````

````{py:attribute} MemoryMapping
:canonical: altdss.LoadShape.LoadShape.MemoryMapping
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.MemoryMapping
```

````

````{py:attribute} NPts
:canonical: altdss.LoadShape.LoadShape.NPts
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.NPts
```

````

````{py:property} Name
:canonical: altdss.LoadShape.LoadShape.Name
:type: str

```{autodoc2-docstring} altdss.LoadShape.LoadShape.Name
```

````

````{py:method} Normalize(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.LoadShape.Normalize

```{autodoc2-docstring} altdss.LoadShape.LoadShape.Normalize
```

````

````{py:attribute} PBase
:canonical: altdss.LoadShape.LoadShape.PBase
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.PBase
```

````

````{py:attribute} PMax
:canonical: altdss.LoadShape.LoadShape.PMax
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.PMax
```

````

````{py:attribute} PMult
:canonical: altdss.LoadShape.LoadShape.PMult
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.PMult
```

````

````{py:attribute} PQCSVFile
:canonical: altdss.LoadShape.LoadShape.PQCSVFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.PQCSVFile
```

````

````{py:attribute} QBase
:canonical: altdss.LoadShape.LoadShape.QBase
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.QBase
```

````

````{py:attribute} QMax
:canonical: altdss.LoadShape.LoadShape.QMax
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.QMax
```

````

````{py:attribute} QMult
:canonical: altdss.LoadShape.LoadShape.QMult
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.QMult
```

````

````{py:attribute} SInterval
:canonical: altdss.LoadShape.LoadShape.SInterval
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.LoadShape.LoadShape.SngFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.SngFile
```

````

````{py:method} SngSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.LoadShape.SngSave

```{autodoc2-docstring} altdss.LoadShape.LoadShape.SngSave
```

````

````{py:attribute} StdDev
:canonical: altdss.LoadShape.LoadShape.StdDev
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.StdDev
```

````

````{py:attribute} UseActual
:canonical: altdss.LoadShape.LoadShape.UseActual
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShape.UseActual
```

````

````{py:method} UseFloat32()
:canonical: altdss.LoadShape.LoadShape.UseFloat32

```{autodoc2-docstring} altdss.LoadShape.LoadShape.UseFloat32
```

````

````{py:method} UseFloat64()
:canonical: altdss.LoadShape.LoadShape.UseFloat64

```{autodoc2-docstring} altdss.LoadShape.LoadShape.UseFloat64
```

````

````{py:method} __hash__()
:canonical: altdss.LoadShape.LoadShape.__hash__

```{autodoc2-docstring} altdss.LoadShape.LoadShape.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.LoadShape.LoadShape.__init__

```{autodoc2-docstring} altdss.LoadShape.LoadShape.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.LoadShape.LoadShape.__ne__

```{autodoc2-docstring} altdss.LoadShape.LoadShape.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.LoadShape.LoadShape.__repr__

```{autodoc2-docstring} altdss.LoadShape.LoadShape.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LoadShape.LoadShape.begin_edit

```{autodoc2-docstring} altdss.LoadShape.LoadShape.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LoadShape.LoadShape.end_edit

```{autodoc2-docstring} altdss.LoadShape.LoadShape.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LoadShape.LoadShape.to_json

```{autodoc2-docstring} altdss.LoadShape.LoadShape.to_json
```

````

`````

`````{py:class} LoadShapeBatch(api_util, **kwargs)
:canonical: altdss.LoadShape.LoadShapeBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.LoadShapeExtras.LoadShapeBatchMixin`

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.LoadShapeAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.LoadShapeBatch.Action

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.LoadShape.LoadShapeBatch.CSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.LoadShape.LoadShapeBatch.DblFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.DblFile
```

````

````{py:method} DblSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.LoadShapeBatch.DblSave

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.DblSave
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.LoadShape.LoadShapeBatch.FullName

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.FullName
```

````

````{py:attribute} Hour
:canonical: altdss.LoadShape.LoadShapeBatch.Hour
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.Hour
```

````

````{py:attribute} Interpolation
:canonical: altdss.LoadShape.LoadShapeBatch.Interpolation
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.Interpolation
```

````

````{py:attribute} Interpolation_str
:canonical: altdss.LoadShape.LoadShapeBatch.Interpolation_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.Interpolation_str
```

````

````{py:attribute} Interval
:canonical: altdss.LoadShape.LoadShapeBatch.Interval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.Interval
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.LoadShapeBatch.Like

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.LoadShape.LoadShapeBatch.MInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.LoadShape.LoadShapeBatch.Mean
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.Mean
```

````

````{py:attribute} MemoryMapping
:canonical: altdss.LoadShape.LoadShapeBatch.MemoryMapping
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.MemoryMapping
```

````

````{py:attribute} NPts
:canonical: altdss.LoadShape.LoadShapeBatch.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.NPts
```

````

````{py:property} Name
:canonical: altdss.LoadShape.LoadShapeBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.Name
```

````

````{py:method} Normalize(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.LoadShapeBatch.Normalize

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.Normalize
```

````

````{py:attribute} PBase
:canonical: altdss.LoadShape.LoadShapeBatch.PBase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.PBase
```

````

````{py:attribute} PMax
:canonical: altdss.LoadShape.LoadShapeBatch.PMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.PMax
```

````

````{py:attribute} PMult
:canonical: altdss.LoadShape.LoadShapeBatch.PMult
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.PMult
```

````

````{py:attribute} PQCSVFile
:canonical: altdss.LoadShape.LoadShapeBatch.PQCSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.PQCSVFile
```

````

````{py:attribute} QBase
:canonical: altdss.LoadShape.LoadShapeBatch.QBase
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.QBase
```

````

````{py:attribute} QMax
:canonical: altdss.LoadShape.LoadShapeBatch.QMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.QMax
```

````

````{py:attribute} QMult
:canonical: altdss.LoadShape.LoadShapeBatch.QMult
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.QMult
```

````

````{py:attribute} SInterval
:canonical: altdss.LoadShape.LoadShapeBatch.SInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.LoadShape.LoadShapeBatch.SngFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.SngFile
```

````

````{py:method} SngSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LoadShape.LoadShapeBatch.SngSave

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.SngSave
```

````

````{py:attribute} StdDev
:canonical: altdss.LoadShape.LoadShapeBatch.StdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.StdDev
```

````

````{py:attribute} UseActual
:canonical: altdss.LoadShape.LoadShapeBatch.UseActual
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.UseActual
```

````

````{py:method} UseFloat32()
:canonical: altdss.LoadShape.LoadShapeBatch.UseFloat32

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.UseFloat32
```

````

````{py:method} UseFloat64()
:canonical: altdss.LoadShape.LoadShapeBatch.UseFloat64

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.UseFloat64
```

````

````{py:method} __call__()
:canonical: altdss.LoadShape.LoadShapeBatch.__call__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.LoadShape.LoadShapeBatch.__getitem__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.LoadShape.LoadShapeBatch.__init__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.LoadShape.LoadShapeBatch.__iter__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.LoadShape.LoadShapeBatch.__len__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LoadShape.LoadShapeBatch.begin_edit

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LoadShape.LoadShapeBatch.end_edit

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LoadShape.LoadShapeBatch.to_json

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.LoadShape.LoadShapeBatch.to_list

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatch.to_list
```

````

`````

`````{py:class} LoadShapeBatchProperties()
:canonical: altdss.LoadShape.LoadShapeBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties
```

````{py:attribute} Action
:canonical: altdss.LoadShape.LoadShapeBatchProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.LoadShapeAction]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.LoadShape.LoadShapeBatchProperties.CSVFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.LoadShape.LoadShapeBatchProperties.DblFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.DblFile
```

````

````{py:attribute} Hour
:canonical: altdss.LoadShape.LoadShapeBatchProperties.Hour
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.Hour
```

````

````{py:attribute} Interpolation
:canonical: altdss.LoadShape.LoadShapeBatchProperties.Interpolation
:type: typing.Union[typing.AnyStr, int, altdss.enums.LoadShapeInterpolation, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LoadShapeInterpolation], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.Interpolation
```

````

````{py:attribute} Interval
:canonical: altdss.LoadShape.LoadShapeBatchProperties.Interval
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.Interval
```

````

````{py:attribute} Like
:canonical: altdss.LoadShape.LoadShapeBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.LoadShape.LoadShapeBatchProperties.MInterval
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.LoadShape.LoadShapeBatchProperties.Mean
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.Mean
```

````

````{py:attribute} MemoryMapping
:canonical: altdss.LoadShape.LoadShapeBatchProperties.MemoryMapping
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.MemoryMapping
```

````

````{py:attribute} NPts
:canonical: altdss.LoadShape.LoadShapeBatchProperties.NPts
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.NPts
```

````

````{py:attribute} PBase
:canonical: altdss.LoadShape.LoadShapeBatchProperties.PBase
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.PBase
```

````

````{py:attribute} PMax
:canonical: altdss.LoadShape.LoadShapeBatchProperties.PMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.PMax
```

````

````{py:attribute} PMult
:canonical: altdss.LoadShape.LoadShapeBatchProperties.PMult
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.PMult
```

````

````{py:attribute} PQCSVFile
:canonical: altdss.LoadShape.LoadShapeBatchProperties.PQCSVFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.PQCSVFile
```

````

````{py:attribute} QBase
:canonical: altdss.LoadShape.LoadShapeBatchProperties.QBase
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.QBase
```

````

````{py:attribute} QMax
:canonical: altdss.LoadShape.LoadShapeBatchProperties.QMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.QMax
```

````

````{py:attribute} QMult
:canonical: altdss.LoadShape.LoadShapeBatchProperties.QMult
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.QMult
```

````

````{py:attribute} SInterval
:canonical: altdss.LoadShape.LoadShapeBatchProperties.SInterval
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.LoadShape.LoadShapeBatchProperties.SngFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.SngFile
```

````

````{py:attribute} StdDev
:canonical: altdss.LoadShape.LoadShapeBatchProperties.StdDev
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.StdDev
```

````

````{py:attribute} UseActual
:canonical: altdss.LoadShape.LoadShapeBatchProperties.UseActual
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.UseActual
```

````

````{py:method} __contains__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__contains__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__delattr__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__delitem__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__dir__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__format__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__ge__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__getitem__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__getstate__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__gt__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__init__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__ior__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__iter__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__le__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__len__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__lt__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__ne__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__new__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__or__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__reduce__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__repr__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__reversed__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__ror__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__setitem__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__str__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.clear

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.copy

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.get

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.items

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.keys

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.pop

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.popitem

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.setdefault

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.update

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.LoadShape.LoadShapeBatchProperties.values

```{autodoc2-docstring} altdss.LoadShape.LoadShapeBatchProperties.values
```

````

`````

`````{py:class} LoadShapeProperties()
:canonical: altdss.LoadShape.LoadShapeProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties
```

````{py:attribute} Action
:canonical: altdss.LoadShape.LoadShapeProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.LoadShapeAction]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.LoadShape.LoadShapeProperties.CSVFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.LoadShape.LoadShapeProperties.DblFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.DblFile
```

````

````{py:attribute} Hour
:canonical: altdss.LoadShape.LoadShapeProperties.Hour
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.Hour
```

````

````{py:attribute} Interpolation
:canonical: altdss.LoadShape.LoadShapeProperties.Interpolation
:type: typing.Union[typing.AnyStr, int, altdss.enums.LoadShapeInterpolation]
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.Interpolation
```

````

````{py:attribute} Interval
:canonical: altdss.LoadShape.LoadShapeProperties.Interval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.Interval
```

````

````{py:attribute} Like
:canonical: altdss.LoadShape.LoadShapeProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.LoadShape.LoadShapeProperties.MInterval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.LoadShape.LoadShapeProperties.Mean
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.Mean
```

````

````{py:attribute} MemoryMapping
:canonical: altdss.LoadShape.LoadShapeProperties.MemoryMapping
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.MemoryMapping
```

````

````{py:attribute} NPts
:canonical: altdss.LoadShape.LoadShapeProperties.NPts
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.NPts
```

````

````{py:attribute} PBase
:canonical: altdss.LoadShape.LoadShapeProperties.PBase
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.PBase
```

````

````{py:attribute} PMax
:canonical: altdss.LoadShape.LoadShapeProperties.PMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.PMax
```

````

````{py:attribute} PMult
:canonical: altdss.LoadShape.LoadShapeProperties.PMult
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.PMult
```

````

````{py:attribute} PQCSVFile
:canonical: altdss.LoadShape.LoadShapeProperties.PQCSVFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.PQCSVFile
```

````

````{py:attribute} QBase
:canonical: altdss.LoadShape.LoadShapeProperties.QBase
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.QBase
```

````

````{py:attribute} QMax
:canonical: altdss.LoadShape.LoadShapeProperties.QMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.QMax
```

````

````{py:attribute} QMult
:canonical: altdss.LoadShape.LoadShapeProperties.QMult
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.QMult
```

````

````{py:attribute} SInterval
:canonical: altdss.LoadShape.LoadShapeProperties.SInterval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.LoadShape.LoadShapeProperties.SngFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.SngFile
```

````

````{py:attribute} StdDev
:canonical: altdss.LoadShape.LoadShapeProperties.StdDev
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.StdDev
```

````

````{py:attribute} UseActual
:canonical: altdss.LoadShape.LoadShapeProperties.UseActual
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.UseActual
```

````

````{py:method} __contains__()
:canonical: altdss.LoadShape.LoadShapeProperties.__contains__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.LoadShape.LoadShapeProperties.__delattr__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.LoadShape.LoadShapeProperties.__delitem__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.LoadShape.LoadShapeProperties.__dir__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.LoadShape.LoadShapeProperties.__format__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.LoadShape.LoadShapeProperties.__ge__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.LoadShape.LoadShapeProperties.__getattribute__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.LoadShape.LoadShapeProperties.__getitem__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.LoadShape.LoadShapeProperties.__getstate__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.LoadShape.LoadShapeProperties.__gt__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.LoadShape.LoadShapeProperties.__init__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.LoadShape.LoadShapeProperties.__ior__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.LoadShape.LoadShapeProperties.__iter__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.LoadShape.LoadShapeProperties.__le__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.LoadShape.LoadShapeProperties.__len__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.LoadShape.LoadShapeProperties.__lt__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.LoadShape.LoadShapeProperties.__ne__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.LoadShape.LoadShapeProperties.__new__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.LoadShape.LoadShapeProperties.__or__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.LoadShape.LoadShapeProperties.__reduce__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.LoadShape.LoadShapeProperties.__reduce_ex__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.LoadShape.LoadShapeProperties.__repr__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.LoadShape.LoadShapeProperties.__reversed__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.LoadShape.LoadShapeProperties.__ror__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.LoadShape.LoadShapeProperties.__setitem__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.LoadShape.LoadShapeProperties.__sizeof__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.LoadShape.LoadShapeProperties.__str__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.LoadShape.LoadShapeProperties.__subclasshook__

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.LoadShape.LoadShapeProperties.clear

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.LoadShape.LoadShapeProperties.copy

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.copy
```

````

````{py:method} get()
:canonical: altdss.LoadShape.LoadShapeProperties.get

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.get
```

````

````{py:method} items()
:canonical: altdss.LoadShape.LoadShapeProperties.items

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.items
```

````

````{py:method} keys()
:canonical: altdss.LoadShape.LoadShapeProperties.keys

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.LoadShape.LoadShapeProperties.pop

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.LoadShape.LoadShapeProperties.popitem

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.LoadShape.LoadShapeProperties.setdefault

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.LoadShape.LoadShapeProperties.update

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.update
```

````

````{py:method} values()
:canonical: altdss.LoadShape.LoadShapeProperties.values

```{autodoc2-docstring} altdss.LoadShape.LoadShapeProperties.values
```

````

`````
