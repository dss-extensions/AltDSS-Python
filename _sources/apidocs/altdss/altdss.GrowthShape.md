# {py:mod}`altdss.GrowthShape`

```{py:module} altdss.GrowthShape
```

```{autodoc2-docstring} altdss.GrowthShape
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GrowthShape <altdss.GrowthShape.GrowthShape>`
  - ```{autodoc2-docstring} altdss.GrowthShape.GrowthShape
    :summary:
    ```
* - {py:obj}`GrowthShapeBatch <altdss.GrowthShape.GrowthShapeBatch>`
  - ```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch
    :summary:
    ```
* - {py:obj}`GrowthShapeBatchProperties <altdss.GrowthShape.GrowthShapeBatchProperties>`
  - ```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties
    :summary:
    ```
* - {py:obj}`GrowthShapeProperties <altdss.GrowthShape.GrowthShapeProperties>`
  - ```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties
    :summary:
    ```
* - {py:obj}`IGrowthShape <altdss.GrowthShape.IGrowthShape>`
  - ```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape
    :summary:
    ```
````

### API

`````{py:class} GrowthShape(api_util, ptr)
:canonical: altdss.GrowthShape.GrowthShape

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape
```

````{py:attribute} CSVFile
:canonical: altdss.GrowthShape.GrowthShape.CSVFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.GrowthShape.GrowthShape.DblFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.DblFile
```

````

````{py:method} FullName() -> str
:canonical: altdss.GrowthShape.GrowthShape.FullName

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.FullName
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.GrowthShape.GrowthShape.Like

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.Like
```

````

````{py:attribute} Mult
:canonical: altdss.GrowthShape.GrowthShape.Mult
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.Mult
```

````

````{py:attribute} NPts
:canonical: altdss.GrowthShape.GrowthShape.NPts
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.NPts
```

````

````{py:property} Name
:canonical: altdss.GrowthShape.GrowthShape.Name
:type: str

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.Name
```

````

````{py:attribute} SngFile
:canonical: altdss.GrowthShape.GrowthShape.SngFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.SngFile
```

````

````{py:attribute} Year
:canonical: altdss.GrowthShape.GrowthShape.Year
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.Year
```

````

````{py:method} __hash__()
:canonical: altdss.GrowthShape.GrowthShape.__hash__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.GrowthShape.GrowthShape.__init__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.GrowthShape.GrowthShape.__ne__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.GrowthShape.GrowthShape.__repr__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GrowthShape.GrowthShape.begin_edit

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.GrowthShape.GrowthShapeProperties]) -> altdss.GrowthShape.GrowthShape
:canonical: altdss.GrowthShape.GrowthShape.edit

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GrowthShape.GrowthShape.end_edit

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GrowthShape.GrowthShape.to_json

```{autodoc2-docstring} altdss.GrowthShape.GrowthShape.to_json
```

````

`````

`````{py:class} GrowthShapeBatch(api_util, **kwargs)
:canonical: altdss.GrowthShape.GrowthShapeBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch
```

````{py:attribute} CSVFile
:canonical: altdss.GrowthShape.GrowthShapeBatch.CSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.GrowthShape.GrowthShapeBatch.DblFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.DblFile
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GrowthShape.GrowthShapeBatch.FullName

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.FullName
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GrowthShape.GrowthShapeBatch.Like

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.Like
```

````

````{py:attribute} Mult
:canonical: altdss.GrowthShape.GrowthShapeBatch.Mult
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.Mult
```

````

````{py:attribute} NPts
:canonical: altdss.GrowthShape.GrowthShapeBatch.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.NPts
```

````

````{py:property} Name
:canonical: altdss.GrowthShape.GrowthShapeBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.Name
```

````

````{py:attribute} SngFile
:canonical: altdss.GrowthShape.GrowthShapeBatch.SngFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.SngFile
```

````

````{py:attribute} Year
:canonical: altdss.GrowthShape.GrowthShapeBatch.Year
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.Year
```

````

````{py:method} __call__()
:canonical: altdss.GrowthShape.GrowthShapeBatch.__call__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.GrowthShape.GrowthShapeBatch.__getitem__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.GrowthShape.GrowthShapeBatch.__init__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GrowthShape.GrowthShapeBatch.__iter__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GrowthShape.GrowthShapeBatch.__len__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.GrowthShape.GrowthShapeBatch.batch

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GrowthShape.GrowthShapeBatch.begin_edit

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.GrowthShape.GrowthShapeBatchProperties]) -> altdss.GrowthShape.GrowthShapeBatch
:canonical: altdss.GrowthShape.GrowthShapeBatch.edit

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GrowthShape.GrowthShapeBatch.end_edit

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GrowthShape.GrowthShapeBatch.to_json

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GrowthShape.GrowthShapeBatch.to_list

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatch.to_list
```

````

`````

`````{py:class} GrowthShapeBatchProperties()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties
```

````{py:attribute} CSVFile
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.CSVFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.DblFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.DblFile
```

````

````{py:attribute} Like
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.Like
```

````

````{py:attribute} Mult
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.Mult
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.Mult
```

````

````{py:attribute} NPts
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.NPts
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.NPts
```

````

````{py:attribute} SngFile
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.SngFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.SngFile
```

````

````{py:attribute} Year
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.Year
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.Year
```

````

````{py:method} __contains__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__contains__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__delattr__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__delitem__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__dir__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__format__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__ge__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__getitem__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__getstate__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__gt__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__init__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__ior__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__iter__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__le__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__len__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__lt__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__ne__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__new__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__or__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__reduce__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__repr__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__reversed__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__ror__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__setitem__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__str__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.clear

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.copy

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.get

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.items

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.keys

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.pop

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.popitem

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.setdefault

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.update

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.GrowthShape.GrowthShapeBatchProperties.values

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeBatchProperties.values
```

````

`````

`````{py:class} GrowthShapeProperties()
:canonical: altdss.GrowthShape.GrowthShapeProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties
```

````{py:attribute} CSVFile
:canonical: altdss.GrowthShape.GrowthShapeProperties.CSVFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.GrowthShape.GrowthShapeProperties.DblFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.DblFile
```

````

````{py:attribute} Like
:canonical: altdss.GrowthShape.GrowthShapeProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.Like
```

````

````{py:attribute} Mult
:canonical: altdss.GrowthShape.GrowthShapeProperties.Mult
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.Mult
```

````

````{py:attribute} NPts
:canonical: altdss.GrowthShape.GrowthShapeProperties.NPts
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.NPts
```

````

````{py:attribute} SngFile
:canonical: altdss.GrowthShape.GrowthShapeProperties.SngFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.SngFile
```

````

````{py:attribute} Year
:canonical: altdss.GrowthShape.GrowthShapeProperties.Year
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.Year
```

````

````{py:method} __contains__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__contains__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__delattr__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__delitem__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__dir__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__format__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__ge__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__getattribute__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__getitem__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__getstate__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__gt__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__init__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__ior__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__iter__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__le__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__len__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__lt__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__ne__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__new__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__or__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__reduce__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__reduce_ex__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__repr__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__reversed__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__ror__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__setitem__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__sizeof__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__str__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.GrowthShape.GrowthShapeProperties.__subclasshook__

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.GrowthShape.GrowthShapeProperties.clear

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.GrowthShape.GrowthShapeProperties.copy

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.copy
```

````

````{py:method} get()
:canonical: altdss.GrowthShape.GrowthShapeProperties.get

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.get
```

````

````{py:method} items()
:canonical: altdss.GrowthShape.GrowthShapeProperties.items

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.items
```

````

````{py:method} keys()
:canonical: altdss.GrowthShape.GrowthShapeProperties.keys

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.GrowthShape.GrowthShapeProperties.pop

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.GrowthShape.GrowthShapeProperties.popitem

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.GrowthShape.GrowthShapeProperties.setdefault

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.GrowthShape.GrowthShapeProperties.update

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.update
```

````

````{py:method} values()
:canonical: altdss.GrowthShape.GrowthShapeProperties.values

```{autodoc2-docstring} altdss.GrowthShape.GrowthShapeProperties.values
```

````

`````

`````{py:class} IGrowthShape(iobj)
:canonical: altdss.GrowthShape.IGrowthShape

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.GrowthShape.GrowthShapeBatch`

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape
```

````{py:attribute} CSVFile
:canonical: altdss.GrowthShape.IGrowthShape.CSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.CSVFile
```

````

````{py:attribute} DblFile
:canonical: altdss.GrowthShape.IGrowthShape.DblFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.DblFile
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.GrowthShape.IGrowthShape.FullName

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.FullName
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.GrowthShape.IGrowthShape.Like

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.Like
```

````

````{py:attribute} Mult
:canonical: altdss.GrowthShape.IGrowthShape.Mult
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.Mult
```

````

````{py:attribute} NPts
:canonical: altdss.GrowthShape.IGrowthShape.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.NPts
```

````

````{py:property} Name
:canonical: altdss.GrowthShape.IGrowthShape.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.Name
```

````

````{py:attribute} SngFile
:canonical: altdss.GrowthShape.IGrowthShape.SngFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.SngFile
```

````

````{py:attribute} Year
:canonical: altdss.GrowthShape.IGrowthShape.Year
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.Year
```

````

````{py:method} __call__()
:canonical: altdss.GrowthShape.IGrowthShape.__call__

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.GrowthShape.IGrowthShape.__contains__

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.GrowthShape.IGrowthShape.__getitem__

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.GrowthShape.IGrowthShape.__init__

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.GrowthShape.IGrowthShape.__iter__

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.GrowthShape.IGrowthShape.__len__

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.GrowthShape.IGrowthShape.batch

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.GrowthShape.GrowthShapeBatchProperties]) -> altdss.GrowthShape.GrowthShapeBatch
:canonical: altdss.GrowthShape.IGrowthShape.batch_new

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.GrowthShape.IGrowthShape.begin_edit

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.GrowthShape.GrowthShapeBatchProperties]) -> altdss.GrowthShape.GrowthShapeBatch
:canonical: altdss.GrowthShape.IGrowthShape.edit

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.GrowthShape.IGrowthShape.end_edit

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.GrowthShape.IGrowthShape.find

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.find
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.GrowthShape.GrowthShapeProperties]) -> altdss.GrowthShape.GrowthShape
:canonical: altdss.GrowthShape.IGrowthShape.new

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.GrowthShape.IGrowthShape.to_json

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.to_json
```

````

````{py:method} to_list()
:canonical: altdss.GrowthShape.IGrowthShape.to_list

```{autodoc2-docstring} altdss.GrowthShape.IGrowthShape.to_list
```

````

`````
