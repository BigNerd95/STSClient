#!/usr/bin/env python3

# License: AGPL 3
# Author: Lorenzo Santina (BigNerd95)

from Crypto.Util.asn1 import DerSequence
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from binascii import a2b_base64
from base64 import b64encode

class PEMCert():
	def __init__(self, filename):
		self.cipher = self.__load_cert__(filename)

	# Load public key from certificate in pem format
	def __load_cert__(self, filename):
		# From pem to der format
		pem_file = open(filename)
		pem_cert = ''.join(pem_file.read().splitlines()[1:-1])
		pem_file.close()
		der = a2b_base64(pem_cert)

		# Get public key from der sequence
		cert = DerSequence()
		cert.decode(der)
		tbsCert = DerSequence()
		tbsCert.decode(cert[0])
		publicKeyData = tbsCert[6]

		# Init encrypter with public key and pkcs padding
		publicKey = RSA.importKey(publicKeyData)
		return PKCS1_v1_5.new(publicKey)

	# Encrypt value
	def encrypt(self, value):
		return self.cipher.encrypt(bytes(value, 'ascii'))

	# Encrypt value and encode it in base64
	def b64encrypt(self, value):
		return b64encode(self.encrypt(value)).decode('ascii')
