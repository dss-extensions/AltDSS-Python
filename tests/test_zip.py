import pytest
from altdss import altdss as DSS, DSSException
try:
    from ._settings import ZIP_FN
except ImportError:
    from _settings import ZIP_FN


def test_zip_redirect():
    with pytest.raises(DSSException):
        DSS.ZIP.Redirect('13Bus/IEEE13Nodeckt.dss')

    DSS.ZIP.Close()
    DSS.ZIP.Open(ZIP_FN)
    DSS.ZIP.Redirect('13Bus/IEEE13Nodeckt.dss')
    DSS.ZIP.Close()
    assert DSS.Name == 'ieee13nodeckt'
    assert DSS.NumNodes == 41
    assert DSS.NumBuses == 16


def test_zip_contains():
    with pytest.raises(DSSException):
        assert 'before open' in DSS.ZIP

    DSS.ZIP.Open(ZIP_FN)
    assert '13Bus/README.txt' in DSS.ZIP
    assert '13Bus/some/wrong/entry.txt' not in DSS.ZIP
    DSS.ZIP.Close()


def test_zip_exists():
    with pytest.raises(DSSException):
        DSS.ZIP.Open('something1/something2/something3.zip')

def test_zip_filelist():
    DSS.ZIP.Open(ZIP_FN)
    assert set(DSS.ZIP.List()) == {'13Bus/', '13Bus/IEEE13Node_BusXY.csv', '13Bus/IEEE13Nodeckt.dss', '13Bus/IEEELineCodes.DSS', '13Bus/README.txt'}
    assert DSS.ZIP.List('.*/RE.*') == ['13Bus/README.txt']

def test_zip_extract():
    DSS.ZIP.Open(ZIP_FN) 
    
    fragment = b'This is a copy of the 13Bus folder which is distributed with OpenDSS.'
    readme_txt = DSS.ZIP.Extract('13Bus/README.txt')
    assert readme_txt.startswith(fragment)

    assert DSS.ZIP['13Bus/README.txt'].startswith(readme_txt)

