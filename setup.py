from setuptools import setup, find_packages

setup(
    name='github-cleaner',
    version='0.1.0',
    author='borzeckid',
    author_email='borzecki.daniel@gmail.com',
    description= 'cleaning service for your dirty pull requests',
    url=''
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Colorama',
        'PyGithub'
    ],
    entry_points='''
        [console_scripts]
        github-cleaner=github-cleaner:cli
    ''',
)
