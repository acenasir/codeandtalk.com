from setuptools import setup

setup(
    name='cat',
    packages=['conf'],
    include_package_data=True,
    install_requires=[
        'jinja2',
    ],
    #setup_requires=[
    #    'pytest-runner',
    #],
    #tests_require=[
    #    'selenium',
    #],
)
