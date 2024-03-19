# {py:mod}`altdss.TSData`

```{py:module} altdss.TSData
```

```{autodoc2-docstring} altdss.TSData
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ITSData <altdss.TSData.ITSData>`
  - ```{autodoc2-docstring} altdss.TSData.ITSData
    :summary:
    ```
* - {py:obj}`TSData <altdss.TSData.TSData>`
  - ```{autodoc2-docstring} altdss.TSData.TSData
    :summary:
    ```
* - {py:obj}`TSDataBatch <altdss.TSData.TSDataBatch>`
  - ```{autodoc2-docstring} altdss.TSData.TSDataBatch
    :summary:
    ```
* - {py:obj}`TSDataBatchProperties <altdss.TSData.TSDataBatchProperties>`
  - ```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties
    :summary:
    ```
* - {py:obj}`TSDataProperties <altdss.TSData.TSDataProperties>`
  - ```{autodoc2-docstring} altdss.TSData.TSDataProperties
    :summary:
    ```
````

### API

`````{py:class} ITSData(iobj)
:canonical: altdss.TSData.ITSData

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.TSData.TSDataBatch`

```{autodoc2-docstring} altdss.TSData.ITSData
```

````{py:attribute} CapRadius
:canonical: altdss.TSData.ITSData.CapRadius
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.CapRadius
```

````

````{py:attribute} DiaCable
:canonical: altdss.TSData.ITSData.DiaCable
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.DiaCable
```

````

````{py:attribute} DiaIns
:canonical: altdss.TSData.ITSData.DiaIns
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.DiaIns
```

````

````{py:attribute} DiaShield
:canonical: altdss.TSData.ITSData.DiaShield
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.DiaShield
```

````

````{py:attribute} Diam
:canonical: altdss.TSData.ITSData.Diam
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.TSData.ITSData.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.EmergAmps
```

````

````{py:attribute} EpsR
:canonical: altdss.TSData.ITSData.EpsR
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.EpsR
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.TSData.ITSData.FullName

```{autodoc2-docstring} altdss.TSData.ITSData.FullName
```

````

````{py:attribute} GMRAC
:canonical: altdss.TSData.ITSData.GMRAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.TSData.ITSData.GMRUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.GMRUnits
```

````

````{py:attribute} GMRUnits_str
:canonical: altdss.TSData.ITSData.GMRUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.GMRUnits_str
```

````

````{py:attribute} InsLayer
:canonical: altdss.TSData.ITSData.InsLayer
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.InsLayer
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TSData.ITSData.Like

```{autodoc2-docstring} altdss.TSData.ITSData.Like
```

````

````{py:property} Name
:canonical: altdss.TSData.ITSData.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.TSData.ITSData.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.TSData.ITSData.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.TSData.ITSData.RAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.TSData.ITSData.RDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.TSData.ITSData.RUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.RUnits
```

````

````{py:attribute} RUnits_str
:canonical: altdss.TSData.ITSData.RUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.RUnits_str
```

````

````{py:attribute} RadUnits
:canonical: altdss.TSData.ITSData.RadUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.RadUnits
```

````

````{py:attribute} RadUnits_str
:canonical: altdss.TSData.ITSData.RadUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.RadUnits_str
```

````

````{py:attribute} Radius
:canonical: altdss.TSData.ITSData.Radius
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.TSData.ITSData.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.TSData.ITSData.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.Seasons
```

````

````{py:attribute} TapeLap
:canonical: altdss.TSData.ITSData.TapeLap
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.TapeLap
```

````

````{py:attribute} TapeLayer
:canonical: altdss.TSData.ITSData.TapeLayer
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.ITSData.TapeLayer
```

````

````{py:method} __call__()
:canonical: altdss.TSData.ITSData.__call__

```{autodoc2-docstring} altdss.TSData.ITSData.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.TSData.ITSData.__contains__

```{autodoc2-docstring} altdss.TSData.ITSData.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.TSData.ITSData.__getitem__

```{autodoc2-docstring} altdss.TSData.ITSData.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.TSData.ITSData.__init__

```{autodoc2-docstring} altdss.TSData.ITSData.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.TSData.ITSData.__iter__

```{autodoc2-docstring} altdss.TSData.ITSData.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.TSData.ITSData.__len__

```{autodoc2-docstring} altdss.TSData.ITSData.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.TSData.ITSData.batch

```{autodoc2-docstring} altdss.TSData.ITSData.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.TSData.TSDataBatchProperties]) -> altdss.TSData.TSDataBatch
:canonical: altdss.TSData.ITSData.batch_new

```{autodoc2-docstring} altdss.TSData.ITSData.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.TSData.ITSData.begin_edit

```{autodoc2-docstring} altdss.TSData.ITSData.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.TSData.TSDataBatchProperties]) -> altdss.TSData.TSDataBatch
:canonical: altdss.TSData.ITSData.edit

```{autodoc2-docstring} altdss.TSData.ITSData.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.TSData.ITSData.end_edit

```{autodoc2-docstring} altdss.TSData.ITSData.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.TSData.ITSData.find

```{autodoc2-docstring} altdss.TSData.ITSData.find
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.TSData.TSDataProperties]) -> altdss.TSData.TSData
:canonical: altdss.TSData.ITSData.new

```{autodoc2-docstring} altdss.TSData.ITSData.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.TSData.ITSData.to_json

```{autodoc2-docstring} altdss.TSData.ITSData.to_json
```

````

````{py:method} to_list()
:canonical: altdss.TSData.ITSData.to_list

```{autodoc2-docstring} altdss.TSData.ITSData.to_list
```

````

`````

`````{py:class} TSData(api_util, ptr)
:canonical: altdss.TSData.TSData

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.TSData.TSData
```

````{py:attribute} CapRadius
:canonical: altdss.TSData.TSData.CapRadius
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.CapRadius
```

````

````{py:attribute} DiaCable
:canonical: altdss.TSData.TSData.DiaCable
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.DiaCable
```

````

````{py:attribute} DiaIns
:canonical: altdss.TSData.TSData.DiaIns
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.DiaIns
```

````

````{py:attribute} DiaShield
:canonical: altdss.TSData.TSData.DiaShield
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.DiaShield
```

````

````{py:attribute} Diam
:canonical: altdss.TSData.TSData.Diam
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.TSData.TSData.EmergAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.EmergAmps
```

````

````{py:attribute} EpsR
:canonical: altdss.TSData.TSData.EpsR
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.EpsR
```

````

````{py:method} FullName() -> str
:canonical: altdss.TSData.TSData.FullName

```{autodoc2-docstring} altdss.TSData.TSData.FullName
```

````

````{py:attribute} GMRAC
:canonical: altdss.TSData.TSData.GMRAC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.TSData.TSData.GMRUnits
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.GMRUnits
```

````

````{py:attribute} GMRUnits_str
:canonical: altdss.TSData.TSData.GMRUnits_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.GMRUnits_str
```

````

````{py:attribute} InsLayer
:canonical: altdss.TSData.TSData.InsLayer
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.InsLayer
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.TSData.TSData.Like

```{autodoc2-docstring} altdss.TSData.TSData.Like
```

````

````{py:property} Name
:canonical: altdss.TSData.TSData.Name
:type: str

```{autodoc2-docstring} altdss.TSData.TSData.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.TSData.TSData.NormAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.TSData.TSData.RAC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.TSData.TSData.RDC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.TSData.TSData.RUnits
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.RUnits
```

````

````{py:attribute} RUnits_str
:canonical: altdss.TSData.TSData.RUnits_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.RUnits_str
```

````

````{py:attribute} RadUnits
:canonical: altdss.TSData.TSData.RadUnits
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.RadUnits
```

````

````{py:attribute} RadUnits_str
:canonical: altdss.TSData.TSData.RadUnits_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.RadUnits_str
```

````

````{py:attribute} Radius
:canonical: altdss.TSData.TSData.Radius
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.TSData.TSData.Ratings
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.TSData.TSData.Seasons
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.Seasons
```

````

````{py:attribute} TapeLap
:canonical: altdss.TSData.TSData.TapeLap
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.TapeLap
```

````

````{py:attribute} TapeLayer
:canonical: altdss.TSData.TSData.TapeLayer
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSData.TapeLayer
```

````

````{py:method} __hash__()
:canonical: altdss.TSData.TSData.__hash__

```{autodoc2-docstring} altdss.TSData.TSData.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.TSData.TSData.__init__

```{autodoc2-docstring} altdss.TSData.TSData.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.TSData.TSData.__ne__

```{autodoc2-docstring} altdss.TSData.TSData.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.TSData.TSData.__repr__

```{autodoc2-docstring} altdss.TSData.TSData.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.TSData.TSData.begin_edit

```{autodoc2-docstring} altdss.TSData.TSData.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.TSData.TSDataProperties]) -> altdss.TSData.TSData
:canonical: altdss.TSData.TSData.edit

```{autodoc2-docstring} altdss.TSData.TSData.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.TSData.TSData.end_edit

```{autodoc2-docstring} altdss.TSData.TSData.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.TSData.TSData.to_json

```{autodoc2-docstring} altdss.TSData.TSData.to_json
```

````

`````

`````{py:class} TSDataBatch(api_util, **kwargs)
:canonical: altdss.TSData.TSDataBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.TSData.TSDataBatch
```

````{py:attribute} CapRadius
:canonical: altdss.TSData.TSDataBatch.CapRadius
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.CapRadius
```

````

````{py:attribute} DiaCable
:canonical: altdss.TSData.TSDataBatch.DiaCable
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.DiaCable
```

````

````{py:attribute} DiaIns
:canonical: altdss.TSData.TSDataBatch.DiaIns
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.DiaIns
```

````

````{py:attribute} DiaShield
:canonical: altdss.TSData.TSDataBatch.DiaShield
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.DiaShield
```

````

````{py:attribute} Diam
:canonical: altdss.TSData.TSDataBatch.Diam
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.TSData.TSDataBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.EmergAmps
```

````

````{py:attribute} EpsR
:canonical: altdss.TSData.TSDataBatch.EpsR
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.EpsR
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.TSData.TSDataBatch.FullName

```{autodoc2-docstring} altdss.TSData.TSDataBatch.FullName
```

````

````{py:attribute} GMRAC
:canonical: altdss.TSData.TSDataBatch.GMRAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.TSData.TSDataBatch.GMRUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.GMRUnits
```

````

````{py:attribute} GMRUnits_str
:canonical: altdss.TSData.TSDataBatch.GMRUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.GMRUnits_str
```

````

````{py:attribute} InsLayer
:canonical: altdss.TSData.TSDataBatch.InsLayer
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.InsLayer
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.TSData.TSDataBatch.Like

```{autodoc2-docstring} altdss.TSData.TSDataBatch.Like
```

````

````{py:property} Name
:canonical: altdss.TSData.TSDataBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.TSData.TSDataBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.TSData.TSDataBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.TSData.TSDataBatch.RAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.TSData.TSDataBatch.RDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.TSData.TSDataBatch.RUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.RUnits
```

````

````{py:attribute} RUnits_str
:canonical: altdss.TSData.TSDataBatch.RUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.RUnits_str
```

````

````{py:attribute} RadUnits
:canonical: altdss.TSData.TSDataBatch.RadUnits
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.RadUnits
```

````

````{py:attribute} RadUnits_str
:canonical: altdss.TSData.TSDataBatch.RadUnits_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.RadUnits_str
```

````

````{py:attribute} Radius
:canonical: altdss.TSData.TSDataBatch.Radius
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.TSData.TSDataBatch.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.TSData.TSDataBatch.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.Seasons
```

````

````{py:attribute} TapeLap
:canonical: altdss.TSData.TSDataBatch.TapeLap
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.TapeLap
```

````

````{py:attribute} TapeLayer
:canonical: altdss.TSData.TSDataBatch.TapeLayer
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.TSData.TSDataBatch.TapeLayer
```

````

````{py:method} __call__()
:canonical: altdss.TSData.TSDataBatch.__call__

```{autodoc2-docstring} altdss.TSData.TSDataBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.TSData.TSDataBatch.__getitem__

```{autodoc2-docstring} altdss.TSData.TSDataBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.TSData.TSDataBatch.__init__

```{autodoc2-docstring} altdss.TSData.TSDataBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.TSData.TSDataBatch.__iter__

```{autodoc2-docstring} altdss.TSData.TSDataBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.TSData.TSDataBatch.__len__

```{autodoc2-docstring} altdss.TSData.TSDataBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.TSData.TSDataBatch.batch

```{autodoc2-docstring} altdss.TSData.TSDataBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.TSData.TSDataBatch.begin_edit

```{autodoc2-docstring} altdss.TSData.TSDataBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.TSData.TSDataBatchProperties]) -> altdss.TSData.TSDataBatch
:canonical: altdss.TSData.TSDataBatch.edit

```{autodoc2-docstring} altdss.TSData.TSDataBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.TSData.TSDataBatch.end_edit

```{autodoc2-docstring} altdss.TSData.TSDataBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.TSData.TSDataBatch.to_json

```{autodoc2-docstring} altdss.TSData.TSDataBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.TSData.TSDataBatch.to_list

```{autodoc2-docstring} altdss.TSData.TSDataBatch.to_list
```

````

`````

`````{py:class} TSDataBatchProperties()
:canonical: altdss.TSData.TSDataBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties
```

````{py:attribute} CapRadius
:canonical: altdss.TSData.TSDataBatchProperties.CapRadius
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.CapRadius
```

````

````{py:attribute} DiaCable
:canonical: altdss.TSData.TSDataBatchProperties.DiaCable
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.DiaCable
```

````

````{py:attribute} DiaIns
:canonical: altdss.TSData.TSDataBatchProperties.DiaIns
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.DiaIns
```

````

````{py:attribute} DiaShield
:canonical: altdss.TSData.TSDataBatchProperties.DiaShield
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.DiaShield
```

````

````{py:attribute} Diam
:canonical: altdss.TSData.TSDataBatchProperties.Diam
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.TSData.TSDataBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.EmergAmps
```

````

````{py:attribute} EpsR
:canonical: altdss.TSData.TSDataBatchProperties.EpsR
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.EpsR
```

````

````{py:attribute} GMRAC
:canonical: altdss.TSData.TSDataBatchProperties.GMRAC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.TSData.TSDataBatchProperties.GMRUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.GMRUnits
```

````

````{py:attribute} InsLayer
:canonical: altdss.TSData.TSDataBatchProperties.InsLayer
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.InsLayer
```

````

````{py:attribute} Like
:canonical: altdss.TSData.TSDataBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.Like
```

````

````{py:attribute} NormAmps
:canonical: altdss.TSData.TSDataBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.TSData.TSDataBatchProperties.RAC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.TSData.TSDataBatchProperties.RDC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.TSData.TSDataBatchProperties.RUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.RUnits
```

````

````{py:attribute} RadUnits
:canonical: altdss.TSData.TSDataBatchProperties.RadUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.RadUnits
```

````

````{py:attribute} Radius
:canonical: altdss.TSData.TSDataBatchProperties.Radius
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.TSData.TSDataBatchProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.TSData.TSDataBatchProperties.Seasons
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.Seasons
```

````

````{py:attribute} TapeLap
:canonical: altdss.TSData.TSDataBatchProperties.TapeLap
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.TapeLap
```

````

````{py:attribute} TapeLayer
:canonical: altdss.TSData.TSDataBatchProperties.TapeLayer
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.TapeLayer
```

````

````{py:method} __contains__()
:canonical: altdss.TSData.TSDataBatchProperties.__contains__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.TSData.TSDataBatchProperties.__delattr__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.TSData.TSDataBatchProperties.__delitem__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.TSData.TSDataBatchProperties.__dir__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.TSData.TSDataBatchProperties.__format__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.TSData.TSDataBatchProperties.__ge__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.TSData.TSDataBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.TSData.TSDataBatchProperties.__getitem__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.TSData.TSDataBatchProperties.__getstate__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.TSData.TSDataBatchProperties.__gt__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.TSData.TSDataBatchProperties.__init__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.TSData.TSDataBatchProperties.__ior__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.TSData.TSDataBatchProperties.__iter__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.TSData.TSDataBatchProperties.__le__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.TSData.TSDataBatchProperties.__len__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.TSData.TSDataBatchProperties.__lt__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.TSData.TSDataBatchProperties.__ne__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.TSData.TSDataBatchProperties.__new__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.TSData.TSDataBatchProperties.__or__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.TSData.TSDataBatchProperties.__reduce__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.TSData.TSDataBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.TSData.TSDataBatchProperties.__repr__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.TSData.TSDataBatchProperties.__reversed__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.TSData.TSDataBatchProperties.__ror__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.TSData.TSDataBatchProperties.__setitem__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.TSData.TSDataBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.TSData.TSDataBatchProperties.__str__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.TSData.TSDataBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.TSData.TSDataBatchProperties.clear

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.TSData.TSDataBatchProperties.copy

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.TSData.TSDataBatchProperties.get

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.TSData.TSDataBatchProperties.items

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.TSData.TSDataBatchProperties.keys

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.TSData.TSDataBatchProperties.pop

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.TSData.TSDataBatchProperties.popitem

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.TSData.TSDataBatchProperties.setdefault

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.TSData.TSDataBatchProperties.update

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.TSData.TSDataBatchProperties.values

```{autodoc2-docstring} altdss.TSData.TSDataBatchProperties.values
```

````

`````

`````{py:class} TSDataProperties()
:canonical: altdss.TSData.TSDataProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.TSData.TSDataProperties
```

````{py:attribute} CapRadius
:canonical: altdss.TSData.TSDataProperties.CapRadius
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.CapRadius
```

````

````{py:attribute} DiaCable
:canonical: altdss.TSData.TSDataProperties.DiaCable
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.DiaCable
```

````

````{py:attribute} DiaIns
:canonical: altdss.TSData.TSDataProperties.DiaIns
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.DiaIns
```

````

````{py:attribute} DiaShield
:canonical: altdss.TSData.TSDataProperties.DiaShield
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.DiaShield
```

````

````{py:attribute} Diam
:canonical: altdss.TSData.TSDataProperties.Diam
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.Diam
```

````

````{py:attribute} EmergAmps
:canonical: altdss.TSData.TSDataProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.EmergAmps
```

````

````{py:attribute} EpsR
:canonical: altdss.TSData.TSDataProperties.EpsR
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.EpsR
```

````

````{py:attribute} GMRAC
:canonical: altdss.TSData.TSDataProperties.GMRAC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.GMRAC
```

````

````{py:attribute} GMRUnits
:canonical: altdss.TSData.TSDataProperties.GMRUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.GMRUnits
```

````

````{py:attribute} InsLayer
:canonical: altdss.TSData.TSDataProperties.InsLayer
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.InsLayer
```

````

````{py:attribute} Like
:canonical: altdss.TSData.TSDataProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.Like
```

````

````{py:attribute} NormAmps
:canonical: altdss.TSData.TSDataProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.NormAmps
```

````

````{py:attribute} RAC
:canonical: altdss.TSData.TSDataProperties.RAC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.RAC
```

````

````{py:attribute} RDC
:canonical: altdss.TSData.TSDataProperties.RDC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.RDC
```

````

````{py:attribute} RUnits
:canonical: altdss.TSData.TSDataProperties.RUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.RUnits
```

````

````{py:attribute} RadUnits
:canonical: altdss.TSData.TSDataProperties.RadUnits
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.RadUnits
```

````

````{py:attribute} Radius
:canonical: altdss.TSData.TSDataProperties.Radius
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.Radius
```

````

````{py:attribute} Ratings
:canonical: altdss.TSData.TSDataProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.TSData.TSDataProperties.Seasons
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.Seasons
```

````

````{py:attribute} TapeLap
:canonical: altdss.TSData.TSDataProperties.TapeLap
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.TapeLap
```

````

````{py:attribute} TapeLayer
:canonical: altdss.TSData.TSDataProperties.TapeLayer
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.TSData.TSDataProperties.TapeLayer
```

````

````{py:method} __contains__()
:canonical: altdss.TSData.TSDataProperties.__contains__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.TSData.TSDataProperties.__delattr__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.TSData.TSDataProperties.__delitem__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.TSData.TSDataProperties.__dir__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.TSData.TSDataProperties.__format__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.TSData.TSDataProperties.__ge__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.TSData.TSDataProperties.__getattribute__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.TSData.TSDataProperties.__getitem__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.TSData.TSDataProperties.__getstate__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.TSData.TSDataProperties.__gt__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.TSData.TSDataProperties.__init__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.TSData.TSDataProperties.__ior__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.TSData.TSDataProperties.__iter__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.TSData.TSDataProperties.__le__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.TSData.TSDataProperties.__len__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.TSData.TSDataProperties.__lt__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.TSData.TSDataProperties.__ne__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.TSData.TSDataProperties.__new__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.TSData.TSDataProperties.__or__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.TSData.TSDataProperties.__reduce__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.TSData.TSDataProperties.__reduce_ex__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.TSData.TSDataProperties.__repr__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.TSData.TSDataProperties.__reversed__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.TSData.TSDataProperties.__ror__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.TSData.TSDataProperties.__setitem__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.TSData.TSDataProperties.__sizeof__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.TSData.TSDataProperties.__str__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.TSData.TSDataProperties.__subclasshook__

```{autodoc2-docstring} altdss.TSData.TSDataProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.TSData.TSDataProperties.clear

```{autodoc2-docstring} altdss.TSData.TSDataProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.TSData.TSDataProperties.copy

```{autodoc2-docstring} altdss.TSData.TSDataProperties.copy
```

````

````{py:method} get()
:canonical: altdss.TSData.TSDataProperties.get

```{autodoc2-docstring} altdss.TSData.TSDataProperties.get
```

````

````{py:method} items()
:canonical: altdss.TSData.TSDataProperties.items

```{autodoc2-docstring} altdss.TSData.TSDataProperties.items
```

````

````{py:method} keys()
:canonical: altdss.TSData.TSDataProperties.keys

```{autodoc2-docstring} altdss.TSData.TSDataProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.TSData.TSDataProperties.pop

```{autodoc2-docstring} altdss.TSData.TSDataProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.TSData.TSDataProperties.popitem

```{autodoc2-docstring} altdss.TSData.TSDataProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.TSData.TSDataProperties.setdefault

```{autodoc2-docstring} altdss.TSData.TSDataProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.TSData.TSDataProperties.update

```{autodoc2-docstring} altdss.TSData.TSDataProperties.update
```

````

````{py:method} values()
:canonical: altdss.TSData.TSDataProperties.values

```{autodoc2-docstring} altdss.TSData.TSDataProperties.values
```

````

`````
