# {py:mod}`altdss.UPFC`

```{py:module} altdss.UPFC
```

```{autodoc2-docstring} altdss.UPFC
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IUPFC <altdss.UPFC.IUPFC>`
  - ```{autodoc2-docstring} altdss.UPFC.IUPFC
    :summary:
    ```
* - {py:obj}`UPFC <altdss.UPFC.UPFC>`
  - ```{autodoc2-docstring} altdss.UPFC.UPFC
    :summary:
    ```
* - {py:obj}`UPFCBatch <altdss.UPFC.UPFCBatch>`
  - ```{autodoc2-docstring} altdss.UPFC.UPFCBatch
    :summary:
    ```
* - {py:obj}`UPFCBatchProperties <altdss.UPFC.UPFCBatchProperties>`
  - ```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties
    :summary:
    ```
* - {py:obj}`UPFCProperties <altdss.UPFC.UPFCProperties>`
  - ```{autodoc2-docstring} altdss.UPFC.UPFCProperties
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PDElement <altdss.UPFC.PDElement>`
  - ```{autodoc2-docstring} altdss.UPFC.PDElement
    :summary:
    ```
````

### API

`````{py:class} IUPFC(iobj)
:canonical: altdss.UPFC.IUPFC

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.UPFC.UPFCBatch`

```{autodoc2-docstring} altdss.UPFC.IUPFC
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFC.IUPFC.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.UPFC.IUPFC.Bus1
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.UPFC.IUPFC.Bus2
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Bus2
```

````

````{py:attribute} CLimit
:canonical: altdss.UPFC.IUPFC.CLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.CLimit
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.IUPFC.ComplexSeqCurrents

```{autodoc2-docstring} altdss.UPFC.IUPFC.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.IUPFC.ComplexSeqVoltages

```{autodoc2-docstring} altdss.UPFC.IUPFC.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.IUPFC.Currents

```{autodoc2-docstring} altdss.UPFC.IUPFC.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFC.IUPFC.CurrentsMagAng

```{autodoc2-docstring} altdss.UPFC.IUPFC.CurrentsMagAng
```

````

````{py:attribute} Element
:canonical: altdss.UPFC.IUPFC.Element
:type: typing.List[altdss.UPFC.PDElement]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.UPFC.IUPFC.Element_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFC.IUPFC.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.UPFC.IUPFC.EnergyMeter

```{autodoc2-docstring} altdss.UPFC.IUPFC.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.UPFC.IUPFC.EnergyMeterName

```{autodoc2-docstring} altdss.UPFC.IUPFC.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.UPFC.IUPFC.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.UPFC.IUPFC.FullName

```{autodoc2-docstring} altdss.UPFC.IUPFC.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.UPFC.IUPFC.GUID

```{autodoc2-docstring} altdss.UPFC.IUPFC.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.UPFC.IUPFC.Handle

```{autodoc2-docstring} altdss.UPFC.IUPFC.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.UPFC.IUPFC.HasOCPDevice

```{autodoc2-docstring} altdss.UPFC.IUPFC.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.UPFC.IUPFC.HasSwitchControl

```{autodoc2-docstring} altdss.UPFC.IUPFC.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.UPFC.IUPFC.HasVoltControl

```{autodoc2-docstring} altdss.UPFC.IUPFC.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.UPFC.IUPFC.IsIsolated

```{autodoc2-docstring} altdss.UPFC.IUPFC.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.UPFC.IUPFC.Like

```{autodoc2-docstring} altdss.UPFC.IUPFC.Like
```

````

````{py:attribute} LossCurve
:canonical: altdss.UPFC.IUPFC.LossCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.LossCurve
```

````

````{py:attribute} LossCurve_str
:canonical: altdss.UPFC.IUPFC.LossCurve_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.LossCurve_str
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.IUPFC.Losses

```{autodoc2-docstring} altdss.UPFC.IUPFC.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.UPFC.IUPFC.MaxCurrent

```{autodoc2-docstring} altdss.UPFC.IUPFC.MaxCurrent
```

````

````{py:attribute} Mode
:canonical: altdss.UPFC.IUPFC.Mode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Mode
```

````

````{py:property} Name
:canonical: altdss.UPFC.IUPFC.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.UPFC.IUPFC.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.UPFC.IUPFC.NumConductors

```{autodoc2-docstring} altdss.UPFC.IUPFC.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.UPFC.IUPFC.NumControllers

```{autodoc2-docstring} altdss.UPFC.IUPFC.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.UPFC.IUPFC.NumPhases

```{autodoc2-docstring} altdss.UPFC.IUPFC.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.UPFC.IUPFC.NumTerminals

```{autodoc2-docstring} altdss.UPFC.IUPFC.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.UPFC.IUPFC.OCPDevice

```{autodoc2-docstring} altdss.UPFC.IUPFC.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.UPFC.IUPFC.OCPDeviceIndex

```{autodoc2-docstring} altdss.UPFC.IUPFC.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.UPFC.IUPFC.OCPDeviceType

```{autodoc2-docstring} altdss.UPFC.IUPFC.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.UPFC.IUPFC.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.PF
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.IUPFC.PhaseLosses

```{autodoc2-docstring} altdss.UPFC.IUPFC.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.UPFC.IUPFC.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.IUPFC.Powers

```{autodoc2-docstring} altdss.UPFC.IUPFC.Powers
```

````

````{py:attribute} RefkV
:canonical: altdss.UPFC.IUPFC.RefkV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.RefkV
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.UPFC.IUPFC.SeqCurrents

```{autodoc2-docstring} altdss.UPFC.IUPFC.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.IUPFC.SeqPowers

```{autodoc2-docstring} altdss.UPFC.IUPFC.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.UPFC.IUPFC.SeqVoltages

```{autodoc2-docstring} altdss.UPFC.IUPFC.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.UPFC.IUPFC.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.UPFC.IUPFC.Spectrum_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Spectrum_str
```

````

````{py:attribute} Tol1
:canonical: altdss.UPFC.IUPFC.Tol1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Tol1
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.IUPFC.TotalPowers

```{autodoc2-docstring} altdss.UPFC.IUPFC.TotalPowers
```

````

````{py:attribute} VHLimit
:canonical: altdss.UPFC.IUPFC.VHLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.VHLimit
```

````

````{py:attribute} VLLimit
:canonical: altdss.UPFC.IUPFC.VLLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.VLLimit
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.IUPFC.Voltages

```{autodoc2-docstring} altdss.UPFC.IUPFC.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFC.IUPFC.VoltagesMagAng

```{autodoc2-docstring} altdss.UPFC.IUPFC.VoltagesMagAng
```

````

````{py:attribute} VpqMax
:canonical: altdss.UPFC.IUPFC.VpqMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.VpqMax
```

````

````{py:attribute} Xs
:canonical: altdss.UPFC.IUPFC.Xs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.Xs
```

````

````{py:method} __call__()
:canonical: altdss.UPFC.IUPFC.__call__

```{autodoc2-docstring} altdss.UPFC.IUPFC.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.UPFC.IUPFC.__contains__

```{autodoc2-docstring} altdss.UPFC.IUPFC.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.UPFC.IUPFC.__getitem__

```{autodoc2-docstring} altdss.UPFC.IUPFC.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.UPFC.IUPFC.__init__

```{autodoc2-docstring} altdss.UPFC.IUPFC.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.UPFC.IUPFC.__iter__

```{autodoc2-docstring} altdss.UPFC.IUPFC.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.UPFC.IUPFC.__len__

```{autodoc2-docstring} altdss.UPFC.IUPFC.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.UPFC.IUPFC.batch

```{autodoc2-docstring} altdss.UPFC.IUPFC.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.UPFC.UPFCBatchProperties]) -> altdss.UPFC.UPFCBatch
:canonical: altdss.UPFC.IUPFC.batch_new

```{autodoc2-docstring} altdss.UPFC.IUPFC.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.UPFC.IUPFC.begin_edit

```{autodoc2-docstring} altdss.UPFC.IUPFC.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.UPFC.IUPFC.end_edit

```{autodoc2-docstring} altdss.UPFC.IUPFC.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.UPFC.IUPFC.find

```{autodoc2-docstring} altdss.UPFC.IUPFC.find
```

````

````{py:attribute} kvarLimit
:canonical: altdss.UPFC.IUPFC.kvarLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.kvarLimit
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.UPFC.UPFCProperties]) -> altdss.UPFC.UPFC
:canonical: altdss.UPFC.IUPFC.new

```{autodoc2-docstring} altdss.UPFC.IUPFC.new
```

````

````{py:attribute} refkV2
:canonical: altdss.UPFC.IUPFC.refkV2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.IUPFC.refkV2
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.UPFC.IUPFC.to_json

```{autodoc2-docstring} altdss.UPFC.IUPFC.to_json
```

````

````{py:method} to_list()
:canonical: altdss.UPFC.IUPFC.to_list

```{autodoc2-docstring} altdss.UPFC.IUPFC.to_list
```

````

`````

````{py:data} PDElement
:canonical: altdss.UPFC.PDElement
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.PDElement
```

````

`````{py:class} UPFC(api_util, ptr)
:canonical: altdss.UPFC.UPFC

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PCElement.PCElementMixin`

```{autodoc2-docstring} altdss.UPFC.UPFC
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFC.UPFC.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.UPFC.UPFC.Bus1
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.UPFC.UPFC.Bus2
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Bus2
```

````

````{py:attribute} CLimit
:canonical: altdss.UPFC.UPFC.CLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.CLimit
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.UPFC.UPFC.Close

```{autodoc2-docstring} altdss.UPFC.UPFC.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFC.ComplexSeqCurrents

```{autodoc2-docstring} altdss.UPFC.UPFC.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFC.ComplexSeqVoltages

```{autodoc2-docstring} altdss.UPFC.UPFC.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFC.Currents

```{autodoc2-docstring} altdss.UPFC.UPFC.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.UPFC.UPFC.DisplayName
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.DisplayName
```

````

````{py:attribute} Element
:canonical: altdss.UPFC.UPFC.Element
:type: altdss.UPFC.PDElement
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.UPFC.UPFC.Element_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFC.UPFC.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.UPFC.UPFC.EnergyMeter

```{autodoc2-docstring} altdss.UPFC.UPFC.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.UPFC.UPFC.EnergyMeterName

```{autodoc2-docstring} altdss.UPFC.UPFC.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.UPFC.UPFC.Frequency
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Frequency
```

````

````{py:method} FullName() -> str
:canonical: altdss.UPFC.UPFC.FullName

```{autodoc2-docstring} altdss.UPFC.UPFC.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.UPFC.UPFC.GUID

```{autodoc2-docstring} altdss.UPFC.UPFC.GUID
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.UPFC.UPFC.GetVariableValue

```{autodoc2-docstring} altdss.UPFC.UPFC.GetVariableValue
```

````

````{py:method} Handle() -> int
:canonical: altdss.UPFC.UPFC.Handle

```{autodoc2-docstring} altdss.UPFC.UPFC.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.UPFC.UPFC.HasOCPDevice

```{autodoc2-docstring} altdss.UPFC.UPFC.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.UPFC.UPFC.HasSwitchControl

```{autodoc2-docstring} altdss.UPFC.UPFC.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.UPFC.UPFC.HasVoltControl

```{autodoc2-docstring} altdss.UPFC.UPFC.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.UPFC.UPFC.IsIsolated

```{autodoc2-docstring} altdss.UPFC.UPFC.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.UPFC.UPFC.IsOpen

```{autodoc2-docstring} altdss.UPFC.UPFC.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.UPFC.UPFC.Like

```{autodoc2-docstring} altdss.UPFC.UPFC.Like
```

````

````{py:attribute} LossCurve
:canonical: altdss.UPFC.UPFC.LossCurve
:type: altdss.XYcurve.XYcurve
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.LossCurve
```

````

````{py:attribute} LossCurve_str
:canonical: altdss.UPFC.UPFC.LossCurve_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.LossCurve_str
```

````

````{py:method} Losses() -> complex
:canonical: altdss.UPFC.UPFC.Losses

```{autodoc2-docstring} altdss.UPFC.UPFC.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.UPFC.UPFC.MaxCurrent

```{autodoc2-docstring} altdss.UPFC.UPFC.MaxCurrent
```

````

````{py:attribute} Mode
:canonical: altdss.UPFC.UPFC.Mode
:type: altdss.enums.UPFCMode
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Mode
```

````

````{py:property} Name
:canonical: altdss.UPFC.UPFC.Name
:type: str

```{autodoc2-docstring} altdss.UPFC.UPFC.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.UPFC.UPFC.NodeOrder

```{autodoc2-docstring} altdss.UPFC.UPFC.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.UPFC.UPFC.NodeRef

```{autodoc2-docstring} altdss.UPFC.UPFC.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.UPFC.UPFC.NumConductors

```{autodoc2-docstring} altdss.UPFC.UPFC.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.UPFC.UPFC.NumControllers

```{autodoc2-docstring} altdss.UPFC.UPFC.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.UPFC.UPFC.NumPhases

```{autodoc2-docstring} altdss.UPFC.UPFC.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.UPFC.UPFC.NumTerminals

```{autodoc2-docstring} altdss.UPFC.UPFC.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.UPFC.UPFC.OCPDevice

```{autodoc2-docstring} altdss.UPFC.UPFC.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.UPFC.UPFC.OCPDeviceIndex

```{autodoc2-docstring} altdss.UPFC.UPFC.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.UPFC.UPFC.OCPDeviceType

```{autodoc2-docstring} altdss.UPFC.UPFC.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.UPFC.UPFC.Open

```{autodoc2-docstring} altdss.UPFC.UPFC.Open
```

````

````{py:attribute} PF
:canonical: altdss.UPFC.UPFC.PF
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.PF
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFC.PhaseLosses

```{autodoc2-docstring} altdss.UPFC.UPFC.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.UPFC.UPFC.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFC.Powers

```{autodoc2-docstring} altdss.UPFC.UPFC.Powers
```

````

````{py:attribute} RefkV
:canonical: altdss.UPFC.UPFC.RefkV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.RefkV
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.UPFC.UPFC.Residuals

```{autodoc2-docstring} altdss.UPFC.UPFC.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.UPFC.UPFC.SeqCurrents

```{autodoc2-docstring} altdss.UPFC.UPFC.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFC.SeqPowers

```{autodoc2-docstring} altdss.UPFC.UPFC.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.UPFC.UPFC.SeqVoltages

```{autodoc2-docstring} altdss.UPFC.UPFC.SeqVoltages
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.UPFC.UPFC.SetVariableValue

```{autodoc2-docstring} altdss.UPFC.UPFC.SetVariableValue
```

````

````{py:attribute} Spectrum
:canonical: altdss.UPFC.UPFC.Spectrum
:type: altdss.Spectrum.Spectrum
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.UPFC.UPFC.Spectrum_str
:type: str
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Spectrum_str
```

````

````{py:attribute} Tol1
:canonical: altdss.UPFC.UPFC.Tol1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Tol1
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFC.TotalPowers

```{autodoc2-docstring} altdss.UPFC.UPFC.TotalPowers
```

````

````{py:attribute} VHLimit
:canonical: altdss.UPFC.UPFC.VHLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.VHLimit
```

````

````{py:attribute} VLLimit
:canonical: altdss.UPFC.UPFC.VLLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.VLLimit
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.UPFC.UPFC.VariableNames

```{autodoc2-docstring} altdss.UPFC.UPFC.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.UPFC.UPFC.VariableValues

```{autodoc2-docstring} altdss.UPFC.UPFC.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.UPFC.UPFC.VariablesDict

```{autodoc2-docstring} altdss.UPFC.UPFC.VariablesDict
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFC.Voltages

```{autodoc2-docstring} altdss.UPFC.UPFC.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFC.UPFC.VoltagesMagAng

```{autodoc2-docstring} altdss.UPFC.UPFC.VoltagesMagAng
```

````

````{py:attribute} VpqMax
:canonical: altdss.UPFC.UPFC.VpqMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.VpqMax
```

````

````{py:attribute} Xs
:canonical: altdss.UPFC.UPFC.Xs
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.Xs
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFC.YPrim

```{autodoc2-docstring} altdss.UPFC.UPFC.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.UPFC.UPFC.__hash__

```{autodoc2-docstring} altdss.UPFC.UPFC.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.UPFC.UPFC.__init__

```{autodoc2-docstring} altdss.UPFC.UPFC.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.UPFC.UPFC.__ne__

```{autodoc2-docstring} altdss.UPFC.UPFC.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.UPFC.UPFC.__repr__

```{autodoc2-docstring} altdss.UPFC.UPFC.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.UPFC.UPFC.begin_edit

```{autodoc2-docstring} altdss.UPFC.UPFC.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.UPFC.UPFC.end_edit

```{autodoc2-docstring} altdss.UPFC.UPFC.end_edit
```

````

````{py:attribute} kvarLimit
:canonical: altdss.UPFC.UPFC.kvarLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.kvarLimit
```

````

````{py:attribute} refkV2
:canonical: altdss.UPFC.UPFC.refkV2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFC.refkV2
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.UPFC.UPFC.to_json

```{autodoc2-docstring} altdss.UPFC.UPFC.to_json
```

````

`````

`````{py:class} UPFCBatch(api_util, **kwargs)
:canonical: altdss.UPFC.UPFCBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PCElement.PCElementBatchMixin`

```{autodoc2-docstring} altdss.UPFC.UPFCBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFC.UPFCBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.UPFC.UPFCBatch.Bus1
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.UPFC.UPFCBatch.Bus2
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Bus2
```

````

````{py:attribute} CLimit
:canonical: altdss.UPFC.UPFCBatch.CLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.CLimit
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFCBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFCBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFCBatch.Currents

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFC.UPFCBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.CurrentsMagAng
```

````

````{py:attribute} Element
:canonical: altdss.UPFC.UPFCBatch.Element
:type: typing.List[altdss.UPFC.PDElement]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.UPFC.UPFCBatch.Element_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFC.UPFCBatch.Enabled
:type: typing.List[bool]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.UPFC.UPFCBatch.EnergyMeter

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.UPFC.UPFCBatch.EnergyMeterName

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.EnergyMeterName
```

````

````{py:attribute} Frequency
:canonical: altdss.UPFC.UPFCBatch.Frequency
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Frequency
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.UPFC.UPFCBatch.FullName

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.UPFC.UPFCBatch.GUID

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.UPFC.UPFCBatch.Handle

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.UPFC.UPFCBatch.HasOCPDevice

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.UPFC.UPFCBatch.HasSwitchControl

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.UPFC.UPFCBatch.HasVoltControl

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.UPFC.UPFCBatch.IsIsolated

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.UPFC.UPFCBatch.Like

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Like
```

````

````{py:attribute} LossCurve
:canonical: altdss.UPFC.UPFCBatch.LossCurve
:type: typing.List[altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.LossCurve
```

````

````{py:attribute} LossCurve_str
:canonical: altdss.UPFC.UPFCBatch.LossCurve_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.LossCurve_str
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFCBatch.Losses

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.UPFC.UPFCBatch.MaxCurrent

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.MaxCurrent
```

````

````{py:attribute} Mode
:canonical: altdss.UPFC.UPFCBatch.Mode
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Mode
```

````

````{py:property} Name
:canonical: altdss.UPFC.UPFCBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.UPFC.UPFCBatch.NumConductors

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.UPFC.UPFCBatch.NumControllers

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.UPFC.UPFCBatch.NumPhases

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.UPFC.UPFCBatch.NumTerminals

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.UPFC.UPFCBatch.OCPDevice

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.UPFC.UPFCBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.UPFC.UPFCBatch.OCPDeviceType

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.OCPDeviceType
```

````

````{py:attribute} PF
:canonical: altdss.UPFC.UPFCBatch.PF
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.PF
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFCBatch.PhaseLosses

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.UPFC.UPFCBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFCBatch.Powers

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Powers
```

````

````{py:attribute} RefkV
:canonical: altdss.UPFC.UPFCBatch.RefkV
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.RefkV
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.UPFC.UPFCBatch.SeqCurrents

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFCBatch.SeqPowers

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.UPFC.UPFCBatch.SeqVoltages

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.SeqVoltages
```

````

````{py:attribute} Spectrum
:canonical: altdss.UPFC.UPFCBatch.Spectrum
:type: typing.List[altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Spectrum
```

````

````{py:attribute} Spectrum_str
:canonical: altdss.UPFC.UPFCBatch.Spectrum_str
:type: typing.List[str]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Spectrum_str
```

````

````{py:attribute} Tol1
:canonical: altdss.UPFC.UPFCBatch.Tol1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Tol1
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFCBatch.TotalPowers

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.TotalPowers
```

````

````{py:attribute} VHLimit
:canonical: altdss.UPFC.UPFCBatch.VHLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.VHLimit
```

````

````{py:attribute} VLLimit
:canonical: altdss.UPFC.UPFCBatch.VLLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.VLLimit
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.UPFC.UPFCBatch.Voltages

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.UPFC.UPFCBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.VoltagesMagAng
```

````

````{py:attribute} VpqMax
:canonical: altdss.UPFC.UPFCBatch.VpqMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.VpqMax
```

````

````{py:attribute} Xs
:canonical: altdss.UPFC.UPFCBatch.Xs
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.Xs
```

````

````{py:method} __call__()
:canonical: altdss.UPFC.UPFCBatch.__call__

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.UPFC.UPFCBatch.__getitem__

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.UPFC.UPFCBatch.__init__

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.UPFC.UPFCBatch.__iter__

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.UPFC.UPFCBatch.__len__

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.UPFC.UPFCBatch.begin_edit

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.UPFC.UPFCBatch.end_edit

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.end_edit
```

````

````{py:attribute} kvarLimit
:canonical: altdss.UPFC.UPFCBatch.kvarLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.kvarLimit
```

````

````{py:attribute} refkV2
:canonical: altdss.UPFC.UPFCBatch.refkV2
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.refkV2
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.UPFC.UPFCBatch.to_json

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.UPFC.UPFCBatch.to_list

```{autodoc2-docstring} altdss.UPFC.UPFCBatch.to_list
```

````

`````

`````{py:class} UPFCBatchProperties()
:canonical: altdss.UPFC.UPFCBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFC.UPFCBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.UPFC.UPFCBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.UPFC.UPFCBatchProperties.Bus2
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Bus2
```

````

````{py:attribute} CLimit
:canonical: altdss.UPFC.UPFCBatchProperties.CLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.CLimit
```

````

````{py:attribute} Element
:canonical: altdss.UPFC.UPFCBatchProperties.Element
:type: typing.Union[typing.AnyStr, altdss.UPFC.PDElement, typing.List[typing.AnyStr], typing.List[altdss.UPFC.PDElement]]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFC.UPFCBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.UPFC.UPFCBatchProperties.Frequency
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Frequency
```

````

````{py:attribute} Like
:canonical: altdss.UPFC.UPFCBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Like
```

````

````{py:attribute} LossCurve
:canonical: altdss.UPFC.UPFCBatchProperties.LossCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve, typing.List[typing.AnyStr], typing.List[altdss.XYcurve.XYcurve]]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.LossCurve
```

````

````{py:attribute} Mode
:canonical: altdss.UPFC.UPFCBatchProperties.Mode
:type: typing.Union[int, altdss.enums.UPFCMode, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Mode
```

````

````{py:attribute} PF
:canonical: altdss.UPFC.UPFCBatchProperties.PF
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.PF
```

````

````{py:attribute} Phases
:canonical: altdss.UPFC.UPFCBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Phases
```

````

````{py:attribute} RefkV
:canonical: altdss.UPFC.UPFCBatchProperties.RefkV
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.RefkV
```

````

````{py:attribute} Spectrum
:canonical: altdss.UPFC.UPFCBatchProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum, typing.List[typing.AnyStr], typing.List[altdss.Spectrum.Spectrum]]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Spectrum
```

````

````{py:attribute} Tol1
:canonical: altdss.UPFC.UPFCBatchProperties.Tol1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Tol1
```

````

````{py:attribute} VHLimit
:canonical: altdss.UPFC.UPFCBatchProperties.VHLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.VHLimit
```

````

````{py:attribute} VLLimit
:canonical: altdss.UPFC.UPFCBatchProperties.VLLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.VLLimit
```

````

````{py:attribute} VpqMax
:canonical: altdss.UPFC.UPFCBatchProperties.VpqMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.VpqMax
```

````

````{py:attribute} Xs
:canonical: altdss.UPFC.UPFCBatchProperties.Xs
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.Xs
```

````

````{py:method} __contains__()
:canonical: altdss.UPFC.UPFCBatchProperties.__contains__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.UPFC.UPFCBatchProperties.__delattr__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.UPFC.UPFCBatchProperties.__delitem__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.UPFC.UPFCBatchProperties.__dir__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.UPFC.UPFCBatchProperties.__format__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.UPFC.UPFCBatchProperties.__ge__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.UPFC.UPFCBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.UPFC.UPFCBatchProperties.__getitem__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.UPFC.UPFCBatchProperties.__getstate__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.UPFC.UPFCBatchProperties.__gt__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.UPFC.UPFCBatchProperties.__init__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.UPFC.UPFCBatchProperties.__ior__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.UPFC.UPFCBatchProperties.__iter__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.UPFC.UPFCBatchProperties.__le__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.UPFC.UPFCBatchProperties.__len__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.UPFC.UPFCBatchProperties.__lt__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.UPFC.UPFCBatchProperties.__ne__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.UPFC.UPFCBatchProperties.__new__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.UPFC.UPFCBatchProperties.__or__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.UPFC.UPFCBatchProperties.__reduce__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.UPFC.UPFCBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.UPFC.UPFCBatchProperties.__repr__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.UPFC.UPFCBatchProperties.__reversed__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.UPFC.UPFCBatchProperties.__ror__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.UPFC.UPFCBatchProperties.__setitem__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.UPFC.UPFCBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.UPFC.UPFCBatchProperties.__str__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.UPFC.UPFCBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.UPFC.UPFCBatchProperties.clear

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.UPFC.UPFCBatchProperties.copy

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.UPFC.UPFCBatchProperties.get

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.UPFC.UPFCBatchProperties.items

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.UPFC.UPFCBatchProperties.keys

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.keys
```

````

````{py:attribute} kvarLimit
:canonical: altdss.UPFC.UPFCBatchProperties.kvarLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.kvarLimit
```

````

````{py:method} pop()
:canonical: altdss.UPFC.UPFCBatchProperties.pop

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.UPFC.UPFCBatchProperties.popitem

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.popitem
```

````

````{py:attribute} refkV2
:canonical: altdss.UPFC.UPFCBatchProperties.refkV2
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.refkV2
```

````

````{py:method} setdefault()
:canonical: altdss.UPFC.UPFCBatchProperties.setdefault

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.UPFC.UPFCBatchProperties.update

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.UPFC.UPFCBatchProperties.values

```{autodoc2-docstring} altdss.UPFC.UPFCBatchProperties.values
```

````

`````

`````{py:class} UPFCProperties()
:canonical: altdss.UPFC.UPFCProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.UPFC.UPFCProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.UPFC.UPFCProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.UPFC.UPFCProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.UPFC.UPFCProperties.Bus2
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Bus2
```

````

````{py:attribute} CLimit
:canonical: altdss.UPFC.UPFCProperties.CLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.CLimit
```

````

````{py:attribute} Element
:canonical: altdss.UPFC.UPFCProperties.Element
:type: typing.Union[typing.AnyStr, altdss.UPFC.PDElement]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.UPFC.UPFCProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Enabled
```

````

````{py:attribute} Frequency
:canonical: altdss.UPFC.UPFCProperties.Frequency
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Frequency
```

````

````{py:attribute} Like
:canonical: altdss.UPFC.UPFCProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Like
```

````

````{py:attribute} LossCurve
:canonical: altdss.UPFC.UPFCProperties.LossCurve
:type: typing.Union[typing.AnyStr, altdss.XYcurve.XYcurve]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.LossCurve
```

````

````{py:attribute} Mode
:canonical: altdss.UPFC.UPFCProperties.Mode
:type: typing.Union[int, altdss.enums.UPFCMode]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Mode
```

````

````{py:attribute} PF
:canonical: altdss.UPFC.UPFCProperties.PF
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.PF
```

````

````{py:attribute} Phases
:canonical: altdss.UPFC.UPFCProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Phases
```

````

````{py:attribute} RefkV
:canonical: altdss.UPFC.UPFCProperties.RefkV
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.RefkV
```

````

````{py:attribute} Spectrum
:canonical: altdss.UPFC.UPFCProperties.Spectrum
:type: typing.Union[typing.AnyStr, altdss.Spectrum.Spectrum]
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Spectrum
```

````

````{py:attribute} Tol1
:canonical: altdss.UPFC.UPFCProperties.Tol1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Tol1
```

````

````{py:attribute} VHLimit
:canonical: altdss.UPFC.UPFCProperties.VHLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.VHLimit
```

````

````{py:attribute} VLLimit
:canonical: altdss.UPFC.UPFCProperties.VLLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.VLLimit
```

````

````{py:attribute} VpqMax
:canonical: altdss.UPFC.UPFCProperties.VpqMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.VpqMax
```

````

````{py:attribute} Xs
:canonical: altdss.UPFC.UPFCProperties.Xs
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.Xs
```

````

````{py:method} __contains__()
:canonical: altdss.UPFC.UPFCProperties.__contains__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.UPFC.UPFCProperties.__delattr__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.UPFC.UPFCProperties.__delitem__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.UPFC.UPFCProperties.__dir__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.UPFC.UPFCProperties.__format__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.UPFC.UPFCProperties.__ge__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.UPFC.UPFCProperties.__getattribute__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.UPFC.UPFCProperties.__getitem__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.UPFC.UPFCProperties.__getstate__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.UPFC.UPFCProperties.__gt__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.UPFC.UPFCProperties.__init__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.UPFC.UPFCProperties.__ior__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.UPFC.UPFCProperties.__iter__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.UPFC.UPFCProperties.__le__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.UPFC.UPFCProperties.__len__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.UPFC.UPFCProperties.__lt__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.UPFC.UPFCProperties.__ne__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.UPFC.UPFCProperties.__new__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.UPFC.UPFCProperties.__or__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.UPFC.UPFCProperties.__reduce__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.UPFC.UPFCProperties.__reduce_ex__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.UPFC.UPFCProperties.__repr__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.UPFC.UPFCProperties.__reversed__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.UPFC.UPFCProperties.__ror__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.UPFC.UPFCProperties.__setitem__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.UPFC.UPFCProperties.__sizeof__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.UPFC.UPFCProperties.__str__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.UPFC.UPFCProperties.__subclasshook__

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.UPFC.UPFCProperties.clear

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.UPFC.UPFCProperties.copy

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.copy
```

````

````{py:method} get()
:canonical: altdss.UPFC.UPFCProperties.get

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.get
```

````

````{py:method} items()
:canonical: altdss.UPFC.UPFCProperties.items

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.items
```

````

````{py:method} keys()
:canonical: altdss.UPFC.UPFCProperties.keys

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.keys
```

````

````{py:attribute} kvarLimit
:canonical: altdss.UPFC.UPFCProperties.kvarLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.kvarLimit
```

````

````{py:method} pop()
:canonical: altdss.UPFC.UPFCProperties.pop

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.UPFC.UPFCProperties.popitem

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.popitem
```

````

````{py:attribute} refkV2
:canonical: altdss.UPFC.UPFCProperties.refkV2
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.refkV2
```

````

````{py:method} setdefault()
:canonical: altdss.UPFC.UPFCProperties.setdefault

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.UPFC.UPFCProperties.update

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.update
```

````

````{py:method} values()
:canonical: altdss.UPFC.UPFCProperties.values

```{autodoc2-docstring} altdss.UPFC.UPFCProperties.values
```

````

`````
