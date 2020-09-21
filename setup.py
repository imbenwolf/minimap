from setuptools import setup

setup(
    name='minimap',
    version='0.1',
    description='Mini nmap',
    py_modules=['minimap'],
    entry_points={
        'console_scripts': ['minimap=minimap:main']
    },
    install_requires=['']
)
