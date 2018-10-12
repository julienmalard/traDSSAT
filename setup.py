from setuptools import setup, find_packages


def read_txt(f):
    with open(f, 'r', encoding='UTF-8') as d:
        return d.read()


setup(
    name='ansla',
    version=read_txt('tradssat/version.txt'),
    packages=find_packages(),
    url='',
    license='MIT',
    author=read_txt('AUTHORS.txt'),
    author_email='julien.malard@mail.mcgill.ca',
    description='DSSAT input and output file reader and writer',
    long_description=read_txt('README.md'),
    setup_requires=[],
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6'
    ],
)
