set -e -x
export PATH=/opt/python/cp311-cp311/bin/:$PATH

cd altdss-python
python3 -m pip install --upgrade pip wheel
python3 -m pip install 'virtualenv<21'
python3 setup.py --quiet bdist_wheel --py-limited-api cp37 --dist-dir="../artifacts"
cd ..
