# {py:mod}`altdss.Line`

```{py:module} altdss.Line
```

```{autodoc2-docstring} altdss.Line
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ILine <altdss.Line.ILine>`
  - ```{autodoc2-docstring} altdss.Line.ILine
    :summary:
    ```
* - {py:obj}`Line <altdss.Line.Line>`
  - ```{autodoc2-docstring} altdss.Line.Line
    :summary:
    ```
* - {py:obj}`LineBatch <altdss.Line.LineBatch>`
  - ```{autodoc2-docstring} altdss.Line.LineBatch
    :summary:
    ```
* - {py:obj}`LineBatchProperties <altdss.Line.LineBatchProperties>`
  - ```{autodoc2-docstring} altdss.Line.LineBatchProperties
    :summary:
    ```
* - {py:obj}`LineProperties <altdss.Line.LineProperties>`
  - ```{autodoc2-docstring} altdss.Line.LineProperties
    :summary:
    ```
````

### API

`````{py:class} ILine(iobj)
:canonical: altdss.Line.ILine

Bases: {py:obj}`altdss.DSSObj.IDSSObj`, {py:obj}`altdss.Line.LineBatch`

```{autodoc2-docstring} altdss.Line.ILine
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Line.ILine.AccumulatedL

```{autodoc2-docstring} altdss.Line.ILine.AccumulatedL
```

````

````{py:attribute} B0
:canonical: altdss.Line.ILine.B0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.B0
```

````

````{py:attribute} B1
:canonical: altdss.Line.ILine.B1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Line.ILine.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Line.ILine.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Line.ILine.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Bus2
```

````

````{py:attribute} C0
:canonical: altdss.Line.ILine.C0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.C0
```

````

````{py:attribute} C1
:canonical: altdss.Line.ILine.C1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.Line.ILine.CMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.CMatrix
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Line.ILine.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Line.ILine.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Line.ILine.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Line.ILine.ComplexSeqVoltages
```

````

````{py:attribute} Conductors
:canonical: altdss.Line.ILine.Conductors
:type: typing.List[typing.List[typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Conductors
```

````

````{py:attribute} Conductors_str
:canonical: altdss.Line.ILine.Conductors_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Conductors_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Line.ILine.Currents

```{autodoc2-docstring} altdss.Line.ILine.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Line.ILine.CurrentsMagAng

```{autodoc2-docstring} altdss.Line.ILine.CurrentsMagAng
```

````

````{py:attribute} EarthModel
:canonical: altdss.Line.ILine.EarthModel
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.EarthModel
```

````

````{py:attribute} EarthModel_str
:canonical: altdss.Line.ILine.EarthModel_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.EarthModel_str
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Line.ILine.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Line.ILine.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Line.ILine.EnergyMeter

```{autodoc2-docstring} altdss.Line.ILine.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Line.ILine.EnergyMeterName

```{autodoc2-docstring} altdss.Line.ILine.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Line.ILine.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.FromTerminal

```{autodoc2-docstring} altdss.Line.ILine.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Line.ILine.FullName

```{autodoc2-docstring} altdss.Line.ILine.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Line.ILine.GUID

```{autodoc2-docstring} altdss.Line.ILine.GUID
```

````

````{py:attribute} Geometry
:canonical: altdss.Line.ILine.Geometry
:type: typing.List[altdss.LineGeometry.LineGeometry]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Geometry
```

````

````{py:attribute} Geometry_str
:canonical: altdss.Line.ILine.Geometry_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Geometry_str
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.Handle

```{autodoc2-docstring} altdss.Line.ILine.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Line.ILine.HasOCPDevice

```{autodoc2-docstring} altdss.Line.ILine.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Line.ILine.HasSwitchControl

```{autodoc2-docstring} altdss.Line.ILine.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Line.ILine.HasVoltControl

```{autodoc2-docstring} altdss.Line.ILine.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Line.ILine.IsIsolated

```{autodoc2-docstring} altdss.Line.ILine.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Line.ILine.IsShunt

```{autodoc2-docstring} altdss.Line.ILine.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Line.ILine.Lambda

```{autodoc2-docstring} altdss.Line.ILine.Lambda
```

````

````{py:attribute} Length
:canonical: altdss.Line.ILine.Length
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Length
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Line.ILine.Like

```{autodoc2-docstring} altdss.Line.ILine.Like
```

````

````{py:attribute} LineCode
:canonical: altdss.Line.ILine.LineCode
:type: typing.List[altdss.LineCode.LineCode]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.LineCode
```

````

````{py:attribute} LineCode_str
:canonical: altdss.Line.ILine.LineCode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.LineCode_str
```

````

````{py:attribute} LineType
:canonical: altdss.Line.ILine.LineType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.LineType
```

````

````{py:attribute} LineType_str
:canonical: altdss.Line.ILine.LineType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.LineType_str
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Line.ILine.Losses

```{autodoc2-docstring} altdss.Line.ILine.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Line.ILine.MaxCurrent

```{autodoc2-docstring} altdss.Line.ILine.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Line.ILine.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Line.ILine.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Line.ILine.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.NumConductors

```{autodoc2-docstring} altdss.Line.ILine.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.NumControllers

```{autodoc2-docstring} altdss.Line.ILine.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.NumCustomers

```{autodoc2-docstring} altdss.Line.ILine.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.NumPhases

```{autodoc2-docstring} altdss.Line.ILine.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.NumTerminals

```{autodoc2-docstring} altdss.Line.ILine.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Line.ILine.OCPDevice

```{autodoc2-docstring} altdss.Line.ILine.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.OCPDeviceIndex

```{autodoc2-docstring} altdss.Line.ILine.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Line.ILine.OCPDeviceType

```{autodoc2-docstring} altdss.Line.ILine.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Line.ILine.ParentPDElement

```{autodoc2-docstring} altdss.Line.ILine.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Line.ILine.PhaseLosses

```{autodoc2-docstring} altdss.Line.ILine.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Line.ILine.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Line.ILine.Powers

```{autodoc2-docstring} altdss.Line.ILine.Powers
```

````

````{py:attribute} R0
:canonical: altdss.Line.ILine.R0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.R0
```

````

````{py:attribute} R1
:canonical: altdss.Line.ILine.R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.Line.ILine.RMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.Line.ILine.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Line.ILine.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Repair
```

````

````{py:attribute} Rg
:canonical: altdss.Line.ILine.Rg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.Line.ILine.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Seasons
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.SectionID

```{autodoc2-docstring} altdss.Line.ILine.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Line.ILine.SeqCurrents

```{autodoc2-docstring} altdss.Line.ILine.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Line.ILine.SeqPowers

```{autodoc2-docstring} altdss.Line.ILine.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Line.ILine.SeqVoltages

```{autodoc2-docstring} altdss.Line.ILine.SeqVoltages
```

````

````{py:attribute} Spacing
:canonical: altdss.Line.ILine.Spacing
:type: typing.List[altdss.LineSpacing.LineSpacing]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Spacing
```

````

````{py:attribute} Spacing_str
:canonical: altdss.Line.ILine.Spacing_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Spacing_str
```

````

````{py:attribute} Switch
:canonical: altdss.Line.ILine.Switch
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Switch
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Line.ILine.TotalCustomers

```{autodoc2-docstring} altdss.Line.ILine.TotalCustomers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Line.ILine.TotalMiles

```{autodoc2-docstring} altdss.Line.ILine.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Line.ILine.TotalPowers

```{autodoc2-docstring} altdss.Line.ILine.TotalPowers
```

````

````{py:attribute} Units
:canonical: altdss.Line.ILine.Units
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.Line.ILine.Units_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Units_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Line.ILine.Voltages

```{autodoc2-docstring} altdss.Line.ILine.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Line.ILine.VoltagesMagAng

```{autodoc2-docstring} altdss.Line.ILine.VoltagesMagAng
```

````

````{py:attribute} X0
:canonical: altdss.Line.ILine.X0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.X0
```

````

````{py:attribute} X1
:canonical: altdss.Line.ILine.X1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.Line.ILine.XMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.Line.ILine.Xg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.Xg
```

````

````{py:method} __call__()
:canonical: altdss.Line.ILine.__call__

```{autodoc2-docstring} altdss.Line.ILine.__call__
```

````

````{py:method} __contains__(name: str) -> bool
:canonical: altdss.Line.ILine.__contains__

```{autodoc2-docstring} altdss.Line.ILine.__contains__
```

````

````{py:method} __getitem__(name_or_idx)
:canonical: altdss.Line.ILine.__getitem__

```{autodoc2-docstring} altdss.Line.ILine.__getitem__
```

````

````{py:method} __init__(iobj)
:canonical: altdss.Line.ILine.__init__

```{autodoc2-docstring} altdss.Line.ILine.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Line.ILine.__iter__

```{autodoc2-docstring} altdss.Line.ILine.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Line.ILine.__len__

```{autodoc2-docstring} altdss.Line.ILine.__len__
```

````

````{py:method} batch(**kwargs)
:canonical: altdss.Line.ILine.batch

```{autodoc2-docstring} altdss.Line.ILine.batch
```

````

````{py:method} batch_new(names: typing.Optional[typing.List[typing.AnyStr]] = None, df=None, count: typing.Optional[int] = None, begin_edit=True, **kwargs: typing_extensions.Unpack[altdss.Line.LineBatchProperties]) -> altdss.Line.LineBatch
:canonical: altdss.Line.ILine.batch_new

```{autodoc2-docstring} altdss.Line.ILine.batch_new
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Line.ILine.begin_edit

```{autodoc2-docstring} altdss.Line.ILine.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Line.ILine.end_edit

```{autodoc2-docstring} altdss.Line.ILine.end_edit
```

````

````{py:method} find(name_or_idx: typing.Union[typing.AnyStr, int]) -> altdss.DSSObj.DSSObj
:canonical: altdss.Line.ILine.find

```{autodoc2-docstring} altdss.Line.ILine.find
```

````

````{py:method} new(name: typing.AnyStr, begin_edit=True, activate=False, **kwargs: typing_extensions.Unpack[altdss.Line.LineProperties]) -> altdss.Line.Line
:canonical: altdss.Line.ILine.new

```{autodoc2-docstring} altdss.Line.ILine.new
```

````

````{py:attribute} pctPerm
:canonical: altdss.Line.ILine.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.pctPerm
```

````

````{py:attribute} rho
:canonical: altdss.Line.ILine.rho
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.ILine.rho
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Line.ILine.to_json

```{autodoc2-docstring} altdss.Line.ILine.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Line.ILine.to_list

```{autodoc2-docstring} altdss.Line.ILine.to_list
```

````

`````

`````{py:class} Line(api_util, ptr)
:canonical: altdss.Line.Line

Bases: {py:obj}`altdss.DSSObj.DSSObj`, {py:obj}`altdss.CircuitElement.CircuitElementMixin`, {py:obj}`altdss.PDElement.PDElementMixin`

```{autodoc2-docstring} altdss.Line.Line
```

````{py:method} AccumulatedL() -> float
:canonical: altdss.Line.Line.AccumulatedL

```{autodoc2-docstring} altdss.Line.Line.AccumulatedL
```

````

````{py:attribute} B0
:canonical: altdss.Line.Line.B0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.B0
```

````

````{py:attribute} B1
:canonical: altdss.Line.Line.B1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Line.Line.BaseFreq
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Line.Line.Bus1
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Line.Line.Bus2
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Bus2
```

````

````{py:attribute} C0
:canonical: altdss.Line.Line.C0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.C0
```

````

````{py:attribute} C1
:canonical: altdss.Line.Line.C1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.Line.Line.CMatrix
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.CMatrix
```

````

````{py:method} Close(terminal: int, phase: int) -> None
:canonical: altdss.Line.Line.Close

```{autodoc2-docstring} altdss.Line.Line.Close
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Line.Line.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Line.Line.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Line.Line.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Line.Line.ComplexSeqVoltages
```

````

````{py:attribute} Conductors
:canonical: altdss.Line.Line.Conductors
:type: typing.List[typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Conductors
```

````

````{py:attribute} Conductors_str
:canonical: altdss.Line.Line.Conductors_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Conductors_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Line.Line.Currents

```{autodoc2-docstring} altdss.Line.Line.Currents
```

````

````{py:attribute} DisplayName
:canonical: altdss.Line.Line.DisplayName
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.DisplayName
```

````

````{py:attribute} EarthModel
:canonical: altdss.Line.Line.EarthModel
:type: altdss.enums.EarthModel
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.EarthModel
```

````

````{py:attribute} EarthModel_str
:canonical: altdss.Line.Line.EarthModel_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.EarthModel_str
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Line.Line.EmergAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Line.Line.Enabled
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Enabled
```

````

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.Line.Line.EnergyMeter

```{autodoc2-docstring} altdss.Line.Line.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.Line.Line.EnergyMeterName

```{autodoc2-docstring} altdss.Line.Line.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Line.Line.FaultRate
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.FaultRate
```

````

````{py:method} FromTerminal() -> int
:canonical: altdss.Line.Line.FromTerminal

```{autodoc2-docstring} altdss.Line.Line.FromTerminal
```

````

````{py:method} FullName() -> str
:canonical: altdss.Line.Line.FullName

```{autodoc2-docstring} altdss.Line.Line.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Line.Line.GUID

```{autodoc2-docstring} altdss.Line.Line.GUID
```

````

````{py:attribute} Geometry
:canonical: altdss.Line.Line.Geometry
:type: altdss.LineGeometry.LineGeometry
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Geometry
```

````

````{py:attribute} Geometry_str
:canonical: altdss.Line.Line.Geometry_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Geometry_str
```

````

````{py:method} Handle() -> int
:canonical: altdss.Line.Line.Handle

```{autodoc2-docstring} altdss.Line.Line.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Line.Line.HasOCPDevice

```{autodoc2-docstring} altdss.Line.Line.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Line.Line.HasSwitchControl

```{autodoc2-docstring} altdss.Line.Line.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Line.Line.HasVoltControl

```{autodoc2-docstring} altdss.Line.Line.HasVoltControl
```

````

````{py:method} IsIsolated() -> bool
:canonical: altdss.Line.Line.IsIsolated

```{autodoc2-docstring} altdss.Line.Line.IsIsolated
```

````

````{py:method} IsOpen(terminal: int, phase: int) -> bool
:canonical: altdss.Line.Line.IsOpen

```{autodoc2-docstring} altdss.Line.Line.IsOpen
```

````

````{py:method} IsShunt() -> bool
:canonical: altdss.Line.Line.IsShunt

```{autodoc2-docstring} altdss.Line.Line.IsShunt
```

````

````{py:method} Lambda() -> float
:canonical: altdss.Line.Line.Lambda

```{autodoc2-docstring} altdss.Line.Line.Lambda
```

````

````{py:attribute} Length
:canonical: altdss.Line.Line.Length
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Length
```

````

````{py:method} Like(value: typing.AnyStr)
:canonical: altdss.Line.Line.Like

```{autodoc2-docstring} altdss.Line.Line.Like
```

````

````{py:attribute} LineCode
:canonical: altdss.Line.Line.LineCode
:type: altdss.LineCode.LineCode
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.LineCode
```

````

````{py:attribute} LineCode_str
:canonical: altdss.Line.Line.LineCode_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.LineCode_str
```

````

````{py:attribute} LineType
:canonical: altdss.Line.Line.LineType
:type: altdss.enums.LineType
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.LineType
```

````

````{py:attribute} LineType_str
:canonical: altdss.Line.Line.LineType_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.LineType_str
```

````

````{py:method} Losses() -> complex
:canonical: altdss.Line.Line.Losses

```{autodoc2-docstring} altdss.Line.Line.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Line.Line.MaxCurrent

```{autodoc2-docstring} altdss.Line.Line.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Line.Line.Name
:type: str

```{autodoc2-docstring} altdss.Line.Line.Name
```

````

````{py:method} NodeOrder() -> altdss.types.Int32Array
:canonical: altdss.Line.Line.NodeOrder

```{autodoc2-docstring} altdss.Line.Line.NodeOrder
```

````

````{py:method} NodeRef() -> altdss.types.Int32Array
:canonical: altdss.Line.Line.NodeRef

```{autodoc2-docstring} altdss.Line.Line.NodeRef
```

````

````{py:attribute} NormAmps
:canonical: altdss.Line.Line.NormAmps
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.NormAmps
```

````

````{py:method} NumConductors() -> int
:canonical: altdss.Line.Line.NumConductors

```{autodoc2-docstring} altdss.Line.Line.NumConductors
```

````

````{py:method} NumControllers() -> int
:canonical: altdss.Line.Line.NumControllers

```{autodoc2-docstring} altdss.Line.Line.NumControllers
```

````

````{py:method} NumCustomers() -> int
:canonical: altdss.Line.Line.NumCustomers

```{autodoc2-docstring} altdss.Line.Line.NumCustomers
```

````

````{py:method} NumPhases() -> int
:canonical: altdss.Line.Line.NumPhases

```{autodoc2-docstring} altdss.Line.Line.NumPhases
```

````

````{py:method} NumTerminals() -> int
:canonical: altdss.Line.Line.NumTerminals

```{autodoc2-docstring} altdss.Line.Line.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.Union[altdss.DSSObj.DSSObj, None]
:canonical: altdss.Line.Line.OCPDevice

```{autodoc2-docstring} altdss.Line.Line.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> int
:canonical: altdss.Line.Line.OCPDeviceIndex

```{autodoc2-docstring} altdss.Line.Line.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Line.Line.OCPDeviceType

```{autodoc2-docstring} altdss.Line.Line.OCPDeviceType
```

````

````{py:method} Open(terminal: int, phase: int) -> None
:canonical: altdss.Line.Line.Open

```{autodoc2-docstring} altdss.Line.Line.Open
```

````

````{py:method} ParentPDElement() -> altdss.DSSObj.DSSObj
:canonical: altdss.Line.Line.ParentPDElement

```{autodoc2-docstring} altdss.Line.Line.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Line.Line.PhaseLosses

```{autodoc2-docstring} altdss.Line.Line.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Line.Line.Phases
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Line.Line.Powers

```{autodoc2-docstring} altdss.Line.Line.Powers
```

````

````{py:attribute} R0
:canonical: altdss.Line.Line.R0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.R0
```

````

````{py:attribute} R1
:canonical: altdss.Line.Line.R1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.Line.Line.RMatrix
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.Line.Line.Ratings
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Line.Line.Repair
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Repair
```

````

````{py:method} Residuals() -> altdss.types.Float64Array
:canonical: altdss.Line.Line.Residuals

```{autodoc2-docstring} altdss.Line.Line.Residuals
```

````

````{py:attribute} Rg
:canonical: altdss.Line.Line.Rg
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.Line.Line.Seasons
:type: int
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Seasons
```

````

````{py:method} SectionID() -> int
:canonical: altdss.Line.Line.SectionID

```{autodoc2-docstring} altdss.Line.Line.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Line.Line.SeqCurrents

```{autodoc2-docstring} altdss.Line.Line.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Line.Line.SeqPowers

```{autodoc2-docstring} altdss.Line.Line.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Line.Line.SeqVoltages

```{autodoc2-docstring} altdss.Line.Line.SeqVoltages
```

````

````{py:attribute} Spacing
:canonical: altdss.Line.Line.Spacing
:type: altdss.LineSpacing.LineSpacing
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Spacing
```

````

````{py:attribute} Spacing_str
:canonical: altdss.Line.Line.Spacing_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Spacing_str
```

````

````{py:attribute} Switch
:canonical: altdss.Line.Line.Switch
:type: bool
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Switch
```

````

````{py:method} TotalCustomers() -> int
:canonical: altdss.Line.Line.TotalCustomers

```{autodoc2-docstring} altdss.Line.Line.TotalCustomers
```

````

````{py:method} TotalMiles() -> float
:canonical: altdss.Line.Line.TotalMiles

```{autodoc2-docstring} altdss.Line.Line.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Line.Line.TotalPowers

```{autodoc2-docstring} altdss.Line.Line.TotalPowers
```

````

````{py:attribute} Units
:canonical: altdss.Line.Line.Units
:type: altdss.enums.LengthUnit
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.Line.Line.Units_str
:type: str
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Units_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Line.Line.Voltages

```{autodoc2-docstring} altdss.Line.Line.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Line.Line.VoltagesMagAng

```{autodoc2-docstring} altdss.Line.Line.VoltagesMagAng
```

````

````{py:attribute} X0
:canonical: altdss.Line.Line.X0
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.X0
```

````

````{py:attribute} X1
:canonical: altdss.Line.Line.X1
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.Line.Line.XMatrix
:type: altdss.types.Float64Array
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.Line.Line.Xg
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.Xg
```

````

````{py:method} YPrim() -> altdss.types.ComplexArray
:canonical: altdss.Line.Line.YPrim

```{autodoc2-docstring} altdss.Line.Line.YPrim
```

````

````{py:method} __hash__()
:canonical: altdss.Line.Line.__hash__

```{autodoc2-docstring} altdss.Line.Line.__hash__
```

````

````{py:method} __init__(api_util, ptr)
:canonical: altdss.Line.Line.__init__

```{autodoc2-docstring} altdss.Line.Line.__init__
```

````

````{py:method} __ne__(other)
:canonical: altdss.Line.Line.__ne__

```{autodoc2-docstring} altdss.Line.Line.__ne__
```

````

````{py:method} __repr__()
:canonical: altdss.Line.Line.__repr__

```{autodoc2-docstring} altdss.Line.Line.__repr__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Line.Line.begin_edit

```{autodoc2-docstring} altdss.Line.Line.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Line.Line.end_edit

```{autodoc2-docstring} altdss.Line.Line.end_edit
```

````

````{py:method} pctEmerg(allNodes=False) -> float
:canonical: altdss.Line.Line.pctEmerg

```{autodoc2-docstring} altdss.Line.Line.pctEmerg
```

````

````{py:method} pctNorm(allNodes=False) -> float
:canonical: altdss.Line.Line.pctNorm

```{autodoc2-docstring} altdss.Line.Line.pctNorm
```

````

````{py:attribute} pctPerm
:canonical: altdss.Line.Line.pctPerm
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.pctPerm
```

````

````{py:attribute} rho
:canonical: altdss.Line.Line.rho
:type: float
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.Line.rho
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Line.Line.to_json

```{autodoc2-docstring} altdss.Line.Line.to_json
```

````

`````

`````{py:class} LineBatch(api_util, **kwargs)
:canonical: altdss.Line.LineBatch

Bases: {py:obj}`altdss.Batch.DSSBatch`, {py:obj}`altdss.CircuitElement.CircuitElementBatchMixin`, {py:obj}`altdss.PDElement.PDElementBatchMixin`

```{autodoc2-docstring} altdss.Line.LineBatch
```

````{py:method} AccumulatedL() -> altdss.types.Float64Array
:canonical: altdss.Line.LineBatch.AccumulatedL

```{autodoc2-docstring} altdss.Line.LineBatch.AccumulatedL
```

````

````{py:attribute} B0
:canonical: altdss.Line.LineBatch.B0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.B0
```

````

````{py:attribute} B1
:canonical: altdss.Line.LineBatch.B1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Line.LineBatch.BaseFreq
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Line.LineBatch.Bus1
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Line.LineBatch.Bus2
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Bus2
```

````

````{py:attribute} C0
:canonical: altdss.Line.LineBatch.C0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.C0
```

````

````{py:attribute} C1
:canonical: altdss.Line.LineBatch.C1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.Line.LineBatch.CMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.CMatrix
```

````

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.Line.LineBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.Line.LineBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.Line.LineBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.Line.LineBatch.ComplexSeqVoltages
```

````

````{py:attribute} Conductors
:canonical: altdss.Line.LineBatch.Conductors
:type: typing.List[typing.List[typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Conductors
```

````

````{py:attribute} Conductors_str
:canonical: altdss.Line.LineBatch.Conductors_str
:type: typing.List[typing.List[str]]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Conductors_str
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.Line.LineBatch.Currents

```{autodoc2-docstring} altdss.Line.LineBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.Line.LineBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.Line.LineBatch.CurrentsMagAng
```

````

````{py:attribute} EarthModel
:canonical: altdss.Line.LineBatch.EarthModel
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.EarthModel
```

````

````{py:attribute} EarthModel_str
:canonical: altdss.Line.LineBatch.EarthModel_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.EarthModel_str
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Line.LineBatch.EmergAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Line.LineBatch.Enabled
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Enabled
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Line.LineBatch.EnergyMeter

```{autodoc2-docstring} altdss.Line.LineBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.Line.LineBatch.EnergyMeterName

```{autodoc2-docstring} altdss.Line.LineBatch.EnergyMeterName
```

````

````{py:attribute} FaultRate
:canonical: altdss.Line.LineBatch.FaultRate
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.FaultRate
```

````

````{py:method} FromTerminal() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.FromTerminal

```{autodoc2-docstring} altdss.Line.LineBatch.FromTerminal
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.Line.LineBatch.FullName

```{autodoc2-docstring} altdss.Line.LineBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.Line.LineBatch.GUID

```{autodoc2-docstring} altdss.Line.LineBatch.GUID
```

````

````{py:attribute} Geometry
:canonical: altdss.Line.LineBatch.Geometry
:type: typing.List[altdss.LineGeometry.LineGeometry]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Geometry
```

````

````{py:attribute} Geometry_str
:canonical: altdss.Line.LineBatch.Geometry_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Geometry_str
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.Handle

```{autodoc2-docstring} altdss.Line.LineBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.Line.LineBatch.HasOCPDevice

```{autodoc2-docstring} altdss.Line.LineBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.Line.LineBatch.HasSwitchControl

```{autodoc2-docstring} altdss.Line.LineBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.Line.LineBatch.HasVoltControl

```{autodoc2-docstring} altdss.Line.LineBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.Line.LineBatch.IsIsolated

```{autodoc2-docstring} altdss.Line.LineBatch.IsIsolated
```

````

````{py:method} IsShunt() -> typing.List[bool]
:canonical: altdss.Line.LineBatch.IsShunt

```{autodoc2-docstring} altdss.Line.LineBatch.IsShunt
```

````

````{py:method} Lambda() -> altdss.types.Float64Array
:canonical: altdss.Line.LineBatch.Lambda

```{autodoc2-docstring} altdss.Line.LineBatch.Lambda
```

````

````{py:attribute} Length
:canonical: altdss.Line.LineBatch.Length
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Length
```

````

````{py:method} Like(value: typing.AnyStr, flags: altdss.enums.SetterFlags = 0)
:canonical: altdss.Line.LineBatch.Like

```{autodoc2-docstring} altdss.Line.LineBatch.Like
```

````

````{py:attribute} LineCode
:canonical: altdss.Line.LineBatch.LineCode
:type: typing.List[altdss.LineCode.LineCode]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.LineCode
```

````

````{py:attribute} LineCode_str
:canonical: altdss.Line.LineBatch.LineCode_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.LineCode_str
```

````

````{py:attribute} LineType
:canonical: altdss.Line.LineBatch.LineType
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.LineType
```

````

````{py:attribute} LineType_str
:canonical: altdss.Line.LineBatch.LineType_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.LineType_str
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.Line.LineBatch.Losses

```{autodoc2-docstring} altdss.Line.LineBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.Line.LineBatch.MaxCurrent

```{autodoc2-docstring} altdss.Line.LineBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.Line.LineBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.Line.LineBatch.Name
```

````

````{py:attribute} NormAmps
:canonical: altdss.Line.LineBatch.NormAmps
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.NormAmps
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.NumConductors

```{autodoc2-docstring} altdss.Line.LineBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.NumControllers

```{autodoc2-docstring} altdss.Line.LineBatch.NumControllers
```

````

````{py:method} NumCustomers() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.NumCustomers

```{autodoc2-docstring} altdss.Line.LineBatch.NumCustomers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.NumPhases

```{autodoc2-docstring} altdss.Line.LineBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.NumTerminals

```{autodoc2-docstring} altdss.Line.LineBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.Line.LineBatch.OCPDevice

```{autodoc2-docstring} altdss.Line.LineBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.Line.LineBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.Line.LineBatch.OCPDeviceType

```{autodoc2-docstring} altdss.Line.LineBatch.OCPDeviceType
```

````

````{py:method} ParentPDElement() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.Line.LineBatch.ParentPDElement

```{autodoc2-docstring} altdss.Line.LineBatch.ParentPDElement
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.Line.LineBatch.PhaseLosses

```{autodoc2-docstring} altdss.Line.LineBatch.PhaseLosses
```

````

````{py:attribute} Phases
:canonical: altdss.Line.LineBatch.Phases
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Phases
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.Line.LineBatch.Powers

```{autodoc2-docstring} altdss.Line.LineBatch.Powers
```

````

````{py:attribute} R0
:canonical: altdss.Line.LineBatch.R0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.R0
```

````

````{py:attribute} R1
:canonical: altdss.Line.LineBatch.R1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.Line.LineBatch.RMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.Line.LineBatch.Ratings
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Line.LineBatch.Repair
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Repair
```

````

````{py:attribute} Rg
:canonical: altdss.Line.LineBatch.Rg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.Line.LineBatch.Seasons
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Seasons
```

````

````{py:method} SectionID() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.SectionID

```{autodoc2-docstring} altdss.Line.LineBatch.SectionID
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.Line.LineBatch.SeqCurrents

```{autodoc2-docstring} altdss.Line.LineBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.Line.LineBatch.SeqPowers

```{autodoc2-docstring} altdss.Line.LineBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.Line.LineBatch.SeqVoltages

```{autodoc2-docstring} altdss.Line.LineBatch.SeqVoltages
```

````

````{py:attribute} Spacing
:canonical: altdss.Line.LineBatch.Spacing
:type: typing.List[altdss.LineSpacing.LineSpacing]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Spacing
```

````

````{py:attribute} Spacing_str
:canonical: altdss.Line.LineBatch.Spacing_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Spacing_str
```

````

````{py:attribute} Switch
:canonical: altdss.Line.LineBatch.Switch
:type: typing.List[bool]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Switch
```

````

````{py:method} TotalCustomers() -> altdss.types.Int32Array
:canonical: altdss.Line.LineBatch.TotalCustomers

```{autodoc2-docstring} altdss.Line.LineBatch.TotalCustomers
```

````

````{py:method} TotalMiles() -> altdss.types.Float64Array
:canonical: altdss.Line.LineBatch.TotalMiles

```{autodoc2-docstring} altdss.Line.LineBatch.TotalMiles
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.Line.LineBatch.TotalPowers

```{autodoc2-docstring} altdss.Line.LineBatch.TotalPowers
```

````

````{py:attribute} Units
:canonical: altdss.Line.LineBatch.Units
:type: altdss.ArrayProxy.BatchInt32ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Units
```

````

````{py:attribute} Units_str
:canonical: altdss.Line.LineBatch.Units_str
:type: typing.List[str]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Units_str
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.Line.LineBatch.Voltages

```{autodoc2-docstring} altdss.Line.LineBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.Line.LineBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.Line.LineBatch.VoltagesMagAng
```

````

````{py:attribute} X0
:canonical: altdss.Line.LineBatch.X0
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.X0
```

````

````{py:attribute} X1
:canonical: altdss.Line.LineBatch.X1
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.Line.LineBatch.XMatrix
:type: typing.List[altdss.types.Float64Array]
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.Line.LineBatch.Xg
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.Xg
```

````

````{py:method} __call__()
:canonical: altdss.Line.LineBatch.__call__

```{autodoc2-docstring} altdss.Line.LineBatch.__call__
```

````

````{py:method} __getitem__(idx0) -> altdss.DSSObj.DSSObj
:canonical: altdss.Line.LineBatch.__getitem__

```{autodoc2-docstring} altdss.Line.LineBatch.__getitem__
```

````

````{py:method} __init__(api_util, **kwargs)
:canonical: altdss.Line.LineBatch.__init__

```{autodoc2-docstring} altdss.Line.LineBatch.__init__
```

````

````{py:method} __iter__()
:canonical: altdss.Line.LineBatch.__iter__

```{autodoc2-docstring} altdss.Line.LineBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.Line.LineBatch.__len__

```{autodoc2-docstring} altdss.Line.LineBatch.__len__
```

````

````{py:method} begin_edit() -> None
:canonical: altdss.Line.LineBatch.begin_edit

```{autodoc2-docstring} altdss.Line.LineBatch.begin_edit
```

````

````{py:method} end_edit(num_changes: int = 1) -> None
:canonical: altdss.Line.LineBatch.end_edit

```{autodoc2-docstring} altdss.Line.LineBatch.end_edit
```

````

````{py:attribute} pctPerm
:canonical: altdss.Line.LineBatch.pctPerm
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.pctPerm
```

````

````{py:attribute} rho
:canonical: altdss.Line.LineBatch.rho
:type: altdss.ArrayProxy.BatchFloat64ArrayProxy
:value: >
   'property(...)'

```{autodoc2-docstring} altdss.Line.LineBatch.rho
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.Line.LineBatch.to_json

```{autodoc2-docstring} altdss.Line.LineBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.Line.LineBatch.to_list

```{autodoc2-docstring} altdss.Line.LineBatch.to_list
```

````

`````

`````{py:class} LineBatchProperties()
:canonical: altdss.Line.LineBatchProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Line.LineBatchProperties
```

````{py:attribute} B0
:canonical: altdss.Line.LineBatchProperties.B0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.B0
```

````

````{py:attribute} B1
:canonical: altdss.Line.LineBatchProperties.B1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Line.LineBatchProperties.BaseFreq
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Line.LineBatchProperties.Bus1
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Line.LineBatchProperties.Bus2
:type: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Bus2
```

````

````{py:attribute} C0
:canonical: altdss.Line.LineBatchProperties.C0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.C0
```

````

````{py:attribute} C1
:canonical: altdss.Line.LineBatchProperties.C1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.Line.LineBatchProperties.CMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.CMatrix
```

````

````{py:attribute} Conductors
:canonical: altdss.Line.LineBatchProperties.Conductors
:type: typing.Union[typing.List[typing.AnyStr], typing.List[typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Conductors
```

````

````{py:attribute} EarthModel
:canonical: altdss.Line.LineBatchProperties.EarthModel
:type: typing.Union[typing.AnyStr, int, altdss.enums.EarthModel, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.EarthModel], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.EarthModel
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Line.LineBatchProperties.EmergAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Line.LineBatchProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.Line.LineBatchProperties.FaultRate
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.FaultRate
```

````

````{py:attribute} Geometry
:canonical: altdss.Line.LineBatchProperties.Geometry
:type: typing.Union[typing.AnyStr, altdss.LineGeometry.LineGeometry, typing.List[typing.AnyStr], typing.List[altdss.LineGeometry.LineGeometry]]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Geometry
```

````

````{py:attribute} Length
:canonical: altdss.Line.LineBatchProperties.Length
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Length
```

````

````{py:attribute} Like
:canonical: altdss.Line.LineBatchProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Like
```

````

````{py:attribute} LineCode
:canonical: altdss.Line.LineBatchProperties.LineCode
:type: typing.Union[typing.AnyStr, altdss.LineCode.LineCode, typing.List[typing.AnyStr], typing.List[altdss.LineCode.LineCode]]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.LineCode
```

````

````{py:attribute} LineType
:canonical: altdss.Line.LineBatchProperties.LineType
:type: typing.Union[typing.AnyStr, int, altdss.enums.LineType, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LineType], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.LineType
```

````

````{py:attribute} NormAmps
:canonical: altdss.Line.LineBatchProperties.NormAmps
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.NormAmps
```

````

````{py:attribute} Phases
:canonical: altdss.Line.LineBatchProperties.Phases
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Phases
```

````

````{py:attribute} R0
:canonical: altdss.Line.LineBatchProperties.R0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.R0
```

````

````{py:attribute} R1
:canonical: altdss.Line.LineBatchProperties.R1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.Line.LineBatchProperties.RMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.Line.LineBatchProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Line.LineBatchProperties.Repair
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Repair
```

````

````{py:attribute} Rg
:canonical: altdss.Line.LineBatchProperties.Rg
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.Line.LineBatchProperties.Seasons
:type: typing.Union[int, altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Seasons
```

````

````{py:attribute} Spacing
:canonical: altdss.Line.LineBatchProperties.Spacing
:type: typing.Union[typing.AnyStr, altdss.LineSpacing.LineSpacing, typing.List[typing.AnyStr], typing.List[altdss.LineSpacing.LineSpacing]]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Spacing
```

````

````{py:attribute} Switch
:canonical: altdss.Line.LineBatchProperties.Switch
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Switch
```

````

````{py:attribute} Units
:canonical: altdss.Line.LineBatchProperties.Units
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit, typing.List[typing.AnyStr], typing.List[int], typing.List[altdss.enums.LengthUnit], altdss.types.Int32Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Units
```

````

````{py:attribute} X0
:canonical: altdss.Line.LineBatchProperties.X0
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.X0
```

````

````{py:attribute} X1
:canonical: altdss.Line.LineBatchProperties.X1
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.Line.LineBatchProperties.XMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.Line.LineBatchProperties.Xg
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.Xg
```

````

````{py:method} __contains__()
:canonical: altdss.Line.LineBatchProperties.__contains__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Line.LineBatchProperties.__delattr__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Line.LineBatchProperties.__delitem__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Line.LineBatchProperties.__dir__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Line.LineBatchProperties.__format__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Line.LineBatchProperties.__ge__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Line.LineBatchProperties.__getattribute__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Line.LineBatchProperties.__getitem__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Line.LineBatchProperties.__getstate__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Line.LineBatchProperties.__gt__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Line.LineBatchProperties.__init__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Line.LineBatchProperties.__ior__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Line.LineBatchProperties.__iter__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Line.LineBatchProperties.__le__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Line.LineBatchProperties.__len__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Line.LineBatchProperties.__lt__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Line.LineBatchProperties.__ne__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Line.LineBatchProperties.__new__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Line.LineBatchProperties.__or__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Line.LineBatchProperties.__reduce__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Line.LineBatchProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Line.LineBatchProperties.__repr__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Line.LineBatchProperties.__reversed__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Line.LineBatchProperties.__ror__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Line.LineBatchProperties.__setitem__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Line.LineBatchProperties.__sizeof__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Line.LineBatchProperties.__str__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Line.LineBatchProperties.__subclasshook__

```{autodoc2-docstring} altdss.Line.LineBatchProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Line.LineBatchProperties.clear

```{autodoc2-docstring} altdss.Line.LineBatchProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Line.LineBatchProperties.copy

```{autodoc2-docstring} altdss.Line.LineBatchProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Line.LineBatchProperties.get

```{autodoc2-docstring} altdss.Line.LineBatchProperties.get
```

````

````{py:method} items()
:canonical: altdss.Line.LineBatchProperties.items

```{autodoc2-docstring} altdss.Line.LineBatchProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Line.LineBatchProperties.keys

```{autodoc2-docstring} altdss.Line.LineBatchProperties.keys
```

````

````{py:attribute} pctPerm
:canonical: altdss.Line.LineBatchProperties.pctPerm
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.pctPerm
```

````

````{py:method} pop()
:canonical: altdss.Line.LineBatchProperties.pop

```{autodoc2-docstring} altdss.Line.LineBatchProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Line.LineBatchProperties.popitem

```{autodoc2-docstring} altdss.Line.LineBatchProperties.popitem
```

````

````{py:attribute} rho
:canonical: altdss.Line.LineBatchProperties.rho
:type: typing.Union[float, altdss.types.Float64Array]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineBatchProperties.rho
```

````

````{py:method} setdefault()
:canonical: altdss.Line.LineBatchProperties.setdefault

```{autodoc2-docstring} altdss.Line.LineBatchProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Line.LineBatchProperties.update

```{autodoc2-docstring} altdss.Line.LineBatchProperties.update
```

````

````{py:method} values()
:canonical: altdss.Line.LineBatchProperties.values

```{autodoc2-docstring} altdss.Line.LineBatchProperties.values
```

````

`````

`````{py:class} LineProperties()
:canonical: altdss.Line.LineProperties

Bases: {py:obj}`typing_extensions.TypedDict`

```{autodoc2-docstring} altdss.Line.LineProperties
```

````{py:attribute} B0
:canonical: altdss.Line.LineProperties.B0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.B0
```

````

````{py:attribute} B1
:canonical: altdss.Line.LineProperties.B1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.B1
```

````

````{py:attribute} BaseFreq
:canonical: altdss.Line.LineProperties.BaseFreq
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.BaseFreq
```

````

````{py:attribute} Bus1
:canonical: altdss.Line.LineProperties.Bus1
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Bus1
```

````

````{py:attribute} Bus2
:canonical: altdss.Line.LineProperties.Bus2
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Bus2
```

````

````{py:attribute} C0
:canonical: altdss.Line.LineProperties.C0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.C0
```

````

````{py:attribute} C1
:canonical: altdss.Line.LineProperties.C1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.C1
```

````

````{py:attribute} CMatrix
:canonical: altdss.Line.LineProperties.CMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.CMatrix
```

````

````{py:attribute} Conductors
:canonical: altdss.Line.LineProperties.Conductors
:type: typing.List[typing.Union[typing.AnyStr, typing.Union[altdss.WireData.WireData, altdss.CNData.CNData, altdss.TSData.TSData]]]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Conductors
```

````

````{py:attribute} EarthModel
:canonical: altdss.Line.LineProperties.EarthModel
:type: typing.Union[typing.AnyStr, int, altdss.enums.EarthModel]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.EarthModel
```

````

````{py:attribute} EmergAmps
:canonical: altdss.Line.LineProperties.EmergAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.EmergAmps
```

````

````{py:attribute} Enabled
:canonical: altdss.Line.LineProperties.Enabled
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Enabled
```

````

````{py:attribute} FaultRate
:canonical: altdss.Line.LineProperties.FaultRate
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.FaultRate
```

````

````{py:attribute} Geometry
:canonical: altdss.Line.LineProperties.Geometry
:type: typing.Union[typing.AnyStr, altdss.LineGeometry.LineGeometry]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Geometry
```

````

````{py:attribute} Length
:canonical: altdss.Line.LineProperties.Length
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Length
```

````

````{py:attribute} Like
:canonical: altdss.Line.LineProperties.Like
:type: typing.AnyStr
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Like
```

````

````{py:attribute} LineCode
:canonical: altdss.Line.LineProperties.LineCode
:type: typing.Union[typing.AnyStr, altdss.LineCode.LineCode]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.LineCode
```

````

````{py:attribute} LineType
:canonical: altdss.Line.LineProperties.LineType
:type: typing.Union[typing.AnyStr, int, altdss.enums.LineType]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.LineType
```

````

````{py:attribute} NormAmps
:canonical: altdss.Line.LineProperties.NormAmps
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.NormAmps
```

````

````{py:attribute} Phases
:canonical: altdss.Line.LineProperties.Phases
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Phases
```

````

````{py:attribute} R0
:canonical: altdss.Line.LineProperties.R0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.R0
```

````

````{py:attribute} R1
:canonical: altdss.Line.LineProperties.R1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.R1
```

````

````{py:attribute} RMatrix
:canonical: altdss.Line.LineProperties.RMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.RMatrix
```

````

````{py:attribute} Ratings
:canonical: altdss.Line.LineProperties.Ratings
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Ratings
```

````

````{py:attribute} Repair
:canonical: altdss.Line.LineProperties.Repair
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Repair
```

````

````{py:attribute} Rg
:canonical: altdss.Line.LineProperties.Rg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Rg
```

````

````{py:attribute} Seasons
:canonical: altdss.Line.LineProperties.Seasons
:type: int
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Seasons
```

````

````{py:attribute} Spacing
:canonical: altdss.Line.LineProperties.Spacing
:type: typing.Union[typing.AnyStr, altdss.LineSpacing.LineSpacing]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Spacing
```

````

````{py:attribute} Switch
:canonical: altdss.Line.LineProperties.Switch
:type: bool
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Switch
```

````

````{py:attribute} Units
:canonical: altdss.Line.LineProperties.Units
:type: typing.Union[typing.AnyStr, int, altdss.enums.LengthUnit]
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Units
```

````

````{py:attribute} X0
:canonical: altdss.Line.LineProperties.X0
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.X0
```

````

````{py:attribute} X1
:canonical: altdss.Line.LineProperties.X1
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.X1
```

````

````{py:attribute} XMatrix
:canonical: altdss.Line.LineProperties.XMatrix
:type: altdss.types.Float64Array
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.XMatrix
```

````

````{py:attribute} Xg
:canonical: altdss.Line.LineProperties.Xg
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.Xg
```

````

````{py:method} __contains__()
:canonical: altdss.Line.LineProperties.__contains__

```{autodoc2-docstring} altdss.Line.LineProperties.__contains__
```

````

````{py:method} __delattr__()
:canonical: altdss.Line.LineProperties.__delattr__

```{autodoc2-docstring} altdss.Line.LineProperties.__delattr__
```

````

````{py:method} __delitem__()
:canonical: altdss.Line.LineProperties.__delitem__

```{autodoc2-docstring} altdss.Line.LineProperties.__delitem__
```

````

````{py:method} __dir__()
:canonical: altdss.Line.LineProperties.__dir__

```{autodoc2-docstring} altdss.Line.LineProperties.__dir__
```

````

````{py:method} __format__()
:canonical: altdss.Line.LineProperties.__format__

```{autodoc2-docstring} altdss.Line.LineProperties.__format__
```

````

````{py:method} __ge__()
:canonical: altdss.Line.LineProperties.__ge__

```{autodoc2-docstring} altdss.Line.LineProperties.__ge__
```

````

````{py:method} __getattribute__()
:canonical: altdss.Line.LineProperties.__getattribute__

```{autodoc2-docstring} altdss.Line.LineProperties.__getattribute__
```

````

````{py:method} __getitem__()
:canonical: altdss.Line.LineProperties.__getitem__

```{autodoc2-docstring} altdss.Line.LineProperties.__getitem__
```

````

````{py:method} __getstate__()
:canonical: altdss.Line.LineProperties.__getstate__

```{autodoc2-docstring} altdss.Line.LineProperties.__getstate__
```

````

````{py:method} __gt__()
:canonical: altdss.Line.LineProperties.__gt__

```{autodoc2-docstring} altdss.Line.LineProperties.__gt__
```

````

````{py:method} __init__()
:canonical: altdss.Line.LineProperties.__init__

```{autodoc2-docstring} altdss.Line.LineProperties.__init__
```

````

````{py:method} __ior__()
:canonical: altdss.Line.LineProperties.__ior__

```{autodoc2-docstring} altdss.Line.LineProperties.__ior__
```

````

````{py:method} __iter__()
:canonical: altdss.Line.LineProperties.__iter__

```{autodoc2-docstring} altdss.Line.LineProperties.__iter__
```

````

````{py:method} __le__()
:canonical: altdss.Line.LineProperties.__le__

```{autodoc2-docstring} altdss.Line.LineProperties.__le__
```

````

````{py:method} __len__()
:canonical: altdss.Line.LineProperties.__len__

```{autodoc2-docstring} altdss.Line.LineProperties.__len__
```

````

````{py:method} __lt__()
:canonical: altdss.Line.LineProperties.__lt__

```{autodoc2-docstring} altdss.Line.LineProperties.__lt__
```

````

````{py:method} __ne__()
:canonical: altdss.Line.LineProperties.__ne__

```{autodoc2-docstring} altdss.Line.LineProperties.__ne__
```

````

````{py:method} __new__()
:canonical: altdss.Line.LineProperties.__new__

```{autodoc2-docstring} altdss.Line.LineProperties.__new__
```

````

````{py:method} __or__()
:canonical: altdss.Line.LineProperties.__or__

```{autodoc2-docstring} altdss.Line.LineProperties.__or__
```

````

````{py:method} __reduce__()
:canonical: altdss.Line.LineProperties.__reduce__

```{autodoc2-docstring} altdss.Line.LineProperties.__reduce__
```

````

````{py:method} __reduce_ex__()
:canonical: altdss.Line.LineProperties.__reduce_ex__

```{autodoc2-docstring} altdss.Line.LineProperties.__reduce_ex__
```

````

````{py:method} __repr__()
:canonical: altdss.Line.LineProperties.__repr__

```{autodoc2-docstring} altdss.Line.LineProperties.__repr__
```

````

````{py:method} __reversed__()
:canonical: altdss.Line.LineProperties.__reversed__

```{autodoc2-docstring} altdss.Line.LineProperties.__reversed__
```

````

````{py:method} __ror__()
:canonical: altdss.Line.LineProperties.__ror__

```{autodoc2-docstring} altdss.Line.LineProperties.__ror__
```

````

````{py:method} __setitem__()
:canonical: altdss.Line.LineProperties.__setitem__

```{autodoc2-docstring} altdss.Line.LineProperties.__setitem__
```

````

````{py:method} __sizeof__()
:canonical: altdss.Line.LineProperties.__sizeof__

```{autodoc2-docstring} altdss.Line.LineProperties.__sizeof__
```

````

````{py:method} __str__()
:canonical: altdss.Line.LineProperties.__str__

```{autodoc2-docstring} altdss.Line.LineProperties.__str__
```

````

````{py:method} __subclasshook__()
:canonical: altdss.Line.LineProperties.__subclasshook__

```{autodoc2-docstring} altdss.Line.LineProperties.__subclasshook__
```

````

````{py:method} clear()
:canonical: altdss.Line.LineProperties.clear

```{autodoc2-docstring} altdss.Line.LineProperties.clear
```

````

````{py:method} copy()
:canonical: altdss.Line.LineProperties.copy

```{autodoc2-docstring} altdss.Line.LineProperties.copy
```

````

````{py:method} get()
:canonical: altdss.Line.LineProperties.get

```{autodoc2-docstring} altdss.Line.LineProperties.get
```

````

````{py:method} items()
:canonical: altdss.Line.LineProperties.items

```{autodoc2-docstring} altdss.Line.LineProperties.items
```

````

````{py:method} keys()
:canonical: altdss.Line.LineProperties.keys

```{autodoc2-docstring} altdss.Line.LineProperties.keys
```

````

````{py:attribute} pctPerm
:canonical: altdss.Line.LineProperties.pctPerm
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.pctPerm
```

````

````{py:method} pop()
:canonical: altdss.Line.LineProperties.pop

```{autodoc2-docstring} altdss.Line.LineProperties.pop
```

````

````{py:method} popitem()
:canonical: altdss.Line.LineProperties.popitem

```{autodoc2-docstring} altdss.Line.LineProperties.popitem
```

````

````{py:attribute} rho
:canonical: altdss.Line.LineProperties.rho
:type: float
:value: >
   None

```{autodoc2-docstring} altdss.Line.LineProperties.rho
```

````

````{py:method} setdefault()
:canonical: altdss.Line.LineProperties.setdefault

```{autodoc2-docstring} altdss.Line.LineProperties.setdefault
```

````

````{py:method} update()
:canonical: altdss.Line.LineProperties.update

```{autodoc2-docstring} altdss.Line.LineProperties.update
```

````

````{py:method} values()
:canonical: altdss.Line.LineProperties.values

```{autodoc2-docstring} altdss.Line.LineProperties.values
```

````

`````
