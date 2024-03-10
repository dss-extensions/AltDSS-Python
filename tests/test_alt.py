try:
    from ._settings import BASE_DIR, WIN32
except ImportError:
    from _settings import BASE_DIR, WIN32


import numpy as np
np.set_printoptions(linewidth=999)
import numpy.testing as nptest
import scipy.sparse as sp

from altdss import altdss, AltDSS
from altdss.CircuitElement import CircuitElementMixin, ElementHasRegistersMixin
from altdss.PDElement import PDElementMixin
from altdss.PCElement import PCElementMixin
from altdss.LoadShape import LoadShapeObjMixin
from altdss.Monitor import MonitorObjMixin
from altdss.Transformer import TransformerObjMixin
from altdss.EnergyMeter import EnergyMeterObjMixin


def test_alt():
    altdss(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"')

    for objset in [altdss.Element, altdss.PDElement, altdss.PCElement]:
        print(objset.IsIsolated())
        (objset.Currents())
        (objset.CurrentsMagAng())
        (objset.SeqCurrents())
        (objset.ComplexSeqCurrents())
        (objset.Voltages())
        (objset.VoltagesMagAng())
        (objset.SeqVoltages())
        (objset.ComplexSeqVoltages())
        print(objset.HasOCPDevice())
        print(objset.HasSwitchControl())
        print(objset.OCPDeviceType())
        print(objset.HasVoltControl())
        print(objset.Losses())
        print(objset.TotalPowers())
        print(objset.SeqPowers())
        print(objset.NumPhases())

    altdss(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/LVTestCase/Master.dss"')

    errors = []

    dss = altdss.to_dss_python()
    for pass_num in (0, 1):
        if pass_num == 1:
            altdss('solve mode=daily')

        for cname in dss.Classes:
            cls = getattr(altdss, cname)
            if not len(cls):
                continue
            
            _ = cls.to_json()

            print(cls, cls._sync_cls_idx, len(cls))

            print('=' * 40)
            c = cls[0]
            for k in dir(c):
                if k.lower() in c._cls_prop_idx:
                    print(f'{c.FullName()}.{k}={getattr(c, k)}')

            # DSSObj
            print('Name', c.Name)
            print('FullName', c.FullName())

            if isinstance(c, CircuitElementMixin):
                print('DisplayName', c.DisplayName)
                for funcname in [
                    'Handle',
                    'NumConductors',
                    'NumPhases',
                    'NumTerminals',
                    'NumControllers',
                    'OCPDevice',
                    'OCPDeviceType',
                    'OCPDeviceIndex',
                    'IsIsolated',
                    'HasOCPDevice',
                    'HasSwitchControl',
                    'HasVoltControl',
                    'NodeOrder',
                    'NodeRef',
                    'ComplexSeqVoltages',
                    'ComplexSeqCurrents',
                    'Currents',
                    'Voltages',
                    'Losses',
                    'PhaseLosses',
                    'Powers',
                    'SeqVoltages',
                    'Residuals',
                    'YPrim',
                    'VoltagesMagAng',
                    'TotalPowers',
                ]:
                    if isinstance(c, EnergyMeterObjMixin) and funcname == 'Losses':
                        continue

                    try:
                        print(funcname, getattr(c, funcname)())
                    except:
                        errors.append((c.FullName(), funcname))
                        continue


            if isinstance(c, PCElementMixin):
                for funcname in [
                    'VariableNames',
                    'VariableValues',
                    'VariablesDict',
                    'EnergyMeter',
                    'EnergyMeterName',
                ]:
                    try:
                        print(funcname, getattr(c, funcname)())
                    except:
                        errors.append((c.FullName(), funcname))
                        continue

            if isinstance(c, PDElementMixin):
                for funcname in [
                    'EnergyMeter',
                    'EnergyMeterName',
                    'IsShunt',
                    'AccumulatedL',
                    'Lambda',
                    'NumCustomers',
                    'ParentPDElement',
                    'TotalCustomers',
                    'FromTerminal',
                    'TotalMiles',
                    'SectionID',
                    'pctNormal',
                    'pctEmergency',
                ]:
                    try:
                        print(funcname, getattr(c, funcname)())
                    except:
                        errors.append((c.FullName(), funcname))
                        continue


            if isinstance(c, LoadShapeObjMixin):
                c.PMult = c.PMult * 100000000 # force it to lose precision
                mult_f64 = c.PMult
                c.UseFloat32()
                mult_f32 = c.PMult
                nptest.assert_allclose(mult_f32, mult_f64)
                assert list(mult_f32) != list(mult_f64)
                c.UseFloat64()
                mult_f64_2 = c.PMult
                assert list(mult_f64_2) != list(mult_f64)
                assert list(mult_f32) == list(mult_f64_2)


            if isinstance(c, TransformerObjMixin):
                for funcname, *params in [
                    ('WindingCurrents',),
                    ('WindingVoltages', 1),
                    ('LossesByType',),
                ]:
                    try:
                        print(funcname, getattr(c, funcname)(*params))
                    except:
                        errors.append((c.FullName(), funcname))
                        continue


            if isinstance(c, MonitorObjMixin):
                for funcname in [
                    'Header',
                    'ByteStream',
                    'FileName',
                    'SampleCount',
                    'NumChannels',
                    'RecordSize',
                    'dblFreq',
                    'dblHour',
                    'AsMatrix',
                    'ToDataFrame'
                ]:
                    try:
                        print(funcname, getattr(c, funcname)())
                    except:
                        errors.append((c.FullName(), funcname))
                        continue

                df = c.ToDataFrame()
                header = c.Header()
                for num in range(c.NumChannels()):
                    assert all(df[header[num]] == c.Channel(num + 1)), 'Monitor should match series from DataFrame'

            if isinstance(c, EnergyMeterObjMixin):
                print('CalcCurrent', getattr(c, 'CalcCurrent'))
                print('AllocFactors', getattr(c, 'AllocFactors'))
                print('len(Sections)', len(c.Sections()))
                for funcname in [
                    'TotalCustomers',
                    'NumEndElements',
                    'NumSections',
                    # 'Sections',
                    # 'ZonePCEs',
                    # 'EndElements',
                    # 'Branches',
                    # 'Loads',
                    # 'Sequence',
                ]:
                    try:
                        print(funcname, getattr(c, funcname)())
                    except:
                        errors.append((c.FullName(), funcname))
                        continue


            if isinstance(c, ElementHasRegistersMixin):
                for funcname in [
                    'RegisterNames',
                    'RegisterValues',
                    'RegistersDict',
                ]:
                    try:
                        print(funcname, getattr(c, funcname)())
                    except:
                        errors.append((c.FullName(), funcname))
                        raise
                        continue



    print('=' * 40)
    print('=' * 40)
    print('ERRORS:', len(errors))
    print('=' * 40)
    for error in errors:
        print(*error)

    print('=' * 40)
    print('=' * 40)


def test_ymatrix_csc():
    # We accidentally left a np.complex in the ymatrix code before, 
    # so let's always check if it's working now

    altdss(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"')
    altdss.Solution.Solve()
    altdss.Settings.AdvancedTypes = True
    assert np.all(altdss.SystemY(dense=True) == sp.csc_matrix(altdss.YMatrix.GetCompressedYMatrix()))
    y_sparse1 = altdss.SystemY(dense=False)
    y_sparse2 = sp.csc_matrix(altdss.YMatrix.GetCompressedYMatrix())
    np.testing.assert_array_equal(y_sparse1.toarray(), y_sparse2.toarray())


# m1 = altdss.EnergyMeter[0]
# print(m1, m1.NumEndElements())
# print(m1, m1.CalcCurrent)
    
if __name__ == '__main__':
    test_alt()