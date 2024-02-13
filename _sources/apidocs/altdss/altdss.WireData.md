# {py:mod}`altdss.WireData`

```{py:module} altdss.WireData
```

```{autodoc2-docstring} altdss.WireData
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IWireData <altdss.WireData.IWireData>`
  - ```{autodoc2-docstring} altdss.WireData.IWireData
    :summary:
    ```
* - {py:obj}`WireData <altdss.WireData.WireData>`
  - ```{autodoc2-docstring} altdss.WireData.WireData
    :summary:
    ```
* - {py:obj}`WireDataBatch <altdss.WireData.WireDataBatch>`
  - ```{autodoc2-docstring} altdss.WireData.WireDataBatch
    :summary:
    ```
* - {py:obj}`WireDataBatchProperties <altdss.WireData.WireDataBatchProperties>`
  - ```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties
    :summary:
    ```
* - {py:obj}`WireDataProperties <altdss.WireData.WireDataProperties>`
  - ```{autodoc2-docstring} altdss.WireData.WireDataProperties
    :summary:
    ```
````

### API

`````{py:class} IWireData(iobj)
:canonical: altdss.WireData.IWireData

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.WireData.WireDataBatch`

```{autodoc2-docstring} altdss.WireData.IWireData
```

````{py:attribute} CapRadius
:canonical: altdss.WireData.IWireData.CapRadius
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.CapRadius
```

````

````{py:attribute} Diam
:canonical: altdss.WireData.IWireData.Diam
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.WireData.IWireData.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.EmergAmps
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.WireData.IWireData.FullName

```{autodoc2-docstring} altdss.WireData.IWireData.FullName
```

````

````{py:attribute} GMRAC
:canonical: altdss.WireData.IWireData.GMRAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.WireData.IWireData.GMRUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.GMRUnits
```

````

````{py:attribute} GMRUnits_str
:canonical: altdss.WireData.IWireData.GMRUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.GMRUnits_str
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.WireData.IWireData.Like

```{autodoc2-docstring} altdss.WireData.IWireData.Like
```

````

````{py:property} Name
:canonical: altdss.WireData.IWireData.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.WireData.IWireData.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.WireData.IWireData.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.WireData.IWireData.RAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.WireData.IWireData.RDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.WireData.IWireData.RUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.RUnits
```

````

````{py:attribute} RUnits_str
:canonical: altdss.WireData.IWireData.RUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.RUnits_str
```

````

````{py:attribute} RadUnits
:canonical: altdss.WireData.IWireData.RadUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.RadUnits
```

````

````{py:attribute} RadUnits_str
:canonical: altdss.WireData.IWireData.RadUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.RadUnits_str
```

````

````{py:attribute} Radius
:canonical: altdss.WireData.IWireData.Radius
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.WireData.IWireData.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.WireData.IWireData.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.IWireData.Seasons
```

````

````{py:method} __call__()
:canonical: altdss.WireData.IWireData.__call__

```{autodoc2-docstring} altdss.WireData.IWireData.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.WireData.IWireData.__contains__

```{autodoc2-docstring} altdss.WireData.IWireData.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.WireData.IWireData.__getitem__

```{autodoc2-docstring} altdss.WireData.IWireData.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.WireData.IWireData.__init__

```{autodoc2-docstring} altdss.WireData.IWireData.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.WireData.IWireData.__iter__

```{autodoc2-docstring} altdss.WireData.IWireData.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.WireData.IWireData.__len__

```{autodoc2-docstring} altdss.WireData.IWireData.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.WireData.IWireData.batch

```{autodoc2-docstring} altdss.WireData.IWireData.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.WireData.WireDataBatchProperties]) -> altdss.WireData.WireDataBatch
:canonical: altdss.WireData.IWireData.batch_new

```{autodoc2-docstring} altdss.WireData.IWireData.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.WireData.IWireData.begin_edit

```{autodoc2-docstring} altdss.WireData.IWireData.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.WireData.IWireData.end_edit

```{autodoc2-docstring} altdss.WireData.IWireData.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.WireData.IWireData.find

```{autodoc2-docstring} altdss.WireData.IWireData.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.WireData.WireDataProperties]) -> altdss.WireData.WireData
:canonical: altdss.WireData.IWireData.new

```{autodoc2-docstring} altdss.WireData.IWireData.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.WireData.IWireData.to_json

```{autodoc2-docstring} altdss.WireData.IWireData.to_json
```

````

````{py:method} to_list()
:canonical: altdss.WireData.IWireData.to_list

```{autodoc2-docstring} altdss.WireData.IWireData.to_list
```

````

`````

`````{py:class} WireData(api_util, ptr)
:canonical: altdss.WireData.WireData

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.WireData.WireData
```

````{py:attribute} CapRadius
:canonical: altdss.WireData.WireData.CapRadius
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.CapRadius
```

````

````{py:attribute} Diam
:canonical: altdss.WireData.WireData.Diam
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.WireData.WireData.EmergAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.EmergAmps
```

````

````{py:method} FullName() -> str
:canonical: altdss.WireData.WireData.FullName

```{autodoc2-docstring} altdss.WireData.WireData.FullName
```

````

````{py:attribute} GMRAC
:canonical: altdss.WireData.WireData.GMRAC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.WireData.WireData.GMRUnits
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.GMRUnits
```

````

````{py:attribute} GMRUnits_str
:canonical: altdss.WireData.WireData.GMRUnits_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.GMRUnits_str
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.WireData.WireData.Like

```{autodoc2-docstring} altdss.WireData.WireData.Like
```

````

````{py:property} Name
:canonical: altdss.WireData.WireData.Name
:type: str

```{autodoc2-docstring} altdss.WireData.WireData.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.WireData.WireData.NormAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.WireData.WireData.RAC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.WireData.WireData.RDC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.WireData.WireData.RUnits
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.RUnits
```

````

````{py:attribute} RUnits_str
:canonical: altdss.WireData.WireData.RUnits_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.RUnits_str
```

````

````{py:attribute} RadUnits
:canonical: altdss.WireData.WireData.RadUnits
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.RadUnits
```

````

````{py:attribute} RadUnits_str
:canonical: altdss.WireData.WireData.RadUnits_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.RadUnits_str
```

````

````{py:attribute} Radius
:canonical: altdss.WireData.WireData.Radius
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.WireData.WireData.Ratings
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.WireData.WireData.Seasons
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireData.Seasons
```

````

````{py:method} __hash__()
:canonical: altdss.WireData.WireData.__hash__

```{autodoc2-docstring} altdss.WireData.WireData.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.WireData.WireData.__init__

```{autodoc2-docstring} altdss.WireData.WireData.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.WireData.WireData.__ne__

```{autodoc2-docstring} altdss.WireData.WireData.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.WireData.WireData.__repr__

```{autodoc2-docstring} altdss.WireData.WireData.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.WireData.WireData.begin_edit

```{autodoc2-docstring} altdss.WireData.WireData.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.WireData.WireData.end_edit

```{autodoc2-docstring} altdss.WireData.WireData.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.WireData.WireData.to_json

```{autodoc2-docstring} altdss.WireData.WireData.to_json
```

````

`````

`````{py:class} WireDataBatch(api_util, **kwargs)
:canonical: altdss.WireData.WireDataBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.WireData.WireDataBatch
```

````{py:attribute} CapRadius
:canonical: altdss.WireData.WireDataBatch.CapRadius
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.CapRadius
```

````

````{py:attribute} Diam
:canonical: altdss.WireData.WireDataBatch.Diam
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.WireData.WireDataBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.EmergAmps
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.WireData.WireDataBatch.FullName

```{autodoc2-docstring} altdss.WireData.WireDataBatch.FullName
```

````

````{py:attribute} GMRAC
:canonical: altdss.WireData.WireDataBatch.GMRAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.WireData.WireDataBatch.GMRUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.GMRUnits
```

````

````{py:attribute} GMRUnits_str
:canonical: altdss.WireData.WireDataBatch.GMRUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.GMRUnits_str
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.WireData.WireDataBatch.Like

```{autodoc2-docstring} altdss.WireData.WireDataBatch.Like
```

````

````{py:property} Name
:canonical: altdss.WireData.WireDataBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.WireData.WireDataBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.WireData.WireDataBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.WireData.WireDataBatch.RAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.WireData.WireDataBatch.RDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.WireData.WireDataBatch.RUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.RUnits
```

````

````{py:attribute} RUnits_str
:canonical: altdss.WireData.WireDataBatch.RUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.RUnits_str
```

````

````{py:attribute} RadUnits
:canonical: altdss.WireData.WireDataBatch.RadUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.RadUnits
```

````

````{py:attribute} RadUnits_str
:canonical: altdss.WireData.WireDataBatch.RadUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.RadUnits_str
```

````

````{py:attribute} Radius
:canonical: altdss.WireData.WireDataBatch.Radius
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.WireData.WireDataBatch.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.WireData.WireDataBatch.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.WireData.WireDataBatch.Seasons
```

````

````{py:method} __call__()
:canonical: altdss.WireData.WireDataBatch.__call__

```{autodoc2-docstring} altdss.WireData.WireDataBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.WireData.WireDataBatch.__getitem__

```{autodoc2-docstring} altdss.WireData.WireDataBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.WireData.WireDataBatch.__init__

```{autodoc2-docstring} altdss.WireData.WireDataBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.WireData.WireDataBatch.__iter__

```{autodoc2-docstring} altdss.WireData.WireDataBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.WireData.WireDataBatch.__len__

```{autodoc2-docstring} altdss.WireData.WireDataBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.WireData.WireDataBatch.begin_edit

```{autodoc2-docstring} altdss.WireData.WireDataBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.WireData.WireDataBatch.end_edit

```{autodoc2-docstring} altdss.WireData.WireDataBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.WireData.WireDataBatch.to_json

```{autodoc2-docstring} altdss.WireData.WireDataBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.WireData.WireDataBatch.to_list

```{autodoc2-docstring} altdss.WireData.WireDataBatch.to_list
```

````

`````

`````{py:class} WireDataBatchProperties()
:canonical: altdss.WireData.WireDataBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties
```

````{py:attribute} CapRadius
:canonical: altdss.WireData.WireDataBatchProperties.CapRadius
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.CapRadius
```

````

````{py:attribute} Diam
:canonical: altdss.WireData.WireDataBatchProperties.Diam
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.WireData.WireDataBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.EmergAmps
```

````

````{py:attribute} GMRAC
:canonical: altdss.WireData.WireDataBatchProperties.GMRAC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.WireData.WireDataBatchProperties.GMRUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.GMRUnits
```

````

````{py:attribute} Like
:canonical: altdss.WireData.WireDataBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.Like
```

````

````{py:attribute} NormAmps
:canonical: altdss.WireData.WireDataBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.WireData.WireDataBatchProperties.RAC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.WireData.WireDataBatchProperties.RDC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.WireData.WireDataBatchProperties.RUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.RUnits
```

````

````{py:attribute} RadUnits
:canonical: altdss.WireData.WireDataBatchProperties.RadUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.RadUnits
```

````

````{py:attribute} Radius
:canonical: altdss.WireData.WireDataBatchProperties.Radius
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.WireData.WireDataBatchProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.WireData.WireDataBatchProperties.Seasons
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.Seasons
```

````

````{py:method} __contains__()
:canonical: altdss.WireData.WireDataBatchProperties.__contains__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.WireData.WireDataBatchProperties.__delattr__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.WireData.WireDataBatchProperties.__delitem__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.WireData.WireDataBatchProperties.__dir__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.WireData.WireDataBatchProperties.__format__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.WireData.WireDataBatchProperties.__ge__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.WireData.WireDataBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.WireData.WireDataBatchProperties.__getitem__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.WireData.WireDataBatchProperties.__getstate__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.WireData.WireDataBatchProperties.__gt__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.WireData.WireDataBatchProperties.__init__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.WireData.WireDataBatchProperties.__ior__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.WireData.WireDataBatchProperties.__iter__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.WireData.WireDataBatchProperties.__le__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.WireData.WireDataBatchProperties.__len__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.WireData.WireDataBatchProperties.__lt__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.WireData.WireDataBatchProperties.__ne__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.WireData.WireDataBatchProperties.__new__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.WireData.WireDataBatchProperties.__or__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.WireData.WireDataBatchProperties.__reduce__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.WireData.WireDataBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.WireData.WireDataBatchProperties.__repr__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.WireData.WireDataBatchProperties.__reversed__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.WireData.WireDataBatchProperties.__ror__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.WireData.WireDataBatchProperties.__setitem__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.WireData.WireDataBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.WireData.WireDataBatchProperties.__str__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.WireData.WireDataBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.WireData.WireDataBatchProperties.clear

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.WireData.WireDataBatchProperties.copy

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.WireData.WireDataBatchProperties.get

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.WireData.WireDataBatchProperties.items

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.WireData.WireDataBatchProperties.keys

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.WireData.WireDataBatchProperties.pop

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.WireData.WireDataBatchProperties.popitem

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.WireData.WireDataBatchProperties.setdefault

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.WireData.WireDataBatchProperties.update

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.WireData.WireDataBatchProperties.values

```{autodoc2-docstring} altdss.WireData.WireDataBatchProperties.values
```

````

`````

`````{py:class} WireDataProperties()
:canonical: altdss.WireData.WireDataProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.WireData.WireDataProperties
```

````{py:attribute} CapRadius
:canonical: altdss.WireData.WireDataProperties.CapRadius
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.CapRadius
```

````

````{py:attribute} Diam
:canonical: altdss.WireData.WireDataProperties.Diam
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.WireData.WireDataProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.EmergAmps
```

````

````{py:attribute} GMRAC
:canonical: altdss.WireData.WireDataProperties.GMRAC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.WireData.WireDataProperties.GMRUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.GMRUnits
```

````

````{py:attribute} Like
:canonical: altdss.WireData.WireDataProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.Like
```

````

````{py:attribute} NormAmps
:canonical: altdss.WireData.WireDataProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.WireData.WireDataProperties.RAC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.WireData.WireDataProperties.RDC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.WireData.WireDataProperties.RUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.RUnits
```

````

````{py:attribute} RadUnits
:canonical: altdss.WireData.WireDataProperties.RadUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.RadUnits
```

````

````{py:attribute} Radius
:canonical: altdss.WireData.WireDataProperties.Radius
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.WireData.WireDataProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.WireData.WireDataProperties.Seasons
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.WireData.WireDataProperties.Seasons
```

````

````{py:method} __contains__()
:canonical: altdss.WireData.WireDataProperties.__contains__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.WireData.WireDataProperties.__delattr__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.WireData.WireDataProperties.__delitem__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.WireData.WireDataProperties.__dir__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.WireData.WireDataProperties.__format__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.WireData.WireDataProperties.__ge__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.WireData.WireDataProperties.__getattribute__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.WireData.WireDataProperties.__getitem__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.WireData.WireDataProperties.__getstate__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.WireData.WireDataProperties.__gt__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.WireData.WireDataProperties.__init__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.WireData.WireDataProperties.__ior__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.WireData.WireDataProperties.__iter__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.WireData.WireDataProperties.__le__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.WireData.WireDataProperties.__len__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.WireData.WireDataProperties.__lt__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.WireData.WireDataProperties.__ne__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.WireData.WireDataProperties.__new__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.WireData.WireDataProperties.__or__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.WireData.WireDataProperties.__reduce__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.WireData.WireDataProperties.__reduce_ex__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.WireData.WireDataProperties.__repr__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.WireData.WireDataProperties.__reversed__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.WireData.WireDataProperties.__ror__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.WireData.WireDataProperties.__setitem__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.WireData.WireDataProperties.__sizeof__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.WireData.WireDataProperties.__str__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.WireData.WireDataProperties.__subclasshook__

```{autodoc2-docstring} altdss.WireData.WireDataProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.WireData.WireDataProperties.clear

```{autodoc2-docstring} altdss.WireData.WireDataProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.WireData.WireDataProperties.copy

```{autodoc2-docstring} altdss.WireData.WireDataProperties.copy
```

````

````{py:method} get()
:canonical: altdss.WireData.WireDataProperties.get

```{autodoc2-docstring} altdss.WireData.WireDataProperties.get
```

````

````{py:method} items()
:canonical: altdss.WireData.WireDataProperties.items

```{autodoc2-docstring} altdss.WireData.WireDataProperties.items
```

````

````{py:method} keys()
:canonical: altdss.WireData.WireDataProperties.keys

```{autodoc2-docstring} altdss.WireData.WireDataProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.WireData.WireDataProperties.pop

```{autodoc2-docstring} altdss.WireData.WireDataProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.WireData.WireDataProperties.popitem

```{autodoc2-docstring} altdss.WireData.WireDataProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.WireData.WireDataProperties.setdefault

```{autodoc2-docstring} altdss.WireData.WireDataProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.WireData.WireDataProperties.update

```{autodoc2-docstring} altdss.WireData.WireDataProperties.update
```

````

````{py:method} values()
:canonical: altdss.WireData.WireDataProperties.values

```{autodoc2-docstring} altdss.WireData.WireDataProperties.values
```

````

`````
