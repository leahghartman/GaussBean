from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'GAUSSian BEam ANalysis package'

# Setting up the package
setup(
        name="gaussbean", 
        version=VERSION,
        author="Leah Hartman",
        author_email="<leah.ghartman@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[], # add any additional packages needed
        keywords=['python', 'gaussian', 'laser'],
        classifiers= []
)