from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

packages = find_packages(exclude=('tests', 'docs'))

setup(
    name='abletonfinder',
    version='0.0.2',
    description='Ableton finder',
    long_description=readme,
    author='Jay Shah',
    author_email='unknown@gmailcom',
    url='https://github.com/jayshah98/abletonfinder',
    license=license,
    packages=packages,
    install_requires=[
        'mdfind>=2018.11.20',
        'beautifulsoup4>=4.7.1'
    ],
    entry_points = {
        'console_scripts': [
            'abletonfinder=abletonfinder.abletonfinder:main'
        ]
    }
)
