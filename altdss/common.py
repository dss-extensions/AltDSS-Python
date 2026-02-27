from dss._cffi_api_util import DSSException, Base as SimpleBase, AltDSSAPIUtil

try:
    import pandas as pd
    LIST_LIKE = (pd.Series, list, tuple)
except ModuleNotFoundError:
    LIST_LIKE = (list, tuple)


class Base(SimpleBase):
    __slots__ = [
        '_get_float64_array',
        '_get_float64_gr_array',
        '_get_int32_array',
        '_get_int32_gr_array',
        '_get_int8_array',
        '_get_int8_gr_array',
        '_get_string_array',
        '_get_complex128_array',
        '_get_complex128_simple',
        '_get_fcomplex128_simple',
        '_get_complex128_gr_array',
        '_get_complex128_gr_simple',
        '_get_fcomplex128_gr_array',
        '_get_fcomplex128_array',
        '_get_fcomplex128_gr_simple',
        '_get_string',
    ]

    def __init__(self, api_util):
        SimpleBase.__init__(self, api_util)

        # Moved from the old DSS-Python _cffi_api_util, until 
        # we rework AltDSS-Python to use FastDSS.
        lib = self._lib

        self._get_fcomplex128_gr_array = lib.get_fcomplex128_gr_array
        self._get_fcomplex128_array = lib.get_fcomplex128_array
        self._get_fcomplex128_simple = lib.get_fcomplex128_simple
        self._get_fcomplex128_gr_simple = lib.get_fcomplex128_gr_simple
        self._get_float64_array = lib.get_float64_array
        self._get_float64_gr_array = lib.get_float64_gr_array
        self._get_int32_array = lib.get_int32_array
        self._get_int32_gr_array = lib.get_int32_gr_array
        self._get_int8_array = lib.get_int8_array
        self._get_int8_gr_array = lib.get_int8_gr_array
        self._get_string_array = lib.get_string_array
        
        self._get_complex128_array = lib.get_complex128_array
        self._get_complex128_simple = lib.get_complex128_simple
        self._get_complex128_gr_array = lib.get_complex128_gr_array
        self._get_complex128_gr_simple = lib.get_complex128_gr_simple

        self._get_string = api_util.get_string


class InvalidatedDSSObject:
    '''
    If you see this class somewhere, such as a traceback, it means that the related 
    (parent) object was invalidated by an operation in the DSS engine. This could
    be a "clear" command, or destruction of the DSSContext where the objects lived.
    '''
    pass

InvalidatedObject = InvalidatedDSSObject()


class InvalidatedDSSObjectIterator:
    '''
    If you see this class somewhere, such as a traceback, it means that the related 
    iterator was invalidated and is out-of-scope. If you need to store the object
    referenced by the iterator, use the Python `copy()` function.
    '''
    pass

InvalidatedObjectIterator = InvalidatedDSSObjectIterator()


class InvalidatedDSSBus:
    '''
    If you see this class somewhere, such as a traceback, it means that the related
    (parent) bus was invalidated by an operation in the DSS engine. This could be
    a "clear" command, destruction of the DSSContext where the buses lived, or a 
    redefinition of the circuit buses.
    '''
    pass

InvalidatedBus = InvalidatedDSSBus()


class InvalidatedDSSBusIterator:
    '''
    If you see this class somewhere, such as a traceback, it means that the related
    bus iterator was invalidated and is out-of-scope. If you need to store the object
    referenced by the iterator, use the Python `copy()` function.
    '''
    pass

InvalidatedBusIterator = InvalidatedDSSBusIterator()


class Edit:
    '''
    Edit is a helper class that makes block-editing DSS properties
    easier. It supports instances for the new Obj and Batch APIs.
    '''

    def __init__(self, obj_or_batch, num_changes=1, needs_begin=True):
        '''
        `num_changes` is required for a few classes to correctly match the official OpenDSS behavior
        and must be the number of properties modified in the current editing block. As of DSS C-API
        v0.13, this is only required for the Monitor class, when the `Action` property is used with 
        the `Process` value.
        '''
        self.needs_begin = needs_begin
        self.obj_or_batch = obj_or_batch
        self.num_changes = num_changes

    def __enter__(self):
        if self.needs_begin:
            self.obj_or_batch.begin_edit()

        return self.obj_or_batch

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.obj_or_batch.end_edit(self.num_changes)


__all__ = ('DSSException', 'Base', 'AltDSSAPIUtil', 'LIST_LIKE', 'Edit')