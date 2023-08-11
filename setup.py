from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in soft/__init__.py
from soft import __version__ as version

setup(
	name="soft",
	version=version,
	description="l",
	author="2",
	author_email="2",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
