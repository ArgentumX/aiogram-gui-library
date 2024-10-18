from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='aiogram-gui',
  version='0.0.1',
  author='ArgentumX',
  author_email='shirinovskyv@gmail.com',
  description='Simple aiogram library for addition gui interfaces',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/ArgentumX/aiogram-gui-library',
  packages=find_packages(),
  install_requires=['aiogram>=3.13.0'],
  classifiers=[
    'Programming Language :: Python :: 3.10',
    'License :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='aiogram gui scroll scrolling ',
  project_urls={
    'GitHub': 'https://github.com/ArgentumX/aiogram-gui-library'
  },
  python_requires='>=3.10'
)