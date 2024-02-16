from extras.plugins import PluginConfig


class NetBoxCertCheckerConfig(PluginConfig):
    name = 'netbox_certchecker'
    verbose_name = 'Netbox Certificate Checker'
    description = 'Checking the certificate expiration date'
    version = '1.0'
    base_url = 'certchecker'
    min_version = '3.7.0'


config = NetBoxCertCheckerConfig
