# CA

This CA is not meant to be secure!

Just a HTTP wrapper for openssl.
For client certificates, serving a revocation list and a certificate generation.

/api/

* /crl #serve certificate revocation list
* /cert #give out the CA certificate
* /create #?=name=name
* /revoke #?=serial=serialnumber
