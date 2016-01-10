from setuptools import setup, find_packages

name = 'madeasy-api'
version = '0.0.1'


setup(
    name=name,
    version=version,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description="A travel companion",
    long_description=open('README.md').read(),
    author="@ikosenn",
    author_email='kosen@madeasy.io',
    license="MIT",
    classifiers=[
        'Development Status ::',
        'Intended Audience :: Travellers',
        'Programming Language :: Python :: 3 :: Only',
    ],
    install_requires=[
        'django==1.9.1',
        'django-oauth-toolkit==0.10.0',
        'psycopg2==2.6.1',
        'djangorestframework==3.3.2',
        'gunicorn==19.4.5',
        'oauthlib==1.0.3',
        'click==6.2',
        'dj-database-url==0.3.0',
        'sarge==0.1.4',
    ],
    scripts=[
        'bin/madeasy_manage',
        'bin/run'
    ],
    include_package_data=True
)
