# Copyright (c) 2021-2023 Paulo Meira
# Copyright (c) 2021-2023 DSS-Extensions contributors
from typing import Union, List, AnyStr, Optional
from typing_extensions import TypedDict, Unpack
from ._obj_bases import (
    CktElementMixin,
    PDElementMixin,
    BatchFloat64ArrayProxy,
    BatchInt32ArrayProxy,
    DSSObj,
    DSSBatch,
    IDSSObj,
    LIST_LIKE,
    # NotSet,
)
from .._types import Float64Array, Int32Array
from .._cffi_api_util import Base
from . import enums
from .LineSpacing import LineSpacing
from .WireData import WireData
from .LineGeometry import LineGeometry
from .LineCode import LineCode as LineCodeObj

class Line(DSSObj, CktElementMixin, PDElementMixin):
    __slots__ = CktElementMixin._extra_slots + PDElementMixin._extra_slots
    _cls_name = 'Line'
    _cls_idx = 15
    _cls_prop_idx = {
        'bus1': 1,
        'bus2': 2,
        'linecode': 3,
        'length': 4,
        'phases': 5,
        'r1': 6,
        'x1': 7,
        'r0': 8,
        'x0': 9,
        'c1': 10,
        'c0': 11,
        'rmatrix': 12,
        'xmatrix': 13,
        'cmatrix': 14,
        'switch': 15,
        'rg': 16,
        'xg': 17,
        'rho': 18,
        'geometry': 19,
        'units': 20,
        'spacing': 21,
        'wires': 22,
        'conductors': 22,
        'earthmodel': 23,
        'cncables': 24,
        'tscables': 25,
        'b1': 26,
        'b0': 27,
        'seasons': 28,
        'ratings': 29,
        'linetype': 30,
        'normamps': 31,
        'emergamps': 32,
        'faultrate': 33,
        'pctperm': 34,
        'repair': 35,
        'basefreq': 36,
        'enabled': 37,
        'like': 38,
    }

    @property
    def Bus1(self) -> str:
        """
        Name of bus to which first terminal is connected.
        Example:
        bus1=busname   (assumes all terminals connected in normal phase order)
        bus1=busname.3.1.2.0 (specify terminal to node connections explicitly)

        DSS property name: `Bus1`, DSS property index: 1.
        """
        return self._get_prop_string(1)

    @Bus1.setter
    def Bus1(self, value: AnyStr):
        self._set_string_o(1, value)

    @property
    def Bus2(self) -> str:
        """
        Name of bus to which 2nd terminal is connected.

        DSS property name: `Bus2`, DSS property index: 2.
        """
        return self._get_prop_string(2)

    @Bus2.setter
    def Bus2(self, value: AnyStr):
        self._set_string_o(2, value)

    @property
    def LineCode(self) -> str:
        """
        Name of linecode object describing line impedances.
        If you use a line code, you do not need to specify the impedances here. The line code must have been PREVIOUSLY defined. The values specified last will prevail over those specified earlier (left-to-right sequence of properties).  You can subsequently change the number of phases if symmetrical component quantities are specified.If no line code or impedance data are specified, the line object defaults to 336 MCM ACSR on 4 ft spacing.

        DSS property name: `LineCode`, DSS property index: 3.
        """
        return self._get_prop_string(3)

    @LineCode.setter
    def LineCode(self, value: Union[AnyStr, LineCodeObj]):
        if isinstance(value, DSSObj):
            self._set_obj(3, value)
            return

        self._set_string_o(3, value)

    @property
    def LineCode_obj(self) -> LineCodeObj:
        """
        Name of linecode object describing line impedances.
        If you use a line code, you do not need to specify the impedances here. The line code must have been PREVIOUSLY defined. The values specified last will prevail over those specified earlier (left-to-right sequence of properties).  You can subsequently change the number of phases if symmetrical component quantities are specified.If no line code or impedance data are specified, the line object defaults to 336 MCM ACSR on 4 ft spacing.

        DSS property name: `LineCode`, DSS property index: 3.
        """
        return self._get_obj(3, LineCodeObj)

    @LineCode_obj.setter
    def LineCode_obj(self, value: LineCodeObj):
        self._set_obj(3, value)

    @property
    def Length(self) -> float:
        """
        Length of line. Default is 1.0. If units do not match the impedance data, specify "units" property. 

        DSS property name: `Length`, DSS property index: 4.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 4)

    @Length.setter
    def Length(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 4, value)

    @property
    def Phases(self) -> int:
        """
        Number of phases, this line.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return self._lib.Obj_GetInt32(self._ptr, 5)

    @Phases.setter
    def Phases(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 5, value)

    @property
    def R1(self) -> float:
        """
        Positive-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Rmatrix.

        DSS property name: `R1`, DSS property index: 6.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 6)

    @R1.setter
    def R1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 6, value)

    @property
    def X1(self) -> float:
        """
        Positive-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.  See also Xmatrix

        DSS property name: `X1`, DSS property index: 7.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 7)

    @X1.setter
    def X1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 7, value)

    @property
    def R0(self) -> float:
        """
        Zero-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `R0`, DSS property index: 8.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 8)

    @R0.setter
    def R0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 8, value)

    @property
    def X0(self) -> float:
        """
        Zero-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `X0`, DSS property index: 9.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 9)

    @X0.setter
    def X0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 9, value)

    @property
    def C1(self) -> float:
        """
        Positive-sequence capacitance, nf per unit length.  Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Cmatrix and B1.

        DSS property name: `C1`, DSS property index: 10.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 10)

    @C1.setter
    def C1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 10, value)

    @property
    def C0(self) -> float:
        """
        Zero-sequence capacitance, nf per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.See also B0.

        DSS property name: `C0`, DSS property index: 11.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    @C0.setter
    def C0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 11, value)

    @property
    def RMatrix(self) -> Float64Array:
        """
        Resistance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition. For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `RMatrix`, DSS property index: 12.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 12)

    @RMatrix.setter
    def RMatrix(self, value: Float64Array):
        self._set_float64_array_o(12, value)

    @property
    def XMatrix(self) -> Float64Array:
        """
        Reactance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `XMatrix`, DSS property index: 13.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 13)

    @XMatrix.setter
    def XMatrix(self, value: Float64Array):
        self._set_float64_array_o(13, value)

    @property
    def CMatrix(self) -> Float64Array:
        """
        Nodal Capacitance matrix, lower triangle, nf per unit length.Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `CMatrix`, DSS property index: 14.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 14)

    @CMatrix.setter
    def CMatrix(self, value: Float64Array):
        self._set_float64_array_o(14, value)

    @property
    def Switch(self) -> bool:
        """
        {y/n | T/F}  Default= no/false.  Designates this line as a switch for graphics and algorithmic purposes. 
        SIDE EFFECT: Sets r1 = 1.0; x1 = 1.0; r0 = 1.0; x0 = 1.0; c1 = 1.1 ; c0 = 1.0;  length = 0.001; You must reset if you want something different.

        DSS property name: `Switch`, DSS property index: 15.
        """
        return self._lib.Obj_GetInt32(self._ptr, 15) != 0

    @Switch.setter
    def Switch(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 15, value)

    @property
    def Rg(self) -> float:
        """
        Carson earth return resistance per unit length used to compute impedance values at base frequency. Default is 0.01805 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Rg`, DSS property index: 16.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 16)

    @Rg.setter
    def Rg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 16, value)

    @property
    def Xg(self) -> float:
        """
        Carson earth return reactance per unit length used to compute impedance values at base frequency.  For making better frequency adjustments. Default is 0.155081 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Xg`, DSS property index: 17.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 17)

    @Xg.setter
    def Xg(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 17, value)

    @property
    def rho(self) -> float:
        """
        Default=100 meter ohms.  Earth resistivity used to compute earth correction factor. Overrides Line geometry definition if specified.

        DSS property name: `rho`, DSS property index: 18.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 18)

    @rho.setter
    def rho(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 18, value)

    @property
    def Geometry(self) -> str:
        """
        Geometry code for LineGeometry Object. Supersedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may alter number of phases. You cannot subsequently change the number of phases unless you change how the line impedance is defined.

        DSS property name: `Geometry`, DSS property index: 19.
        """
        return self._get_prop_string(19)

    @Geometry.setter
    def Geometry(self, value: Union[AnyStr, LineGeometry]):
        if isinstance(value, DSSObj):
            self._set_obj(19, value)
            return

        self._set_string_o(19, value)

    @property
    def Geometry_obj(self) -> LineGeometry:
        """
        Geometry code for LineGeometry Object. Supersedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may alter number of phases. You cannot subsequently change the number of phases unless you change how the line impedance is defined.

        DSS property name: `Geometry`, DSS property index: 19.
        """
        return self._get_obj(19, LineGeometry)

    @Geometry_obj.setter
    def Geometry_obj(self, value: LineGeometry):
        self._set_obj(19, value)

    @property
    def Units(self) -> enums.LengthUnit:
        """
        Length Units = {none | mi|kft|km|m|Ft|in|cm } Default is None - assumes length units match impedance units.

        DSS property name: `Units`, DSS property index: 20.
        """
        return enums.LengthUnit(self._lib.Obj_GetInt32(self._ptr, 20))

    @Units.setter
    def Units(self, value: Union[AnyStr, int, enums.LengthUnit]):
        if not isinstance(value, int):
            self._set_string_o(20, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 20, value)

    @property
    def Units_str(self) -> str:
        """
        Length Units = {none | mi|kft|km|m|Ft|in|cm } Default is None - assumes length units match impedance units.

        DSS property name: `Units`, DSS property index: 20.
        """
        return self._get_prop_string(20)

    @Units_str.setter
    def Units_str(self, value: AnyStr):
        self.Units = value

    @property
    def Spacing(self) -> str:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Must be used in conjunction with the Wires property.
        Specify this before the wires property.

        DSS property name: `Spacing`, DSS property index: 21.
        """
        return self._get_prop_string(21)

    @Spacing.setter
    def Spacing(self, value: Union[AnyStr, LineSpacing]):
        if isinstance(value, DSSObj):
            self._set_obj(21, value)
            return

        self._set_string_o(21, value)

    @property
    def Spacing_obj(self) -> LineSpacing:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Must be used in conjunction with the Wires property.
        Specify this before the wires property.

        DSS property name: `Spacing`, DSS property index: 21.
        """
        return self._get_obj(21, LineSpacing)

    @Spacing_obj.setter
    def Spacing_obj(self, value: LineSpacing):
        self._set_obj(21, value)

    @property
    def conductors(self) -> List[str]:
        """
        Array of WireData names for use in an overhead line constants calculation.
        Must be used in conjunction with the Spacing property.
        Specify the Spacing first, and "ncond" wires.
        May also be used to specify bare neutrals with cables, using "ncond-nphase" wires.

        DSS property name: `Wires`, DSS property index: 22.
        """
        return self._get_string_array(self._lib.Obj_GetStringArray, self._ptr, 22)

    @conductors.setter
    def conductors(self, value: List[Union[AnyStr, WireData]]):
        if value is None or len(value) == 0 or not isinstance(value[0], DSSObj):
            self._set_string_array_o(22, value)
            return

        self._set_obj_array(22, value)

    @property
    def conductors_obj(self) -> List[WireData]:
        """
        Array of WireData names for use in an overhead line constants calculation.
        Must be used in conjunction with the Spacing property.
        Specify the Spacing first, and "ncond" wires.
        May also be used to specify bare neutrals with cables, using "ncond-nphase" wires.

        DSS property name: `Wires`, DSS property index: 22.
        """
        return self._get_obj_array(22, WireData)

    @conductors_obj.setter
    def conductors_obj(self, value: List[WireData]):
        self._set_obj_array(22, value)

    @property
    def EarthModel(self) -> enums.EarthModel:
        """
        One of {Carson | FullCarson | Deri}. Default is the global value established with the Set EarthModel command. See the Options Help on EarthModel option. This is used to override the global value for this line. This option applies only when the "geometry" property is used.

        DSS property name: `EarthModel`, DSS property index: 23.
        """
        return enums.EarthModel(self._lib.Obj_GetInt32(self._ptr, 23))

    @EarthModel.setter
    def EarthModel(self, value: Union[AnyStr, int, enums.EarthModel]):
        if not isinstance(value, int):
            self._set_string_o(23, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 23, value)

    @property
    def EarthModel_str(self) -> str:
        """
        One of {Carson | FullCarson | Deri}. Default is the global value established with the Set EarthModel command. See the Options Help on EarthModel option. This is used to override the global value for this line. This option applies only when the "geometry" property is used.

        DSS property name: `EarthModel`, DSS property index: 23.
        """
        return self._get_prop_string(23)

    @EarthModel_str.setter
    def EarthModel_str(self, value: AnyStr):
        self.EarthModel = value

    @property
    def B1(self) -> float:
        """
        Alternate way to specify C1. MicroS per unit length

        DSS property name: `B1`, DSS property index: 26.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 26)

    @B1.setter
    def B1(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 26, value)

    @property
    def B0(self) -> float:
        """
        Alternate way to specify C0. MicroS per unit length

        DSS property name: `B0`, DSS property index: 27.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 27)

    @B0.setter
    def B0(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 27, value)

    @property
    def Seasons(self) -> int:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 28.
        """
        return self._lib.Obj_GetInt32(self._ptr, 28)

    @Seasons.setter
    def Seasons(self, value: int):
        self._lib.Obj_SetInt32(self._ptr, 28, value)

    @property
    def Ratings(self) -> Float64Array:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 29.
        """
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 29)

    @Ratings.setter
    def Ratings(self, value: Float64Array):
        self._set_float64_array_o(29, value)

    @property
    def LineType(self) -> enums.LineType:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 30.
        """
        return enums.LineType(self._lib.Obj_GetInt32(self._ptr, 30))

    @LineType.setter
    def LineType(self, value: Union[AnyStr, int, enums.LineType]):
        if not isinstance(value, int):
            self._set_string_o(30, value)
            return
        self._lib.Obj_SetInt32(self._ptr, 30, value)

    @property
    def LineType_str(self) -> str:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 30.
        """
        return self._get_prop_string(30)

    @LineType_str.setter
    def LineType_str(self, value: AnyStr):
        self.LineType = value

    @property
    def NormAmps(self) -> float:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 31.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 31)

    @NormAmps.setter
    def NormAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 31, value)

    @property
    def EmergAmps(self) -> float:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 32.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 32)

    @EmergAmps.setter
    def EmergAmps(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 32, value)

    @property
    def FaultRate(self) -> float:
        """
        Failure rate PER UNIT LENGTH per year. Length must be same units as LENGTH property. Default is 0.1 fault per unit length per year.

        DSS property name: `FaultRate`, DSS property index: 33.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 33)

    @FaultRate.setter
    def FaultRate(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 33, value)

    @property
    def pctPerm(self) -> float:
        """
        Percent of failures that become permanent. Default is 20.

        DSS property name: `pctPerm`, DSS property index: 34.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 34)

    @pctPerm.setter
    def pctPerm(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 34, value)

    @property
    def Repair(self) -> float:
        """
        Hours to repair. Default is 3 hr.

        DSS property name: `Repair`, DSS property index: 35.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 35)

    @Repair.setter
    def Repair(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 35, value)

    @property
    def BaseFreq(self) -> float:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 36.
        """
        return self._lib.Obj_GetFloat64(self._ptr, 36)

    @BaseFreq.setter
    def BaseFreq(self, value: float):
        self._lib.Obj_SetFloat64(self._ptr, 36, value)

    @property
    def Enabled(self) -> bool:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 37.
        """
        return self._lib.Obj_GetInt32(self._ptr, 37) != 0

    @Enabled.setter
    def Enabled(self, value: bool):
        self._lib.Obj_SetInt32(self._ptr, 37, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 38.
        """
        self._set_string_o(38, value)


class LineProperties(TypedDict):
    Bus1: AnyStr
    Bus2: AnyStr
    LineCode: Union[AnyStr, LineCodeObj]
    Length: float
    Phases: int
    R1: float
    X1: float
    R0: float
    X0: float
    C1: float
    C0: float
    RMatrix: Float64Array
    XMatrix: Float64Array
    CMatrix: Float64Array
    Switch: bool
    Rg: float
    Xg: float
    rho: float
    Geometry: Union[AnyStr, LineGeometry]
    Units: Union[AnyStr, int, enums.LengthUnit]
    Spacing: Union[AnyStr, LineSpacing]
    conductors: List[Union[AnyStr, WireData]]
    EarthModel: Union[AnyStr, int, enums.EarthModel]
    B1: float
    B0: float
    Seasons: int
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType]
    NormAmps: float
    EmergAmps: float
    FaultRate: float
    pctPerm: float
    Repair: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class LineBatch(DSSBatch):
    _cls_name = 'Line'
    _obj_cls = Line
    _cls_idx = 15


    @property
    def Bus1(self) -> List[str]:
        """
        Name of bus to which first terminal is connected.
        Example:
        bus1=busname   (assumes all terminals connected in normal phase order)
        bus1=busname.3.1.2.0 (specify terminal to node connections explicitly)

        DSS property name: `Bus1`, DSS property index: 1.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 1) 

    @Bus1.setter
    def Bus1(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(1, value)

    @property
    def Bus2(self) -> List[str]:
        """
        Name of bus to which 2nd terminal is connected.

        DSS property name: `Bus2`, DSS property index: 2.
        """

        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 2) 

    @Bus2.setter
    def Bus2(self, value: Union[AnyStr, List[AnyStr]]):
        self._set_batch_string(2, value)

    @property
    def LineCode(self) -> List[str]:
        """
        Name of linecode object describing line impedances.
        If you use a line code, you do not need to specify the impedances here. The line code must have been PREVIOUSLY defined. The values specified last will prevail over those specified earlier (left-to-right sequence of properties).  You can subsequently change the number of phases if symmetrical component quantities are specified.If no line code or impedance data are specified, the line object defaults to 336 MCM ACSR on 4 ft spacing.

        DSS property name: `LineCode`, DSS property index: 3.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 3)

    @LineCode.setter
    def LineCode(self, value: Union[AnyStr, LineCodeObj, List[AnyStr], List[LineCodeObj]]):
        self._set_batch_obj_prop(3, value)

    @property
    def LineCode_obj(self) -> List[LineCodeObj]:
        """
        Name of linecode object describing line impedances.
        If you use a line code, you do not need to specify the impedances here. The line code must have been PREVIOUSLY defined. The values specified last will prevail over those specified earlier (left-to-right sequence of properties).  You can subsequently change the number of phases if symmetrical component quantities are specified.If no line code or impedance data are specified, the line object defaults to 336 MCM ACSR on 4 ft spacing.

        DSS property name: `LineCode`, DSS property index: 3.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 3)

    @LineCode_obj.setter
    def LineCode_obj(self, value: LineCodeObj):
        self._set_batch_string(3, value)

    @property
    def Length(self) -> BatchFloat64ArrayProxy:
        """
        Length of line. Default is 1.0. If units do not match the impedance data, specify "units" property. 

        DSS property name: `Length`, DSS property index: 4.
        """
        return BatchFloat64ArrayProxy(self, 4)

    @Length.setter
    def Length(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(4, value)

    @property
    def Phases(self) -> BatchInt32ArrayProxy:
        """
        Number of phases, this line.

        DSS property name: `Phases`, DSS property index: 5.
        """
        return BatchInt32ArrayProxy(self, 5)

    @Phases.setter
    def Phases(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(5, value)

    @property
    def R1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Rmatrix.

        DSS property name: `R1`, DSS property index: 6.
        """
        return BatchFloat64ArrayProxy(self, 6)

    @R1.setter
    def R1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(6, value)

    @property
    def X1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.  See also Xmatrix

        DSS property name: `X1`, DSS property index: 7.
        """
        return BatchFloat64ArrayProxy(self, 7)

    @X1.setter
    def X1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(7, value)

    @property
    def R0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence Resistance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `R0`, DSS property index: 8.
        """
        return BatchFloat64ArrayProxy(self, 8)

    @R0.setter
    def R0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(8, value)

    @property
    def X0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence Reactance, ohms per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.

        DSS property name: `X0`, DSS property index: 9.
        """
        return BatchFloat64ArrayProxy(self, 9)

    @X0.setter
    def X0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(9, value)

    @property
    def C1(self) -> BatchFloat64ArrayProxy:
        """
        Positive-sequence capacitance, nf per unit length.  Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition. See also Cmatrix and B1.

        DSS property name: `C1`, DSS property index: 10.
        """
        return BatchFloat64ArrayProxy(self, 10)

    @C1.setter
    def C1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(10, value)

    @property
    def C0(self) -> BatchFloat64ArrayProxy:
        """
        Zero-sequence capacitance, nf per unit length. Setting any of R1, R0, X1, X0, C1, C0 forces the program to use the symmetrical component line definition.See also B0.

        DSS property name: `C0`, DSS property index: 11.
        """
        return BatchFloat64ArrayProxy(self, 11)

    @C0.setter
    def C0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(11, value)

    @property
    def RMatrix(self) -> List[Float64Array]:
        """
        Resistance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition. For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `RMatrix`, DSS property index: 12.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 12)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @RMatrix.setter
    def RMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(12, value)

    @property
    def XMatrix(self) -> List[Float64Array]:
        """
        Reactance matrix, lower triangle, ohms per unit length. Order of the matrix is the number of phases. May be used to specify the impedance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `XMatrix`, DSS property index: 13.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 13)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @XMatrix.setter
    def XMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(13, value)

    @property
    def CMatrix(self) -> List[Float64Array]:
        """
        Nodal Capacitance matrix, lower triangle, nf per unit length.Order of the matrix is the number of phases. May be used to specify the shunt capacitance of any line configuration. Using any of Rmatrix, Xmatrix, Cmatrix forces program to use the matrix values for line impedance definition.  For balanced line models, you may use the standard symmetrical component data definition instead.

        DSS property name: `CMatrix`, DSS property index: 14.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 14)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @CMatrix.setter
    def CMatrix(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(14, value)

    @property
    def Switch(self) -> List[bool]:
        """
        {y/n | T/F}  Default= no/false.  Designates this line as a switch for graphics and algorithmic purposes. 
        SIDE EFFECT: Sets r1 = 1.0; x1 = 1.0; r0 = 1.0; x0 = 1.0; c1 = 1.1 ; c0 = 1.0;  length = 0.001; You must reset if you want something different.

        DSS property name: `Switch`, DSS property index: 15.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 15)
        ]
    @Switch.setter
    def Switch(self, value: bool):
        self._set_batch_int32_array(15, value)

    @property
    def Rg(self) -> BatchFloat64ArrayProxy:
        """
        Carson earth return resistance per unit length used to compute impedance values at base frequency. Default is 0.01805 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Rg`, DSS property index: 16.
        """
        return BatchFloat64ArrayProxy(self, 16)

    @Rg.setter
    def Rg(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(16, value)

    @property
    def Xg(self) -> BatchFloat64ArrayProxy:
        """
        Carson earth return reactance per unit length used to compute impedance values at base frequency.  For making better frequency adjustments. Default is 0.155081 = 60 Hz value in ohms per kft (matches default line impedances). This value is required for harmonic solutions if you wish to adjust the earth return impedances for frequency. If not, set both Rg and Xg = 0.

        DSS property name: `Xg`, DSS property index: 17.
        """
        return BatchFloat64ArrayProxy(self, 17)

    @Xg.setter
    def Xg(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(17, value)

    @property
    def rho(self) -> BatchFloat64ArrayProxy:
        """
        Default=100 meter ohms.  Earth resistivity used to compute earth correction factor. Overrides Line geometry definition if specified.

        DSS property name: `rho`, DSS property index: 18.
        """
        return BatchFloat64ArrayProxy(self, 18)

    @rho.setter
    def rho(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(18, value)

    @property
    def Geometry(self) -> List[str]:
        """
        Geometry code for LineGeometry Object. Supersedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may alter number of phases. You cannot subsequently change the number of phases unless you change how the line impedance is defined.

        DSS property name: `Geometry`, DSS property index: 19.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 19)

    @Geometry.setter
    def Geometry(self, value: Union[AnyStr, LineGeometry, List[AnyStr], List[LineGeometry]]):
        self._set_batch_obj_prop(19, value)

    @property
    def Geometry_obj(self) -> List[LineGeometry]:
        """
        Geometry code for LineGeometry Object. Supersedes any previous definition of line impedance. Line constants are computed for each frequency change or rho change. CAUTION: may alter number of phases. You cannot subsequently change the number of phases unless you change how the line impedance is defined.

        DSS property name: `Geometry`, DSS property index: 19.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 19)

    @Geometry_obj.setter
    def Geometry_obj(self, value: LineGeometry):
        self._set_batch_string(19, value)

    @property
    def Units(self) -> BatchInt32ArrayProxy:
        """
        Length Units = {none | mi|kft|km|m|Ft|in|cm } Default is None - assumes length units match impedance units.

        DSS property name: `Units`, DSS property index: 20.
        """
        return BatchInt32ArrayProxy(self, 20)

    @Units.setter
    def Units(self, value: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(20, value)
            return
    
        self._set_batch_int32_array(20, value)

    @property
    def Units_str(self) -> str:
        """
        Length Units = {none | mi|kft|km|m|Ft|in|cm } Default is None - assumes length units match impedance units.

        DSS property name: `Units`, DSS property index: 20.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 20)

    @Units_str.setter
    def Units_str(self, value: AnyStr):
        self.Units = value

    @property
    def Spacing(self) -> List[str]:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Must be used in conjunction with the Wires property.
        Specify this before the wires property.

        DSS property name: `Spacing`, DSS property index: 21.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 21)

    @Spacing.setter
    def Spacing(self, value: Union[AnyStr, LineSpacing, List[AnyStr], List[LineSpacing]]):
        self._set_batch_obj_prop(21, value)

    @property
    def Spacing_obj(self) -> List[LineSpacing]:
        """
        Reference to a LineSpacing for use in a line constants calculation.
        Must be used in conjunction with the Wires property.
        Specify this before the wires property.

        DSS property name: `Spacing`, DSS property index: 21.
        """
        return self._get_obj_array(self._lib.Batch_GetObject, self.pointer[0], self.count[0], 21)

    @Spacing_obj.setter
    def Spacing_obj(self, value: LineSpacing):
        self._set_batch_string(21, value)

    @property
    def conductors(self) -> List[List[str]]:
        """
        Array of WireData names for use in an overhead line constants calculation.
        Must be used in conjunction with the Spacing property.
        Specify the Spacing first, and "ncond" wires.
        May also be used to specify bare neutrals with cables, using "ncond-nphase" wires.

        DSS property name: `Wires`, DSS property index: 22.
        """
        return self._get_string_ll(22)

    @conductors.setter
    def conductors(self, value: Union[List[AnyStr], List[WireData]]):
        if (not len(value)) or isinstance(value[0], (bytes, str)) or (len(value[0]) and isinstance(value[0][0], (bytes, str))):
            self._set_batch_stringlist_prop(22, value)
            return

        self._set_batch_objlist_prop(22, value)

    @property
    def conductors_obj(self) -> List[List[WireData]]:
        """
        Array of WireData names for use in an overhead line constants calculation.
        Must be used in conjunction with the Spacing property.
        Specify the Spacing first, and "ncond" wires.
        May also be used to specify bare neutrals with cables, using "ncond-nphase" wires.

        DSS property name: `Wires`, DSS property index: 22.
        """
        return self._get_obj_ll(22, WireData)

    @conductors_obj.setter
    def conductors_obj(self, value: List[WireData]):
        self._set_batch_objlist_prop(22, value)

    @property
    def EarthModel(self) -> BatchInt32ArrayProxy:
        """
        One of {Carson | FullCarson | Deri}. Default is the global value established with the Set EarthModel command. See the Options Help on EarthModel option. This is used to override the global value for this line. This option applies only when the "geometry" property is used.

        DSS property name: `EarthModel`, DSS property index: 23.
        """
        return BatchInt32ArrayProxy(self, 23)

    @EarthModel.setter
    def EarthModel(self, value: Union[AnyStr, int, enums.EarthModel, List[AnyStr], List[int], List[enums.EarthModel], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(23, value)
            return
    
        self._set_batch_int32_array(23, value)

    @property
    def EarthModel_str(self) -> str:
        """
        One of {Carson | FullCarson | Deri}. Default is the global value established with the Set EarthModel command. See the Options Help on EarthModel option. This is used to override the global value for this line. This option applies only when the "geometry" property is used.

        DSS property name: `EarthModel`, DSS property index: 23.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 23)

    @EarthModel_str.setter
    def EarthModel_str(self, value: AnyStr):
        self.EarthModel = value

    @property
    def B1(self) -> BatchFloat64ArrayProxy:
        """
        Alternate way to specify C1. MicroS per unit length

        DSS property name: `B1`, DSS property index: 26.
        """
        return BatchFloat64ArrayProxy(self, 26)

    @B1.setter
    def B1(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(26, value)

    @property
    def B0(self) -> BatchFloat64ArrayProxy:
        """
        Alternate way to specify C0. MicroS per unit length

        DSS property name: `B0`, DSS property index: 27.
        """
        return BatchFloat64ArrayProxy(self, 27)

    @B0.setter
    def B0(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(27, value)

    @property
    def Seasons(self) -> BatchInt32ArrayProxy:
        """
        Defines the number of ratings to be defined for the wire, to be used only when defining seasonal ratings using the "Ratings" property.

        DSS property name: `Seasons`, DSS property index: 28.
        """
        return BatchInt32ArrayProxy(self, 28)

    @Seasons.setter
    def Seasons(self, value: Union[int, Int32Array]):
        self._set_batch_int32_array(28, value)

    @property
    def Ratings(self) -> List[Float64Array]:
        """
        An array of ratings to be used when the seasonal ratings flag is True. It can be used to insert
        multiple ratings to change during a QSTS simulation to evaluate different ratings in lines.

        DSS property name: `Ratings`, DSS property index: 29.
        """
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 29)
            for x in self._ffi.unpack(self.pointer[0], self.count[0])
        ]

    @Ratings.setter
    def Ratings(self, value: Union[Float64Array, List[Float64Array]]):
        self._set_batch_float64_array_prop(29, value)

    @property
    def LineType(self) -> BatchInt32ArrayProxy:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 30.
        """
        return BatchInt32ArrayProxy(self, 30)

    @LineType.setter
    def LineType(self, value: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array]):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(30, value)
            return
    
        self._set_batch_int32_array(30, value)

    @property
    def LineType_str(self) -> str:
        """
        Code designating the type of line. 
        One of: OH, UG, UG_TS, UG_CN, SWT_LDBRK, SWT_FUSE, SWT_SECT, SWT_REC, SWT_DISC, SWT_BRK, SWT_ELBOW, BUSBAR

        OpenDSS currently does not use this internally. For whatever purpose the user defines. Default is OH.

        DSS property name: `LineType`, DSS property index: 30.
        """
        return self._get_string_array(self._lib.Batch_GetString, self.pointer[0], self.count[0], 30)

    @LineType_str.setter
    def LineType_str(self, value: AnyStr):
        self.LineType = value

    @property
    def NormAmps(self) -> BatchFloat64ArrayProxy:
        """
        Normal rated current.

        DSS property name: `NormAmps`, DSS property index: 31.
        """
        return BatchFloat64ArrayProxy(self, 31)

    @NormAmps.setter
    def NormAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(31, value)

    @property
    def EmergAmps(self) -> BatchFloat64ArrayProxy:
        """
        Maximum or emerg current.

        DSS property name: `EmergAmps`, DSS property index: 32.
        """
        return BatchFloat64ArrayProxy(self, 32)

    @EmergAmps.setter
    def EmergAmps(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(32, value)

    @property
    def FaultRate(self) -> BatchFloat64ArrayProxy:
        """
        Failure rate PER UNIT LENGTH per year. Length must be same units as LENGTH property. Default is 0.1 fault per unit length per year.

        DSS property name: `FaultRate`, DSS property index: 33.
        """
        return BatchFloat64ArrayProxy(self, 33)

    @FaultRate.setter
    def FaultRate(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(33, value)

    @property
    def pctPerm(self) -> BatchFloat64ArrayProxy:
        """
        Percent of failures that become permanent. Default is 20.

        DSS property name: `pctPerm`, DSS property index: 34.
        """
        return BatchFloat64ArrayProxy(self, 34)

    @pctPerm.setter
    def pctPerm(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(34, value)

    @property
    def Repair(self) -> BatchFloat64ArrayProxy:
        """
        Hours to repair. Default is 3 hr.

        DSS property name: `Repair`, DSS property index: 35.
        """
        return BatchFloat64ArrayProxy(self, 35)

    @Repair.setter
    def Repair(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(35, value)

    @property
    def BaseFreq(self) -> BatchFloat64ArrayProxy:
        """
        Base Frequency for ratings.

        DSS property name: `BaseFreq`, DSS property index: 36.
        """
        return BatchFloat64ArrayProxy(self, 36)

    @BaseFreq.setter
    def BaseFreq(self, value: Union[float, Float64Array]):
        self._set_batch_float64_array(36, value)

    @property
    def Enabled(self) -> List[bool]:
        """
        {Yes|No or True|False} Indicates whether this element is enabled.

        DSS property name: `Enabled`, DSS property index: 37.
        """
        return [v != 0 for v in 
            self._get_int32_array(self._lib.Batch_GetInt32, self.pointer[0], self.count[0], 37)
        ]
    @Enabled.setter
    def Enabled(self, value: bool):
        self._set_batch_int32_array(37, value)

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 38.
        """
        self._set_batch_string(38, value)

class LineBatchProperties(TypedDict):
    Bus1: Union[AnyStr, List[AnyStr]]
    Bus2: Union[AnyStr, List[AnyStr]]
    LineCode: Union[AnyStr, LineCodeObj, List[AnyStr], List[LineCodeObj]]
    Length: Union[float, Float64Array]
    Phases: Union[int, Int32Array]
    R1: Union[float, Float64Array]
    X1: Union[float, Float64Array]
    R0: Union[float, Float64Array]
    X0: Union[float, Float64Array]
    C1: Union[float, Float64Array]
    C0: Union[float, Float64Array]
    RMatrix: Float64Array
    XMatrix: Float64Array
    CMatrix: Float64Array
    Switch: bool
    Rg: Union[float, Float64Array]
    Xg: Union[float, Float64Array]
    rho: Union[float, Float64Array]
    Geometry: Union[AnyStr, LineGeometry, List[AnyStr], List[LineGeometry]]
    Units: Union[AnyStr, int, enums.LengthUnit, List[AnyStr], List[int], List[enums.LengthUnit], Int32Array]
    Spacing: Union[AnyStr, LineSpacing, List[AnyStr], List[LineSpacing]]
    conductors: Union[List[AnyStr], List[WireData]]
    EarthModel: Union[AnyStr, int, enums.EarthModel, List[AnyStr], List[int], List[enums.EarthModel], Int32Array]
    B1: Union[float, Float64Array]
    B0: Union[float, Float64Array]
    Seasons: Union[int, Int32Array]
    Ratings: Float64Array
    LineType: Union[AnyStr, int, enums.LineType, List[AnyStr], List[int], List[enums.LineType], Int32Array]
    NormAmps: Union[float, Float64Array]
    EmergAmps: Union[float, Float64Array]
    FaultRate: Union[float, Float64Array]
    pctPerm: Union[float, Float64Array]
    Repair: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

class ILine(IDSSObj):
    __slots__ = ()

    def __init__(self, iobj):
        super().__init__(iobj, Line, LineBatch)

    # We need this one for better type hinting
    def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Line:
        return self.find(name_or_idx)

    def new(self, name: AnyStr, begin_edit=True, activate=False, **kwargs: Unpack[LineProperties]) -> Line:
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, df = None, count: Optional[int] = None, begin_edit=True, **kwargs: Unpack[LineBatchProperties]) -> LineBatch:
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
