mkdir -p artifacts
cd altdss-python
$PYTHON -m pip install --upgrade pip setuptools
$PYTHON -m pip install cffi wheel
$PYTHON setup.py --quiet bdist_wheel --py-limited-api cp37 --dist-dir=$ARTIFACTS_FOLDER
