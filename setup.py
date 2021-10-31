from setuptools import setup, find_packages


PACKAGENAME = "cosmojax"
VERSION = "0.0.dev"


setup(
    name=PACKAGENAME,
    version=VERSION,
    author="Andrew Hearin",
    author_email="ahearin@anl.gov",
    description="Cosmology in JAX",
    long_description="Cosmology in JAX",
    install_requires=["numpy", "jax"],
    packages=find_packages(),
    url="https://github.com/aphearin/cosmojax",
)
