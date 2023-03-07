from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name = 'django_uml',
    version = '1.0.0',
    author = 'Pedro Vieira',
    author_email = 'pedrophdv@outlook.com',
    packages = ['django_uml'],
    install_requires=['django' , 'plantuml' , 'six'],
    description = 'A UML Generator for Django and Django Rest Framework projects',
    long_description=readme,
    long_description_content_type="text/markdown",
    license = 'MIT',
    keywords = 'generator UML Django',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Internationalization',
        'Topic :: Scientific/Engineering :: Physics'
    ]
)