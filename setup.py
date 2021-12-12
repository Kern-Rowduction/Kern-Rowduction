"""The setup.py of the Kern_Rowduction package."""

from setuptools import setup, find_packages
from pathlib import Path


VERSION = '0.0.3'
DESCRIPTION = 'Kern Rowduction - A package to reduce the number of rows / undersample the \
    (imbalanced) datasets by graph kernelisation methods.'
CURRENT_DIRECTORY = Path(__file__).parent
LONG_DESCRIPTION = (CURRENT_DIRECTORY / "README.md").read_text()

# Setting up
setup(
        name="Kern-Rowduction",
        version=VERSION,
        author="Hichem Boughattas & Hamza Bouanani",
        author_email="kern.rowduction@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=["pandas","numpy","networkx"],
        url = 'https://github.com/Kern-Rowduction/Kern-Rowduction',
        download_url = 'https://github.com/Kern-Rowduction/Kern-Rowduction/archive/refs/tags/v_0.0.1.tar.gz',
        keywords=['python', 'graph', "kernel", "rowduction", \
        "imbalance", "data", "science", "dataset"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Intended Audience :: End Users/Desktop",
            "Intended Audience :: Science/Research",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Operating System :: POSIX :: Linux",
            "Topic :: Scientific/Engineering :: Mathematics"
        ]
)
