import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("digs/__init__.py", "r", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

with open("README.rst", "rb") as f:
    readme = f.read().decode("utf-8")

with open("requirements.txt", "rb") as f:
    requirements = f.read().decode("utf-8")

setup(
    name="digs",
    version=version,
    description="dig multiple nameservers at once",
    long_description=readme,
    long_description_content_type="text/x-rst",
    url="https://github.com/azzamsa/digs",
    author="azzamsa",
    author_email="oktinastuzi@pm.me",
    license="GPLv3 license",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "License :: OSI Approved :: GPLv3 License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="cli",
    include_package_data=True,
    packages=["digs"],
    install_requires=requirements,
    entry_points={"console_scripts": ["digs=digs.digs:main"]},
)
