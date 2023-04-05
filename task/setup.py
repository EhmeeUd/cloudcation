from setuptools import setup

setup(
    name="my-project",
    version="0.1",
    install_requires=["requests>=2.0.0"],
    py_modules=["main"],
    entry_points={"console_scripts": ["my-command=main:main"]},
)
