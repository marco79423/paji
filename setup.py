# mypy: ignore_errors
import os

import setuptools

base_dir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(base_dir, 'requirements.txt'), encoding='utf-8') as fp:
    REQUIREMENTS = fp.read().split()

with open(os.path.join(base_dir, 'README.md'), encoding='utf-8') as fp:
    long_description = fp.read()

setuptools.setup(
    name='paji',
    version='0.1.0a1',
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
            'paji = paji.command:cli'
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
