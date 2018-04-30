from setuptools import setup

setup(
    name="qitto",
    version='0.1',
    py_modules=['qittolist'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        qitto=qittolist:cli
    ''',
)
