import sys

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='digitalocean-api-v2',
    version='0.0.1',
    description='Python3 wrapper for Digital Ocean API v2',
    author='Gustav Johansson',
    author_email='gustav@neer.se',
    url='https://github.com/neerdoc/digitalocean-api',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['requests>=2.2.1'],
    provides=['digitalocean'],
    tests_require=['pytest', 'mock'],
    cmdclass={'test': PyTest},
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
