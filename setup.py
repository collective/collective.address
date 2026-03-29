"""Installer for the bda.aaf.site package."""

from setuptools import setup

version = "2.0.dev0"

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
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Development Status :: 5 - Production/Stable",
    ],
    python_requires=">=3.10",
    keywords="plone collective address",
    author="Johannes Raggam",
    author_email="thetetet@gmail.com",
    url="https://github.com/collective/collective.address",
    license="GPL version 2",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "plone.api",
        "plone.app.content",
        "plone.autoform",
        "plone.behavior",
        "plone.i18n",
        "plone.indexer",
        "plone.supermodel",
        "Products.CMFPlone",
        "pycountry",
        "six",
        "z3c.form",
    ],
    extras_require={
        "test": [],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
