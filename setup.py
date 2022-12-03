from setuptools import setup, find_packages

setup(
    name='sord',
    version='0.1.0',
    py_modules=['sord'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'sord = sord.cli:cli',
        ],
    },
    packages=find_packages(),
)
