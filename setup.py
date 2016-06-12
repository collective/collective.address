from setuptools import setup
from setuptools import find_packages

version = '1.3.3.dev0'


setup(name='collective.address',
      version=version,
      description="Dexterity address behavior.",
      long_description=open("README.rst").read()
                       + "\n" +
                       open("CHANGES.rst").read(),
      classifiers=[
          'Framework :: Plone',
          'Programming Language :: Python',
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Plone',
          'Framework :: Plone :: 4.2',
          'Framework :: Plone :: 4.3',
          'Framework :: Plone :: 5.0',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Office/Business',
          'Topic :: Office/Business :: Scheduling',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='plone collective address',
      author='Johannes Raggam',
      author_email='raggam-nl@adm.at',
      url='https://github.com/collective/collective.address',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.CMFPlone',
          'plone.app.textfield',
          'plone.autoform',
          'plone.behavior',
          'plone.indexer',
          'plone.supermodel',
          'pycountry',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.schema',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """)
