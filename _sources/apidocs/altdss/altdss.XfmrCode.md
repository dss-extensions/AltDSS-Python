# {py:mod}`altdss.XfmrCode`

```{py:module} altdss.XfmrCode
```

```{autodoc2-docstring} altdss.XfmrCode
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IXfmrCode <altdss.XfmrCode.IXfmrCode>`
  - ```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode
    :summary:
    ```
* - {py:obj}`XfmrCode <altdss.XfmrCode.XfmrCode>`
  - ```{autodoc2-docstring} altdss.XfmrCode.XfmrCode
    :summary:
    ```
* - {py:obj}`XfmrCodeBatch <altdss.XfmrCode.XfmrCodeBatch>`
  - ```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch
    :summary:
    ```
* - {py:obj}`XfmrCodeBatchProperties <altdss.XfmrCode.XfmrCodeBatchProperties>`
  - ```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties
    :summary:
    ```
* - {py:obj}`XfmrCodeProperties <altdss.XfmrCode.XfmrCodeProperties>`
  - ```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties
    :summary:
    ```
````

### API

`````{py:class} IXfmrCode(iobj)
:canonical: altdss.XfmrCode.IXfmrCode

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.XfmrCode.XfmrCodeBatch`

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode
```

````{py:attribute} Conns
:canonical: altdss.XfmrCode.IXfmrCode.Conns
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Conns
```

````

````{py:attribute} Conns_str
:canonical: altdss.XfmrCode.IXfmrCode.Conns_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Conns_str
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.XfmrCode.IXfmrCode.EmergHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.EmergHkVA
```

````

````{py:attribute} FLRise
:canonical: altdss.XfmrCode.IXfmrCode.FLRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.FLRise
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.XfmrCode.IXfmrCode.FullName

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.FullName
```

````

````{py:attribute} HSRise
:canonical: altdss.XfmrCode.IXfmrCode.HSRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.HSRise
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.XfmrCode.IXfmrCode.Like

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Like
```

````

````{py:attribute} MaxTap
:canonical: altdss.XfmrCode.IXfmrCode.MaxTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.XfmrCode.IXfmrCode.MinTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.MinTap
```

````

````{py:property} Name
:canonical: altdss.XfmrCode.IXfmrCode.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Name
```

````

````{py:attribute} NormHkVA
:canonical: altdss.XfmrCode.IXfmrCode.NormHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.NormHkVA
```

````

````{py:attribute} NumTaps
:canonical: altdss.XfmrCode.IXfmrCode.NumTaps
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.NumTaps
```

````

````{py:attribute} Phases
:canonical: altdss.XfmrCode.IXfmrCode.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Phases
```

````

````{py:attribute} RDCOhms
:canonical: altdss.XfmrCode.IXfmrCode.RDCOhms
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.XfmrCode.IXfmrCode.RNeut
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.XfmrCode.IXfmrCode.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.XfmrCode.IXfmrCode.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Seasons
```

````

````{py:attribute} Taps
:canonical: altdss.XfmrCode.IXfmrCode.Taps
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.XfmrCode.IXfmrCode.Thermal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Thermal
```

````

````{py:attribute} Windings
:canonical: altdss.XfmrCode.IXfmrCode.Windings
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.Windings
```

````

````{py:attribute} X12
:canonical: altdss.XfmrCode.IXfmrCode.X12
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.X12
```

````

````{py:attribute} X13
:canonical: altdss.XfmrCode.IXfmrCode.X13
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.X13
```

````

````{py:attribute} X23
:canonical: altdss.XfmrCode.IXfmrCode.X23
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.X23
```

````

````{py:attribute} XHL
:canonical: altdss.XfmrCode.IXfmrCode.XHL
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.XfmrCode.IXfmrCode.XHT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.XfmrCode.IXfmrCode.XLT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.XfmrCode.IXfmrCode.XNeut
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.XNeut
```

````

````{py:attribute} XSCArray
:canonical: altdss.XfmrCode.IXfmrCode.XSCArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.XSCArray
```

````

````{py:method} __call__()
:canonical: altdss.XfmrCode.IXfmrCode.__call__

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.XfmrCode.IXfmrCode.__contains__

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.XfmrCode.IXfmrCode.__getitem__

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.XfmrCode.IXfmrCode.__init__

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.XfmrCode.IXfmrCode.__iter__

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.XfmrCode.IXfmrCode.__len__

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.XfmrCode.IXfmrCode.batch

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, *, df=None, count: typing.Optional[int] = None, begin_edit: typing.Optional[bool] = None, **kwargs: typing_extensions.Unpack[altdss.XfmrCode.XfmrCodeBatchProperties]) -> altdss.XfmrCode.XfmrCodeBatch
:canonical: altdss.XfmrCode.IXfmrCode.batch_new

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.XfmrCode.IXfmrCode.begin_edit

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.XfmrCode.XfmrCodeBatchProperties]) -> altdss.XfmrCode.XfmrCodeBatch
:canonical: altdss.XfmrCode.IXfmrCode.edit

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.XfmrCode.IXfmrCode.end_edit

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.XfmrCode.IXfmrCode.find

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.find
```

````

````{py:attribute} kVAs
:canonical: altdss.XfmrCode.IXfmrCode.kVAs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.XfmrCode.IXfmrCode.kVs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.kVs
```

````

````{py:attribute} m
:canonical: altdss.XfmrCode.IXfmrCode.m
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.m
```

````

````{py:attribute} n
:canonical: altdss.XfmrCode.IXfmrCode.n
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.n
```

````

````{py:method} new(name: typing.AnyStr, *, begin_edit: typing.Optional[bool] = None, activate=False, **kwargs: typing_extensions.Unpack[altdss.XfmrCode.XfmrCodeProperties]) -> altdss.XfmrCode.XfmrCode
:canonical: altdss.XfmrCode.IXfmrCode.new

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.new
```

````

````{py:attribute} pctIMag
:canonical: altdss.XfmrCode.IXfmrCode.pctIMag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.XfmrCode.IXfmrCode.pctLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.XfmrCode.IXfmrCode.pctNoLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.pctNoLoadLoss
```

````

````{py:attribute} pctR
:canonical: altdss.XfmrCode.IXfmrCode.pctR
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.XfmrCode.IXfmrCode.pctRs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.pctRs
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.XfmrCode.IXfmrCode.ppm_Antifloat
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.ppm_Antifloat
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.XfmrCode.IXfmrCode.to_json

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.to_json
```

````

````{py:method} to_list()
:canonical: altdss.XfmrCode.IXfmrCode.to_list

```{autodoc2-docstring} altdss.XfmrCode.IXfmrCode.to_list
```

````

`````

`````{py:class} XfmrCode(api_util, ptr)
:canonical: altdss.XfmrCode.XfmrCode

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode
```

````{py:attribute} Conns
:canonical: altdss.XfmrCode.XfmrCode.Conns
:type: altdss.enums.Connection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Conns
```

````

````{py:attribute} Conns_str
:canonical: altdss.XfmrCode.XfmrCode.Conns_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Conns_str
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.XfmrCode.XfmrCode.EmergHkVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.EmergHkVA
```

````

````{py:attribute} FLRise
:canonical: altdss.XfmrCode.XfmrCode.FLRise
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.FLRise
```

````

````{py:method} FullName() -> str
:canonical: altdss.XfmrCode.XfmrCode.FullName

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.FullName
```

````

````{py:attribute} HSRise
:canonical: altdss.XfmrCode.XfmrCode.HSRise
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.HSRise
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.XfmrCode.XfmrCode.Like

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Like
```

````

````{py:attribute} MaxTap
:canonical: altdss.XfmrCode.XfmrCode.MaxTap
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.XfmrCode.XfmrCode.MinTap
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.MinTap
```

````

````{py:property} Name
:canonical: altdss.XfmrCode.XfmrCode.Name
:type: str

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Name
```

````

````{py:attribute} NormHkVA
:canonical: altdss.XfmrCode.XfmrCode.NormHkVA
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.NormHkVA
```

````

````{py:attribute} NumTaps
:canonical: altdss.XfmrCode.XfmrCode.NumTaps
:type: altdss.types.Int32Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.NumTaps
```

````

````{py:attribute} Phases
:canonical: altdss.XfmrCode.XfmrCode.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Phases
```

````

````{py:attribute} RDCOhms
:canonical: altdss.XfmrCode.XfmrCode.RDCOhms
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.XfmrCode.XfmrCode.RNeut
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.XfmrCode.XfmrCode.Ratings
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.XfmrCode.XfmrCode.Seasons
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Seasons
```

````

````{py:attribute} Taps
:canonical: altdss.XfmrCode.XfmrCode.Taps
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.XfmrCode.XfmrCode.Thermal
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Thermal
```

````

````{py:attribute} Windings
:canonical: altdss.XfmrCode.XfmrCode.Windings
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.Windings
```

````

````{py:attribute} X12
:canonical: altdss.XfmrCode.XfmrCode.X12
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.X12
```

````

````{py:attribute} X13
:canonical: altdss.XfmrCode.XfmrCode.X13
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.X13
```

````

````{py:attribute} X23
:canonical: altdss.XfmrCode.XfmrCode.X23
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.X23
```

````

````{py:attribute} XHL
:canonical: altdss.XfmrCode.XfmrCode.XHL
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.XfmrCode.XfmrCode.XHT
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.XfmrCode.XfmrCode.XLT
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.XfmrCode.XfmrCode.XNeut
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.XNeut
```

````

````{py:attribute} XSCArray
:canonical: altdss.XfmrCode.XfmrCode.XSCArray
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.XSCArray
```

````

````{py:method} __hash__()
:canonical: altdss.XfmrCode.XfmrCode.__hash__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.XfmrCode.XfmrCode.__init__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.XfmrCode.XfmrCode.__ne__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.XfmrCode.XfmrCode.__repr__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.XfmrCode.XfmrCode.begin_edit

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.XfmrCode.XfmrCodeProperties]) -> altdss.XfmrCode.XfmrCode
:canonical: altdss.XfmrCode.XfmrCode.edit

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.XfmrCode.XfmrCode.end_edit

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.end_edit
```

````

````{py:attribute} kVAs
:canonical: altdss.XfmrCode.XfmrCode.kVAs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.XfmrCode.XfmrCode.kVs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.kVs
```

````

````{py:attribute} m
:canonical: altdss.XfmrCode.XfmrCode.m
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.m
```

````

````{py:attribute} n
:canonical: altdss.XfmrCode.XfmrCode.n
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.n
```

````

````{py:attribute} pctIMag
:canonical: altdss.XfmrCode.XfmrCode.pctIMag
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.XfmrCode.XfmrCode.pctLoadLoss
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.XfmrCode.XfmrCode.pctNoLoadLoss
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.pctNoLoadLoss
```

````

````{py:attribute} pctR
:canonical: altdss.XfmrCode.XfmrCode.pctR
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.XfmrCode.XfmrCode.pctRs
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.pctRs
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.XfmrCode.XfmrCode.ppm_Antifloat
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.ppm_Antifloat
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.XfmrCode.XfmrCode.to_json

```{autodoc2-docstring} altdss.XfmrCode.XfmrCode.to_json
```

````

`````

`````{py:class} XfmrCodeBatch(api_util, **kwargs)
:canonical: altdss.XfmrCode.XfmrCodeBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch
```

````{py:attribute} Conns
:canonical: altdss.XfmrCode.XfmrCodeBatch.Conns
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Conns
```

````

````{py:attribute} Conns_str
:canonical: altdss.XfmrCode.XfmrCodeBatch.Conns_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Conns_str
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.XfmrCode.XfmrCodeBatch.EmergHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.EmergHkVA
```

````

````{py:attribute} FLRise
:canonical: altdss.XfmrCode.XfmrCodeBatch.FLRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.FLRise
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.XfmrCode.XfmrCodeBatch.FullName

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.FullName
```

````

````{py:attribute} HSRise
:canonical: altdss.XfmrCode.XfmrCodeBatch.HSRise
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.HSRise
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.XfmrCode.XfmrCodeBatch.Like

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Like
```

````

````{py:attribute} MaxTap
:canonical: altdss.XfmrCode.XfmrCodeBatch.MaxTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.XfmrCode.XfmrCodeBatch.MinTap
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.MinTap
```

````

````{py:property} Name
:canonical: altdss.XfmrCode.XfmrCodeBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Name
```

````

````{py:attribute} NormHkVA
:canonical: altdss.XfmrCode.XfmrCodeBatch.NormHkVA
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.NormHkVA
```

````

````{py:attribute} NumTaps
:canonical: altdss.XfmrCode.XfmrCodeBatch.NumTaps
:type: typing.List[altdss.types.Int32Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.NumTaps
```

````

````{py:attribute} Phases
:canonical: altdss.XfmrCode.XfmrCodeBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Phases
```

````

````{py:attribute} RDCOhms
:canonical: altdss.XfmrCode.XfmrCodeBatch.RDCOhms
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.XfmrCode.XfmrCodeBatch.RNeut
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.XfmrCode.XfmrCodeBatch.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.XfmrCode.XfmrCodeBatch.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Seasons
```

````

````{py:attribute} Taps
:canonical: altdss.XfmrCode.XfmrCodeBatch.Taps
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.XfmrCode.XfmrCodeBatch.Thermal
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Thermal
```

````

````{py:attribute} Windings
:canonical: altdss.XfmrCode.XfmrCodeBatch.Windings
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.Windings
```

````

````{py:attribute} X12
:canonical: altdss.XfmrCode.XfmrCodeBatch.X12
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.X12
```

````

````{py:attribute} X13
:canonical: altdss.XfmrCode.XfmrCodeBatch.X13
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.X13
```

````

````{py:attribute} X23
:canonical: altdss.XfmrCode.XfmrCodeBatch.X23
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.X23
```

````

````{py:attribute} XHL
:canonical: altdss.XfmrCode.XfmrCodeBatch.XHL
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.XfmrCode.XfmrCodeBatch.XHT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.XfmrCode.XfmrCodeBatch.XLT
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.XfmrCode.XfmrCodeBatch.XNeut
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.XNeut
```

````

````{py:attribute} XSCArray
:canonical: altdss.XfmrCode.XfmrCodeBatch.XSCArray
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.XSCArray
```

````

````{py:method} __call__()
:canonical: altdss.XfmrCode.XfmrCodeBatch.__call__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.XfmrCode.XfmrCodeBatch.__getitem__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.XfmrCode.XfmrCodeBatch.__init__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.XfmrCode.XfmrCodeBatch.__iter__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.XfmrCode.XfmrCodeBatch.__len__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.XfmrCode.XfmrCodeBatch.batch

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.XfmrCode.XfmrCodeBatch.begin_edit

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.begin_edit
```

````

````{py:method} edit(**kwargs: typing_extensions.Unpack[altdss.XfmrCode.XfmrCodeBatchProperties]) -> altdss.XfmrCode.XfmrCodeBatch
:canonical: altdss.XfmrCode.XfmrCodeBatch.edit

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.XfmrCode.XfmrCodeBatch.end_edit

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.end_edit
```

````

````{py:attribute} kVAs
:canonical: altdss.XfmrCode.XfmrCodeBatch.kVAs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.XfmrCode.XfmrCodeBatch.kVs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.kVs
```

````

````{py:attribute} m
:canonical: altdss.XfmrCode.XfmrCodeBatch.m
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.m
```

````

````{py:attribute} n
:canonical: altdss.XfmrCode.XfmrCodeBatch.n
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.n
```

````

````{py:attribute} pctIMag
:canonical: altdss.XfmrCode.XfmrCodeBatch.pctIMag
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.XfmrCode.XfmrCodeBatch.pctLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.XfmrCode.XfmrCodeBatch.pctNoLoadLoss
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.pctNoLoadLoss
```

````

````{py:attribute} pctR
:canonical: altdss.XfmrCode.XfmrCodeBatch.pctR
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.XfmrCode.XfmrCodeBatch.pctRs
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.pctRs
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.XfmrCode.XfmrCodeBatch.ppm_Antifloat
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.ppm_Antifloat
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.XfmrCode.XfmrCodeBatch.to_json

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.XfmrCode.XfmrCodeBatch.to_list

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatch.to_list
```

````

`````

`````{py:class} XfmrCodeBatchProperties()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties
```

````{py:attribute} Conns
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.Conns
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.Connection]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.Conns
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.EmergHkVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.EmergHkVA
```

````

````{py:attribute} FLRise
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.FLRise
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.FLRise
```

````

````{py:attribute} HSRise
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.HSRise
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.HSRise
```

````

````{py:attribute} Like
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.Like
```

````

````{py:attribute} MaxTap
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.MaxTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.MinTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.MinTap
```

````

````{py:attribute} NormHkVA
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.NormHkVA
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.NormHkVA
```

````

````{py:attribute} NumTaps
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.NumTaps
:type: altdss.types.Int32Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.NumTaps
```

````

````{py:attribute} Phases
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.Phases
```

````

````{py:attribute} RDCOhms
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.RDCOhms
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.RNeut
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.Seasons
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.Seasons
```

````

````{py:attribute} Taps
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.Taps
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.Thermal
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.Thermal
```

````

````{py:attribute} Windings
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.Windings
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.Windings
```

````

````{py:attribute} X12
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.X12
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.X12
```

````

````{py:attribute} X13
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.X13
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.X13
```

````

````{py:attribute} X23
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.X23
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.X23
```

````

````{py:attribute} XHL
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.XHL
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.XHT
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.XLT
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.XNeut
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.XNeut
```

````

````{py:attribute} XSCArray
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.XSCArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.XSCArray
```

````

````{py:method} __contains__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__contains__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__delattr__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__delitem__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__dir__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__format__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__ge__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__getitem__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__getstate__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__gt__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__init__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__ior__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__iter__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__le__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__len__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__lt__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__ne__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__new__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__or__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__reduce__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__repr__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__reversed__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__ror__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__setitem__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__str__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.clear

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.copy

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.get

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.items

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.items
```

````

````{py:attribute} kVAs
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.kVAs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.kVs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.kVs
```

````

````{py:method} keys()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.keys

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.keys
```

````

````{py:attribute} m
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.m
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.m
```

````

````{py:attribute} n
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.n
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.n
```

````

````{py:attribute} pctIMag
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.pctIMag
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.pctLoadLoss
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.pctNoLoadLoss
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.pctNoLoadLoss
```

````

````{py:attribute} pctR
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.pctR
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.pctRs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.pctRs
```

````

````{py:method} pop()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.pop

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.popitem

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.popitem
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.ppm_Antifloat
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.ppm_Antifloat
```

````

````{py:method} setdefault()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.setdefault

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.update

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.XfmrCode.XfmrCodeBatchProperties.values

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeBatchProperties.values
```

````

`````

`````{py:class} XfmrCodeProperties()
:canonical: altdss.XfmrCode.XfmrCodeProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties
```

````{py:attribute} Conns
:canonical: altdss.XfmrCode.XfmrCodeProperties.Conns
:type: typing.Union[typing.List[typing.Union[int, altdss.enums.Connection]], typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.Conns
```

````

````{py:attribute} EmergHkVA
:canonical: altdss.XfmrCode.XfmrCodeProperties.EmergHkVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.EmergHkVA
```

````

````{py:attribute} FLRise
:canonical: altdss.XfmrCode.XfmrCodeProperties.FLRise
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.FLRise
```

````

````{py:attribute} HSRise
:canonical: altdss.XfmrCode.XfmrCodeProperties.HSRise
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.HSRise
```

````

````{py:attribute} Like
:canonical: altdss.XfmrCode.XfmrCodeProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.Like
```

````

````{py:attribute} MaxTap
:canonical: altdss.XfmrCode.XfmrCodeProperties.MaxTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.MaxTap
```

````

````{py:attribute} MinTap
:canonical: altdss.XfmrCode.XfmrCodeProperties.MinTap
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.MinTap
```

````

````{py:attribute} NormHkVA
:canonical: altdss.XfmrCode.XfmrCodeProperties.NormHkVA
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.NormHkVA
```

````

````{py:attribute} NumTaps
:canonical: altdss.XfmrCode.XfmrCodeProperties.NumTaps
:type: altdss.types.Int32Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.NumTaps
```

````

````{py:attribute} Phases
:canonical: altdss.XfmrCode.XfmrCodeProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.Phases
```

````

````{py:attribute} RDCOhms
:canonical: altdss.XfmrCode.XfmrCodeProperties.RDCOhms
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.RDCOhms
```

````

````{py:attribute} RNeut
:canonical: altdss.XfmrCode.XfmrCodeProperties.RNeut
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.RNeut
```

````

````{py:attribute} Ratings
:canonical: altdss.XfmrCode.XfmrCodeProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.Ratings
```

````

````{py:attribute} Seasons
:canonical: altdss.XfmrCode.XfmrCodeProperties.Seasons
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.Seasons
```

````

````{py:attribute} Taps
:canonical: altdss.XfmrCode.XfmrCodeProperties.Taps
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.Taps
```

````

````{py:attribute} Thermal
:canonical: altdss.XfmrCode.XfmrCodeProperties.Thermal
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.Thermal
```

````

````{py:attribute} Windings
:canonical: altdss.XfmrCode.XfmrCodeProperties.Windings
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.Windings
```

````

````{py:attribute} X12
:canonical: altdss.XfmrCode.XfmrCodeProperties.X12
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.X12
```

````

````{py:attribute} X13
:canonical: altdss.XfmrCode.XfmrCodeProperties.X13
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.X13
```

````

````{py:attribute} X23
:canonical: altdss.XfmrCode.XfmrCodeProperties.X23
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.X23
```

````

````{py:attribute} XHL
:canonical: altdss.XfmrCode.XfmrCodeProperties.XHL
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.XHL
```

````

````{py:attribute} XHT
:canonical: altdss.XfmrCode.XfmrCodeProperties.XHT
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.XHT
```

````

````{py:attribute} XLT
:canonical: altdss.XfmrCode.XfmrCodeProperties.XLT
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.XLT
```

````

````{py:attribute} XNeut
:canonical: altdss.XfmrCode.XfmrCodeProperties.XNeut
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.XNeut
```

````

````{py:attribute} XSCArray
:canonical: altdss.XfmrCode.XfmrCodeProperties.XSCArray
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.XSCArray
```

````

````{py:method} __contains__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__contains__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__delattr__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__delitem__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__dir__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__format__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__ge__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__getattribute__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__getitem__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__getstate__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__gt__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__init__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__ior__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__iter__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__le__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__len__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__lt__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__ne__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__new__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__or__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__reduce__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__reduce_ex__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__repr__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__reversed__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__ror__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__setitem__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__sizeof__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__str__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.XfmrCode.XfmrCodeProperties.__subclasshook__

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.XfmrCode.XfmrCodeProperties.clear

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.XfmrCode.XfmrCodeProperties.copy

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.copy
```

````

````{py:method} get()
:canonical: altdss.XfmrCode.XfmrCodeProperties.get

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.get
```

````

````{py:method} items()
:canonical: altdss.XfmrCode.XfmrCodeProperties.items

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.items
```

````

````{py:attribute} kVAs
:canonical: altdss.XfmrCode.XfmrCodeProperties.kVAs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.kVAs
```

````

````{py:attribute} kVs
:canonical: altdss.XfmrCode.XfmrCodeProperties.kVs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.kVs
```

````

````{py:method} keys()
:canonical: altdss.XfmrCode.XfmrCodeProperties.keys

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.keys
```

````

````{py:attribute} m
:canonical: altdss.XfmrCode.XfmrCodeProperties.m
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.m
```

````

````{py:attribute} n
:canonical: altdss.XfmrCode.XfmrCodeProperties.n
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.n
```

````

````{py:attribute} pctIMag
:canonical: altdss.XfmrCode.XfmrCodeProperties.pctIMag
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.pctIMag
```

````

````{py:attribute} pctLoadLoss
:canonical: altdss.XfmrCode.XfmrCodeProperties.pctLoadLoss
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.pctLoadLoss
```

````

````{py:attribute} pctNoLoadLoss
:canonical: altdss.XfmrCode.XfmrCodeProperties.pctNoLoadLoss
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.pctNoLoadLoss
```

````

````{py:attribute} pctR
:canonical: altdss.XfmrCode.XfmrCodeProperties.pctR
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.pctR
```

````

````{py:attribute} pctRs
:canonical: altdss.XfmrCode.XfmrCodeProperties.pctRs
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.pctRs
```

````

````{py:method} pop()
:canonical: altdss.XfmrCode.XfmrCodeProperties.pop

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.XfmrCode.XfmrCodeProperties.popitem

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.popitem
```

````

````{py:attribute} ppm_Antifloat
:canonical: altdss.XfmrCode.XfmrCodeProperties.ppm_Antifloat
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.ppm_Antifloat
```

````

````{py:method} setdefault()
:canonical: altdss.XfmrCode.XfmrCodeProperties.setdefault

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.XfmrCode.XfmrCodeProperties.update

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.update
```

````

````{py:method} values()
:canonical: altdss.XfmrCode.XfmrCodeProperties.values

```{autodoc2-docstring} altdss.XfmrCode.XfmrCodeProperties.values
```

````

`````
