from setuptools import setup, find_packages

setup(
    name="jarvis",
    version="0.0.1",
    author="Marcel Gietzmann-Sanders",
    author_email="marcelsanders96@gmail.com",
    packages=find_packages(include=["jarvis", "jarvis*"]),
    install_requires=[
        "flask==3.1.1",
        "flask_bootstrap==3.3.7.1",
        "pyyaml==6.0.2",
    ],
    entry_points={
        "console_scripts": [
            "jarvis = jarvis.cli:cli",
        ]
    },
)