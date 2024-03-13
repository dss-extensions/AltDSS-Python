# {py:mod}`altdss.RegControl`

```{py:module} altdss.RegControl
```

```{autodoc2-docstring} altdss.RegControl
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IRegControl <altdss.RegControl.IRegControl>`
  - ```{autodoc2-docstring} altdss.RegControl.IRegControl
    :summary:
    ```
* - {py:obj}`RegControl <altdss.RegControl.RegControl>`
  - ```{autodoc2-docstring} altdss.RegControl.RegControl
    :summary:
    ```
* - {py:obj}`RegControlBatch <altdss.RegControl.RegControlBatch>`
  - ```{autodoc2-docstring} altdss.RegControl.RegControlBatch
    :summary:
    ```
* - {py:obj}`RegControlBatchProperties <altdss.RegControl.RegControlBatchProperties>`
  - ```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties
    :summary:
    ```
* - {py:obj}`RegControlProperties <altdss.RegControl.RegControlProperties>`
  - ```{autodoc2-docstring} altdss.RegControl.RegControlProperties
    :summary:
    ```
````

### API

`````{py:class} IRegControl(iobj)
:canonical: altdss.RegControl.IRegControl

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.RegControl.RegControlBatch`

```{autodoc2-docstring} altdss.RegControl.IRegControl
```

````{py:attribute} Band
:canonical: altdss.RegControl.IRegControl.Band
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Band
```

````

````{py:attribute} BaseFreq
:canonical: altdss.RegControl.IRegControl.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.BaseFreq
```

````

````{py:attribute} Bus
:canonical: altdss.RegControl.IRegControl.Bus
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Bus
```

````

````{py:attribute} CTPrim
:canonical: altdss.RegControl.IRegControl.CTPrim
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.CTPrim
```

````

````{py:attribute} Cogen
:canonical: altdss.RegControl.IRegControl.Cogen
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Cogen
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.IRegControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.RegControl.IRegControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.IRegControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.RegControl.IRegControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.IRegControl.Currents

```{autodoc2-docstring} altdss.RegControl.IRegControl.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.RegControl.IRegControl.CurrentsMagAng

```{autodoc2-docstring} altdss.RegControl.IRegControl.CurrentsMagAng
```

````

````{py:attribute} DebugTrace
:canonical: altdss.RegControl.IRegControl.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.RegControl.IRegControl.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.RegControl.IRegControl.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.RegControl.IRegControl.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.RegControl.IRegControl.FullName

```{autodoc2-docstring} altdss.RegControl.IRegControl.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.RegControl.IRegControl.GUID

```{autodoc2-docstring} altdss.RegControl.IRegControl.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.RegControl.IRegControl.Handle

```{autodoc2-docstring} altdss.RegControl.IRegControl.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.RegControl.IRegControl.HasOCPDevice

```{autodoc2-docstring} altdss.RegControl.IRegControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.RegControl.IRegControl.HasSwitchControl

```{autodoc2-docstring} altdss.RegControl.IRegControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.RegControl.IRegControl.HasVoltControl

```{autodoc2-docstring} altdss.RegControl.IRegControl.HasVoltControl
```

````

````{py:attribute} InverseTime
:canonical: altdss.RegControl.IRegControl.InverseTime
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.InverseTime
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.RegControl.IRegControl.IsIsolated

```{autodoc2-docstring} altdss.RegControl.IRegControl.IsIsolated
```

````

````{py:attribute} LDC_Z
:canonical: altdss.RegControl.IRegControl.LDC_Z
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.LDC_Z
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.RegControl.IRegControl.Like

```{autodoc2-docstring} altdss.RegControl.IRegControl.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.IRegControl.Losses

```{autodoc2-docstring} altdss.RegControl.IRegControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.RegControl.IRegControl.MaxCurrent

```{autodoc2-docstring} altdss.RegControl.IRegControl.MaxCurrent
```

````

````{py:attribute} MaxTapChange
:canonical: altdss.RegControl.IRegControl.MaxTapChange
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.MaxTapChange
```

````

````{py:property} Name
:canonical: altdss.RegControl.IRegControl.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.RegControl.IRegControl.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.RegControl.IRegControl.NumConductors

```{autodoc2-docstring} altdss.RegControl.IRegControl.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.RegControl.IRegControl.NumControllers

```{autodoc2-docstring} altdss.RegControl.IRegControl.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.RegControl.IRegControl.NumPhases

```{autodoc2-docstring} altdss.RegControl.IRegControl.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.RegControl.IRegControl.NumTerminals

```{autodoc2-docstring} altdss.RegControl.IRegControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.RegControl.IRegControl.OCPDevice

```{autodoc2-docstring} altdss.RegControl.IRegControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.RegControl.IRegControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.RegControl.IRegControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.RegControl.IRegControl.OCPDeviceType

```{autodoc2-docstring} altdss.RegControl.IRegControl.OCPDeviceType
```

````

````{py:attribute} PTPhase
:canonical: altdss.RegControl.IRegControl.PTPhase
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.PTPhase
```

````

````{py:attribute} PTPhase_str
:canonical: altdss.RegControl.IRegControl.PTPhase_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.PTPhase_str
```

````

````{py:attribute} PTRatio
:canonical: altdss.RegControl.IRegControl.PTRatio
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.PTRatio
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.IRegControl.PhaseLosses

```{autodoc2-docstring} altdss.RegControl.IRegControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.IRegControl.Powers

```{autodoc2-docstring} altdss.RegControl.IRegControl.Powers
```

````

````{py:attribute} R
:canonical: altdss.RegControl.IRegControl.R
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.R
```

````

````{py:attribute} RemotePTRatio
:canonical: altdss.RegControl.IRegControl.RemotePTRatio
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.RemotePTRatio
```

````

````{py:method} Reset(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.RegControl.IRegControl.Reset

```{autodoc2-docstring} altdss.RegControl.IRegControl.Reset
```

````

````{py:attribute} RevBand
:canonical: altdss.RegControl.IRegControl.RevBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.RevBand
```

````

````{py:attribute} RevDelay
:canonical: altdss.RegControl.IRegControl.RevDelay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.RevDelay
```

````

````{py:attribute} RevNeutral
:canonical: altdss.RegControl.IRegControl.RevNeutral
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.RevNeutral
```

````

````{py:attribute} RevR
:canonical: altdss.RegControl.IRegControl.RevR
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.RevR
```

````

````{py:attribute} RevThreshold
:canonical: altdss.RegControl.IRegControl.RevThreshold
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.RevThreshold
```

````

````{py:attribute} RevVReg
:canonical: altdss.RegControl.IRegControl.RevVReg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.RevVReg
```

````

````{py:attribute} RevX
:canonical: altdss.RegControl.IRegControl.RevX
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.RevX
```

````

````{py:attribute} Rev_Z
:canonical: altdss.RegControl.IRegControl.Rev_Z
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Rev_Z
```

````

````{py:attribute} Reversible
:canonical: altdss.RegControl.IRegControl.Reversible
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Reversible
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.RegControl.IRegControl.SeqCurrents

```{autodoc2-docstring} altdss.RegControl.IRegControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.IRegControl.SeqPowers

```{autodoc2-docstring} altdss.RegControl.IRegControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.RegControl.IRegControl.SeqVoltages

```{autodoc2-docstring} altdss.RegControl.IRegControl.SeqVoltages
```

````

````{py:attribute} TapDelay
:canonical: altdss.RegControl.IRegControl.TapDelay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.TapDelay
```

````

````{py:attribute} TapNum
:canonical: altdss.RegControl.IRegControl.TapNum
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.TapNum
```

````

````{py:attribute} TapWinding
:canonical: altdss.RegControl.IRegControl.TapWinding
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.TapWinding
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.IRegControl.TotalPowers

```{autodoc2-docstring} altdss.RegControl.IRegControl.TotalPowers
```

````

````{py:attribute} Transformer
:canonical: altdss.RegControl.IRegControl.Transformer
:type: typing.List[typing.Union[altdss.Transformer.Transformer, altdss.AutoTrans.AutoTrans]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Transformer
```

````

````{py:attribute} Transformer_str
:canonical: altdss.RegControl.IRegControl.Transformer_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Transformer_str
```

````

````{py:attribute} VLimit
:canonical: altdss.RegControl.IRegControl.VLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.VLimit
```

````

````{py:attribute} VReg
:canonical: altdss.RegControl.IRegControl.VReg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.VReg
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.IRegControl.Voltages

```{autodoc2-docstring} altdss.RegControl.IRegControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.RegControl.IRegControl.VoltagesMagAng

```{autodoc2-docstring} altdss.RegControl.IRegControl.VoltagesMagAng
```

````

````{py:attribute} Winding
:canonical: altdss.RegControl.IRegControl.Winding
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.Winding
```

````

````{py:attribute} X
:canonical: altdss.RegControl.IRegControl.X
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.IRegControl.X
```

````

````{py:method} __call__()
:canonical: altdss.RegControl.IRegControl.__call__

```{autodoc2-docstring} altdss.RegControl.IRegControl.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.RegControl.IRegControl.__contains__

```{autodoc2-docstring} altdss.RegControl.IRegControl.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.RegControl.IRegControl.__getitem__

```{autodoc2-docstring} altdss.RegControl.IRegControl.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.RegControl.IRegControl.__init__

```{autodoc2-docstring} altdss.RegControl.IRegControl.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.RegControl.IRegControl.__iter__

```{autodoc2-docstring} altdss.RegControl.IRegControl.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.RegControl.IRegControl.__len__

```{autodoc2-docstring} altdss.RegControl.IRegControl.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.RegControl.IRegControl.batch

```{autodoc2-docstring} altdss.RegControl.IRegControl.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.RegControl.RegControlBatchProperties]) -> altdss.RegControl.RegControlBatch
:canonical: altdss.RegControl.IRegControl.batch_new

```{autodoc2-docstring} altdss.RegControl.IRegControl.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.RegControl.IRegControl.begin_edit

```{autodoc2-docstring} altdss.RegControl.IRegControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.RegControl.IRegControl.end_edit

```{autodoc2-docstring} altdss.RegControl.IRegControl.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.RegControl.IRegControl.find

```{autodoc2-docstring} altdss.RegControl.IRegControl.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.RegControl.RegControlProperties]) -> altdss.RegControl.RegControl
:canonical: altdss.RegControl.IRegControl.new

```{autodoc2-docstring} altdss.RegControl.IRegControl.new
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.RegControl.IRegControl.to_json

```{autodoc2-docstring} altdss.RegControl.IRegControl.to_json
```

````

````{py:method} to_list()
:canonical: altdss.RegControl.IRegControl.to_list

```{autodoc2-docstring} altdss.RegControl.IRegControl.to_list
```

````

`````

`````{py:class} RegControl(api_util, ptr)
:canonical: altdss.RegControl.RegControl

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`

```{autodoc2-docstring} altdss.RegControl.RegControl
```

````{py:attribute} Band
:canonical: altdss.RegControl.RegControl.Band
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Band
```

````

````{py:attribute} BaseFreq
:canonical: altdss.RegControl.RegControl.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.BaseFreq
```

````

````{py:attribute} Bus
:canonical: altdss.RegControl.RegControl.Bus
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Bus
```

````

````{py:attribute} CTPrim
:canonical: altdss.RegControl.RegControl.CTPrim
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.CTPrim
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.RegControl.RegControl.Close

```{autodoc2-docstring} altdss.RegControl.RegControl.Close
```

````

````{py:attribute} Cogen
:canonical: altdss.RegControl.RegControl.Cogen
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Cogen
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControl.ComplexSeqCurrents

```{autodoc2-docstring} altdss.RegControl.RegControl.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControl.ComplexSeqVoltages

```{autodoc2-docstring} altdss.RegControl.RegControl.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControl.Currents

```{autodoc2-docstring} altdss.RegControl.RegControl.Currents
```

````

````{py:attribute} DebugTrace
:canonical: altdss.RegControl.RegControl.DebugTrace
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.RegControl.RegControl.Delay
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Delay
```

````

````{py:attribute} DisplayName
:canonical: altdss.RegControl.RegControl.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.DisplayName
```

````

````{py:attribute} Enabled
:canonical: altdss.RegControl.RegControl.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.RegControl.RegControl.EventLog
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.EventLog
```

````

````{py:method} FullName() -> str
:canonical: altdss.RegControl.RegControl.FullName

```{autodoc2-docstring} altdss.RegControl.RegControl.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.RegControl.RegControl.GUID

```{autodoc2-docstring} altdss.RegControl.RegControl.GUID
```

````

````{py:method} Handle() -> int
:canonical: altdss.RegControl.RegControl.Handle

```{autodoc2-docstring} altdss.RegControl.RegControl.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.RegControl.RegControl.HasOCPDevice

```{autodoc2-docstring} altdss.RegControl.RegControl.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.RegControl.RegControl.HasSwitchControl

```{autodoc2-docstring} altdss.RegControl.RegControl.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.RegControl.RegControl.HasVoltControl

```{autodoc2-docstring} altdss.RegControl.RegControl.HasVoltControl
```

````

````{py:attribute} InverseTime
:canonical: altdss.RegControl.RegControl.InverseTime
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.InverseTime
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.RegControl.RegControl.IsIsolated

```{autodoc2-docstring} altdss.RegControl.RegControl.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.RegControl.RegControl.IsOpen

```{autodoc2-docstring} altdss.RegControl.RegControl.IsOpen
```

````

````{py:attribute} LDC_Z
:canonical: altdss.RegControl.RegControl.LDC_Z
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.LDC_Z
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.RegControl.RegControl.Like

```{autodoc2-docstring} altdss.RegControl.RegControl.Like
```

````

````{py:method} Losses() -> complex
:canonical: altdss.RegControl.RegControl.Losses

```{autodoc2-docstring} altdss.RegControl.RegControl.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.RegControl.RegControl.MaxCurrent

```{autodoc2-docstring} altdss.RegControl.RegControl.MaxCurrent
```

````

````{py:attribute} MaxTapChange
:canonical: altdss.RegControl.RegControl.MaxTapChange
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.MaxTapChange
```

````

````{py:property} Name
:canonical: altdss.RegControl.RegControl.Name
:type: str

```{autodoc2-docstring} altdss.RegControl.RegControl.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.RegControl.RegControl.NodeOrder

```{autodoc2-docstring} altdss.RegControl.RegControl.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.RegControl.RegControl.NodeRef

```{autodoc2-docstring} altdss.RegControl.RegControl.NodeRef
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.RegControl.RegControl.NumConductors

```{autodoc2-docstring} altdss.RegControl.RegControl.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.RegControl.RegControl.NumControllers

```{autodoc2-docstring} altdss.RegControl.RegControl.NumControllers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.RegControl.RegControl.NumPhases

```{autodoc2-docstring} altdss.RegControl.RegControl.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.RegControl.RegControl.NumTerminals

```{autodoc2-docstring} altdss.RegControl.RegControl.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.RegControl.RegControl.OCPDevice

```{autodoc2-docstring} altdss.RegControl.RegControl.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.RegControl.RegControl.OCPDeviceIndex

```{autodoc2-docstring} altdss.RegControl.RegControl.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.RegControl.RegControl.OCPDeviceType

```{autodoc2-docstring} altdss.RegControl.RegControl.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.RegControl.RegControl.Open

```{autodoc2-docstring} altdss.RegControl.RegControl.Open
```

````

````{py:attribute} PTPhase
:canonical: altdss.RegControl.RegControl.PTPhase
:type: altdss.enums.RegControlPhaseSelection
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.PTPhase
```

````

````{py:attribute} PTPhase_str
:canonical: altdss.RegControl.RegControl.PTPhase_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.PTPhase_str
```

````

````{py:attribute} PTRatio
:canonical: altdss.RegControl.RegControl.PTRatio
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.PTRatio
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControl.PhaseLosses

```{autodoc2-docstring} altdss.RegControl.RegControl.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControl.Powers

```{autodoc2-docstring} altdss.RegControl.RegControl.Powers
```

````

````{py:attribute} R
:canonical: altdss.RegControl.RegControl.R
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.R
```

````

````{py:attribute} RemotePTRatio
:canonical: altdss.RegControl.RegControl.RemotePTRatio
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.RemotePTRatio
```

````

````{py:method} Reset(value: bool = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.RegControl.RegControl.Reset

```{autodoc2-docstring} altdss.RegControl.RegControl.Reset
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.RegControl.RegControl.Residuals

```{autodoc2-docstring} altdss.RegControl.RegControl.Residuals
```

````

````{py:attribute} RevBand
:canonical: altdss.RegControl.RegControl.RevBand
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.RevBand
```

````

````{py:attribute} RevDelay
:canonical: altdss.RegControl.RegControl.RevDelay
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.RevDelay
```

````

````{py:attribute} RevNeutral
:canonical: altdss.RegControl.RegControl.RevNeutral
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.RevNeutral
```

````

````{py:attribute} RevR
:canonical: altdss.RegControl.RegControl.RevR
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.RevR
```

````

````{py:attribute} RevThreshold
:canonical: altdss.RegControl.RegControl.RevThreshold
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.RevThreshold
```

````

````{py:attribute} RevVReg
:canonical: altdss.RegControl.RegControl.RevVReg
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.RevVReg
```

````

````{py:attribute} RevX
:canonical: altdss.RegControl.RegControl.RevX
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.RevX
```

````

````{py:attribute} Rev_Z
:canonical: altdss.RegControl.RegControl.Rev_Z
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Rev_Z
```

````

````{py:attribute} Reversible
:canonical: altdss.RegControl.RegControl.Reversible
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Reversible
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.RegControl.RegControl.SeqCurrents

```{autodoc2-docstring} altdss.RegControl.RegControl.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControl.SeqPowers

```{autodoc2-docstring} altdss.RegControl.RegControl.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.RegControl.RegControl.SeqVoltages

```{autodoc2-docstring} altdss.RegControl.RegControl.SeqVoltages
```

````

````{py:attribute} TapDelay
:canonical: altdss.RegControl.RegControl.TapDelay
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.TapDelay
```

````

````{py:attribute} TapNum
:canonical: altdss.RegControl.RegControl.TapNum
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.TapNum
```

````

````{py:attribute} TapWinding
:canonical: altdss.RegControl.RegControl.TapWinding
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.TapWinding
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControl.TotalPowers

```{autodoc2-docstring} altdss.RegControl.RegControl.TotalPowers
```

````

````{py:attribute} Transformer
:canonical: altdss.RegControl.RegControl.Transformer
:type: (altdss.Transformer.Transformer, altdss.AutoTrans.AutoTrans)
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Transformer
```

````

````{py:attribute} Transformer_str
:canonical: altdss.RegControl.RegControl.Transformer_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Transformer_str
```

````

````{py:attribute} VLimit
:canonical: altdss.RegControl.RegControl.VLimit
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.VLimit
```

````

````{py:attribute} VReg
:canonical: altdss.RegControl.RegControl.VReg
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.VReg
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControl.Voltages

```{autodoc2-docstring} altdss.RegControl.RegControl.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.RegControl.RegControl.VoltagesMagAng

```{autodoc2-docstring} altdss.RegControl.RegControl.VoltagesMagAng
```

````

````{py:attribute} Winding
:canonical: altdss.RegControl.RegControl.Winding
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.Winding
```

````

````{py:attribute} X
:canonical: altdss.RegControl.RegControl.X
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControl.X
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControl.YPrim

```{autodoc2-docstring} altdss.RegControl.RegControl.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.RegControl.RegControl.__hash__

```{autodoc2-docstring} altdss.RegControl.RegControl.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.RegControl.RegControl.__init__

```{autodoc2-docstring} altdss.RegControl.RegControl.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.RegControl.RegControl.__ne__

```{autodoc2-docstring} altdss.RegControl.RegControl.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.RegControl.RegControl.__repr__

```{autodoc2-docstring} altdss.RegControl.RegControl.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.RegControl.RegControl.begin_edit

```{autodoc2-docstring} altdss.RegControl.RegControl.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.RegControl.RegControl.end_edit

```{autodoc2-docstring} altdss.RegControl.RegControl.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.RegControl.RegControl.to_json

```{autodoc2-docstring} altdss.RegControl.RegControl.to_json
```

````

`````

`````{py:class} RegControlBatch(api_util, **kwargs)
:canonical: altdss.RegControl.RegControlBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`

```{autodoc2-docstring} altdss.RegControl.RegControlBatch
```

````{py:attribute} Band
:canonical: altdss.RegControl.RegControlBatch.Band
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Band
```

````

````{py:attribute} BaseFreq
:canonical: altdss.RegControl.RegControlBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.BaseFreq
```

````

````{py:attribute} Bus
:canonical: altdss.RegControl.RegControlBatch.Bus
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Bus
```

````

````{py:attribute} CTPrim
:canonical: altdss.RegControl.RegControlBatch.CTPrim
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.CTPrim
```

````

````{py:attribute} Cogen
:canonical: altdss.RegControl.RegControlBatch.Cogen
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Cogen
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControlBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControlBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControlBatch.Currents

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.RegControl.RegControlBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.CurrentsMagAng
```

````

````{py:attribute} DebugTrace
:canonical: altdss.RegControl.RegControlBatch.DebugTrace
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.RegControl.RegControlBatch.Delay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.RegControl.RegControlBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.RegControl.RegControlBatch.EventLog
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.EventLog
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.RegControl.RegControlBatch.FullName

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.FullName
```

````

````{py:method} GUID() -> typing.List[str]
:canonical: altdss.RegControl.RegControlBatch.GUID

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.RegControl.RegControlBatch.Handle

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Handle
```

````

````{py:method} HasOCPDevice() -> altdss.types.BoolArray
:canonical: altdss.RegControl.RegControlBatch.HasOCPDevice

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> altdss.types.BoolArray
:canonical: altdss.RegControl.RegControlBatch.HasSwitchControl

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> altdss.types.BoolArray
:canonical: altdss.RegControl.RegControlBatch.HasVoltControl

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.HasVoltControl
```

````

````{py:attribute} InverseTime
:canonical: altdss.RegControl.RegControlBatch.InverseTime
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.InverseTime
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.RegControl.RegControlBatch.IsIsolated

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.IsIsolated
```

````

````{py:attribute} LDC_Z
:canonical: altdss.RegControl.RegControlBatch.LDC_Z
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.LDC_Z
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.RegControl.RegControlBatch.Like

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Like
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControlBatch.Losses

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> altdss.types.Float64Array
:canonical: altdss.RegControl.RegControlBatch.MaxCurrent

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.MaxCurrent
```

````

````{py:attribute} MaxTapChange
:canonical: altdss.RegControl.RegControlBatch.MaxTapChange
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.MaxTapChange
```

````

````{py:property} Name
:canonical: altdss.RegControl.RegControlBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.RegControl.RegControlBatch.NumConductors

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.RegControl.RegControlBatch.NumControllers

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.RegControl.RegControlBatch.NumPhases

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.RegControl.RegControlBatch.NumTerminals

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.RegControl.RegControlBatch.OCPDevice

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.RegControl.RegControlBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> typing.List[dss.enums.OCPDevType]
:canonical: altdss.RegControl.RegControlBatch.OCPDeviceType

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.OCPDeviceType
```

````

````{py:attribute} PTPhase
:canonical: altdss.RegControl.RegControlBatch.PTPhase
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.PTPhase
```

````

````{py:attribute} PTPhase_str
:canonical: altdss.RegControl.RegControlBatch.PTPhase_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.PTPhase_str
```

````

````{py:attribute} PTRatio
:canonical: altdss.RegControl.RegControlBatch.PTRatio
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.PTRatio
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControlBatch.PhaseLosses

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControlBatch.Powers

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Powers
```

````

````{py:attribute} R
:canonical: altdss.RegControl.RegControlBatch.R
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.R
```

````

````{py:attribute} RemotePTRatio
:canonical: altdss.RegControl.RegControlBatch.RemotePTRatio
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.RemotePTRatio
```

````

````{py:method} Reset(value: typing.Union[bool, typing.List[bool]] = True, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.RegControl.RegControlBatch.Reset

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Reset
```

````

````{py:attribute} RevBand
:canonical: altdss.RegControl.RegControlBatch.RevBand
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.RevBand
```

````

````{py:attribute} RevDelay
:canonical: altdss.RegControl.RegControlBatch.RevDelay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.RevDelay
```

````

````{py:attribute} RevNeutral
:canonical: altdss.RegControl.RegControlBatch.RevNeutral
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.RevNeutral
```

````

````{py:attribute} RevR
:canonical: altdss.RegControl.RegControlBatch.RevR
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.RevR
```

````

````{py:attribute} RevThreshold
:canonical: altdss.RegControl.RegControlBatch.RevThreshold
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.RevThreshold
```

````

````{py:attribute} RevVReg
:canonical: altdss.RegControl.RegControlBatch.RevVReg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.RevVReg
```

````

````{py:attribute} RevX
:canonical: altdss.RegControl.RegControlBatch.RevX
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.RevX
```

````

````{py:attribute} Rev_Z
:canonical: altdss.RegControl.RegControlBatch.Rev_Z
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Rev_Z
```

````

````{py:attribute} Reversible
:canonical: altdss.RegControl.RegControlBatch.Reversible
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Reversible
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.RegControl.RegControlBatch.SeqCurrents

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControlBatch.SeqPowers

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.RegControl.RegControlBatch.SeqVoltages

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.SeqVoltages
```

````

````{py:attribute} TapDelay
:canonical: altdss.RegControl.RegControlBatch.TapDelay
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.TapDelay
```

````

````{py:attribute} TapNum
:canonical: altdss.RegControl.RegControlBatch.TapNum
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.TapNum
```

````

````{py:attribute} TapWinding
:canonical: altdss.RegControl.RegControlBatch.TapWinding
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.TapWinding
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControlBatch.TotalPowers

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.TotalPowers
```

````

````{py:attribute} Transformer
:canonical: altdss.RegControl.RegControlBatch.Transformer
:type: typing.List[typing.Union[altdss.Transformer.Transformer, altdss.AutoTrans.AutoTrans]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Transformer
```

````

````{py:attribute} Transformer_str
:canonical: altdss.RegControl.RegControlBatch.Transformer_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Transformer_str
```

````

````{py:attribute} VLimit
:canonical: altdss.RegControl.RegControlBatch.VLimit
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.VLimit
```

````

````{py:attribute} VReg
:canonical: altdss.RegControl.RegControlBatch.VReg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.VReg
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.RegControl.RegControlBatch.Voltages

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.RegControl.RegControlBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.VoltagesMagAng
```

````

````{py:attribute} Winding
:canonical: altdss.RegControl.RegControlBatch.Winding
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.Winding
```

````

````{py:attribute} X
:canonical: altdss.RegControl.RegControlBatch.X
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.X
```

````

````{py:method} __call__()
:canonical: altdss.RegControl.RegControlBatch.__call__

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.RegControl.RegControlBatch.__getitem__

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.RegControl.RegControlBatch.__init__

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.RegControl.RegControlBatch.__iter__

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.RegControl.RegControlBatch.__len__

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.__len__
```

````

````{py:method} batch(**kwargs) -> altdss.Batch.DSSBatch
:canonical: altdss.RegControl.RegControlBatch.batch

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.batch
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.RegControl.RegControlBatch.begin_edit

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.RegControl.RegControlBatch.end_edit

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.end_edit
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.RegControl.RegControlBatch.to_json

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.RegControl.RegControlBatch.to_list

```{autodoc2-docstring} altdss.RegControl.RegControlBatch.to_list
```

````

`````

`````{py:class} RegControlBatchProperties()
:canonical: altdss.RegControl.RegControlBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties
```

````{py:attribute} Band
:canonical: altdss.RegControl.RegControlBatchProperties.Band
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Band
```

````

````{py:attribute} BaseFreq
:canonical: altdss.RegControl.RegControlBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.BaseFreq
```

````

````{py:attribute} Bus
:canonical: altdss.RegControl.RegControlBatchProperties.Bus
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Bus
```

````

````{py:attribute} CTPrim
:canonical: altdss.RegControl.RegControlBatchProperties.CTPrim
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.CTPrim
```

````

````{py:attribute} Cogen
:canonical: altdss.RegControl.RegControlBatchProperties.Cogen
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Cogen
```

````

````{py:attribute} DebugTrace
:canonical: altdss.RegControl.RegControlBatchProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.RegControl.RegControlBatchProperties.Delay
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.RegControl.RegControlBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.RegControl.RegControlBatchProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.EventLog
```

````

````{py:attribute} InverseTime
:canonical: altdss.RegControl.RegControlBatchProperties.InverseTime
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.InverseTime
```

````

````{py:attribute} LDC_Z
:canonical: altdss.RegControl.RegControlBatchProperties.LDC_Z
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.LDC_Z
```

````

````{py:attribute} Like
:canonical: altdss.RegControl.RegControlBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Like
```

````

````{py:attribute} MaxTapChange
:canonical: altdss.RegControl.RegControlBatchProperties.MaxTapChange
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.MaxTapChange
```

````

````{py:attribute} PTPhase
:canonical: altdss.RegControl.RegControlBatchProperties.PTPhase
:type: typing.Union[typing.AnyStr, int, altdss.enums.RegControlPhaseSelection, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.RegControlPhaseSelection], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.PTPhase
```

````

````{py:attribute} PTRatio
:canonical: altdss.RegControl.RegControlBatchProperties.PTRatio
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.PTRatio
```

````

````{py:attribute} R
:canonical: altdss.RegControl.RegControlBatchProperties.R
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.R
```

````

````{py:attribute} RemotePTRatio
:canonical: altdss.RegControl.RegControlBatchProperties.RemotePTRatio
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.RemotePTRatio
```

````

````{py:attribute} Reset
:canonical: altdss.RegControl.RegControlBatchProperties.Reset
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Reset
```

````

````{py:attribute} RevBand
:canonical: altdss.RegControl.RegControlBatchProperties.RevBand
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.RevBand
```

````

````{py:attribute} RevDelay
:canonical: altdss.RegControl.RegControlBatchProperties.RevDelay
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.RevDelay
```

````

````{py:attribute} RevNeutral
:canonical: altdss.RegControl.RegControlBatchProperties.RevNeutral
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.RevNeutral
```

````

````{py:attribute} RevR
:canonical: altdss.RegControl.RegControlBatchProperties.RevR
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.RevR
```

````

````{py:attribute} RevThreshold
:canonical: altdss.RegControl.RegControlBatchProperties.RevThreshold
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.RevThreshold
```

````

````{py:attribute} RevVReg
:canonical: altdss.RegControl.RegControlBatchProperties.RevVReg
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.RevVReg
```

````

````{py:attribute} RevX
:canonical: altdss.RegControl.RegControlBatchProperties.RevX
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.RevX
```

````

````{py:attribute} Rev_Z
:canonical: altdss.RegControl.RegControlBatchProperties.Rev_Z
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Rev_Z
```

````

````{py:attribute} Reversible
:canonical: altdss.RegControl.RegControlBatchProperties.Reversible
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Reversible
```

````

````{py:attribute} TapDelay
:canonical: altdss.RegControl.RegControlBatchProperties.TapDelay
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.TapDelay
```

````

````{py:attribute} TapNum
:canonical: altdss.RegControl.RegControlBatchProperties.TapNum
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.TapNum
```

````

````{py:attribute} TapWinding
:canonical: altdss.RegControl.RegControlBatchProperties.TapWinding
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.TapWinding
```

````

````{py:attribute} Transformer
:canonical: altdss.RegControl.RegControlBatchProperties.Transformer
:type: typing.Union[typing.AnyStr, altdss.Transformer.Transformer, altdss.AutoTrans.AutoTrans, typing.List[typing.AnyStr], typing.List[typing.Union[altdss.Transformer.Transformer, altdss.AutoTrans.AutoTrans]]]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Transformer
```

````

````{py:attribute} VLimit
:canonical: altdss.RegControl.RegControlBatchProperties.VLimit
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.VLimit
```

````

````{py:attribute} VReg
:canonical: altdss.RegControl.RegControlBatchProperties.VReg
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.VReg
```

````

````{py:attribute} Winding
:canonical: altdss.RegControl.RegControlBatchProperties.Winding
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.Winding
```

````

````{py:attribute} X
:canonical: altdss.RegControl.RegControlBatchProperties.X
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.X
```

````

````{py:method} __contains__()
:canonical: altdss.RegControl.RegControlBatchProperties.__contains__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.RegControl.RegControlBatchProperties.__delattr__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.RegControl.RegControlBatchProperties.__delitem__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.RegControl.RegControlBatchProperties.__dir__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.RegControl.RegControlBatchProperties.__format__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.RegControl.RegControlBatchProperties.__ge__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.RegControl.RegControlBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.RegControl.RegControlBatchProperties.__getitem__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.RegControl.RegControlBatchProperties.__getstate__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.RegControl.RegControlBatchProperties.__gt__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.RegControl.RegControlBatchProperties.__init__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.RegControl.RegControlBatchProperties.__ior__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.RegControl.RegControlBatchProperties.__iter__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.RegControl.RegControlBatchProperties.__le__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.RegControl.RegControlBatchProperties.__len__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.RegControl.RegControlBatchProperties.__lt__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.RegControl.RegControlBatchProperties.__ne__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.RegControl.RegControlBatchProperties.__new__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.RegControl.RegControlBatchProperties.__or__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.RegControl.RegControlBatchProperties.__reduce__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.RegControl.RegControlBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.RegControl.RegControlBatchProperties.__repr__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.RegControl.RegControlBatchProperties.__reversed__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.RegControl.RegControlBatchProperties.__ror__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.RegControl.RegControlBatchProperties.__setitem__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.RegControl.RegControlBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.RegControl.RegControlBatchProperties.__str__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.RegControl.RegControlBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.RegControl.RegControlBatchProperties.clear

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.RegControl.RegControlBatchProperties.copy

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.RegControl.RegControlBatchProperties.get

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.RegControl.RegControlBatchProperties.items

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.RegControl.RegControlBatchProperties.keys

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.RegControl.RegControlBatchProperties.pop

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.RegControl.RegControlBatchProperties.popitem

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.RegControl.RegControlBatchProperties.setdefault

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.RegControl.RegControlBatchProperties.update

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.RegControl.RegControlBatchProperties.values

```{autodoc2-docstring} altdss.RegControl.RegControlBatchProperties.values
```

````

`````

`````{py:class} RegControlProperties()
:canonical: altdss.RegControl.RegControlProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.RegControl.RegControlProperties
```

````{py:attribute} Band
:canonical: altdss.RegControl.RegControlProperties.Band
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Band
```

````

````{py:attribute} BaseFreq
:canonical: altdss.RegControl.RegControlProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.BaseFreq
```

````

````{py:attribute} Bus
:canonical: altdss.RegControl.RegControlProperties.Bus
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Bus
```

````

````{py:attribute} CTPrim
:canonical: altdss.RegControl.RegControlProperties.CTPrim
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.CTPrim
```

````

````{py:attribute} Cogen
:canonical: altdss.RegControl.RegControlProperties.Cogen
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Cogen
```

````

````{py:attribute} DebugTrace
:canonical: altdss.RegControl.RegControlProperties.DebugTrace
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.DebugTrace
```

````

````{py:attribute} Delay
:canonical: altdss.RegControl.RegControlProperties.Delay
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Delay
```

````

````{py:attribute} Enabled
:canonical: altdss.RegControl.RegControlProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Enabled
```

````

````{py:attribute} EventLog
:canonical: altdss.RegControl.RegControlProperties.EventLog
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.EventLog
```

````

````{py:attribute} InverseTime
:canonical: altdss.RegControl.RegControlProperties.InverseTime
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.InverseTime
```

````

````{py:attribute} LDC_Z
:canonical: altdss.RegControl.RegControlProperties.LDC_Z
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.LDC_Z
```

````

````{py:attribute} Like
:canonical: altdss.RegControl.RegControlProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Like
```

````

````{py:attribute} MaxTapChange
:canonical: altdss.RegControl.RegControlProperties.MaxTapChange
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.MaxTapChange
```

````

````{py:attribute} PTPhase
:canonical: altdss.RegControl.RegControlProperties.PTPhase
:type: typing.Union[typing.AnyStr, int, altdss.enums.RegControlPhaseSelection]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.PTPhase
```

````

````{py:attribute} PTRatio
:canonical: altdss.RegControl.RegControlProperties.PTRatio
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.PTRatio
```

````

````{py:attribute} R
:canonical: altdss.RegControl.RegControlProperties.R
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.R
```

````

````{py:attribute} RemotePTRatio
:canonical: altdss.RegControl.RegControlProperties.RemotePTRatio
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.RemotePTRatio
```

````

````{py:attribute} Reset
:canonical: altdss.RegControl.RegControlProperties.Reset
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Reset
```

````

````{py:attribute} RevBand
:canonical: altdss.RegControl.RegControlProperties.RevBand
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.RevBand
```

````

````{py:attribute} RevDelay
:canonical: altdss.RegControl.RegControlProperties.RevDelay
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.RevDelay
```

````

````{py:attribute} RevNeutral
:canonical: altdss.RegControl.RegControlProperties.RevNeutral
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.RevNeutral
```

````

````{py:attribute} RevR
:canonical: altdss.RegControl.RegControlProperties.RevR
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.RevR
```

````

````{py:attribute} RevThreshold
:canonical: altdss.RegControl.RegControlProperties.RevThreshold
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.RevThreshold
```

````

````{py:attribute} RevVReg
:canonical: altdss.RegControl.RegControlProperties.RevVReg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.RevVReg
```

````

````{py:attribute} RevX
:canonical: altdss.RegControl.RegControlProperties.RevX
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.RevX
```

````

````{py:attribute} Rev_Z
:canonical: altdss.RegControl.RegControlProperties.Rev_Z
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Rev_Z
```

````

````{py:attribute} Reversible
:canonical: altdss.RegControl.RegControlProperties.Reversible
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Reversible
```

````

````{py:attribute} TapDelay
:canonical: altdss.RegControl.RegControlProperties.TapDelay
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.TapDelay
```

````

````{py:attribute} TapNum
:canonical: altdss.RegControl.RegControlProperties.TapNum
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.TapNum
```

````

````{py:attribute} TapWinding
:canonical: altdss.RegControl.RegControlProperties.TapWinding
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.TapWinding
```

````

````{py:attribute} Transformer
:canonical: altdss.RegControl.RegControlProperties.Transformer
:type: typing.Union[typing.AnyStr, altdss.Transformer.Transformer, altdss.AutoTrans.AutoTrans]
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Transformer
```

````

````{py:attribute} VLimit
:canonical: altdss.RegControl.RegControlProperties.VLimit
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.VLimit
```

````

````{py:attribute} VReg
:canonical: altdss.RegControl.RegControlProperties.VReg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.VReg
```

````

````{py:attribute} Winding
:canonical: altdss.RegControl.RegControlProperties.Winding
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.Winding
```

````

````{py:attribute} X
:canonical: altdss.RegControl.RegControlProperties.X
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.X
```

````

````{py:method} __contains__()
:canonical: altdss.RegControl.RegControlProperties.__contains__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.RegControl.RegControlProperties.__delattr__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.RegControl.RegControlProperties.__delitem__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.RegControl.RegControlProperties.__dir__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.RegControl.RegControlProperties.__format__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.RegControl.RegControlProperties.__ge__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.RegControl.RegControlProperties.__getattribute__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.RegControl.RegControlProperties.__getitem__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.RegControl.RegControlProperties.__getstate__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.RegControl.RegControlProperties.__gt__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.RegControl.RegControlProperties.__init__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.RegControl.RegControlProperties.__ior__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.RegControl.RegControlProperties.__iter__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.RegControl.RegControlProperties.__le__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.RegControl.RegControlProperties.__len__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.RegControl.RegControlProperties.__lt__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.RegControl.RegControlProperties.__ne__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.RegControl.RegControlProperties.__new__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.RegControl.RegControlProperties.__or__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.RegControl.RegControlProperties.__reduce__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.RegControl.RegControlProperties.__reduce_ex__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.RegControl.RegControlProperties.__repr__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.RegControl.RegControlProperties.__reversed__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.RegControl.RegControlProperties.__ror__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.RegControl.RegControlProperties.__setitem__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.RegControl.RegControlProperties.__sizeof__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.RegControl.RegControlProperties.__str__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.RegControl.RegControlProperties.__subclasshook__

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.RegControl.RegControlProperties.clear

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.RegControl.RegControlProperties.copy

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.copy
```

````

````{py:method} get()
:canonical: altdss.RegControl.RegControlProperties.get

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.get
```

````

````{py:method} items()
:canonical: altdss.RegControl.RegControlProperties.items

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.items
```

````

````{py:method} keys()
:canonical: altdss.RegControl.RegControlProperties.keys

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.keys
```

````

````{py:method} pop()
:canonical: altdss.RegControl.RegControlProperties.pop

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.RegControl.RegControlProperties.popitem

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.popitem
```

````

````{py:method} setdefault()
:canonical: altdss.RegControl.RegControlProperties.setdefault

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.RegControl.RegControlProperties.update

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.update
```

````

````{py:method} values()
:canonical: altdss.RegControl.RegControlProperties.values

```{autodoc2-docstring} altdss.RegControl.RegControlProperties.values
```

````

`````
