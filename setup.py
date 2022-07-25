from setuptools import setup

setup(
    name='BeeCell',
    version='0.1.0',
    author='BEEGroup - CIMNE',
    author_email='beegroup@cimne.upc.edu',
    packages=['dexma'],
    scripts=['dexma/device.py', 'dexma/location.py', 'dexma/parameter.py', 'dexma/reading.py', 'dexma/supply.py'],
    url='https://github.com/BeeGroup-cimne/beecell',
    license='',
    description='An awesome package that does something',
    long_description=open('README.txt').read(),
    install_requires=[
        "attrs == 21.4.0",
        "certifi == 2021.10.8",
        "charset-normalizer == 2.0.12",
        "click == 8.0.4",
        "idna == 3.3",
        "iniconfig == 1.1.1",
        "packaging == 21.3",
        "pluggy == 1.0.0",
        "py == 1.11.0",
        "pyparsing == 3.0.7",
        "pytest == 7.1.1",
        "python-dotenv == 0.20.0",
        "requests == 2.27.1",
        "tomli == 2.0.1",
        "urllib3 == 1.26.9"
    ],
)
