from setuptools import setup


setup(name="PySoundCloud",
      version="2020.6.1",
      description="A Python wrapper for the SoundCloud API",
      install_requires=open("requirements.txt").read(),
      py_modules=[],
      packages=["pysoundcloud"],
      author="Anthony Provenza",
      url="https://github.com/AnthonyWritesBadCode/PySoundCloud/",
      license=open("license.txt").read(),
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown")
