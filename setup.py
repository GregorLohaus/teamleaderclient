import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "teamleaderclient",
    version = "0.1.0",
    python_requires='>=3.11.*',
    author = "Gregor Lohaus",
    author_email = "lohausgregor@gmail.com",
    license = "BSD",
    packages=find_packages(),
    install_requires=['dataclasses_json','requests'],
    # entry_points = {
    #     'console_scripts': ['sortconfig=sortconfig.main:main'],
    # },
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)