from setuptools import setup


name = "Brian Curtin"
email = "brian@python.org"

setup(name="lenk",
      description="A dictionary that always finds what it's looking for.",
      license="Apache Software License",
      version="1.0",
      author=name,
      author_email=email,
      maintainer=name,
      maintainer_email=email,
      long_description=open("README.rst").read(),
      py_modules=["lenk"],
      classifiers=["Development Status :: 5 - Production/Stable",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: Apache Software License",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 3",
                  ],
     )
