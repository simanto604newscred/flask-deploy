from setuptools import setup, find_packages

requirements_to_requires = lambda fn: [req.strip() for req in open(fn, 'rb')]

setup(name='flask_project',
      version='0.0-dev',
      packages=find_packages(exclude=('tests', 'tests.*')),
      install_requires=requirements_to_requires('requirements.txt'),
      setup_requires=[
          'wheel==0.24.0',
      ],
      zip_safe=False,
      )
