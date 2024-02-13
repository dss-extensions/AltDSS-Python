# {py:mod}`altdss.Settings`

```{py:module} altdss.Settings
```

```{autodoc2-docstring} altdss.Settings
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ISettings <altdss.Settings.ISettings>`
  - ```{autodoc2-docstring} altdss.Settings.ISettings
    :summary:
    ```
````

### API

`````{py:class} ISettings(api_util, prefer_lists=False)
:canonical: altdss.Settings.ISettings

Bases: {py:obj}`altdss.common.Base`

```{autodoc2-docstring} altdss.Settings.ISettings
```

````{py:property} AdvancedTypes
:canonical: altdss.Settings.ISettings.AdvancedTypes
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.AdvancedTypes
```

````

````{py:property} AllocationFactors
:canonical: altdss.Settings.ISettings.AllocationFactors

```{autodoc2-docstring} altdss.Settings.ISettings.AllocationFactors
```

````

````{py:property} AllowChangeDir
:canonical: altdss.Settings.ISettings.AllowChangeDir
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.AllowChangeDir
```

````

````{py:property} AllowDOScmd
:canonical: altdss.Settings.ISettings.AllowDOScmd
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.AllowDOScmd
```

````

````{py:property} AllowDuplicates
:canonical: altdss.Settings.ISettings.AllowDuplicates
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.AllowDuplicates
```

````

````{py:property} AllowEditor
:canonical: altdss.Settings.ISettings.AllowEditor
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.AllowEditor
```

````

````{py:property} AllowForms
:canonical: altdss.Settings.ISettings.AllowForms
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.AllowForms
```

````

````{py:property} AutoBusList
:canonical: altdss.Settings.ISettings.AutoBusList
:type: str

```{autodoc2-docstring} altdss.Settings.ISettings.AutoBusList
```

````

````{py:property} COMErrorResults
:canonical: altdss.Settings.ISettings.COMErrorResults
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.COMErrorResults
```

````

````{py:property} CktModel
:canonical: altdss.Settings.ISettings.CktModel
:type: int

```{autodoc2-docstring} altdss.Settings.ISettings.CktModel
```

````

````{py:property} CompatFlags
:canonical: altdss.Settings.ISettings.CompatFlags
:type: int

```{autodoc2-docstring} altdss.Settings.ISettings.CompatFlags
```

````

````{py:property} ControlTrace
:canonical: altdss.Settings.ISettings.ControlTrace
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.ControlTrace
```

````

````{py:property} DataPath
:canonical: altdss.Settings.ISettings.DataPath
:type: str

```{autodoc2-docstring} altdss.Settings.ISettings.DataPath
```

````

````{py:property} DefaultEditor
:canonical: altdss.Settings.ISettings.DefaultEditor
:type: str

```{autodoc2-docstring} altdss.Settings.ISettings.DefaultEditor
```

````

````{py:property} EmergVmaxpu
:canonical: altdss.Settings.ISettings.EmergVmaxpu
:type: float

```{autodoc2-docstring} altdss.Settings.ISettings.EmergVmaxpu
```

````

````{py:property} EmergVminpu
:canonical: altdss.Settings.ISettings.EmergVminpu
:type: float

```{autodoc2-docstring} altdss.Settings.ISettings.EmergVminpu
```

````

````{py:property} IterateDisabled
:canonical: altdss.Settings.ISettings.IterateDisabled
:type: int

```{autodoc2-docstring} altdss.Settings.ISettings.IterateDisabled
```

````

````{py:property} LoadsTerminalCheck
:canonical: altdss.Settings.ISettings.LoadsTerminalCheck
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.LoadsTerminalCheck
```

````

````{py:property} LossRegs
:canonical: altdss.Settings.ISettings.LossRegs
:type: altdss.types.Int32Array

```{autodoc2-docstring} altdss.Settings.ISettings.LossRegs
```

````

````{py:property} LossWeight
:canonical: altdss.Settings.ISettings.LossWeight
:type: float

```{autodoc2-docstring} altdss.Settings.ISettings.LossWeight
```

````

````{py:property} NormVmaxpu
:canonical: altdss.Settings.ISettings.NormVmaxpu
:type: float

```{autodoc2-docstring} altdss.Settings.ISettings.NormVmaxpu
```

````

````{py:property} NormVminpu
:canonical: altdss.Settings.ISettings.NormVminpu
:type: float

```{autodoc2-docstring} altdss.Settings.ISettings.NormVminpu
```

````

````{py:property} PriceCurve
:canonical: altdss.Settings.ISettings.PriceCurve
:type: str

```{autodoc2-docstring} altdss.Settings.ISettings.PriceCurve
```

````

````{py:property} PriceSignal
:canonical: altdss.Settings.ISettings.PriceSignal
:type: float

```{autodoc2-docstring} altdss.Settings.ISettings.PriceSignal
```

````

````{py:method} SetPropertyNameStyle(value: dss.enums.DSSPropertyNameStyle)
:canonical: altdss.Settings.ISettings.SetPropertyNameStyle

```{autodoc2-docstring} altdss.Settings.ISettings.SetPropertyNameStyle
```

````

````{py:property} Trapezoidal
:canonical: altdss.Settings.ISettings.Trapezoidal
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.Trapezoidal
```

````

````{py:property} UEregs
:canonical: altdss.Settings.ISettings.UEregs
:type: altdss.types.Int32Array

```{autodoc2-docstring} altdss.Settings.ISettings.UEregs
```

````

````{py:property} UEweight
:canonical: altdss.Settings.ISettings.UEweight
:type: float

```{autodoc2-docstring} altdss.Settings.ISettings.UEweight
```

````

````{py:property} VoltageBases
:canonical: altdss.Settings.ISettings.VoltageBases
:type: altdss.types.Float64Array

```{autodoc2-docstring} altdss.Settings.ISettings.VoltageBases
```

````

````{py:property} ZoneLock
:canonical: altdss.Settings.ISettings.ZoneLock
:type: bool

```{autodoc2-docstring} altdss.Settings.ISettings.ZoneLock
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: altdss.Settings.ISettings.__init__

```{autodoc2-docstring} altdss.Settings.ISettings.__init__
```

````

`````
