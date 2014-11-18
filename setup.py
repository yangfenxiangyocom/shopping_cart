from setuptools import setup, find_packages
import os
version = "0.5.0"

setup(
    name='shopping_cart',
    version=version,
    description='Online sale/order cart',
    author='Web Notes Technologies',
    author_email='support@erpboost.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
