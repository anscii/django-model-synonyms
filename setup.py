#!/usr/bin/env python

from setuptools import setup, find_packages

tests_require = [
    'django',
]

setup(
    name='django-model-synonyms',
    version=".".join(map(str, __import__('msyn').__version__)),
    author='anscii',
    author_email='nt.aknt@gmail.com',
    description="Model objects synonyms support for Django",
    url='http://github.com/anscii/django-model-synonyms',
    install_requires=[
        'django',
    ],
    #tests_require=tests_require,
    #extras_require={'test': tests_require},
    #test_suite='modelnotice.runtests.runtests',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)