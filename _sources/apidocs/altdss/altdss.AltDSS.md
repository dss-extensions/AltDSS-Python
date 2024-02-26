# {py:mod}`altdss.AltDSS`

```{py:module} altdss.AltDSS
```

```{autodoc2-docstring} altdss.AltDSS
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AltDSS <altdss.AltDSS.AltDSS>`
  - ```{autodoc2-docstring} altdss.AltDSS.AltDSS
    :summary:
    ```
````

### API

`````{py:class} AltDSS(api_util)
:canonical: altdss.AltDSS.AltDSS

Bases: {py:obj}`altdss.Obj.IObj`

```{autodoc2-docstring} altdss.AltDSS.AltDSS
```

````{py:attribute} AutoTrans
:canonical: altdss.AltDSS.AltDSS.AutoTrans
:type: altdss.AutoTrans.IAutoTrans
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.AutoTrans
```

````

````{py:attribute} Bus
:canonical: altdss.AltDSS.AltDSS.Bus
:type: altdss.Bus.IBuses
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Bus
```

````

````{py:method} BusDistances() -> altdss.types.Float64Array
:canonical: altdss.AltDSS.AltDSS.BusDistances

```{autodoc2-docstring} altdss.AltDSS.AltDSS.BusDistances
```

````

````{py:method} BusNames() -> typing.List[str]
:canonical: altdss.AltDSS.AltDSS.BusNames

```{autodoc2-docstring} altdss.AltDSS.AltDSS.BusNames
```

````

````{py:method} BusVMag() -> altdss.types.Float64Array
:canonical: altdss.AltDSS.AltDSS.BusVMag

```{autodoc2-docstring} altdss.AltDSS.AltDSS.BusVMag
```

````

````{py:method} BusVMagPU() -> altdss.types.Float64Array
:canonical: altdss.AltDSS.AltDSS.BusVMagPU

```{autodoc2-docstring} altdss.AltDSS.AltDSS.BusVMagPU
```

````

````{py:method} BusVolts() -> altdss.types.ComplexArray
:canonical: altdss.AltDSS.AltDSS.BusVolts

```{autodoc2-docstring} altdss.AltDSS.AltDSS.BusVolts
```

````

````{py:attribute} CNData
:canonical: altdss.AltDSS.AltDSS.CNData
:type: altdss.CNData.ICNData
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.CNData
```

````

````{py:attribute} CapControl
:canonical: altdss.AltDSS.AltDSS.CapControl
:type: altdss.CapControl.ICapControl
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.CapControl
```

````

````{py:attribute} Capacitor
:canonical: altdss.AltDSS.AltDSS.Capacitor
:type: altdss.Capacitor.ICapacitor
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Capacitor
```

````

````{py:method} Capacity(Start: float, Increment: float) -> float
:canonical: altdss.AltDSS.AltDSS.Capacity

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Capacity
```

````

````{py:method} Clear()
:canonical: altdss.AltDSS.AltDSS.Clear

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Clear
```

````

````{py:method} ClearAll()
:canonical: altdss.AltDSS.AltDSS.ClearAll

```{autodoc2-docstring} altdss.AltDSS.AltDSS.ClearAll
```

````

````{py:method} Command(value: typing.Optional[typing.AnyStr]) -> typing.Optional[str]
:canonical: altdss.AltDSS.AltDSS.Command

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Command
```

````

````{py:method} Commands(Value: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]])
:canonical: altdss.AltDSS.AltDSS.Commands

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Commands
```

````

````{py:attribute} ControlQueue
:canonical: altdss.AltDSS.AltDSS.ControlQueue
:type: altdss.ControlQueue.IControlQueue
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.ControlQueue
```

````

````{py:method} DisableElement(name: typing.AnyStr)
:canonical: altdss.AltDSS.AltDSS.DisableElement

```{autodoc2-docstring} altdss.AltDSS.AltDSS.DisableElement
```

````

````{py:attribute} DynamicExp
:canonical: altdss.AltDSS.AltDSS.DynamicExp
:type: altdss.DynamicExp.IDynamicExp
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.DynamicExp
```

````

````{py:attribute} ESPVLControl
:canonical: altdss.AltDSS.AltDSS.ESPVLControl
:type: altdss.ESPVLControl.IESPVLControl
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.ESPVLControl
```

````

````{py:attribute} Element
:canonical: altdss.AltDSS.AltDSS.Element
:type: altdss.CircuitElement.CircuitElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Element
```

````

````{py:method} EnableElement(name: typing.AnyStr)
:canonical: altdss.AltDSS.AltDSS.EnableElement

```{autodoc2-docstring} altdss.AltDSS.AltDSS.EnableElement
```

````

````{py:attribute} EnergyMeter
:canonical: altdss.AltDSS.AltDSS.EnergyMeter
:type: altdss.EnergyMeter.IEnergyMeter
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.EnergyMeter
```

````

````{py:attribute} Error
:canonical: altdss.AltDSS.AltDSS.Error
:type: altdss.Error.IError
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Error
```

````

````{py:attribute} ExpControl
:canonical: altdss.AltDSS.AltDSS.ExpControl
:type: altdss.ExpControl.IExpControl
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.ExpControl
```

````

````{py:attribute} Fault
:canonical: altdss.AltDSS.AltDSS.Fault
:type: altdss.Fault.IFault
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Fault
```

````

````{py:attribute} Fuse
:canonical: altdss.AltDSS.AltDSS.Fuse
:type: altdss.Fuse.IFuse
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Fuse
```

````

````{py:attribute} GICLine
:canonical: altdss.AltDSS.AltDSS.GICLine
:type: altdss.GICLine.IGICLine
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.GICLine
```

````

````{py:attribute} GICTransformer
:canonical: altdss.AltDSS.AltDSS.GICTransformer
:type: altdss.GICTransformer.IGICTransformer
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.GICTransformer
```

````

````{py:attribute} GICsource
:canonical: altdss.AltDSS.AltDSS.GICsource
:type: altdss.GICsource.IGICsource
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.GICsource
```

````

````{py:attribute} GenDispatcher
:canonical: altdss.AltDSS.AltDSS.GenDispatcher
:type: altdss.GenDispatcher.IGenDispatcher
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.GenDispatcher
```

````

````{py:attribute} Generator
:canonical: altdss.AltDSS.AltDSS.Generator
:type: altdss.Generator.IGenerator
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Generator
```

````

````{py:attribute} GrowthShape
:canonical: altdss.AltDSS.AltDSS.GrowthShape
:type: altdss.GrowthShape.IGrowthShape
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.GrowthShape
```

````

````{py:attribute} IndMach012
:canonical: altdss.AltDSS.AltDSS.IndMach012
:type: altdss.IndMach012.IIndMach012
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.IndMach012
```

````

````{py:attribute} InvControl
:canonical: altdss.AltDSS.AltDSS.InvControl
:type: altdss.InvControl.IInvControl
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.InvControl
```

````

````{py:attribute} Isource
:canonical: altdss.AltDSS.AltDSS.Isource
:type: altdss.Isource.IIsource
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Isource
```

````

````{py:attribute} Line
:canonical: altdss.AltDSS.AltDSS.Line
:type: altdss.Line.ILine
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Line
```

````

````{py:attribute} LineCode
:canonical: altdss.AltDSS.AltDSS.LineCode
:type: altdss.LineCode.ILineCode
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.LineCode
```

````

````{py:attribute} LineGeometry
:canonical: altdss.AltDSS.AltDSS.LineGeometry
:type: altdss.LineGeometry.ILineGeometry
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.LineGeometry
```

````

````{py:method} LineLosses() -> complex
:canonical: altdss.AltDSS.AltDSS.LineLosses

```{autodoc2-docstring} altdss.AltDSS.AltDSS.LineLosses
```

````

````{py:attribute} LineSpacing
:canonical: altdss.AltDSS.AltDSS.LineSpacing
:type: altdss.LineSpacing.ILineSpacing
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.LineSpacing
```

````

````{py:attribute} Load
:canonical: altdss.AltDSS.AltDSS.Load
:type: altdss.Load.ILoad
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Load
```

````

````{py:attribute} LoadShape
:canonical: altdss.AltDSS.AltDSS.LoadShape
:type: altdss.LoadShape.ILoadShape
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.LoadShape
```

````

````{py:method} Losses() -> complex
:canonical: altdss.AltDSS.AltDSS.Losses

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Losses
```

````

````{py:attribute} Monitor
:canonical: altdss.AltDSS.AltDSS.Monitor
:type: altdss.Monitor.IMonitor
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Monitor
```

````

````{py:property} Name
:canonical: altdss.AltDSS.AltDSS.Name
:type: str

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Name
```

````

````{py:method} NewContext() -> altdss.AltDSS.AltDSS
:canonical: altdss.AltDSS.AltDSS.NewContext

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NewContext
```

````

````{py:method} NodeDistances() -> altdss.types.Float64Array
:canonical: altdss.AltDSS.AltDSS.NodeDistances

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NodeDistances
```

````

````{py:method} NodeDistancesByPhase(Phase: int) -> altdss.types.Float64Array
:canonical: altdss.AltDSS.AltDSS.NodeDistancesByPhase

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NodeDistancesByPhase
```

````

````{py:method} NodeNames() -> typing.List[str]
:canonical: altdss.AltDSS.AltDSS.NodeNames

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NodeNames
```

````

````{py:method} NodeNamesByPhase(Phase: int) -> typing.List[str]
:canonical: altdss.AltDSS.AltDSS.NodeNamesByPhase

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NodeNamesByPhase
```

````

````{py:method} NodeVMagByPhase(Phase: int) -> altdss.types.Float64Array
:canonical: altdss.AltDSS.AltDSS.NodeVMagByPhase

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NodeVMagByPhase
```

````

````{py:method} NodeVMagPUByPhase(Phase: int) -> altdss.types.Float64Array
:canonical: altdss.AltDSS.AltDSS.NodeVMagPUByPhase

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NodeVMagPUByPhase
```

````

````{py:property} NumBuses
:canonical: altdss.AltDSS.AltDSS.NumBuses
:type: int

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NumBuses
```

````

````{py:property} NumCircuitElements
:canonical: altdss.AltDSS.AltDSS.NumCircuitElements
:type: int

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NumCircuitElements
```

````

````{py:property} NumNodes
:canonical: altdss.AltDSS.AltDSS.NumNodes
:type: int

```{autodoc2-docstring} altdss.AltDSS.AltDSS.NumNodes
```

````

````{py:attribute} PCElement
:canonical: altdss.AltDSS.AltDSS.PCElement
:type: altdss.PCElement.PCElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.PCElement
```

````

````{py:attribute} PDElement
:canonical: altdss.AltDSS.AltDSS.PDElement
:type: altdss.PDElement.PDElementBatch
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.PDElement
```

````

````{py:attribute} PVSystem
:canonical: altdss.AltDSS.AltDSS.PVSystem
:type: altdss.PVSystem.IPVSystem
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.PVSystem
```

````

````{py:attribute} PriceShape
:canonical: altdss.AltDSS.AltDSS.PriceShape
:type: altdss.PriceShape.IPriceShape
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.PriceShape
```

````

````{py:attribute} Reactor
:canonical: altdss.AltDSS.AltDSS.Reactor
:type: altdss.Reactor.IReactor
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Reactor
```

````

````{py:attribute} Recloser
:canonical: altdss.AltDSS.AltDSS.Recloser
:type: altdss.Recloser.IRecloser
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Recloser
```

````

````{py:attribute} ReduceCircuit
:canonical: altdss.AltDSS.AltDSS.ReduceCircuit
:type: altdss.ReduceCkt.IReduceCkt
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.ReduceCircuit
```

````

````{py:attribute} RegControl
:canonical: altdss.AltDSS.AltDSS.RegControl
:type: altdss.RegControl.IRegControl
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.RegControl
```

````

````{py:attribute} Relay
:canonical: altdss.AltDSS.AltDSS.Relay
:type: altdss.Relay.IRelay
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Relay
```

````

````{py:method} SaveSample()
:canonical: altdss.AltDSS.AltDSS.SaveSample

```{autodoc2-docstring} altdss.AltDSS.AltDSS.SaveSample
```

````

````{py:attribute} Sensor
:canonical: altdss.AltDSS.AltDSS.Sensor
:type: altdss.Sensor.ISensor
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Sensor
```

````

````{py:attribute} Settings
:canonical: altdss.AltDSS.AltDSS.Settings
:type: altdss.Settings.ISettings
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Settings
```

````

````{py:attribute} Solution
:canonical: altdss.AltDSS.AltDSS.Solution
:type: altdss.Solution.ISolution
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Solution
```

````

````{py:attribute} Spectrum
:canonical: altdss.AltDSS.AltDSS.Spectrum
:type: altdss.Spectrum.ISpectrum
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Spectrum
```

````

````{py:attribute} Storage
:canonical: altdss.AltDSS.AltDSS.Storage
:type: altdss.Storage.IStorage
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Storage
```

````

````{py:attribute} StorageController
:canonical: altdss.AltDSS.AltDSS.StorageController
:type: altdss.StorageController.IStorageController
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.StorageController
```

````

````{py:property} SubstationLosses
:canonical: altdss.AltDSS.AltDSS.SubstationLosses
:type: complex

```{autodoc2-docstring} altdss.AltDSS.AltDSS.SubstationLosses
```

````

````{py:attribute} SwtControl
:canonical: altdss.AltDSS.AltDSS.SwtControl
:type: altdss.SwtControl.ISwtControl
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.SwtControl
```

````

````{py:method} SystemY(dense=False) -> altdss.types.ComplexArray
:canonical: altdss.AltDSS.AltDSS.SystemY

```{autodoc2-docstring} altdss.AltDSS.AltDSS.SystemY
```

````

````{py:attribute} TCC_Curve
:canonical: altdss.AltDSS.AltDSS.TCC_Curve
:type: altdss.TCC_Curve.ITCC_Curve
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.TCC_Curve
```

````

````{py:attribute} TSData
:canonical: altdss.AltDSS.AltDSS.TSData
:type: altdss.TSData.ITSData
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.TSData
```

````

````{py:attribute} TShape
:canonical: altdss.AltDSS.AltDSS.TShape
:type: altdss.TShape.ITShape
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.TShape
```

````

````{py:method} TakeSample()
:canonical: altdss.AltDSS.AltDSS.TakeSample

```{autodoc2-docstring} altdss.AltDSS.AltDSS.TakeSample
```

````

````{py:property} TextResult
:canonical: altdss.AltDSS.AltDSS.TextResult
:type: str

```{autodoc2-docstring} altdss.AltDSS.AltDSS.TextResult
```

````

````{py:attribute} Topology
:canonical: altdss.AltDSS.AltDSS.Topology
:type: altdss.Topology.ITopology
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Topology
```

````

````{py:method} TotalPower() -> complex
:canonical: altdss.AltDSS.AltDSS.TotalPower

```{autodoc2-docstring} altdss.AltDSS.AltDSS.TotalPower
```

````

````{py:attribute} Transformer
:canonical: altdss.AltDSS.AltDSS.Transformer
:type: altdss.Transformer.ITransformer
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Transformer
```

````

````{py:attribute} UPFC
:canonical: altdss.AltDSS.AltDSS.UPFC
:type: altdss.UPFC.IUPFC
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.UPFC
```

````

````{py:attribute} UPFCControl
:canonical: altdss.AltDSS.AltDSS.UPFCControl
:type: altdss.UPFCControl.IUPFCControl
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.UPFCControl
```

````

````{py:method} UpdateStorage()
:canonical: altdss.AltDSS.AltDSS.UpdateStorage

```{autodoc2-docstring} altdss.AltDSS.AltDSS.UpdateStorage
```

````

````{py:attribute} VCCS
:canonical: altdss.AltDSS.AltDSS.VCCS
:type: altdss.VCCS.IVCCS
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.VCCS
```

````

````{py:attribute} VSConverter
:canonical: altdss.AltDSS.AltDSS.VSConverter
:type: altdss.VSConverter.IVSConverter
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.VSConverter
```

````

````{py:method} Version() -> str
:canonical: altdss.AltDSS.AltDSS.Version

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Version
```

````

````{py:attribute} Vsource
:canonical: altdss.AltDSS.AltDSS.Vsource
:type: altdss.Vsource.IVsource
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.Vsource
```

````

````{py:attribute} WireData
:canonical: altdss.AltDSS.AltDSS.WireData
:type: altdss.WireData.IWireData
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.WireData
```

````

````{py:attribute} XYcurve
:canonical: altdss.AltDSS.AltDSS.XYcurve
:type: altdss.XYcurve.IXYcurve
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.XYcurve
```

````

````{py:attribute} XfmrCode
:canonical: altdss.AltDSS.AltDSS.XfmrCode
:type: altdss.XfmrCode.IXfmrCode
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.XfmrCode
```

````

````{py:method} YCurrents() -> altdss.types.ComplexArray
:canonical: altdss.AltDSS.AltDSS.YCurrents

```{autodoc2-docstring} altdss.AltDSS.AltDSS.YCurrents
```

````

````{py:attribute} YMatrix
:canonical: altdss.AltDSS.AltDSS.YMatrix
:type: altdss.YMatrix.IYMatrix
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.YMatrix
```

````

````{py:method} YNodeOrder() -> typing.List[str]
:canonical: altdss.AltDSS.AltDSS.YNodeOrder

```{autodoc2-docstring} altdss.AltDSS.AltDSS.YNodeOrder
```

````

````{py:method} YNodeVarray() -> altdss.types.ComplexArray
:canonical: altdss.AltDSS.AltDSS.YNodeVarray

```{autodoc2-docstring} altdss.AltDSS.AltDSS.YNodeVarray
```

````

````{py:attribute} ZIP
:canonical: altdss.AltDSS.AltDSS.ZIP
:type: altdss.ZIP.IZIP
:value: >
   None

```{autodoc2-docstring} altdss.AltDSS.AltDSS.ZIP
```

````

````{py:method} __call__(cmds: typing.Union[typing.AnyStr, typing.List[typing.AnyStr]])
:canonical: altdss.AltDSS.AltDSS.__call__

```{autodoc2-docstring} altdss.AltDSS.AltDSS.__call__
```

````

````{py:method} __init__(api_util)
:canonical: altdss.AltDSS.AltDSS.__init__

```{autodoc2-docstring} altdss.AltDSS.AltDSS.__init__
```

````

````{py:method} to_dss_python() -> dss.IDSS
:canonical: altdss.AltDSS.AltDSS.to_dss_python

```{autodoc2-docstring} altdss.AltDSS.AltDSS.to_dss_python
```

````

````{py:method} to_json(options: dss.enums.DSSJSONFlags = 0) -> str
:canonical: altdss.AltDSS.AltDSS.to_json

```{autodoc2-docstring} altdss.AltDSS.AltDSS.to_json
```

````

````{py:method} to_opendssdirect() -> opendssdirect.OpenDSSDirect.OpenDSSDirect
:canonical: altdss.AltDSS.AltDSS.to_opendssdirect

```{autodoc2-docstring} altdss.AltDSS.AltDSS.to_opendssdirect
```

````

`````
