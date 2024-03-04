# AltDSS-Python changelog

Remember that changes in our alternative OpenDSS engine, currently known as AltDSS/DSS C-API, are always
relevant. See [DSS C-API's repository](https://github.com/dss-extensions/dss_capi/) for more information.

## 0.2.2

- CircuitElementBatch: fix `MaxCurrent`. This will require the backend to be updated to v0.14.3.

## 0.2.1

- Meter/Generator/etc.: Remove the previous workaround for issue with the DSS C-API headers related to `RegisterValues` -- now working without it. Add test.

## 0.2.0

Version incremented to 0.2.0 due to the number of changes in the function/property names. The engine is also updated to DSS C-API 0.14.2.

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

- Meter/Generator/etc.: Add workaround for issue with the DSS C-API headers related to `RegisterValues`.
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
