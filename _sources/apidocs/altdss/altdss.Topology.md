# {py:mod}`altdss.Topology`

```{py:module} altdss.Topology
```

```{autodoc2-docstring} altdss.Topology
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ITopology <altdss.Topology.ITopology>`
  - ```{autodoc2-docstring} altdss.Topology.ITopology
    :summary:
    ```
````

### API

`````{py:class} ITopology(api_util, prefer_lists=False)
:canonical: altdss.Topology.ITopology

Bases: {py:obj}`altdss.common.Base`

```{autodoc2-docstring} altdss.Topology.ITopology
```

````{py:property} ActiveBranch
:canonical: altdss.Topology.ITopology.ActiveBranch
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.ActiveBranch
```

````

````{py:property} ActiveLevel
:canonical: altdss.Topology.ITopology.ActiveLevel
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.ActiveLevel
```

````

````{py:property} AllIsolatedBranches
:canonical: altdss.Topology.ITopology.AllIsolatedBranches
:type: typing.List[str]

```{autodoc2-docstring} altdss.Topology.ITopology.AllIsolatedBranches
```

````

````{py:property} AllIsolatedLoads
:canonical: altdss.Topology.ITopology.AllIsolatedLoads
:type: typing.List[str]

```{autodoc2-docstring} altdss.Topology.ITopology.AllIsolatedLoads
```

````

````{py:property} AllLoopedPairs
:canonical: altdss.Topology.ITopology.AllLoopedPairs
:type: typing.List[str]

```{autodoc2-docstring} altdss.Topology.ITopology.AllLoopedPairs
```

````

````{py:property} BackwardBranch
:canonical: altdss.Topology.ITopology.BackwardBranch
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.BackwardBranch
```

````

````{py:property} BranchName
:canonical: altdss.Topology.ITopology.BranchName
:type: str

```{autodoc2-docstring} altdss.Topology.ITopology.BranchName
```

````

````{py:property} BusName
:canonical: altdss.Topology.ITopology.BusName
:type: str

```{autodoc2-docstring} altdss.Topology.ITopology.BusName
```

````

````{py:property} First
:canonical: altdss.Topology.ITopology.First
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.First
```

````

````{py:property} FirstLoad
:canonical: altdss.Topology.ITopology.FirstLoad
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.FirstLoad
```

````

````{py:property} ForwardBranch
:canonical: altdss.Topology.ITopology.ForwardBranch
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.ForwardBranch
```

````

````{py:property} LoopedBranch
:canonical: altdss.Topology.ITopology.LoopedBranch
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.LoopedBranch
```

````

````{py:property} Next
:canonical: altdss.Topology.ITopology.Next
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.Next
```

````

````{py:property} NextLoad
:canonical: altdss.Topology.ITopology.NextLoad
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.NextLoad
```

````

````{py:property} NumIsolatedBranches
:canonical: altdss.Topology.ITopology.NumIsolatedBranches
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.NumIsolatedBranches
```

````

````{py:property} NumIsolatedLoads
:canonical: altdss.Topology.ITopology.NumIsolatedLoads
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.NumIsolatedLoads
```

````

````{py:property} NumLoops
:canonical: altdss.Topology.ITopology.NumLoops
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.NumLoops
```

````

````{py:property} ParallelBranch
:canonical: altdss.Topology.ITopology.ParallelBranch
:type: int

```{autodoc2-docstring} altdss.Topology.ITopology.ParallelBranch
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: altdss.Topology.ITopology.__init__

```{autodoc2-docstring} altdss.Topology.ITopology.__init__
```

````

`````
