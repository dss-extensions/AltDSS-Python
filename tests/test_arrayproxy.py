import json
import numpy as np
import pytest

try:
    from ._settings import BASE_DIR, WIN32
except ImportError:
    from _settings import BASE_DIR, WIN32

if WIN32:
    # When running pytest, the faulthandler seems too eager to grab FPC's exceptions, even when handled
    import faulthandler
    faulthandler.disable()
    import altdss
    faulthandler.enable()
else:
    import altdss


def test_float64_ops():
    from altdss import altdss
    altdss(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"')
    dss2 = altdss.NewContext()
    dss2(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"')


    # Test an explicit batch of 3-phase loads -- broadcast value
    load_batch = altdss.Load.batch(Phases=1)
    original_kW = load_batch.kW.to_list()
    original_Class = load_batch.Class.to_list()

    load_batch.kW = 1.123

    assert load_batch.kW.to_list() == [1.123 for l in altdss.Load if l.Phases == 1]

    load_batch.Class = 941
    assert load_batch.Class.to_list() == [941 for l in altdss.Load if l.Phases == 1]


    # Reset -- test array assigns
    altdss(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"')    

    load_batch = altdss.Load.batch(Phases=1)
    load_batch.kW = [1.123] * len(load_batch)
    assert load_batch.kW.to_list() == [1.123 for l in altdss.Load if l.Phases == 1]

    with pytest.raises(ValueError):
        load_batch.kW = [1.123] * (len(load_batch) - 1)

    load_batch.Class = [941] * len(load_batch)
    assert load_batch.Class.to_list() == [941 for l in altdss.Load if l.Phases == 1]

    with pytest.raises(ValueError):
        load_batch.Class = [941] * (len(load_batch) - 1)

    # Check with the other instance
    load_batch2 = dss2.Load.batch(Phases=1)
    
    assert len(load_batch) == len(load_batch2)
    load_batch.kW = load_batch2.kW
    load_batch.Class = load_batch2.Class

    assert load_batch.kW.to_list() == original_kW
    assert load_batch.Class.to_list() == original_Class


    # Reset and do other tests
    altdss(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"')    

    kW_for_each = [l.kW for l in altdss.Load]
    kW_ap = altdss.Load.kW

    assert list(kW_ap // 2) == [x // 2 for x in kW_for_each]
    assert list(kW_ap + 2.1) == [x + 2.1 for x in kW_for_each]
    assert list(kW_ap - 153.2) == [x - 153.2 for x in kW_for_each]
    assert len(kW_ap) == len(kW_for_each)
    assert isinstance(kW_ap.to_array(), np.ndarray)
    assert isinstance(kW_ap(), np.ndarray)
    assert kW_ap.to_list() == kW_for_each
    assert [x for x in kW_ap] == kW_for_each
    np.testing.assert_almost_equal(altdss.Load.kW / 1.1, [x / 1.1 for x in kW_for_each])
    altdss.Load.kW /= 1.1
    np.testing.assert_almost_equal(kW_ap.to_list(), [x / 1.1 for x in kW_for_each])

    with pytest.raises(ValueError):
        # Provide wrong number of elements
        altdss.Load.kW += [0.0] * (len(altdss.Load) - 1)


    altdss.Load.kW += [0.1] * (len(altdss.Load))
    altdss.Load.kW -= 0.1
    np.testing.assert_almost_equal(altdss.Load.kW, [x / 1.1 for x in kW_for_each])
    altdss.Load.kW -= [0.5] * (len(altdss.Load))
    altdss.Load.kW += 0.5
    np.testing.assert_almost_equal(altdss.Load.kW, [x / 1.1 for x in kW_for_each])

    altdss.Load.kW *= [1.0] * (len(altdss.Load))
    altdss.Load.kW *= np.ones(len(altdss.Load)) * 2.0
    np.testing.assert_almost_equal(altdss.Load.kW, [2 * (x / 1.1) for x in kW_for_each])
    with pytest.raises(ValueError):    
        altdss.Load.kW *= np.ones(len(altdss.Load) - 1) * 2.0

    altdss.Load.kW /= np.ones(len(altdss.Load)) * 2.0
    np.testing.assert_almost_equal(altdss.Load.kW, [(x / 1.1) for x in kW_for_each])
    with pytest.raises(ValueError):    
        altdss.Load.kW /= np.ones(len(altdss.Load) - 1) * 2.0


def test_int32_ops():
    from altdss import altdss
    altdss(f'redirect "{BASE_DIR}/Version8/Distrib/IEEETestCases/13Bus/IEEE13Nodeckt.dss"')    

    phases = altdss.Load.Phases.to_list()
    phases_arr = altdss.Load.Phases()
    assert len(altdss.Load) == len(altdss.Load.Phases)
    assert list(phases_arr) == phases
    assert [x for x in altdss.Load.Phases] == phases
    assert tuple(altdss.Load.Phases * 10) == tuple(10 * x for x in phases)
    np.testing.assert_equal(np.asarray(altdss.Load.Phases), phases_arr)

    np.testing.assert_equal(np.asarray(altdss.Load.Phases), phases_arr)

    altdss.Load.Class = 10
    assert altdss.Load.Class.to_list() == [10] * len(altdss.Load)
    altdss.Load.Class *= 3
    assert altdss.Load.Class.to_list() == [30] * len(altdss.Load)
    assert (altdss.Load.Class - 25).tolist() == [5] * len(altdss.Load)

    with pytest.raises(ValueError):    
        altdss.Load.Class = [2] * (len(altdss.Load) - 1)

    altdss.Load.Class = [4] * len(altdss.Load)
    assert altdss.Load.Class.to_list() == [4] * len(altdss.Load)

    assert list(altdss.Load.Class / 4) == [1] * len(altdss.Load)
    assert list(altdss.Load.Class // 4) == [1] * len(altdss.Load)
    assert list((altdss.Load.Class + 1) // 2) == [2] * len(altdss.Load)
    
    altdss.Load.Class += 1
    
    assert list(altdss.Load.batch().Class) == [5] * len(altdss.Load)

    with pytest.raises(ValueError):
        altdss.Load.Class += list(range(len(altdss.Load) - 1))


    prev_list = altdss.Load.Class.to_list()
    altdss.Load.Class += list(range(len(altdss.Load)))

    assert list(altdss.Load.batch().Class) == [i + c for i, c in zip(range(len(altdss.Load)), prev_list)]

    altdss.Load.Class -= list(range(len(altdss.Load)))

    assert list(altdss.Load.batch().Class) == prev_list

    with pytest.raises(ValueError):
        altdss.Load.Class *= [3] * (len(altdss.Load) - 1)

    altdss.Load.Class *= [3] * len(altdss.Load)
    assert list(altdss.Load.batch().Class) == [3 * x for x in prev_list]

    assert list((altdss.Load.Class) // 3) == prev_list

    altdss.Load.Class //= 2
    assert altdss.Load.Class.to_list() == [7] * len(altdss.Load)

    with pytest.raises(ValueError):
        altdss.Load.Class //= [2, 3, 4]

    altdss.Load.Class *= 6  # == 7 * 6

    altdss.Load.Class //= [2, 3] * (len(altdss.Load) // 2) + [1] # [21, 14, ..., 42]

    assert list(altdss.Load.Class) == ([21, 14] * (len(altdss.Load) // 2) + [42])

if __name__ == '__main__':
    test_int32_ops()