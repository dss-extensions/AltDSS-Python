# {py:mod}`altdss.Batch`

```{py:module} altdss.Batch
```

```{autodoc2-docstring} altdss.Batch
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BatchCommon <altdss.Batch.BatchCommon>`
  - ```{autodoc2-docstring} altdss.Batch.BatchCommon
    :summary:
    ```
* - {py:obj}`DSSBatch <altdss.Batch.DSSBatch>`
  - ```{autodoc2-docstring} altdss.Batch.DSSBatch
    :summary:
    ```
* - {py:obj}`NonUniformBatch <altdss.Batch.NonUniformBatch>`
  - ```{autodoc2-docstring} altdss.Batch.NonUniformBatch
    :summary:
    ```
````

### API

`````{py:class} BatchCommon
:canonical: altdss.Batch.BatchCommon

```{autodoc2-docstring} altdss.Batch.BatchCommon
```

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Batch.BatchCommon.FullName

```{autodoc2-docstring} altdss.Batch.BatchCommon.FullName
```

````

````{py:property} Name
:canonical: altdss.Batch.BatchCommon.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Batch.BatchCommon.Name
```

````

````{py:method} __call__()
:canonical: altdss.Batch.BatchCommon.__call__

```{autodoc2-docstring} altdss.Batch.BatchCommon.__call__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Batch.BatchCommon.__len__

```{autodoc2-docstring} altdss.Batch.BatchCommon.__len__
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Batch.BatchCommon.to_json

```{autodoc2-docstring} altdss.Batch.BatchCommon.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Batch.BatchCommon.to_list

```{autodoc2-docstring} altdss.Batch.BatchCommon.to_list
```

````

`````

`````{py:class} DSSBatch(api_util, **kwargs)
:canonical: altdss.Batch.DSSBatch

Bases: {py:obj}`altdss.common.Base`, {py:obj}`altdss.Batch.BatchCommon`

```{autodoc2-docstring} altdss.Batch.DSSBatch
```

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Batch.DSSBatch.FullName

```{autodoc2-docstring} altdss.Batch.DSSBatch.FullName
```

````

````{py:property} Name
:canonical: altdss.Batch.DSSBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Batch.DSSBatch.Name
```

````

````{py:method} __call__()
:canonical: altdss.Batch.DSSBatch.__call__

```{autodoc2-docstring} altdss.Batch.DSSBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Batch.DSSBatch.__getitem__

```{autodoc2-docstring} altdss.Batch.DSSBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Batch.DSSBatch.__init__

```{autodoc2-docstring} altdss.Batch.DSSBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Batch.DSSBatch.__iter__

```{autodoc2-docstring} altdss.Batch.DSSBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Batch.DSSBatch.__len__

```{autodoc2-docstring} altdss.Batch.DSSBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Batch.DSSBatch.begin_edit

```{autodoc2-docstring} altdss.Batch.DSSBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Batch.DSSBatch.end_edit

```{autodoc2-docstring} altdss.Batch.DSSBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Batch.DSSBatch.to_json

```{autodoc2-docstring} altdss.Batch.DSSBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Batch.DSSBatch.to_list

```{autodoc2-docstring} altdss.Batch.DSSBatch.to_list
```

````

`````

`````{py:class} NonUniformBatch(func, parent, pycls=None, copy_safe=False, sync_cls_idx=None)
:canonical: altdss.Batch.NonUniformBatch

Bases: {py:obj}`altdss.common.Base`, {py:obj}`altdss.Batch.BatchCommon`

```{autodoc2-docstring} altdss.Batch.NonUniformBatch
```

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Batch.NonUniformBatch.FullName

```{autodoc2-docstring} altdss.Batch.NonUniformBatch.FullName
```

````

````{py:property} Name
:canonical: altdss.Batch.NonUniformBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Batch.NonUniformBatch.Name
```

````

````{py:method} __call__()
:canonical: altdss.Batch.NonUniformBatch.__call__

```{autodoc2-docstring} altdss.Batch.NonUniformBatch.__call__
```

````

````{py:method} __init__(func, parent, pycls=None, copy_safe=False, sync_cls_idx=None)
:canonical: altdss.Batch.NonUniformBatch.__init__

```{autodoc2-docstring} altdss.Batch.NonUniformBatch.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[altdss.DSSObj.DSSObj]
:canonical: altdss.Batch.NonUniformBatch.__iter__

```{autodoc2-docstring} altdss.Batch.NonUniformBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Batch.NonUniformBatch.__len__

```{autodoc2-docstring} altdss.Batch.NonUniformBatch.__len__
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Batch.NonUniformBatch.to_json

```{autodoc2-docstring} altdss.Batch.NonUniformBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Batch.NonUniformBatch.to_list

```{autodoc2-docstring} altdss.Batch.NonUniformBatch.to_list
```

````

`````
