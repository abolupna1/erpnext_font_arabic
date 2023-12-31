from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in font_arabic/__init__.py
from font_arabic import __version__ as version

setup(
	name="font_arabic",
	version=version,
	description="font arabic almarai",
	author="edom",
	author_email="abolupna1@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
