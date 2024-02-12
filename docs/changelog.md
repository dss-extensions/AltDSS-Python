# AltDSS-Python changelog

Remember that changes in our alternative OpenDSS engine, currently known as AltDSS/DSS C-API, are always
relevant. See [DSS C-API's repository](https://github.com/dss-extensions/dss_capi/) for more information.


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
