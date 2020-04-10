digs
====

dig multiple nameservers at once

Installation
------------

::

    pip install digs


Features
--------
* `Check all record in multiple defined nameservers`_
* `Assert the returned result`_
* Check config in current directory by default. Either using ``yml`` or ``yaml`` as
  extension
* Support custom config location.

Take the tour
-------------

Check all record in multiple defined nameservers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    $ digs foo.com SOA

      66.0.0.0 - Los Angeles
      satu.neodns.id. hostmaster.neodns.id. 2019102900 10800 3600 604800 38400
      45.0.0.0 - Silicon Valley
      satu.neodns.id. hostmaster.neodns.id. 2019102900 10800 3600 604800 38400
      108.0.0.0 - New Jersey
      satu.neodns.id. hostmaster.neodns.id. 2019102900 10800 3600 604800 38400


Assert the returned result
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. role:: red
.. role:: green
.. code-block:: bash

    $ digs foo.com SOA -f custom-servers.yaml --check

      :green:`66.0.0.0 - Los Angeles`
      :green:`satu.neodns.id. hostmaster.neodns.id. 2019102900 10800 3600 604800 38400`
      :green:`45.0.0.0 - Silicon Valley`
      :green:`satu.neodns.id. hostmaster.neodns.id. 2019102900 10800 3600 604800 38400`
      :red:`108.0.0.0 - New Jersey`
      :red:`1.dns.id. hs.dns.id. 2019102900 10800 3600 604800 38400`

Quick Start
-----------

Create ``digs.yml`` file based on ``digs.yml.example``. Adjust the value to your
needs, then run ``digs``.
