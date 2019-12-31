from setuptools import setup, find_packages


def read_txt(f):
    with open(f, 'r', encoding='UTF-8') as d:
        return d.read()


setup(
    name='tradssat',
    version=read_txt('tradssat/version.txt'),
    packages=find_packages(),
    url='',
    license='MIT',
    author=read_txt('tradssat/AUTHORS.txt'),
    author_email='julien.malard@mail.mcgill.ca',
    description='DSSAT input and output file reader and writer',
    setup_requires=[],
    install_requires=['numpy', 'chardet'],
    package_data={'tradssat': ['*.txt']},
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha'
    ],
)
