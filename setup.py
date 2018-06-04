from distutils.core import setup
from setuptools import find_packages


setup(
    # Basic metadata
    name='not-ansible-awork',
    version='1.0',
    author='Alan',
    author_email='arominge@redhat.com',

    # Additional information
    description='A CLI, rewriting tower-CLI.',
    license='Apache 2.0',

    # How to do the install
    install_requires=['click', 'requests', 'six', 'PyYAML'],
    provides=['awork'],
    entry_points={
        'console_scripts': [
            'awork=awork.cli.run:cli'
        ],
    },
    packages=['awork'],
    include_package_data=True,
    zip_safe=False
)
