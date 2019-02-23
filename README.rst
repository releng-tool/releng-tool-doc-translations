releng-tool documentation translations
======================================

This repository manages translations for releng-tool's documentation.

commands
--------

gettext_'s portable object templates are generated with the following:

.. code-block:: shell

   sphinx-build -b gettext . locale/pot
    (or)
   python -m sphinx -b gettext . locale/pot

A specific language's translation set is updated as follows:

.. code-block:: shell

   sphinx-intl update -p locale/pot -l <language>
    (or)
   python -m sphinx_intl update -p locale/pot -l <language>

A specific language's documentation is generated as follows:

.. code-block:: shell

   sphinx-build -D language=<language> -b html . _build/html
    (or)
   python -m sphinx -D language=<language> -b html . _build/html

.. _gettext: https://www.gnu.org/software/gettext/
