# {py:mod}`altdss.DSSObj`

```{py:module} altdss.DSSObj
```

```{autodoc2-docstring} altdss.DSSObj
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DSSObj <altdss.DSSObj.DSSObj>`
  - ```{autodoc2-docstring} altdss.DSSObj.DSSObj
    :summary:
    ```
* - {py:obj}`IDSSObj <altdss.DSSObj.IDSSObj>`
  - ```{autodoc2-docstring} altdss.DSSObj.IDSSObj
    :summary:
    ```
````

### API

`````{py:class} DSSObj(api_util, ptr)
:canonical: altdss.DSSObj.DSSObj

Bases: {py:obj}`altdss.common.Base`

```{autodoc2-docstring} altdss.DSSObj.DSSObj
```

````{py:method} FullName() -> str
:canonical: altdss.DSSObj.DSSObj.FullName

```{autodoc2-docstring} altdss.DSSObj.DSSObj.FullName
```

````

````{py:property} Name
:canonical: altdss.DSSObj.DSSObj.Name
:type: str

```{autodoc2-docstring} altdss.DSSObj.DSSObj.Name
```

````

````{py:method} __hash__()
:canonical: altdss.DSSObj.DSSObj.__hash__

```{autodoc2-docstring} altdss.DSSObj.DSSObj.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.DSSObj.DSSObj.__init__

```{autodoc2-docstring} altdss.DSSObj.DSSObj.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.DSSObj.DSSObj.__ne__

```{autodoc2-docstring} altdss.DSSObj.DSSObj.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.DSSObj.DSSObj.__repr__

```{autodoc2-docstring} altdss.DSSObj.DSSObj.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.DSSObj.DSSObj.begin_edit

```{autodoc2-docstring} altdss.DSSObj.DSSObj.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.DSSObj.DSSObj.end_edit

```{autodoc2-docstring} altdss.DSSObj.DSSObj.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.DSSObj.DSSObj.to_json

```{autodoc2-docstring} altdss.DSSObj.DSSObj.to_json
```

````

`````

`````{py:class} IDSSObj(iobj, obj_cls, batch_cls)
:canonical: altdss.DSSObj.IDSSObj

Bases: {py:obj}`altdss.common.Base`

```{autodoc2-docstring} altdss.DSSObj.IDSSObj
```

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.DSSObj.IDSSObj.__contains__

```{autodoc2-docstring} altdss.DSSObj.IDSSObj.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.DSSObj.IDSSObj.__getitem__

```{autodoc2-docstring} altdss.DSSObj.IDSSObj.__getitem__
```

````

````{py:method} __init__(iobj, obj_cls, batch_cls)
:canonical: altdss.DSSObj.IDSSObj.__init__

```{autodoc2-docstring} altdss.DSSObj.IDSSObj.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.DSSObj.IDSSObj.__iter__

```{autodoc2-docstring} altdss.DSSObj.IDSSObj.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.DSSObj.IDSSObj.__len__

```{autodoc2-docstring} altdss.DSSObj.IDSSObj.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.DSSObj.IDSSObj.batch

```{autodoc2-docstring} altdss.DSSObj.IDSSObj.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, count: typing.Optional[int] = None, begin_edit=None)
:canonical: altdss.DSSObj.IDSSObj.batch_new

```{autodoc2-docstring} altdss.DSSObj.IDSSObj.batch_new
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.DSSObj.IDSSObj.find

```{autodoc2-docstring} altdss.DSSObj.IDSSObj.find
```

````

````{py:method} new(name: str, begin_edit=True, activate=False)
:canonical: altdss.DSSObj.IDSSObj.new

```{autodoc2-docstring} altdss.DSSObj.IDSSObj.new
```

````

`````
