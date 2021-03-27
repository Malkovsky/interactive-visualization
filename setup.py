# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="interactive-visualization", # Replace with your own username
    version="0.1.1",
    author="Nikolay Malkovsky",
    author_email="malkovskynv@gmail.com",
    description="Package provides a simple widget-based framework for interactive visualization of algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Malkovsky/interactive-visualization",
    project_urls={
        "Bug Tracker": "https://github.com/Malkovsky/interactive-visualization/issues",
    },
    classifiers=[
	"Development Status :: 4 - Beta",
	"Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
)