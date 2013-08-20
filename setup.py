# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):

    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()

    except IOError:
        return ''

setup(
    name='django-color-captcha',

    version=__import__('color_captcha').__version__,
    description=read('DESCRIPTION'),

    license='MIT',
    keywords='django captcha',

    author='Victor Smirnov',

    author_email='victor.smirnov@redsolution.ru',

    maintainer='Victor Smirnov',
    maintainer_email='victor.smirnov@redsolution.ru',

    url='https://github.com/qvit/django-color-captcha',
    classifiers=[
        'Development Status :: Alpha',
        'Intended Audience :: Developers',

        'License :: MIT',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Natural Language :: English',

        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    packages=find_packages(exclude=['example', 'example.*']),

    install_requires=[],
    include_package_data=True,

    long_description=read('README'),
)
