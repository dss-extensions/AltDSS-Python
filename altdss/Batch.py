from __future__ import annotations
import numpy as np
from typing import Union, List, AnyStr, Optional, Iterator
from dss.enums import DSSJSONFlags
from .enums import SetterFlags
from .common import Base, LIST_LIKE, InvalidatedObject
from .types import Float64Array, Int32Array
from .DSSObj import DSSObj
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy

class BatchCommon:
    __slots__ = []

    _get_obj_from_ptr = DSSObj._get_obj_from_ptr

    @property
    def Name(self) -> List[str]:
        res = [
            self._ffi.string(self._lib.Obj_GetName(ptr)).decode(self._api_util.codec)
            for ptr in self._unpack()
        ]
        self._check_for_error()
        return res

    def FullName(self) -> List[str]:
        '''Returns the full name (including object type) for all objects in this batch'''

        res = [
            f'{DSSObj._idx_to_cls[self._lib.Obj_GetClassIdx(ptr)]._cls_name}.' + self._ffi.string(self._lib.Obj_GetName(ptr)).decode()
            for ptr in self._unpack()
        ]
        self._check_for_error()
        return res

    def _get_batch_float64_func(self, funcname):
        func = self._ffi.addressof(self._api_util.lib_unpatched, funcname)
        res = self._get_float64_array(self._lib.Batch_GetFloat64FromFunc, *self._get_ptr_cnt(), func)
        self._check_for_error()
        return res

    def _get_batch_float64_int32_func(self, funcname, funcArg: int):
        func = self._ffi.addressof(self._api_util.lib_unpatched, funcname)
        res = self._get_float64_array(self._lib.Batch_GetFloat64FromFunc2, *self._get_ptr_cnt(), func, funcArg)
        self._check_for_error()
        return res

    def _get_batch_int32_func(self, funcname):
        func = self._ffi.addressof(self._api_util.lib_unpatched, funcname)
        res = self._get_int32_array(self._lib.Batch_GetInt32FromFunc, *self._get_ptr_cnt(), func)
        self._check_for_error()
        return res

    def _unpack(self):
        ptr, cnt = self._get_ptr_cnt()
        if not cnt:
            return []
        
        return self._ffi.unpack(*self._get_ptr_cnt())

    def _dispose_batch(self, batch_ptr):
        if batch_ptr != self._ffi.NULL:
            self._lib.Batch_Dispose(batch_ptr)

    def _invalidate_ptr(self):
        self._pointer = InvalidatedObject

    def _wrap_ptr(self, ptrptr, countptr):
        if ptrptr != self._ffi.NULL:
            self._pointer = self._ffi.gc(ptrptr[0], self._dispose_batch)
        else:
            self._pointer = self._ffi.NULL

        self._count = countptr[0] if countptr != self._ffi.NULL else 0

    def __eq__(self, other):
        return self is other

    def __len__(self) -> int:
        if self._sync_cls_idx:
            return self._lib.Obj_GetCount(self._api_util.ctx, self._sync_cls_idx)

        _, cnt = self._get_ptr_cnt()
        if cnt is None or cnt == self._ffi.NULL:
            return 0

        return cnt
    
    def __call__(self):
        if self._obj_cls is None:
            res = []
            for other_ptr in self._unpack():
                cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
                pycls = DSSObj._idx_to_cls[cls_idx]
                res.append(pycls(self._api_util, other_ptr))
        else:
            res = [
                self._obj_cls(self._api_util, other_ptr)
                for other_ptr in self._unpack()
            ]

        return res

    def to_list(self):
        return self()

    def to_json(self, options: Union[int, DSSJSONFlags] = 0):
        '''
        Returns the data (as a list) of the elements in a batch as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.

        Additionally, the `ExcludeDisabled` flag can be used to excluded disabled elements from the output.
        '''
        s = self._ffi.gc(self._lib.Batch_ToJSON(*self._get_ptr_cnt(), options), self._lib.DSS_Dispose_String)
        self._check_for_error()
        if s == self._ffi.NULL:
            return '[]'
        
        return self._ffi.string(s).decode(self._api_util.codec)


class DSSBatch(Base, BatchCommon):
    #TODO: keep property name for debugging? Or maybe use from the parent object
    __slots__ = [
        '_sync_cls_idx',
        '_ptrptr',
        '_countptr',
        '_pointer',
        '_count',
        '_ffi',
        '__weakref__',
    ]

    def batch(self, **kwargs) -> DSSBatch:
        '''
        Filter a batch using integer or float DSS properties, returning a new batch.

        For integers, provide a single value to match.

        For floats, provide a range as a 2-valued tuple/list (min value, max value), or an exact value to value (not recommended).

        Multiple properties can be listed to allow filtering various conditions.

        Example for loads:

        ```python
            # Create an initial batch using a regular expression
            abc_loads = altdss.Load.batch(re=r'^abc.*$') # a batch of all loads with names starting with "abc"
            abc_loads_filtered = abc_loads.batch(Class=1, Phases=1, kV=(0.1, 1.0))

            # Create an initial batch, already filtered
            abc_loads_filtered = altdss.Load.batch(re=r'^abc.*$', Class=1, Phases=1, kV=(0.1, 1.0))
        ```        
        
        '''
        return self.__class__(self._api_util, _clone_from=self, **kwargs)

    def _filter(self, _existing=True, **kwargs):
        if not kwargs:
            return
            
        batch_exists = _existing
        while kwargs:
            if batch_exists:
                # If a batch already exists, get its info
                prev_ptr, prev_count = self._get_ptr_cnt()

            self._ptrptr = ptrptr = self._ffi.new('void***')
            self._countptr = countptr = self._ffi.new('int32_t[4]')
        
            (prop_name, val) = kwargs.popitem()
            prop_idx = self._obj_cls._cls_prop_idx.get(prop_name.lower())
            if prop_idx is None:
                raise ValueError(f'Invalid property name "{prop_name}"')
            
            if isinstance(val, int) and prop_idx in self._obj_cls._cls_int_idx:
                # Single integer value for an integer property
                if batch_exists:
                    self._lib.Batch_FilterByInt32Property(ptrptr, countptr, prev_ptr, prev_count, prop_idx, val)
                else:
                    self._lib.Batch_CreateByInt32Property(ptrptr, countptr, self._cls_idx, prop_idx, val)

                prop_name = None
            elif prop_idx in self._obj_cls._cls_float_idx:
                if isinstance(val, LIST_LIKE) and len(val) == 2 and isinstance(val[0], (int, float)):
                    # Range of values for a float property
                    if batch_exists:
                        self._lib.Batch_FilterByFloat64PropertyRange(ptrptr, countptr, prev_ptr, prev_count, prop_idx, *val)
                    else:
                        self._lib.Batch_CreateByFloat64PropertyRange(ptrptr, countptr, self._cls_idx, prop_idx, *val)

                    prop_name = None
                elif isinstance(val, (int, float)):
                    # Single value for a float property
                    if batch_exists:
                        self._lib.Batch_FilterByFloat64PropertyRange(ptrptr, countptr, prev_ptr, prev_count, prop_idx, val, val)
                    else:
                        self._lib.Batch_CreateByFloat64PropertyRange(ptrptr, countptr, self._cls_idx, prop_idx, val, val)

                    prop_name = None

            if prop_name is not None:
                raise ValueError(f'Property "{prop_name}" cannot be used to create a filtered batch with value {repr(val)}.')

            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            batch_exists = True

        # Track it only once, the other batches are discarded if temporary, or already tracked somewhere else.
        self._api_util.track_batch(self)


    def __init__(self, api_util, **kwargs):
        begin_edit = bool(kwargs.pop('begin_edit', None))
        self._sync_cls_idx = kwargs.pop('sync_cls_idx', False)

        new_batch_args = kwargs.keys() & {'new_names', 'new_count', }
        existing_batch_args = kwargs.keys() & {'from_func', 'sync_cls_idx', 'idx', 're', '_clone_from'}
        if len(new_batch_args) > 1:
            raise ValueError("Multiple ways to create a batch of new elements were provided.")

        if len(new_batch_args) > 0 and len(existing_batch_args):
            raise ValueError("Mixed batch definitions found. Cannot create new elements and use existing elements at the same time.")
        
        if len(existing_batch_args) > 1:
            raise ValueError("Multiple ways to create a batch of existing elements were provided.")

        if not self._sync_cls_idx:
            Base.__init__(self, api_util)

        self._ffi = api_util.ffi
        self._ptrptr = ptrptr = self._ffi.new('void***')
        self._countptr = countptr = self._ffi.new('int32_t[4]')

        # Clone and filter?
        clone_source = kwargs.pop('_clone_from', None)
        if clone_source is not None:
            self._pointer, self._count = clone_source._get_ptr_cnt()
            self._filter(**kwargs)
            return

        # Create new elements?

        new_names = kwargs.pop('new_names', None)
        if new_names is not None:
            names, names_ptr, names_count = self._prepare_string_array(new_names)
            self._lib.Batch_CreateFromNew(ptrptr, countptr, self._cls_idx, names_ptr, names_count, begin_edit)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        new_count = kwargs.pop('new_count', None)
        if new_count is not None:
            self._lib.Batch_CreateFromNew(ptrptr, countptr, self._cls_idx, self._ffi.NULL, new_count, begin_edit)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        # Use a whole collection? Since no more kwargs, no filter is expected

        if len(kwargs) == 0 or self._sync_cls_idx:
            if not self._sync_cls_idx:
                self._lib.Batch_CreateByClass(ptrptr, countptr, self._cls_idx)
                self._wrap_ptr(ptrptr, countptr)
                # No need to track this kind of batch since it's dynamic
            else:
                self._pointer = self._lib.Obj_GetListPointer(self._api_util.ctx, self._cls_idx)                
                self._count = self._lib.Obj_GetCount(self._api_util.ctx, self._cls_idx)
                api_util.track_batch(self)

            self._check_for_error()
            return

        # Create from specified function, regexp, or list of indices?

        from_func = kwargs.pop('from_func', None)
        if from_func is not None:
            func, *func_args = from_func
            func(ptrptr, countptr, *func_args)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            self._filter(**kwargs)
            return

        regexp = kwargs.pop('re', None)
        if regexp is not None:
            if not isinstance(regexp, bytes):
                regexp = regexp.encode(self._api_util.codec)

            self._lib.Batch_CreateByRegExp(ptrptr, countptr, self._cls_idx, regexp)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            self._filter(**kwargs)
            return

        idx = kwargs.pop('idx', None)
        if idx is not None:
            idx, idx_ptr, idx_cnt = self._prepare_int32_array(np.asarray(idx) + 1)
            self._lib.Batch_CreateByIndex(ptrptr, countptr, self._cls_idx, idx_ptr, idx_cnt)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            self._filter(**kwargs)
            return
        
        # Apply filters on the base collection
        self._filter(_existing=False, **kwargs)

    def begin_edit(self) -> None:
        '''
        Marks for editing all DSS objects in the batch

        In the editing mode, some final side-effects of changing properties are postponed
        until `end_edit` is called. This side-effects can be somewhat costly, like updating
        the model parameters or internal matrices.

        If you don't have any performance constraint, you may edit each property individually
        without worrying about using `begin_edit` and `end_edit`. For convenience, those are
        emitted automatically when editing single properties outside an edit block.
        '''
        self._lib.Batch_BeginEdit(*self._get_ptr_cnt())
        self._check_for_error()

    def end_edit(self, num_changes: int = 1) -> None:
        '''
        Leaves the editing states of all DSS objects in the batch

        `num_changes` is required for a few classes to correctly match the official OpenDSS behavior
        and must be the number of properties modified in the current editing block. As of DSS C-API
        v0.13, this is only required for the Monitor class, when the `Action` property is used with 
        the `Process` value.
        '''
        self._lib.Batch_EndEdit(*self._get_ptr_cnt(), num_changes)
        self._check_for_error()

    def _get_ptr_cnt(self):
        if self._sync_cls_idx:
            self._pointer = self._lib.Obj_GetListPointer(self._api_util.ctx, self._sync_cls_idx)
            self._count = self._lib.Obj_GetCount(self._api_util.ctx, self._sync_cls_idx)

        return (self._pointer, self._count)

    def __iter__(self):
        for ptr in self._unpack():
            yield self._obj_cls(self._api_util, ptr)

    def __getitem__(self, idx0) -> DSSObj:
        '''Get element at 0-based index of the batch pointer array'''
        if idx0 >= len(self) or idx0 < 0:
            raise IndexError

        _pointer, _count = self._get_ptr_cnt()
        ptr = _pointer[idx0]
        return self._obj_cls(self._api_util, ptr)

    def _set_batch_float64_array(self, idx: int, value: Union[BatchFloat64ArrayProxy, float, List[float], Float64Array], flags: SetterFlags = 0):
        if isinstance(value, (BatchFloat64ArrayProxy, BatchInt32ArrayProxy)):
            if self is value._batch and value._idx == idx:
                # ignore if we're setting to property to itself
                return

            value = value.to_array()

        ptr_cnt = self._get_ptr_cnt()
        if np.isscalar(value):
            self._lib.Batch_Float64(
                *ptr_cnt,
                idx,
                self._lib.BatchOperation_Set,
                value,
                flags
            )
            return

        data, data_ptr, data_cnt = self._prepare_float64_array(value)
        if data_cnt != len(self):
            raise ValueError("Number of elements must match")

        self._lib.Batch_Float64Array(
            *ptr_cnt,
            idx,
            self._lib.BatchOperation_Set,
            data_ptr,
            flags
        )


    def _set_batch_int32_array(self, idx: int, value: Union[BatchInt32ArrayProxy, int, List[int], Int32Array], flags: SetterFlags = 0):
        if isinstance(value, BatchInt32ArrayProxy):
            if self is value._batch and value._idx == idx:
                # ignore if we're setting to property to itself
                return

            value = value.to_array()

        ptr_cnt = self._get_ptr_cnt()
        if np.isscalar(value):
            self._lib.Batch_Int32(
                *ptr_cnt,
                idx,
                self._lib.BatchOperation_Set,
                value,
                flags
            )
            return

        data, data_ptr, data_cnt = self._prepare_int32_array(value)
        if data_cnt != len(self):
            raise ValueError("Number of elements must match")

        self._lib.Batch_Int32Array(
            *ptr_cnt,
            idx,
            self._lib.BatchOperation_Set,
            data_ptr,
            flags
        )

    def _set_batch_string(self, idx: int, value: Union[AnyStr, List[AnyStr]], flags: SetterFlags = 0):
        if isinstance(value, (bytes, str)):
            if not isinstance(value, bytes):
                value = value.encode(self._api_util.codec)
            self._lib.Batch_SetString(*self._get_ptr_cnt(), idx, value, flags)
            self._check_for_error()
            return

        # Assume it's a list otherwise
        if len(value) != len(self):
            raise ValueError("The number of elements must match the number of elements in the batch.")

        if not len(value):
            value_ptr = self._ffi.NULL
        else:
            value, value_ptr, _ = self._prepare_string_array(value)

        self._lib.Batch_SetStringArray(*self._get_ptr_cnt(), idx, value_ptr, flags)
        self._check_for_error()

    def _get_batch_float_prop(self, index):
        return self._get_float64_array(self._lib.Batch_GetFloat64, *self._get_ptr_cnt(), index)

    def _get_batch_float_prop_as_list(self, index):
        return self._api_util.get_float64_array2(self._lib.Batch_GetFloat64, *self._get_ptr_cnt(), index)

    def _get_batch_int32_prop(self, index):
        return self._get_int32_array(self._lib.Batch_GetInt32, *self._get_ptr_cnt(), index)

    def _get_batch_int32_prop_as_list(self, index):
        return self._api_util.get_int32_array2(self._lib.Batch_GetInt32, *self._get_ptr_cnt(), index)

    def _get_batch_str_prop(self, index):
        return self._get_string_array(self._lib.Batch_GetString, *self._get_ptr_cnt(), index)

    def _get_batch_obj_prop(self, index, pycls=None):
        ptr = self._ffi.new('void***')
        cnt = self._ffi.new('int32_t[4]')
        self._lib.Batch_GetObject(ptr, cnt, *self._get_ptr_cnt(), index)
        if not cnt[0]:
            self._lib.DSS_Dispose_PPointer(ptr)
            self._check_for_error()
            return []

        # wrap the results with Python classes
        NULL = self._ffi.NULL
        if pycls is None:
            res = []
            for other_ptr in self._ffi.unpack(ptr[0], cnt[0]):
                if other_ptr == NULL:
                    res.append(None)
                    continue
    
                cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
                pycls = DSSObj._idx_to_cls[cls_idx]
                res.append(pycls(self._api_util, other_ptr))
        else:
            res = [
                pycls(self._api_util, other_ptr) if other_ptr != NULL else None
                for other_ptr in self._ffi.unpack(ptr[0], cnt[0])
            ]

        self._lib.DSS_Dispose_PPointer(ptr)
        self._check_for_error()
        return res

    def _set_batch_stringlist_prop(self, idx: int, value: List[AnyStr], flags: SetterFlags = 0):
        '''
        A SINGLE STRING LIST is applied to all objects in the batch for property `idx`
        '''
        if len(self) == 0:
            return

        if not len(value):
            value_ptr, value_count = self._ffi.NULL, 0
        else:
            value, value_ptr, value_count = self._prepare_string_array(value)

        for x in self._unpack():
            self._lib.Obj_SetStringArray(x, idx, value_ptr, value_count, flags)

        self._check_for_error()


    def _set_batch_float64_array_prop(self, idx: int, value: Union[Float64Array, None], flags: SetterFlags = 0):
        '''
        Set values to a FLOAT64 ARRAY property `idx`
        '''
        if len(self) == 0:
            return
        
        if isinstance(value, (BatchFloat64ArrayProxy, BatchInt32ArrayProxy)):
            value = value.to_array()
        
        # Assume 2-d values at first
        single_array = False

        # Empty arrays or None
        if value is None or not len(value):
            value_ptr, value_count = self._ffi.NULL, 0
            single_array = True
        
        # Lists of values, 1-d series, or 1-d array
        elif (isinstance(value, LIST_LIKE) and np.isscalar(value[0])) or (isinstance(value, np.ndarray) and len(value.shape) == 1):
            value, value_ptr, value_count = self._prepare_float64_array(value)
            single_array = True


        if single_array:
            # Apply the same array for all objects in the batch
            for x in self._unpack():
                self._lib.Obj_SetFloat64Array(x, idx, value_ptr, value_count)
        else:
            # Apply one array for each object
            value_2d = value
            for x, value in zip(self._unpack(), value_2d):
                # if np.isscalar(value) and np.isnan(value):
                #     continue

                if value is None or not len(value):
                    value_ptr, value_count = self._ffi.NULL, 0
                else:
                    value, value_ptr, value_count = self._prepare_float64_array(value)

                self._lib.Obj_SetFloat64Array(x, idx, value_ptr, value_count, flags)

        self._check_for_error()


    def _set_batch_int32_array_prop(self, idx: int, value: Union[Int32Array, None], flags: SetterFlags = 0):
        '''
        Set values to an INT32 ARRAY property `idx`
        '''
        if len(self) == 0:
            return
        
        if isinstance(value, (BatchFloat64ArrayProxy, BatchInt32ArrayProxy)):
            value = value.to_array()
        
        # Assume 2-d values at first
        single_array = False

        # Empty arrays or None
        if value is None or not len(value):            
            value_ptr, value_count = self._ffi.NULL, 0
            single_array = True
        
        # Lists of values, 1-d series, or 1-d array
        elif (isinstance(value, LIST_LIKE) and np.isscalar(value[0])) or (isinstance(value, np.ndarray) and len(value.shape) == 1):
            value, value_ptr, value_count = self._prepare_int32_array(value)
            single_array = True

        if single_array:
            # Apply the same array for all objects in the batch
            for x in self._unpack():
                self._lib.Obj_SetInt32Array(x, idx, value_ptr, value_count, flags)
        else:
            # Apply one array for each object
            value_2d = value
            for x, value in zip(self._unpack(), value_2d):
                if value is None or not len(value):
                    value_ptr, value_count = self._ffi.NULL, 0
                else:
                    value, value_ptr, value_count = self._prepare_int32_array(value)

                self._lib.Obj_SetInt32Array(x, idx, value_ptr, value_count, flags)

        self._check_for_error()


    def _get_string_ll(self, idx: int):
        return [
            self._get_string_array(self._lib.Obj_GetStringArray, x, idx)
            for x in self._unpack()
        ]
    
    # def _get_string(self, str_ptr) -> str:
    #     self._check_for_error()
    #     return self._ffi.string(str_ptr).decode(self._api_util.codec)

    def _get_obj_ll(self, idx: int, pycls):
        if len(self) == 0:
            return []

        _pointer, _ = self._get_ptr_cnt()
        obj = self._obj_cls(self._api_util, _pointer[0])
        res = []
        for ptr in self._unpack():
            obj._ptr = ptr
            res.append(obj._get_obj_array(idx, pycls))

        return res

    def _set_batch_obj_prop(self, idx: int, other: Optional[Union[DSSObj, List[DSSObj]]], flags: SetterFlags = 0):
        if len(self) == 0:
            return

        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            # Set each object to empty
            self._lib.Batch_SetObject(*self._get_ptr_cnt(), idx, self._ffi.NULL, flags)
            self._check_for_error()
            return

        if isinstance(other, DSSObj):
            self._lib.Batch_SetObject(*self._get_ptr_cnt(), idx, other._ptr, flags)
            self._check_for_error()
            return

        if (other is not None and isinstance(other, (bytes, str))) or (isinstance(other, LIST_LIKE) and len(other) and isinstance(other[0], (bytes, str))):
            self._set_batch_string(idx, other, flags)
            return

        # Assume it's a list otherwise
        if len(other) != len(self):
            raise ValueError("The number of elements must match the number of elements in the batch.")

        other_ptr = self._ffi.new('void*[]', len(other))
        other_cnt = len(other)
        other_ptr[0:other_cnt] = [o._ptr if o is not None else self._ffi.NULL for o in other]
        self._lib.Batch_SetObjectArray(*self._get_ptr_cnt(), idx, other_ptr, flags)
        self._check_for_error()


    def _set_batch_objlist_prop(self, idx: int, other: List[DSSObj], flags: SetterFlags = 0):
        if len(self) == 0:
            return

        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            other_ptr = self._ffi.NULL
            other_cnt = 0
        else:
            other_ptr = self._ffi.new('void*[]', len(other))
            other_cnt = len(other)
            other_ptr[0:other_cnt] = [o._ptr if o is not None else self._ffi.NULL for o in other]

        for ptr in self._unpack():
            self._lib.Obj_SetObjectArray(ptr, idx, other_ptr, other_cnt, flags)

        self._check_for_error()

        # if len(other) != len(self):
        #     raise ValueError("Number of element in the list must match the number of elements in the batch.")
        # obj = self._obj_cls(self._api_util, self._pointer[0])
        # for other_objs, ptr in zip(other, self._unpack()):
        #     # this could be further optimized to reuse the pointers, but it's 
        #     # not usually in the hot path
        #     obj._ptr = ptr
        #     obj._set_obj_array(idx, other_objs)

    def _edit(self, props):
        ptr, cnt = self._get_ptr_cnt()
        if cnt == 0:
            return

        if not (self._lib.Obj_GetFlags(ptr[0]) and self._lib.DSSObjectFlags_Editing):
            self._lib.Batch_BeginEdit(ptr, cnt)

        self._check_for_error()

        for k, v in props.items():
            setattr(self, k, v)

        self._lib.Batch_EndEdit(ptr, cnt, len(props))
        self._check_for_error()


class NonUniformBatch(Base, BatchCommon):
    '''
    A batch of non-uniform objects.

    Currently, provides:
    - iteration through individual objects
    - access as a list of objects, either through a call statement or `to_list()` function.
    - all basic names as a list of strings
    - all full names (including DSS object type) as a list of strings
    '''

    __slots__ = (
        '_func',
        '_parent_ptr',
        '_ptr',
        '_pointer', #TODO: using both _pointer and _ptr?
        '_cnt', 
        '_count', #TODO: using both _count and _cnt?
        '_obj_cls',
        '_ffi',
        '_copy_safe',
        '_sync_cls_idx',
        '__weakref__',
    )

    def _invalidate_ptr(self):
        self._ptr = InvalidatedObject
        self._pointer = InvalidatedObject

    def __init__(self, func, parent, pycls=None, copy_safe=False, sync_cls_idx=None):
        Base.__init__(self, parent._api_util)
        BatchCommon.__init__(self)
        self._ffi = self._api_util.ffi
        self._func = func
        self._parent_ptr = parent._ptr
        self._obj_cls = pycls
        self._ptr = None
        self._cnt = None
        self._copy_safe = copy_safe
        if self._copy_safe:
            self._api_util.track_batch(self)

        if func is None:
            self._sync_cls_idx = sync_cls_idx
        else:
            self._sync_cls_idx = None

    def _dispose_batch(self, batch_ptr):
        if batch_ptr != self._ffi.NULL and batch_ptr[0] != self._ffi.NULL:
            self._lib.Batch_Dispose(batch_ptr[0])

    def _get_ptr_cnt(self):
        if self._sync_cls_idx:
            self._pointer = self._lib.Obj_GetListPointer(self._api_util.ctx, self._sync_cls_idx)
            self._count = self._lib.Obj_GetCount(self._api_util.ctx, self._sync_cls_idx)
            return (self._pointer, self._count)

        if self._copy_safe and self._cnt is not None:
            return (self._ptr[0], self._cnt[0])

        self._ptr = self._ffi.gc(self._ffi.new('void***'), self._dispose_batch)
        self._cnt = self._ffi.new('int32_t[4]')
        self._func(self._ptr, self._cnt, self._parent_ptr)
        return (self._ptr[0], self._cnt[0])

    def __iter__(self) -> Iterator[DSSObj]:
        ptr, cnt = self._get_ptr_cnt()
        if self._obj_cls is None:
            for idx in range(cnt):
                other_ptr = ptr[idx]
                cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
                pycls = DSSObj._idx_to_cls[cls_idx]
                yield pycls(self._api_util, other_ptr)

            return

        for idx in range(cnt[0]):
            yield self._obj_cls(self._api_util, ptr[idx])

    def __getitem__(self, idx: int) -> DSSObj:
        '''
        Return an object of the batch by index (0-based).
        '''
        _pointer, _count = self._get_ptr_cnt()
        if idx > _count or idx < 0:
            raise IndexError('Invalid object index inside the batch')
        
        ptr = _pointer[idx]
        if ptr == self._ffi.NULL:
            return None

        if self._obj_cls is None:
            cls_idx = self._lib.Obj_GetClassIdx(ptr)
            pycls = DSSObj._idx_to_cls[cls_idx]
            return pycls(self._api_util, ptr)

        return self._obj_cls(self._api_util, ptr)


__all__ = ('DSSBatch', 'NonUniformBatch', )
