'''
Copyright 2011 SRI International

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Created on May 6, 2011

@author: jklo
'''


MISSING_SIGNATURE = "MISSING_SIGNATURE"
MISSING_KEY_LOCATION = "MISSING_KEY_LOCATION"
BAD_KEY_OWNER = "BAD_KEY_OWNER"

class SignatureException(Exception):
    def __init__(self, message=None):
        Exception.__init__(self)
        self.message = message


class UnknownKeyException(SignatureException):
    '''
    Exception to be thrown when a key is not found in local keyring.
    '''

    def __init__(self, keyid):
        SignatureException.__init__(self)
        self.keyid = keyid


class UnsupportedSignatureAlgorithm(SignatureException):
    '''
    Exception to be thrown when an unsupported method of signing is encountered.

    Params:
        alg : the algorithm encountered
    '''

    def __init__(self, alg=None):
        '''
        Constructor
        '''
        Exception.__init__(self)
        self.alg = alg


class BadSignatureFormat(SignatureException):
    '''
    Exception to be thrown when a supported method of signing is advertised but not adhered.
    '''
    pass

class MissingPublicKey(SignatureException):
    '''
    Exception to be raised when the public key cannot be found.
    '''
    def __init__(self, message=None, keyid=None):
        Exception.__init__(self)
        self.message = message
        self.keyid = keyid


class InvalidPassphrase(SignatureException):
    '''
    Exception to be raised when an invalid passphrase is provided for key
    '''
    pass

class IncompatibleDocumentVersion(SignatureException):
    '''
    Exception to be raised when a document does not have a compatible version for the signer
    '''
    pass
