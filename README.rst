releng-tool documentation translations
======================================

This repository manages translations for releng-tool's documentation.

commands
--------

Fetch required repositories to work against by invoking:

.. code-block:: shell

   $ ./fetch

Generate gettext_'s portable object templates with the following:

.. code-block:: shell

   $ ./update

Register a new language translation set with the following:

.. code-block:: shell

   $ ./register-language

.. _gettext: https://www.gnu.org/software/gettext/
