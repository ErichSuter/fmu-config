#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup, find_packages
import versioneer

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
]

setup_requirements = [
    'pytest-runner',
]

test_requirements = [
    'pytest',
]

# erv_function = ('estimate_remaining_volumes='
#                 'xtgeo_utils1.estimate_remaining_volumes.erv:main')
# rrp_function = ('rename_roff_parameter='
#                 'xtgeo_utils1.rename_roff_prop.rrp:main')
# cgf_function = ('convert_grid_format='
#                 'xtgeo_utils1.convert_grid_format.cgf:main')
# xsc_function = ('xsections='
#                 'xtgeo_utils1.xsections.xsect:main')

setup(
    name='fmu_config',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Library for various smaller scripts in FMU scope",
    long_description=readme + '\n\n' + history,
    author="Jan C. Rivenaes",
    author_email='jriv@statoil.com',
    url='https://git.statoil.no/fmu-utilities/fmu_config',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    # entry_points={
    #     'console_scripts': [
    #         erv_function, rrp_function, cgf_function, xsc_function
    #     ]
    # },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='fmu_config',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
