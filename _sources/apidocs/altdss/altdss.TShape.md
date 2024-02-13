# {py:mod}`altdss.TShape`

```{py:module} altdss.TShape
```

```{autodoc2-docstring} altdss.TShape
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ITShape <altdss.TShape.ITShape>`
  - ```{autodoc2-docstring} altdss.TShape.ITShape
    :summary:
    ```
* - {py:obj}`TShape <altdss.TShape.TShape>`
  - ```{autodoc2-docstring} altdss.TShape.TShape
    :summary:
    ```
* - {py:obj}`TShapeBatch <altdss.TShape.TShapeBatch>`
  - ```{autodoc2-docstring} altdss.TShape.TShapeBatch
    :summary:
    ```
* - {py:obj}`TShapeBatchProperties <altdss.TShape.TShapeBatchProperties>`
  - ```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties
    :summary:
    ```
* - {py:obj}`TShapeProperties <altdss.TShape.TShapeProperties>`
  - ```{autodoc2-docstring} altdss.TShape.TShapeProperties
    :summary:
    ```
````

### API

`````{py:class} ITShape(iobj)
:canonical: altdss.TShape.ITShape

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.TShape.TShapeBatch`

```{autodoc2-docstring} altdss.TShape.ITShape
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.TShapeAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.ITShape.Action

```{autodoc2-docstring} altdss.TShape.ITShape.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.TShape.ITShape.CSVFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.TShape.ITShape.DblFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.DblFile
```

````

````{py:method} DblSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.ITShape.DblSave

```{autodoc2-docstring} altdss.TShape.ITShape.DblSave
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.TShape.ITShape.FullName

```{autodoc2-docstring} altdss.TShape.ITShape.FullName
```

````

````{py:attribute} Hour
:canonical: altdss.TShape.ITShape.Hour
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.TShape.ITShape.Interval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.Interval
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.ITShape.Like

```{autodoc2-docstring} altdss.TShape.ITShape.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.TShape.ITShape.MInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.TShape.ITShape.Mean
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.TShape.ITShape.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.NPts
```

````

````{py:property} Name
:canonical: altdss.TShape.ITShape.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.TShape.ITShape.Name
```

````

````{py:attribute} SInterval
:canonical: altdss.TShape.ITShape.SInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.TShape.ITShape.SngFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.SngFile
```

````

````{py:method} SngSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.ITShape.SngSave

```{autodoc2-docstring} altdss.TShape.ITShape.SngSave
```

````

````{py:attribute} StdDev
:canonical: altdss.TShape.ITShape.StdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.StdDev
```

````

````{py:attribute} Temp
:canonical: altdss.TShape.ITShape.Temp
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.ITShape.Temp
```

````

````{py:method} __call__()
:canonical: altdss.TShape.ITShape.__call__

```{autodoc2-docstring} altdss.TShape.ITShape.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.TShape.ITShape.__contains__

```{autodoc2-docstring} altdss.TShape.ITShape.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.TShape.ITShape.__getitem__

```{autodoc2-docstring} altdss.TShape.ITShape.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.TShape.ITShape.__init__

```{autodoc2-docstring} altdss.TShape.ITShape.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.TShape.ITShape.__iter__

```{autodoc2-docstring} altdss.TShape.ITShape.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.TShape.ITShape.__len__

```{autodoc2-docstring} altdss.TShape.ITShape.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.TShape.ITShape.batch

```{autodoc2-docstring} altdss.TShape.ITShape.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.TShape.TShapeBatchProperties]) -> altdss.TShape.TShapeBatch
:canonical: altdss.TShape.ITShape.batch_new

```{autodoc2-docstring} altdss.TShape.ITShape.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.TShape.ITShape.begin_edit

```{autodoc2-docstring} altdss.TShape.ITShape.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.TShape.ITShape.end_edit

```{autodoc2-docstring} altdss.TShape.ITShape.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.TShape.ITShape.find

```{autodoc2-docstring} altdss.TShape.ITShape.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.TShape.TShapeProperties]) -> altdss.TShape.TShape
:canonical: altdss.TShape.ITShape.new

```{autodoc2-docstring} altdss.TShape.ITShape.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.TShape.ITShape.to_json

```{autodoc2-docstring} altdss.TShape.ITShape.to_json
```

````

````{py:method} to_list()
:canonical: altdss.TShape.ITShape.to_list

```{autodoc2-docstring} altdss.TShape.ITShape.to_list
```

````

`````

`````{py:class} TShape(api_util, ptr)
:canonical: altdss.TShape.TShape

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.TShape.TShape
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.TShapeAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.TShape.Action

```{autodoc2-docstring} altdss.TShape.TShape.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.TShape.TShape.CSVFile
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.TShape.TShape.DblFile
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.DblFile
```

````

````{py:method} DblSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.TShape.DblSave

```{autodoc2-docstring} altdss.TShape.TShape.DblSave
```

````

````{py:method} FullName() -> str
:canonical: altdss.TShape.TShape.FullName

```{autodoc2-docstring} altdss.TShape.TShape.FullName
```

````

````{py:attribute} Hour
:canonical: altdss.TShape.TShape.Hour
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.TShape.TShape.Interval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.Interval
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.TShape.TShape.Like

```{autodoc2-docstring} altdss.TShape.TShape.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.TShape.TShape.MInterval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.TShape.TShape.Mean
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.TShape.TShape.NPts
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.NPts
```

````

````{py:property} Name
:canonical: altdss.TShape.TShape.Name
:type: str

```{autodoc2-docstring} altdss.TShape.TShape.Name
```

````

````{py:attribute} SInterval
:canonical: altdss.TShape.TShape.SInterval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.TShape.TShape.SngFile
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.SngFile
```

````

````{py:method} SngSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.TShape.SngSave

```{autodoc2-docstring} altdss.TShape.TShape.SngSave
```

````

````{py:attribute} StdDev
:canonical: altdss.TShape.TShape.StdDev
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.StdDev
```

````

````{py:attribute} Temp
:canonical: altdss.TShape.TShape.Temp
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShape.Temp
```

````

````{py:method} __hash__()
:canonical: altdss.TShape.TShape.__hash__

```{autodoc2-docstring} altdss.TShape.TShape.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.TShape.TShape.__init__

```{autodoc2-docstring} altdss.TShape.TShape.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.TShape.TShape.__ne__

```{autodoc2-docstring} altdss.TShape.TShape.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.TShape.TShape.__repr__

```{autodoc2-docstring} altdss.TShape.TShape.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.TShape.TShape.begin_edit

```{autodoc2-docstring} altdss.TShape.TShape.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.TShape.TShape.end_edit

```{autodoc2-docstring} altdss.TShape.TShape.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.TShape.TShape.to_json

```{autodoc2-docstring} altdss.TShape.TShape.to_json
```

````

`````

`````{py:class} TShapeBatch(api_util, **kwargs)
:canonical: altdss.TShape.TShapeBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.TShape.TShapeBatch
```

````{py:method} Action(value: typing.Union[typing.AnyStr, int, altdss.enums.TShapeAction], flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.TShapeBatch.Action

```{autodoc2-docstring} altdss.TShape.TShapeBatch.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.TShape.TShapeBatch.CSVFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.TShape.TShapeBatch.DblFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.DblFile
```

````

````{py:method} DblSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.TShapeBatch.DblSave

```{autodoc2-docstring} altdss.TShape.TShapeBatch.DblSave
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.TShape.TShapeBatch.FullName

```{autodoc2-docstring} altdss.TShape.TShapeBatch.FullName
```

````

````{py:attribute} Hour
:canonical: altdss.TShape.TShapeBatch.Hour
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.TShape.TShapeBatch.Interval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.Interval
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.TShapeBatch.Like

```{autodoc2-docstring} altdss.TShape.TShapeBatch.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.TShape.TShapeBatch.MInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.TShape.TShapeBatch.Mean
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.TShape.TShapeBatch.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.NPts
```

````

````{py:property} Name
:canonical: altdss.TShape.TShapeBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.TShape.TShapeBatch.Name
```

````

````{py:attribute} SInterval
:canonical: altdss.TShape.TShapeBatch.SInterval
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.TShape.TShapeBatch.SngFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.SngFile
```

````

````{py:method} SngSave(flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TShape.TShapeBatch.SngSave

```{autodoc2-docstring} altdss.TShape.TShapeBatch.SngSave
```

````

````{py:attribute} StdDev
:canonical: altdss.TShape.TShapeBatch.StdDev
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.StdDev
```

````

````{py:attribute} Temp
:canonical: altdss.TShape.TShapeBatch.Temp
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatch.Temp
```

````

````{py:method} __call__()
:canonical: altdss.TShape.TShapeBatch.__call__

```{autodoc2-docstring} altdss.TShape.TShapeBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.TShape.TShapeBatch.__getitem__

```{autodoc2-docstring} altdss.TShape.TShapeBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.TShape.TShapeBatch.__init__

```{autodoc2-docstring} altdss.TShape.TShapeBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.TShape.TShapeBatch.__iter__

```{autodoc2-docstring} altdss.TShape.TShapeBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.TShape.TShapeBatch.__len__

```{autodoc2-docstring} altdss.TShape.TShapeBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.TShape.TShapeBatch.begin_edit

```{autodoc2-docstring} altdss.TShape.TShapeBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.TShape.TShapeBatch.end_edit

```{autodoc2-docstring} altdss.TShape.TShapeBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.TShape.TShapeBatch.to_json

```{autodoc2-docstring} altdss.TShape.TShapeBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.TShape.TShapeBatch.to_list

```{autodoc2-docstring} altdss.TShape.TShapeBatch.to_list
```

````

`````

`````{py:class} TShapeBatchProperties()
:canonical: altdss.TShape.TShapeBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties
```

````{py:attribute} Action
:canonical: altdss.TShape.TShapeBatchProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.TShapeAction]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.TShape.TShapeBatchProperties.CSVFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.TShape.TShapeBatchProperties.DblFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.DblFile
```

````

````{py:attribute} Hour
:canonical: altdss.TShape.TShapeBatchProperties.Hour
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.TShape.TShapeBatchProperties.Interval
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.Interval
```

````

````{py:attribute} Like
:canonical: altdss.TShape.TShapeBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.TShape.TShapeBatchProperties.MInterval
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.TShape.TShapeBatchProperties.Mean
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.TShape.TShapeBatchProperties.NPts
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.NPts
```

````

````{py:attribute} SInterval
:canonical: altdss.TShape.TShapeBatchProperties.SInterval
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.TShape.TShapeBatchProperties.SngFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.SngFile
```

````

````{py:attribute} StdDev
:canonical: altdss.TShape.TShapeBatchProperties.StdDev
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.StdDev
```

````

````{py:attribute} Temp
:canonical: altdss.TShape.TShapeBatchProperties.Temp
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.Temp
```

````

````{py:method} __contains__()
:canonical: altdss.TShape.TShapeBatchProperties.__contains__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.TShape.TShapeBatchProperties.__delattr__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.TShape.TShapeBatchProperties.__delitem__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.TShape.TShapeBatchProperties.__dir__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.TShape.TShapeBatchProperties.__format__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.TShape.TShapeBatchProperties.__ge__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.TShape.TShapeBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.TShape.TShapeBatchProperties.__getitem__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.TShape.TShapeBatchProperties.__getstate__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.TShape.TShapeBatchProperties.__gt__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.TShape.TShapeBatchProperties.__init__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.TShape.TShapeBatchProperties.__ior__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.TShape.TShapeBatchProperties.__iter__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.TShape.TShapeBatchProperties.__le__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.TShape.TShapeBatchProperties.__len__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.TShape.TShapeBatchProperties.__lt__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.TShape.TShapeBatchProperties.__ne__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.TShape.TShapeBatchProperties.__new__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.TShape.TShapeBatchProperties.__or__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.TShape.TShapeBatchProperties.__reduce__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.TShape.TShapeBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.TShape.TShapeBatchProperties.__repr__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.TShape.TShapeBatchProperties.__reversed__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.TShape.TShapeBatchProperties.__ror__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.TShape.TShapeBatchProperties.__setitem__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.TShape.TShapeBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.TShape.TShapeBatchProperties.__str__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.TShape.TShapeBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.TShape.TShapeBatchProperties.clear

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.TShape.TShapeBatchProperties.copy

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.TShape.TShapeBatchProperties.get

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.TShape.TShapeBatchProperties.items

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.TShape.TShapeBatchProperties.keys

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.TShape.TShapeBatchProperties.pop

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.TShape.TShapeBatchProperties.popitem

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.TShape.TShapeBatchProperties.setdefault

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.TShape.TShapeBatchProperties.update

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.TShape.TShapeBatchProperties.values

```{autodoc2-docstring} altdss.TShape.TShapeBatchProperties.values
```

````

`````

`````{py:class} TShapeProperties()
:canonical: altdss.TShape.TShapeProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.TShape.TShapeProperties
```

````{py:attribute} Action
:canonical: altdss.TShape.TShapeProperties.Action
:type: typing.Union[typing.AnyStr, int, altdss.enums.TShapeAction]
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.Action
```

````

````{py:attribute} CSVFile
:canonical: altdss.TShape.TShapeProperties.CSVFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.TShape.TShapeProperties.DblFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.DblFile
```

````

````{py:attribute} Hour
:canonical: altdss.TShape.TShapeProperties.Hour
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.Hour
```

````

````{py:attribute} Interval
:canonical: altdss.TShape.TShapeProperties.Interval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.Interval
```

````

````{py:attribute} Like
:canonical: altdss.TShape.TShapeProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.Like
```

````

````{py:attribute} MInterval
:canonical: altdss.TShape.TShapeProperties.MInterval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.MInterval
```

````

````{py:attribute} Mean
:canonical: altdss.TShape.TShapeProperties.Mean
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.Mean
```

````

````{py:attribute} NPts
:canonical: altdss.TShape.TShapeProperties.NPts
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.NPts
```

````

````{py:attribute} SInterval
:canonical: altdss.TShape.TShapeProperties.SInterval
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.SInterval
```

````

````{py:attribute} SngFile
:canonical: altdss.TShape.TShapeProperties.SngFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.SngFile
```

````

````{py:attribute} StdDev
:canonical: altdss.TShape.TShapeProperties.StdDev
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.StdDev
```

````

````{py:attribute} Temp
:canonical: altdss.TShape.TShapeProperties.Temp
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TShape.TShapeProperties.Temp
```

````

````{py:method} __contains__()
:canonical: altdss.TShape.TShapeProperties.__contains__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.TShape.TShapeProperties.__delattr__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.TShape.TShapeProperties.__delitem__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.TShape.TShapeProperties.__dir__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.TShape.TShapeProperties.__format__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.TShape.TShapeProperties.__ge__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.TShape.TShapeProperties.__getattribute__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.TShape.TShapeProperties.__getitem__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.TShape.TShapeProperties.__getstate__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.TShape.TShapeProperties.__gt__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.TShape.TShapeProperties.__init__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.TShape.TShapeProperties.__ior__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.TShape.TShapeProperties.__iter__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.TShape.TShapeProperties.__le__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.TShape.TShapeProperties.__len__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.TShape.TShapeProperties.__lt__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.TShape.TShapeProperties.__ne__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.TShape.TShapeProperties.__new__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.TShape.TShapeProperties.__or__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.TShape.TShapeProperties.__reduce__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.TShape.TShapeProperties.__reduce_ex__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.TShape.TShapeProperties.__repr__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.TShape.TShapeProperties.__reversed__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.TShape.TShapeProperties.__ror__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.TShape.TShapeProperties.__setitem__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.TShape.TShapeProperties.__sizeof__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.TShape.TShapeProperties.__str__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.TShape.TShapeProperties.__subclasshook__

```{autodoc2-docstring} altdss.TShape.TShapeProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.TShape.TShapeProperties.clear

```{autodoc2-docstring} altdss.TShape.TShapeProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.TShape.TShapeProperties.copy

```{autodoc2-docstring} altdss.TShape.TShapeProperties.copy
```

````

````{py:method} get()
:canonical: altdss.TShape.TShapeProperties.get

```{autodoc2-docstring} altdss.TShape.TShapeProperties.get
```

````

````{py:method} items()
:canonical: altdss.TShape.TShapeProperties.items

```{autodoc2-docstring} altdss.TShape.TShapeProperties.items
```

````

````{py:method} keys()
:canonical: altdss.TShape.TShapeProperties.keys

```{autodoc2-docstring} altdss.TShape.TShapeProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.TShape.TShapeProperties.pop

```{autodoc2-docstring} altdss.TShape.TShapeProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.TShape.TShapeProperties.popitem

```{autodoc2-docstring} altdss.TShape.TShapeProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.TShape.TShapeProperties.setdefault

```{autodoc2-docstring} altdss.TShape.TShapeProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.TShape.TShapeProperties.update

```{autodoc2-docstring} altdss.TShape.TShapeProperties.update
```

````

````{py:method} values()
:canonical: altdss.TShape.TShapeProperties.values

```{autodoc2-docstring} altdss.TShape.TShapeProperties.values
```

````

`````
