Django asset_server_url
===

Provides the URL for an asset server, as a template context variable. Can be set through settings.py or by passing an environment variable to the app.

Setup
---

``` python
# settings.py
TEMPLATE_CONTEXT_PROCESSORS += [
    "assets_template_context.asset_server_url"
]
```

Definition
---

Set it in settings, e.g.:

``` python
# settings.py
ASSET_SERVER_URL = '//assets.example.com/'
```

Or when starting the site, e.g.:

``` bash
ASSET_SERVER_URL=//assets.example.com/ python manage.py runserver
```

Usage
---

Use in templates:

``` html
# templates/index.html

<img src="{{ ASSET_SERVER_URL }}a34bc3-fish.jpg" />
```

Output:

``` html
<img src="//assets.example.com/a34bc3-fish.jpg"
```
