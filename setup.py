from setuptools import setup, find_packages
setup(
    name="ogs-batch-analyser",
    version="0.1",
    py_modules=["ogs_batch_analyser"],
    entry_points={
        'console_scripts': [
            'ogs-batch-analyser=ogs_batch_analyser:main',
        ],
    },
    install_requires=['requests>=2.18']
)
