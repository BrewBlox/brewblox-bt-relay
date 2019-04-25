from setuptools import find_packages, setup

setup(
    name='brewblox-bt-relay',
    use_scm_version={'local_scheme': lambda v: ''},
    long_description=open('README.md').read(),
    url='https://github.com/BrewBlox/brewblox-bt-relay',
    author='BrewPi',
    author_email='development@brewpi.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: End Users/Desktop',
        'Topic :: System :: Hardware',
    ],
    keywords='brewblox proof-of-concept',
    packages=find_packages(exclude=['test']),
    install_requires=[
        'rpyc',
        'bluepy',
        'click',
    ],
    python_requires='>=3.7',
    setup_requires=['setuptools_scm'],
)
