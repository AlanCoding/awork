from setuptools import setup, find_packages


setup(
    # Basic metadata
    name='awork',
    version='1.0',
    author='Alan',
    author_email='arominge@redhat.com',

    # Additional information
    description='A CLI, rewriting tower-CLI.',
    license='Apache 2.0',

    # How to do the install
    install_requires=['click', 'requests', 'six', 'PyYAML'],
    entry_points={
        'console_scripts': [
            'awork=awork.cli.run:cli'
        ],
    },
    packages=find_packages(),
    include_package_data=True,
    zip_safe=True
)
