# {py:mod}`altdss.XYcurve`

```{py:module} altdss.XYcurve
```

```{autodoc2-docstring} altdss.XYcurve
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IXYcurve <altdss.XYcurve.IXYcurve>`
  - ```{autodoc2-docstring} altdss.XYcurve.IXYcurve
    :summary:
    ```
* - {py:obj}`XYcurve <altdss.XYcurve.XYcurve>`
  - ```{autodoc2-docstring} altdss.XYcurve.XYcurve
    :summary:
    ```
* - {py:obj}`XYcurveBatch <altdss.XYcurve.XYcurveBatch>`
  - ```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch
    :summary:
    ```
* - {py:obj}`XYcurveBatchProperties <altdss.XYcurve.XYcurveBatchProperties>`
  - ```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties
    :summary:
    ```
* - {py:obj}`XYcurveProperties <altdss.XYcurve.XYcurveProperties>`
  - ```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties
    :summary:
    ```
````

### API

`````{py:class} IXYcurve(iobj)
:canonical: altdss.XYcurve.IXYcurve

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.XYcurve.XYcurveBatch`

```{autodoc2-docstring} altdss.XYcurve.IXYcurve
```

````{py:attribute} CSVFile
:canonical: altdss.XYcurve.IXYcurve.CSVFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.XYcurve.IXYcurve.DblFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.DblFile
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.XYcurve.IXYcurve.FullName

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.FullName
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.XYcurve.IXYcurve.Like

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.Like
```

````

````{py:attribute} NPts
:canonical: altdss.XYcurve.IXYcurve.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.NPts
```

````

````{py:property} Name
:canonical: altdss.XYcurve.IXYcurve.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.Name
```

````

````{py:attribute} SngFile
:canonical: altdss.XYcurve.IXYcurve.SngFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.SngFile
```

````

````{py:attribute} X
:canonical: altdss.XYcurve.IXYcurve.X
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.X
```

````

````{py:attribute} XArray
:canonical: altdss.XYcurve.IXYcurve.XArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.XArray
```

````

````{py:attribute} XScale
:canonical: altdss.XYcurve.IXYcurve.XScale
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.XScale
```

````

````{py:attribute} XShift
:canonical: altdss.XYcurve.IXYcurve.XShift
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.XShift
```

````

````{py:attribute} Y
:canonical: altdss.XYcurve.IXYcurve.Y
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.Y
```

````

````{py:attribute} YArray
:canonical: altdss.XYcurve.IXYcurve.YArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.YArray
```

````

````{py:attribute} YScale
:canonical: altdss.XYcurve.IXYcurve.YScale
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.YScale
```

````

````{py:attribute} YShift
:canonical: altdss.XYcurve.IXYcurve.YShift
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.YShift
```

````

````{py:method} __call__()
:canonical: altdss.XYcurve.IXYcurve.__call__

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.XYcurve.IXYcurve.__contains__

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.XYcurve.IXYcurve.__getitem__

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.XYcurve.IXYcurve.__init__

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.XYcurve.IXYcurve.__iter__

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.XYcurve.IXYcurve.__len__

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.XYcurve.IXYcurve.batch

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.XYcurve.XYcurveBatchProperties]) -> altdss.XYcurve.XYcurveBatch
:canonical: altdss.XYcurve.IXYcurve.batch_new

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.XYcurve.IXYcurve.begin_edit

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.XYcurve.IXYcurve.end_edit

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.XYcurve.IXYcurve.find

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.XYcurve.XYcurveProperties]) -> altdss.XYcurve.XYcurve
:canonical: altdss.XYcurve.IXYcurve.new

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.XYcurve.IXYcurve.to_json

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.to_json
```

````

````{py:method} to_list()
:canonical: altdss.XYcurve.IXYcurve.to_list

```{autodoc2-docstring} altdss.XYcurve.IXYcurve.to_list
```

````

`````

`````{py:class} XYcurve(api_util, ptr)
:canonical: altdss.XYcurve.XYcurve

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.XYcurve.XYcurve
```

````{py:attribute} CSVFile
:canonical: altdss.XYcurve.XYcurve.CSVFile
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.XYcurve.XYcurve.DblFile
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.DblFile
```

````

````{py:method} FullName() -> str
:canonical: altdss.XYcurve.XYcurve.FullName

```{autodoc2-docstring} altdss.XYcurve.XYcurve.FullName
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.XYcurve.XYcurve.Like

```{autodoc2-docstring} altdss.XYcurve.XYcurve.Like
```

````

````{py:attribute} NPts
:canonical: altdss.XYcurve.XYcurve.NPts
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.NPts
```

````

````{py:property} Name
:canonical: altdss.XYcurve.XYcurve.Name
:type: str

```{autodoc2-docstring} altdss.XYcurve.XYcurve.Name
```

````

````{py:attribute} SngFile
:canonical: altdss.XYcurve.XYcurve.SngFile
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.SngFile
```

````

````{py:attribute} X
:canonical: altdss.XYcurve.XYcurve.X
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.X
```

````

````{py:attribute} XArray
:canonical: altdss.XYcurve.XYcurve.XArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.XArray
```

````

````{py:attribute} XScale
:canonical: altdss.XYcurve.XYcurve.XScale
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.XScale
```

````

````{py:attribute} XShift
:canonical: altdss.XYcurve.XYcurve.XShift
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.XShift
```

````

````{py:attribute} Y
:canonical: altdss.XYcurve.XYcurve.Y
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.Y
```

````

````{py:attribute} YArray
:canonical: altdss.XYcurve.XYcurve.YArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.YArray
```

````

````{py:attribute} YScale
:canonical: altdss.XYcurve.XYcurve.YScale
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.YScale
```

````

````{py:attribute} YShift
:canonical: altdss.XYcurve.XYcurve.YShift
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurve.YShift
```

````

````{py:method} __hash__()
:canonical: altdss.XYcurve.XYcurve.__hash__

```{autodoc2-docstring} altdss.XYcurve.XYcurve.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.XYcurve.XYcurve.__init__

```{autodoc2-docstring} altdss.XYcurve.XYcurve.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.XYcurve.XYcurve.__ne__

```{autodoc2-docstring} altdss.XYcurve.XYcurve.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.XYcurve.XYcurve.__repr__

```{autodoc2-docstring} altdss.XYcurve.XYcurve.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.XYcurve.XYcurve.begin_edit

```{autodoc2-docstring} altdss.XYcurve.XYcurve.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.XYcurve.XYcurve.end_edit

```{autodoc2-docstring} altdss.XYcurve.XYcurve.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.XYcurve.XYcurve.to_json

```{autodoc2-docstring} altdss.XYcurve.XYcurve.to_json
```

````

`````

`````{py:class} XYcurveBatch(api_util, **kwargs)
:canonical: altdss.XYcurve.XYcurveBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch
```

````{py:attribute} CSVFile
:canonical: altdss.XYcurve.XYcurveBatch.CSVFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.XYcurve.XYcurveBatch.DblFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.DblFile
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.XYcurve.XYcurveBatch.FullName

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.FullName
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.XYcurve.XYcurveBatch.Like

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.Like
```

````

````{py:attribute} NPts
:canonical: altdss.XYcurve.XYcurveBatch.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.NPts
```

````

````{py:property} Name
:canonical: altdss.XYcurve.XYcurveBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.Name
```

````

````{py:attribute} SngFile
:canonical: altdss.XYcurve.XYcurveBatch.SngFile
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.SngFile
```

````

````{py:attribute} X
:canonical: altdss.XYcurve.XYcurveBatch.X
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.X
```

````

````{py:attribute} XArray
:canonical: altdss.XYcurve.XYcurveBatch.XArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.XArray
```

````

````{py:attribute} XScale
:canonical: altdss.XYcurve.XYcurveBatch.XScale
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.XScale
```

````

````{py:attribute} XShift
:canonical: altdss.XYcurve.XYcurveBatch.XShift
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.XShift
```

````

````{py:attribute} Y
:canonical: altdss.XYcurve.XYcurveBatch.Y
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.Y
```

````

````{py:attribute} YArray
:canonical: altdss.XYcurve.XYcurveBatch.YArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.YArray
```

````

````{py:attribute} YScale
:canonical: altdss.XYcurve.XYcurveBatch.YScale
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.YScale
```

````

````{py:attribute} YShift
:canonical: altdss.XYcurve.XYcurveBatch.YShift
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.YShift
```

````

````{py:method} __call__()
:canonical: altdss.XYcurve.XYcurveBatch.__call__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.XYcurve.XYcurveBatch.__getitem__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.XYcurve.XYcurveBatch.__init__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.XYcurve.XYcurveBatch.__iter__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.XYcurve.XYcurveBatch.__len__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.XYcurve.XYcurveBatch.begin_edit

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.XYcurve.XYcurveBatch.end_edit

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.XYcurve.XYcurveBatch.to_json

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.XYcurve.XYcurveBatch.to_list

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatch.to_list
```

````

`````

`````{py:class} XYcurveBatchProperties()
:canonical: altdss.XYcurve.XYcurveBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties
```

````{py:attribute} CSVFile
:canonical: altdss.XYcurve.XYcurveBatchProperties.CSVFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.XYcurve.XYcurveBatchProperties.DblFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.DblFile
```

````

````{py:attribute} Like
:canonical: altdss.XYcurve.XYcurveBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.Like
```

````

````{py:attribute} NPts
:canonical: altdss.XYcurve.XYcurveBatchProperties.NPts
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.NPts
```

````

````{py:attribute} SngFile
:canonical: altdss.XYcurve.XYcurveBatchProperties.SngFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.SngFile
```

````

````{py:attribute} X
:canonical: altdss.XYcurve.XYcurveBatchProperties.X
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.X
```

````

````{py:attribute} XArray
:canonical: altdss.XYcurve.XYcurveBatchProperties.XArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.XArray
```

````

````{py:attribute} XScale
:canonical: altdss.XYcurve.XYcurveBatchProperties.XScale
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.XScale
```

````

````{py:attribute} XShift
:canonical: altdss.XYcurve.XYcurveBatchProperties.XShift
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.XShift
```

````

````{py:attribute} Y
:canonical: altdss.XYcurve.XYcurveBatchProperties.Y
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.Y
```

````

````{py:attribute} YArray
:canonical: altdss.XYcurve.XYcurveBatchProperties.YArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.YArray
```

````

````{py:attribute} YScale
:canonical: altdss.XYcurve.XYcurveBatchProperties.YScale
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.YScale
```

````

````{py:attribute} YShift
:canonical: altdss.XYcurve.XYcurveBatchProperties.YShift
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.YShift
```

````

````{py:method} __contains__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__contains__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__delattr__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__delitem__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__dir__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__format__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__ge__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__getitem__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__getstate__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__gt__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__init__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__ior__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__iter__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__le__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__len__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__lt__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__ne__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__new__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__or__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__reduce__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__repr__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__reversed__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__ror__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__setitem__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__str__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.XYcurve.XYcurveBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.XYcurve.XYcurveBatchProperties.clear

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.XYcurve.XYcurveBatchProperties.copy

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.XYcurve.XYcurveBatchProperties.get

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.XYcurve.XYcurveBatchProperties.items

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.XYcurve.XYcurveBatchProperties.keys

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.XYcurve.XYcurveBatchProperties.pop

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.XYcurve.XYcurveBatchProperties.popitem

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.XYcurve.XYcurveBatchProperties.setdefault

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.XYcurve.XYcurveBatchProperties.update

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.XYcurve.XYcurveBatchProperties.values

```{autodoc2-docstring} altdss.XYcurve.XYcurveBatchProperties.values
```

````

`````

`````{py:class} XYcurveProperties()
:canonical: altdss.XYcurve.XYcurveProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties
```

````{py:attribute} CSVFile
:canonical: altdss.XYcurve.XYcurveProperties.CSVFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.XYcurve.XYcurveProperties.DblFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.DblFile
```

````

````{py:attribute} Like
:canonical: altdss.XYcurve.XYcurveProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.Like
```

````

````{py:attribute} NPts
:canonical: altdss.XYcurve.XYcurveProperties.NPts
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.NPts
```

````

````{py:attribute} SngFile
:canonical: altdss.XYcurve.XYcurveProperties.SngFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.SngFile
```

````

````{py:attribute} X
:canonical: altdss.XYcurve.XYcurveProperties.X
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.X
```

````

````{py:attribute} XArray
:canonical: altdss.XYcurve.XYcurveProperties.XArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.XArray
```

````

````{py:attribute} XScale
:canonical: altdss.XYcurve.XYcurveProperties.XScale
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.XScale
```

````

````{py:attribute} XShift
:canonical: altdss.XYcurve.XYcurveProperties.XShift
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.XShift
```

````

````{py:attribute} Y
:canonical: altdss.XYcurve.XYcurveProperties.Y
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.Y
```

````

````{py:attribute} YArray
:canonical: altdss.XYcurve.XYcurveProperties.YArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.YArray
```

````

````{py:attribute} YScale
:canonical: altdss.XYcurve.XYcurveProperties.YScale
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.YScale
```

````

````{py:attribute} YShift
:canonical: altdss.XYcurve.XYcurveProperties.YShift
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.YShift
```

````

````{py:method} __contains__()
:canonical: altdss.XYcurve.XYcurveProperties.__contains__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.XYcurve.XYcurveProperties.__delattr__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.XYcurve.XYcurveProperties.__delitem__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.XYcurve.XYcurveProperties.__dir__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.XYcurve.XYcurveProperties.__format__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.XYcurve.XYcurveProperties.__ge__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.XYcurve.XYcurveProperties.__getattribute__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.XYcurve.XYcurveProperties.__getitem__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.XYcurve.XYcurveProperties.__getstate__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.XYcurve.XYcurveProperties.__gt__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.XYcurve.XYcurveProperties.__init__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.XYcurve.XYcurveProperties.__ior__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.XYcurve.XYcurveProperties.__iter__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.XYcurve.XYcurveProperties.__le__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.XYcurve.XYcurveProperties.__len__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.XYcurve.XYcurveProperties.__lt__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.XYcurve.XYcurveProperties.__ne__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.XYcurve.XYcurveProperties.__new__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.XYcurve.XYcurveProperties.__or__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.XYcurve.XYcurveProperties.__reduce__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.XYcurve.XYcurveProperties.__reduce_ex__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.XYcurve.XYcurveProperties.__repr__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.XYcurve.XYcurveProperties.__reversed__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.XYcurve.XYcurveProperties.__ror__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.XYcurve.XYcurveProperties.__setitem__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.XYcurve.XYcurveProperties.__sizeof__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.XYcurve.XYcurveProperties.__str__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.XYcurve.XYcurveProperties.__subclasshook__

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.XYcurve.XYcurveProperties.clear

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.XYcurve.XYcurveProperties.copy

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.copy
```

````

````{py:method} get()
:canonical: altdss.XYcurve.XYcurveProperties.get

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.get
```

````

````{py:method} items()
:canonical: altdss.XYcurve.XYcurveProperties.items

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.items
```

````

````{py:method} keys()
:canonical: altdss.XYcurve.XYcurveProperties.keys

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.XYcurve.XYcurveProperties.pop

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.XYcurve.XYcurveProperties.popitem

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.XYcurve.XYcurveProperties.setdefault

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.XYcurve.XYcurveProperties.update

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.update
```

````

````{py:method} values()
:canonical: altdss.XYcurve.XYcurveProperties.values

```{autodoc2-docstring} altdss.XYcurve.XYcurveProperties.values
```

````

`````
