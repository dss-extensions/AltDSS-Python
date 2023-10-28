'''
Object and batch API bases, used internally.

Copyright (c) 2021-2023 Paulo Meira
Copyright (c) 2021-2023 DSS-Extensions contributors
'''
import numpy as np
from typing import Union, List, AnyStr, Optional, Generator, Dict
from typing_extensions import Self
from .._types import Float64Array, Int32Array, Int8Array, Float32Array, ComplexArray, BoolArray
from .._cffi_api_util import Base, DSSException, CffiApiUtil
from ..enums import DSSJSONFlags, OCPDevType, SolveModes

try:
    import pandas as pd
    LIST_LIKE = (pd.Series, list, tuple)
except ModuleNotFoundError:
    LIST_LIKE = (list, tuple)

import warnings
# class NotSet:
#     pass

class BatchFloat64ArrayProxy:
    def __init__(self, batch, idx):
        self._batch = batch
        self._idx = idx
        self._lib = batch._api_util.lib

    def to_array(self):
        return self._batch._get_batch_float_prop(self._idx)

    def __call__(self):
        return self.to_array()

    def __len__(self):
        return len(self._batch)

    def __mul__(self, other):
        return self.to_array() * other

    def __truediv__(self, other):
        return self.to_array() / other

    def __floordiv__(self, other):
        return self.to_array() // other

    def __add__(self, other):
        return self.to_array() + other

    def __sub__(self, other):
        return self.to_array() - other

    def __array__(self):
        return self.to_array()

    def __iadd__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Float64(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Increment,
                other
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() + other
        data, data_ptr, _ = batch._prepare_float64_array(data)
        batch._lib.Batch_SetFloat64Array(
            *ptr_cnt,
            self._idx,
            data_ptr
        )
        batch._check_for_error()
        return self

    def __isub__(self, other):
        return self.__iadd__(-other)

    def __imul__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Float64(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                other
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() * other
        data, data_ptr, _ = batch._prepare_float64_array(data)
        batch._lib.Batch_SetFloat64Array(
            *ptr_cnt,
            self._idx,
            data_ptr
        )
        batch._check_for_error()
        return self

    def __idiv__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Float64(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                1 / other
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() / other
        data, data_ptr, _ = batch._prepare_float64_array(data)
        batch._lib.Batch_SetFloat64Array(
            *ptr_cnt,
            self._idx,
            data_ptr
        )
        batch._check_for_error()
        return self


class BatchInt32ArrayProxy:
    def __init__(self, batch, idx):#, kind):
        self._batch = batch
        self._idx = idx
        self._lib = batch._api_util.lib

    def to_array(self):
        return self._batch._get_batch_int32_prop(self._idx)

    def __call__(self):
        return self.to_array()

    def __len__(self):
        return len(self._batch)

    def __mul__(self, other):
        return self.to_array() * other

    def __truediv__(self, other):
        return self.to_array() / other

    def __floordiv__(self, other):
        return self.to_array() // other

    def __add__(self, other):
        return self.to_array() + other

    def __sub__(self, other):
        return self.to_array() - other

    def __array__(self):
        return self.to_array()

    def __iadd__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Int32(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Increment,
                other
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() + other
        data, data_ptr, _ = batch._api_util.prepare_int32_array(data)
        batch._lib.Batch_SetInt32Array(
            *ptr_cnt,
            self._idx,
            data_ptr
        )
        batch._check_for_error()
        return self

    def __isub__(self, other):
        return self.__iadd__(-other)

    def __imul__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Int32(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                other
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() * other
        data, data_ptr, _ = batch._prepare_int32_array(data)
        batch._lib.Batch_SetInt32Array(
            *ptr_cnt,
            self._idx,
            data_ptr
        )
        batch._check_for_error()
        return self

    def __idiv__(self, other):
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Int32(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                1 / other
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data = self.to_array() / other
        data, data_ptr, _ = batch._prepare_int32_array(data)
        self._lib.Batch_SetInt32Array(
            *ptr_cnt,
            self._idx,
            data_ptr
        )
        batch._check_for_error()
        return self


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


class DSSObj(Base):
    # _properties_by_idx = {
    #     1: ('kV', 'Obj_SetDouble')
    # }
    # _properties_by_name = {
    #     'kV': (1, 'Obj_SetDouble')
    # }
    __slots__ = [
        '_ptr',
        '_ffi',
        '_get_int32_list',
    ]

    def __init__(self, api_util, ptr):
        super().__init__(api_util)
        self._ptr = ptr
        self._ffi = api_util.ffi
        self._get_int32_list = api_util.get_int32_array2

    def __hash__(self):
        return self._ptr.__hash__()

    def __eq__(self, other):
        return self._ptr == getattr(other, '_ptr')

    def __ne__(self, other):
        return self._ptr != getattr(other, '_ptr')

    # def __getitem__(self, name_or_idx):
    #     if isinstance(name_or_idx, int):
    #         funcname, *_ = self._properties_by_idx[name_or_idx]
    #         return getattr(self._lib, funcname)(name_or_idx)

    #     if type(name_or_idx) is bytes:
    #         name_or_idx = name_or_idx.decode(self._api_util.codec)

    #     idx, funcname, *_ = self._properties_by_name[name_or_idx]
    #     return getattr(self._lib, funcname)(idx)

    # def to_dict(self):
    #     return {
    #         name: getattr(self._lib, funcname)(idx)
    #         for (name, (idx, funcname, *_)) in self._properties_by_name.items()
    #     }

    def to_json(self, options: Union[int, DSSJSONFlags] = 0):
        '''
        Returns an element's data as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.

        By default (`options = 0`), only the properties explicitly set. The properties are returned in the order they are set in the input.
        As a reminder, OpenDSS is sensitive to the order of the properties.

        The `options` bit-flags are available in the `DSSJSONFlags` enum.
        Values used by this function are:

        - `Full`: if set, all properties are returned, ordered by property index instead.
        - `SkipRedundant`: if used with `Full`, all properties except redundant and unused ones are returned.
        - `EnumAsInt`: enumerated properties are returned as integer values instead of strings.
        - `FullNames`: any element reference will use the full name (`{class name}.{element name}`) even if not required.
        - `Pretty`: more whitespace is used in the output for a "prettier" format.
        - `SkipDSSClass`: do not add the "DSSClass" property to the JSON objects.

        **NOT IMPLEMENTED YET**:
        - `State`: include run-time state information
        - `Debug`: include debug information

        Other bit-flags are reserved for future uses. Please use `DSSJSONFlags` enum to avoid potential conflicts.

        (API Extension)
        '''
        s = self._ffi.gc(self._lib.Obj_ToJSON(self._ptr, options), self._lib.DSS_Dispose_String)
        self._check_for_error()
        return self._ffi.string(s).decode(self._api_util.codec)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and (other._ptr == self._ptr)

    def __repr__(self):
        # This could probably be done in DSS C-API instead (equivalent to SaveWrite)
        # ffi = self._api_util.ffi
        # seq = sorted(enumerate(ffi.unpack(self._lib.Obj_GetPropSeqPtr(self._ptr, ffi.NULL), self._lib.Obj_GetNumProperties(self._ptr)), start=1), key=lambda v: v[1])
        # vals = []
        # for propidx, propseq in seq:
        #     if propseq:
        #         vals.append(f'{self._properties_by_idx[propidx][0]}={self[propidx]}')

        return f'<{self._cls_name}.{self.name}>'# {" ".join(vals)}'

    @property
    def name(self) -> str:
        s = self._lib.Obj_GetName(self._ptr)
        self._check_for_error()
        return self._ffi.string(s).decode(self._api_util.codec)

    def _get_complex(self, idx: int) -> complex:
        return self._get_float64_array(
            self._lib.Obj_GetFloat64Array,
            self._ptr,
            idx
        ).view(complex)[0]

    def _set_complex(self, idx: int, value: complex):
        data = np.array([complex(value)])
        data, data_ptr, cnt_ptr = self._prepare_float64_array(data.view(dtype=np.float64))
        self._lib.Obj_SetFloat64Array(self._ptr, idx, data_ptr, cnt_ptr)
        self._check_for_error()

    def _get_prop_string(self, idx: int) -> str:
        s = self._lib.Obj_GetString(self._ptr, idx)
        return self._decode_and_free_string(s)

    def _set_string_o(self, idx: int, value: AnyStr):
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Obj_SetString(self._ptr, idx, value)
        self._check_for_error()

    def _set_float64_array_o(self, idx: int, value: Float64Array):
        value, value_ptr, value_count = self._prepare_float64_array(value)
        self._lib.Obj_SetFloat64Array(self._ptr, idx, value_ptr, value_count)
        self._check_for_error()

    def _set_int32_array_o(self, idx: int, value: Int32Array):
        value, value_ptr, value_count = self._prepare_int32_array(value)
        self._lib.Obj_SetInt32Array(self._ptr, idx, value_ptr, value_count)
        self._check_for_error()

    def _set_string_array_o(self, idx: int, value: List[AnyStr]):
        value, value_ptr, value_count = self._prepare_string_array(value)
        self._lib.Obj_SetStringArray(self._ptr, idx, value_ptr, value_count)
        self._check_for_error()

    def _get_obj_from_ptr(self, other_ptr, pycls):
        self._check_for_error()
        if other_ptr == self._ffi.NULL:
            return None

        if pycls is None:
            cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
            pycls = DSSObj._idx_to_cls[cls_idx]

        return pycls(self._api_util, other_ptr)

    def _get_obj(self, idx: int, pycls):
        other_ptr = self._lib.Obj_GetObject(self._ptr, idx)
        self._check_for_error()
        if other_ptr == self._ffi.NULL:
            return None

        if pycls is None:
            cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
            pycls = DSSObj._idx_to_cls[cls_idx]

        return pycls(self._api_util, other_ptr)

    def _set_obj(self, idx: int, other):
        if other is not None:
            other_ptr = other._ptr
        else:
            other_ptr = self._ffi.NULL

        self._lib.Obj_SetObject(self._ptr, idx, other_ptr)
        self._check_for_error()

    def _get_obj_array(self, idx: int, pycls=None):
        ptr = self._ffi.new('void***')
        cnt = self._ffi.new('int32_t[4]')
        self._lib.Obj_GetObjectArray(ptr, cnt, self._ptr, idx)
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

    def _get_obj_array_func(self, func, *args, pycls=None):
        ptr = self._ffi.new('void***')
        cnt = self._ffi.new('int32_t[4]')
        func(self._ptr, ptr, cnt, *args)
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


    def _set_obj_array(self, idx: int, other):
        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            other_ptr = self._ffi.NULL
            other_cnt = 0
        else:
            other_cnt = len(other)
            other_ptr = self.ffi.new('void*[]', other_cnt)
            other_ptr[:] = [o._ptr for o in other]

        self._lib.Obj_SetObjectArray(self._ptr, idx, other_ptr, other_cnt)
        self._check_for_error()

    def begin_edit(self) -> None:
        '''
        Marks a DSS object for editing

        In the editing mode, some final side-effects of changing properties are post-poned
        until `_end_edit` is called. This side-effects can be somewhat costly, like updating
        the model parameters or internal matrices.

        If you don't have any performance constraint, you may edit each property individually
        without worrying about using `begin_edit` and `end_edit`. For convenience, those are
        emitted automatically when editing single properties outside an edit block.
        '''
        self._lib.Obj_BeginEdit(self._ptr)
        self._check_for_error()

    def end_edit(self, num_changes: int = 1) -> None:
        '''
        Leaves the editing state of a DSS object

        `num_changes` is required for a few classes to correctly match the official OpenDSS behavior
        and must be the number of properties modified in the current editing block. As of DSS C-API
        v0.13, this is only required for the Monitor class, when the `Action` property is used with 
        the `Process` value.
        '''
        self._lib.Obj_EndEdit(self._ptr, num_changes)
        self._check_for_error()


def _get_dispose_batch(lib, ffi):
    def _dispose_batch(ptr):
        if ptr != ffi.NULL:
            lib.Batch_Dispose(ptr)

    return _dispose_batch


class DSSBatch(Base):

    #TODO: keep property name for debugging? Or maybe use from the parent object
    def _wrap_ptr(self, ptrptr, countptr):
        self._pointer = self._ffi.gc(ptrptr[0] if ptrptr != self._ffi.NULL else self._ffi.NULL, _get_dispose_batch(self._lib, self._ffi))
        self._count = countptr[0] if countptr != self._ffi.NULL else 0

    def __init__(self, api_util, **kwargs):
        begin_edit = kwargs.pop('begin_edit', None)
        if begin_edit is None:
            begin_edit = True

        if len(kwargs) > 1:
            raise ValueError('Exactly one argument is expected.')

        self._sync_cls = kwargs.get('sync_cls', False)

        if not self._sync_cls:
            Base.__init__(self, api_util)

        self._ffi = api_util.ffi
        self._ptrptr = ptrptr = self._ffi.new('void***')
        self._countptr = countptr = self._ffi.new('int32_t[4]')

        #TODO: weakref

        if len(kwargs) == 0 or (len(kwargs) == 1 and self._sync_cls):
            if not self._sync_cls:
                self._lib.Batch_CreateByClass(ptrptr, countptr, self._cls_idx)
                self._wrap_ptr(ptrptr, countptr)
            else:
                self._pointer = self._lib.Obj_GetListPointer(self._api_util.ctx, self._cls_idx)                
                self._count = self._lib.Obj_GetCount(self._api_util.ctx, self._cls_idx)

            self._check_for_error()
            return

        from_func = kwargs.get('from_func')
        if from_func is not None:
            func, *func_args = from_func
            func(ptrptr, countptr, *func_args)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        new_names = kwargs.get('new_names')
        if new_names is not None:
            names, names_ptr, names_count = self._prepare_string_array(new_names)
            self._lib.Batch_CreateFromNew(ptrptr, countptr, self._cls_idx, names_ptr, names_count, begin_edit)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        new_count = kwargs.get('new_count')
        if new_count is not None:
            self._lib.Batch_CreateFromNew(ptrptr, countptr, self._cls_idx, self._ffi.NULL, new_count, begin_edit)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        regexp = kwargs.get('re')
        if regexp is not None:
            if not isinstance(regexp, bytes):
                regexp = regexp.encode(self._api_util.codec)

            self._lib.Batch_CreateByRegExp(ptrptr, countptr, self._cls_idx, regexp)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        idx = kwargs.get('idx')
        if regexp is not None:
            idx, idx_ptr, idx_cnt = self._prepare_int32_array(idx)
            self._lib.Batch_CreateByIndex(ptrptr, countptr, self._cls_idx, idx_ptr, idx_cnt)
            self._wrap_ptr(ptrptr, countptr)
            self._check_for_error()
            return

        (prop_name, intval), = kwargs.items()
        prop_idx = self._obj_cls._cls_prop_idx.get(prop_name.lower())
        if prop_idx is None:
            raise ValueError('Invalid property name "{}"'.format(prop_name))
        self._lib.Batch_CreateByInt32Property(ptrptr, countptr, self._cls_idx, prop_idx, intval)
        self._wrap_ptr(ptrptr, countptr)
        self._check_for_error()


    def to_json(self, options: Union[int, DSSJSONFlags] = 0):
        '''
        Returns the data (as a list) of the elements in a batch as a JSON-encoded string.

        The `options` parameter contains bit-flags to toggle specific features.
        See `Obj_ToJSON` (C-API) for more, or `DSSObj.to_json` in Python.

        Additionally, the `ExcludeDisabled` flag can be used to excluded disabled elements from the output.

        (API Extension)
        '''
        s = self._ffi.gc(self._lib.Batch_ToJSON(*self._get_ptr_cnt(), options), self._lib.DSS_Dispose_String)
        self._check_for_error()
        return self._ffi.string(s).decode(self._api_util.codec)

    def begin_edit(self) -> None:
        '''
        Marks for editing all DSS objects in the batch

        In the editing mode, some final side-effects of changing properties are post-poned
        until `_end_edit` is called. This side-effects can be somewhat costly, like updating
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

    def __eq__(self, other):
        return self is other

    def __len__(self):
        if self._sync_cls:
            return self._lib.Obj_GetCount(self._api_util.ctx, self._cls_idx)

        if self._count is None or self._count == self._ffi.NULL:
            return 0

        return self._count
    
    def _get_ptr_cnt(self):
        if self._sync_cls:
            self._pointer = self._lib.Obj_GetListPointer(self._api_util.ctx, self._cls_idx)                
            self._count = self._lib.Obj_GetCount(self._api_util.ctx, self._cls_idx)

        return (self._pointer, self._count)

    def __iter__(self):
        for ptr in self._unpack():
            yield self._obj_cls(self._api_util, ptr)

    def __getitem__(self, idx0) -> DSSObj:
        #TODO: decide if we keep it 0-based or 1-based here
        '''Get element at 0-based index of the batch pointer array'''
        if idx0 >= len(self) or idx0 < 0:
            raise IndexError

        _pointer, _count = self._get_ptr_cnt()
        ptr = _pointer[idx0]
        return self._obj_cls(self._api_util, ptr)

    def _set_batch_float64_array(self, idx: int, value: Union[BatchFloat64ArrayProxy, float, List[float], Float64Array]):
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
                value
            )
            return

        data, data_ptr, data_cnt = self._prepare_float64_array(value)
        if data_cnt != len(self):
            raise ValueError("Number of elements must match")

        self._lib.Batch_SetFloat64Array(
            *ptr_cnt,
            idx,
            data_ptr
        )


    def _set_batch_int32_array(self, idx: int, value: Union[BatchInt32ArrayProxy, int, List[int], Int32Array]):
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
                value
            )
            return

        data, data_ptr, data_cnt = self._prepare_int32_array(value)
        if data_cnt != len(self):
            raise ValueError("Number of elements must match")

        self._lib.Batch_SetInt32Array(
            *ptr_cnt,
            idx,
            data_ptr
        )

    def _set_batch_string(self, idx: int, value: Union[AnyStr, List[AnyStr]]):
        if isinstance(value, (bytes, str)):
            if not isinstance(value, bytes):
                value = value.encode(self._api_util.codec)
            self._lib.Batch_SetString(*self._get_ptr_cnt(), idx, value)
            self._check_for_error()
            return

        # Assume it's a list otherwise
        if len(value) != len(self):
            raise ValueError("The number of elements must match the number of elements in the batch.")

        if not len(value):
            value_ptr = self._ffi.NULL
        else:
            value, value_ptr, _ = self._prepare_string_array(value)

        self._lib.Batch_SetStringArray(*self._get_ptr_cnt(), idx, value_ptr)
        self._check_for_error()

    def _unpack(self):
        return self._ffi.unpack(*self._get_ptr_cnt())

    def _get_batch_float_prop(self, index):
        return self._get_float64_array(self._lib.Batch_GetFloat64, *self._get_ptr_cnt(), index)

    def _get_batch_float_func(self, funcname):
        func = self._ffi.addressof(self._api_util.lib_unpatched, funcname)
        res = self._get_float64_array(self._lib.Batch_GetFloat64FromFunc, *self._get_ptr_cnt(), func)
        self._check_for_error()
        return res

    def _get_batch_float64_int32_func(self, funcname, funcArg: int):
        func = self._ffi.addressof(self._api_util.lib_unpatched, funcname)
        res = self._get_float64_array(self._lib.Batch_GetFloat64FromFunc2, *self._get_ptr_cnt(), func, funcArg)
        self._check_for_error()
        return res

    def _get_batch_int32_prop(self, index):
        return self._get_int32_array(self._lib.Batch_GetInt32, *self._get_ptr_cnt(), index)

    def _get_batch_int32_func(self, funcname):
        func = self._ffi.addressof(self._api_util.lib_unpatched, funcname)
        res = self._get_int32_array(self._lib.Batch_GetInt32FromFunc, *self._get_ptr_cnt(), func)
        self._check_for_error()
        return res

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

    def _set_batch_stringlist_prop(self, idx: int, value: List[AnyStr]):
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
            self._lib.Obj_SetStringArray(x, idx, value_ptr, value_count)

        self._check_for_error()


    def _set_batch_float64_array_prop(self, idx: int, value: Union[Float64Array, None]):
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
        if not len(value) or value is None:
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
                if not len(value) or value is None:
                    value_ptr, value_count = self._ffi.NULL, 0
                else:
                    value, value_ptr, value_count = self._prepare_float64_array(value)

                self._lib.Obj_SetFloat64Array(x, idx, value_ptr, value_count)

        self._check_for_error()


    def _set_batch_int32_array_prop(self, idx: int, value: Union[Int32Array, None]):
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
        if not len(value) or value is None:
            value_ptr, value_count = self._ffi.NULL, 0
            single_array = True
        
        # Lists of values, 1-d series, or 1-d array
        elif (isinstance(value, LIST_LIKE) and np.isscalar(value[0])) or (isinstance(value, np.ndarray) and len(value.shape) == 1):
            value, value_ptr, value_count = self._prepare_int32_array(value)
            single_array = True

        if single_array:
            # Apply the same array for all objects in the batch
            for x in self._unpack():
                self._lib.Obj_SetInt32Array(x, idx, value_ptr, value_count)
        else:
            # Apply one array for each object
            value_2d = value
            for x, value in zip(self._unpack(), value_2d):
                if not len(value) or value is None:
                    value_ptr, value_count = self._ffi.NULL, 0
                else:
                    value, value_ptr, value_count = self._prepare_int32_array(value)

                self._lib.Obj_SetInt32Array(x, idx, value_ptr, value_count)

        self._check_for_error()


    def _get_string_ll(self, idx: int):
        return [
            self._get_string_array(self._lib.Obj_GetStringArray, x, idx)
            for x in self._unpack()
        ]
    
    def _get_string(self, str_ptr) -> str:
        self._check_for_error()
        return self._ffi.string(str_ptr).decode(self._api_util.codec)

    @property
    def name(self) -> List[str]:
        res = [
            self._ffi.string(self._lib.Obj_GetName(ptr)).decode(self._api_util.codec)
            for ptr in self._unpack()
        ]
        self._check_for_error()
        return res


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

    def _set_batch_obj_prop(self, idx: int, other: Optional[Union[DSSObj, List[DSSObj]]]):
        if len(self) == 0:
            return

        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            # Set each object to empty
            self._lib.Batch_SetObject(*self._get_ptr_cnt(), idx, self._ffi.NULL)
            self._check_for_error()
            return

        if other is not None or isinstance(other, (bytes, str)) or (isinstance(other, LIST_LIKE) and len(other) and isinstance(other[0], (bytes, str))):
            self._set_batch_string(idx, other)
            return

        if isinstance(other, DSSObj):
            self._lib.Batch_SetObject(*self._get_ptr_cnt(), idx, other._ptr)
            self._check_for_error()
            return

        # Assume it's a list otherwise
        if len(other) != len(self):
            raise ValueError("The number of elements must match the number of elements in the batch.")

        other_ptr = self._ffi.new('void*[]', len(other))
        other_ptr[:] = [o._ptr if o is not None else self._ffi.NULL for o in other]
        other_cnt = len(other)
        self._lib.Batch_SetObjectArray(*self._get_ptr_cnt(), idx, other_ptr)
        self._check_for_error()


    def _set_batch_objlist_prop(self, idx: int, other: List[DSSObj]):
        if len(self) == 0:
            return

        if other is None or (isinstance(other, LIST_LIKE) and len(other) == 0):
            other_ptr = self._ffi.NULL
            other_cnt = 0
        else:
            other_ptr = self._ffi.new('void*[]', len(other))
            other_ptr[:] = [o._ptr if o is not None else self._ffi.NULL for o in other]
            other_cnt = len(other)

        for ptr in self._unpack():
            self._lib.Obj_SetObjectArray(ptr, idx, other_ptr, other_cnt)

        self._check_for_error()

        # if len(other) != len(self):
        #     raise ValueError("Number of element in the list must match the number of elements in the batch.")
        # obj = self._obj_cls(self._api_util, self._pointer[0])
        # for other_objs, ptr in zip(other, self._unpack()):
        #     # this could be further optimized to reuse the pointers, but it's 
        #     # not usually in the hot path
        #     obj._ptr = ptr
        #     obj._set_obj_array(idx, other_objs)


class IDSSObj(Base):
    def __init__(self, iobj, obj_cls, batch_cls):
        super().__init__(iobj._api_util)
        self._iobj = iobj
        self.cls_idx = obj_cls._cls_idx
        self._obj_cls = obj_cls
        self._batch_cls = batch_cls
        DSSObj._idx_to_cls[self.cls_idx] = obj_cls

    def batch(self, **kwargs):
        '''
        Creates a new batch handler of (existing) objects
        '''
        return self._batch_cls(self._api_util, **kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, count: Optional[int] = None, begin_edit=True):
        '''
        Creates a new batch handler of new objects, with the specified names, 
        or "count" elements with a randomized prefix.
        '''
        if names is not None:
            if count is not None:
                raise ValueError("Provide either names or count, not both")

            return self._batch_cls(self._api_util, new_names=names, begin_edit=begin_edit)

        if count is not None:
            return self._batch_cls(self._api_util, new_count=count, begin_edit=begin_edit)

        raise ValueError("Provide either names or count to create a new batch")

    def _batch_new_aux(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, props=None):
        '''
        Aux. function used by the descendant classes (which provide typing info) to create the batches.
        '''
        if df is not None:
            columns = list(df.columns)
            if names is None:
                if 'name' in df.columns:
                    names = df['name'].astype(str)
                    columns.remove('name')
                elif 'names' in df.columns:
                    names = df['names'].astype(str)
                    columns.remove('names')

            batch = IDSSObj.batch_new(self, names=names, begin_edit=True)
            try:
                for k in columns:
                    setattr(batch, k, df[k])
            finally:
                batch.end_edit()

            return batch

        if props:
            # Allow using name instead of names if passing kwargs for pre-filling
            if names is None and count is None and 'name' in props:
                names = props.pop('name')

            batch = IDSSObj.batch_new(self, names=names, count=count, begin_edit=True)
            try:
                for k, v in props.items():
                    setattr(batch, k, v)
            finally:
                batch.end_edit()

            return batch

        return IDSSObj.batch_new(self, names, count, begin_edit)


    def new(self, name: str, begin_edit=True, activate=False):
        if not isinstance(name, bytes):
            name = name.encode(self._api_util.codec)

        ptr = self._api_util.lib.Obj_New(
            self._api_util.ctx,
            self.cls_idx,
            name,
            activate,
            begin_edit
        )

        if ptr == self._api_util.ffi.NULL:
            raise ValueError('Could not create object "{}".'.format(name))

        return self._obj_cls(self._api_util, ptr)


    def _new(self, name: AnyStr, begin_edit=True, activate=False, props=None):
        '''
        Aux. function used by the descendant classes (which provide typing info) to create the objects.
        '''
        if props:
            obj = IDSSObj.new(self, name, True, activate)
            try:
                for k, v in props.items():
                    setattr(obj, k, v)
            finally:
                obj.end_edit()

            return obj

        return IDSSObj.new(self, name, begin_edit, activate)
        

    def find(self, name_or_idx):
        lib = self._lib

        if isinstance(name_or_idx, int):
            ptr = lib.Obj_GetHandleByIdx(self._api_util.ctx, self.cls_idx, name_or_idx)
            if ptr == self._api_util.ffi.NULL:
                raise ValueError('Could not find object by index "{}".'.format(name_or_idx))
        else:
            if type(name_or_idx) is not bytes:
                name_or_idx = name_or_idx.encode(self._api_util.codec)

            ptr = lib.Obj_GetHandleByName(self._api_util.ctx, self.cls_idx, name_or_idx)
            if ptr == self._api_util.ffi.NULL:
                raise ValueError('Could not find object by name "{}".'.format(name_or_idx))

        return self._obj_cls(self._api_util, ptr)

    def __len__(self):
        return self._lib.Obj_GetCount(self._api_util.ctx, self.cls_idx)

    def __iter__(self):
        for idx in range(len(self)):
            ptr = self._lib.Obj_GetHandleByIdx(self._api_util.ctx, self.cls_idx, idx + 1)
            yield self._obj_cls(self._api_util, ptr)

    def __getitem__(self, name_or_idx):
        return self.find(name_or_idx)

    def __contains__(self, name: str) -> bool:
        lib = self._lib
        if type(name) is not bytes:
            name = name.encode(self._api_util.codec)

        return (lib.Obj_GetHandleByName(self._api_util.ctx, self.cls_idx, name) != self._api_util.ffi.NULL)


class NonUniformBatch(Base):
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
        '_cnt',
        '_pycls',
        '_ffi',
        '_copy_safe'
    )

    def __init__(self, func, parent, pycls=None, copy_safe=False):
        super().__init__(parent._api_util)
        self._ffi = self._api_util.ffi
        self._func = func
        self._parent_ptr = parent._ptr
        self._pycls = pycls
        self._ptr = None
        self._cnt = None
        self._copy_safe = copy_safe

    def _fill_data(self):
        if self._copysafe and self._cnt is None:
            return (self._ptr, self._cnt)
                
        self._ptr = self._ffi.gc(self._ffi.new('void***'), _get_dispose_batch(self._lib, self._ffi))
        self._cnt = self._ffi.new('int32_t[4]')
        self._func(self._ptr, self._cnt, self._parent_ptr)

        return (self._ptr, self._cnt)
        
    def __len__(self):
        _, cnt = self._fill_data()
        res = cnt[0]
        return res

    def __iter__(self):
        ptr, cnt = self._fill_data()
        ptr = ptr[0]
        if self._pycls is None:
            for idx in range(cnt[0]):
                other_ptr = ptr[idx]
                cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
                pycls = DSSObj._idx_to_cls[cls_idx]
                yield pycls(self._api_util, other_ptr)

            return

        for idx in range(cnt[0]):
            yield self._pycls(self._api_util, ptr[idx])

    def __call__(self):
        ptr, cnt = self._fill_data()
        if not cnt[0]:
            return []
    
        if self._pycls is None:
            res = []
            for other_ptr in self._ffi.unpack(ptr[0], cnt[0]):
                cls_idx = self._lib.Obj_GetClassIdx(other_ptr)
                pycls = DSSObj._idx_to_cls[cls_idx]
                res.append(pycls(self._api_util, other_ptr))
        else:
            res = [
                self._pycls(self._api_util, other_ptr)
                for other_ptr in self._ffi.unpack(ptr[0], cnt[0])
            ]

        return res

    def to_list(self):
        return self()

    def Name(self) -> List[str]:
        '''Returns the name (without object type) for all objects in this batch'''
        ptr, cnt = self._fill_data()
        if not cnt[0]:
            return []

        res = [
            self._ffi.string(self._lib.Obj_GetName(other_ptr)).decode()
            for other_ptr in self._ffi.unpack(ptr[0], cnt[0])
        ]
        self._check_for_error()
        return res

    def FullName(self) -> List[str]:
        '''Returns the full name (including object type) for all objects in this batch'''

        ptr, cnt = self._fill_data()
        if not cnt[0]:
            return []

        res = [
            f'{DSSObj._idx_to_cls[self._lib.Obj_GetClassIdx(other_ptr)]._cls_name}.' + self._ffi.string(self._lib.Obj_GetName(other_ptr)).decode()
            for other_ptr in self._ffi.unpack(ptr[0], cnt[0])
        ]
        self._check_for_error()
        return res


class CircuitElementMixin:
    __slots__ = () 
    # To avoid layout issues, let the final class use the following instead
    _extra_slots = ['Controllers', ]

    def __init__(self, *args):
        super().__init__(*args)
        self.Controllers = NonUniformBatch(self._lib.Alt_CE_Get_Controllers, self)

    def GUID(self) -> str:
        '''Object's GUID/UUID. Currently used only in the CIM-related methods.'''
        return self._get_string(self._lib.Alt_CE_Get_GUID(self._ptr))

    def _getDisplayName(self) -> str:
        return self._get_string(self._lib.Alt_CE_Get_DisplayName(self._ptr))
    
    def _setDisplayName(self, value: AnyStr):
        if not isinstance(value, bytes):
            value = value.encode(self._api_util.codec)
        self._lib.Alt_CE_Set_DisplayName(self._ptr, value)

    DisplayName = property(_getDisplayName, _setDisplayName)

    # TODO: is BusNames too redundant to keep?
    # def GetBusNames(self) -> List[str]:
    #     return self._get_string_array(self._lib.Alt_CE_Get_BusNames, self._ptr)

    # def SetBusNames(self, value: List[AnyStr]):
    #     value, value_ptr, value_count = self._prepare_string_array(value)
    #     self._lib.Alt_CE_Set_BusNames(self._ptr, value_ptr, value_count)

    # BusNames = property(GetBusNames, SetBusNames)

    def Handle(self) -> int:
        return self._lib.Alt_CE_Get_Handle(self._ptr)

    def NumConductors(self) -> int:
        return self._lib.Alt_CE_Get_NumConductors(self._ptr)

    def NumPhases(self) -> int:
        return self._lib.Alt_CE_Get_NumPhases(self._ptr)

    def NumTerminals(self) -> int:
        return self._lib.Alt_CE_Get_NumTerminals(self._ptr)

    def NumControllers(self) -> int:
        return self._lib.Alt_CE_Get_NumControllers(self._ptr)

    def OCPDevice(self) -> Union[DSSObj, None]:
        return self._get_obj_from_ptr(self._lib.Alt_CE_Get_OCPDevice(self._ptr))

    def OCPDeviceIndex(self) -> int:
        return self._lib.Alt_CE_Get_OCPDeviceIndex(self._ptr)

    def OCPDeviceType(self) -> OCPDevType:
        return OCPDevType(self._lib.Alt_CE_Get_OCPDeviceType(self._ptr))

    def IsIsolated(self) -> bool:
        return self._lib.Alt_CE_Get_IsIsolated(self._ptr) != 0

    def HasOCPDevice(self) -> bool:
        return self._lib.Alt_CE_Get_HasOCPDevice(self._ptr) != 0

    def HasSwitchControl(self) -> bool:
        return self._lib.Alt_CE_Get_HasSwitchControl(self._ptr) != 0

    def HasVoltControl(self) -> bool:
        return self._lib.Alt_CE_Get_HasVoltControl(self._ptr) != 0

    def IsOpen(self, terminal: int, phase: int) -> bool:
        return self._lib.Alt_CE_IsOpen(self._ptr, terminal, phase) != 0

    def MaxCurrent(self, terminal: int) -> float:
        '''
        Returns the maximum current (magnitude) at the specificed terminal. 
        Use -1 as terminal to get the value across all terminals.
        '''
        return self._lib.Alt_CE_MaxCurrent(self._ptr, terminal)

    def Open(self, terminal: int, phase: int) -> None:
        self._lib.Alt_CE_Open(self._ptr, terminal, phase)

    def Close(self, terminal: int, phase: int) -> None:
        self._lib.Alt_CE_Close(self._ptr, terminal, phase)

    def NodeOrder(self) -> Int32Array:
        return self._get_int32_array(self._lib.Alt_CE_Get_NodeOrder, self._ptr)

    def NodeRef(self) -> Int32Array:
        return self._get_int32_array(self._lib.Alt_CE_Get_NodeRef, self._ptr)

    def ComplexSeqVoltages(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_ComplexSeqVoltages, self._ptr)

    def ComplexSeqCurrents(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_ComplexSeqCurrents, self._ptr)

    def Currents(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Currents, self._ptr)

    def Voltages(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Voltages, self._ptr)

    def Losses(self) -> complex:
        '''Total (complex) losses in the element, in VA (watts, vars)'''
        return self._get_fcomplex128_simple(self._lib.Alt_CE_Get_Losses, self._ptr)

    def PhaseLosses(self) -> ComplexArray:
        '''Complex array of losses (kVA) by phase'''
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_PhaseLosses, self._ptr)

    def Powers(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Powers, self._ptr)

    def SeqCurrents(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_SeqCurrents, self._ptr)

    def SeqPowers(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_SeqPowers, self._ptr)

    def SeqVoltages(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_SeqVoltages, self._ptr)

    def Residuals(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_Residuals, self._ptr)

    def Yprim(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_Yprim, self._ptr)

    def VoltagesMagAng(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_VoltagesMagAng, self._ptr)

    def TotalPowers(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CE_Get_TotalPowers, self._ptr)


class CircuitElementBatchMixin:
    __slots__ = ()

    def GUID(self) -> str:
        '''GUID/UUID for each object. Currently used only in the CIM-related methods.'''
        return [self._get_string(self._lib.Alt_CE_Get_GUID(ptr)) for ptr in self._unpack()]

    def Handle(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_Handle")

    def NumConductors(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_NumConductors")

    def NumPhases(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_NumPhases")

    def NumTerminals(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_NumTerminals")

    def NumControllers(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_NumControllers")

    def OCPDevice(self) -> List[Union[DSSObj, None]]: #TODO
        return self._get_obj_from_ptr(self._lib.Alt_CE_Get_OCPDevice(self._ptr))

    def OCPDeviceIndex(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_CE_Get_OCPDeviceIndex")

    def OCPDeviceType(self) -> OCPDevType:
        return [
            OCPDevType(val) for val in self._get_batch_int32_func("Alt_CE_Get_OCPDeviceType")
        ]

    def MaxCurrent(self, terminal: int) -> float:
        '''
        Returns the maximum current (magnitude) at the specificed terminal for all elements in this batch. 
        Use -1 as terminal to get the value across all terminals.
        '''
        return self._get_batch_float_int32_func("Alt_CE_MaxCurrent", terminal)
    
    def IsIsolated(self) -> BoolArray:
        return self._get_batch_int32_func("Alt_CE_Get_IsIsolated").astype(bool)

    def HasOCPDevice(self) -> bool:
        return self._get_batch_int32_func("Alt_CE_Get_HasOCPDevice").astype(bool)

    def HasSwitchControl(self) -> bool:
        return self._get_batch_int32_func("Alt_CE_Get_HasSwitchControl").astype(bool)

    def HasVoltControl(self) -> bool:
        return self._get_batch_int32_func("Alt_CE_Get_HasVoltControl").astype(bool)

    def Powers(self) -> ComplexArray:
        '''Complex array of powers (kVA) into each conductor of each terminal, of each element in the batch.'''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Powers, *self._get_ptr_cnt())

    def Losses(self) -> ComplexArray:
        '''Total losses for each element, complex VA (watts, vars)'''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Losses, *self._get_ptr_cnt())

    def PhaseLosses(self) -> ComplexArray:
        '''Complex array of losses (kVA) by phase, for each element'''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_PhaseLosses, self._ptr)

    def TotalPowers(self) -> ComplexArray:
        '''
        Returns an array with the total powers (complex, kVA) at all terminals of the circuit elements in this batch.

        The resulting array is equivalent to concatenating the TotalPowers for each element.        
        '''
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_TotalPowers, *self._get_ptr_cnt())

    def SeqPowers(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_SeqPowers, *self._get_ptr_cnt())

    def SeqCurrents(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_SeqCurrents, *self._get_ptr_cnt())
        
    def ComplexSeqCurrents(self) -> ComplexArray:
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_ComplexSeqCurrents, *self._get_ptr_cnt())

    def Currents(self) -> ComplexArray:
        return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Currents, *self._get_ptr_cnt())

    def CurrentsMagAng(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CEBatch_Get_CurrentsMagAng, *self._get_ptr_cnt())

    # def Voltages(self) -> ComplexArray:
    #     return self._get_fcomplex128_array(self._lib.Alt_CEBatch_Get_Voltages, *self._get_ptr_cnt())

    # def SeqVoltages(self) -> Float64Array:
    #     return self._get_float64_array(self._lib.Alt_CEBatch_Get_SeqVoltages, *self._get_ptr_cnt())

    # def VoltagesMagAng(self) -> Float64Array:
    #     return self._get_float64_array(self._lib.Alt_CEBatch_Get_VoltagesMagAng, *self._get_ptr_cnt())

    # def ComplexSeqVoltages(self) -> ComplexArray:
    #     return self._get_fcomplex128_array(self._lib.Alt_CE_Get_ComplexSeqVoltages, self._ptr)



class ElementHasRegistersMixin:
    __slots__ = ()
    _extra_slots = []

    def RegisterNames(self) -> List[str]:
        return self._get_string_array(self._lib.Alt_CE_Get_RegisterNames, self._ptr)

    def RegisterValues(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_CE_Get_RegisterValues, self._ptr)

    def RegistersDict(self) -> Dict[str, float]:
        return dict(*zip(self.RegisterNames(), self.RegisterValues()))


class PCElementMixin:
    __slots__ = ()
    _extra_slots = []

    def VariableNames(self) -> List[str]:
        return self._get_string_array(self._lib.Alt_PCE_Get_VariableNames, self._ptr)

    def VariableValues(self) -> Float64Array:
        return self._get_float64_array(self._lib.Alt_PCE_Get_VariableValues, self._ptr)
    
    def VariablesDict(self) -> Dict[str, float]:
        return dict(*zip(self.VariableNames(), self.VariableValues()))

    def GetVariableValue(self, varIdxName: Union[AnyStr, int]) -> float:
        if isinstance(varIdxName, int):
            return self._lib.Alt_PCE_Get_VariableValue(self._ptr, varIdxName)
        else:
            if not isinstance(varIdxName, bytes):
                varIdxName = varIdxName.encode(self._api_util.codec)

            return self._lib.Alt_PCE_Get_VariableValueS(self._ptr, varIdxName)


    def SetVariableValue(self, varIdxName: Union[AnyStr, int], value: float):
        if isinstance(varIdxName, int):
            self._lib.Alt_PCE_Set_VariableValue(self._ptr, varIdxName, value)
        else:
            if not isinstance(varIdxName, bytes):
                varIdxName = varIdxName.encode(self._api_util.codec)

            self._lib.Alt_PCE_Set_VariableValueS(self._ptr, varIdxName, value)

    def EnergyMeter(self) -> DSSObj:
        return self._get_obj_from_ptr(self._lib.Alt_PCE_Get_EnergyMeter(self._ptr))

    def EnergyMeterName(self) -> str:
        return self._get_string(self._lib.Alt_PCE_Get_EnergyMeterName(self._ptr))


class PCElementBatchMixin:
    __slots__ = ()

    def EnergyMeter(self) -> List[DSSObj]:
        return [self._get_obj_from_ptr(self._lib.Alt_PCE_Get_EnergyMeter(ptr)) for ptr in self._unpack()]

    def EnergyMeterName(self) -> List[str]:
        return [self._get_string(self._lib.Alt_PCE_Get_EnergyMeterName(ptr)) for ptr in self._unpack()]


class PDElementMixin:
    __slots__ = ()
    _extra_slots = []

    def EnergyMeter(self) -> DSSObj:
        return self._get_obj_from_ptr(self._lib.Alt_PDE_Get_EnergyMeter(self._ptr))

    def EnergyMeterName(self) -> str:
        return self._get_string(self._lib.Alt_PDE_Get_EnergyMeterName(self._ptr))

    def IsShunt(self) -> bool:
        return self._lib.Alt_PDE_Get_IsShunt(self._ptr) != 0

    def AccumulatedL(self) -> float:
        return self._lib.Alt_PDE_Get_AccumulatedL(self._ptr)

    def Lambda(self) -> float:
        return self._lib.Alt_PDE_Get_Lambda(self._ptr)

    def NumCustomers(self) -> int:
        return self._lib.Alt_PDE_Get_NumCustomers(self._ptr)

    def ParentPDElement(self) -> DSSObj:
        return self._lib.Alt_PDE_Get_ParentPDElement(self._ptr)

    def TotalCustomers(self) -> int:
        return self._lib.Alt_PDE_Get_TotalCustomers(self._ptr)

    def FromTerminal(self) -> int:
        return self._lib.Alt_PDE_Get_FromTerminal(self._ptr)

    def TotalMiles(self) -> float:
        return self._lib.Alt_PDE_Get_TotalMiles(self._ptr)

    def SectionID(self) -> int:
        return self._lib.Alt_PDE_Get_SectionID(self._ptr)

    def pctNorm(self, allNodes=False) -> float:
        '''
        '''
        return self._lib.Alt_PDE_Get_pctNorm(self._ptr, allNodes)

    def pctEmerg(self, allNodes=False) -> float:
        '''
        '''
        return self._lib.Alt_PDE_Get_pctEmerg(self._ptr, allNodes)


class PDElementBatchMixin:
    __slots__ = ()

    def EnergyMeter(self) -> List[DSSObj]:
        return [self._get_obj_from_ptr(self._lib.Alt_PDE_Get_EnergyMeter(ptr)) for ptr in self._unpack()]

    def EnergyMeterName(self) -> List[str]:
        return [self._get_string(self._lib.Alt_PDE_Get_EnergyMeterName(ptr)) for ptr in self._unpack()]

    def IsShunt(self) -> List[bool]:
        return [self._lib.Alt_PDE_Get_IsShunt(ptr) != 0 for ptr in self._unpack()]

    def AccumulatedL(self) -> Float64Array:
        return self._get_batch_float_func("Alt_PDE_Get_AccumulatedL")

    def Lambda(self) -> Float64Array:
        return self._get_batch_float_func("Alt_PDE_Get_Lambda")

    def NumCustomers(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_PDE_Get_NumCustomers")

    def ParentPDElement(self) -> List[DSSObj]:
        return [self._lib.Alt_PDE_Get_ParentPDElement(self._ptr) for ptr in self._unpack()]

    def TotalCustomers(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_PDE_Get_TotalCustomers")

    def FromTerminal(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_PDE_Get_FromTerminal")

    def TotalMiles(self) -> Float64Array:
        return self._get_batch_float_func("Alt_PDE_Get_TotalMiles")

    def SectionID(self) -> Int32Array:
        return self._get_batch_int32_func("Alt_PDE_Get_SectionID")


class LoadShapeObjMixin:
    # TODO: integrate Alt_LoadShape_Set_Points
    __slots__ = ()
    _extra_slots = []

    def UseFloat32(self):
        '''
        If this loadshape is using float64/double precision internal data, use this function
        to convert to float32/single precision. If the data is not owned by the loadshape,
        this operation is not allowed.
        '''
        self._lib.Alt_LoadShape_UseFloat32(self._ptr)

    def UseFloat64(self):
        '''
        If this loadshape is using float32/single precision internal data, use this function
        to convert to float64/double precision. If the data is not owned by the loadshape,
        this operation is not allowed.
        '''
        self._lib.Alt_LoadShape_UseFloat64(self._ptr)


class LoadShapeBatchMixin:
    __slots__ = ()

    def UseFloat32(self):
        '''
        If the loadshapes are using float64/double precision internal data, use this function
        to convert to float32/single precision. If the data is not owned by the loadshape,
        this operation is not allowed.
        '''
        for ptr in self._unpack():
            self._lib.Alt_LoadShape_UseFloat32(ptr)

    def UseFloat64(self):
        '''
        If the loadshape are using float32/single precision internal data, use this function
        to convert to float64/double precision. If the data is not owned by the loadshape,
        this operation is not allowed.
        '''
        for ptr in self._unpack():
            self._lib.Alt_LoadShape_UseFloat64(ptr)


class MonitorObjMixin:
    #TODO: dataframe
    __slots__ = ()
    _extra_slots = []

    def Show(self):
        self._lib.Alt_Monitor_Show(self._ptr)

    def Header(self) -> List[str]:
        return self._get_string_array(self._lib.Alt_Monitor_Get_Header, self._ptr)

    def ByteStream(self) -> Int8Array:
        return self._get_int8_array(self._lib.Alt_Monitor_Get_ByteStream, self._ptr)

    def FileName(self) -> str:
        return self._get_string(self._lib.Alt_Monitor_Get_FileName(self._ptr))

    def SampleCount(self) -> int:
        return self._lib.Alt_Monitor_Get_SampleCount(self._ptr)

    def NumChannels(self) -> int:
        return self._lib.Alt_Monitor_Get_NumChannels(self._ptr)

    def RecordSize(self) -> int:
        return self._lib.Alt_Monitor_Get_RecordSize(self._ptr)

    def dblFreq(self) -> Float64Array:
        '''
        Frequency values for harmonics mode solutions.
        Empty for time mode solutions (use dblHour instead).
        '''
        return self._get_float64_array(self._lib.Alt_Monitor_Get_dblFreq, self._ptr)

    def dblHour(self) -> Float64Array:
        '''
        Time value in hours for time-sampled monitor values. 
        Empty if frequency-sampled values for harmonics solution (use dblFreq instead).
        '''
        return self._get_float64_array(self._lib.Alt_Monitor_Get_dblHour, self._ptr)

    def Channel(self, index: int) -> Float32Array:
        '''
        Array of float32 for the specified channel.
        A Save or SaveAll should be executed first, and that is done automatically by most standard solution modes.
        Channels start at index 1.
        '''
        num_channels = self.NumChannels()
        if index < 1 or index > num_channels:
            raise DSSException(
                'Monitor.Channel: Invalid channel index ({}), monitor "{}" has {} channels.'.format(
                index, self.name, num_channels
            ))
        
        buffer = self._get_int8_array(self._lib.Alt_Monitor_Get_ByteStream, self._ptr)
        
        if len(buffer) <= 1:
            return None
        record_size = buffer.view(dtype=np.int32)[2] + 2
        data = buffer[272:].view(dtype=np.float32)
        data = data.reshape((len(data) // record_size, record_size)).copy()
        return data

    def AsMatrix(self) -> Float64Array:
        '''
        Returns a copy of the matrix of this monitor, containing the hour vector, seconds vector, and all channels
        (index 2 = channel 1). If you need multiple channels, prefer using this function as it processes the monitor 
        byte-stream once.

        For harmonic solutions, the first two columns are the frequency and the harmonic, respectively.
        '''

        buffer = self._get_int8_array(self._lib.Alt_Monitor_Get_ByteStream, self._ptr)

        if len(buffer) <= 1:
            return None
        record_size = buffer.view(dtype=np.int32)[2] + 2
        data = buffer[272:].view(dtype=np.float32)
        data = data.reshape((len(data) // record_size, record_size)).copy()
        return data


    def ToDataFrame(self):
        '''
        Returns this monitor's data as a Pandas DataFrame

        Requires pandas
        '''
        try:
            import pandas as pd
        except ImportError:
            raise RuntimeError("Pandas is required to use this function")
            
        if self._lib.Solution_Get_Mode() in (SolveModes.Harmonic, SolveModes.HarmonicT):
            columns = ['frequency', 'harmonic']
        else:
            columns = ['hour', 'second']

        columns.extend(col.strip() for col in self.Header())
        data = self.AsMatrix()

        return pd.DataFrame(data, columns=columns)


class TransformerObjMixin: #TODO: batch version?
    __slots__ = ()
    _extra_slots = []

    def WindingCurrents(self) -> ComplexArray:
        '''
        All Winding currents (ph1, wdg1, wdg2,... ph2, wdg1, wdg2 ...)

        WARNING: If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24
        '''
        return self._get_fcomplex128_array(self._lib.Alt_Transformer_Get_WdgCurrents, self._ptr)

    def WindingVoltages(self, winding: int) -> ComplexArray:
        '''
        Complex array of voltages for a target winding
        
        WARNING: If the transformer has open terminal(s), results may be wrong, i.e. avoid using this
        in those situations. For more information, see https://github.com/dss-extensions/dss-extensions/issues/24
        '''
        return self._get_fcomplex128_array(self._lib.Alt_Transformer_Get_WdgVoltages, self._ptr, winding)

    def LossesByType(self) -> ComplexArray:
        '''
        Complex array with the losses by type (total losses, load losses, no-load losses), in VA
        '''
        return self._get_fcomplex128_array(self._lib.Alt_Transformer_Get_LossesByType, self._ptr)


class CircuitElementBatch(NonUniformBatch, CircuitElementBatchMixin):
    '''
    Non-uniform batch of circuit elements. Can contain distinct types, while providing 
    common functions
    '''


class PCElementBatch(NonUniformBatch, CircuitElementBatchMixin, PCElementBatchMixin, ElementHasRegistersMixin):
    '''
    Non-uniform batch of PC elements. Can contain distinct PC types, while providing 
    common functions
    '''
    pass


class PDElementBatch(NonUniformBatch, CircuitElementBatchMixin, PDElementBatchMixin):
    '''
    Non-uniform batch of PD elements. Can contain distinct PD types, while providing 
    common functions
    '''
    pass

