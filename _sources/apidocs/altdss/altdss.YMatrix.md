# {py:mod}`altdss.YMatrix`

```{py:module} altdss.YMatrix
```

```{autodoc2-docstring} altdss.YMatrix
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IYMatrix <altdss.YMatrix.IYMatrix>`
  - ```{autodoc2-docstring} altdss.YMatrix.IYMatrix
    :summary:
    ```
````

### API

`````{py:class} IYMatrix(api_util, prefer_lists=False)
:canonical: altdss.YMatrix.IYMatrix

Bases: {py:obj}`altdss.common.Base`

```{autodoc2-docstring} altdss.YMatrix.IYMatrix
```

````{py:method} AddInAuxCurrents(SType)
:canonical: altdss.YMatrix.IYMatrix.AddInAuxCurrents

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.AddInAuxCurrents
```

````

````{py:method} BuildYMatrixD(BuildOps: int, AllocateVI: bool)
:canonical: altdss.YMatrix.IYMatrix.BuildYMatrixD

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.BuildYMatrixD
```

````

````{py:method} CheckConvergence() -> bool
:canonical: altdss.YMatrix.IYMatrix.CheckConvergence

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.CheckConvergence
```

````

````{py:method} GetCompressedYMatrix(factor: bool = True) -> typing.Tuple[altdss.types.ComplexArray, altdss.types.Int32Array, altdss.types.Int32Array]
:canonical: altdss.YMatrix.IYMatrix.GetCompressedYMatrix

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.GetCompressedYMatrix
```

````

````{py:method} GetIPointer()
:canonical: altdss.YMatrix.IYMatrix.GetIPointer

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.GetIPointer
```

````

````{py:method} GetPCInjCurr()
:canonical: altdss.YMatrix.IYMatrix.GetPCInjCurr

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.GetPCInjCurr
```

````

````{py:method} GetSourceInjCurrents()
:canonical: altdss.YMatrix.IYMatrix.GetSourceInjCurrents

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.GetSourceInjCurrents
```

````

````{py:method} GetVPointer()
:canonical: altdss.YMatrix.IYMatrix.GetVPointer

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.GetVPointer
```

````

````{py:property} Iteration
:canonical: altdss.YMatrix.IYMatrix.Iteration
:type: int

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.Iteration
```

````

````{py:property} LoadsNeedUpdating
:canonical: altdss.YMatrix.IYMatrix.LoadsNeedUpdating
:type: bool

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.LoadsNeedUpdating
```

````

````{py:method} SetGeneratordQdV()
:canonical: altdss.YMatrix.IYMatrix.SetGeneratordQdV

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.SetGeneratordQdV
```

````

````{py:property} SolutionInitialized
:canonical: altdss.YMatrix.IYMatrix.SolutionInitialized
:type: bool

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.SolutionInitialized
```

````

````{py:method} SolveSystem(NodeV=None) -> int
:canonical: altdss.YMatrix.IYMatrix.SolveSystem

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.SolveSystem
```

````

````{py:property} SolverOptions
:canonical: altdss.YMatrix.IYMatrix.SolverOptions
:type: int

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.SolverOptions
```

````

````{py:property} SystemYChanged
:canonical: altdss.YMatrix.IYMatrix.SystemYChanged
:type: bool

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.SystemYChanged
```

````

````{py:property} UseAuxCurrents
:canonical: altdss.YMatrix.IYMatrix.UseAuxCurrents
:type: bool

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.UseAuxCurrents
```

````

````{py:method} ZeroInjCurr()
:canonical: altdss.YMatrix.IYMatrix.ZeroInjCurr

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.ZeroInjCurr
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: altdss.YMatrix.IYMatrix.__init__

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.__init__
```

````

````{py:method} getI() -> typing.List[float]
:canonical: altdss.YMatrix.IYMatrix.getI

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.getI
```

````

````{py:method} getV() -> typing.List[float]
:canonical: altdss.YMatrix.IYMatrix.getV

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.getV
```

````

````{py:attribute} getYSparse
:canonical: altdss.YMatrix.IYMatrix.getYSparse
:value: >
   None

```{autodoc2-docstring} altdss.YMatrix.IYMatrix.getYSparse
```

````

`````
