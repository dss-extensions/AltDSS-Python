import re
from pathlib import Path
from pytest import FixtureRequest

def test_lib_funcs(request: FixtureRequest):
    '''
    Check if all DSS C-API functions used are present
    '''
    from dss import api_util
    lib = api_util.lib
    found = set()
    package_path = (request.path.parent.parent / 'altdss').absolute()
    print('Checking path:', package_path)
    for fn in package_path.rglob('*.py'):
        print(str(fn))
        code = Path(fn).read_text()
        for m in re.findall(r'lib\.(\w+)', code):
            if m not in found:
                print(m, end=' ')
                found.add(m)

        print()

    for m in found:
        assert hasattr(lib, m)
