# {py:mod}`altdss.Solution`

```{py:module} altdss.Solution
```

```{autodoc2-docstring} altdss.Solution
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ISolution <altdss.Solution.ISolution>`
  - ```{autodoc2-docstring} altdss.Solution.ISolution
    :summary:
    ```
````

### API

`````{py:class} ISolution(api_util, prefer_lists=False)
:canonical: altdss.Solution.ISolution

Bases: {py:obj}`altdss.common.Base`

```{autodoc2-docstring} altdss.Solution.ISolution
```

````{py:property} AddType
:canonical: altdss.Solution.ISolution.AddType
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.AddType
```

````

````{py:property} Algorithm
:canonical: altdss.Solution.ISolution.Algorithm
:type: dss.enums.SolutionAlgorithms

```{autodoc2-docstring} altdss.Solution.ISolution.Algorithm
```

````

````{py:method} BuildYMatrix(BuildOption: int, AllocateVI: bool)
:canonical: altdss.Solution.ISolution.BuildYMatrix

```{autodoc2-docstring} altdss.Solution.ISolution.BuildYMatrix
```

````

````{py:property} BusLevels
:canonical: altdss.Solution.ISolution.BusLevels
:type: altdss.types.Int32Array

```{autodoc2-docstring} altdss.Solution.ISolution.BusLevels
```

````

````{py:property} Capkvar
:canonical: altdss.Solution.ISolution.Capkvar
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.Capkvar
```

````

````{py:method} CheckControls()
:canonical: altdss.Solution.ISolution.CheckControls

```{autodoc2-docstring} altdss.Solution.ISolution.CheckControls
```

````

````{py:method} CheckFaultStatus()
:canonical: altdss.Solution.ISolution.CheckFaultStatus

```{autodoc2-docstring} altdss.Solution.ISolution.CheckFaultStatus
```

````

````{py:method} Cleanup()
:canonical: altdss.Solution.ISolution.Cleanup

```{autodoc2-docstring} altdss.Solution.ISolution.Cleanup
```

````

````{py:property} ControlActionsDone
:canonical: altdss.Solution.ISolution.ControlActionsDone
:type: bool

```{autodoc2-docstring} altdss.Solution.ISolution.ControlActionsDone
```

````

````{py:property} ControlIterations
:canonical: altdss.Solution.ISolution.ControlIterations
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.ControlIterations
```

````

````{py:property} ControlMode
:canonical: altdss.Solution.ISolution.ControlMode
:type: dss.enums.ControlModes

```{autodoc2-docstring} altdss.Solution.ISolution.ControlMode
```

````

````{py:property} Converged
:canonical: altdss.Solution.ISolution.Converged
:type: bool

```{autodoc2-docstring} altdss.Solution.ISolution.Converged
```

````

````{py:property} DefaultDaily
:canonical: altdss.Solution.ISolution.DefaultDaily
:type: str

```{autodoc2-docstring} altdss.Solution.ISolution.DefaultDaily
```

````

````{py:property} DefaultYearly
:canonical: altdss.Solution.ISolution.DefaultYearly
:type: str

```{autodoc2-docstring} altdss.Solution.ISolution.DefaultYearly
```

````

````{py:method} DoControlActions()
:canonical: altdss.Solution.ISolution.DoControlActions

```{autodoc2-docstring} altdss.Solution.ISolution.DoControlActions
```

````

````{py:property} EventLog
:canonical: altdss.Solution.ISolution.EventLog
:type: typing.List[str]

```{autodoc2-docstring} altdss.Solution.ISolution.EventLog
```

````

````{py:method} FinishTimeStep()
:canonical: altdss.Solution.ISolution.FinishTimeStep

```{autodoc2-docstring} altdss.Solution.ISolution.FinishTimeStep
```

````

````{py:property} Frequency
:canonical: altdss.Solution.ISolution.Frequency
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.Frequency
```

````

````{py:property} GenMult
:canonical: altdss.Solution.ISolution.GenMult
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.GenMult
```

````

````{py:property} GenPF
:canonical: altdss.Solution.ISolution.GenPF
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.GenPF
```

````

````{py:property} GenkW
:canonical: altdss.Solution.ISolution.GenkW
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.GenkW
```

````

````{py:property} Hour
:canonical: altdss.Solution.ISolution.Hour
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.Hour
```

````

````{py:property} IncMatrix
:canonical: altdss.Solution.ISolution.IncMatrix
:type: altdss.types.Int32Array

```{autodoc2-docstring} altdss.Solution.ISolution.IncMatrix
```

````

````{py:property} IncMatrixCols
:canonical: altdss.Solution.ISolution.IncMatrixCols
:type: typing.List[str]

```{autodoc2-docstring} altdss.Solution.ISolution.IncMatrixCols
```

````

````{py:property} IncMatrixRows
:canonical: altdss.Solution.ISolution.IncMatrixRows
:type: typing.List[str]

```{autodoc2-docstring} altdss.Solution.ISolution.IncMatrixRows
```

````

````{py:method} InitSnap()
:canonical: altdss.Solution.ISolution.InitSnap

```{autodoc2-docstring} altdss.Solution.ISolution.InitSnap
```

````

````{py:property} IntervalHrs
:canonical: altdss.Solution.ISolution.IntervalHrs
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.IntervalHrs
```

````

````{py:property} Iterations
:canonical: altdss.Solution.ISolution.Iterations
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.Iterations
```

````

````{py:property} LDCurve
:canonical: altdss.Solution.ISolution.LDCurve
:type: str

```{autodoc2-docstring} altdss.Solution.ISolution.LDCurve
```

````

````{py:property} Laplacian
:canonical: altdss.Solution.ISolution.Laplacian
:type: altdss.types.Int32Array

```{autodoc2-docstring} altdss.Solution.ISolution.Laplacian
```

````

````{py:property} LoadModel
:canonical: altdss.Solution.ISolution.LoadModel
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.LoadModel
```

````

````{py:property} LoadMult
:canonical: altdss.Solution.ISolution.LoadMult
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.LoadMult
```

````

````{py:property} MaxControlIterations
:canonical: altdss.Solution.ISolution.MaxControlIterations
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.MaxControlIterations
```

````

````{py:property} MaxIterations
:canonical: altdss.Solution.ISolution.MaxIterations
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.MaxIterations
```

````

````{py:property} MinIterations
:canonical: altdss.Solution.ISolution.MinIterations
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.MinIterations
```

````

````{py:property} Mode
:canonical: altdss.Solution.ISolution.Mode
:type: dss.enums.SolveModes

```{autodoc2-docstring} altdss.Solution.ISolution.Mode
```

````

````{py:property} Mode_str
:canonical: altdss.Solution.ISolution.Mode_str
:type: str

```{autodoc2-docstring} altdss.Solution.ISolution.Mode_str
```

````

````{py:property} MostIterationsDone
:canonical: altdss.Solution.ISolution.MostIterationsDone
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.MostIterationsDone
```

````

````{py:property} Number
:canonical: altdss.Solution.ISolution.Number
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.Number
```

````

````{py:property} ProcessTime
:canonical: altdss.Solution.ISolution.ProcessTime
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.ProcessTime
```

````

````{py:property} Random
:canonical: altdss.Solution.ISolution.Random
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.Random
```

````

````{py:method} SampleControlDevices()
:canonical: altdss.Solution.ISolution.SampleControlDevices

```{autodoc2-docstring} altdss.Solution.ISolution.SampleControlDevices
```

````

````{py:method} Sample_DoControlActions()
:canonical: altdss.Solution.ISolution.Sample_DoControlActions

```{autodoc2-docstring} altdss.Solution.ISolution.Sample_DoControlActions
```

````

````{py:property} Seconds
:canonical: altdss.Solution.ISolution.Seconds
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.Seconds
```

````

````{py:method} Solve()
:canonical: altdss.Solution.ISolution.Solve

```{autodoc2-docstring} altdss.Solution.ISolution.Solve
```

````

````{py:method} SolveAll()
:canonical: altdss.Solution.ISolution.SolveAll

```{autodoc2-docstring} altdss.Solution.ISolution.SolveAll
```

````

````{py:method} SolveDirect()
:canonical: altdss.Solution.ISolution.SolveDirect

```{autodoc2-docstring} altdss.Solution.ISolution.SolveDirect
```

````

````{py:method} SolveNoControl()
:canonical: altdss.Solution.ISolution.SolveNoControl

```{autodoc2-docstring} altdss.Solution.ISolution.SolveNoControl
```

````

````{py:method} SolvePflow()
:canonical: altdss.Solution.ISolution.SolvePflow

```{autodoc2-docstring} altdss.Solution.ISolution.SolvePflow
```

````

````{py:method} SolvePlusControl()
:canonical: altdss.Solution.ISolution.SolvePlusControl

```{autodoc2-docstring} altdss.Solution.ISolution.SolvePlusControl
```

````

````{py:method} SolveSnap()
:canonical: altdss.Solution.ISolution.SolveSnap

```{autodoc2-docstring} altdss.Solution.ISolution.SolveSnap
```

````

````{py:property} StepSize
:canonical: altdss.Solution.ISolution.StepSize
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.StepSize
```

````

````{py:property} StepsizeHr
:canonical: altdss.Solution.ISolution.StepsizeHr
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.StepsizeHr
```

````

````{py:property} StepsizeMin
:canonical: altdss.Solution.ISolution.StepsizeMin
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.StepsizeMin
```

````

````{py:property} SystemYChanged
:canonical: altdss.Solution.ISolution.SystemYChanged
:type: bool

```{autodoc2-docstring} altdss.Solution.ISolution.SystemYChanged
```

````

````{py:property} TimeOfStep
:canonical: altdss.Solution.ISolution.TimeOfStep
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.TimeOfStep
```

````

````{py:property} Tolerance
:canonical: altdss.Solution.ISolution.Tolerance
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.Tolerance
```

````

````{py:property} TotalIterations
:canonical: altdss.Solution.ISolution.TotalIterations
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.TotalIterations
```

````

````{py:property} TotalTime
:canonical: altdss.Solution.ISolution.TotalTime
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.TotalTime
```

````

````{py:property} Year
:canonical: altdss.Solution.ISolution.Year
:type: int

```{autodoc2-docstring} altdss.Solution.ISolution.Year
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: altdss.Solution.ISolution.__init__

```{autodoc2-docstring} altdss.Solution.ISolution.__init__
```

````

````{py:property} pctGrowth
:canonical: altdss.Solution.ISolution.pctGrowth
:type: float

```{autodoc2-docstring} altdss.Solution.ISolution.pctGrowth
```

````

`````
