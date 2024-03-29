# Copyright (c) 2021-2024 Paulo Meira
# Copyright (c) 2021-2024 DSS-Extensions contributors
from __future__ import annotations
from typing import Union, List, AnyStr, Optional, Iterator, TYPE_CHECKING
from typing_extensions import TypedDict, Unpack
from .types import Float64Array, Int32Array
from . import enums
from .DSSObj import IDSSObj, DSSObj
from .Batch import DSSBatch
from .ArrayProxy import BatchFloat64ArrayProxy, BatchInt32ArrayProxy
from .common import LIST_LIKE
from .CircuitElement import CircuitElementBatchMixin, CircuitElementMixin

class Sensor(DSSObj, CircuitElementMixin):
    __slots__ = DSSObj._extra_slots + CircuitElementMixin._extra_slots
    _cls_name = 'Sensor'
    _cls_idx = 49
    _cls_int_idx = {
        2,
        9,
        10,
        14,
    }
    _cls_float_idx = {
        3,
        11,
        12,
        13,
    }
    _cls_prop_idx = {
        'element': 1,
        'terminal': 2,
        'kvbase': 3,
        'clear': 4,
        'kvs': 5,
        'currents': 6,
        'kws': 7,
        'kvars': 8,
        'conn': 9,
        'deltadirection': 10,
        'pcterror': 11,
        '%error': 11,
        'weight': 12,
        'basefreq': 13,
        'enabled': 14,
        'like': 15,
    }

    def __init__(self, api_util, ptr):
       DSSObj.__init__(self, api_util, ptr)
       CircuitElementMixin.__init__(self)

    def edit(self, **kwargs: Unpack[SensorProperties]) -> Sensor:
        """
        Edit this Sensor.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context. 
        It can be seen as a shortcut to manually setting each property, or a Pythonic 
        analogous (but extended) to the DSS `Edit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    def _get_Element_str(self) -> str:
        return self._get_prop_string(1)

    def _set_Element_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_string_o(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: str
    """
    Name (Full Object name) of element to which the Sensor is connected.

    DSS property name: `Element`, DSS property index: 1.
    """

    def _get_Element(self) -> DSSObj:
        return self._get_obj(1, None)

    def _set_Element(self, value: Union[AnyStr, DSSObj], flags: enums.SetterFlags = 0):
        if isinstance(value, DSSObj) or value is None:
            self._set_obj(1, value, flags)
            return

        self._set_string_o(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: DSSObj
    """
    Name (Full Object name) of element to which the Sensor is connected.

    DSS property name: `Element`, DSS property index: 1.
    """

    def _get_Terminal(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 2)

    def _set_Terminal(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: int
    """
    Number of the terminal of the circuit element to which the Sensor is connected. 1 or 2, typically. Default is 1.

    DSS property name: `Terminal`, DSS property index: 2.
    """

    def _get_kVBase(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 3)

    def _set_kVBase(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 3, value, flags)

    kVBase = property(_get_kVBase, _set_kVBase) # type: float
    """
    Voltage base for the sensor, in kV. If connected to a 2- or 3-phase terminal, 
    specify L-L voltage. For 1-phase devices specify L-N or actual 1-phase voltage. Like many other DSS devices, default is 12.47kV.

    DSS property name: `kVBase`, DSS property index: 3.
    """

    def Clear(self, value: bool = True, flags: enums.SetterFlags = 0):
        """
        { Yes | No }. Clear=Yes clears sensor values. Should be issued before putting in a new set of measurements.

        DSS property name: `Clear`, DSS property index: 4.
        """
        self._lib.Obj_SetInt32(self._ptr, 4, value, flags)

    def _get_kVs(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 5)

    def _set_kVs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(5, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: Float64Array
    """
    Array of Voltages (kV) measured by the voltage sensor. For Delta-connected sensors, Line-Line voltages are expected. For Wye, Line-Neutral are expected.

    DSS property name: `kVs`, DSS property index: 5.
    """

    def _get_Currents(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 6)

    def _set_Currents(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(6, value, flags)

    Currents = property(_get_Currents, _set_Currents) # type: Float64Array
    """
    Array of Currents (amps) measured by the current sensor. Specify this or power quantities; not both.

    DSS property name: `Currents`, DSS property index: 6.
    """

    def _get_kWs(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 7)

    def _set_kWs(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(7, value, flags)

    kWs = property(_get_kWs, _set_kWs) # type: Float64Array
    """
    Array of Active power (kW) measurements at the sensor. Is converted into Currents along with q=[...]
    Will override any currents=[...] specification.

    DSS property name: `kWs`, DSS property index: 7.
    """

    def _get_kvars(self) -> Float64Array:
        return self._get_float64_array(self._lib.Obj_GetFloat64Array, self._ptr, 8)

    def _set_kvars(self, value: Float64Array, flags: enums.SetterFlags = 0):
        self._set_float64_array_o(8, value, flags)

    kvars = property(_get_kvars, _set_kvars) # type: Float64Array
    """
    Array of Reactive power (kvar) measurements at the sensor. Is converted into Currents along with p=[...]

    DSS property name: `kvars`, DSS property index: 8.
    """

    def _get_Conn(self) -> enums.Connection:
        return enums.Connection(self._lib.Obj_GetInt32(self._ptr, 9))

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection], flags: enums.SetterFlags = 0):
        if not isinstance(value, int):
            self._set_string_o(9, value, flags)
            return
        self._lib.Obj_SetInt32(self._ptr, 9, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: enums.Connection
    """
    Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
    Currents are always assumed to be line currents.
    If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

    DSS property name: `Conn`, DSS property index: 9.
    """

    def _get_Conn_str(self) -> str:
        return self._get_prop_string(9)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: str
    """
    Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
    Currents are always assumed to be line currents.
    If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

    DSS property name: `Conn`, DSS property index: 9.
    """

    def _get_DeltaDirection(self) -> int:
        return self._lib.Obj_GetInt32(self._ptr, 10)

    def _set_DeltaDirection(self, value: int, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 10, value, flags)

    DeltaDirection = property(_get_DeltaDirection, _set_DeltaDirection) # type: int
    """
    {1 or -1}  Default is 1:  1-2, 2-3, 3-1.  For reverse rotation, enter -1. Any positive or negative entry will suffice.

    DSS property name: `DeltaDirection`, DSS property index: 10.
    """

    def _get_pctError(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 11)

    def _set_pctError(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 11, value, flags)

    pctError = property(_get_pctError, _set_pctError) # type: float
    """
    Assumed percent error in the measurement. Default is 1.

    DSS property name: `%Error`, DSS property index: 11.
    """

    def _get_Weight(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 12)

    def _set_Weight(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 12, value, flags)

    Weight = property(_get_Weight, _set_Weight) # type: float
    """
    Weighting factor: Default is 1.

    DSS property name: `Weight`, DSS property index: 12.
    """

    def _get_BaseFreq(self) -> float:
        return self._lib.Obj_GetFloat64(self._ptr, 13)

    def _set_BaseFreq(self, value: float, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetFloat64(self._ptr, 13, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: float
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 13.
    """

    def _get_Enabled(self) -> bool:
        return self._lib.Obj_GetInt32(self._ptr, 14) != 0

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._lib.Obj_SetInt32(self._ptr, 14, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: bool
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 14.
    """

    def Like(self, value: AnyStr):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 15.
        """
        self._set_string_o(15, value)


class SensorProperties(TypedDict):
    Element: Union[AnyStr, DSSObj]
    Terminal: int
    kVBase: float
    Clear: bool
    kVs: Float64Array
    Currents: Float64Array
    kWs: Float64Array
    kvars: Float64Array
    Conn: Union[AnyStr, int, enums.Connection]
    DeltaDirection: int
    pctError: float
    Weight: float
    BaseFreq: float
    Enabled: bool
    Like: AnyStr

class SensorBatch(DSSBatch, CircuitElementBatchMixin):
    _cls_name = 'Sensor'
    _obj_cls = Sensor
    _cls_idx = 49
    __slots__ = []

    def __init__(self, api_util, **kwargs):
       DSSBatch.__init__(self, api_util, **kwargs)
       CircuitElementBatchMixin.__init__(self)

    def edit(self, **kwargs: Unpack[SensorBatchProperties]) -> SensorBatch:
        """
        Edit this Sensor batch.

        This method will try to open a new edit context (if not already open), 
        edit the properties, and finalize the edit context for objects in the batch.
        It can be seen as a shortcut to manually setting each property, or a Pythonic
        analogous (but extended) to the DSS `BatchEdit` command.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the objects.
        :return: Returns itself to allow call chaining.
        """

        self._edit(props=kwargs)
        return self


    if TYPE_CHECKING:
        def __iter__(self) -> Iterator[Sensor]:
            yield from DSSBatch.__iter__(self)

    def _get_Element_str(self) -> List[str]:
        return self._get_batch_str_prop(1)

    def _set_Element_str(self, value: Union[AnyStr, List[AnyStr]], flags: enums.SetterFlags = 0):
        self._set_batch_string(1, value, flags)

    Element_str = property(_get_Element_str, _set_Element_str) # type: List[str]
    """
    Name (Full Object name) of element to which the Sensor is connected.

    DSS property name: `Element`, DSS property index: 1.
    """

    def _get_Element(self) -> List[DSSObj]:
        return self._get_batch_obj_prop(1)

    def _set_Element(self, value: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]], flags: enums.SetterFlags = 0):
        self._set_batch_obj_prop(1, value, flags)

    Element = property(_get_Element, _set_Element) # type: List[DSSObj]
    """
    Name (Full Object name) of element to which the Sensor is connected.

    DSS property name: `Element`, DSS property index: 1.
    """

    def _get_Terminal(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 2)

    def _set_Terminal(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(2, value, flags)

    Terminal = property(_get_Terminal, _set_Terminal) # type: BatchInt32ArrayProxy
    """
    Number of the terminal of the circuit element to which the Sensor is connected. 1 or 2, typically. Default is 1.

    DSS property name: `Terminal`, DSS property index: 2.
    """

    def _get_kVBase(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 3)

    def _set_kVBase(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(3, value, flags)

    kVBase = property(_get_kVBase, _set_kVBase) # type: BatchFloat64ArrayProxy
    """
    Voltage base for the sensor, in kV. If connected to a 2- or 3-phase terminal, 
    specify L-L voltage. For 1-phase devices specify L-N or actual 1-phase voltage. Like many other DSS devices, default is 12.47kV.

    DSS property name: `kVBase`, DSS property index: 3.
    """

    def Clear(self, value: Union[bool, List[bool]] = True, flags: enums.SetterFlags = 0):
        """
        { Yes | No }. Clear=Yes clears sensor values. Should be issued before putting in a new set of measurements.

        DSS property name: `Clear`, DSS property index: 4.
        """
        self._set_batch_int32_array(4, value, flags)

    def _get_kVs(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 5)
            for x in self._unpack()
        ]

    def _set_kVs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(5, value, flags)

    kVs = property(_get_kVs, _set_kVs) # type: List[Float64Array]
    """
    Array of Voltages (kV) measured by the voltage sensor. For Delta-connected sensors, Line-Line voltages are expected. For Wye, Line-Neutral are expected.

    DSS property name: `kVs`, DSS property index: 5.
    """

    def _get_Currents(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 6)
            for x in self._unpack()
        ]

    def _set_Currents(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(6, value, flags)

    Currents = property(_get_Currents, _set_Currents) # type: List[Float64Array]
    """
    Array of Currents (amps) measured by the current sensor. Specify this or power quantities; not both.

    DSS property name: `Currents`, DSS property index: 6.
    """

    def _get_kWs(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 7)
            for x in self._unpack()
        ]

    def _set_kWs(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(7, value, flags)

    kWs = property(_get_kWs, _set_kWs) # type: List[Float64Array]
    """
    Array of Active power (kW) measurements at the sensor. Is converted into Currents along with q=[...]
    Will override any currents=[...] specification.

    DSS property name: `kWs`, DSS property index: 7.
    """

    def _get_kvars(self) -> List[Float64Array]:
        return [
            self._get_float64_array(self._lib.Obj_GetFloat64Array, x, 8)
            for x in self._unpack()
        ]

    def _set_kvars(self, value: Union[Float64Array, List[Float64Array]], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array_prop(8, value, flags)

    kvars = property(_get_kvars, _set_kvars) # type: List[Float64Array]
    """
    Array of Reactive power (kvar) measurements at the sensor. Is converted into Currents along with p=[...]

    DSS property name: `kvars`, DSS property index: 8.
    """

    def _get_Conn(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 9)

    def _set_Conn(self, value: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array], flags: enums.SetterFlags = 0):
        if isinstance(value, (str, bytes)) or (isinstance(value, LIST_LIKE) and isinstance(value[0], (str, bytes))):
            self._set_batch_string(9, value, flags)
            return

        self._set_batch_int32_array(9, value, flags)

    Conn = property(_get_Conn, _set_Conn) # type: BatchInt32ArrayProxy
    """
    Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
    Currents are always assumed to be line currents.
    If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

    DSS property name: `Conn`, DSS property index: 9.
    """

    def _get_Conn_str(self) -> List[str]:
        return self._get_batch_str_prop(9)

    def _set_Conn_str(self, value: AnyStr, flags: enums.SetterFlags = 0):
        self._set_Conn(value, flags)

    Conn_str = property(_get_Conn_str, _set_Conn_str) # type: List[str]
    """
    Voltage sensor Connection: { wye | delta | LN | LL }.  Default is wye. Applies to voltage measurement only. 
    Currents are always assumed to be line currents.
    If wye or LN, voltage is assumed measured line-neutral; otherwise, line-line.

    DSS property name: `Conn`, DSS property index: 9.
    """

    def _get_DeltaDirection(self) -> BatchInt32ArrayProxy:
        return BatchInt32ArrayProxy(self, 10)

    def _set_DeltaDirection(self, value: Union[int, Int32Array], flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(10, value, flags)

    DeltaDirection = property(_get_DeltaDirection, _set_DeltaDirection) # type: BatchInt32ArrayProxy
    """
    {1 or -1}  Default is 1:  1-2, 2-3, 3-1.  For reverse rotation, enter -1. Any positive or negative entry will suffice.

    DSS property name: `DeltaDirection`, DSS property index: 10.
    """

    def _get_pctError(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 11)

    def _set_pctError(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(11, value, flags)

    pctError = property(_get_pctError, _set_pctError) # type: BatchFloat64ArrayProxy
    """
    Assumed percent error in the measurement. Default is 1.

    DSS property name: `%Error`, DSS property index: 11.
    """

    def _get_Weight(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 12)

    def _set_Weight(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(12, value, flags)

    Weight = property(_get_Weight, _set_Weight) # type: BatchFloat64ArrayProxy
    """
    Weighting factor: Default is 1.

    DSS property name: `Weight`, DSS property index: 12.
    """

    def _get_BaseFreq(self) -> BatchFloat64ArrayProxy:
        return BatchFloat64ArrayProxy(self, 13)

    def _set_BaseFreq(self, value: Union[float, Float64Array], flags: enums.SetterFlags = 0):
        self._set_batch_float64_array(13, value, flags)

    BaseFreq = property(_get_BaseFreq, _set_BaseFreq) # type: BatchFloat64ArrayProxy
    """
    Base Frequency for ratings.

    DSS property name: `BaseFreq`, DSS property index: 13.
    """

    def _get_Enabled(self) -> List[bool]:
        return [v != 0 for v in
            self._get_batch_int32_prop(14)
        ]

    def _set_Enabled(self, value: bool, flags: enums.SetterFlags = 0):
        self._set_batch_int32_array(14, value, flags)

    Enabled = property(_get_Enabled, _set_Enabled) # type: List[bool]
    """
    {Yes|No or True|False} Indicates whether this element is enabled.

    DSS property name: `Enabled`, DSS property index: 14.
    """

    def Like(self, value: AnyStr, flags: enums.SetterFlags = 0):
        """
        Make like another object, e.g.:

        New Capacitor.C2 like=c1  ...

        DSS property name: `Like`, DSS property index: 15.
        """
        self._set_batch_string(15, value, flags)

class SensorBatchProperties(TypedDict):
    Element: Union[AnyStr, DSSObj, List[AnyStr], List[DSSObj]]
    Terminal: Union[int, Int32Array]
    kVBase: Union[float, Float64Array]
    Clear: bool
    kVs: Float64Array
    Currents: Float64Array
    kWs: Float64Array
    kvars: Float64Array
    Conn: Union[AnyStr, int, enums.Connection, List[AnyStr], List[int], List[enums.Connection], Int32Array]
    DeltaDirection: Union[int, Int32Array]
    pctError: Union[float, Float64Array]
    Weight: Union[float, Float64Array]
    BaseFreq: Union[float, Float64Array]
    Enabled: bool
    Like: AnyStr

#TODO: warn that begin_edit=False with extra params will be ignored?

class ISensor(IDSSObj, SensorBatch):
    __slots__ = IDSSObj._extra_slots

    def __init__(self, iobj):
        IDSSObj.__init__(self, iobj, Sensor, SensorBatch)
        SensorBatch.__init__(self, self._api_util, sync_cls_idx=Sensor._cls_idx)

    if TYPE_CHECKING:
        def __getitem__(self, name_or_idx: Union[AnyStr, int]) -> Sensor:
            return self.find(name_or_idx)

        def batch(self, **kwargs) -> SensorBatch: #TODO: add annotation to kwargs (specialized typed dict)
            """
            Creates a new batch handler of (existing) Sensor objects
            """
            return self._batch_cls(self._api_util, **kwargs)

        def __iter__(self) -> Iterator[Sensor]:
            yield from SensorBatch.__iter__(self)

        
    def new(self, name: AnyStr, *, begin_edit: Optional[bool] = None, activate=False, **kwargs: Unpack[SensorProperties]) -> Sensor:
        """
        Creates a new Sensor.

        :param name: The object's name is a required positional argument.

        :param activate: Activation (setting `activate` to true) is useful for integration with the classic API, and some internal OpenDSS commands.
        If you interact with this object only via the Alt API, no need to activate it (due to performance costs).

        :param begin_edit: This controls how the edit context is left after the object creation:
        - `True`: The object will be left in the edit state, requiring an `end_edit` call or equivalent.
        - `False`: No edit context is started.
        - `None`: If no properties are passed as keyword arguments, the object will be left in the edit state (assumes the user will fill the properties from Python attributes). Otherwise, the internal edit context will be finalized.

        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :return: Returns the new DSS object, wrapped in Python.

        Note that, to make it easier for new users where the edit context might not be too relevant, AltDSS automatically opens/closes edit contexts for single properties if the object is not in the edit state already.
        """
        return self._new(name, begin_edit=begin_edit, activate=activate, props=kwargs)

    def batch_new(self, names: Optional[List[AnyStr]] = None, *, df = None, count: Optional[int] = None, begin_edit: Optional[bool] = None, **kwargs: Unpack[SensorBatchProperties]) -> SensorBatch:
        """
        Creates a new batch of Sensor objects

        Either `names`, `count` or `df` is required. 

        :param begin_edit: The argument `begin_edit` indicates if the user want to leave the elements in the edit state, and requires a call to `end_edit()` or equivalent. The default `begin_edit` is set to `None`. With `None`, the behavior will be adjusted according the default of how the batch is created.
        :param **kwargs: Pass keyword arguments equivalent to the DSS properties of the object.
        :param names: When using a list of names, each new object will match the names from this list. `begin_edit` defaults to `True` if no arguments for properties were passed, `False` otherwise.
        :param count: When using `count`, new objects will be created with based on a random prefix, with an increasing integer up to `count`. `begin_edit` defaults to `True` if no arguments for properties were passed, `False` otherwise.
        :param df: Currently **EXPERIMENTAL AND LIMITED**, tries to get the columns from a dataframe to populate the names and the DSS properties. `begin_edit` defaults to `False`.
        :return: Returns the new batch of DSS objects, wrapped in Python.

        Note that, to make it easier for new users where the edit context might not be too relevant, AltDSS automatically opens/closes edit contexts for single properties if the object is not in the edit state already.
        """
        return self._batch_new_aux(names=names, df=df, count=count, begin_edit=begin_edit, props=kwargs)
