# Architecture details

Any DSS object can be manipulated in Python without using the Text or Properties API, plus there are new APIs to complement some aspects of the classic.

## Object lifetime

The Python objects live while the parent circuit is still loaded.

That is, it is safe to keep a Python object reference a `Load` right after the circuit is initially loaded until the circuit is cleared. It doesn't matter if the circuit, the load, or other objects are modified in the interim, the reference is still be valid.

After the circuit is cleared, the DSS object doesn't exist anymore and the Python object is invalid. Since AltDSS observes the circuit for events such as the `clear` command, trying to access the properties of the DSS object, which no longer exists, through a Python object will result in an error. The error message should mention `InvalidatedObject` somewhere in the traceback message. `InvalidatedObject` is an instance used to tag the Python objects that lost their engine-level objects in a nice way instead of leaving all the burden of keeping only valid objects to the user and just plainly killing the Python process on invalid accesses.

This automatic lifetime management is done for plain DSS objects, batches of objects.

### Buses

Most of the object lifetime rules also applies to buses, with the caveat that buses can change during the circuit lifetime, being added or removed according to the present and enabled circuit elements. It a bus is removed, or the circuit disposed, the bus object is invalidated.

## Batches

Batches of DSS objects and buses generalize some aspects of the API to get or set values in bulk.

### Array proxies

Array proxies provide an efficient way to manipulate `float` or `int` properties of a batch. Common operations are pushed down to the engine, avoiding Python loops when possible.
