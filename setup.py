from setuptools import setup

# Runtime dependencies. See requirements.txt for development dependencies.
dependencies = [
    'requests',
    'httpretty'
]

version = '0.0.1'

setup(name='cryptopia',
    version=version,
    description = 'Python wrapper for cryptopia API',
    author = 'The Bot Guy',
    author_email = 'thebotguy@protonmail.com',
    url = 'https://github.com/MarcSallent/cryptopia-api-python',
    license = 'GNU GENERAL PUBLIC LICENSE',
    packages=['.'],
#    scripts = ['scripts/bitfinex-poll-orderbook'],
    install_requires = dependencies,
    download_url = 'https://github.com/MarcSallent/cryptopia-api-python.tarball/',
    keywords = ['bitcoin', 'btc', 'cryptopia'],
    classifiers = [],
    zip_safe=True)