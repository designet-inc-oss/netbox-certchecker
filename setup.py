from setuptools import find_packages, setup

setup(
    name='netbox-certchecker',
    version='1.0',
    description='Netbox plugin for checking the certificate expiration date',
    install_requires=[],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
