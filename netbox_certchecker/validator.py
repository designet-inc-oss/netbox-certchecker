from OpenSSL import crypto
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile

class CertificateValidator:

    def __init__(self):
        self._err_message = f"Invalid certificate file or system error."

    def __call__(self, file_val: UploadedFile):
        try:
            reader = file_val.file.read()
            cert = crypto.load_certificate(crypto.FILETYPE_PEM, reader)
        except crypto.Error:
            raise ValidationError(message=f"Invalid certificate format.Need x509 format.")
        except:
            raise ValidationError(message=f"Invalid certificate file or system error.")
