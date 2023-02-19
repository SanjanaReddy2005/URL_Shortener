from setuptools import setup,find_packages

with open('requirements.txt') as f:
      requirements=f.readlines()

long_description = 'Enter the url and the name of the url to create the shorter link for using it easily'

setup ( name='URL_Shortener',
        version='1.0.0',
        author='Sai Sanjana Reddy Algubelly',
        author_email='cse220001065@iiti.ac.in',
        url='https://github.com/SanjanaReddy2005/URL_ShortenerCLI.git',
        description='To shorten the urlwhich is given by the user',
        long_description= long_description,
        packages = find_packages(),
        # install_requires = [
        #     'requests'
        # ],
        install_requires = requirements,
        classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ]
)
       


