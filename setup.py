import setuptools
from HamodyToolp import Hamody

with open('README.md', 'r') as fh:
    long_description = fh.read()
with open('requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setuptools.setup(
    name="HamodyToolp",
    version="1.0.0",
    author="MahmoudAyman",
    author_email="mahmoudhshs8@gmail.com",
    description='7AMODY TOOLp',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Almheb6/HamodyToolp',
    packages=["HamodyToolp"],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License'],
    install_requires=requires,
)