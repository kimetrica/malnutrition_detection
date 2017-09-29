"""Setuptools script for malnutrition_detection project."""
from setuptools import setup


setup(name='malnutrition_detection',
      version='0.0.1',
      description='Use machine learning to detect malnutrition in images',
      url='https://github.com/kimetrica/malnutrition_detection',
      author='Eric Nussbaumer',
      author_email='Eric Nussbaumer <eric.nussbaumer@kimetrica.com>',
      packages=['malnutrition_detection'],
      install_requires=['Pillow==4.2.1'],
      )
