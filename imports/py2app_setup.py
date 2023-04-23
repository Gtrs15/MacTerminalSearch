from setuptools import setup

APP = ['run_installation.py']
OPTIONS = {
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup=["py2app"]
)
