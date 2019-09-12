
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='qg_eureka',
    version='0.0.1',
    description=(
        '全高连接eureka组件'
    ),
    long_description=open('README.md').read(),
    author='zouwendi',
    author_email='tz310200@gamil.com',
    maintainer='zouwendi',
    maintainer_email='tz310200@gamil.com',
    license='GPL3 License',
    packages=find_packages(),
    platforms=["all"],
    url='',
    install_requires=[
        "setuptools>=41.0.1",
        "requests>=2.21.0",
        "typing>=3.7.4.1",
        "ujson>=1.35",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL3 License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
)
