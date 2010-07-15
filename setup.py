from distutils.core import setup

setup(
    name = 'django-ifactiveurl',
    version = '0.1',
    url = 'http://github.com/cdr/django-ifactiveurl',
    author = 'Charles Reinman',
    author_email = 'creinman@gmail.com',
    description = 'Simple Django template tag for evaluating current url name',
    long_description = ('A simple if/else template tag evaluating whether the '
                        'current url name matches one of a list of url names'),
    packages = ['ifactiveurl'],
    classifiers = ['Development Status :: 3 - Alpha',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
)