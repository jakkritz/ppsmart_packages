import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='ppsmart',
    version='0.0.1',
    description='ppsmart packages utilities collection',
    author='jakkrit s.',
    author_email='jakkrit@ppsmartbot.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jakkritz/ppsmart_packages',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)
