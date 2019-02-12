from setuptools import find_packages, setup

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='package',
    version='0.3.0',
    description='Creates a new python package from basic template',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Daniel Omar Vergara Pérez',
    author_email='daniel.omar.vergara@gmail.com',
    url='https://github.com/dany2691/package-scaffold',
    packages=find_packages(),
    install_requires=[
        'click==7.0.0'
    ],
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    entry_points={
        'console_scripts': [
            'package-scaffold=package_scaffold.main:main'
        ]
    }
)
