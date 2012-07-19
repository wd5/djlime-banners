#!/usr/bin/env python
from os.path import join, dirname
from setuptools import setup, find_packages

from banners import __version__

def long_description():
    try:
        return open(join(dirname(__file__), 'README.rst')).read()
    except IOError:
        return ''

setup(
    name='djlime-banners',
    author='Andrey Butenko',
    author_email='whitespysoftware@yandex.ru',
    url='https://github.com/whitespy/djlime-banners',
    description='A application display of banners.',
    long_description=long_description(),
    install_requires=['South==0.7.4', 'djlime>=0.0.8',
                      'django-imagekit==2.0.1'],
    version = __version__,
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=['Framework :: Django',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License']
)
