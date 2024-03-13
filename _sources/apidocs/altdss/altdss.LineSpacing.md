# {py:mod}`altdss.LineSpacing`

```{py:module} altdss.LineSpacing
```

```{autodoc2-docstring} altdss.LineSpacing
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ILineSpacing <altdss.LineSpacing.ILineSpacing>`
  - ```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing
    :summary:
    ```
* - {py:obj}`LineSpacing <altdss.LineSpacing.LineSpacing>`
  - ```{autodoc2-docstring} altdss.LineSpacing.LineSpacing
    :summary:
    ```
* - {py:obj}`LineSpacingBatch <altdss.LineSpacing.LineSpacingBatch>`
  - ```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch
    :summary:
    ```
* - {py:obj}`LineSpacingBatchProperties <altdss.LineSpacing.LineSpacingBatchProperties>`
  - ```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties
    :summary:
    ```
* - {py:obj}`LineSpacingProperties <altdss.LineSpacing.LineSpacingProperties>`
  - ```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties
    :summary:
    ```
````

### API

`````{py:class} ILineSpacing(iobj)
:canonical: altdss.LineSpacing.ILineSpacing

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.LineSpacing.LineSpacingBatch`

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing
```

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.LineSpacing.ILineSpacing.FullName

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.FullName
```

````

````{py:attribute} H
:canonical: altdss.LineSpacing.ILineSpacing.H
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.H
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LineSpacing.ILineSpacing.Like

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.Like
```

````

````{py:attribute} NConds
:canonical: altdss.LineSpacing.ILineSpacing.NConds
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineSpacing.ILineSpacing.NPhases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.NPhases
```

````

````{py:property} Name
:canonical: altdss.LineSpacing.ILineSpacing.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.Name
```

````

````{py:attribute} Units
:canonical: altdss.LineSpacing.ILineSpacing.Units
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.LineSpacing.ILineSpacing.Units_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.Units_str
```

````

````{py:attribute} X
:canonical: altdss.LineSpacing.ILineSpacing.X
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.X
```

````

````{py:method} __call__()
:canonical: altdss.LineSpacing.ILineSpacing.__call__

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.LineSpacing.ILineSpacing.__contains__

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.LineSpacing.ILineSpacing.__getitem__

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.LineSpacing.ILineSpacing.__init__

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.LineSpacing.ILineSpacing.__iter__

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.LineSpacing.ILineSpacing.__len__

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.LineSpacing.ILineSpacing.batch

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.LineSpacing.LineSpacingBatchProperties]) -> altdss.LineSpacing.LineSpacingBatch
:canonical: altdss.LineSpacing.ILineSpacing.batch_new

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LineSpacing.ILineSpacing.begin_edit

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LineSpacing.ILineSpacing.end_edit

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.LineSpacing.ILineSpacing.find

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.LineSpacing.LineSpacingProperties]) -> altdss.LineSpacing.LineSpacing
:canonical: altdss.LineSpacing.ILineSpacing.new

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LineSpacing.ILineSpacing.to_json

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.to_json
```

````

````{py:method} to_list()
:canonical: altdss.LineSpacing.ILineSpacing.to_list

```{autodoc2-docstring} altdss.LineSpacing.ILineSpacing.to_list
```

````

`````

`````{py:class} LineSpacing(api_util, ptr)
:canonical: altdss.LineSpacing.LineSpacing

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing
```

````{py:method} FullName() -> str
:canonical: altdss.LineSpacing.LineSpacing.FullName

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.FullName
```

````

````{py:attribute} H
:canonical: altdss.LineSpacing.LineSpacing.H
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.H
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.LineSpacing.LineSpacing.Like

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.Like
```

````

````{py:attribute} NConds
:canonical: altdss.LineSpacing.LineSpacing.NConds
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineSpacing.LineSpacing.NPhases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.NPhases
```

````

````{py:property} Name
:canonical: altdss.LineSpacing.LineSpacing.Name
:type: str

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.Name
```

````

````{py:attribute} Units
:canonical: altdss.LineSpacing.LineSpacing.Units
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.LineSpacing.LineSpacing.Units_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.Units_str
```

````

````{py:attribute} X
:canonical: altdss.LineSpacing.LineSpacing.X
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.X
```

````

````{py:method} __hash__()
:canonical: altdss.LineSpacing.LineSpacing.__hash__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.LineSpacing.LineSpacing.__init__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.LineSpacing.LineSpacing.__ne__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.LineSpacing.LineSpacing.__repr__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LineSpacing.LineSpacing.begin_edit

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LineSpacing.LineSpacing.end_edit

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LineSpacing.LineSpacing.to_json

```{autodoc2-docstring} altdss.LineSpacing.LineSpacing.to_json
```

````

`````

`````{py:class} LineSpacingBatch(api_util, **kwargs)
:canonical: altdss.LineSpacing.LineSpacingBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch
```

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.LineSpacing.LineSpacingBatch.FullName

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.FullName
```

````

````{py:attribute} H
:canonical: altdss.LineSpacing.LineSpacingBatch.H
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.H
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LineSpacing.LineSpacingBatch.Like

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.Like
```

````

````{py:attribute} NConds
:canonical: altdss.LineSpacing.LineSpacingBatch.NConds
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineSpacing.LineSpacingBatch.NPhases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.NPhases
```

````

````{py:property} Name
:canonical: altdss.LineSpacing.LineSpacingBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.Name
```

````

````{py:attribute} Units
:canonical: altdss.LineSpacing.LineSpacingBatch.Units
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.LineSpacing.LineSpacingBatch.Units_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.Units_str
```

````

````{py:attribute} X
:canonical: altdss.LineSpacing.LineSpacingBatch.X
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.X
```

````

````{py:method} __call__()
:canonical: altdss.LineSpacing.LineSpacingBatch.__call__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.LineSpacing.LineSpacingBatch.__getitem__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.LineSpacing.LineSpacingBatch.__init__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.LineSpacing.LineSpacingBatch.__iter__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.LineSpacing.LineSpacingBatch.__len__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.LineSpacing.LineSpacingBatch.batch

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LineSpacing.LineSpacingBatch.begin_edit

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LineSpacing.LineSpacingBatch.end_edit

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LineSpacing.LineSpacingBatch.to_json

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.LineSpacing.LineSpacingBatch.to_list

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatch.to_list
```

````

`````

`````{py:class} LineSpacingBatchProperties()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties
```

````{py:attribute} H
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.H
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.H
```

````

````{py:attribute} Like
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.Like
```

````

````{py:attribute} NConds
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.NConds
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.NPhases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.NPhases
```

````

````{py:attribute} Units
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.Units
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.Units
```

````

````{py:attribute} X
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.X
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.X
```

````

````{py:method} __contains__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__contains__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__delattr__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__delitem__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__dir__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__format__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__ge__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__getitem__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__getstate__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__gt__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__init__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__ior__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__iter__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__le__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__len__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__lt__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__ne__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__new__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__or__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__reduce__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__repr__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__reversed__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__ror__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__setitem__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__str__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.clear

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.copy

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.get

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.items

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.keys

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.pop

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.popitem

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.setdefault

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.update

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.LineSpacing.LineSpacingBatchProperties.values

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingBatchProperties.values
```

````

`````

`````{py:class} LineSpacingProperties()
:canonical: altdss.LineSpacing.LineSpacingProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties
```

````{py:attribute} H
:canonical: altdss.LineSpacing.LineSpacingProperties.H
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.H
```

````

````{py:attribute} Like
:canonical: altdss.LineSpacing.LineSpacingProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.Like
```

````

````{py:attribute} NConds
:canonical: altdss.LineSpacing.LineSpacingProperties.NConds
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineSpacing.LineSpacingProperties.NPhases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.NPhases
```

````

````{py:attribute} Units
:canonical: altdss.LineSpacing.LineSpacingProperties.Units
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.Units
```

````

````{py:attribute} X
:canonical: altdss.LineSpacing.LineSpacingProperties.X
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.X
```

````

````{py:method} __contains__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__contains__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__delattr__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__delitem__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__dir__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__format__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__ge__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__getattribute__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__getitem__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__getstate__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__gt__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__init__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__ior__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__iter__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__le__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__len__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__lt__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__ne__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__new__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__or__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__reduce__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__reduce_ex__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__repr__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__reversed__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__ror__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__setitem__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__sizeof__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__str__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.LineSpacing.LineSpacingProperties.__subclasshook__

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.LineSpacing.LineSpacingProperties.clear

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.LineSpacing.LineSpacingProperties.copy

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.copy
```

````

````{py:method} get()
:canonical: altdss.LineSpacing.LineSpacingProperties.get

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.get
```

````

````{py:method} items()
:canonical: altdss.LineSpacing.LineSpacingProperties.items

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.items
```

````

````{py:method} keys()
:canonical: altdss.LineSpacing.LineSpacingProperties.keys

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.LineSpacing.LineSpacingProperties.pop

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.LineSpacing.LineSpacingProperties.popitem

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.LineSpacing.LineSpacingProperties.setdefault

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.LineSpacing.LineSpacingProperties.update

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.update
```

````

````{py:method} values()
:canonical: altdss.LineSpacing.LineSpacingProperties.values

```{autodoc2-docstring} altdss.LineSpacing.LineSpacingProperties.values
```

````

`````
