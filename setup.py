from setuptools import setup, find_packages
import os

version = '2.1.6.dev0'

setup(name='collective.wfcomment',
      version=version,
      description="Add a prompt on selected workflow transitions for the user "
                  "to enter a comment",
      long_description="\n\n".join([
          open("README.rst").read(),
          open("CHANGES.rst").read(),
      ]),
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
      extras_require={
          'test': [
              'plone.app.testing [robot] >=4.2.2',
              'plone.app.robotframework',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
