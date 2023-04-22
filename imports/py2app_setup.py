from setuptools import setup

APP = ['imports/install.py']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup=["py2app"]
)
