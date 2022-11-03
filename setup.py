from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in frappe_disable_signup/__init__.py
from frappe_disable_signup import __version__ as version

setup(
	name='frappe_disable_signup',
	version=version,
	description='signup for specific domains',
	author='Shrihar Patil',
	author_email='shridhar.p@zerodha.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
