#!/bin/env python
# -*- coding: utf-8 -*-

'Django package for modernizr:' \
    ' JavaScript library that detects HTML5' \
    ' and CSS3 features in the user`s browser'


from setuptools import setup


setup(
    name='django-modernizr',
    version='2.8.3',
    url='http://modernizr.com',
    description=globals()['__doc__'],
    author='Faruk Ates, Paul Irish, Alex Sexton',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    license='MIT License',
    keywords=['django', 'modernizr'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_modernizr'],
    package_data={'django_modernizr': ['static/django_modernizr/js/*.js']}
)
