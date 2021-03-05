from setuptools import setup
import os
import sys

setup(
    name='subspace_inference',
    version='0.0',
    description='Subspace Inference for Bayesian Deep Learning',
    author='Pavel Izmailov, Wesley Maddox, Polina Kirichenko, Timur Garipov, Dmitry Vetrov, Andrew Gordon Wilson',
    author_email='wm326@cornell.edu',
    url='https://github.com/wjmaddox/drbayes',
    license='MPL-2.0',
    packages=['subspace_inference'],
    install_requires=[
        'tqdm>=4.26.0',
        'numpy>=1.14.3',
        'torchvision>=0.1.8',
        'gpytorch>=0.1.0rc4',
        'tabulate>=0.8.2',
        'scipy>=1.1.0',
        'setuptools>=39.1.0',
        'matplotlib>=2.2.2',
        'torch>=1.7.1',
        'scikit_learn>=0.20.2',
        'pyro-ppl>=1.5.2',
        'pyparsing>=2.4.5',
        'Pillow>=8.1.0'
   ],
    include_package_data=True,
    classifiers=[
        'Development Status :: 0',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.6'],
)
