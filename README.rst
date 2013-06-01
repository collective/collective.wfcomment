.. image:: https://travis-ci.org/collective/collective.wfcomment.png?branch=master
   :target: https://travis-ci.org/collective/collective.wfcomment

Introduction
============

This package installs a JavaScript handler (using jQuery) that will present
a prompt box inviting the user to enter a comment before triggering a workflow
transition from the 'state' drop-down in a standard Plone site.

The handler will only be used for workflow actions using the standard
``content_status_modify`` script.

You can restrict this behaviour on some transitions through a control panel.

You can make the comment required or not.


Screenshot
==========

If enabled, you'll see a popup as shown below when initiating a workflow
transition.

.. image:: https://raw.github.com/collective/collective.wfcomment/master/docs/screenshot-wfcomment.jpg


Requirements
============

- Plone 4.0+ (tested under Plone 4.0, 4.1, 4.2 and 4.3).
- Tested with ie6, ie7, ff3, ff4, chrome.

Languages
=========

- English
- French
- German

Credits
=======

- Martin Aspeli, release 1.0
- Vincent Fretin and Thomas Desvenain, release 2.0
- Daniel Widerin  [saily]
