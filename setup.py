from setuptools import find_packages
from setuptools import setup

import os


long_description = (
    open("README.rst").read() + "\n" +
    open(os.path.join("src", "collective", "cart", "shipping", "docs", "HISTORY.rst")).read() + "\n" +
    open(os.path.join("src", "collective", "cart", "shipping", "docs", "CREDITS.rst")).read())

setup(
    name='collective.cart.shipping',
    version='0.6.0.2',
    description="Adds shipping methods to Plone.",
    long_description=long_description,
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7"],
    keywords='',
    author='Taito Horiuchi',
    author_email='taito.horiuchi@gmail.com',
    url='https://github.com/collective/collective.cart.shipping',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['collective', 'collective.cart'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.ATCountryWidget',
        'Products.PythonField',
        'collective.behavior.vat',
        'plone.app.dexterity',
        'setuptools'],
    extras_require={'test': ['hexagonit.testing']},
    entry_points="""
    # -*- Entry points: -*-

    [z3c.autoinclude.plugin]
    target = plone
    """)
