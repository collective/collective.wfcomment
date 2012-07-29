from setuptools import setup, find_packages
import os

version = '2.1.1'

setup(name='collective.wfcomment',
      version=version,
      description="Add a prompt on selected workflow transitions for the user to enter a comment",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read() + "\n" +
                       open("docs/INSTALL.txt").read(),
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Plone workflow comment',
      author='Thomas Desvenain',
      author_email='thomas.desvenain@gmail.com',
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
