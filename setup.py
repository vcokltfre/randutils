from setuptools import setup, find_packages

version = "1.0.0"

setup(
	name='randutils',
	version=version,
	packages=find_packages(),
	url='https://github.com/vcokltfre/randutils',
	license='MIT',
	author='vcokltfre',
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=[],
	description='A collection of utilities to work with random data, usually text.',
	python_requires='>=3.6',
)