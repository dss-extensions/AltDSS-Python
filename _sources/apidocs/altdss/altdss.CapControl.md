# {py:mod}`altdss.CapControl`

```{py:module} altdss.CapControl
```

```{autodoc2-docstring} altdss.CapControl
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CapControl <altdss.CapControl.CapControl>`
  - ```{autodoc2-docstring} altdss.CapControl.CapControl
    :summary:
    ```
* - {py:obj}`CapControlBatch <altdss.CapControl.CapControlBatch>`
  - ```{autodoc2-docstring} altdss.CapControl.CapControlBatch
    :summary:
    ```
* - {py:obj}`CapControlBatchProperties <altdss.CapControl.CapControlBatchProperties>`
  - ```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties
    :summary:
    ```
* - {py:obj}`CapControlProperties <altdss.CapControl.CapControlProperties>`
  - ```{autodoc2-docstring} altdss.CapControl.CapControlProperties
    :summary:
    ```
* - {py:obj}`ICapControl <altdss.CapControl.ICapControl>`
  - ```{autodoc2-docstring} altdss.CapControl.ICapControl
    :summary:
    ```
````

### API

`````{py:class} CapControl(api_util, ptr)
:canonical: altdss.CapControl.CapControl

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.CapControl.CapControl
```

````{py:attribute} BaseFreq
:canonical: altdss.CapControl.CapControl.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.BaseFreq
```

````

````{py:attribute} CTPhase
:canonical: altdss.CapControl.CapControl.CTPhase
:type: altdss.enums.MonitoredPhase
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.CTPhase
```

````

````{py:attribute} CTPhase_str
:canonical: altdss.CapControl.CapControl.CTPhase_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.CTPhase_str
```

````

````{py:attribute} CTRatio
:canonical: altdss.CapControl.CapControl.CTRatio
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.CTRatio
```

````

````{py:attribute} Capacitor
:canonical: altdss.CapControl.CapControl.Capacitor
:type: altdss.Capacitor.Capacitor
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.Capacitor
```

````

````{py:attribute} Capacitor_str
:canonical: altdss.CapControl.CapControl.Capacitor_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.Capacitor_str
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.CapControl.CapControl.Close

```{autodoc2-docstring} altdss.CapControl.CapControl.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.CapControl.CapControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.CapControl.CapControl.ComplexSeqVoltages
```

````

````{py:attribute} ControlSignal
:canonical: altdss.CapControl.CapControl.ControlSignal
:type: altdss.LoadShape.LoadShape
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.ControlSignal
```

````

````{py:attribute} ControlSignal_str
:canonical: altdss.CapControl.CapControl.ControlSignal_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.ControlSignal_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControl.Currents

```{autodoc2-docstring} altdss.CapControl.CapControl.Currents
```

````

````{py:attribute} DeadTime
:canonical: altdss.CapControl.CapControl.DeadTime
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.DeadTime
```

````

````{py:attribute} Delay
:canonical: altdss.CapControl.CapControl.Delay
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.Delay
```

````

````{py:attribute} DelayOff
:canonical: altdss.CapControl.CapControl.DelayOff
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.DelayOff
```

````

````{py:attribute} DisplayName
:canonical: altdss.CapControl.CapControl.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.DisplayName
```

````

````{py:attribute} Element
:canonical: altdss.CapControl.CapControl.Element
:type: altdss.DSSObj.DSSObj
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.CapControl.CapControl.Element_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.CapControl.CapControl.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.CapControl.CapControl.EventLog
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.EventLog
```

````

````{py:method} FullName() -> str
:canonical: altdss.CapControl.CapControl.FullName

```{autodoc2-docstring} altdss.CapControl.CapControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.CapControl.CapControl.GUID

```{autodoc2-docstring} altdss.CapControl.CapControl.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.CapControl.CapControl.Handle

```{autodoc2-docstring} altdss.CapControl.CapControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.CapControl.CapControl.HasOCPDevice

```{autodoc2-docstring} altdss.CapControl.CapControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.CapControl.CapControl.HasSwitchControl

```{autodoc2-docstring} altdss.CapControl.CapControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.CapControl.CapControl.HasVoltControl

```{autodoc2-docstring} altdss.CapControl.CapControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.CapControl.CapControl.IsIsolated

```{autodoc2-docstring} altdss.CapControl.CapControl.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.CapControl.CapControl.IsOpen

```{autodoc2-docstring} altdss.CapControl.CapControl.IsOpen
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.CapControl.CapControl.Like

```{autodoc2-docstring} altdss.CapControl.CapControl.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.CapControl.CapControl.Losses

```{autodoc2-docstring} altdss.CapControl.CapControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.CapControl.CapControl.MaxCurrent

```{autodoc2-docstring} altdss.CapControl.CapControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.CapControl.CapControl.Name
:type: str

```{autodoc2-docstring} altdss.CapControl.CapControl.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.CapControl.CapControl.NodeOrder

```{autodoc2-docstring} altdss.CapControl.CapControl.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.CapControl.CapControl.NodeRef

```{autodoc2-docstring} altdss.CapControl.CapControl.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.CapControl.CapControl.NumConductors

```{autodoc2-docstring} altdss.CapControl.CapControl.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.CapControl.CapControl.NumControllers

```{autodoc2-docstring} altdss.CapControl.CapControl.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.CapControl.CapControl.NumPhases

```{autodoc2-docstring} altdss.CapControl.CapControl.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.CapControl.CapControl.NumTerminals

```{autodoc2-docstring} altdss.CapControl.CapControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.CapControl.CapControl.OCPDevice

```{autodoc2-docstring} altdss.CapControl.CapControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.CapControl.CapControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.CapControl.CapControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.CapControl.CapControl.OCPDeviceType

```{autodoc2-docstring} altdss.CapControl.CapControl.OCPDeviceType
```

````

````{py:attribute} OffSetting
:canonical: altdss.CapControl.CapControl.OffSetting
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.OffSetting
```

````

````{py:attribute} OnSetting
:canonical: altdss.CapControl.CapControl.OnSetting
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.OnSetting
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.CapControl.CapControl.Open

```{autodoc2-docstring} altdss.CapControl.CapControl.Open
```

````

````{py:attribute} PTPhase
:canonical: altdss.CapControl.CapControl.PTPhase
:type: altdss.enums.MonitoredPhase
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.PTPhase
```

````

````{py:attribute} PTPhase_str
:canonical: altdss.CapControl.CapControl.PTPhase_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.PTPhase_str
```

````

````{py:attribute} PTRatio
:canonical: altdss.CapControl.CapControl.PTRatio
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.PTRatio
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControl.PhaseLosses

```{autodoc2-docstring} altdss.CapControl.CapControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControl.Powers

```{autodoc2-docstring} altdss.CapControl.CapControl.Powers
```

````

````{py:method} Reset(value: bool = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.CapControl.CapControl.Reset

```{autodoc2-docstring} altdss.CapControl.CapControl.Reset
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.CapControl.CapControl.Residuals

```{autodoc2-docstring} altdss.CapControl.CapControl.Residuals
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.CapControl.CapControl.SeqCurrents

```{autodoc2-docstring} altdss.CapControl.CapControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControl.SeqPowers

```{autodoc2-docstring} altdss.CapControl.CapControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.CapControl.CapControl.SeqVoltages

```{autodoc2-docstring} altdss.CapControl.CapControl.SeqVoltages
```

````

````{py:attribute} Terminal
:canonical: altdss.CapControl.CapControl.Terminal
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControl.TotalPowers

```{autodoc2-docstring} altdss.CapControl.CapControl.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.CapControl.CapControl.Type
:type: altdss.enums.CapControlType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.CapControl.CapControl.Type_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.Type_str
```

````

````{py:attribute} UserData
:canonical: altdss.CapControl.CapControl.UserData
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.CapControl.CapControl.UserModel
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.UserModel
```

````

````{py:attribute} VBus
:canonical: altdss.CapControl.CapControl.VBus
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.VBus
```

````

````{py:attribute} VMax
:canonical: altdss.CapControl.CapControl.VMax
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.VMax
```

````

````{py:attribute} VMin
:canonical: altdss.CapControl.CapControl.VMin
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.VMin
```

````

````{py:attribute} VoltOverride
:canonical: altdss.CapControl.CapControl.VoltOverride
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.VoltOverride
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControl.Voltages

```{autodoc2-docstring} altdss.CapControl.CapControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.CapControl.CapControl.VoltagesMagAng

```{autodoc2-docstring} altdss.CapControl.CapControl.VoltagesMagAng
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControl.YPrim

```{autodoc2-docstring} altdss.CapControl.CapControl.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.CapControl.CapControl.__hash__

```{autodoc2-docstring} altdss.CapControl.CapControl.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.CapControl.CapControl.__init__

```{autodoc2-docstring} altdss.CapControl.CapControl.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.CapControl.CapControl.__ne__

```{autodoc2-docstring} altdss.CapControl.CapControl.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.CapControl.CapControl.__repr__

```{autodoc2-docstring} altdss.CapControl.CapControl.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.CapControl.CapControl.begin_edit

```{autodoc2-docstring} altdss.CapControl.CapControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.CapControl.CapControl.end_edit

```{autodoc2-docstring} altdss.CapControl.CapControl.end_edit
```

````

````{py:attribute} pctMinkvar
:canonical: altdss.CapControl.CapControl.pctMinkvar
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControl.pctMinkvar
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.CapControl.CapControl.to_json

```{autodoc2-docstring} altdss.CapControl.CapControl.to_json
```

````

`````

`````{py:class} CapControlBatch(api_util, **kwargs)
:canonical: altdss.CapControl.CapControlBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.CapControl.CapControlBatch
```

````{py:attribute} BaseFreq
:canonical: altdss.CapControl.CapControlBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.BaseFreq
```

````

````{py:attribute} CTPhase
:canonical: altdss.CapControl.CapControlBatch.CTPhase
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.CTPhase
```

````

````{py:attribute} CTPhase_str
:canonical: altdss.CapControl.CapControlBatch.CTPhase_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.CTPhase_str
```

````

````{py:attribute} CTRatio
:canonical: altdss.CapControl.CapControlBatch.CTRatio
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.CTRatio
```

````

````{py:attribute} Capacitor
:canonical: altdss.CapControl.CapControlBatch.Capacitor
:type: typing.List[altdss.Capacitor.Capacitor]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Capacitor
```

````

````{py:attribute} Capacitor_str
:canonical: altdss.CapControl.CapControlBatch.Capacitor_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Capacitor_str
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControlBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControlBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.ComplexSeqVoltages
```

````

````{py:attribute} ControlSignal
:canonical: altdss.CapControl.CapControlBatch.ControlSignal
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.ControlSignal
```

````

````{py:attribute} ControlSignal_str
:canonical: altdss.CapControl.CapControlBatch.ControlSignal_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.ControlSignal_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControlBatch.Currents

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.CapControl.CapControlBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.CurrentsMagAng
```

````

````{py:attribute} DeadTime
:canonical: altdss.CapControl.CapControlBatch.DeadTime
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.DeadTime
```

````

````{py:attribute} Delay
:canonical: altdss.CapControl.CapControlBatch.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Delay
```

````

````{py:attribute} DelayOff
:canonical: altdss.CapControl.CapControlBatch.DelayOff
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.DelayOff
```

````

````{py:attribute} Element
:canonical: altdss.CapControl.CapControlBatch.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.CapControl.CapControlBatch.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.CapControl.CapControlBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.CapControl.CapControlBatch.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.CapControl.CapControlBatch.FullName

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.CapControl.CapControlBatch.GUID

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.CapControl.CapControlBatch.Handle

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.CapControl.CapControlBatch.HasOCPDevice

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.CapControl.CapControlBatch.HasSwitchControl

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.CapControl.CapControlBatch.HasVoltControl

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.CapControl.CapControlBatch.IsIsolated

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.CapControl.CapControlBatch.Like

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControlBatch.Losses

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.CapControl.CapControlBatch.MaxCurrent

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.CapControl.CapControlBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.CapControl.CapControlBatch.NumConductors

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.CapControl.CapControlBatch.NumControllers

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.CapControl.CapControlBatch.NumPhases

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.CapControl.CapControlBatch.NumTerminals

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.CapControl.CapControlBatch.OCPDevice

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.CapControl.CapControlBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.CapControl.CapControlBatch.OCPDeviceType

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.OCPDeviceType
```

````

````{py:attribute} OffSetting
:canonical: altdss.CapControl.CapControlBatch.OffSetting
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.OffSetting
```

````

````{py:attribute} OnSetting
:canonical: altdss.CapControl.CapControlBatch.OnSetting
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.OnSetting
```

````

````{py:attribute} PTPhase
:canonical: altdss.CapControl.CapControlBatch.PTPhase
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.PTPhase
```

````

````{py:attribute} PTPhase_str
:canonical: altdss.CapControl.CapControlBatch.PTPhase_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.PTPhase_str
```

````

````{py:attribute} PTRatio
:canonical: altdss.CapControl.CapControlBatch.PTRatio
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.PTRatio
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControlBatch.PhaseLosses

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControlBatch.Powers

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Powers
```

````

````{py:method} Reset(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.CapControl.CapControlBatch.Reset

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Reset
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.CapControl.CapControlBatch.SeqCurrents

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControlBatch.SeqPowers

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.CapControl.CapControlBatch.SeqVoltages

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.SeqVoltages
```

````

````{py:attribute} Terminal
:canonical: altdss.CapControl.CapControlBatch.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControlBatch.TotalPowers

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.CapControl.CapControlBatch.Type
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.CapControl.CapControlBatch.Type_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Type_str
```

````

````{py:attribute} UserData
:canonical: altdss.CapControl.CapControlBatch.UserData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.CapControl.CapControlBatch.UserModel
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.UserModel
```

````

````{py:attribute} VBus
:canonical: altdss.CapControl.CapControlBatch.VBus
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.VBus
```

````

````{py:attribute} VMax
:canonical: altdss.CapControl.CapControlBatch.VMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.VMax
```

````

````{py:attribute} VMin
:canonical: altdss.CapControl.CapControlBatch.VMin
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.VMin
```

````

````{py:attribute} VoltOverride
:canonical: altdss.CapControl.CapControlBatch.VoltOverride
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.VoltOverride
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.CapControlBatch.Voltages

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.CapControl.CapControlBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.CapControl.CapControlBatch.__call__

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.CapControl.CapControlBatch.__getitem__

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.CapControl.CapControlBatch.__init__

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.CapControl.CapControlBatch.__iter__

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.CapControl.CapControlBatch.__len__

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.CapControl.CapControlBatch.begin_edit

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.CapControl.CapControlBatch.end_edit

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.end_edit
```

````

````{py:attribute} pctMinkvar
:canonical: altdss.CapControl.CapControlBatch.pctMinkvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.pctMinkvar
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.CapControl.CapControlBatch.to_json

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.CapControl.CapControlBatch.to_list

```{autodoc2-docstring} altdss.CapControl.CapControlBatch.to_list
```

````

`````

`````{py:class} CapControlBatchProperties()
:canonical: altdss.CapControl.CapControlBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.CapControl.CapControlBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.BaseFreq
```

````

````{py:attribute} CTPhase
:canonical: altdss.CapControl.CapControlBatchProperties.CTPhase
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitoredPhase, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.MonitoredPhase], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.CTPhase
```

````

````{py:attribute} CTRatio
:canonical: altdss.CapControl.CapControlBatchProperties.CTRatio
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.CTRatio
```

````

````{py:attribute} Capacitor
:canonical: altdss.CapControl.CapControlBatchProperties.Capacitor
:type: typing.Union[typing.AnyStr, altdss.Capacitor.Capacitor, typing.List[typing.AnyStr], typing.List[altdss.Capacitor.Capacitor]]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.Capacitor
```

````

````{py:attribute} ControlSignal
:canonical: altdss.CapControl.CapControlBatchProperties.ControlSignal
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape, typing.List[typing.AnyStr], typing.List[altdss.LoadShape.LoadShape]]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.ControlSignal
```

````

````{py:attribute} DeadTime
:canonical: altdss.CapControl.CapControlBatchProperties.DeadTime
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.DeadTime
```

````

````{py:attribute} Delay
:canonical: altdss.CapControl.CapControlBatchProperties.Delay
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.Delay
```

````

````{py:attribute} DelayOff
:canonical: altdss.CapControl.CapControlBatchProperties.DelayOff
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.DelayOff
```

````

````{py:attribute} Element
:canonical: altdss.CapControl.CapControlBatchProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj, typing.List[typing.AnyStr], typing.List[altdss.DSSObj.DSSObj]]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.CapControl.CapControlBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.CapControl.CapControlBatchProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.EventLog
```

````

````{py:attribute} Like
:canonical: altdss.CapControl.CapControlBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.Like
```

````

````{py:attribute} OffSetting
:canonical: altdss.CapControl.CapControlBatchProperties.OffSetting
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.OffSetting
```

````

````{py:attribute} OnSetting
:canonical: altdss.CapControl.CapControlBatchProperties.OnSetting
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.OnSetting
```

````

````{py:attribute} PTPhase
:canonical: altdss.CapControl.CapControlBatchProperties.PTPhase
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitoredPhase, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.MonitoredPhase], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.PTPhase
```

````

````{py:attribute} PTRatio
:canonical: altdss.CapControl.CapControlBatchProperties.PTRatio
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.PTRatio
```

````

````{py:attribute} Reset
:canonical: altdss.CapControl.CapControlBatchProperties.Reset
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.Reset
```

````

````{py:attribute} Terminal
:canonical: altdss.CapControl.CapControlBatchProperties.Terminal
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.Terminal
```

````

````{py:attribute} Type
:canonical: altdss.CapControl.CapControlBatchProperties.Type
:type: typing.Union[typing.AnyStr, int, altdss.enums.CapControlType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.CapControlType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.Type
```

````

````{py:attribute} UserData
:canonical: altdss.CapControl.CapControlBatchProperties.UserData
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.CapControl.CapControlBatchProperties.UserModel
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.UserModel
```

````

````{py:attribute} VBus
:canonical: altdss.CapControl.CapControlBatchProperties.VBus
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.VBus
```

````

````{py:attribute} VMax
:canonical: altdss.CapControl.CapControlBatchProperties.VMax
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.VMax
```

````

````{py:attribute} VMin
:canonical: altdss.CapControl.CapControlBatchProperties.VMin
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.VMin
```

````

````{py:attribute} VoltOverride
:canonical: altdss.CapControl.CapControlBatchProperties.VoltOverride
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.VoltOverride
```

````

````{py:method} __contains__()
:canonical: altdss.CapControl.CapControlBatchProperties.__contains__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.CapControl.CapControlBatchProperties.__delattr__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.CapControl.CapControlBatchProperties.__delitem__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.CapControl.CapControlBatchProperties.__dir__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.CapControl.CapControlBatchProperties.__format__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.CapControl.CapControlBatchProperties.__ge__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.CapControl.CapControlBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.CapControl.CapControlBatchProperties.__getitem__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.CapControl.CapControlBatchProperties.__getstate__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.CapControl.CapControlBatchProperties.__gt__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.CapControl.CapControlBatchProperties.__init__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.CapControl.CapControlBatchProperties.__ior__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.CapControl.CapControlBatchProperties.__iter__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.CapControl.CapControlBatchProperties.__le__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.CapControl.CapControlBatchProperties.__len__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.CapControl.CapControlBatchProperties.__lt__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.CapControl.CapControlBatchProperties.__ne__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.CapControl.CapControlBatchProperties.__new__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.CapControl.CapControlBatchProperties.__or__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.CapControl.CapControlBatchProperties.__reduce__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.CapControl.CapControlBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.CapControl.CapControlBatchProperties.__repr__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.CapControl.CapControlBatchProperties.__reversed__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.CapControl.CapControlBatchProperties.__ror__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.CapControl.CapControlBatchProperties.__setitem__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.CapControl.CapControlBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.CapControl.CapControlBatchProperties.__str__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.CapControl.CapControlBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.CapControl.CapControlBatchProperties.clear

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.CapControl.CapControlBatchProperties.copy

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.CapControl.CapControlBatchProperties.get

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.CapControl.CapControlBatchProperties.items

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.CapControl.CapControlBatchProperties.keys

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.keys
```

````

````{py:attribute} pctMinkvar
:canonical: altdss.CapControl.CapControlBatchProperties.pctMinkvar
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.pctMinkvar
```

````

````{py:method} pop()
:canonical: altdss.CapControl.CapControlBatchProperties.pop

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.CapControl.CapControlBatchProperties.popitem

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.CapControl.CapControlBatchProperties.setdefault

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.CapControl.CapControlBatchProperties.update

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.CapControl.CapControlBatchProperties.values

```{autodoc2-docstring} altdss.CapControl.CapControlBatchProperties.values
```

````

`````

`````{py:class} CapControlProperties()
:canonical: altdss.CapControl.CapControlProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.CapControl.CapControlProperties
```

````{py:attribute} BaseFreq
:canonical: altdss.CapControl.CapControlProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.BaseFreq
```

````

````{py:attribute} CTPhase
:canonical: altdss.CapControl.CapControlProperties.CTPhase
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitoredPhase]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.CTPhase
```

````

````{py:attribute} CTRatio
:canonical: altdss.CapControl.CapControlProperties.CTRatio
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.CTRatio
```

````

````{py:attribute} Capacitor
:canonical: altdss.CapControl.CapControlProperties.Capacitor
:type: typing.Union[typing.AnyStr, altdss.Capacitor.Capacitor]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.Capacitor
```

````

````{py:attribute} ControlSignal
:canonical: altdss.CapControl.CapControlProperties.ControlSignal
:type: typing.Union[typing.AnyStr, altdss.LoadShape.LoadShape]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.ControlSignal
```

````

````{py:attribute} DeadTime
:canonical: altdss.CapControl.CapControlProperties.DeadTime
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.DeadTime
```

````

````{py:attribute} Delay
:canonical: altdss.CapControl.CapControlProperties.Delay
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.Delay
```

````

````{py:attribute} DelayOff
:canonical: altdss.CapControl.CapControlProperties.DelayOff
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.DelayOff
```

````

````{py:attribute} Element
:canonical: altdss.CapControl.CapControlProperties.Element
:type: typing.Union[typing.AnyStr, altdss.DSSObj.DSSObj]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.Element
```

````

````{py:attribute} Enabled
:canonical: altdss.CapControl.CapControlProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.CapControl.CapControlProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.EventLog
```

````

````{py:attribute} Like
:canonical: altdss.CapControl.CapControlProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.Like
```

````

````{py:attribute} OffSetting
:canonical: altdss.CapControl.CapControlProperties.OffSetting
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.OffSetting
```

````

````{py:attribute} OnSetting
:canonical: altdss.CapControl.CapControlProperties.OnSetting
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.OnSetting
```

````

````{py:attribute} PTPhase
:canonical: altdss.CapControl.CapControlProperties.PTPhase
:type: typing.Union[typing.AnyStr, int, altdss.enums.MonitoredPhase]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.PTPhase
```

````

````{py:attribute} PTRatio
:canonical: altdss.CapControl.CapControlProperties.PTRatio
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.PTRatio
```

````

````{py:attribute} Reset
:canonical: altdss.CapControl.CapControlProperties.Reset
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.Reset
```

````

````{py:attribute} Terminal
:canonical: altdss.CapControl.CapControlProperties.Terminal
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.Terminal
```

````

````{py:attribute} Type
:canonical: altdss.CapControl.CapControlProperties.Type
:type: typing.Union[typing.AnyStr, int, altdss.enums.CapControlType]
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.Type
```

````

````{py:attribute} UserData
:canonical: altdss.CapControl.CapControlProperties.UserData
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.CapControl.CapControlProperties.UserModel
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.UserModel
```

````

````{py:attribute} VBus
:canonical: altdss.CapControl.CapControlProperties.VBus
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.VBus
```

````

````{py:attribute} VMax
:canonical: altdss.CapControl.CapControlProperties.VMax
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.VMax
```

````

````{py:attribute} VMin
:canonical: altdss.CapControl.CapControlProperties.VMin
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.VMin
```

````

````{py:attribute} VoltOverride
:canonical: altdss.CapControl.CapControlProperties.VoltOverride
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.VoltOverride
```

````

````{py:method} __contains__()
:canonical: altdss.CapControl.CapControlProperties.__contains__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.CapControl.CapControlProperties.__delattr__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.CapControl.CapControlProperties.__delitem__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.CapControl.CapControlProperties.__dir__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.CapControl.CapControlProperties.__format__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.CapControl.CapControlProperties.__ge__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.CapControl.CapControlProperties.__getattribute__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.CapControl.CapControlProperties.__getitem__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.CapControl.CapControlProperties.__getstate__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.CapControl.CapControlProperties.__gt__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.CapControl.CapControlProperties.__init__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.CapControl.CapControlProperties.__ior__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.CapControl.CapControlProperties.__iter__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.CapControl.CapControlProperties.__le__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.CapControl.CapControlProperties.__len__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.CapControl.CapControlProperties.__lt__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.CapControl.CapControlProperties.__ne__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.CapControl.CapControlProperties.__new__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.CapControl.CapControlProperties.__or__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.CapControl.CapControlProperties.__reduce__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.CapControl.CapControlProperties.__reduce_ex__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.CapControl.CapControlProperties.__repr__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.CapControl.CapControlProperties.__reversed__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.CapControl.CapControlProperties.__ror__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.CapControl.CapControlProperties.__setitem__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.CapControl.CapControlProperties.__sizeof__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.CapControl.CapControlProperties.__str__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.CapControl.CapControlProperties.__subclasshook__

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.CapControl.CapControlProperties.clear

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.CapControl.CapControlProperties.copy

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.copy
```

````

````{py:method} get()
:canonical: altdss.CapControl.CapControlProperties.get

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.get
```

````

````{py:method} items()
:canonical: altdss.CapControl.CapControlProperties.items

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.items
```

````

````{py:method} keys()
:canonical: altdss.CapControl.CapControlProperties.keys

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.keys
```

````

````{py:attribute} pctMinkvar
:canonical: altdss.CapControl.CapControlProperties.pctMinkvar
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.pctMinkvar
```

````

````{py:method} pop()
:canonical: altdss.CapControl.CapControlProperties.pop

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.CapControl.CapControlProperties.popitem

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.CapControl.CapControlProperties.setdefault

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.CapControl.CapControlProperties.update

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.update
```

````

````{py:method} values()
:canonical: altdss.CapControl.CapControlProperties.values

```{autodoc2-docstring} altdss.CapControl.CapControlProperties.values
```

````

`````

`````{py:class} ICapControl(iobj)
:canonical: altdss.CapControl.ICapControl

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.CapControl.CapControlBatch`

```{autodoc2-docstring} altdss.CapControl.ICapControl
```

````{py:attribute} BaseFreq
:canonical: altdss.CapControl.ICapControl.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.BaseFreq
```

````

````{py:attribute} CTPhase
:canonical: altdss.CapControl.ICapControl.CTPhase
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.CTPhase
```

````

````{py:attribute} CTPhase_str
:canonical: altdss.CapControl.ICapControl.CTPhase_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.CTPhase_str
```

````

````{py:attribute} CTRatio
:canonical: altdss.CapControl.ICapControl.CTRatio
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.CTRatio
```

````

````{py:attribute} Capacitor
:canonical: altdss.CapControl.ICapControl.Capacitor
:type: typing.List[altdss.Capacitor.Capacitor]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.Capacitor
```

````

````{py:attribute} Capacitor_str
:canonical: altdss.CapControl.ICapControl.Capacitor_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.Capacitor_str
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.ICapControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.CapControl.ICapControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.ICapControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.CapControl.ICapControl.ComplexSeqVoltages
```

````

````{py:attribute} ControlSignal
:canonical: altdss.CapControl.ICapControl.ControlSignal
:type: typing.List[altdss.LoadShape.LoadShape]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.ControlSignal
```

````

````{py:attribute} ControlSignal_str
:canonical: altdss.CapControl.ICapControl.ControlSignal_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.ControlSignal_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.ICapControl.Currents

```{autodoc2-docstring} altdss.CapControl.ICapControl.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.CapControl.ICapControl.CurrentsMagAng

```{autodoc2-docstring} altdss.CapControl.ICapControl.CurrentsMagAng
```

````

````{py:attribute} DeadTime
:canonical: altdss.CapControl.ICapControl.DeadTime
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.DeadTime
```

````

````{py:attribute} Delay
:canonical: altdss.CapControl.ICapControl.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.Delay
```

````

````{py:attribute} DelayOff
:canonical: altdss.CapControl.ICapControl.DelayOff
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.DelayOff
```

````

````{py:attribute} Element
:canonical: altdss.CapControl.ICapControl.Element
:type: typing.List[altdss.DSSObj.DSSObj]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.Element
```

````

````{py:attribute} Element_str
:canonical: altdss.CapControl.ICapControl.Element_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.Element_str
```

````

````{py:attribute} Enabled
:canonical: altdss.CapControl.ICapControl.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.CapControl.ICapControl.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.CapControl.ICapControl.FullName

```{autodoc2-docstring} altdss.CapControl.ICapControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.CapControl.ICapControl.GUID

```{autodoc2-docstring} altdss.CapControl.ICapControl.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.CapControl.ICapControl.Handle

```{autodoc2-docstring} altdss.CapControl.ICapControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.CapControl.ICapControl.HasOCPDevice

```{autodoc2-docstring} altdss.CapControl.ICapControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.CapControl.ICapControl.HasSwitchControl

```{autodoc2-docstring} altdss.CapControl.ICapControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.CapControl.ICapControl.HasVoltControl

```{autodoc2-docstring} altdss.CapControl.ICapControl.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.CapControl.ICapControl.IsIsolated

```{autodoc2-docstring} altdss.CapControl.ICapControl.IsIsolated
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.CapControl.ICapControl.Like

```{autodoc2-docstring} altdss.CapControl.ICapControl.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.ICapControl.Losses

```{autodoc2-docstring} altdss.CapControl.ICapControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.CapControl.ICapControl.MaxCurrent

```{autodoc2-docstring} altdss.CapControl.ICapControl.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.CapControl.ICapControl.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.CapControl.ICapControl.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.CapControl.ICapControl.NumConductors

```{autodoc2-docstring} altdss.CapControl.ICapControl.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.CapControl.ICapControl.NumControllers

```{autodoc2-docstring} altdss.CapControl.ICapControl.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.CapControl.ICapControl.NumPhases

```{autodoc2-docstring} altdss.CapControl.ICapControl.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.CapControl.ICapControl.NumTerminals

```{autodoc2-docstring} altdss.CapControl.ICapControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.CapControl.ICapControl.OCPDevice

```{autodoc2-docstring} altdss.CapControl.ICapControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.CapControl.ICapControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.CapControl.ICapControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.CapControl.ICapControl.OCPDeviceType

```{autodoc2-docstring} altdss.CapControl.ICapControl.OCPDeviceType
```

````

````{py:attribute} OffSetting
:canonical: altdss.CapControl.ICapControl.OffSetting
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.OffSetting
```

````

````{py:attribute} OnSetting
:canonical: altdss.CapControl.ICapControl.OnSetting
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.OnSetting
```

````

````{py:attribute} PTPhase
:canonical: altdss.CapControl.ICapControl.PTPhase
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.PTPhase
```

````

````{py:attribute} PTPhase_str
:canonical: altdss.CapControl.ICapControl.PTPhase_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.PTPhase_str
```

````

````{py:attribute} PTRatio
:canonical: altdss.CapControl.ICapControl.PTRatio
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.PTRatio
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.ICapControl.PhaseLosses

```{autodoc2-docstring} altdss.CapControl.ICapControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.ICapControl.Powers

```{autodoc2-docstring} altdss.CapControl.ICapControl.Powers
```

````

````{py:method} Reset(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.CapControl.ICapControl.Reset

```{autodoc2-docstring} altdss.CapControl.ICapControl.Reset
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.CapControl.ICapControl.SeqCurrents

```{autodoc2-docstring} altdss.CapControl.ICapControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.ICapControl.SeqPowers

```{autodoc2-docstring} altdss.CapControl.ICapControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.CapControl.ICapControl.SeqVoltages

```{autodoc2-docstring} altdss.CapControl.ICapControl.SeqVoltages
```

````

````{py:attribute} Terminal
:canonical: altdss.CapControl.ICapControl.Terminal
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.Terminal
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.ICapControl.TotalPowers

```{autodoc2-docstring} altdss.CapControl.ICapControl.TotalPowers
```

````

````{py:attribute} Type
:canonical: altdss.CapControl.ICapControl.Type
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.Type
```

````

````{py:attribute} Type_str
:canonical: altdss.CapControl.ICapControl.Type_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.Type_str
```

````

````{py:attribute} UserData
:canonical: altdss.CapControl.ICapControl.UserData
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.UserData
```

````

````{py:attribute} UserModel
:canonical: altdss.CapControl.ICapControl.UserModel
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.UserModel
```

````

````{py:attribute} VBus
:canonical: altdss.CapControl.ICapControl.VBus
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.VBus
```

````

````{py:attribute} VMax
:canonical: altdss.CapControl.ICapControl.VMax
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.VMax
```

````

````{py:attribute} VMin
:canonical: altdss.CapControl.ICapControl.VMin
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.VMin
```

````

````{py:attribute} VoltOverride
:canonical: altdss.CapControl.ICapControl.VoltOverride
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.VoltOverride
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.CapControl.ICapControl.Voltages

```{autodoc2-docstring} altdss.CapControl.ICapControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.CapControl.ICapControl.VoltagesMagAng

```{autodoc2-docstring} altdss.CapControl.ICapControl.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.CapControl.ICapControl.__call__

```{autodoc2-docstring} altdss.CapControl.ICapControl.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.CapControl.ICapControl.__contains__

```{autodoc2-docstring} altdss.CapControl.ICapControl.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.CapControl.ICapControl.__getitem__

```{autodoc2-docstring} altdss.CapControl.ICapControl.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.CapControl.ICapControl.__init__

```{autodoc2-docstring} altdss.CapControl.ICapControl.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.CapControl.ICapControl.__iter__

```{autodoc2-docstring} altdss.CapControl.ICapControl.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.CapControl.ICapControl.__len__

```{autodoc2-docstring} altdss.CapControl.ICapControl.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.CapControl.ICapControl.batch

```{autodoc2-docstring} altdss.CapControl.ICapControl.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.CapControl.CapControlBatchProperties]) -> altdss.CapControl.CapControlBatch
:canonical: altdss.CapControl.ICapControl.batch_new

```{autodoc2-docstring} altdss.CapControl.ICapControl.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.CapControl.ICapControl.begin_edit

```{autodoc2-docstring} altdss.CapControl.ICapControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.CapControl.ICapControl.end_edit

```{autodoc2-docstring} altdss.CapControl.ICapControl.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.CapControl.ICapControl.find

```{autodoc2-docstring} altdss.CapControl.ICapControl.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.CapControl.CapControlProperties]) -> altdss.CapControl.CapControl
:canonical: altdss.CapControl.ICapControl.new

```{autodoc2-docstring} altdss.CapControl.ICapControl.new
```

````

````{py:attribute} pctMinkvar
:canonical: altdss.CapControl.ICapControl.pctMinkvar
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.CapControl.ICapControl.pctMinkvar
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.CapControl.ICapControl.to_json

```{autodoc2-docstring} altdss.CapControl.ICapControl.to_json
```

````

````{py:method} to_list()
:canonical: altdss.CapControl.ICapControl.to_list

```{autodoc2-docstring} altdss.CapControl.ICapControl.to_list
```

````

`````
