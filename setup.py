from setuptools import setup, find_packages
setup(
    name="HelloWorld",
    version="0.1",
    packages=find_packages(),
    # scripts=['main.py'],
    entry_points={
        "console_scripts": [
            "foo = main:foo",
            "bar = main:bar",
        ],
    }
)
