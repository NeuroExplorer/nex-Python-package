import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nex", 
    version="1.0.0",
    author="Alex Kirillov",
    author_email="<alex@neuroexplorer.com>",
    description="Run NeuroExplorer Python scripts and read and write .nex and .nex5 files in any Python IDE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NeuroExplorer/nex-Python-package",
    packages=setuptools.find_packages(),
    install_requires=['numpy',
                      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7.*',
)