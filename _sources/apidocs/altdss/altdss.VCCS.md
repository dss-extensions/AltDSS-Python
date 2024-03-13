# {py:mod}`altdss.VCCS`

```{py:module} altdss.VCCS
```

```{autodoc2-docstring} altdss.VCCS
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IVCCS <altdss.VCCS.IVCCS>`
  - ```{autodoc2-docstring} altdss.VCCS.IVCCS
    :summary:
    ```
* - {py:obj}`VCCS <altdss.VCCS.VCCS>`
  - ```{autodoc2-docstring} altdss.VCCS.VCCS
    :summary:
    ```
* - {py:obj}`VCCSBatch <altdss.VCCS.VCCSBatch>`
  - ```{autodoc2-docstring} altdss.VCCS.VCCSBatch
    :summary:
    ```
* - {py:obj}`VCCSBatchProperties <altdss.VCCS.VCCSBatchProperties>`
  - ```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties
    :summary:
    ```
* - {py:obj}`VCCSProperties <altdss.VCCS.VCCSProperties>`
  - ```{autodoc2-docstring} altdss.VCCS.VCCSProperties
    :summary:
    ```
````

### API

`````{py:class} IVCCS(iobj)
:canonical: altdss.VCCS.IVCCS

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.VCCS.VCCSBatch`

```{autodoc2-docstring} altdss.VCCS.IVCCS
```

````{py:attribute} BP1
:canonical: altdss.VCCS.IVCCS.BP1
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.BP1
```

````

````{py:attribute} BP1_str
:canonical: altdss.VCCS.IVCCS.BP1_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.BP1_str
```

````

````{py:attribute} BP2
:canonical: altdss.VCCS.IVCCS.BP2
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.BP2
```

````

````{py:attribute} BP2_str
:canonical: altdss.VCCS.IVCCS.BP2_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.BP2_str
```

````

````{py:attribute} BaseFreq
:canonical: altdss.VCCS.IVCCS.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VCCS.IVCCS.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.Bus1
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.IVCCS.ComplexSeqCurrents

```{autodoc2-docstring} altdss.VCCS.IVCCS.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.IVCCS.ComplexSeqVoltages

```{autodoc2-docstring} altdss.VCCS.IVCCS.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.IVCCS.Currents

```{autodoc2-docstring} altdss.VCCS.IVCCS.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.VCCS.IVCCS.CurrentsMagAng

```{autodoc2-docstring} altdss.VCCS.IVCCS.CurrentsMagAng
```

````

````{py:attribute} Enabled
:canonical: altdss.VCCS.IVCCS.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.VCCS.IVCCS.EnergyMeter

```{autodoc2-docstring} altdss.VCCS.IVCCS.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.VCCS.IVCCS.EnergyMeterName

```{autodoc2-docstring} altdss.VCCS.IVCCS.EnergyMeterName
```

````

````{py:attribute} FSample
:canonical: altdss.VCCS.IVCCS.FSample
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.FSample
```

````

````{py:attribute} Filter
:canonical: altdss.VCCS.IVCCS.Filter
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.Filter
```

````

````{py:attribute} Filter_str
:canonical: altdss.VCCS.IVCCS.Filter_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.Filter_str
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.VCCS.IVCCS.FullName

```{autodoc2-docstring} altdss.VCCS.IVCCS.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.VCCS.IVCCS.GUID

```{autodoc2-docstring} altdss.VCCS.IVCCS.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.VCCS.IVCCS.Handle

```{autodoc2-docstring} altdss.VCCS.IVCCS.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.VCCS.IVCCS.HasOCPDevice

```{autodoc2-docstring} altdss.VCCS.IVCCS.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.VCCS.IVCCS.HasSwitchControl

```{autodoc2-docstring} altdss.VCCS.IVCCS.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.VCCS.IVCCS.HasVoltControl

```{autodoc2-docstring} altdss.VCCS.IVCCS.HasVoltControl
```

````

````{py:attribute} IMaxpu
:canonical: altdss.VCCS.IVCCS.IMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.IMaxpu
```

````

````{py:attribute} IRMSTau
:canonical: altdss.VCCS.IVCCS.IRMSTau
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.IRMSTau
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.VCCS.IVCCS.IsIsolated

```{autodoc2-docstring} altdss.VCCS.IVCCS.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.VCCS.IVCCS.Like

```{autodoc2-docstring} altdss.VCCS.IVCCS.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.IVCCS.Losses

```{autodoc2-docstring} altdss.VCCS.IVCCS.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.VCCS.IVCCS.MaxCurrent

```{autodoc2-docstring} altdss.VCCS.IVCCS.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.VCCS.IVCCS.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.VCCS.IVCCS.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.VCCS.IVCCS.NumConductors

```{autodoc2-docstring} altdss.VCCS.IVCCS.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.VCCS.IVCCS.NumControllers

```{autodoc2-docstring} altdss.VCCS.IVCCS.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.VCCS.IVCCS.NumPhases

```{autodoc2-docstring} altdss.VCCS.IVCCS.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.VCCS.IVCCS.NumTerminals

```{autodoc2-docstring} altdss.VCCS.IVCCS.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.VCCS.IVCCS.OCPDevice

```{autodoc2-docstring} altdss.VCCS.IVCCS.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.VCCS.IVCCS.OCPDeviceIndex

```{autodoc2-docstring} altdss.VCCS.IVCCS.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.VCCS.IVCCS.OCPDeviceType

```{autodoc2-docstring} altdss.VCCS.IVCCS.OCPDeviceType
```

````

````{py:attribute} PRated
:canonical: altdss.VCCS.IVCCS.PRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.PRated
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.IVCCS.PhaseLosses

```{autodoc2-docstring} altdss.VCCS.IVCCS.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.VCCS.IVCCS.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.IVCCS.Powers

```{autodoc2-docstring} altdss.VCCS.IVCCS.Powers
```

````

````{py:attribute} Ppct
:canonical: altdss.VCCS.IVCCS.Ppct
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.Ppct
```

````

````{py:attribute} RMSMode
:canonical: altdss.VCCS.IVCCS.RMSMode
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.RMSMode
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.VCCS.IVCCS.SeqCurrents

```{autodoc2-docstring} altdss.VCCS.IVCCS.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.IVCCS.SeqPowers

```{autodoc2-docstring} altdss.VCCS.IVCCS.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.VCCS.IVCCS.SeqVoltages

```{autodoc2-docstring} altdss.VCCS.IVCCS.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.VCCS.IVCCS.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.VCCS.IVCCS.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.IVCCS.TotalPowers

```{autodoc2-docstring} altdss.VCCS.IVCCS.TotalPowers
```

````

````{py:attribute} VRMSTau
:canonical: altdss.VCCS.IVCCS.VRMSTau
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.VRMSTau
```

````

````{py:attribute} VRated
:canonical: altdss.VCCS.IVCCS.VRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.IVCCS.VRated
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.IVCCS.Voltages

```{autodoc2-docstring} altdss.VCCS.IVCCS.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.VCCS.IVCCS.VoltagesMagAng

```{autodoc2-docstring} altdss.VCCS.IVCCS.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.VCCS.IVCCS.__call__

```{autodoc2-docstring} altdss.VCCS.IVCCS.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.VCCS.IVCCS.__contains__

```{autodoc2-docstring} altdss.VCCS.IVCCS.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.VCCS.IVCCS.__getitem__

```{autodoc2-docstring} altdss.VCCS.IVCCS.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.VCCS.IVCCS.__init__

```{autodoc2-docstring} altdss.VCCS.IVCCS.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.VCCS.IVCCS.__iter__

```{autodoc2-docstring} altdss.VCCS.IVCCS.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.VCCS.IVCCS.__len__

```{autodoc2-docstring} altdss.VCCS.IVCCS.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.VCCS.IVCCS.batch

```{autodoc2-docstring} altdss.VCCS.IVCCS.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.VCCS.VCCSBatchProperties]) -> altdss.VCCS.VCCSBatch
:canonical: altdss.VCCS.IVCCS.batch_new

```{autodoc2-docstring} altdss.VCCS.IVCCS.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.VCCS.IVCCS.begin_edit

```{autodoc2-docstring} altdss.VCCS.IVCCS.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.VCCS.IVCCS.end_edit

```{autodoc2-docstring} altdss.VCCS.IVCCS.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.VCCS.IVCCS.find

```{autodoc2-docstring} altdss.VCCS.IVCCS.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.VCCS.VCCSProperties]) -> altdss.VCCS.VCCS
:canonical: altdss.VCCS.IVCCS.new

```{autodoc2-docstring} altdss.VCCS.IVCCS.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.VCCS.IVCCS.to_json

```{autodoc2-docstring} altdss.VCCS.IVCCS.to_json
```

````

````{py:method} to_list()
:canonical: altdss.VCCS.IVCCS.to_list

```{autodoc2-docstring} altdss.VCCS.IVCCS.to_list
```

````

`````

`````{py:class} VCCS(api_util, ptr)
:canonical: altdss.VCCS.VCCS

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`

```{autodoc2-docstring} altdss.VCCS.VCCS
```

````{py:attribute} BP1
:canonical: altdss.VCCS.VCCS.BP1
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.BP1
```

````

````{py:attribute} BP1_str
:canonical: altdss.VCCS.VCCS.BP1_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.BP1_str
```

````

````{py:attribute} BP2
:canonical: altdss.VCCS.VCCS.BP2
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.BP2
```

````

````{py:attribute} BP2_str
:canonical: altdss.VCCS.VCCS.BP2_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.BP2_str
```

````

````{py:attribute} BaseFreq
:canonical: altdss.VCCS.VCCS.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VCCS.VCCS.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.Bus1
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.VCCS.VCCS.Close

```{autodoc2-docstring} altdss.VCCS.VCCS.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCS.ComplexSeqCurrents

```{autodoc2-docstring} altdss.VCCS.VCCS.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCS.ComplexSeqVoltages

```{autodoc2-docstring} altdss.VCCS.VCCS.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCS.Currents

```{autodoc2-docstring} altdss.VCCS.VCCS.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.VCCS.VCCS.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.DisplayName
```

````

````{py:attribute} Enabled
:canonical: altdss.VCCS.VCCS.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.VCCS.VCCS.EnergyMeter

```{autodoc2-docstring} altdss.VCCS.VCCS.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.VCCS.VCCS.EnergyMeterName

```{autodoc2-docstring} altdss.VCCS.VCCS.EnergyMeterName
```

````

````{py:attribute} FSample
:canonical: altdss.VCCS.VCCS.FSample
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.FSample
```

````

````{py:attribute} Filter
:canonical: altdss.VCCS.VCCS.Filter
:type: altdss.XYcurve.XYcurve
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.Filter
```

````

````{py:attribute} Filter_str
:canonical: altdss.VCCS.VCCS.Filter_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.Filter_str
```

````

````{py:method} FullName() -> str
:canonical: altdss.VCCS.VCCS.FullName

```{autodoc2-docstring} altdss.VCCS.VCCS.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.VCCS.VCCS.GUID

```{autodoc2-docstring} altdss.VCCS.VCCS.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.VCCS.VCCS.GetVariableValue

```{autodoc2-docstring} altdss.VCCS.VCCS.GetVariableValue
```

````

````{py:method} Handle() -> int
:canonical: altdss.VCCS.VCCS.Handle

```{autodoc2-docstring} altdss.VCCS.VCCS.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.VCCS.VCCS.HasOCPDevice

```{autodoc2-docstring} altdss.VCCS.VCCS.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.VCCS.VCCS.HasSwitchControl

```{autodoc2-docstring} altdss.VCCS.VCCS.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.VCCS.VCCS.HasVoltControl

```{autodoc2-docstring} altdss.VCCS.VCCS.HasVoltControl
```

````

````{py:attribute} IMaxpu
:canonical: altdss.VCCS.VCCS.IMaxpu
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.IMaxpu
```

````

````{py:attribute} IRMSTau
:canonical: altdss.VCCS.VCCS.IRMSTau
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.IRMSTau
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.VCCS.VCCS.IsIsolated

```{autodoc2-docstring} altdss.VCCS.VCCS.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.VCCS.VCCS.IsOpen

```{autodoc2-docstring} altdss.VCCS.VCCS.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.VCCS.VCCS.Like

```{autodoc2-docstring} altdss.VCCS.VCCS.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.VCCS.VCCS.Losses

```{autodoc2-docstring} altdss.VCCS.VCCS.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.VCCS.VCCS.MaxCurrent

```{autodoc2-docstring} altdss.VCCS.VCCS.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.VCCS.VCCS.Name
:type: str

```{autodoc2-docstring} altdss.VCCS.VCCS.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.VCCS.VCCS.NodeOrder

```{autodoc2-docstring} altdss.VCCS.VCCS.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.VCCS.VCCS.NodeRef

```{autodoc2-docstring} altdss.VCCS.VCCS.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.VCCS.VCCS.NumConductors

```{autodoc2-docstring} altdss.VCCS.VCCS.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.VCCS.VCCS.NumControllers

```{autodoc2-docstring} altdss.VCCS.VCCS.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.VCCS.VCCS.NumPhases

```{autodoc2-docstring} altdss.VCCS.VCCS.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.VCCS.VCCS.NumTerminals

```{autodoc2-docstring} altdss.VCCS.VCCS.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.VCCS.VCCS.OCPDevice

```{autodoc2-docstring} altdss.VCCS.VCCS.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.VCCS.VCCS.OCPDeviceIndex

```{autodoc2-docstring} altdss.VCCS.VCCS.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.VCCS.VCCS.OCPDeviceType

```{autodoc2-docstring} altdss.VCCS.VCCS.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.VCCS.VCCS.Open

```{autodoc2-docstring} altdss.VCCS.VCCS.Open
```

````

````{py:attribute} PRated
:canonical: altdss.VCCS.VCCS.PRated
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.PRated
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCS.PhaseLosses

```{autodoc2-docstring} altdss.VCCS.VCCS.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.VCCS.VCCS.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCS.Powers

```{autodoc2-docstring} altdss.VCCS.VCCS.Powers
```

````

````{py:attribute} Ppct
:canonical: altdss.VCCS.VCCS.Ppct
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.Ppct
```

````

````{py:attribute} RMSMode
:canonical: altdss.VCCS.VCCS.RMSMode
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.RMSMode
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCS.Residuals

```{autodoc2-docstring} altdss.VCCS.VCCS.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCS.SeqCurrents

```{autodoc2-docstring} altdss.VCCS.VCCS.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCS.SeqPowers

```{autodoc2-docstring} altdss.VCCS.VCCS.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCS.SeqVoltages

```{autodoc2-docstring} altdss.VCCS.VCCS.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.VCCS.VCCS.SetVariableValue

```{autodoc2-docstring} altdss.VCCS.VCCS.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.VCCS.VCCS.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.VCCS.VCCS.Spectrum_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCS.TotalPowers

```{autodoc2-docstring} altdss.VCCS.VCCS.TotalPowers
```

````

````{py:attribute} VRMSTau
:canonical: altdss.VCCS.VCCS.VRMSTau
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.VRMSTau
```

````

````{py:attribute} VRated
:canonical: altdss.VCCS.VCCS.VRated
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCS.VRated
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.VCCS.VCCS.VariableNames

```{autodoc2-docstring} altdss.VCCS.VCCS.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCS.VariableValues

```{autodoc2-docstring} altdss.VCCS.VCCS.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.VCCS.VCCS.VariablesDict

```{autodoc2-docstring} altdss.VCCS.VCCS.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCS.Voltages

```{autodoc2-docstring} altdss.VCCS.VCCS.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCS.VoltagesMagAng

```{autodoc2-docstring} altdss.VCCS.VCCS.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCS.YPrim

```{autodoc2-docstring} altdss.VCCS.VCCS.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.VCCS.VCCS.__hash__

```{autodoc2-docstring} altdss.VCCS.VCCS.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.VCCS.VCCS.__init__

```{autodoc2-docstring} altdss.VCCS.VCCS.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.VCCS.VCCS.__ne__

```{autodoc2-docstring} altdss.VCCS.VCCS.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.VCCS.VCCS.__repr__

```{autodoc2-docstring} altdss.VCCS.VCCS.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.VCCS.VCCS.begin_edit

```{autodoc2-docstring} altdss.VCCS.VCCS.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.VCCS.VCCS.end_edit

```{autodoc2-docstring} altdss.VCCS.VCCS.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.VCCS.VCCS.to_json

```{autodoc2-docstring} altdss.VCCS.VCCS.to_json
```

````

`````

`````{py:class} VCCSBatch(api_util, **kwargs)
:canonical: altdss.VCCS.VCCSBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.VCCS.VCCSBatch
```

````{py:attribute} BP1
:canonical: altdss.VCCS.VCCSBatch.BP1
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.BP1
```

````

````{py:attribute} BP1_str
:canonical: altdss.VCCS.VCCSBatch.BP1_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.BP1_str
```

````

````{py:attribute} BP2
:canonical: altdss.VCCS.VCCSBatch.BP2
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.BP2
```

````

````{py:attribute} BP2_str
:canonical: altdss.VCCS.VCCSBatch.BP2_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.BP2_str
```

````

````{py:attribute} BaseFreq
:canonical: altdss.VCCS.VCCSBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VCCS.VCCSBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Bus1
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCSBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCSBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCSBatch.Currents

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCSBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.CurrentsMagAng
```

````

````{py:attribute} Enabled
:canonical: altdss.VCCS.VCCSBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.VCCS.VCCSBatch.EnergyMeter

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.VCCS.VCCSBatch.EnergyMeterName

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.EnergyMeterName
```

````

````{py:attribute} FSample
:canonical: altdss.VCCS.VCCSBatch.FSample
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.FSample
```

````

````{py:attribute} Filter
:canonical: altdss.VCCS.VCCSBatch.Filter
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Filter
```

````

````{py:attribute} Filter_str
:canonical: altdss.VCCS.VCCSBatch.Filter_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Filter_str
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.VCCS.VCCSBatch.FullName

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.VCCS.VCCSBatch.GUID

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.VCCS.VCCSBatch.Handle

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.VCCS.VCCSBatch.HasOCPDevice

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.VCCS.VCCSBatch.HasSwitchControl

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.VCCS.VCCSBatch.HasVoltControl

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.HasVoltControl
```

````

````{py:attribute} IMaxpu
:canonical: altdss.VCCS.VCCSBatch.IMaxpu
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.IMaxpu
```

````

````{py:attribute} IRMSTau
:canonical: altdss.VCCS.VCCSBatch.IRMSTau
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.IRMSTau
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.VCCS.VCCSBatch.IsIsolated

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.VCCS.VCCSBatch.Like

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCSBatch.Losses

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCSBatch.MaxCurrent

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.VCCS.VCCSBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.VCCS.VCCSBatch.NumConductors

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.VCCS.VCCSBatch.NumControllers

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.VCCS.VCCSBatch.NumPhases

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.VCCS.VCCSBatch.NumTerminals

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.VCCS.VCCSBatch.OCPDevice

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.VCCS.VCCSBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.VCCS.VCCSBatch.OCPDeviceType

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.OCPDeviceType
```

````

````{py:attribute} PRated
:canonical: altdss.VCCS.VCCSBatch.PRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.PRated
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCSBatch.PhaseLosses

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.VCCS.VCCSBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCSBatch.Powers

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Powers
```

````

````{py:attribute} Ppct
:canonical: altdss.VCCS.VCCSBatch.Ppct
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Ppct
```

````

````{py:attribute} RMSMode
:canonical: altdss.VCCS.VCCSBatch.RMSMode
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.RMSMode
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCSBatch.SeqCurrents

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCSBatch.SeqPowers

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCSBatch.SeqVoltages

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.VCCS.VCCSBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.VCCS.VCCSBatch.Spectrum_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Spectrum_str
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCSBatch.TotalPowers

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.TotalPowers
```

````

````{py:attribute} VRMSTau
:canonical: altdss.VCCS.VCCSBatch.VRMSTau
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.VRMSTau
```

````

````{py:attribute} VRated
:canonical: altdss.VCCS.VCCSBatch.VRated
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.VRated
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.VCCS.VCCSBatch.Voltages

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.VCCS.VCCSBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.VCCS.VCCSBatch.__call__

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.VCCS.VCCSBatch.__getitem__

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.VCCS.VCCSBatch.__init__

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.VCCS.VCCSBatch.__iter__

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.VCCS.VCCSBatch.__len__

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.VCCS.VCCSBatch.batch

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.VCCS.VCCSBatch.begin_edit

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.VCCS.VCCSBatch.end_edit

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.VCCS.VCCSBatch.to_json

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.VCCS.VCCSBatch.to_list

```{autodoc2-docstring} altdss.VCCS.VCCSBatch.to_list
```

````

`````

`````{py:class} VCCSBatchProperties()
:canonical: altdss.VCCS.VCCSBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties
```

````{py:attribute} BP1
:canonical: altdss.VCCS.VCCSBatchProperties.BP1
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.BP1
```

````

````{py:attribute} BP2
:canonical: altdss.VCCS.VCCSBatchProperties.BP2
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.BP2
```

````

````{py:attribute} BaseFreq
:canonical: altdss.VCCS.VCCSBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VCCS.VCCSBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.Bus1
```

````

````{py:attribute} Enabled
:canonical: altdss.VCCS.VCCSBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.Enabled
```

````

````{py:attribute} FSample
:canonical: altdss.VCCS.VCCSBatchProperties.FSample
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.FSample
```

````

````{py:attribute} Filter
:canonical: altdss.VCCS.VCCSBatchProperties.Filter
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.Filter
```

````

````{py:attribute} IMaxpu
:canonical: altdss.VCCS.VCCSBatchProperties.IMaxpu
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.IMaxpu
```

````

````{py:attribute} IRMSTau
:canonical: altdss.VCCS.VCCSBatchProperties.IRMSTau
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.IRMSTau
```

````

````{py:attribute} Like
:canonical: altdss.VCCS.VCCSBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.Like
```

````

````{py:attribute} PRated
:canonical: altdss.VCCS.VCCSBatchProperties.PRated
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.PRated
```

````

````{py:attribute} Phases
:canonical: altdss.VCCS.VCCSBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.Phases
```

````

````{py:attribute} Ppct
:canonical: altdss.VCCS.VCCSBatchProperties.Ppct
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.Ppct
```

````

````{py:attribute} RMSMode
:canonical: altdss.VCCS.VCCSBatchProperties.RMSMode
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.RMSMode
```

````

````{py:attribute} Spectrum
:canonical: altdss.VCCS.VCCSBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.Spectrum
```

````

````{py:attribute} VRMSTau
:canonical: altdss.VCCS.VCCSBatchProperties.VRMSTau
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.VRMSTau
```

````

````{py:attribute} VRated
:canonical: altdss.VCCS.VCCSBatchProperties.VRated
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.VRated
```

````

````{py:method} __contains__()
:canonical: altdss.VCCS.VCCSBatchProperties.__contains__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.VCCS.VCCSBatchProperties.__delattr__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.VCCS.VCCSBatchProperties.__delitem__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.VCCS.VCCSBatchProperties.__dir__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.VCCS.VCCSBatchProperties.__format__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.VCCS.VCCSBatchProperties.__ge__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.VCCS.VCCSBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.VCCS.VCCSBatchProperties.__getitem__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.VCCS.VCCSBatchProperties.__getstate__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.VCCS.VCCSBatchProperties.__gt__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.VCCS.VCCSBatchProperties.__init__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.VCCS.VCCSBatchProperties.__ior__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.VCCS.VCCSBatchProperties.__iter__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.VCCS.VCCSBatchProperties.__le__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.VCCS.VCCSBatchProperties.__len__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.VCCS.VCCSBatchProperties.__lt__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.VCCS.VCCSBatchProperties.__ne__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.VCCS.VCCSBatchProperties.__new__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.VCCS.VCCSBatchProperties.__or__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.VCCS.VCCSBatchProperties.__reduce__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.VCCS.VCCSBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.VCCS.VCCSBatchProperties.__repr__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.VCCS.VCCSBatchProperties.__reversed__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.VCCS.VCCSBatchProperties.__ror__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.VCCS.VCCSBatchProperties.__setitem__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.VCCS.VCCSBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.VCCS.VCCSBatchProperties.__str__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.VCCS.VCCSBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.VCCS.VCCSBatchProperties.clear

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.VCCS.VCCSBatchProperties.copy

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.VCCS.VCCSBatchProperties.get

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.VCCS.VCCSBatchProperties.items

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.VCCS.VCCSBatchProperties.keys

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.VCCS.VCCSBatchProperties.pop

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.VCCS.VCCSBatchProperties.popitem

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.VCCS.VCCSBatchProperties.setdefault

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.VCCS.VCCSBatchProperties.update

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.VCCS.VCCSBatchProperties.values

```{autodoc2-docstring} altdss.VCCS.VCCSBatchProperties.values
```

````

`````

`````{py:class} VCCSProperties()
:canonical: altdss.VCCS.VCCSProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.VCCS.VCCSProperties
```

````{py:attribute} BP1
:canonical: altdss.VCCS.VCCSProperties.BP1
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.BP1
```

````

````{py:attribute} BP2
:canonical: altdss.VCCS.VCCSProperties.BP2
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.BP2
```

````

````{py:attribute} BaseFreq
:canonical: altdss.VCCS.VCCSProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.VCCS.VCCSProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.Bus1
```

````

````{py:attribute} Enabled
:canonical: altdss.VCCS.VCCSProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.Enabled
```

````

````{py:attribute} FSample
:canonical: altdss.VCCS.VCCSProperties.FSample
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.FSample
```

````

````{py:attribute} Filter
:canonical: altdss.VCCS.VCCSProperties.Filter
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.Filter
```

````

````{py:attribute} IMaxpu
:canonical: altdss.VCCS.VCCSProperties.IMaxpu
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.IMaxpu
```

````

````{py:attribute} IRMSTau
:canonical: altdss.VCCS.VCCSProperties.IRMSTau
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.IRMSTau
```

````

````{py:attribute} Like
:canonical: altdss.VCCS.VCCSProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.Like
```

````

````{py:attribute} PRated
:canonical: altdss.VCCS.VCCSProperties.PRated
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.PRated
```

````

````{py:attribute} Phases
:canonical: altdss.VCCS.VCCSProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.Phases
```

````

````{py:attribute} Ppct
:canonical: altdss.VCCS.VCCSProperties.Ppct
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.Ppct
```

````

````{py:attribute} RMSMode
:canonical: altdss.VCCS.VCCSProperties.RMSMode
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.RMSMode
```

````

````{py:attribute} Spectrum
:canonical: altdss.VCCS.VCCSProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.Spectrum
```

````

````{py:attribute} VRMSTau
:canonical: altdss.VCCS.VCCSProperties.VRMSTau
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.VRMSTau
```

````

````{py:attribute} VRated
:canonical: altdss.VCCS.VCCSProperties.VRated
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.VRated
```

````

````{py:method} __contains__()
:canonical: altdss.VCCS.VCCSProperties.__contains__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.VCCS.VCCSProperties.__delattr__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.VCCS.VCCSProperties.__delitem__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.VCCS.VCCSProperties.__dir__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.VCCS.VCCSProperties.__format__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.VCCS.VCCSProperties.__ge__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.VCCS.VCCSProperties.__getattribute__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.VCCS.VCCSProperties.__getitem__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.VCCS.VCCSProperties.__getstate__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.VCCS.VCCSProperties.__gt__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.VCCS.VCCSProperties.__init__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.VCCS.VCCSProperties.__ior__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.VCCS.VCCSProperties.__iter__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.VCCS.VCCSProperties.__le__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.VCCS.VCCSProperties.__len__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.VCCS.VCCSProperties.__lt__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.VCCS.VCCSProperties.__ne__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.VCCS.VCCSProperties.__new__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.VCCS.VCCSProperties.__or__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.VCCS.VCCSProperties.__reduce__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.VCCS.VCCSProperties.__reduce_ex__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.VCCS.VCCSProperties.__repr__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.VCCS.VCCSProperties.__reversed__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.VCCS.VCCSProperties.__ror__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.VCCS.VCCSProperties.__setitem__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.VCCS.VCCSProperties.__sizeof__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.VCCS.VCCSProperties.__str__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.VCCS.VCCSProperties.__subclasshook__

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.VCCS.VCCSProperties.clear

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.VCCS.VCCSProperties.copy

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.copy
```

````

````{py:method} get()
:canonical: altdss.VCCS.VCCSProperties.get

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.get
```

````

````{py:method} items()
:canonical: altdss.VCCS.VCCSProperties.items

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.items
```

````

````{py:method} keys()
:canonical: altdss.VCCS.VCCSProperties.keys

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.VCCS.VCCSProperties.pop

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.VCCS.VCCSProperties.popitem

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.VCCS.VCCSProperties.setdefault

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.VCCS.VCCSProperties.update

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.update
```

````

````{py:method} values()
:canonical: altdss.VCCS.VCCSProperties.values

```{autodoc2-docstring} altdss.VCCS.VCCSProperties.values
```

````

`````
