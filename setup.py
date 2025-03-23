# setup.py
from setuptools import setup, find_packages

setup(
    name="forestlandscape",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.20.0",
        "pandas>=1.3.0",
        "matplotlib>=3.4.0",
        "scikit-learn>=1.0.0",
    ],
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email
    description="Python tools for analyzing forest landscape dynamics and fragmentation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ForestLandscapeAnalysis",  # Replace with your username
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: GIS",
    ],
    python_requires=">=3.7",
)
