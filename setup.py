from setuptools import setup

setup(
    name='django-asset-server-url',
    version='0.1',
    author='Robin',
    author_email='robin.winslow@canonical.com',
    url='https://github.com/ubuntudesign/django-asset-server-url',
    packages=[
        'django_asset_server_url'
    ],
    description=(
        'Provides the URL for an asset server, as a template context variable.'
    ),
    long_description=open('README.rst').read(),
    install_requires=[
        "Django >= 1.3",
    ],
)
