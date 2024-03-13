# {py:mod}`altdss.Spectrum`

```{py:module} altdss.Spectrum
```

```{autodoc2-docstring} altdss.Spectrum
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ISpectrum <altdss.Spectrum.ISpectrum>`
  - ```{autodoc2-docstring} altdss.Spectrum.ISpectrum
    :summary:
    ```
* - {py:obj}`Spectrum <altdss.Spectrum.Spectrum>`
  - ```{autodoc2-docstring} altdss.Spectrum.Spectrum
    :summary:
    ```
* - {py:obj}`SpectrumBatch <altdss.Spectrum.SpectrumBatch>`
  - ```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch
    :summary:
    ```
* - {py:obj}`SpectrumBatchProperties <altdss.Spectrum.SpectrumBatchProperties>`
  - ```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties
    :summary:
    ```
* - {py:obj}`SpectrumProperties <altdss.Spectrum.SpectrumProperties>`
  - ```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties
    :summary:
    ```
````

### API

`````{py:class} ISpectrum(iobj)
:canonical: altdss.Spectrum.ISpectrum

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Spectrum.SpectrumBatch`

```{autodoc2-docstring} altdss.Spectrum.ISpectrum
```

````{py:attribute} Angle
:canonical: altdss.Spectrum.ISpectrum.Angle
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.Angle
```

````

````{py:attribute} CSVFile
:canonical: altdss.Spectrum.ISpectrum.CSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.CSVFile
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Spectrum.ISpectrum.FullName

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.FullName
```

````

````{py:attribute} Harmonic
:canonical: altdss.Spectrum.ISpectrum.Harmonic
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.Harmonic
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Spectrum.ISpectrum.Like

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.Like
```

````

````{py:property} Name
:canonical: altdss.Spectrum.ISpectrum.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.Name
```

````

````{py:attribute} NumHarm
:canonical: altdss.Spectrum.ISpectrum.NumHarm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.NumHarm
```

````

````{py:method} __call__()
:canonical: altdss.Spectrum.ISpectrum.__call__

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Spectrum.ISpectrum.__contains__

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Spectrum.ISpectrum.__getitem__

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Spectrum.ISpectrum.__init__

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Spectrum.ISpectrum.__iter__

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Spectrum.ISpectrum.__len__

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Spectrum.ISpectrum.batch

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Spectrum.SpectrumBatchProperties]) -> altdss.Spectrum.SpectrumBatch
:canonical: altdss.Spectrum.ISpectrum.batch_new

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Spectrum.ISpectrum.begin_edit

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Spectrum.ISpectrum.end_edit

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Spectrum.ISpectrum.find

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Spectrum.SpectrumProperties]) -> altdss.Spectrum.Spectrum
:canonical: altdss.Spectrum.ISpectrum.new

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.new
```

````

````{py:attribute} pctMag
:canonical: altdss.Spectrum.ISpectrum.pctMag
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.pctMag
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Spectrum.ISpectrum.to_json

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Spectrum.ISpectrum.to_list

```{autodoc2-docstring} altdss.Spectrum.ISpectrum.to_list
```

````

`````

`````{py:class} Spectrum(api_util, ptr)
:canonical: altdss.Spectrum.Spectrum

Bases: {py:obj}`altdss.DSSObj.DSSObj`

```{autodoc2-docstring} altdss.Spectrum.Spectrum
```

````{py:attribute} Angle
:canonical: altdss.Spectrum.Spectrum.Angle
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.Spectrum.Angle
```

````

````{py:attribute} CSVFile
:canonical: altdss.Spectrum.Spectrum.CSVFile
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.Spectrum.CSVFile
```

````

````{py:method} FullName() -> str
:canonical: altdss.Spectrum.Spectrum.FullName

```{autodoc2-docstring} altdss.Spectrum.Spectrum.FullName
```

````

````{py:attribute} Harmonic
:canonical: altdss.Spectrum.Spectrum.Harmonic
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.Spectrum.Harmonic
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Spectrum.Spectrum.Like

```{autodoc2-docstring} altdss.Spectrum.Spectrum.Like
```

````

````{py:property} Name
:canonical: altdss.Spectrum.Spectrum.Name
:type: str

```{autodoc2-docstring} altdss.Spectrum.Spectrum.Name
```

````

````{py:attribute} NumHarm
:canonical: altdss.Spectrum.Spectrum.NumHarm
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.Spectrum.NumHarm
```

````

````{py:method} __hash__()
:canonical: altdss.Spectrum.Spectrum.__hash__

```{autodoc2-docstring} altdss.Spectrum.Spectrum.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Spectrum.Spectrum.__init__

```{autodoc2-docstring} altdss.Spectrum.Spectrum.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Spectrum.Spectrum.__ne__

```{autodoc2-docstring} altdss.Spectrum.Spectrum.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Spectrum.Spectrum.__repr__

```{autodoc2-docstring} altdss.Spectrum.Spectrum.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Spectrum.Spectrum.begin_edit

```{autodoc2-docstring} altdss.Spectrum.Spectrum.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Spectrum.Spectrum.end_edit

```{autodoc2-docstring} altdss.Spectrum.Spectrum.end_edit
```

````

````{py:attribute} pctMag
:canonical: altdss.Spectrum.Spectrum.pctMag
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.Spectrum.pctMag
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Spectrum.Spectrum.to_json

```{autodoc2-docstring} altdss.Spectrum.Spectrum.to_json
```

````

`````

`````{py:class} SpectrumBatch(api_util, **kwargs)
:canonical: altdss.Spectrum.SpectrumBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch
```

````{py:attribute} Angle
:canonical: altdss.Spectrum.SpectrumBatch.Angle
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.Angle
```

````

````{py:attribute} CSVFile
:canonical: altdss.Spectrum.SpectrumBatch.CSVFile
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.CSVFile
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Spectrum.SpectrumBatch.FullName

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.FullName
```

````

````{py:attribute} Harmonic
:canonical: altdss.Spectrum.SpectrumBatch.Harmonic
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.Harmonic
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Spectrum.SpectrumBatch.Like

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.Like
```

````

````{py:property} Name
:canonical: altdss.Spectrum.SpectrumBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.Name
```

````

````{py:attribute} NumHarm
:canonical: altdss.Spectrum.SpectrumBatch.NumHarm
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.NumHarm
```

````

````{py:method} __call__()
:canonical: altdss.Spectrum.SpectrumBatch.__call__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Spectrum.SpectrumBatch.__getitem__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Spectrum.SpectrumBatch.__init__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Spectrum.SpectrumBatch.__iter__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Spectrum.SpectrumBatch.__len__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.Spectrum.SpectrumBatch.batch

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Spectrum.SpectrumBatch.begin_edit

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Spectrum.SpectrumBatch.end_edit

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.end_edit
```

````

````{py:attribute} pctMag
:canonical: altdss.Spectrum.SpectrumBatch.pctMag
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.pctMag
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Spectrum.SpectrumBatch.to_json

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Spectrum.SpectrumBatch.to_list

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatch.to_list
```

````

`````

`````{py:class} SpectrumBatchProperties()
:canonical: altdss.Spectrum.SpectrumBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties
```

````{py:attribute} Angle
:canonical: altdss.Spectrum.SpectrumBatchProperties.Angle
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.Angle
```

````

````{py:attribute} CSVFile
:canonical: altdss.Spectrum.SpectrumBatchProperties.CSVFile
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.CSVFile
```

````

````{py:attribute} Harmonic
:canonical: altdss.Spectrum.SpectrumBatchProperties.Harmonic
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.Harmonic
```

````

````{py:attribute} Like
:canonical: altdss.Spectrum.SpectrumBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.Like
```

````

````{py:attribute} NumHarm
:canonical: altdss.Spectrum.SpectrumBatchProperties.NumHarm
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.NumHarm
```

````

````{py:method} __contains__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__contains__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__dir__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__format__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__ge__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__gt__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__init__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__ior__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__iter__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__le__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__len__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__lt__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__ne__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__new__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__or__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__repr__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__ror__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__str__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Spectrum.SpectrumBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Spectrum.SpectrumBatchProperties.clear

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Spectrum.SpectrumBatchProperties.copy

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Spectrum.SpectrumBatchProperties.get

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Spectrum.SpectrumBatchProperties.items

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Spectrum.SpectrumBatchProperties.keys

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.keys
```

````

````{py:attribute} pctMag
:canonical: altdss.Spectrum.SpectrumBatchProperties.pctMag
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.pctMag
```

````

````{py:method} pop()
:canonical: altdss.Spectrum.SpectrumBatchProperties.pop

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Spectrum.SpectrumBatchProperties.popitem

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Spectrum.SpectrumBatchProperties.setdefault

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Spectrum.SpectrumBatchProperties.update

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Spectrum.SpectrumBatchProperties.values

```{autodoc2-docstring} altdss.Spectrum.SpectrumBatchProperties.values
```

````

`````

`````{py:class} SpectrumProperties()
:canonical: altdss.Spectrum.SpectrumProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties
```

````{py:attribute} Angle
:canonical: altdss.Spectrum.SpectrumProperties.Angle
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.Angle
```

````

````{py:attribute} CSVFile
:canonical: altdss.Spectrum.SpectrumProperties.CSVFile
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.CSVFile
```

````

````{py:attribute} Harmonic
:canonical: altdss.Spectrum.SpectrumProperties.Harmonic
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.Harmonic
```

````

````{py:attribute} Like
:canonical: altdss.Spectrum.SpectrumProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.Like
```

````

````{py:attribute} NumHarm
:canonical: altdss.Spectrum.SpectrumProperties.NumHarm
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.NumHarm
```

````

````{py:method} __contains__()
:canonical: altdss.Spectrum.SpectrumProperties.__contains__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Spectrum.SpectrumProperties.__delattr__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Spectrum.SpectrumProperties.__delitem__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Spectrum.SpectrumProperties.__dir__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Spectrum.SpectrumProperties.__format__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Spectrum.SpectrumProperties.__ge__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Spectrum.SpectrumProperties.__getattribute__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Spectrum.SpectrumProperties.__getitem__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Spectrum.SpectrumProperties.__getstate__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Spectrum.SpectrumProperties.__gt__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Spectrum.SpectrumProperties.__init__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Spectrum.SpectrumProperties.__ior__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Spectrum.SpectrumProperties.__iter__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Spectrum.SpectrumProperties.__le__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Spectrum.SpectrumProperties.__len__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Spectrum.SpectrumProperties.__lt__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Spectrum.SpectrumProperties.__ne__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Spectrum.SpectrumProperties.__new__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Spectrum.SpectrumProperties.__or__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Spectrum.SpectrumProperties.__reduce__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Spectrum.SpectrumProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Spectrum.SpectrumProperties.__repr__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Spectrum.SpectrumProperties.__reversed__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Spectrum.SpectrumProperties.__ror__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Spectrum.SpectrumProperties.__setitem__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Spectrum.SpectrumProperties.__sizeof__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Spectrum.SpectrumProperties.__str__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Spectrum.SpectrumProperties.__subclasshook__

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Spectrum.SpectrumProperties.clear

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Spectrum.SpectrumProperties.copy

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Spectrum.SpectrumProperties.get

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.get
```

````

````{py:method} items()
:canonical: altdss.Spectrum.SpectrumProperties.items

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Spectrum.SpectrumProperties.keys

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.keys
```

````

````{py:attribute} pctMag
:canonical: altdss.Spectrum.SpectrumProperties.pctMag
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.pctMag
```

````

````{py:method} pop()
:canonical: altdss.Spectrum.SpectrumProperties.pop

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Spectrum.SpectrumProperties.popitem

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.Spectrum.SpectrumProperties.setdefault

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Spectrum.SpectrumProperties.update

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.update
```

````

````{py:method} values()
:canonical: altdss.Spectrum.SpectrumProperties.values

```{autodoc2-docstring} altdss.Spectrum.SpectrumProperties.values
```

````

`````
