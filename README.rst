Django-go: Because you'd rather be working
===========================================

Django-go is an MIT licensed tool for starting new projects quickly. 

Features
--------

- Lets you setup your project templates with Jinja2.
- Less typing saves your fingers.
- Less typing saves you money.

Installation
------------

To install django-go, simply: ::

    $ pip install -e git+ssh://git@github.com/qbyt/django-go.git#egg=django-go

Or download the files and run: ::
    
    $ python setup.py install

Go go go (Usage)
-----------------

Keeping it real simple like for now: ::

    $ django-go.py <project_name> <setup_directory>

Runway
------

On the horizon:

- Support for .project files
- Conditional configuration templates
- Additional command line arguments

Mad Props
---------

Thanks go to:

- `Lincoln Loop <http://lincolnloop.com/>`_ (for writing `the project that inspired this one <https://github.com/lincolnloop/django-startproject.git>`__)
- Fiona (for the egg sandwiches I had for lunch)
