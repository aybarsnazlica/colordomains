from setuptools import setup

setup(
    name="colordomains",
    version="0.1.0",
    packages=["colordomains"],
    entry_points={"console_scripts": ["colordomains = colordomains.__main__:main"]},
)
