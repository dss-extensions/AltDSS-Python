import io, json
try:
    from ._settings import BASE_DIR, WIN32
except ImportError:
    from _settings import BASE_DIR, WIN32
import numpy as np
import pandas as pd
if WIN32:
    # When running pytest, the faulthandler seems too eager to grab FPC's exceptions, even when handled
    import faulthandler
    faulthandler.disable()
    import altdss
    faulthandler.enable()
else:
    import altdss

from dss import set_case_insensitive_attributes, IDSS
from altdss import Edit, AltDSS, altdss, SetterFlags

from altdss import (
    Vsource, Transformer, LineCode, Load, Line, Capacitor,
    Connection as Conn, RegControl, LengthUnit as Units,
    LoadModel, DSSException
)
from dss_python_backend.enums import SparseSolverOptions
import pytest as pt

loads_cols = 'name,Bus1,Phases,Conn,Model,kV,kW,kvar'.split(',')
loads_data = (
    ('671', '671.1.2.3', 3, Conn.delta, LoadModel.ConstantPQ, 4.16, 1155, 660),
    ('634a', '634.1', 1, Conn.wye, LoadModel.ConstantPQ, 0.277, 160, 110),
    ('634b', '634.2', 1, Conn.wye, LoadModel.ConstantPQ, 0.277, 120, 90),
    ('634c', '634.3', 1, Conn.wye, LoadModel.ConstantPQ, 0.277, 120, 90),
    ('645', '645.2', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 170, 125),
    ('646', '646.2.3', 1, Conn.delta, LoadModel.ConstantZ, 4.16, 230, 132),
    ('692', '692.3.1', 1, Conn.delta, LoadModel.ConstantI, 4.16, 170, 151),
    ('675a', '675.1', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 485, 190),
    ('675b', '675.2', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 68, 60),
    ('675c', '675.3', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 290, 212),
    ('611', '611.3', 1, Conn.wye, LoadModel.ConstantI, 2.4, 170, 80),
    ('652', '652.1', 1, Conn.wye, LoadModel.ConstantZ, 2.4, 128, 86),
    ('670a', '670.1', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 17, 10),
    ('670b', '670.2', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 66, 38),
    ('670c', '670.3', 1, Conn.wye, LoadModel.ConstantPQ, 2.4, 117, 68),
)

lines_cols = 'name,Phases,Bus1,Bus2,LineCode,Length,Units'.split(',')
lines_data = (
    ('650632', 3, 'RG60.1.2.3', '632.1.2.3', 'mtx601', 2000, Units.ft),
    ('632670', 3, '632.1.2.3', '670.1.2.3', 'mtx601', 667, Units.ft),
    ('670671', 3, '670.1.2.3', '671.1.2.3', 'mtx601', 1333, Units.ft),
    ('671680', 3, '671.1.2.3', '680.1.2.3', 'mtx601', 1000, Units.ft),
    ('632633', 3, '632.1.2.3', '633.1.2.3', 'mtx602', 500, Units.ft),
    ('632645', 2, '632.3.2', '645.3.2', 'mtx603', 500, Units.ft),
    ('645646', 2, '645.3.2', '646.3.2', 'mtx603', 300, Units.ft),
    ('692675', 3, '692.1.2.3', '675.1.2.3', 'mtx606', 500, Units.ft),
    ('671684', 2, '671.1.3', '684.1.3', 'mtx604', 300, Units.ft),
    ('684611', 1, '684.3', '611.3', 'mtx605', 300, Units.ft),
    ('684652', 1, '684.1', '652.1', 'mtx607', 800, Units.ft),
)

loads_data_csv = '''name,Bus1,Phases,Conn,Model,kV,kW,kvar
671,671.1.2.3,3,delta,1,4.16,1155,660
634a,634.1,1,wye,1,0.277,160,110
634b,634.2,1,wye,1,0.277,120,90
634c,634.3,1,wye,1,0.277,120,90
645,645.2,1,wye,1,2.4,170,125
646,646.2.3,1,delta,2,4.16,230,132
692,692.3.1,1,delta,5,4.16,170,151
675a,675.1,1,wye,1,2.4,485,190
675b,675.2,1,wye,1,2.4,68,60
675c,675.3,1,wye,1,2.4,290,212
611,611.3,1,wye,5,2.4,170,80
652,652.1,1,wye,2,2.4,128,86
670a,670.1,1,wye,1,2.4,17,10
670b,670.2,1,wye,1,2.4,66,38
670c,670.3,1,wye,1,2.4,117,68
''' 

lines_data_csv = '''name,Phases,Bus1,Bus2,LineCode,Length,Units
650632,3,RG60.1.2.3,632.1.2.3,mtx601,2000,ft
632670,3,632.1.2.3,670.1.2.3,mtx601,667,ft
670671,3,670.1.2.3,671.1.2.3,mtx601,1333,ft
671680,3,671.1.2.3,680.1.2.3,mtx601,1000,ft
632633,3,632.1.2.3,633.1.2.3,mtx602,500,ft
632645,2,632.3.2,645.3.2,mtx603,500,ft
645646,2,645.3.2,646.3.2,mtx603,300,ft
692675,3,692.1.2.3,675.1.2.3,mtx606,500,ft
671684,2,671.1.3,684.1.3,mtx604,300,ft
684611,1,684.3,611.3,mtx605,300,ft
684652,1,684.1,652.1,mtx607,800,ft
'''

def setup_function():
    set_case_insensitive_attributes(True, False)

def teardown_function():
    set_case_insensitive_attributes(False, False)

def create_ref_ckt13(ref):
    ref(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"')

def create_ckt13_batch_attr(dss: AltDSS):
    dss.ClearAll()
    dss('new circuit.IEEE13Nodeckt')
    dss.Settings.AdvancedTypes = True

    # Get some local names for cleaner syntax
    LineCode = dss.LineCode
    Line = dss.Line
    Load = dss.Load
    Transformer = dss.Transformer
    Capacitor = dss.Capacitor
    RegControl = dss.RegControl

    src: Vsource = dss.Vsource[0]
    with Edit(src):
        src.basekv = 115
        src.pu = 1.0001
        src.phases = 3
        src.bus1 = 'SourceBus'
        src.angle = 30
        src.MVAsc3 = 20000
        src.MVAsc1 = 21000

    # Transformers and regulators
    Transformer.new('Sub', phases=3, windings=2, XHL=8 / 1000, buses=['SourceBus', '650'], conns=[Conn.delta, Conn.wye], kVs=[115, 4.16], kVAs=[5000, 5000], pctRs=[0.5 / 1000, 0.5 / 1000])
    for i in (1, 2, 3):
        tr = Transformer.new(f'Reg{i}', phases=1, bank='reg1', XHL=0.01, kVAs=[1666, 1666], buses=[f'650.{i}', f'RG60.{i}'], kVs=[2.4, 2.4], pctloadloss=0.01)
        RegControl.new(f'Reg{i}', transformer=tr, winding=2, vreg=122, band=2, ptratio=20, CTprim=700, R=3, X=9)

    Transformer.new('XFM1', phases=3, windings=2, XHL=2, buses=['633', '634'], conns=[Conn.wye, Conn.wye], kVs=[4.16, 0.480], kVAs=[500, 500], pctRs=[0.55, 0.55])

    # Line codes
    mtx601 = LineCode.new('mtx601', nphases=3, baseFreq=60,
        rmatrix=[0.3465, 0.1560, 0.3375, 0.1580, 0.1535, 0.3414],
        xmatrix=[1.0179, 0.5017, 1.0478, 0.4236, 0.3849, 1.0348],
        units=Units.miles
    )
    mtx602 = LineCode.new('mtx602', nphases=3, baseFreq=60,
        rmatrix=[[0.7526, 0.1580, 0.1560], [0.1580, 0.7475, 0.1535], [0.1560, 0.1535, 0.7436]],
        xmatrix=(1.1814, 0.4236, 1.1983, 0.5017, 0.3849, 1.2112),
        units=Units.miles
    )
    mtx603 = LineCode.new('mtx603', nphases=2, baseFreq=60,
        rmatrix=[1.3238, 0.2066, 0.2066, 1.3294], xmatrix=[1.3569, 0.4591, 0.4591, 1.3471],
        units=Units.miles
    )
    mtx604 = LineCode.new('mtx604', nphases=2, baseFreq=60,
        rmatrix=(1.3238, 0.2066, 0.2066, 1.3294), xmatrix=(1.3569, 0.4591, 0.4591, 1.3471),
        units=Units.miles)
    mtx605 = LineCode.new('mtx605', nphases=1, baseFreq=60, rmatrix=[1.3292], xmatrix=[1.3475], units=Units.miles)
    mtx606 = LineCode.new('mtx606', nphases=3, units=Units.miles,
        rmatrix=[0.791721, 0.318476, 0.781649, 0.28345, 0.318476, 0.791721],
        xmatrix=[0.438352, 0.0276838, 0.396697, -0.0184204, 0.0276838, 0.438352],
        cmatrix=[383.948, 0, 383.948, 0, 0, 383.948]
    )
    mtx607 = LineCode.new('mtx607', nphases=1, baseFreq=60, rmatrix=(1.3425,), xmatrix=(0.5124,), cmatrix=[236], units=Units.miles)

    # Loads
    name, bus1, phases, conn, model, kV, kW, kvar = zip(*loads_data)
    
    # Either use as a context manager, or remember to call `loads.end_edit()`
    with Edit(Load.batch_new(name), needs_begin=False) as loads:
        loads.bus1 = bus1
        loads.conn = conn
        loads.phases = phases
        loads.model = model
        loads.kV = kV
        loads.kW = kW
        loads.kvar = kvar

    # Capacitors
    Capacitor.new('Cap1', bus1='675', phases=3, kvar=600, kv=4.16)
    Capacitor.new('Cap2', bus1='611.3', phases=1, kvar=100, kv=2.4)

    # Lines
    name, phases, bus1, bus2, linecode, length, units = zip(*lines_data)

    # Either use as a context manager, or remember to call `lines.end_edit()`
    with Edit(Line.batch_new(name), needs_begin=False) as lines:
        lines.phases = phases
        lines.bus1 = bus1
        lines.bus2 = bus2
        lines.linecode = linecode
        lines.length = length
        lines.units = Units.ft # all the same

    # Switch
    Line.new('671692', phases=3, bus1='671', bus2='692', Switch=True, r1=1e-4, r0=1e-4, x1=0.0, x0=0.0, C1=0.0, C0=0.0)

    dss.Settings.VoltageBases = [115, 4.16, .48]
    dss('CalcV')
    dss.Solution.Solve()


def create_ckt13_batch_new(dss: AltDSS):
    dss.ClearAll()
    dss('new circuit.IEEE13Nodeckt')
    dss.Settings.AdvancedTypes = True

    # Get some local names for cleaner syntax
    LineCode = dss.LineCode
    Line = dss.Line
    Load = dss.Load
    Transformer = dss.Transformer
    Capacitor = dss.Capacitor
    RegControl = dss.RegControl

    src: Vsource = dss.Vsource[0]
    with Edit(src):
        src.basekv = 115
        src.pu = 1.0001
        src.phases = 3
        src.bus1 = 'SourceBus'
        src.angle = 30
        src.MVAsc3 = 20000
        src.MVAsc1 = 21000

    # Transformers and regulators
    Transformer.new('Sub', phases=3, windings=2, XHL=8 / 1000, buses=['SourceBus', '650'], conns=[Conn.delta, Conn.wye], kVs=[115, 4.16], kVAs=[5000, 5000], pctRs=[0.5 / 1000, 0.5 / 1000])
    for i in (1, 2, 3):
        tr = Transformer.new(f'Reg{i}', phases=1, bank='reg1', XHL=0.01, kVAs=[1666, 1666], buses=[f'650.{i}', f'RG60.{i}'], kVs=[2.4, 2.4], pctloadloss=0.01)
        RegControl.new(f'Reg{i}', transformer=tr, winding=2, vreg=122, band=2, ptratio=20, CTprim=700, R=3, X=9)

    Transformer.new('XFM1', phases=3, windings=2, XHL=2, buses=['633', '634'], conns=[Conn.wye, Conn.wye], kVs=[4.16, 0.480], kVAs=[500, 500], pctRs=[0.55, 0.55])

    # Line codes
    mtx601 = LineCode.new('mtx601', nphases=3, baseFreq=60,
        rmatrix=[0.3465, 0.1560, 0.3375, 0.1580, 0.1535, 0.3414],
        xmatrix=[1.0179, 0.5017, 1.0478, 0.4236, 0.3849, 1.0348],
        units=Units.miles
    )
    mtx602 = LineCode.new('mtx602', nphases=3, baseFreq=60,
        rmatrix=[[0.7526, 0.1580, 0.1560], [0.1580, 0.7475, 0.1535], [0.1560, 0.1535, 0.7436]],
        xmatrix=(1.1814, 0.4236, 1.1983, 0.5017, 0.3849, 1.2112),
        units=Units.miles
    )
    mtx603 = LineCode.new('mtx603', nphases=2, baseFreq=60,
        rmatrix=[1.3238, 0.2066, 0.2066, 1.3294], xmatrix=[1.3569, 0.4591, 0.4591, 1.3471],
        units=Units.miles
    )
    mtx604 = LineCode.new('mtx604', nphases=2, baseFreq=60,
        rmatrix=(1.3238, 0.2066, 0.2066, 1.3294), xmatrix=(1.3569, 0.4591, 0.4591, 1.3471),
        units=Units.miles)
    mtx605 = LineCode.new('mtx605', nphases=1, baseFreq=60, rmatrix=[1.3292], xmatrix=[1.3475], units=Units.miles)
    mtx606 = LineCode.new('mtx606', nphases=3, units=Units.miles,
        rmatrix=[0.791721, 0.318476, 0.781649, 0.28345, 0.318476, 0.791721],
        xmatrix=[0.438352, 0.0276838, 0.396697, -0.0184204, 0.0276838, 0.438352],
        cmatrix=[383.948, 0, 383.948, 0, 0, 383.948]
    )
    mtx607 = LineCode.new('mtx607', nphases=1, baseFreq=60, rmatrix=(1.3425,), xmatrix=(0.5124,), cmatrix=[236], units=Units.miles)

    # Loads
    name, bus1, phases, conn, model, kV, kW, kvar = zip(*loads_data)
    Load.batch_new(name, bus1=bus1, conn=conn, phases=phases, model=model, kV=kV, kW=kW, kvar=kvar)

    # Capacitors
    Capacitor.new('Cap1', bus1='675', phases=3, kvar=600, kv=4.16)
    Capacitor.new('Cap2', bus1='611.3', phases=1, kvar=100, kv=2.4)

    # Lines
    Line.batch_new(**dict(zip(lines_cols, zip(*lines_data))))

    # Switch
    Line.new('671692', phases=3, bus1='671', bus2='692', Switch=True, r1=1e-4, r0=1e-4, x1=0.0, x0=0.0, C1=0.0, C0=0.0)

    dss.Settings.VoltageBases = [115, 4.16, .48]
    dss('CalcV')
    dss.Solution.Solve()


def create_ckt13_batch_df(dss: AltDSS):
    dss.ClearAll()
    dss('new circuit.IEEE13Nodeckt')
    dss.Settings.AdvancedTypes = True

    # Get some local names for cleaner syntax
    LineCode = dss.LineCode
    Line = dss.Line
    Load = dss.Load
    Transformer = dss.Transformer
    Capacitor = dss.Capacitor
    RegControl = dss.RegControl

    src: Vsource = dss.Vsource[0]
    with Edit(src):
        src.basekv = 115
        src.pu = 1.0001
        src.phases = 3
        src.bus1 = 'SourceBus'
        src.angle = 30
        src.MVAsc3 = 20000
        src.MVAsc1 = 21000

    # Transformers and regulators
    Transformer.new('Sub', phases=3, windings=2, XHL=8 / 1000, buses=['SourceBus', '650'], conns=[Conn.delta, Conn.wye], kVs=[115, 4.16], kVAs=[5000, 5000], pctRs=[0.5 / 1000, 0.5 / 1000])
    for i in (1, 2, 3):
        tr = Transformer.new(f'Reg{i}', phases=1, bank='reg1', XHL=0.01, kVAs=[1666, 1666], buses=[f'650.{i}', f'RG60.{i}'], kVs=[2.4, 2.4], pctloadloss=0.01)
        RegControl.new(f'Reg{i}', transformer=tr, winding=2, vreg=122, band=2, ptratio=20, CTprim=700, R=3, X=9)

    Transformer.new('XFM1', phases=3, windings=2, XHL=2, buses=['633', '634'], conns=[Conn.wye, Conn.wye], kVs=[4.16, 0.480], kVAs=[500, 500], pctRs=[0.55, 0.55])

    # Line codes
    mtx601 = LineCode.new('mtx601', nphases=3, baseFreq=60,
        rmatrix=[0.3465, 0.1560, 0.3375, 0.1580, 0.1535, 0.3414],
        xmatrix=[1.0179, 0.5017, 1.0478, 0.4236, 0.3849, 1.0348],
        units=Units.miles
    )
    mtx602 = LineCode.new('mtx602', nphases=3, baseFreq=60,
        rmatrix=[[0.7526, 0.1580, 0.1560], [0.1580, 0.7475, 0.1535], [0.1560, 0.1535, 0.7436]],
        xmatrix=(1.1814, 0.4236, 1.1983, 0.5017, 0.3849, 1.2112),
        units=Units.miles
    )
    mtx603 = LineCode.new('mtx603', nphases=2, baseFreq=60,
        rmatrix=[1.3238, 0.2066, 0.2066, 1.3294], xmatrix=[1.3569, 0.4591, 0.4591, 1.3471],
        units=Units.miles
    )
    mtx604 = LineCode.new('mtx604', nphases=2, baseFreq=60,
        rmatrix=(1.3238, 0.2066, 0.2066, 1.3294), xmatrix=(1.3569, 0.4591, 0.4591, 1.3471),
        units=Units.miles)
    mtx605 = LineCode.new('mtx605', nphases=1, baseFreq=60, rmatrix=[1.3292], xmatrix=[1.3475], units=Units.miles)
    mtx606 = LineCode.new('mtx606', nphases=3, units=Units.miles,
        rmatrix=[0.791721, 0.318476, 0.781649, 0.28345, 0.318476, 0.791721],
        xmatrix=[0.438352, 0.0276838, 0.396697, -0.0184204, 0.0276838, 0.438352],
        cmatrix=[383.948, 0, 383.948, 0, 0, 383.948]
    )
    mtx607 = LineCode.new('mtx607', nphases=1, baseFreq=60, rmatrix=(1.3425,), xmatrix=(0.5124,), cmatrix=[236], units=Units.miles)

    # Loads
    with io.StringIO(loads_data_csv) as loads_csv:
        df_loads = pd.read_csv(loads_csv)

    Load.batch_new(df=df_loads)

    # Capacitors
    Capacitor.new('Cap1', bus1='675', phases=3, kvar=600, kv=4.16)
    Capacitor.new('Cap2', bus1='611.3', phases=1, kvar=100, kv=2.4)

    # Lines
    with io.StringIO(lines_data_csv) as lines_csv:
        df_lines = pd.read_csv(lines_csv)

    Line.batch_new(df=df_lines)

    # Switch
    Line.new('671692', phases=3, bus1='671', bus2='692', Switch=True, r1=1e-4, r0=1e-4, x1=0.0, x0=0.0, C1=0.0, C0=0.0)

    dss.Settings.VoltageBases = [115, 4.16, .48]
    dss('CalcV')
    dss.Solution.Solve()

# def create_from_dump(dss: AltDSS):
#     # Try exporting as dataframes from JSON and reading back.
#     # NOT RECOMMENDED, but may work in most common scenarios.

#     dss.ClearAll()
#     ref: IDSS = dss.NewContext().to_dss_python()
#     create_ref_ckt13(ref)

#     dss('new circuit.IEEE13Nodeckt')

#     # Vsource is special since the circuit always creates the first one
#     src: Vsource = dss.Vsource[0]
#     _ = ref.ActiveCircuit.Vsources.First
#     ref_vsource = json.loads(ref.ActiveCircuit.ActiveDSSElement.ToJSON())
#     # del ref_vsource['DSSClass']
#     del ref_vsource['Name']
#     with Edit(src):
#         #NOTE: this wouldn't handle properties like %..., etc.
#         for prop_name, prop_value in ref_vsource.items():
#             setattr(src, prop_name, prop_value)

#     for clsname in ref.Classes:
#         ref.SetActiveClass(clsname)
#         df = pd.read_json(ref.ActiveClass.ToJSON(), dtype_backend='pyarrow')

#         if clsname == 'Vsource':
#             if len(df) == 1:
#                 continue

#             df = df.iloc[1:]

#         if df.empty:
#             continue

#         # Handle some column issues
#         for col in ['DSSClass', 'Like']:
#             if col in df.columns:
#                 del df[col]

#         for col in df.columns:
#             c = df[col]
#             if col.lower().endswith('file') or c.isna().all():
#                 del df[col]

#             try:
#                 if (c.apply(lambda x: len(x)) == 0).all():
#                     del df[col]
#             except:
#                 pass

#             print(col, c)


#         print(clsname)

#         ObjCls = getattr(dss, clsname)
#         print(df.T)
#         print(df.dtypes)
#         ObjCls.batch_new(df=df)
       
#         dss.Settings.VoltageBases = ref.ActiveCircuit.Settings.VoltageBases
#         dss('CalcV')
#         dss.Solution.Solve()

def test_loads_no_yprim():
    from dss import dss as dss_prime

    classic = dss_prime.NewContext()
    alt = altdss.NewContext()
    alt2 = altdss.NewContext()

    # Use classic API to set kW
    create_ref_ckt13(classic)
    # classic.YMatrix.SolverOptions = SparseSolverOptions.AlwaysResetYPrimInvalid
    # classic.ActiveCircuit.Solution.Solve()
    for load in classic.ActiveCircuit.Loads:
        load.kW *= 1.1

    classic.ActiveCircuit.Solution.Solve()

    # Use proxy with AvoidFullRecalc to skip Yprim updates
    # like in the classic API
    create_ref_ckt13(alt)
    # alt.YMatrix.SolverOptions = SparseSolverOptions.AlwaysResetYPrimInvalid
    # alt.Solution.Solve()

    alt.Load.kW.imul(1.1, SetterFlags.AvoidFullRecalc)

    alt.Solution.Solve()
    np.testing.assert_array_equal(
        classic.ActiveCircuit.SystemY.view(dtype=complex).ravel(), 
        alt.SystemY(dense=True).ravel()
    )
    np.testing.assert_array_equal(classic.ActiveCircuit.AllBusVmag, alt.BusVmag())

    # Use set_kW with AvoidFullRecalc to skip Yprim updates
    # like in the classic API
    create_ref_ckt13(alt2)
    # alt2.YMatrix.SolverOptions = SparseSolverOptions.AlwaysResetYPrimInvalid
    # alt2.Solution.Solve()

    for load in alt2.Load:
        load._set_kW(load.kW * 1.1, SetterFlags.AvoidFullRecalc)

    alt2.Solution.Solve()
    np.testing.assert_array_equal(
        classic.ActiveCircuit.SystemY.view(dtype=complex).ravel(), 
        alt2.SystemY(dense=True).ravel()
    )
    np.testing.assert_array_equal(classic.ActiveCircuit.AllBusVmag, alt2.BusVmag())


def test_loads_float_na():
    alt1 = altdss.NewContext()
    alt2 = altdss.NewContext()
    create_ref_ckt13(alt1)
    create_ref_ckt13(alt2)

    # Generate some test data -- half the loads are multiplied by 1.1
    mults = np.asarray([1.1] * len(alt1.Load))
    mults[0:len(alt1.Load) // 2] = np.NaN
    kWs = alt1.Load.kW * mults

    for kW, load in zip(kWs, alt1.Load):
        if not np.isnan(kW):
            load.kW = kW

    alt2.Load._set_kW(kWs, SetterFlags.SkipNA)

    for l1, l2 in zip(alt1.Load, alt2.Load):
        assert l1.kW == l2.kW

    alt1.Solution.Solve()
    alt2.Solution.Solve()
    np.testing.assert_array_equal(alt1.BusVolts(), alt2.BusVolts())


def test_loads_int_na():
    NA = 0x7fffffff
    alt1 = altdss.NewContext()
    alt2 = altdss.NewContext()
    create_ref_ckt13(alt1)
    create_ref_ckt13(alt2)

    # Generate some test data -- increasing class numbers, alternating NA
    load_classes = np.array(range(len(alt1.Load)), dtype=np.int32)
    
    load_classes[::2] = NA

    for load_cls, load in zip(load_classes, alt1.Load):
        if load_cls != NA:
            load.Class = load_cls

    alt2.Load._set_Class(load_classes, SetterFlags.SkipNA)

    for l1, l2 in zip(alt1.Load, alt2.Load):
        assert l1.Class == l2.Class

    np.testing.assert_array_equal(l1.Class, l2.Class)


def test_loads_str_na():
    alt1 = altdss.NewContext()
    alt2 = altdss.NewContext()
    create_ref_ckt13(alt1)
    create_ref_ckt13(alt2)

    # Generate some test data -- "default" for half the loads, None for the rest
    daily_shapes = ['default'] * len(alt1.Load)
    for i in range(len(daily_shapes)):
        if i % 2 != 0:
            daily_shapes[i] = None

    for daily, load in zip(daily_shapes, alt1.Load):
        if daily is not None:
            load.Daily = daily

    alt2.Load._set_Daily(daily_shapes, SetterFlags.SkipNA)

    for l1, l2 in zip(alt1.Load, alt2.Load):
        assert l1.Daily_str == l2.Daily_str

    assert l1.Daily_str == l2.Daily_str


def test_loadshape_array_implicit_size():
    alt = altdss

    alt.Clear()
    ls = alt.LoadShape.new('test_shape')
    with pt.raises(DSSException):
        ls.PMult = [1.0, 2.0, 3.0]

    ls._set_PMult([1.0, 2.0, 3.0], SetterFlags.ImplicitSizes)
    assert tuple(ls.PMult) == (1.0, 2.0, 3.0)

    ls.end_edit()


    # TODO: maybe add a new flag to allow resizing too, if the user needs to do it?
    # ls._set_PMult([10.0, 20.0, 30.0, 40.0, 50.0], SetterFlags.ImplicitSizes)
    # assert tuple(ls.PMult) == (10.0, 20.0, 30.0, 40.0, 50.0)


def _test_create_ckt13_batch(which):
    if which == 1:
        create_ckt13_batch_attr(altdss)
    elif which == 2:
        create_ckt13_batch_new(altdss)
    elif which == 3:
        create_ckt13_batch_df(altdss)
    # else:
    #     create_from_dump(altdss)

    ref: AltDSS = altdss.NewContext()
    create_ref_ckt13(ref)

    assert altdss.Line.Name == ref.Line.Name
    assert altdss.Load.Name == ref.Load.Name
    assert [l.Phases for l in altdss.Line] == [l.Phases for l in ref.Line]
    assert [l.Length for l in altdss.Line] == [l.Length for l in ref.Line]
    assert [l.Phases for l in altdss.Load] == [l.Phases for l in ref.Load]
    assert [l.kW for l in altdss.Load] == [l.kW for l in ref.Load]
    assert [l.kvar for l in altdss.Load] == [l.kvar for l in ref.Load]
    assert altdss.Transformer.Name == ref.Transformer.Name
    assert altdss.Element.FullName() == ref.Element.FullName()

    # Check some batch properties
    line_batch = altdss.Line # .batch()
    assert [l.LineCode_str for l in ref.Line] == line_batch.linecode_str

    load_batch = altdss.Load # .batch()
    assert load_batch.conn_str == ref.Load.Conn_str
    assert load_batch.conn.to_list() == ref.Load.conn.to_list()
    
    # Should be the same result, except for some parsing detail
    assert max(abs(ref.BusVolts() - altdss.BusVolts())) < 1e-12, 'Voltages before changing loads differ'

    all_loads = altdss.Load #.batch()

    all_loads.kW += 45

    altdss.Solution.Solve()


    # for load in ref.Load:
    #     load.kW += 45
    # # Need to force-rebuild the matrices here
    # ref.Solution.BuildYMatrix(YMatrixModes.WholeMatrix, False)
    cmds = []
    for l in ref.Load:
        cmds.append(f'load.{l.Name}.kW={l.kW + 45}')

    for cmd in cmds:
        ref(cmd)

    ref.Solution.Solve()

    

    assert ref.Solution.Converged

    # Should also be the same result now
    assert max(abs(ref.BusVolts() - altdss.BusVolts())) < 1e-12, 'Voltages after changing loads differ'

def test_create_ckt13_batch_attr():
    _test_create_ckt13_batch(1)

def test_create_ckt13_batch_new():
    _test_create_ckt13_batch(2)

def test_create_ckt13_batch_df():
    _test_create_ckt13_batch(3)

# def test_create_ckt13_batch_dump_df():
#     _test_create_ckt13_batch(4)

def test_batch_set_obj():
    create_ref_ckt13(altdss)
    ls = altdss.LoadShape['default']
    assert altdss.Load.Daily_str == [''] * len(altdss.Load)
    altdss.Load.Daily = ls
    assert altdss.Load.Daily_str == ['default'] * len(altdss.Load)

if __name__ == '__main__':
    # Adjust for manually running a test-case
    test_loads_no_yprim()
