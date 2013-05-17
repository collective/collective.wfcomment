Changelog
=========

2.1.5 (unreleased)
------------------

- Nothing changed yet.


2.1.4 (2013-05-17)
------------------

- Add a new test and remove unneeded ones.
  [saily]

- Add support for dexterity content types.
  [saily]

- Update permissions for comment view and javascript viewlet.
  [saily]


2.1.3 (2013-05-16)
------------------

- Add tests using robotframework, travis integration and .
  [saily]

- Add german translations and add an ``update_translations`` script to be
  generated through buildout.  [saily]

- 'form.buttons.cancel' in ``prepOverlay`` closeselector has to be in quotes
  to avoid unrecognized expression javascript errors.  [saily]

- Set correct javascript filter for ``prepOverlay``.
  [saily]

- Move from svn to collective, merge tdesvenain's remote repo into collective.
  Please maintain in collective in future.  [saily]

- Restructure buildout for Plone 4.3 and Plone 4.2.
  [saily]


2.1.2 (2013-04-18)
------------------

- Really removed kss dependency (unused imports)
  [cedricmessiant]


2.1.1 (2012-07-29)
------------------

- Full jquery: kss behaviours entirely replaced.
  Fixes under 4.1.x
  [thomasdesvenain]

2.0.2 (2011-05-02)
------------------

- controlpanel: hide transition selection if 'all transitions' option is selected.
  [thomasdesvenain]

- fix when 'all transitions' option is selected.
  [thomasdesvenain]

- fix plone.app.registry dependency
  [toutpt]


2.0.1 (2011-05-02)
------------------

- Fixed profile.


2.0 (2011-04-28)
----------------

Complete rewrite :

  * uses ajax internationalized form,
  * allows to select a list of transitions,
  * kss compliant.
  [vincentfretin, thomasdesvenain]


1.0b2 - 2009-08-31
------------------

* Fix 'undefined' error in IE.

1.0b1 - 2009-03-19
------------------

* Initial release

