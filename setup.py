# mypy: ignore_errors
import os

import setuptools

base_dir = os.path.abspath(os.path.dirname(__file__))

REQUIREMENTS = []
with open(os.path.join(base_dir, 'requirements.txt'), encoding='utf-8') as fp:
    for line in fp.readlines():
        line = line.strip()
        if line and not line.startswith('#'):
            REQUIREMENTS.append(line)

with open(os.path.join(base_dir, 'README.md'), encoding='utf-8') as fp:
    long_description = fp.read()

setuptools.setup(
    name='paji',
    version='0.2.2',
    author='兩大類',
    author_email='marco79423@gmail.com',
    url='https://github.com/marco79423/paji',
    python_requires='>=3.6',
    description='兩大類專用中台',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'paji = paji.cmd:cli'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
