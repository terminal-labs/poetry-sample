from setuptools import setup

setup(
    name='my_script',
    version='0.1.0',
    py_modules=['my_script'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'my_script = my_script:hello',
        ],
    },
)