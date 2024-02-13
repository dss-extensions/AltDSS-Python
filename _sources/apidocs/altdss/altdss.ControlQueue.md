# {py:mod}`altdss.ControlQueue`

```{py:module} altdss.ControlQueue
```

```{autodoc2-docstring} altdss.ControlQueue
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`IControlQueue <altdss.ControlQueue.IControlQueue>`
  - ```{autodoc2-docstring} altdss.ControlQueue.IControlQueue
    :summary:
    ```
````

### API

`````{py:class} IControlQueue(api_util, prefer_lists=False)
:canonical: altdss.ControlQueue.IControlQueue

Bases: {py:obj}`altdss.common.Base`

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue
```

````{py:property} ActionCode
:canonical: altdss.ControlQueue.IControlQueue.ActionCode
:type: int

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.ActionCode
```

````

````{py:method} ClearActions()
:canonical: altdss.ControlQueue.IControlQueue.ClearActions

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.ClearActions
```

````

````{py:method} ClearQueue()
:canonical: altdss.ControlQueue.IControlQueue.ClearQueue

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.ClearQueue
```

````

````{py:method} Delete(ActionHandle)
:canonical: altdss.ControlQueue.IControlQueue.Delete

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.Delete
```

````

````{py:property} DeviceHandle
:canonical: altdss.ControlQueue.IControlQueue.DeviceHandle
:type: int

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.DeviceHandle
```

````

````{py:method} DoAllQueue()
:canonical: altdss.ControlQueue.IControlQueue.DoAllQueue

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.DoAllQueue
```

````

````{py:property} NumActions
:canonical: altdss.ControlQueue.IControlQueue.NumActions
:type: int

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.NumActions
```

````

````{py:property} PopAction
:canonical: altdss.ControlQueue.IControlQueue.PopAction
:type: int

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.PopAction
```

````

````{py:method} Push(Hour: int, Seconds: float, ActionCode: int, DeviceHandle: int)
:canonical: altdss.ControlQueue.IControlQueue.Push

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.Push
```

````

````{py:property} Queue
:canonical: altdss.ControlQueue.IControlQueue.Queue
:type: typing.List[str]

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.Queue
```

````

````{py:property} QueueSize
:canonical: altdss.ControlQueue.IControlQueue.QueueSize
:type: int

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.QueueSize
```

````

````{py:method} SetAction(index: int)
:canonical: altdss.ControlQueue.IControlQueue.SetAction

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.SetAction
```

````

````{py:method} Show()
:canonical: altdss.ControlQueue.IControlQueue.Show

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.Show
```

````

````{py:method} __init__(api_util, prefer_lists=False)
:canonical: altdss.ControlQueue.IControlQueue.__init__

```{autodoc2-docstring} altdss.ControlQueue.IControlQueue.__init__
```

````

`````
