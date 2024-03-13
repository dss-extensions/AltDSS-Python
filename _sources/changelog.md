# AltDSS-Python changelog

Remember that changes in our alternative OpenDSS engine, currently known as AltDSS/DSS C-API, are always
relevant. See [AltDSS/DSS C-API's repository](https://github.com/dss-extensions/dss_capi/) for more information.

## 0.2.2

This release includes a lot more tests, reaching 100% coverage of the *Python* code of several important modules, considering both the public and private tests. The engine was updated to AltDSS/DSS C-API 0.14.3 to include a couple of new features and fixes found during the tests.

- SystemY: in `AltDSS.SystemY`, return the matrix as a SciPy sparse matrix directly.
- BusBatch: Add missing `Name` function (the bus names were already exposed in the individual objects and at circuit level in `AltDSS.BusNames`).
- Batch, creation function `.batch(...)`:
    - Fix by list of indices (`...batch(idx=[0,1,10]`)
    - Add some basic type checks 
    - Add support for selecting items by float property (`...batch(kW=0)` or `...batch(kV=[0.0, 1.0])`)
    - Add support for filtering multiple properties (`...batch(Phases=2, kV=[0.0, 1.0])`), and filtering existing batches.
- CircuitElement/CircuitElementBatch: Complement doc strings; fix some type hints.
- CircuitElementBatch: 
    - Fix `MaxCurrent`. This will require the backend to be updated to v0.14.3.
    - Implement `OCPDevice`
- NonUniformBatch: allow `batch[idx]` to get a single element by index.
- Setters: 
    - Allow using `None` to clear object references (e.g. `altdss.Load[0].Daily = None`)
    - Allow using list of live objects to fill a property that represents a DSS object.
- ArrayProxy: 
    - Fix `BatchFloat64ArrayProxy.to_list()`. It was returning an array instead a list.
    - Accepts lists for in-place sub, e.g. `arrayProxy -= [1.1, 1.4]` now works as expected.
    - Use new low-level operations for in-place operations with array values

## 0.2.1

- Meter/Generator/etc.: Remove the previous workaround for issue with the AltDSS/DSS C-API headers related to `RegisterValues` -- now working without it. Add test.

## 0.2.0

Version incremented to 0.2.0 due to the number of changes in the function/property names. The engine is also updated to AltDSS/DSS C-API 0.14.2.

- PDElement: 
    - Fix `ParentPDElement`
    - Fix and update names:
        - `pctNorm` to `pctNormal`
        - `pctEmerg` to `pctEmergency`
    - Batch: add `pctNormal` and `pctEmergency`
    - Add/complement docstrings

- Bus class: 
    - Fix errors in `ZSC0`, `ZSC1`, `Voltages`
    - Batch: fix `len(bus_batch)`
    - Fix element batches (PCElements, PDElements)
    - Tweak tracking when buses are redefined but there are still live objects
    - Complement docstrings
    - Update names of several items:
        - `Voc` to `VOC`
        - `Isc` to `ISC`
        - `YscMatrix` to `YSC`
        - `ZscMatrix` to `ZSC`
        - `Zsc012Matrix` to `ZSC012`
        - `Zsc0` to `ZSC0`
        - `Zsc1` to `ZSC1`
        - `ZscRefresh` to `ZSCRefresh`

- AltDSS (main class): adjust capitalization of a few items:
    - `NodeVmagByPhase` to `NodeVMagByPhase`
    - `NodeVmagPUByPhase` to `NodeVMagPUByPhase`
    - `BusVmag` to `BusVMag`
    - `BusVmagPu` to `BusVMagPU`


## 0.1.3

- Meter/Generator/etc.: Add workaround for issue with the AltDSS/DSS C-API headers related to `RegisterValues`.
- Monitor: fix issue with `Channel` returning the whole data instead of the channel data.

## 0.1.2

- Fix `SetterFlags`: import from backend instead of defining a new enum here.
- Batch:
    - Implement `__slots__` to constrain the attributes and avoid accidental names.
    - `EnergyMeter.Loads`: make it a function to avoid issues with uninitialized meters (such as new meters).
    - Minor quality of life changes, such as returning zero instead of error for some empty batches.

- Known issue: reading `pctEmerg` or `pctNorm` for uninitialized PDElements (missing solution for the circuit) will crash. This is already fixed in the engine and will be included in the next backend update.


## 0.1.1

- Batch: fix setter for single object
- Line: adjust Conductors to allow any conductor data object (WireData, CNData, TSData).
- LineGeometry: rename "Wire" to "Conductors", follow the changes in Line.
- Depend on DSS-Python 0.15.2 for the updated backend.
- Add tests to ensure the following issues don't happen again:
    - Bus: Fix typo in `puVMagAngle` (rename it from `puVmagAngle`), and `Voc`.
    - Meters: Fix typo in call to `DoReliabilityCalc`
    - Circuit: Fix typo in `NumCircuitElements`
    - PCE: Found a function not implemented in the engine. Fixed there.

## 0.1.0

First version. Still depends on DSS-Python for the backend, but otherwise can be used for a lot of common operations by itself.

Highlights compared to the previous Obj API on DSS-Python:

- The method `find()` (and `__getitem__`) now assume 0-based numeric indices. This is more appropriate to Python, e.g. `altdss.Load[0]` now returns the first load.
- Besides the previous DSS property functions, new API methods to allow extracting data and manipulating objects through generalized versions of the classic (COM-like) API.
- Introduce extra batch types for special classes
- Introduce non-uniform batches
- Introduce dynamic batches, avoiding redundant copies
- Special handling of EnergyMeter and MeterSections
- Object lifetime: implement synchronization of circuit state and pointers, invalidating dead pointer instead of crashing


 ## 0.0.1

 Published to PyPI to reserve the name.
