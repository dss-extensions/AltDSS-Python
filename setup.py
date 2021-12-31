from setuptools import setup
import re, sys, shutil, os, io
import subprocess
from dss_setup_common import PLATFORM_FOLDER, DSS_VERSIONS, DLL_SUFFIX, DLL_PREFIX
import glob

# Copy README.md contents
with io.open('README.md', encoding='utf8') as readme_md:
    long_description = readme_md.read()

# Extract version from the source files
with open('dss/__init__.py', 'r') as f:
    match = re.search("__version__ = '(.*?)'", f.read())
    package_version = match.group(1)


# Copy all the DLLs from DSS C-API
src_path = os.environ.get('SRC_DIR', '')
DSS_CAPI_PATH = os.environ.get('DSS_CAPI_PATH', os.path.join(src_path, '..', 'dss_capi'))
base_dll_path_in = os.path.join(DSS_CAPI_PATH, 'lib', PLATFORM_FOLDER)
dll_path_out = os.path.abspath(os.path.join(src_path, 'dss'))
include_path_out = os.path.join(dll_path_out, 'include')

for fn in glob.glob(os.path.join(base_dll_path_in, '*{}'.format(DLL_SUFFIX))):
    shutil.copy(fn, dll_path_out)

# Copy libs (easier to build custom extensions with a default DSS Python installation)
for fn in glob.glob(os.path.join(base_dll_path_in, '*.lib')) + glob.glob(os.path.join(base_dll_path_in, '*.a')):
    shutil.copy(fn, dll_path_out)

# Copy headers
if os.path.exists(include_path_out):
    shutil.rmtree(include_path_out)

shutil.copytree(os.path.join(DSS_CAPI_PATH, 'include'), include_path_out)

# Filter files to include in the Python package
extra_files = (
    glob.glob(os.path.join(include_path_out, '**', '*')) + 
    glob.glob(os.path.join(include_path_out, '*')) + 
    glob.glob(os.path.join(dll_path_out, '*.lib')) + 
    glob.glob(os.path.join(dll_path_out, '*.a'))
)

if os.environ.get('DSS_PYTHON_MANYLINUX', '0') == '1':
    # Do not pack .so files when building manylinux wheels
    # (auditwheel will copy them anyway)
    extra_args = dict(package_data={
        'dss': extra_files
    })
else:
    extra_args = dict(package_data={
        'dss': ['*{}'.format(DLL_SUFFIX)] + extra_files
    })

# (2019-02-24) PEP 496 didn't work, using a workaround
if (sys.version_info.major, sys.version_info.minor) < (3, 5):
    compat_requires = ['enum34']
else:
    compat_requires = []

setup(
    name="dss_python",
    description="OpenDSS bindings and tools based on the DSS C-API project",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Paulo Meira",
    author_email="pmeira@ieee.org",
    version=package_version,
    license="BSD",
    packages=['dss', 'dss.UserModels', 'dss.dss_capi_gr', 'dss.dss_capi_ir'],
    setup_requires=["cffi>=1.11.2"],
    cffi_modules=["dss_build.py:ffi_builder_{}".format(version) for version in DSS_VERSIONS] + 
        [
            'dss_build.py:ffi_builder_GenUserModel', 
            'dss_build.py:ffi_builder_PVSystemUserModel', 
            'dss_build.py:ffi_builder_StoreDynaModel', 
            'dss_build.py:ffi_builder_StoreUserModel', 
            'dss_build.py:ffi_builder_CapUserControl'
        ],
    ext_package="dss",
    install_requires=["cffi>=1.11.2", "numpy>=1.0"] + compat_requires,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
#        'Programming Language :: SQL', -- not yet!
        'Development Status :: 4 - Beta',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License'
    ],
    **extra_args
)

