from setuptools import setup, find_packages

version = '1.0'

setup(name='caes.contact',
      version=version,
      description="",
      long_description=open("README.rst").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='dexterity plone behavior contact richtextallthethings',
      author='eleddy',
      author_email='',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['caes'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity',
          'plone.behavior',
          'plone.directives.form',
          'zope.schema',
          'zope.interface',
          'zope.component',
          'rwproperty',
      ],
      extras_require={
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=[],
      )
