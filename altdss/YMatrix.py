# Copyright (c) 2016-2024 Paulo Meira
# Copyright (c) 2018-2024 DSS-Extensions contributors
from .common import Base
import numpy as np
from .types import Int32Array, ComplexArray
from typing import Tuple, List

class IYMatrix(Base):
    __slots__ = []

    def GetCompressedYMatrix(self, factor: bool = True) -> Tuple[ComplexArray, Int32Array, Int32Array]:
        '''Return as (data, indices, indptr) that can fed into `scipy.sparse.csc_matrix`'''
        
        ffi = self._api_util.ffi
        
        nBus = ffi.new('uint32_t*')
        nBus[0] = 0
        nNz = ffi.new('uint32_t*')
        nNz[0] = 0

        ColPtr = ffi.new('int32_t**')
        RowIdxPtr = ffi.new('int32_t**')
        cValsPtr = ffi.new('double**')

        self._lib.YMatrix_GetCompressedYMatrix(factor, nBus, nNz, ColPtr, RowIdxPtr, cValsPtr)

        if not nBus[0] or not nNz[0]:
            res = None
        else:
            # return as (data, indices, indptr) that can fed into scipy.sparse.csc_matrix
            res = (
                np.frombuffer(ffi.buffer(cValsPtr[0], nNz[0] * 16), dtype=complex).copy(),
                np.frombuffer(ffi.buffer(RowIdxPtr[0], nNz[0] * 4), dtype=np.int32).copy(),
                np.frombuffer(ffi.buffer(ColPtr[0], (nBus[0] + 1) * 4), dtype=np.int32).copy()
            )

        self._lib.DSS_Dispose_PInteger(ColPtr)
        self._lib.DSS_Dispose_PInteger(RowIdxPtr)
        self._lib.DSS_Dispose_PDouble(cValsPtr)
        
        self._check_for_error()

        return res

    def ZeroInjCurr(self):
        self._check_for_error(self._lib.YMatrix_ZeroInjCurr())

    def GetSourceInjCurrents(self):
        self._check_for_error(self._lib.YMatrix_GetSourceInjCurrents())

    def GetPCInjCurr(self):
        self._check_for_error(self._lib.YMatrix_GetPCInjCurr())

    def BuildYMatrixD(self, BuildOps: int, AllocateVI: bool):
        self._check_for_error(self._lib.YMatrix_BuildYMatrixD(BuildOps, AllocateVI))

    def AddInAuxCurrents(self, SType):
        self._check_for_error(self._lib.YMatrix_AddInAuxCurrents(SType))

    def GetIPointer(self):
        '''Get access to the internal Current pointer'''
        IvectorPtr = self._api_util.ffi.new('double**')
        self._check_for_error(self._lib.YMatrix_getIpointer(IvectorPtr))
        return IvectorPtr[0]

    def GetVPointer(self):
        '''Get access to the internal Voltage pointer'''
        VvectorPtr = self._api_util.ffi.new('double**')
        self._check_for_error(self._lib.YMatrix_getVpointer(VvectorPtr))
        return VvectorPtr[0]

    def SolveSystem(self, NodeV=None) -> int:
        if NodeV is not None and type(NodeV) is not np.ndarray:
            NodeV = np.array(NodeV)

        if NodeV is None:
            NodeVPtr = self._api_util.ffi.NULL
        else:
            NodeVPtr = self._api_util.ffi.cast("double *", NodeV.ctypes.data)

        result = self._check_for_error(self._lib.YMatrix_SolveSystem(NodeVPtr))
        return result

    @property
    def SystemYChanged(self) -> bool:
        return self._check_for_error(self._lib.YMatrix_Get_SystemYChanged() != 0)

    @SystemYChanged.setter
    def SystemYChanged(self, value: bool):
        self._check_for_error(self._lib.YMatrix_Set_SystemYChanged(value))

    @property
    def UseAuxCurrents(self) -> bool:
        return self._check_for_error(self._lib.YMatrix_Get_UseAuxCurrents() != 0)

    @UseAuxCurrents.setter
    def UseAuxCurrents(self, value: bool):
        self._check_for_error(self._lib.YMatrix_Set_UseAuxCurrents(value))

    # for better compatibility with OpenDSSDirect.py
    getYSparse = GetCompressedYMatrix

    @property
    def SolverOptions(self) -> int:
        '''Sparse solver options. See the enumeration SparseSolverOptions'''
        return self._lib.YMatrix_Get_SolverOptions()

    @SolverOptions.setter
    def SolverOptions(self, Value: int):
        self._lib.YMatrix_Set_SolverOptions(Value)

    def getI(self) -> List[float]:
        '''Get the data from the internal Current pointer'''
        IvectorPtr = self.GetIPointer()
        return self._api_util.ffi.unpack(IvectorPtr, 2 * (self._check_for_error(self._lib.Circuit_Get_NumNodes() + 1)))

    def getV(self) -> List[float]:
        '''Get the data from the internal Voltage pointer'''
        VvectorPtr = self.GetVPointer()
        return self._api_util.ffi.unpack(VvectorPtr, 2 * (self._check_for_error(self._lib.Circuit_Get_NumNodes() + 1)))

    def CheckConvergence(self) -> bool:
        return self._check_for_error(self._lib.YMatrix_CheckConvergence() != 0)

    def SetGeneratordQdV(self):
        self._check_for_error(self._lib.YMatrix_SetGeneratordQdV())

    @property
    def LoadsNeedUpdating(self) -> bool:
        return self._check_for_error(self._lib.YMatrix_Get_LoadsNeedUpdating() != 0)

    @LoadsNeedUpdating.setter
    def LoadsNeedUpdating(self, value: bool):
        self._check_for_error(self._lib.YMatrix_Set_LoadsNeedUpdating(value))

    @property
    def SolutionInitialized(self) -> bool:
        return self._check_for_error(self._lib.YMatrix_Get_SolutionInitialized() != 0)

    @SolutionInitialized.setter
    def SolutionInitialized(self, value: bool):
        self._check_for_error(self._lib.YMatrix_Set_SolutionInitialized(value))

    @property
    def Iteration(self) -> int:
        return self._check_for_error(self._lib.YMatrix_Get_Iteration())

    @Iteration.setter
    def Iteration(self, value: int):
        self._check_for_error(self._lib.YMatrix_Set_Iteration(value))
