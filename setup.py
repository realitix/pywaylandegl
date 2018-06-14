from distutils.command.build import build
from setuptools import setup
from os import path
import platform


setup(
    name="pywaylandegl",
    version="1.0",
    author="realitix",
    author_email="realitix@gmail.com",
    description="Python CFFI binding for Wayland-EGL",
    long_description="Python CFFI binding for Wayland-EGL",
    packages=['pywaylandegl'],
    install_requires=["cffi"],
    setup_requires=["cffi"],
    include_package_data=True,
    url="http://github.com/realitix/pywaylandegl",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.5",
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    license="Apache 2.0",
    ext_package="pywaylandegl",
    cffi_modules=["pywaylandegl/pywaylandegl_build/pywaylandegl_build.py:ffibuilder"]
)
