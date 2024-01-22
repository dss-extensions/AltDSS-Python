from setuptools import setup
import re, os, io
import glob

# Copy README.md contents
with io.open('README.md', encoding='utf8') as readme_md:
    long_description = readme_md.read()

# Handle the version string
# 1. Try env var ALTDSS_PYTHON_VERSION
# 2. Try GITHUB_REF for a Git tag
# 3. Otherwise, just use the hardcoded version
package_version = os.environ.get('ALTDSS_PYTHON_VERSION')
github_ref = os.environ.get('GITHUB_REF')
if package_version is None and github_ref is not None:
    package_version = github_ref[len("refs/tags/"):]

if package_version is not None:
    if re.match(r'^\d+\.\d+\.\d+((-\d+){0,1}|((a|b|(rc))\d*)|(\.dev\d+)){0,1}$', package_version) is None:        
        package_version = None

if package_version is None:
    # Extract version from the source files
    with open('dss/__init__.py', 'r') as f:
        match = re.search("__version__ = '(.*?)'", f.read())
        package_version = match.group(1)
else:
    with open('dss/__init__.py', 'r') as f:
        init_py_orig = f.read()

    init_py = re.sub("__version__ = '(.*?)'", f"__version__ = '{package_version}'", init_py_orig)
    if init_py_orig != init_py:
        with open('dss/__init__.py', 'w') as f:
            f.write(init_py)

# Copy all the i18n files
src_path = os.environ.get('SRC_DIR', '')
mo_path_out = os.path.abspath(os.path.join(src_path, 'dss', 'messages'))

# Filter files to include in the Python package
extra_files = (
    glob.glob(os.path.join(mo_path_out, '*.mo'))
)

extra_args = dict(package_data={
    'dss': extra_files
})

setup(
    name="altdss",
    description="Modern, detailed Python bindings and tools based on the DSS C-API project, the alternative OpenDSS implementation from DSS-Extensions.org. Tries to expose all OpenDSS objects and many details which previously required using the Text interface, or just weren't available.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Paulo Meira",
    author_email="pmeira@ieee.org",
    version=package_version,
    license="BSD",
    packages=['altdss'],
    ext_package="altdss",
    install_requires=["dss_python", "numpy>=1.21.0", "typing_extensions>=4.5,<5", "scipy"],
    tests_require=["scipy", "ruff", "xmldiff", "pandas", "pytest"],
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: BSD License'
    ],
    **extra_args
)

