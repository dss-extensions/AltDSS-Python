import numpy as np

class BatchFloat64ArrayProxy:
    def __init__(self, batch, idx):
        self._batch = batch
        self._idx = idx
        self._lib = batch._api_util.lib

    def to_array(self):
        return self._batch._get_batch_float_prop(self._idx)

    def to_list(self):
        return self._batch._get_batch_float_prop_as_list(self._idx)

    def __call__(self):
        return self.to_array()

    def __len__(self) -> int:
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

    def __iter__(self):
        return self.to_array().__iter__()

    def __array__(self):
        return self.to_array()

    def __iadd__(self, other, flags=0):
        '''
        Inplace modification of the array. When possible, it runs the operation in the engine.

        Use `iadd` instead of the `+=` operator in order to specify SetterFlags.
        '''
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Float64(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Increment,
                other,
                flags
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data, data_ptr, _ = batch._prepare_float64_array(other)
        batch._lib.Batch_Float64Array(
            *ptr_cnt,
            self._idx,
            self._lib.BatchOperation_Increment,
            data_ptr,
            flags
        )
        batch._check_for_error()
        return self

    def __isub__(self, other, flags=0):
        '''
        Inplace modification of the array. When possible, it runs the operation in the engine.

        Use `isub` instead of the `-=` operator in order to specify SetterFlags.
        '''
        return self.__iadd__(-np.asarray(other), flags)

    def __imul__(self, other, flags=0):
        '''
        Inplace modification of the array. When possible, it runs the operation in the engine.

        Use `imul` instead of the `*=` operator in order to specify SetterFlags.
        '''
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Float64(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                other,
                flags
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data, data_ptr, _ = batch._prepare_float64_array(other)
        batch._lib.Batch_Float64Array(
            *ptr_cnt,
            self._idx,
            self._lib.BatchOperation_Multiply,
            data_ptr,
            flags
        )
        batch._check_for_error()
        return self

    def __itruediv__(self, other, flags=0):
        '''
        Inplace modification of the array. When possible, it runs the operation in the engine.

        Use `idiv` instead of the `/=` operator in order to specify SetterFlags.
        '''
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Float64(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Divide,
                other,
                flags
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data, data_ptr, _ = batch._prepare_float64_array(other)
        batch._lib.Batch_Float64Array(
            *ptr_cnt,
            self._idx,
            self._lib.BatchOperation_Divide,
            data_ptr,
            flags
        )
        batch._check_for_error()
        return self



    idiv = __itruediv__
    imul = __imul__
    iadd = __iadd__
    isub = __isub__


class BatchInt32ArrayProxy:
    def __init__(self, batch, idx):#, kind):
        self._batch = batch
        self._idx = idx
        self._lib = batch._api_util.lib

    def to_array(self):
        return self._batch._get_batch_int32_prop(self._idx)

    def to_list(self):
        return self._batch._get_batch_int32_prop_as_list(self._idx)

    def __call__(self):
        return self.to_array()

    def __len__(self) -> int:
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

    def __iter__(self):
        return self.to_array().__iter__()

    def __array__(self):
        return self.to_array()

    def __iadd__(self, other, flags=0):
        '''
        Inplace modification of the array. When possible, it runs the operation in the engine.

        Use `iadd` instead of the `+=` operator in order to specify SetterFlags.
        '''
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Int32(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Increment,
                other,
                flags
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data, data_ptr, _ = batch._api_util.prepare_int32_array(other)
        batch._lib.Batch_Int32Array(
            *ptr_cnt,
            self._idx,
            self._lib.BatchOperation_Increment,
            data_ptr,
            flags
        )
        batch._check_for_error()
        return self

    def __isub__(self, other, flags=0):
        '''
        Inplace modification of the array. When possible, it runs the operation in the engine.

        Use `isub` instead of the `-=` operator in order to specify SetterFlags.
        '''
        return self.__iadd__(-np.asarray(other), flags)

    def __imul__(self, other, flags=0):
        '''
        Inplace modification of the array. When possible, it runs the operation in the engine.

        Use `imul` instead of the `*=` operator in order to specify SetterFlags.
        '''
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Int32(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Multiply,
                other,
                flags
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data, data_ptr, _ = batch._prepare_int32_array(other)
        batch._lib.Batch_Int32Array(
            *ptr_cnt,
            self._idx,
            self._lib.BatchOperation_Multiply,
            data_ptr,
            flags
        )
        batch._check_for_error()
        return self

    def __ifloordiv__(self, other, flags=0):
        '''
        Inplace modification of the array. When possible, it runs the operation in the engine.

        Use `idiv` instead of the `/=` operator in order to specify SetterFlags.
        '''
        batch = self._batch
        ptr_cnt = batch._get_ptr_cnt()
        if np.isscalar(other):
            self._lib.Batch_Int32(
                *ptr_cnt,
                self._idx,
                self._lib.BatchOperation_Divide,
                other,
                flags
            )
            return self

        if len(other) != len(batch):
            raise ValueError(f"Number of elements ({len(other)}) doesn't match the batch size ({len(batch)})")

        data, data_ptr, _ = batch._prepare_int32_array(other)
        self._lib.Batch_Int32Array(
            *ptr_cnt,
            self._idx,
            self._lib.BatchOperation_Divide,
            data_ptr,
            flags
        )
        batch._check_for_error()
        return self

    idiv = __floordiv__
    imul = __imul__
    iadd = __iadd__
    isub = __isub__


__all__ = ('BatchFloat64ArrayProxy', 'BatchInt32ArrayProxy')