# {py:mod}`altdss.LineGeometry`

```{py:module} altdss.LineGeometry
```

```{autodoc2-docstring} altdss.LineGeometry
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ILineGeometry <altdss.LineGeometry.ILineGeometry>`
  - ```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry
    :summary:
    ```
* - {py:obj}`LineGeometry <altdss.LineGeometry.LineGeometry>`
  - ```{autodoc2-docstring} altdss.LineGeometry.LineGeometry
    :summary:
    ```
* - {py:obj}`LineGeometryBatch <altdss.LineGeometry.LineGeometryBatch>`
  - ```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch
    :summary:
    ```
* - {py:obj}`LineGeometryBatchProperties <altdss.LineGeometry.LineGeometryBatchProperties>`
  - ```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties
    :summary:
    ```
* - {py:obj}`LineGeometryProperties <altdss.LineGeometry.LineGeometryProperties>`
  - ```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties
    :summary:
    ```
````

### API

`````{py:class} ILineGeometry(iobj)
:canonical: altdss.LineGeometry.ILineGeometry

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.LineGeometry.LineGeometryBatch`

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry
```

````{py:attribute} Conductors
:canonical: altdss.LineGeometry.ILineGeometry.Conductors
:type: typing.List[typing.List[typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Conductors
```

````

````{py:attribute} Conductors_str
:canonical: altdss.LineGeometry.ILineGeometry.Conductors_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Conductors_str
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineGeometry.ILineGeometry.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.EmergAmps
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.LineGeometry.ILineGeometry.FullName

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.FullName
```

````

````{py:attribute} H
:canonical: altdss.LineGeometry.ILineGeometry.H
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.H
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LineGeometry.ILineGeometry.Like

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineGeometry.ILineGeometry.LineType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.LineType
```

````

````{py:attribute} LineType_str
:canonical: altdss.LineGeometry.ILineGeometry.LineType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.LineType_str
```

````

````{py:attribute} NConds
:canonical: altdss.LineGeometry.ILineGeometry.NConds
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineGeometry.ILineGeometry.NPhases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.NPhases
```

````

````{py:property} Name
:canonical: altdss.LineGeometry.ILineGeometry.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineGeometry.ILineGeometry.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.NormAmps
```

````

````{py:attribute} Ratings
:canonical: altdss.LineGeometry.ILineGeometry.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Ratings
```

````

````{py:attribute} Reduce
:canonical: altdss.LineGeometry.ILineGeometry.Reduce
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Reduce
```

````

````{py:attribute} Seasons
:canonical: altdss.LineGeometry.ILineGeometry.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Seasons
```

````

````{py:attribute} Spacing
:canonical: altdss.LineGeometry.ILineGeometry.Spacing
:type: typing.List[altdss.LineSpacing.LineSpacing]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Spacing
```

````

````{py:attribute} Spacing_str
:canonical: altdss.LineGeometry.ILineGeometry.Spacing_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Spacing_str
```

````

````{py:attribute} Units
:canonical: altdss.LineGeometry.ILineGeometry.Units
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.LineGeometry.ILineGeometry.Units_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.Units_str
```

````

````{py:attribute} X
:canonical: altdss.LineGeometry.ILineGeometry.X
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.X
```

````

````{py:method} __call__()
:canonical: altdss.LineGeometry.ILineGeometry.__call__

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.LineGeometry.ILineGeometry.__contains__

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.LineGeometry.ILineGeometry.__getitem__

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.LineGeometry.ILineGeometry.__init__

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.LineGeometry.ILineGeometry.__iter__

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.LineGeometry.ILineGeometry.__len__

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.LineGeometry.ILineGeometry.batch

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.LineGeometry.LineGeometryBatchProperties]) -> altdss.LineGeometry.LineGeometryBatch
:canonical: altdss.LineGeometry.ILineGeometry.batch_new

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LineGeometry.ILineGeometry.begin_edit

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LineGeometry.ILineGeometry.end_edit

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.LineGeometry.ILineGeometry.find

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.LineGeometry.LineGeometryProperties]) -> altdss.LineGeometry.LineGeometry
:canonical: altdss.LineGeometry.ILineGeometry.new

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LineGeometry.ILineGeometry.to_json

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.to_json
```

````

````{py:method} to_list()
:canonical: altdss.LineGeometry.ILineGeometry.to_list

```{autodoc2-docstring} altdss.LineGeometry.ILineGeometry.to_list
```

````

`````

`````{py:class} LineGeometry(api_util, ptr)
:canonical: altdss.LineGeometry.LineGeometry

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry
```

````{py:attribute} Conductors
:canonical: altdss.LineGeometry.LineGeometry.Conductors
:type: typing.List[typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Conductors
```

````

````{py:attribute} Conductors_str
:canonical: altdss.LineGeometry.LineGeometry.Conductors_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Conductors_str
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineGeometry.LineGeometry.EmergAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.EmergAmps
```

````

````{py:method} FullName() -> str
:canonical: altdss.LineGeometry.LineGeometry.FullName

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.FullName
```

````

````{py:attribute} H
:canonical: altdss.LineGeometry.LineGeometry.H
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.H
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.LineGeometry.LineGeometry.Like

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineGeometry.LineGeometry.LineType
:type: altdss.enums.LineType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.LineType
```

````

````{py:attribute} LineType_str
:canonical: altdss.LineGeometry.LineGeometry.LineType_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.LineType_str
```

````

````{py:attribute} NConds
:canonical: altdss.LineGeometry.LineGeometry.NConds
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineGeometry.LineGeometry.NPhases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.NPhases
```

````

````{py:property} Name
:canonical: altdss.LineGeometry.LineGeometry.Name
:type: str

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineGeometry.LineGeometry.NormAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.NormAmps
```

````

````{py:attribute} Ratings
:canonical: altdss.LineGeometry.LineGeometry.Ratings
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Ratings
```

````

````{py:attribute} Reduce
:canonical: altdss.LineGeometry.LineGeometry.Reduce
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Reduce
```

````

````{py:attribute} Seasons
:canonical: altdss.LineGeometry.LineGeometry.Seasons
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Seasons
```

````

````{py:attribute} Spacing
:canonical: altdss.LineGeometry.LineGeometry.Spacing
:type: altdss.LineSpacing.LineSpacing
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Spacing
```

````

````{py:attribute} Spacing_str
:canonical: altdss.LineGeometry.LineGeometry.Spacing_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Spacing_str
```

````

````{py:attribute} Units
:canonical: altdss.LineGeometry.LineGeometry.Units
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.LineGeometry.LineGeometry.Units_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.Units_str
```

````

````{py:attribute} X
:canonical: altdss.LineGeometry.LineGeometry.X
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.X
```

````

````{py:method} __hash__()
:canonical: altdss.LineGeometry.LineGeometry.__hash__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.LineGeometry.LineGeometry.__init__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.LineGeometry.LineGeometry.__ne__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.LineGeometry.LineGeometry.__repr__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LineGeometry.LineGeometry.begin_edit

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LineGeometry.LineGeometry.end_edit

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LineGeometry.LineGeometry.to_json

```{autodoc2-docstring} altdss.LineGeometry.LineGeometry.to_json
```

````

`````

`````{py:class} LineGeometryBatch(api_util, **kwargs)
:canonical: altdss.LineGeometry.LineGeometryBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch
```

````{py:attribute} Conductors
:canonical: altdss.LineGeometry.LineGeometryBatch.Conductors
:type: typing.List[typing.List[typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Conductors
```

````

````{py:attribute} Conductors_str
:canonical: altdss.LineGeometry.LineGeometryBatch.Conductors_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Conductors_str
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineGeometry.LineGeometryBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.EmergAmps
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.LineGeometry.LineGeometryBatch.FullName

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.FullName
```

````

````{py:attribute} H
:canonical: altdss.LineGeometry.LineGeometryBatch.H
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.H
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.LineGeometry.LineGeometryBatch.Like

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineGeometry.LineGeometryBatch.LineType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.LineType
```

````

````{py:attribute} LineType_str
:canonical: altdss.LineGeometry.LineGeometryBatch.LineType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.LineType_str
```

````

````{py:attribute} NConds
:canonical: altdss.LineGeometry.LineGeometryBatch.NConds
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineGeometry.LineGeometryBatch.NPhases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.NPhases
```

````

````{py:property} Name
:canonical: altdss.LineGeometry.LineGeometryBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineGeometry.LineGeometryBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.NormAmps
```

````

````{py:attribute} Ratings
:canonical: altdss.LineGeometry.LineGeometryBatch.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Ratings
```

````

````{py:attribute} Reduce
:canonical: altdss.LineGeometry.LineGeometryBatch.Reduce
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Reduce
```

````

````{py:attribute} Seasons
:canonical: altdss.LineGeometry.LineGeometryBatch.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Seasons
```

````

````{py:attribute} Spacing
:canonical: altdss.LineGeometry.LineGeometryBatch.Spacing
:type: typing.List[altdss.LineSpacing.LineSpacing]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Spacing
```

````

````{py:attribute} Spacing_str
:canonical: altdss.LineGeometry.LineGeometryBatch.Spacing_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Spacing_str
```

````

````{py:attribute} Units
:canonical: altdss.LineGeometry.LineGeometryBatch.Units
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.LineGeometry.LineGeometryBatch.Units_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.Units_str
```

````

````{py:attribute} X
:canonical: altdss.LineGeometry.LineGeometryBatch.X
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.X
```

````

````{py:method} __call__()
:canonical: altdss.LineGeometry.LineGeometryBatch.__call__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.LineGeometry.LineGeometryBatch.__getitem__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.LineGeometry.LineGeometryBatch.__init__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.LineGeometry.LineGeometryBatch.__iter__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.LineGeometry.LineGeometryBatch.__len__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.LineGeometry.LineGeometryBatch.begin_edit

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.LineGeometry.LineGeometryBatch.end_edit

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.LineGeometry.LineGeometryBatch.to_json

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.LineGeometry.LineGeometryBatch.to_list

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatch.to_list
```

````

`````

`````{py:class} LineGeometryBatchProperties()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties
```

````{py:attribute} Conductors
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.Conductors
:type: typing.Union[typing.List[typing.AnyStr], typing.List[typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.Conductors
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.EmergAmps
```

````

````{py:attribute} H
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.H
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.H
```

````

````{py:attribute} Like
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.LineType
:type: typing.Union[typing.AnyStr, int, altdss.enums.LineType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LineType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.LineType
```

````

````{py:attribute} NConds
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.NConds
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.NPhases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.NPhases
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.NormAmps
```

````

````{py:attribute} Ratings
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.Ratings
```

````

````{py:attribute} Reduce
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.Reduce
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.Reduce
```

````

````{py:attribute} Seasons
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.Seasons
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.Seasons
```

````

````{py:attribute} Spacing
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.Spacing
:type: typing.Union[typing.AnyStr, altdss.LineSpacing.LineSpacing, typing.List[typing.AnyStr], typing.List[altdss.LineSpacing.LineSpacing]]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.Spacing
```

````

````{py:attribute} Units
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.Units
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.Units
```

````

````{py:attribute} X
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.X
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.X
```

````

````{py:method} __contains__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__contains__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__delattr__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__delitem__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__dir__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__format__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__ge__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__getitem__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__getstate__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__gt__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__init__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__ior__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__iter__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__le__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__len__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__lt__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__ne__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__new__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__or__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__reduce__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__repr__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__reversed__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__ror__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__setitem__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__str__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.clear

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.copy

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.get

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.items

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.keys

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.pop

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.popitem

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.setdefault

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.update

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.LineGeometry.LineGeometryBatchProperties.values

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryBatchProperties.values
```

````

`````

`````{py:class} LineGeometryProperties()
:canonical: altdss.LineGeometry.LineGeometryProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties
```

````{py:attribute} Conductors
:canonical: altdss.LineGeometry.LineGeometryProperties.Conductors
:type: typing.List[typing.Union[typing.AnyStr, typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.Conductors
```

````

````{py:attribute} EmergAmps
:canonical: altdss.LineGeometry.LineGeometryProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.EmergAmps
```

````

````{py:attribute} H
:canonical: altdss.LineGeometry.LineGeometryProperties.H
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.H
```

````

````{py:attribute} Like
:canonical: altdss.LineGeometry.LineGeometryProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.Like
```

````

````{py:attribute} LineType
:canonical: altdss.LineGeometry.LineGeometryProperties.LineType
:type: typing.Union[typing.AnyStr, int, altdss.enums.LineType]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.LineType
```

````

````{py:attribute} NConds
:canonical: altdss.LineGeometry.LineGeometryProperties.NConds
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.NConds
```

````

````{py:attribute} NPhases
:canonical: altdss.LineGeometry.LineGeometryProperties.NPhases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.NPhases
```

````

````{py:attribute} NormAmps
:canonical: altdss.LineGeometry.LineGeometryProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.NormAmps
```

````

````{py:attribute} Ratings
:canonical: altdss.LineGeometry.LineGeometryProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.Ratings
```

````

````{py:attribute} Reduce
:canonical: altdss.LineGeometry.LineGeometryProperties.Reduce
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.Reduce
```

````

````{py:attribute} Seasons
:canonical: altdss.LineGeometry.LineGeometryProperties.Seasons
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.Seasons
```

````

````{py:attribute} Spacing
:canonical: altdss.LineGeometry.LineGeometryProperties.Spacing
:type: typing.Union[typing.AnyStr, altdss.LineSpacing.LineSpacing]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.Spacing
```

````

````{py:attribute} Units
:canonical: altdss.LineGeometry.LineGeometryProperties.Units
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.Units
```

````

````{py:attribute} X
:canonical: altdss.LineGeometry.LineGeometryProperties.X
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.X
```

````

````{py:method} __contains__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__contains__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__delattr__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__delitem__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__dir__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__format__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__ge__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__getattribute__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__getitem__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__getstate__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__gt__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__init__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__ior__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__iter__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__le__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__len__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__lt__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__ne__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__new__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__or__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__reduce__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__reduce_ex__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__repr__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__reversed__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__ror__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__setitem__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__sizeof__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__str__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.LineGeometry.LineGeometryProperties.__subclasshook__

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.LineGeometry.LineGeometryProperties.clear

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.LineGeometry.LineGeometryProperties.copy

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.copy
```

````

````{py:method} get()
:canonical: altdss.LineGeometry.LineGeometryProperties.get

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.get
```

````

````{py:method} items()
:canonical: altdss.LineGeometry.LineGeometryProperties.items

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.items
```

````

````{py:method} keys()
:canonical: altdss.LineGeometry.LineGeometryProperties.keys

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.LineGeometry.LineGeometryProperties.pop

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.LineGeometry.LineGeometryProperties.popitem

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.LineGeometry.LineGeometryProperties.setdefault

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.LineGeometry.LineGeometryProperties.update

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.update
```

````

````{py:method} values()
:canonical: altdss.LineGeometry.LineGeometryProperties.values

```{autodoc2-docstring} altdss.LineGeometry.LineGeometryProperties.values
```

````

`````
