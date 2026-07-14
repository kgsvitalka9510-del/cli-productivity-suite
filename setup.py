from setuptools import setup, find_packages

setup(
    name="cli-productivity-suite",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "click>=8.0",
    ],
    entry_points={
        "console_scripts": [
            "cli-suite=cli.main:cli",
        ],
    },
    author="Agent Developer",
    description="Professional CLI tools for developers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kgsvitalka9510-del/cli-productivity-suite",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
