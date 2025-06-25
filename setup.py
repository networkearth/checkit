from setuptools import setup, find_packages

setup(
    name="checkit",
    version="0.0.1",
    author="Marcel Gietzmann-Sanders",
    author_email="marcelsanders96@gmail.com",
    packages=find_packages(include=["checkit", "checkit*"]),
    install_requires=[
        "flask==3.1.1",
        "flask_bootstrap==3.3.7.1",
        "pyyaml==6.0.2",
    ],
    entry_points={
        "console_scripts": [
            "checkit = checkit.cli:cli",
        ]
    },
)