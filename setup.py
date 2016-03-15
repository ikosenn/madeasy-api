from setuptools import setup, find_packages

name = 'madeasy-api'
version = '0.0.9'


setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description="A travel companion",
    long_description=open('README.md').read(),
    author="@ikosenn",
    url="https://api/madeasy.io",
    author_email='kosen@madeasy.io',
    license="MIT",
    classifiers=[
        'Development Status ::',
        'Intended Audience :: Travellers',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'ansible==2.0.0',
        'django==1.9.1',
        'django-oauth-toolkit==0.10.0',
        'psycopg2==2.6.1',
        'djangorestframework==3.3.2',
        'django-cors-headers==1.1.0',
        'gunicorn==19.4.5',
        'oauthlib==1.0.3',
        'click==6.2',
        'dj-database-url==0.3.0',
        'sarge==0.1.4',
        'ujson==1.35',
        'textX==0.4.2',
        'python-dateutil==2.5.0',
        'django-mptt==0.8.3',

    ],
    scripts=[
        'bin/madeasy_manage',
        'bin/run'
    ],
    include_package_data=True
)
