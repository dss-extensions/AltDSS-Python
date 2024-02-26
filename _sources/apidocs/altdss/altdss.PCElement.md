# {py:mod}`altdss.PCElement`

```{py:module} altdss.PCElement
```

```{autodoc2-docstring} altdss.PCElement
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PCElementBatch <altdss.PCElement.PCElementBatch>`
  - ```{autodoc2-docstring} altdss.PCElement.PCElementBatch
    :summary:
    ```
* - {py:obj}`PCElementBatchMixin <altdss.PCElement.PCElementBatchMixin>`
  - ```{autodoc2-docstring} altdss.PCElement.PCElementBatchMixin
    :summary:
    ```
* - {py:obj}`PCElementMixin <altdss.PCElement.PCElementMixin>`
  - ```{autodoc2-docstring} altdss.PCElement.PCElementMixin
    :summary:
    ```
````

### API

`````{py:class} PCElementBatch(func, parent, sync_cls_idx=ExtraClassIDs.PCElements, copy_safe=False)
:canonical: altdss.PCElement.PCElementBatch

Bases: {py:obj}`altdss.CircuitElement.CircuitElementBatch`, {py:obj}`altdss.PCElement.PCElementBatchMixin`, {py:obj}`altdss.CircuitElement.ElementHasRegistersMixin`

```{autodoc2-docstring} altdss.PCElement.PCElementBatch
```

````{py:method} ComplexSeqCurrents() -> altdss.types.ComplexArray
:canonical: altdss.PCElement.PCElementBatch.ComplexSeqCurrents

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.ComplexSeqCurrents
```

````

````{py:method} ComplexSeqVoltages() -> altdss.types.ComplexArray
:canonical: altdss.PCElement.PCElementBatch.ComplexSeqVoltages

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.ComplexSeqVoltages
```

````

````{py:method} Currents() -> altdss.types.ComplexArray
:canonical: altdss.PCElement.PCElementBatch.Currents

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.Currents
```

````

````{py:method} CurrentsMagAng() -> altdss.types.Float64Array
:canonical: altdss.PCElement.PCElementBatch.CurrentsMagAng

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.CurrentsMagAng
```

````

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.PCElement.PCElementBatch.EnergyMeter

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.PCElement.PCElementBatch.EnergyMeterName

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.EnergyMeterName
```

````

````{py:method} FullName() -> typing.List[str]
:canonical: altdss.PCElement.PCElementBatch.FullName

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.FullName
```

````

````{py:method} GUID() -> str
:canonical: altdss.PCElement.PCElementBatch.GUID

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.GUID
```

````

````{py:method} Handle() -> altdss.types.Int32Array
:canonical: altdss.PCElement.PCElementBatch.Handle

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.Handle
```

````

````{py:method} HasOCPDevice() -> bool
:canonical: altdss.PCElement.PCElementBatch.HasOCPDevice

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.HasOCPDevice
```

````

````{py:method} HasSwitchControl() -> bool
:canonical: altdss.PCElement.PCElementBatch.HasSwitchControl

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.HasSwitchControl
```

````

````{py:method} HasVoltControl() -> bool
:canonical: altdss.PCElement.PCElementBatch.HasVoltControl

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.HasVoltControl
```

````

````{py:method} IsIsolated() -> altdss.types.BoolArray
:canonical: altdss.PCElement.PCElementBatch.IsIsolated

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.IsIsolated
```

````

````{py:method} Losses() -> altdss.types.ComplexArray
:canonical: altdss.PCElement.PCElementBatch.Losses

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.Losses
```

````

````{py:method} MaxCurrent(terminal: int) -> float
:canonical: altdss.PCElement.PCElementBatch.MaxCurrent

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.MaxCurrent
```

````

````{py:property} Name
:canonical: altdss.PCElement.PCElementBatch.Name
:type: typing.List[str]

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.Name
```

````

````{py:method} NumConductors() -> altdss.types.Int32Array
:canonical: altdss.PCElement.PCElementBatch.NumConductors

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.NumConductors
```

````

````{py:method} NumControllers() -> altdss.types.Int32Array
:canonical: altdss.PCElement.PCElementBatch.NumControllers

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.NumControllers
```

````

````{py:method} NumPhases() -> altdss.types.Int32Array
:canonical: altdss.PCElement.PCElementBatch.NumPhases

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.NumPhases
```

````

````{py:method} NumTerminals() -> altdss.types.Int32Array
:canonical: altdss.PCElement.PCElementBatch.NumTerminals

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.NumTerminals
```

````

````{py:method} OCPDevice() -> typing.List[typing.Union[altdss.DSSObj.DSSObj, None]]
:canonical: altdss.PCElement.PCElementBatch.OCPDevice

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.OCPDevice
```

````

````{py:method} OCPDeviceIndex() -> altdss.types.Int32Array
:canonical: altdss.PCElement.PCElementBatch.OCPDeviceIndex

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.OCPDeviceIndex
```

````

````{py:method} OCPDeviceType() -> dss.enums.OCPDevType
:canonical: altdss.PCElement.PCElementBatch.OCPDeviceType

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.OCPDeviceType
```

````

````{py:method} PhaseLosses() -> altdss.types.ComplexArray
:canonical: altdss.PCElement.PCElementBatch.PhaseLosses

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.PhaseLosses
```

````

````{py:method} Powers() -> altdss.types.ComplexArray
:canonical: altdss.PCElement.PCElementBatch.Powers

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.Powers
```

````

````{py:method} RegisterNames() -> typing.List[str]
:canonical: altdss.PCElement.PCElementBatch.RegisterNames

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.RegisterNames
```

````

````{py:method} RegisterValues() -> altdss.types.Float64Array
:canonical: altdss.PCElement.PCElementBatch.RegisterValues

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.RegisterValues
```

````

````{py:method} RegistersDict() -> typing.Dict[str, float]
:canonical: altdss.PCElement.PCElementBatch.RegistersDict

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.RegistersDict
```

````

````{py:method} SeqCurrents() -> altdss.types.Float64Array
:canonical: altdss.PCElement.PCElementBatch.SeqCurrents

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.SeqCurrents
```

````

````{py:method} SeqPowers() -> altdss.types.ComplexArray
:canonical: altdss.PCElement.PCElementBatch.SeqPowers

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.SeqPowers
```

````

````{py:method} SeqVoltages() -> altdss.types.Float64Array
:canonical: altdss.PCElement.PCElementBatch.SeqVoltages

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.SeqVoltages
```

````

````{py:method} TotalPowers() -> altdss.types.ComplexArray
:canonical: altdss.PCElement.PCElementBatch.TotalPowers

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.TotalPowers
```

````

````{py:method} Voltages() -> altdss.types.ComplexArray
:canonical: altdss.PCElement.PCElementBatch.Voltages

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.Voltages
```

````

````{py:method} VoltagesMagAng() -> altdss.types.Float64Array
:canonical: altdss.PCElement.PCElementBatch.VoltagesMagAng

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.VoltagesMagAng
```

````

````{py:method} __call__()
:canonical: altdss.PCElement.PCElementBatch.__call__

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.__call__
```

````

````{py:method} __init__(func, parent, sync_cls_idx=ExtraClassIDs.PCElements, copy_safe=False)
:canonical: altdss.PCElement.PCElementBatch.__init__

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.__init__
```

````

````{py:method} __iter__() -> typing.Iterator[altdss.DSSObj.DSSObj]
:canonical: altdss.PCElement.PCElementBatch.__iter__

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.__iter__
```

````

````{py:method} __len__() -> int
:canonical: altdss.PCElement.PCElementBatch.__len__

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.__len__
```

````

````{py:method} to_json(options: typing.Union[int, dss.enums.DSSJSONFlags] = 0)
:canonical: altdss.PCElement.PCElementBatch.to_json

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.to_json
```

````

````{py:method} to_list()
:canonical: altdss.PCElement.PCElementBatch.to_list

```{autodoc2-docstring} altdss.PCElement.PCElementBatch.to_list
```

````

`````

`````{py:class} PCElementBatchMixin
:canonical: altdss.PCElement.PCElementBatchMixin

```{autodoc2-docstring} altdss.PCElement.PCElementBatchMixin
```

````{py:method} EnergyMeter() -> typing.List[altdss.DSSObj.DSSObj]
:canonical: altdss.PCElement.PCElementBatchMixin.EnergyMeter

```{autodoc2-docstring} altdss.PCElement.PCElementBatchMixin.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> typing.List[str]
:canonical: altdss.PCElement.PCElementBatchMixin.EnergyMeterName

```{autodoc2-docstring} altdss.PCElement.PCElementBatchMixin.EnergyMeterName
```

````

`````

`````{py:class} PCElementMixin
:canonical: altdss.PCElement.PCElementMixin

```{autodoc2-docstring} altdss.PCElement.PCElementMixin
```

````{py:method} EnergyMeter() -> altdss.DSSObj.DSSObj
:canonical: altdss.PCElement.PCElementMixin.EnergyMeter

```{autodoc2-docstring} altdss.PCElement.PCElementMixin.EnergyMeter
```

````

````{py:method} EnergyMeterName() -> str
:canonical: altdss.PCElement.PCElementMixin.EnergyMeterName

```{autodoc2-docstring} altdss.PCElement.PCElementMixin.EnergyMeterName
```

````

````{py:method} GetVariableValue(varIdxName: typing.Union[typing.AnyStr, int]) -> float
:canonical: altdss.PCElement.PCElementMixin.GetVariableValue

```{autodoc2-docstring} altdss.PCElement.PCElementMixin.GetVariableValue
```

````

````{py:method} SetVariableValue(varIdxName: typing.Union[typing.AnyStr, int], value: float)
:canonical: altdss.PCElement.PCElementMixin.SetVariableValue

```{autodoc2-docstring} altdss.PCElement.PCElementMixin.SetVariableValue
```

````

````{py:method} VariableNames() -> typing.List[str]
:canonical: altdss.PCElement.PCElementMixin.VariableNames

```{autodoc2-docstring} altdss.PCElement.PCElementMixin.VariableNames
```

````

````{py:method} VariableValues() -> altdss.types.Float64Array
:canonical: altdss.PCElement.PCElementMixin.VariableValues

```{autodoc2-docstring} altdss.PCElement.PCElementMixin.VariableValues
```

````

````{py:method} VariablesDict() -> typing.Dict[str, float]
:canonical: altdss.PCElement.PCElementMixin.VariablesDict

```{autodoc2-docstring} altdss.PCElement.PCElementMixin.VariablesDict
```

````

`````
