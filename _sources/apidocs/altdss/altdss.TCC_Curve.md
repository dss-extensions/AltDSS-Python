# {py:mod}`altdss.TCC_Curve`

```{py:module} altdss.TCC_Curve
```

```{autodoc2-docstring} altdss.TCC_Curve
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ITCC_Curve <altdss.TCC_Curve.ITCC_Curve>`
  - ```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve
    :summary:
    ```
* - {py:obj}`TCC_Curve <altdss.TCC_Curve.TCC_Curve>`
  - ```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve
    :summary:
    ```
* - {py:obj}`TCC_CurveBatch <altdss.TCC_Curve.TCC_CurveBatch>`
  - ```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch
    :summary:
    ```
* - {py:obj}`TCC_CurveBatchProperties <altdss.TCC_Curve.TCC_CurveBatchProperties>`
  - ```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties
    :summary:
    ```
* - {py:obj}`TCC_CurveProperties <altdss.TCC_Curve.TCC_CurveProperties>`
  - ```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties
    :summary:
    ```
````

### API

`````{py:class} ITCC_Curve(iobj)
:canonical: altdss.TCC_Curve.ITCC_Curve

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.TCC_Curve.TCC_CurveBatch`

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve
```

````{py:attribute} C_Array
:canonical: altdss.TCC_Curve.ITCC_Curve.C_Array
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.C_Array
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.TCC_Curve.ITCC_Curve.FullName

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.FullName
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TCC_Curve.ITCC_Curve.Like

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.Like
```

````

````{py:attribute} NPts
:canonical: altdss.TCC_Curve.ITCC_Curve.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.NPts
```

````

````{py:property} Name
:canonical: altdss.TCC_Curve.ITCC_Curve.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.Name
```

````

````{py:attribute} T_Array
:canonical: altdss.TCC_Curve.ITCC_Curve.T_Array
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.T_Array
```

````

````{py:method} __call__()
:canonical: altdss.TCC_Curve.ITCC_Curve.__call__

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.TCC_Curve.ITCC_Curve.__contains__

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.TCC_Curve.ITCC_Curve.__getitem__

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.TCC_Curve.ITCC_Curve.__init__

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.TCC_Curve.ITCC_Curve.__iter__

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.TCC_Curve.ITCC_Curve.__len__

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.TCC_Curve.ITCC_Curve.batch

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.TCC_Curve.TCC_CurveBatchProperties]) -> altdss.TCC_Curve.TCC_CurveBatch
:canonical: altdss.TCC_Curve.ITCC_Curve.batch_new

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.TCC_Curve.ITCC_Curve.begin_edit

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.TCC_Curve.ITCC_Curve.end_edit

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.TCC_Curve.ITCC_Curve.find

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.TCC_Curve.TCC_CurveProperties]) -> altdss.TCC_Curve.TCC_Curve
:canonical: altdss.TCC_Curve.ITCC_Curve.new

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.TCC_Curve.ITCC_Curve.to_json

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.to_json
```

````

````{py:method} to_list()
:canonical: altdss.TCC_Curve.ITCC_Curve.to_list

```{autodoc2-docstring} altdss.TCC_Curve.ITCC_Curve.to_list
```

````

`````

`````{py:class} TCC_Curve(api_util, ptr)
:canonical: altdss.TCC_Curve.TCC_Curve

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve
```

````{py:attribute} C_Array
:canonical: altdss.TCC_Curve.TCC_Curve.C_Array
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.C_Array
```

````

````{py:method} FullName() -> str
:canonical: altdss.TCC_Curve.TCC_Curve.FullName

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.FullName
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.TCC_Curve.TCC_Curve.Like

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.Like
```

````

````{py:attribute} NPts
:canonical: altdss.TCC_Curve.TCC_Curve.NPts
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.NPts
```

````

````{py:property} Name
:canonical: altdss.TCC_Curve.TCC_Curve.Name
:type: str

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.Name
```

````

````{py:attribute} T_Array
:canonical: altdss.TCC_Curve.TCC_Curve.T_Array
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.T_Array
```

````

````{py:method} __hash__()
:canonical: altdss.TCC_Curve.TCC_Curve.__hash__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.TCC_Curve.TCC_Curve.__init__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.TCC_Curve.TCC_Curve.__ne__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.TCC_Curve.TCC_Curve.__repr__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.TCC_Curve.TCC_Curve.begin_edit

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.TCC_Curve.TCC_Curve.end_edit

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.TCC_Curve.TCC_Curve.to_json

```{autodoc2-docstring} altdss.TCC_Curve.TCC_Curve.to_json
```

````

`````

`````{py:class} TCC_CurveBatch(api_util, **kwargs)
:canonical: altdss.TCC_Curve.TCC_CurveBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch
```

````{py:attribute} C_Array
:canonical: altdss.TCC_Curve.TCC_CurveBatch.C_Array
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.C_Array
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.TCC_Curve.TCC_CurveBatch.FullName

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.FullName
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TCC_Curve.TCC_CurveBatch.Like

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.Like
```

````

````{py:attribute} NPts
:canonical: altdss.TCC_Curve.TCC_CurveBatch.NPts
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.NPts
```

````

````{py:property} Name
:canonical: altdss.TCC_Curve.TCC_CurveBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.Name
```

````

````{py:attribute} T_Array
:canonical: altdss.TCC_Curve.TCC_CurveBatch.T_Array
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.T_Array
```

````

````{py:method} __call__()
:canonical: altdss.TCC_Curve.TCC_CurveBatch.__call__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.TCC_Curve.TCC_CurveBatch.__getitem__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.TCC_Curve.TCC_CurveBatch.__init__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.TCC_Curve.TCC_CurveBatch.__iter__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.TCC_Curve.TCC_CurveBatch.__len__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.TCC_Curve.TCC_CurveBatch.batch

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.TCC_Curve.TCC_CurveBatch.begin_edit

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.TCC_Curve.TCC_CurveBatch.end_edit

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.TCC_Curve.TCC_CurveBatch.to_json

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.TCC_Curve.TCC_CurveBatch.to_list

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatch.to_list
```

````

`````

`````{py:class} TCC_CurveBatchProperties()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties
```

````{py:attribute} C_Array
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.C_Array
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.C_Array
```

````

````{py:attribute} Like
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.Like
```

````

````{py:attribute} NPts
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.NPts
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.NPts
```

````

````{py:attribute} T_Array
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.T_Array
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.T_Array
```

````

````{py:method} __contains__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__contains__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__delattr__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__delitem__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__dir__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__format__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__ge__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__getitem__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__getstate__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__gt__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__init__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__ior__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__iter__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__le__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__len__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__lt__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__ne__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__new__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__or__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__reduce__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__repr__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__reversed__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__ror__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__setitem__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__str__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.clear

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.copy

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.get

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.items

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.keys

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.pop

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.popitem

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.setdefault

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.update

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.TCC_Curve.TCC_CurveBatchProperties.values

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveBatchProperties.values
```

````

`````

`````{py:class} TCC_CurveProperties()
:canonical: altdss.TCC_Curve.TCC_CurveProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties
```

````{py:attribute} C_Array
:canonical: altdss.TCC_Curve.TCC_CurveProperties.C_Array
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.C_Array
```

````

````{py:attribute} Like
:canonical: altdss.TCC_Curve.TCC_CurveProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.Like
```

````

````{py:attribute} NPts
:canonical: altdss.TCC_Curve.TCC_CurveProperties.NPts
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.NPts
```

````

````{py:attribute} T_Array
:canonical: altdss.TCC_Curve.TCC_CurveProperties.T_Array
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.T_Array
```

````

````{py:method} __contains__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__contains__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__delattr__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__delitem__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__dir__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__format__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__ge__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__getattribute__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__getitem__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__getstate__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__gt__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__init__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__ior__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__iter__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__le__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__len__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__lt__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__ne__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__new__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__or__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__reduce__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__reduce_ex__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__repr__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__reversed__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__ror__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__setitem__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__sizeof__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__str__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.__subclasshook__

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.clear

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.copy

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.copy
```

````

````{py:method} get()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.get

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.get
```

````

````{py:method} items()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.items

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.items
```

````

````{py:method} keys()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.keys

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.pop

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.popitem

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.setdefault

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.update

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.update
```

````

````{py:method} values()
:canonical: altdss.TCC_Curve.TCC_CurveProperties.values

```{autodoc2-docstring} altdss.TCC_Curve.TCC_CurveProperties.values
```

````

`````
