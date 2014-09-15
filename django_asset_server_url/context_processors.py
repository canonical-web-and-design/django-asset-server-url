from os import environ

from django.conf import settings


def asset_server_url(request):
    """
    Set the ASSET_SERVER_URL
    """

    environ_url = environ.get('ASSET_SERVER_URL')

    if environ_url:
        asset_server_url = environ_url
    else:
        asset_server_url = getattr(
            settings,
            'ASSET_SERVER_URL',
            '//localhost:8001/'
        )

    return {
        'ASSET_SERVER_URL': asset_server_url
    }
