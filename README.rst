livesplit-mv-run
==============

WIP

.. image:: https://badge.fury.io/py/livesplit-mv-run.png
    :target: https://badge.fury.io/py/livesplit-mv-run

.. image:: https://travis-ci.org/narfman0/livesplit-mv-run.png?branch=master
    :target: https://travis-ci.org/narfman0/livesplit-mv-run

Move a particular run from one split file to another

Installation
------------

Install via pip::

    pip install livesplit-mv-run

Development
-----------

Run test suite to ensure everything works::

    make test

Release
-------

To publish your plugin to pypi, sdist and wheels are registered, created and uploaded with::

    make release-test

For test. After ensuring the package works, run the prod target and win::

    make release-prod

License
-------

Copyright (c) 2020 Jon Robison

See LICENSE for details
