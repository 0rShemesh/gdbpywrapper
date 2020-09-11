import setuptools


install_requires = [
    "pexpect"
]

setuptools.setup(
    name="gdb_wrapper",
    version="0.0.1",
    author_email="author@example.com",
    description="A gdb wrapper that parse also commands data",
    
    url="https://github.com/0rShemesh/gdbpywrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"],
    python_requires='>=3.6',
    install_requires = install_requires,
)