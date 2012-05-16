import setuptools
from distutils.core import setup

setup(name='django-go',
      version='0.1',
      author='Matt Smith',
      author_email='me@qbyt.me.uk',
      description=('Gives you the skeleton for a brand-new Django project'),
      requires=['distutils', 'Jinja2'],
      packages=['django_go'],
      package_dir = {'': 'lib'},
      scripts=['bin/django-go.py'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules'])
