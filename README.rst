========
vistring
========


.. image:: https://img.shields.io/pypi/v/vistring.svg
        :target: https://pypi.python.org/pypi/vistring

.. image:: https://img.shields.io/travis/pymivn/vistring.svg
        :target: https://travis-ci.org/pymivn/vistring

.. image:: https://readthedocs.org/projects/vistring/badge/?version=latest
        :target: https://vistring.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pymivn/vistring/shield.svg
     :target: https://pyup.io/repos/github/pymivn/vistring/
     :alt: Updates


Python library for handling Vietnamese string, especially with tones


* Free software: BSD license
* Documentation: https://vistring.readthedocs.io.

Install
-------

::

  $ pip install vistring

Usage
-----

Remove tones::

  >>> import vistring
  >>> vistring.remove_tones(u'Em ơi có bao nhiêu? Sáu mươi năm cuộc đời!')
  'Em oi co bao nhieu? Sau muoi nam cuoc doi!'

Features
--------

* TODO

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

