# {py:mod}`altdss.DynamicExp`

```{py:module} altdss.DynamicExp
```

```{autodoc2-docstring} altdss.DynamicExp
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DynamicExp <altdss.DynamicExp.DynamicExp>`
  - ```{autodoc2-docstring} altdss.DynamicExp.DynamicExp
    :summary:
    ```
* - {py:obj}`DynamicExpBatch <altdss.DynamicExp.DynamicExpBatch>`
  - ```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch
    :summary:
    ```
* - {py:obj}`DynamicExpBatchProperties <altdss.DynamicExp.DynamicExpBatchProperties>`
  - ```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties
    :summary:
    ```
* - {py:obj}`DynamicExpProperties <altdss.DynamicExp.DynamicExpProperties>`
  - ```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties
    :summary:
    ```
* - {py:obj}`IDynamicExp <altdss.DynamicExp.IDynamicExp>`
  - ```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp
    :summary:
    ```
````

### API

`````{py:class} DynamicExp(api_util, ptr)
:canonical: altdss.DynamicExp.DynamicExp

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp
```

````{py:attribute} Domain
:canonical: altdss.DynamicExp.DynamicExp.Domain
:type: altdss.enums.DynamicExpDomain
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.Domain
```

````

````{py:attribute} Domain_str
:canonical: altdss.DynamicExp.DynamicExp.Domain_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.Domain_str
```

````

````{py:attribute} Expression
:canonical: altdss.DynamicExp.DynamicExp.Expression
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.Expression
```

````

````{py:method} FullName() -> str
:canonical: altdss.DynamicExp.DynamicExp.FullName

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.FullName
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.DynamicExp.DynamicExp.Like

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.Like
```

````

````{py:attribute} NVariables
:canonical: altdss.DynamicExp.DynamicExp.NVariables
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.NVariables
```

````

````{py:property} Name
:canonical: altdss.DynamicExp.DynamicExp.Name
:type: str

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.Name
```

````

````{py:attribute} Var
:canonical: altdss.DynamicExp.DynamicExp.Var
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.Var
```

````

````{py:attribute} VarIdx
:canonical: altdss.DynamicExp.DynamicExp.VarIdx
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.VarIdx
```

````

````{py:attribute} VarNames
:canonical: altdss.DynamicExp.DynamicExp.VarNames
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.VarNames
```

````

````{py:method} __hash__()
:canonical: altdss.DynamicExp.DynamicExp.__hash__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.DynamicExp.DynamicExp.__init__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.DynamicExp.DynamicExp.__ne__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.DynamicExp.DynamicExp.__repr__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.DynamicExp.DynamicExp.begin_edit

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.DynamicExp.DynamicExp.end_edit

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.DynamicExp.DynamicExp.to_json

```{autodoc2-docstring} altdss.DynamicExp.DynamicExp.to_json
```

````

`````

`````{py:class} DynamicExpBatch(api_util, **kwargs)
:canonical: altdss.DynamicExp.DynamicExpBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch
```

````{py:attribute} Domain
:canonical: altdss.DynamicExp.DynamicExpBatch.Domain
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.Domain
```

````

````{py:attribute} Domain_str
:canonical: altdss.DynamicExp.DynamicExpBatch.Domain_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.Domain_str
```

````

````{py:attribute} Expression
:canonical: altdss.DynamicExp.DynamicExpBatch.Expression
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.Expression
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.DynamicExp.DynamicExpBatch.FullName

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.FullName
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.DynamicExp.DynamicExpBatch.Like

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.Like
```

````

````{py:attribute} NVariables
:canonical: altdss.DynamicExp.DynamicExpBatch.NVariables
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.NVariables
```

````

````{py:property} Name
:canonical: altdss.DynamicExp.DynamicExpBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.Name
```

````

````{py:attribute} Var
:canonical: altdss.DynamicExp.DynamicExpBatch.Var
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.Var
```

````

````{py:attribute} VarIdx
:canonical: altdss.DynamicExp.DynamicExpBatch.VarIdx
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.VarIdx
```

````

````{py:attribute} VarNames
:canonical: altdss.DynamicExp.DynamicExpBatch.VarNames
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.VarNames
```

````

````{py:method} __call__()
:canonical: altdss.DynamicExp.DynamicExpBatch.__call__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.DynamicExp.DynamicExpBatch.__getitem__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.DynamicExp.DynamicExpBatch.__init__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.DynamicExp.DynamicExpBatch.__iter__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.DynamicExp.DynamicExpBatch.__len__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.DynamicExp.DynamicExpBatch.batch

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.DynamicExp.DynamicExpBatch.begin_edit

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.DynamicExp.DynamicExpBatch.end_edit

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.DynamicExp.DynamicExpBatch.to_json

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.DynamicExp.DynamicExpBatch.to_list

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatch.to_list
```

````

`````

`````{py:class} DynamicExpBatchProperties()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties
```

````{py:attribute} Domain
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.Domain
:type: typing.Union[typing.AnyStr, int, altdss.enums.DynamicExpDomain, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.DynamicExpDomain], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.Domain
```

````

````{py:attribute} Expression
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.Expression
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.Expression
```

````

````{py:attribute} Like
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.Like
```

````

````{py:attribute} NVariables
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.NVariables
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.NVariables
```

````

````{py:attribute} Var
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.Var
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.Var
```

````

````{py:attribute} VarIdx
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.VarIdx
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.VarIdx
```

````

````{py:attribute} VarNames
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.VarNames
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.VarNames
```

````

````{py:method} __contains__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__contains__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__delattr__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__delitem__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__dir__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__format__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__ge__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__getitem__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__getstate__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__gt__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__init__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__ior__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__iter__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__le__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__len__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__lt__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__ne__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__new__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__or__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__reduce__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__repr__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__reversed__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__ror__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__setitem__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__str__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.clear

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.copy

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.get

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.items

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.keys

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.pop

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.popitem

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.setdefault

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.update

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.DynamicExp.DynamicExpBatchProperties.values

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpBatchProperties.values
```

````

`````

`````{py:class} DynamicExpProperties()
:canonical: altdss.DynamicExp.DynamicExpProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties
```

````{py:attribute} Domain
:canonical: altdss.DynamicExp.DynamicExpProperties.Domain
:type: typing.Union[typing.AnyStr, int, altdss.enums.DynamicExpDomain]
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.Domain
```

````

````{py:attribute} Expression
:canonical: altdss.DynamicExp.DynamicExpProperties.Expression
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.Expression
```

````

````{py:attribute} Like
:canonical: altdss.DynamicExp.DynamicExpProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.Like
```

````

````{py:attribute} NVariables
:canonical: altdss.DynamicExp.DynamicExpProperties.NVariables
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.NVariables
```

````

````{py:attribute} Var
:canonical: altdss.DynamicExp.DynamicExpProperties.Var
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.Var
```

````

````{py:attribute} VarIdx
:canonical: altdss.DynamicExp.DynamicExpProperties.VarIdx
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.VarIdx
```

````

````{py:attribute} VarNames
:canonical: altdss.DynamicExp.DynamicExpProperties.VarNames
:type: typing.List[typing.AnyStr]
:value: >
   None

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.VarNames
```

````

````{py:method} __contains__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__contains__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__delattr__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__delitem__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__dir__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__format__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__ge__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__getattribute__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__getitem__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__getstate__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__gt__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__init__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__ior__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__iter__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__le__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__len__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__lt__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__ne__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__new__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__or__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__reduce__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__reduce_ex__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__repr__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__reversed__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__ror__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__setitem__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__sizeof__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__str__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.DynamicExp.DynamicExpProperties.__subclasshook__

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.DynamicExp.DynamicExpProperties.clear

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.DynamicExp.DynamicExpProperties.copy

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.copy
```

````

````{py:method} get()
:canonical: altdss.DynamicExp.DynamicExpProperties.get

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.get
```

````

````{py:method} items()
:canonical: altdss.DynamicExp.DynamicExpProperties.items

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.items
```

````

````{py:method} keys()
:canonical: altdss.DynamicExp.DynamicExpProperties.keys

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.DynamicExp.DynamicExpProperties.pop

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.DynamicExp.DynamicExpProperties.popitem

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.DynamicExp.DynamicExpProperties.setdefault

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.DynamicExp.DynamicExpProperties.update

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.update
```

````

````{py:method} values()
:canonical: altdss.DynamicExp.DynamicExpProperties.values

```{autodoc2-docstring} altdss.DynamicExp.DynamicExpProperties.values
```

````

`````

`````{py:class} IDynamicExp(iobj)
:canonical: altdss.DynamicExp.IDynamicExp

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.DynamicExp.DynamicExpBatch`

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp
```

````{py:attribute} Domain
:canonical: altdss.DynamicExp.IDynamicExp.Domain
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.Domain
```

````

````{py:attribute} Domain_str
:canonical: altdss.DynamicExp.IDynamicExp.Domain_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.Domain_str
```

````

````{py:attribute} Expression
:canonical: altdss.DynamicExp.IDynamicExp.Expression
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.Expression
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.DynamicExp.IDynamicExp.FullName

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.FullName
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.DynamicExp.IDynamicExp.Like

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.Like
```

````

````{py:attribute} NVariables
:canonical: altdss.DynamicExp.IDynamicExp.NVariables
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.NVariables
```

````

````{py:property} Name
:canonical: altdss.DynamicExp.IDynamicExp.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.Name
```

````

````{py:attribute} Var
:canonical: altdss.DynamicExp.IDynamicExp.Var
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.Var
```

````

````{py:attribute} VarIdx
:canonical: altdss.DynamicExp.IDynamicExp.VarIdx
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.VarIdx
```

````

````{py:attribute} VarNames
:canonical: altdss.DynamicExp.IDynamicExp.VarNames
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.VarNames
```

````

````{py:method} __call__()
:canonical: altdss.DynamicExp.IDynamicExp.__call__

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.DynamicExp.IDynamicExp.__contains__

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.DynamicExp.IDynamicExp.__getitem__

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.DynamicExp.IDynamicExp.__init__

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.DynamicExp.IDynamicExp.__iter__

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.DynamicExp.IDynamicExp.__len__

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.DynamicExp.IDynamicExp.batch

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.DynamicExp.DynamicExpBatchProperties]) -> altdss.DynamicExp.DynamicExpBatch
:canonical: altdss.DynamicExp.IDynamicExp.batch_new

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.DynamicExp.IDynamicExp.begin_edit

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.DynamicExp.IDynamicExp.end_edit

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.DynamicExp.IDynamicExp.find

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.DynamicExp.DynamicExpProperties]) -> altdss.DynamicExp.DynamicExp
:canonical: altdss.DynamicExp.IDynamicExp.new

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.DynamicExp.IDynamicExp.to_json

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.to_json
```

````

````{py:method} to_list()
:canonical: altdss.DynamicExp.IDynamicExp.to_list

```{autodoc2-docstring} altdss.DynamicExp.IDynamicExp.to_list
```

````

`````
