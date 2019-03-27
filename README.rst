    **Archived**

    This project is being archived as we should no longer be using `ASSET_SERVER_URL` variables in our projects - it's more straightforwardly obvious & maintainable to simply write the URL `https://assets.ubuntu.com/v1/` directly, and it avoids the (over)engineering associated with maintaining and including this module.

    If we ever do change that URL and need to replace it in projects, it's as simple as:

    .. code:: bash

        find templates -name '*.html' -exec sed -i 's!/https://assets.ubuntu.com/v1/!https://assets.example.com/!g' {} \;

----


Django asset\_server\_url
=========================

Provides ``{{ ASSET_SERVER_URL }}`` (the URL for an asset server) as a
template context variable. Can be set through settings.py or by passing
an environment variable to the app.

Setup
-----

.. code:: python

    # settings.py
    TEMPLATE_CONTEXT_PROCESSORS += [
        "assets_template_context.asset_server_url"
    ]

Definition
----------

Set it in settings, e.g.:

.. code:: python

    # settings.py
    ASSET_SERVER_URL = '//assets.example.com/'

Or when starting the site, e.g.:

.. code:: bash

    ASSET_SERVER_URL=//assets.example.com/ python manage.py runserver

Usage
-----

Use in templates:

.. code:: html

    # templates/index.html

    <img src="{{ ASSET_SERVER_URL }}a34bc3-fish.jpg" />

Output:

.. code:: html

    <img src="//assets.example.com/a34bc3-fish.jpg"
