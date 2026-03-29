"""Installer for the bda.aaf.site package."""

from setuptools import find_packages
from setuptools import setup

version = "1.8.dev0"

long_description = "\n\n".join(
    [
        open("README.md").read(),
        open("CHANGES.md").read(),
    ]
)


setup(
    name="collective.address",
    version=version,
    description="Dexterity address behavior.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: 6.1",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Development Status :: 5 - Production/Stable",
    ],
    python_requires=">=2.7",
    keywords="plone collective address",
    author="Johannes Raggam",
    author_email="thetetet@gmail.com",
    url="https://github.com/collective/collective.address",
    license="GPL",
    packages=find_packages(),
    namespace_packages=["collective"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "plone.api",
        "plone.app.textfield",
        "plone.autoform",
        "plone.behavior",
        "plone.indexer",
        "plone.supermodel",
        "Products.CMFPlone",
        "pycountry",
        "zope.i18nmessageid",
        "zope.interface",
        "zope.schema",
        "six",
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
