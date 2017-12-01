from setuptools import setup, find_packages
setup(
    name="ogs-batch-analyser",
    version="0.1",
    packages=find_packages(),
    scripts=['ogs-batch-analyser.py'],
    install_requires=['requests>=2.18']
)
