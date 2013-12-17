try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Risk, or Prysk!',
    'author': 'Anders Ekbom',
    'url': 'ekbom.org',
    'download_url': 'ekbom.org/donwload',
    'author_email': 'anders.ekbom@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['main'],
    'scripts': [],
    'name': 'prysk'
}

setup(**config)
