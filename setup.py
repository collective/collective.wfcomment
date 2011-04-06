from setuptools import setup, find_packages
import os

version = '2.0'

setup(name='collective.wfcomment',
      version=version,
      description="Require ausers to enter a comment with "
                  "each workflow transition",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone workflow comment',
      author='Martin Aspeli',
      author_email='optilude@gmail.com',
      url='http://pypi.python.org/pypi/collective.wfcomment',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'z3c.form',
          'plone.app.registry',
          'plone.z3cform',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
