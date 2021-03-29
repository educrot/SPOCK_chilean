import os
from setuptools import setup, find_packages

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='SPOCK_chilean',
    version='0.0.0',
    author='Elsa Ducrot',
    author_email='educrot@uliege.be',
    description=('Speculoos Observatory SChedule maKer for chilean night on SPECULOOS South Observatory'),
    keywords='',
    url='https://github.com/educrot/SPOCK_chilean/',
    packages=find_packages(),
    long_description=read('README.rst'),
    install_requires=['pandas','numpy==1.19.0','astroquery','astroplan','astropy','matplotlib','datetime','pyaml',
                        'docx','plotly','scipy','xlrd==1.2.0'],
)