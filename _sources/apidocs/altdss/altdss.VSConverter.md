# {py:mod}`altdss.VSConverter`

```{py:module} altdss.VSConverter
```

```{autodoc2-docstring} altdss.VSConverter
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IVSConverter <altdss.VSConverter.IVSConverter>`
  - ```{autodoc2-docstring} altdss.VSConverter.IVSConverter
    :summary:
    ```
* - {py:obj}`VSConverter <altdss.VSConverter.VSConverter>`
  - ```{autodoc2-docstring} altdss.VSConverter.VSConverter
    :summary:
    ```
* - {py:obj}`VSConverterBatch <altdss.VSConverter.VSConverterBatch>`
  - ```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch
    :summary:
    ```
* - {py:obj}`VSConverterBatchProperties <altdss.VSConverter.VSConverterBatchProperties>`
  - ```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties
    :summary:
    ```
* - {py:obj}`VSConverterProperties <altdss.VSConverter.VSConverterProperties>`
  - ```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties
    :summary:
    ```
````

### API

`````{py:class} IVSConverter(iobj)
:canonical: altdss.VSConverter.IVSConverter

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.VSConverter.VSConverterBatch`

```{autodoc2-docstring} altdss.VSConverter.IVSConverter
```

````{py:attribute} BaseFreq
:canonical: altdss.VSConverter.IVSConverter.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VSConverter.IVSConverter.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Bus1
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.IVSConverter.ComplexSeqCurrents

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.IVSConverter.ComplexSeqVoltages

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.IVSConverter.Currents

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.IVSConverter.CurrentsMagAng

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.CurrentsMagAng
```

````

````{py:attribute} Enabled
:canonical: altdss.VSConverter.IVSConverter.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.VSConverter.IVSConverter.EnergyMeter

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.VSConverter.IVSConverter.EnergyMeterName

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.VSConverter.IVSConverter.FullName

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.VSConverter.IVSConverter.GUID

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.IVSConverter.Handle

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.VSConverter.IVSConverter.HasOCPDevice

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.VSConverter.IVSConverter.HasSwitchControl

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.VSConverter.IVSConverter.HasVoltControl

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.HasVoltControl
```

````

````{py:attribute} IACMax
:canonical: altdss.VSConverter.IVSConverter.IACMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.IACMax
```

````

````{py:attribute} IDCMax
:canonical: altdss.VSConverter.IVSConverter.IDCMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.IDCMax
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.VSConverter.IVSConverter.IsIsolated

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.VSConverter.IVSConverter.Like

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.IVSConverter.Losses

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Losses
```

````

````{py:attribute} M0
:canonical: altdss.VSConverter.IVSConverter.M0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.M0
```

````

````{py:attribute} MMax
:canonical: altdss.VSConverter.IVSConverter.MMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.MMax
```

````

````{py:attribute} MMin
:canonical: altdss.VSConverter.IVSConverter.MMin
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.MMin
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.VSConverter.IVSConverter.MaxCurrent

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.MaxCurrent
```

````

````{py:attribute} NDC
:canonical: altdss.VSConverter.IVSConverter.NDC
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.NDC
```

````

````{py:property} Name
:canonical: altdss.VSConverter.IVSConverter.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.IVSConverter.NumConductors

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.IVSConverter.NumControllers

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.IVSConverter.NumPhases

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.IVSConverter.NumTerminals

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.VSConverter.IVSConverter.OCPDevice

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.IVSConverter.OCPDeviceIndex

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.VSConverter.IVSConverter.OCPDeviceType

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.OCPDeviceType
```

````

````{py:attribute} PACRef
:canonical: altdss.VSConverter.IVSConverter.PACRef
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.PACRef
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.IVSConverter.PhaseLosses

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.VSConverter.IVSConverter.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.IVSConverter.Powers

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Powers
```

````

````{py:attribute} QACRef
:canonical: altdss.VSConverter.IVSConverter.QACRef
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.QACRef
```

````

````{py:attribute} RAC
:canonical: altdss.VSConverter.IVSConverter.RAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.RAC
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.IVSConverter.SeqCurrents

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.IVSConverter.SeqPowers

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.IVSConverter.SeqVoltages

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.VSConverter.IVSConverter.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.VSConverter.IVSConverter.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.IVSConverter.TotalPowers

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.TotalPowers
```

````

````{py:attribute} VACRef
:canonical: altdss.VSConverter.IVSConverter.VACRef
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.VACRef
```

````

````{py:attribute} VDCRef
:canonical: altdss.VSConverter.IVSConverter.VDCRef
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.VDCRef
```

````

````{py:attribute} VSCMode
:canonical: altdss.VSConverter.IVSConverter.VSCMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.VSCMode
```

````

````{py:attribute} VSCMode_str
:canonical: altdss.VSConverter.IVSConverter.VSCMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.VSCMode_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.IVSConverter.Voltages

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.IVSConverter.VoltagesMagAng

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.VoltagesMagAng
```

````

````{py:attribute} XAC
:canonical: altdss.VSConverter.IVSConverter.XAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.XAC
```

````

````{py:method} __call__()
:canonical: altdss.VSConverter.IVSConverter.__call__

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.VSConverter.IVSConverter.__contains__

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.VSConverter.IVSConverter.__getitem__

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.VSConverter.IVSConverter.__init__

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.VSConverter.IVSConverter.__iter__

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.VSConverter.IVSConverter.__len__

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.VSConverter.IVSConverter.batch

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.VSConverter.VSConverterBatchProperties]) -> altdss.VSConverter.VSConverterBatch
:canonical: altdss.VSConverter.IVSConverter.batch_new

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.VSConverter.IVSConverter.begin_edit

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.begin_edit
```

````

````{py:attribute} d0
:canonical: altdss.VSConverter.IVSConverter.d0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.d0
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.VSConverter.IVSConverter.end_edit

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.VSConverter.IVSConverter.find

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.find
```

````

````{py:attribute} kVAC
:canonical: altdss.VSConverter.IVSConverter.kVAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.kVAC
```

````

````{py:attribute} kVDC
:canonical: altdss.VSConverter.IVSConverter.kVDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.VSConverter.IVSConverter.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.kW
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.VSConverter.VSConverterProperties]) -> altdss.VSConverter.VSConverter
:canonical: altdss.VSConverter.IVSConverter.new

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.VSConverter.IVSConverter.to_json

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.to_json
```

````

````{py:method} to_list()
:canonical: altdss.VSConverter.IVSConverter.to_list

```{autodoc2-docstring} altdss.VSConverter.IVSConverter.to_list
```

````

`````

`````{py:class} VSConverter(api_util, ptr)
:canonical: altdss.VSConverter.VSConverter

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`

```{autodoc2-docstring} altdss.VSConverter.VSConverter
```

````{py:attribute} BaseFreq
:canonical: altdss.VSConverter.VSConverter.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VSConverter.VSConverter.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Bus1
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.VSConverter.VSConverter.Close

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverter.ComplexSeqCurrents

```{autodoc2-docstring} altdss.VSConverter.VSConverter.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverter.ComplexSeqVoltages

```{autodoc2-docstring} altdss.VSConverter.VSConverter.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverter.Currents

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.VSConverter.VSConverter.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.DisplayName
```

````

````{py:attribute} Enabled
:canonical: altdss.VSConverter.VSConverter.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.VSConverter.VSConverter.EnergyMeter

```{autodoc2-docstring} altdss.VSConverter.VSConverter.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.VSConverter.VSConverter.EnergyMeterName

```{autodoc2-docstring} altdss.VSConverter.VSConverter.EnergyMeterName
```

````

````{py:method} FullName() -> str
:canonical: altdss.VSConverter.VSConverter.FullName

```{autodoc2-docstring} altdss.VSConverter.VSConverter.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.VSConverter.VSConverter.GUID

```{autodoc2-docstring} altdss.VSConverter.VSConverter.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.VSConverter.VSConverter.GetVariableValue

```{autodoc2-docstring} altdss.VSConverter.VSConverter.GetVariableValue
```

````

````{py:method} Handle() -> int
:canonical: altdss.VSConverter.VSConverter.Handle

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.VSConverter.VSConverter.HasOCPDevice

```{autodoc2-docstring} altdss.VSConverter.VSConverter.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.VSConverter.VSConverter.HasSwitchControl

```{autodoc2-docstring} altdss.VSConverter.VSConverter.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.VSConverter.VSConverter.HasVoltControl

```{autodoc2-docstring} altdss.VSConverter.VSConverter.HasVoltControl
```

````

````{py:attribute} IACMax
:canonical: altdss.VSConverter.VSConverter.IACMax
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.IACMax
```

````

````{py:attribute} IDCMax
:canonical: altdss.VSConverter.VSConverter.IDCMax
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.IDCMax
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.VSConverter.VSConverter.IsIsolated

```{autodoc2-docstring} altdss.VSConverter.VSConverter.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.VSConverter.VSConverter.IsOpen

```{autodoc2-docstring} altdss.VSConverter.VSConverter.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.VSConverter.VSConverter.Like

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.VSConverter.VSConverter.Losses

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Losses
```

````

````{py:attribute} M0
:canonical: altdss.VSConverter.VSConverter.M0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.M0
```

````

````{py:attribute} MMax
:canonical: altdss.VSConverter.VSConverter.MMax
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.MMax
```

````

````{py:attribute} MMin
:canonical: altdss.VSConverter.VSConverter.MMin
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.MMin
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.VSConverter.VSConverter.MaxCurrent

```{autodoc2-docstring} altdss.VSConverter.VSConverter.MaxCurrent
```

````

````{py:attribute} NDC
:canonical: altdss.VSConverter.VSConverter.NDC
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.NDC
```

````

````{py:property} Name
:canonical: altdss.VSConverter.VSConverter.Name
:type: str

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.VSConverter.NodeOrder

```{autodoc2-docstring} altdss.VSConverter.VSConverter.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.VSConverter.NodeRef

```{autodoc2-docstring} altdss.VSConverter.VSConverter.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.VSConverter.VSConverter.NumConductors

```{autodoc2-docstring} altdss.VSConverter.VSConverter.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.VSConverter.VSConverter.NumControllers

```{autodoc2-docstring} altdss.VSConverter.VSConverter.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.VSConverter.VSConverter.NumPhases

```{autodoc2-docstring} altdss.VSConverter.VSConverter.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.VSConverter.VSConverter.NumTerminals

```{autodoc2-docstring} altdss.VSConverter.VSConverter.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.VSConverter.VSConverter.OCPDevice

```{autodoc2-docstring} altdss.VSConverter.VSConverter.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.VSConverter.VSConverter.OCPDeviceIndex

```{autodoc2-docstring} altdss.VSConverter.VSConverter.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.VSConverter.VSConverter.OCPDeviceType

```{autodoc2-docstring} altdss.VSConverter.VSConverter.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.VSConverter.VSConverter.Open

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Open
```

````

````{py:attribute} PACRef
:canonical: altdss.VSConverter.VSConverter.PACRef
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.PACRef
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverter.PhaseLosses

```{autodoc2-docstring} altdss.VSConverter.VSConverter.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.VSConverter.VSConverter.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverter.Powers

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Powers
```

````

````{py:attribute} QACRef
:canonical: altdss.VSConverter.VSConverter.QACRef
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.QACRef
```

````

````{py:attribute} RAC
:canonical: altdss.VSConverter.VSConverter.RAC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.RAC
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverter.Residuals

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverter.SeqCurrents

```{autodoc2-docstring} altdss.VSConverter.VSConverter.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverter.SeqPowers

```{autodoc2-docstring} altdss.VSConverter.VSConverter.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverter.SeqVoltages

```{autodoc2-docstring} altdss.VSConverter.VSConverter.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.VSConverter.VSConverter.SetVariableValue

```{autodoc2-docstring} altdss.VSConverter.VSConverter.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.VSConverter.VSConverter.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.VSConverter.VSConverter.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverter.TotalPowers

```{autodoc2-docstring} altdss.VSConverter.VSConverter.TotalPowers
```

````

````{py:attribute} VACRef
:canonical: altdss.VSConverter.VSConverter.VACRef
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.VACRef
```

````

````{py:attribute} VDCRef
:canonical: altdss.VSConverter.VSConverter.VDCRef
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.VDCRef
```

````

````{py:attribute} VSCMode
:canonical: altdss.VSConverter.VSConverter.VSCMode
:type: altdss.enums.VSConverterControlMode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.VSCMode
```

````

````{py:attribute} VSCMode_str
:canonical: altdss.VSConverter.VSConverter.VSCMode_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.VSCMode_str
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.VSConverter.VSConverter.VariableNames

```{autodoc2-docstring} altdss.VSConverter.VSConverter.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverter.VariableValues

```{autodoc2-docstring} altdss.VSConverter.VSConverter.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.VSConverter.VSConverter.VariablesDict

```{autodoc2-docstring} altdss.VSConverter.VSConverter.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverter.Voltages

```{autodoc2-docstring} altdss.VSConverter.VSConverter.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverter.VoltagesMagAng

```{autodoc2-docstring} altdss.VSConverter.VSConverter.VoltagesMagAng
```

````

````{py:attribute} XAC
:canonical: altdss.VSConverter.VSConverter.XAC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.XAC
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverter.YPrim

```{autodoc2-docstring} altdss.VSConverter.VSConverter.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.VSConverter.VSConverter.__hash__

```{autodoc2-docstring} altdss.VSConverter.VSConverter.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.VSConverter.VSConverter.__init__

```{autodoc2-docstring} altdss.VSConverter.VSConverter.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.VSConverter.VSConverter.__ne__

```{autodoc2-docstring} altdss.VSConverter.VSConverter.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.VSConverter.VSConverter.__repr__

```{autodoc2-docstring} altdss.VSConverter.VSConverter.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.VSConverter.VSConverter.begin_edit

```{autodoc2-docstring} altdss.VSConverter.VSConverter.begin_edit
```

````

````{py:attribute} d0
:canonical: altdss.VSConverter.VSConverter.d0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.d0
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.VSConverter.VSConverter.end_edit

```{autodoc2-docstring} altdss.VSConverter.VSConverter.end_edit
```

````

````{py:attribute} kVAC
:canonical: altdss.VSConverter.VSConverter.kVAC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.kVAC
```

````

````{py:attribute} kVDC
:canonical: altdss.VSConverter.VSConverter.kVDC
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.VSConverter.VSConverter.kW
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverter.kW
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.VSConverter.VSConverter.to_json

```{autodoc2-docstring} altdss.VSConverter.VSConverter.to_json
```

````

`````

`````{py:class} VSConverterBatch(api_util, **kwargs)
:canonical: altdss.VSConverter.VSConverterBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.VSConverter.VSConverterBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VSConverter.VSConverterBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Bus1
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverterBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverterBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverterBatch.Currents

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverterBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.CurrentsMagAng
```

````

````{py:attribute} Enabled
:canonical: altdss.VSConverter.VSConverterBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.VSConverter.VSConverterBatch.EnergyMeter

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.VSConverter.VSConverterBatch.EnergyMeterName

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.VSConverter.VSConverterBatch.FullName

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.VSConverter.VSConverterBatch.GUID

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.VSConverterBatch.Handle

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.VSConverter.VSConverterBatch.HasOCPDevice

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.VSConverter.VSConverterBatch.HasSwitchControl

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.VSConverter.VSConverterBatch.HasVoltControl

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.HasVoltControl
```

````

````{py:attribute} IACMax
:canonical: altdss.VSConverter.VSConverterBatch.IACMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.IACMax
```

````

````{py:attribute} IDCMax
:canonical: altdss.VSConverter.VSConverterBatch.IDCMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.IDCMax
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.VSConverter.VSConverterBatch.IsIsolated

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.VSConverter.VSConverterBatch.Like

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverterBatch.Losses

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Losses
```

````

````{py:attribute} M0
:canonical: altdss.VSConverter.VSConverterBatch.M0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.M0
```

````

````{py:attribute} MMax
:canonical: altdss.VSConverter.VSConverterBatch.MMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.MMax
```

````

````{py:attribute} MMin
:canonical: altdss.VSConverter.VSConverterBatch.MMin
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.MMin
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverterBatch.MaxCurrent

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.MaxCurrent
```

````

````{py:attribute} NDC
:canonical: altdss.VSConverter.VSConverterBatch.NDC
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.NDC
```

````

````{py:property} Name
:canonical: altdss.VSConverter.VSConverterBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.VSConverterBatch.NumConductors

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.VSConverterBatch.NumControllers

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.VSConverterBatch.NumPhases

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.VSConverterBatch.NumTerminals

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.VSConverter.VSConverterBatch.OCPDevice

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.VSConverter.VSConverterBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.VSConverter.VSConverterBatch.OCPDeviceType

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.OCPDeviceType
```

````

````{py:attribute} PACRef
:canonical: altdss.VSConverter.VSConverterBatch.PACRef
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.PACRef
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverterBatch.PhaseLosses

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.VSConverter.VSConverterBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverterBatch.Powers

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Powers
```

````

````{py:attribute} QACRef
:canonical: altdss.VSConverter.VSConverterBatch.QACRef
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.QACRef
```

````

````{py:attribute} RAC
:canonical: altdss.VSConverter.VSConverterBatch.RAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.RAC
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverterBatch.SeqCurrents

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverterBatch.SeqPowers

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverterBatch.SeqVoltages

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.VSConverter.VSConverterBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.VSConverter.VSConverterBatch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverterBatch.TotalPowers

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.TotalPowers
```

````

````{py:attribute} VACRef
:canonical: altdss.VSConverter.VSConverterBatch.VACRef
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.VACRef
```

````

````{py:attribute} VDCRef
:canonical: altdss.VSConverter.VSConverterBatch.VDCRef
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.VDCRef
```

````

````{py:attribute} VSCMode
:canonical: altdss.VSConverter.VSConverterBatch.VSCMode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.VSCMode
```

````

````{py:attribute} VSCMode_str
:canonical: altdss.VSConverter.VSConverterBatch.VSCMode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.VSCMode_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.VSConverter.VSConverterBatch.Voltages

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.VSConverter.VSConverterBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.VoltagesMagAng
```

````

````{py:attribute} XAC
:canonical: altdss.VSConverter.VSConverterBatch.XAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.XAC
```

````

````{py:method} __call__()
:canonical: altdss.VSConverter.VSConverterBatch.__call__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.VSConverter.VSConverterBatch.__getitem__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.VSConverter.VSConverterBatch.__init__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.VSConverter.VSConverterBatch.__iter__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.VSConverter.VSConverterBatch.__len__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.VSConverter.VSConverterBatch.batch

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.VSConverter.VSConverterBatch.begin_edit

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.begin_edit
```

````

````{py:attribute} d0
:canonical: altdss.VSConverter.VSConverterBatch.d0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.d0
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.VSConverter.VSConverterBatch.end_edit

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.end_edit
```

````

````{py:attribute} kVAC
:canonical: altdss.VSConverter.VSConverterBatch.kVAC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.kVAC
```

````

````{py:attribute} kVDC
:canonical: altdss.VSConverter.VSConverterBatch.kVDC
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.VSConverter.VSConverterBatch.kW
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.kW
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.VSConverter.VSConverterBatch.to_json

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.VSConverter.VSConverterBatch.to_list

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatch.to_list
```

````

`````

`````{py:class} VSConverterBatchProperties()
:canonical: altdss.VSConverter.VSConverterBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.VSConverter.VSConverterBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VSConverter.VSConverterBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.Bus1
```

````

````{py:attribute} Enabled
:canonical: altdss.VSConverter.VSConverterBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.Enabled
```

````

````{py:attribute} IACMax
:canonical: altdss.VSConverter.VSConverterBatchProperties.IACMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.IACMax
```

````

````{py:attribute} IDCMax
:canonical: altdss.VSConverter.VSConverterBatchProperties.IDCMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.IDCMax
```

````

````{py:attribute} Like
:canonical: altdss.VSConverter.VSConverterBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.Like
```

````

````{py:attribute} M0
:canonical: altdss.VSConverter.VSConverterBatchProperties.M0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.M0
```

````

````{py:attribute} MMax
:canonical: altdss.VSConverter.VSConverterBatchProperties.MMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.MMax
```

````

````{py:attribute} MMin
:canonical: altdss.VSConverter.VSConverterBatchProperties.MMin
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.MMin
```

````

````{py:attribute} NDC
:canonical: altdss.VSConverter.VSConverterBatchProperties.NDC
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.NDC
```

````

````{py:attribute} PACRef
:canonical: altdss.VSConverter.VSConverterBatchProperties.PACRef
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.PACRef
```

````

````{py:attribute} Phases
:canonical: altdss.VSConverter.VSConverterBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.Phases
```

````

````{py:attribute} QACRef
:canonical: altdss.VSConverter.VSConverterBatchProperties.QACRef
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.QACRef
```

````

````{py:attribute} RAC
:canonical: altdss.VSConverter.VSConverterBatchProperties.RAC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.RAC
```

````

````{py:attribute} Spectrum
:canonical: altdss.VSConverter.VSConverterBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.Spectrum
```

````

````{py:attribute} VACRef
:canonical: altdss.VSConverter.VSConverterBatchProperties.VACRef
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.VACRef
```

````

````{py:attribute} VDCRef
:canonical: altdss.VSConverter.VSConverterBatchProperties.VDCRef
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.VDCRef
```

````

````{py:attribute} VSCMode
:canonical: altdss.VSConverter.VSConverterBatchProperties.VSCMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.VSConverterControlMode, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.VSConverterControlMode], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.VSCMode
```

````

````{py:attribute} XAC
:canonical: altdss.VSConverter.VSConverterBatchProperties.XAC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.XAC
```

````

````{py:method} __contains__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__contains__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__delattr__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__delitem__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__dir__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__format__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__ge__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__getitem__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__getstate__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__gt__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__init__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__ior__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__iter__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__le__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__len__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__lt__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__ne__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__new__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__or__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__reduce__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__repr__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__reversed__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__ror__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__setitem__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__str__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.VSConverter.VSConverterBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.VSConverter.VSConverterBatchProperties.clear

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.VSConverter.VSConverterBatchProperties.copy

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.copy
```

````

````{py:attribute} d0
:canonical: altdss.VSConverter.VSConverterBatchProperties.d0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.d0
```

````

````{py:method} get()
:canonical: altdss.VSConverter.VSConverterBatchProperties.get

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.VSConverter.VSConverterBatchProperties.items

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.items
```

````

````{py:attribute} kVAC
:canonical: altdss.VSConverter.VSConverterBatchProperties.kVAC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.kVAC
```

````

````{py:attribute} kVDC
:canonical: altdss.VSConverter.VSConverterBatchProperties.kVDC
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.VSConverter.VSConverterBatchProperties.kW
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.kW
```

````

````{py:method} keys()
:canonical: altdss.VSConverter.VSConverterBatchProperties.keys

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.VSConverter.VSConverterBatchProperties.pop

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.VSConverter.VSConverterBatchProperties.popitem

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.VSConverter.VSConverterBatchProperties.setdefault

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.VSConverter.VSConverterBatchProperties.update

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.VSConverter.VSConverterBatchProperties.values

```{autodoc2-docstring} altdss.VSConverter.VSConverterBatchProperties.values
```

````

`````

`````{py:class} VSConverterProperties()
:canonical: altdss.VSConverter.VSConverterProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.VSConverter.VSConverterProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VSConverter.VSConverterProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.Bus1
```

````

````{py:attribute} Enabled
:canonical: altdss.VSConverter.VSConverterProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.Enabled
```

````

````{py:attribute} IACMax
:canonical: altdss.VSConverter.VSConverterProperties.IACMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.IACMax
```

````

````{py:attribute} IDCMax
:canonical: altdss.VSConverter.VSConverterProperties.IDCMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.IDCMax
```

````

````{py:attribute} Like
:canonical: altdss.VSConverter.VSConverterProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.Like
```

````

````{py:attribute} M0
:canonical: altdss.VSConverter.VSConverterProperties.M0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.M0
```

````

````{py:attribute} MMax
:canonical: altdss.VSConverter.VSConverterProperties.MMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.MMax
```

````

````{py:attribute} MMin
:canonical: altdss.VSConverter.VSConverterProperties.MMin
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.MMin
```

````

````{py:attribute} NDC
:canonical: altdss.VSConverter.VSConverterProperties.NDC
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.NDC
```

````

````{py:attribute} PACRef
:canonical: altdss.VSConverter.VSConverterProperties.PACRef
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.PACRef
```

````

````{py:attribute} Phases
:canonical: altdss.VSConverter.VSConverterProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.Phases
```

````

````{py:attribute} QACRef
:canonical: altdss.VSConverter.VSConverterProperties.QACRef
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.QACRef
```

````

````{py:attribute} RAC
:canonical: altdss.VSConverter.VSConverterProperties.RAC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.RAC
```

````

````{py:attribute} Spectrum
:canonical: altdss.VSConverter.VSConverterProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.Spectrum
```

````

````{py:attribute} VACRef
:canonical: altdss.VSConverter.VSConverterProperties.VACRef
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.VACRef
```

````

````{py:attribute} VDCRef
:canonical: altdss.VSConverter.VSConverterProperties.VDCRef
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.VDCRef
```

````

````{py:attribute} VSCMode
:canonical: altdss.VSConverter.VSConverterProperties.VSCMode
:type: typing.Union[typing.AnyStr, int, altdss.enums.VSConverterControlMode]
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.VSCMode
```

````

````{py:attribute} XAC
:canonical: altdss.VSConverter.VSConverterProperties.XAC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.XAC
```

````

````{py:method} __contains__()
:canonical: altdss.VSConverter.VSConverterProperties.__contains__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.VSConverter.VSConverterProperties.__delattr__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.VSConverter.VSConverterProperties.__delitem__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.VSConverter.VSConverterProperties.__dir__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.VSConverter.VSConverterProperties.__format__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.VSConverter.VSConverterProperties.__ge__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.VSConverter.VSConverterProperties.__getattribute__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.VSConverter.VSConverterProperties.__getitem__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.VSConverter.VSConverterProperties.__getstate__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.VSConverter.VSConverterProperties.__gt__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.VSConverter.VSConverterProperties.__init__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.VSConverter.VSConverterProperties.__ior__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.VSConverter.VSConverterProperties.__iter__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.VSConverter.VSConverterProperties.__le__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.VSConverter.VSConverterProperties.__len__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.VSConverter.VSConverterProperties.__lt__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.VSConverter.VSConverterProperties.__ne__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.VSConverter.VSConverterProperties.__new__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.VSConverter.VSConverterProperties.__or__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.VSConverter.VSConverterProperties.__reduce__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.VSConverter.VSConverterProperties.__reduce_ex__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.VSConverter.VSConverterProperties.__repr__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.VSConverter.VSConverterProperties.__reversed__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.VSConverter.VSConverterProperties.__ror__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.VSConverter.VSConverterProperties.__setitem__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.VSConverter.VSConverterProperties.__sizeof__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.VSConverter.VSConverterProperties.__str__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.VSConverter.VSConverterProperties.__subclasshook__

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.VSConverter.VSConverterProperties.clear

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.VSConverter.VSConverterProperties.copy

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.copy
```

````

````{py:attribute} d0
:canonical: altdss.VSConverter.VSConverterProperties.d0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.d0
```

````

````{py:method} get()
:canonical: altdss.VSConverter.VSConverterProperties.get

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.get
```

````

````{py:method} items()
:canonical: altdss.VSConverter.VSConverterProperties.items

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.items
```

````

````{py:attribute} kVAC
:canonical: altdss.VSConverter.VSConverterProperties.kVAC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.kVAC
```

````

````{py:attribute} kVDC
:canonical: altdss.VSConverter.VSConverterProperties.kVDC
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.kVDC
```

````

````{py:attribute} kW
:canonical: altdss.VSConverter.VSConverterProperties.kW
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.kW
```

````

````{py:method} keys()
:canonical: altdss.VSConverter.VSConverterProperties.keys

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.VSConverter.VSConverterProperties.pop

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.VSConverter.VSConverterProperties.popitem

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.VSConverter.VSConverterProperties.setdefault

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.VSConverter.VSConverterProperties.update

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.update
```

````

````{py:method} values()
:canonical: altdss.VSConverter.VSConverterProperties.values

```{autodoc2-docstring} altdss.VSConverter.VSConverterProperties.values
```

````

`````
