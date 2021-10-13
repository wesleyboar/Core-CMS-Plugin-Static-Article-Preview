import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# To allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='taccsite_static_article_preview',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='A DjangoCMS plugin (for TACC Core CMS) to render a static preview of content from an article.',
    long_description=README,
    url='https://github.com/TACC/Core-CMS-Plugin-Static-Article-Preview/',
    author='Wesley Bomar',
    author_email='wbomar@tacc.utexas.edu',
    # SEE: https://pypi.org/classifiers/
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.2.16',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
