# {py:mod}`altdss.PriceShape`

```{py:module} altdss.PriceShape
```

```{autodoc2-docstring} altdss.PriceShape
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IPriceShape <altdss.PriceShape.IPriceShape>`
  - ```{autodoc2-docstring} altdss.PriceShape.IPriceShape
    :summary:
    ```
* - {py:obj}`PriceShape <altdss.PriceShape.PriceShape>`
  - ```{autodoc2-docstring} altdss.PriceShape.PriceShape
    :summary:
    ```
* - {py:obj}`PriceShapeBatch <altdss.PriceShape.PriceShapeBatch>`
  - ```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch
    :summary:
    ```
* - {py:obj}`PriceShapeBatchProperties <altdss.PriceShape.PriceShapeBatchProperties>`
  - ```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties
    :summary:
    ```
* - {py:obj}`PriceShapeProperties <altdss.PriceShape.PriceShapeProperties>`
  - ```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties
    :summary:
    ```
````

### API

`````{py:class} IPriceShape(iobj)
:canonical: altdss.PriceShape.IPriceShape

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.PriceShape.PriceShapeBatch`

```{autodoc2-docstring} altdss.PriceShape.IPriceShape
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.PriceShapeAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.IPriceShape.Action

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.PriceShape.IPriceShape.CSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.PriceShape.IPriceShape.DblFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.DblFile
```

````

````{py:method} DblSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.IPriceShape.DblSave

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.DblSave
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.PriceShape.IPriceShape.FullName

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.FullName
```

````

````{py:attribute} Hour
:canonical: altdss.PriceShape.IPriceShape.Hour
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.PriceShape.IPriceShape.Interval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.Interval
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.IPriceShape.Like

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.PriceShape.IPriceShape.MInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.PriceShape.IPriceShape.Mean
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.PriceShape.IPriceShape.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.NPts
```

````

````{py:property} Name
:canonical: altdss.PriceShape.IPriceShape.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.Name
```

````

````{py:attribute} Price
:canonical: altdss.PriceShape.IPriceShape.Price
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.Price
```

````

````{py:attribute} SInterval
:canonical: altdss.PriceShape.IPriceShape.SInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.PriceShape.IPriceShape.SngFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.SngFile
```

````

````{py:method} SngSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.IPriceShape.SngSave

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.SngSave
```

````

````{py:attribute} StdDev
:canonical: altdss.PriceShape.IPriceShape.StdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.StdDev
```

````

````{py:method} __call__()
:canonical: altdss.PriceShape.IPriceShape.__call__

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.PriceShape.IPriceShape.__contains__

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.PriceShape.IPriceShape.__getitem__

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.PriceShape.IPriceShape.__init__

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.PriceShape.IPriceShape.__iter__

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.PriceShape.IPriceShape.__len__

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.PriceShape.IPriceShape.batch

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.PriceShape.PriceShapeBatchProperties]) -> altdss.PriceShape.PriceShapeBatch
:canonical: altdss.PriceShape.IPriceShape.batch_new

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.PriceShape.IPriceShape.begin_edit

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.PriceShape.IPriceShape.end_edit

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.PriceShape.IPriceShape.find

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.PriceShape.PriceShapeProperties]) -> altdss.PriceShape.PriceShape
:canonical: altdss.PriceShape.IPriceShape.new

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.PriceShape.IPriceShape.to_json

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.to_json
```

````

````{py:method} to_list()
:canonical: altdss.PriceShape.IPriceShape.to_list

```{autodoc2-docstring} altdss.PriceShape.IPriceShape.to_list
```

````

`````

`````{py:class} PriceShape(api_util, ptr)
:canonical: altdss.PriceShape.PriceShape

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.PriceShape.PriceShape
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.PriceShapeAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.PriceShape.Action

```{autodoc2-docstring} altdss.PriceShape.PriceShape.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.PriceShape.PriceShape.CSVFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.PriceShape.PriceShape.DblFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.DblFile
```

````

````{py:method} DblSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.PriceShape.DblSave

```{autodoc2-docstring} altdss.PriceShape.PriceShape.DblSave
```

````

````{py:method} FullName() -> str
:canonical: altdss.PriceShape.PriceShape.FullName

```{autodoc2-docstring} altdss.PriceShape.PriceShape.FullName
```

````

````{py:attribute} Hour
:canonical: altdss.PriceShape.PriceShape.Hour
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.PriceShape.PriceShape.Interval
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.Interval
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.PriceShape.PriceShape.Like

```{autodoc2-docstring} altdss.PriceShape.PriceShape.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.PriceShape.PriceShape.MInterval
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.PriceShape.PriceShape.Mean
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.PriceShape.PriceShape.NPts
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.NPts
```

````

````{py:property} Name
:canonical: altdss.PriceShape.PriceShape.Name
:type: str

```{autodoc2-docstring} altdss.PriceShape.PriceShape.Name
```

````

````{py:attribute} Price
:canonical: altdss.PriceShape.PriceShape.Price
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.Price
```

````

````{py:attribute} SInterval
:canonical: altdss.PriceShape.PriceShape.SInterval
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.PriceShape.PriceShape.SngFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.SngFile
```

````

````{py:method} SngSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.PriceShape.SngSave

```{autodoc2-docstring} altdss.PriceShape.PriceShape.SngSave
```

````

````{py:attribute} StdDev
:canonical: altdss.PriceShape.PriceShape.StdDev
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShape.StdDev
```

````

````{py:method} __hash__()
:canonical: altdss.PriceShape.PriceShape.__hash__

```{autodoc2-docstring} altdss.PriceShape.PriceShape.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.PriceShape.PriceShape.__init__

```{autodoc2-docstring} altdss.PriceShape.PriceShape.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.PriceShape.PriceShape.__ne__

```{autodoc2-docstring} altdss.PriceShape.PriceShape.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.PriceShape.PriceShape.__repr__

```{autodoc2-docstring} altdss.PriceShape.PriceShape.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.PriceShape.PriceShape.begin_edit

```{autodoc2-docstring} altdss.PriceShape.PriceShape.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.PriceShape.PriceShape.end_edit

```{autodoc2-docstring} altdss.PriceShape.PriceShape.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.PriceShape.PriceShape.to_json

```{autodoc2-docstring} altdss.PriceShape.PriceShape.to_json
```

````

`````

`````{py:class} PriceShapeBatch(api_util, **kwargs)
:canonical: altdss.PriceShape.PriceShapeBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.PriceShapeAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.PriceShapeBatch.Action

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.PriceShape.PriceShapeBatch.CSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.PriceShape.PriceShapeBatch.DblFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.DblFile
```

````

````{py:method} DblSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.PriceShapeBatch.DblSave

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.DblSave
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.PriceShape.PriceShapeBatch.FullName

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.FullName
```

````

````{py:attribute} Hour
:canonical: altdss.PriceShape.PriceShapeBatch.Hour
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.PriceShape.PriceShapeBatch.Interval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.Interval
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.PriceShapeBatch.Like

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.PriceShape.PriceShapeBatch.MInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.PriceShape.PriceShapeBatch.Mean
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.PriceShape.PriceShapeBatch.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.NPts
```

````

````{py:property} Name
:canonical: altdss.PriceShape.PriceShapeBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.Name
```

````

````{py:attribute} Price
:canonical: altdss.PriceShape.PriceShapeBatch.Price
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.Price
```

````

````{py:attribute} SInterval
:canonical: altdss.PriceShape.PriceShapeBatch.SInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.PriceShape.PriceShapeBatch.SngFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.SngFile
```

````

````{py:method} SngSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.PriceShape.PriceShapeBatch.SngSave

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.SngSave
```

````

````{py:attribute} StdDev
:canonical: altdss.PriceShape.PriceShapeBatch.StdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.StdDev
```

````

````{py:method} __call__()
:canonical: altdss.PriceShape.PriceShapeBatch.__call__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.PriceShape.PriceShapeBatch.__getitem__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.PriceShape.PriceShapeBatch.__init__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.PriceShape.PriceShapeBatch.__iter__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.PriceShape.PriceShapeBatch.__len__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.PriceShape.PriceShapeBatch.batch

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.PriceShape.PriceShapeBatch.begin_edit

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.PriceShape.PriceShapeBatch.end_edit

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.PriceShape.PriceShapeBatch.to_json

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.PriceShape.PriceShapeBatch.to_list

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatch.to_list
```

````

`````

`````{py:class} PriceShapeBatchProperties()
:canonical: altdss.PriceShape.PriceShapeBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties
```

````{py:attribute} Action
:canonical: altdss.PriceShape.PriceShapeBatchProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.PriceShapeAction]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.PriceShape.PriceShapeBatchProperties.CSVFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.PriceShape.PriceShapeBatchProperties.DblFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.DblFile
```

````

````{py:attribute} Hour
:canonical: altdss.PriceShape.PriceShapeBatchProperties.Hour
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.PriceShape.PriceShapeBatchProperties.Interval
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.Interval
```

````

````{py:attribute} Like
:canonical: altdss.PriceShape.PriceShapeBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.PriceShape.PriceShapeBatchProperties.MInterval
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.PriceShape.PriceShapeBatchProperties.Mean
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.PriceShape.PriceShapeBatchProperties.NPts
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.NPts
```

````

````{py:attribute} Price
:canonical: altdss.PriceShape.PriceShapeBatchProperties.Price
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.Price
```

````

````{py:attribute} SInterval
:canonical: altdss.PriceShape.PriceShapeBatchProperties.SInterval
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.PriceShape.PriceShapeBatchProperties.SngFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.SngFile
```

````

````{py:attribute} StdDev
:canonical: altdss.PriceShape.PriceShapeBatchProperties.StdDev
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.StdDev
```

````

````{py:method} __contains__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__contains__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__delattr__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__delitem__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__dir__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__format__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__ge__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__getitem__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__getstate__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__gt__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__init__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__ior__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__iter__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__le__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__len__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__lt__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__ne__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__new__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__or__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__reduce__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__repr__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__reversed__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__ror__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__setitem__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__str__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.clear

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.copy

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.get

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.items

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.keys

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.pop

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.popitem

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.setdefault

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.update

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.PriceShape.PriceShapeBatchProperties.values

```{autodoc2-docstring} altdss.PriceShape.PriceShapeBatchProperties.values
```

````

`````

`````{py:class} PriceShapeProperties()
:canonical: altdss.PriceShape.PriceShapeProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties
```

````{py:attribute} Action
:canonical: altdss.PriceShape.PriceShapeProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.PriceShapeAction]
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.PriceShape.PriceShapeProperties.CSVFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.PriceShape.PriceShapeProperties.DblFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.DblFile
```

````

````{py:attribute} Hour
:canonical: altdss.PriceShape.PriceShapeProperties.Hour
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.PriceShape.PriceShapeProperties.Interval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.Interval
```

````

````{py:attribute} Like
:canonical: altdss.PriceShape.PriceShapeProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.PriceShape.PriceShapeProperties.MInterval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.PriceShape.PriceShapeProperties.Mean
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.PriceShape.PriceShapeProperties.NPts
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.NPts
```

````

````{py:attribute} Price
:canonical: altdss.PriceShape.PriceShapeProperties.Price
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.Price
```

````

````{py:attribute} SInterval
:canonical: altdss.PriceShape.PriceShapeProperties.SInterval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.PriceShape.PriceShapeProperties.SngFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.SngFile
```

````

````{py:attribute} StdDev
:canonical: altdss.PriceShape.PriceShapeProperties.StdDev
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.StdDev
```

````

````{py:method} __contains__()
:canonical: altdss.PriceShape.PriceShapeProperties.__contains__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.PriceShape.PriceShapeProperties.__delattr__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.PriceShape.PriceShapeProperties.__delitem__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.PriceShape.PriceShapeProperties.__dir__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.PriceShape.PriceShapeProperties.__format__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.PriceShape.PriceShapeProperties.__ge__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.PriceShape.PriceShapeProperties.__getattribute__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.PriceShape.PriceShapeProperties.__getitem__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.PriceShape.PriceShapeProperties.__getstate__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.PriceShape.PriceShapeProperties.__gt__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.PriceShape.PriceShapeProperties.__init__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.PriceShape.PriceShapeProperties.__ior__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.PriceShape.PriceShapeProperties.__iter__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.PriceShape.PriceShapeProperties.__le__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.PriceShape.PriceShapeProperties.__len__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.PriceShape.PriceShapeProperties.__lt__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.PriceShape.PriceShapeProperties.__ne__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.PriceShape.PriceShapeProperties.__new__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.PriceShape.PriceShapeProperties.__or__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.PriceShape.PriceShapeProperties.__reduce__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.PriceShape.PriceShapeProperties.__reduce_ex__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.PriceShape.PriceShapeProperties.__repr__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.PriceShape.PriceShapeProperties.__reversed__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.PriceShape.PriceShapeProperties.__ror__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.PriceShape.PriceShapeProperties.__setitem__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.PriceShape.PriceShapeProperties.__sizeof__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.PriceShape.PriceShapeProperties.__str__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.PriceShape.PriceShapeProperties.__subclasshook__

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.PriceShape.PriceShapeProperties.clear

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.PriceShape.PriceShapeProperties.copy

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.copy
```

````

````{py:method} get()
:canonical: altdss.PriceShape.PriceShapeProperties.get

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.get
```

````

````{py:method} items()
:canonical: altdss.PriceShape.PriceShapeProperties.items

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.items
```

````

````{py:method} keys()
:canonical: altdss.PriceShape.PriceShapeProperties.keys

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.PriceShape.PriceShapeProperties.pop

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.PriceShape.PriceShapeProperties.popitem

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.PriceShape.PriceShapeProperties.setdefault

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.PriceShape.PriceShapeProperties.update

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.update
```

````

````{py:method} values()
:canonical: altdss.PriceShape.PriceShapeProperties.values

```{autodoc2-docstring} altdss.PriceShape.PriceShapeProperties.values
```

````

`````
