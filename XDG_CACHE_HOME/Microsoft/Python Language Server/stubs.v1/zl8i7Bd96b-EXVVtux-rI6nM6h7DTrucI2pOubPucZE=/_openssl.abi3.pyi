import builtins as _mod_builtins

__doc__ = None
__file__ = '/home/nj/.conda/envs/cs231n/lib/python3.6/site-packages/cryptography/hazmat/bindings/_openssl.abi3.so'
__name__ = 'cryptography.hazmat.bindings._openssl'
__package__ = 'cryptography.hazmat.bindings'
ffi = _mod_builtins.CompiledFFI()
class lib(_mod_builtins.object):
    @staticmethod
    def ACCESS_DESCRIPTION_free():
        'void ACCESS_DESCRIPTION_free(ACCESS_DESCRIPTION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ACCESS_DESCRIPTION_new():
        'ACCESS_DESCRIPTION *ACCESS_DESCRIPTION_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AES_set_decrypt_key():
        'int AES_set_decrypt_key(unsigned char *, int, AES_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AES_set_encrypt_key():
        'int AES_set_encrypt_key(unsigned char *, int, AES_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AES_unwrap_key():
        'int AES_unwrap_key(AES_KEY *, unsigned char *, unsigned char *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AES_wrap_key():
        'int AES_wrap_key(AES_KEY *, unsigned char *, unsigned char *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_BIT_STRING_free():
        'void ASN1_BIT_STRING_free(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_BIT_STRING_get_bit():
        'int ASN1_BIT_STRING_get_bit(struct asn1_string_st *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_BIT_STRING_new():
        'struct asn1_string_st *ASN1_BIT_STRING_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_BIT_STRING_set_bit():
        'int ASN1_BIT_STRING_set_bit(struct asn1_string_st *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_ENUMERATED_free():
        'void ASN1_ENUMERATED_free(ASN1_ENUMERATED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_ENUMERATED_get():
        'long ASN1_ENUMERATED_get(ASN1_ENUMERATED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_ENUMERATED_new():
        'ASN1_ENUMERATED *ASN1_ENUMERATED_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_ENUMERATED_set():
        'int ASN1_ENUMERATED_set(ASN1_ENUMERATED *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_GENERALIZEDTIME_free():
        'void ASN1_GENERALIZEDTIME_free(ASN1_GENERALIZEDTIME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_GENERALIZEDTIME_set():
        'ASN1_GENERALIZEDTIME *ASN1_GENERALIZEDTIME_set(ASN1_GENERALIZEDTIME *, int64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_IA5STRING_new():
        'struct asn1_string_st *ASN1_IA5STRING_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_free():
        'void ASN1_INTEGER_free(ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_set():
        'int ASN1_INTEGER_set(ASN1_INTEGER *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_INTEGER_to_BN():
        'BIGNUM *ASN1_INTEGER_to_BN(ASN1_INTEGER *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_NULL_new():
        'ASN1_NULL *ASN1_NULL_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OBJECT_free():
        'void ASN1_OBJECT_free(ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OCTET_STRING_free():
        'void ASN1_OCTET_STRING_free(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OCTET_STRING_new():
        'struct asn1_string_st *ASN1_OCTET_STRING_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_OCTET_STRING_set():
        'int ASN1_OCTET_STRING_set(struct asn1_string_st *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    ASN1_R_BOOLEAN_IS_WRONG_LENGTH = 106
    ASN1_R_BUFFER_TOO_SMALL = 107
    ASN1_R_CIPHER_HAS_NO_OBJECT_IDENTIFIER = 108
    ASN1_R_DATA_IS_WRONG = 109
    ASN1_R_DECODE_ERROR = 110
    ASN1_R_DEPTH_EXCEEDED = 174
    ASN1_R_ENCODE_ERROR = 112
    ASN1_R_ERROR_GETTING_TIME = 173
    ASN1_R_ERROR_LOADING_SECTION = 172
    ASN1_R_HEADER_TOO_LONG = 123
    ASN1_R_MSTRING_WRONG_TAG = 140
    ASN1_R_NESTED_ASN1_STRING = 197
    ASN1_R_NO_CONTENT_TYPE = 209
    ASN1_R_NO_MATCHING_CHOICE_TYPE = 143
    ASN1_R_NO_MULTIPART_BODY_FAILURE = 210
    ASN1_R_NO_MULTIPART_BOUNDARY = 211
    ASN1_R_UNKNOWN_MESSAGE_DIGEST_ALGORITHM = 161
    ASN1_R_UNKNOWN_OBJECT_TYPE = 162
    ASN1_R_UNKNOWN_PUBLIC_KEY_TYPE = 163
    ASN1_R_UNKNOWN_TAG = 194
    ASN1_R_UNSUPPORTED_ANY_DEFINED_BY_TYPE = 164
    ASN1_R_UNSUPPORTED_PUBLIC_KEY_TYPE = 167
    ASN1_R_UNSUPPORTED_TYPE = 196
    ASN1_R_WRONG_TAG = 168
    @staticmethod
    def ASN1_STRING_data():
        'unsigned char *ASN1_STRING_data(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_length():
        'int ASN1_STRING_length(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_set():
        'int ASN1_STRING_set(struct asn1_string_st *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_set_default_mask_asc():
        'int ASN1_STRING_set_default_mask_asc(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_to_UTF8():
        'int ASN1_STRING_to_UTF8(unsigned char * *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_STRING_type():
        'int ASN1_STRING_type(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_free():
        'void ASN1_TIME_free(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_new():
        'struct asn1_string_st *ASN1_TIME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_set():
        'struct asn1_string_st *ASN1_TIME_set(struct asn1_string_st *, int64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_set_string():
        'int ASN1_TIME_set_string(struct asn1_string_st *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_TIME_to_generalizedtime():
        'ASN1_GENERALIZEDTIME *ASN1_TIME_to_generalizedtime(struct asn1_string_st *, ASN1_GENERALIZEDTIME * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTF8STRING_free():
        'void ASN1_UTF8STRING_free(struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ASN1_UTF8STRING_new():
        'struct asn1_string_st *ASN1_UTF8STRING_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AUTHORITY_KEYID_free():
        'void AUTHORITY_KEYID_free(AUTHORITY_KEYID *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def AUTHORITY_KEYID_new():
        'AUTHORITY_KEYID *AUTHORITY_KEYID_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BASIC_CONSTRAINTS_free():
        'void BASIC_CONSTRAINTS_free(BASIC_CONSTRAINTS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BASIC_CONSTRAINTS_new():
        'BASIC_CONSTRAINTS *BASIC_CONSTRAINTS_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_clear_retry_flags():
        'void BIO_clear_retry_flags(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_ctrl_pending():
        'size_t BIO_ctrl_pending(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_free():
        'int BIO_free(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_get_mem_data():
        'long BIO_get_mem_data(BIO *, char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_gets():
        'int BIO_gets(BIO *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new():
        'BIO *BIO_new(BIO_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new_dgram():
        'BIO *BIO_new_dgram(int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new_file():
        'BIO *BIO_new_file(char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_new_mem_buf():
        'BIO *BIO_new_mem_buf(void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_read():
        'int BIO_read(BIO *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_reset():
        'int BIO_reset(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_s_datagram():
        'BIO_METHOD *BIO_s_datagram();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_s_mem():
        'BIO_METHOD *BIO_s_mem();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_mem_eof_return():
        'long BIO_set_mem_eof_return(BIO *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_set_retry_read():
        'void BIO_set_retry_read(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_should_io_special():
        'int BIO_should_io_special(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_should_read():
        'int BIO_should_read(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_should_retry():
        'int BIO_should_retry(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_should_write():
        'int BIO_should_write(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_up_ref():
        'int BIO_up_ref(BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BIO_write():
        'int BIO_write(BIO *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_end():
        'void BN_CTX_end(BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_free():
        'void BN_CTX_free(BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_get():
        'BIGNUM *BN_CTX_get(BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_new():
        'BN_CTX *BN_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_CTX_start():
        'void BN_CTX_start(BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    BN_FLG_CONSTTIME = 4
    @staticmethod
    def BN_MONT_CTX_free():
        'void BN_MONT_CTX_free(BN_MONT_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_MONT_CTX_new():
        'BN_MONT_CTX *BN_MONT_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_MONT_CTX_set():
        'int BN_MONT_CTX_set(BN_MONT_CTX *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_add():
        'int BN_add(BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_bin2bn():
        'BIGNUM *BN_bin2bn(unsigned char *, int, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_bn2bin():
        'int BN_bn2bin(BIGNUM *, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_bn2hex():
        'char *BN_bn2hex(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_clear_free():
        'void BN_clear_free(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_cmp():
        'int BN_cmp(BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_dup():
        'BIGNUM *BN_dup(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_free():
        'void BN_free(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_generate_prime_ex():
        'int BN_generate_prime_ex(BIGNUM *, int, int, BIGNUM *, BIGNUM *, BN_GENCB *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_hex2bn():
        'int BN_hex2bn(BIGNUM * *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_is_prime_ex():
        'int BN_is_prime_ex(BIGNUM *, int, BN_CTX *, BN_GENCB *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod():
        'int BN_mod(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_add():
        'int BN_mod_add(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_exp():
        'int BN_mod_exp(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_exp_mont():
        'int BN_mod_exp_mont(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *, BN_MONT_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_exp_mont_consttime():
        'int BN_mod_exp_mont_consttime(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *, BN_MONT_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_inverse():
        'BIGNUM *BN_mod_inverse(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_mul():
        'int BN_mod_mul(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_mod_sub():
        'int BN_mod_sub(BIGNUM *, BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_new():
        'BIGNUM *BN_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_nnmod():
        'int BN_nnmod(BIGNUM *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_num_bits():
        'int BN_num_bits(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_num_bytes():
        'int BN_num_bytes(BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_prime_checks_for_size():
        'int BN_prime_checks_for_size(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_rand_range():
        'int BN_rand_range(BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_set_flags():
        'void BN_set_flags(BIGNUM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_set_word():
        'int BN_set_word(BIGNUM *, uint64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_sub():
        'int BN_sub(BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_to_ASN1_INTEGER():
        'ASN1_INTEGER *BN_to_ASN1_INTEGER(BIGNUM *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def BN_value_one():
        'BIGNUM *BN_value_one();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CERTIFICATEPOLICIES_free():
        'void CERTIFICATEPOLICIES_free(Cryptography_STACK_OF_POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_CTX_copy():
        'int CMAC_CTX_copy(CMAC_CTX *, CMAC_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_CTX_free():
        'void CMAC_CTX_free(CMAC_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_CTX_new():
        'CMAC_CTX *CMAC_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_Final():
        'int CMAC_Final(CMAC_CTX *, unsigned char *, size_t *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_Init():
        'int CMAC_Init(CMAC_CTX *, void *, size_t, EVP_CIPHER *, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CMAC_Update():
        'int CMAC_Update(CMAC_CTX *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CRL_DIST_POINTS_free():
        'void CRL_DIST_POINTS_free(Cryptography_STACK_OF_DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    CRYPTOGRAPHY_IS_LIBRESSL = 0
    CRYPTOGRAPHY_LIBRESSL_28_OR_GREATER = 0
    CRYPTOGRAPHY_OPENSSL_102L_OR_GREATER = 1
    CRYPTOGRAPHY_OPENSSL_110F_OR_GREATER = 1
    CRYPTOGRAPHY_OPENSSL_110_OR_GREATER = 1
    CRYPTOGRAPHY_OPENSSL_LESS_THAN_102 = 0
    CRYPTOGRAPHY_OPENSSL_LESS_THAN_102I = 0
    CRYPTOGRAPHY_OPENSSL_LESS_THAN_111 = 0
    CRYPTOGRAPHY_OPENSSL_LESS_THAN_111B = 0
    @staticmethod
    def CRYPTOGRAPHY_PACKAGE_VERSION():
        pass
    
    CRYPTO_MEM_CHECK_DISABLE = 3
    CRYPTO_MEM_CHECK_ENABLE = 2
    CRYPTO_MEM_CHECK_OFF = 0
    CRYPTO_MEM_CHECK_ON = 1
    @staticmethod
    def CRYPTO_get_locking_callback():
        'void(*CRYPTO_get_locking_callback())(int, int, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def CRYPTO_mem_ctrl():
        'int CRYPTO_mem_ctrl(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    CT_LOG_ENTRY_TYPE_NOT_SET = -1
    CT_LOG_ENTRY_TYPE_PRECERT = 1
    CT_LOG_ENTRY_TYPE_X509 = 0
    @staticmethod
    def Cryptography_CRYPTO_set_mem_functions():
        'int Cryptography_CRYPTO_set_mem_functions(void *(*)(size_t, char *, int), void *(*)(void *, size_t, char *, int), void(*)(void *, char *, int));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_DH_check():
        'int Cryptography_DH_check(DH *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_DTLSv1_get_timeout():
        'long Cryptography_DTLSv1_get_timeout(SSL *, int64_t *, long *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_EVP_MD_CTX_free():
        'void Cryptography_EVP_MD_CTX_free(EVP_MD_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_EVP_MD_CTX_new():
        'EVP_MD_CTX *Cryptography_EVP_MD_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_EVP_PKEY_id():
        'int Cryptography_EVP_PKEY_id(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    Cryptography_HAS_102_VERIFICATION_ERROR_CODES = 1
    Cryptography_HAS_102_VERIFICATION_PARAMS = 1
    Cryptography_HAS_110_VERIFICATION_PARAMS = 1
    Cryptography_HAS_ALPN = 1
    Cryptography_HAS_CIPHER_DETAILS = 1
    Cryptography_HAS_COMPRESSION = 1
    Cryptography_HAS_CUSTOM_EXT = 1
    Cryptography_HAS_DTLS = 1
    Cryptography_HAS_EC2M = 1
    Cryptography_HAS_ECDSA = 1
    Cryptography_HAS_EC_1_0_2 = 1
    Cryptography_HAS_EC_CODES = 1
    Cryptography_HAS_ED25519 = 1
    Cryptography_HAS_ED448 = 1
    Cryptography_HAS_EGD = 0
    Cryptography_HAS_ENGINE = 1
    Cryptography_HAS_EVP_DIGESTFINAL_XOF = 1
    Cryptography_HAS_EVP_PKEY_DHX = 1
    Cryptography_HAS_EVP_PKEY_get_set_tls_encodedpoint = 1
    Cryptography_HAS_EVP_R_MEMORY_LIMIT_EXCEEDED = 1
    Cryptography_HAS_FIPS = 1
    Cryptography_HAS_GENERIC_DTLS_METHOD = 1
    Cryptography_HAS_GET_SERVER_TMP_KEY = 1
    Cryptography_HAS_LOCKING_CALLBACKS = 0
    Cryptography_HAS_MEM_FUNCTIONS = 1
    Cryptography_HAS_NEXTPROTONEG = 1
    Cryptography_HAS_ONESHOT_EVP_DIGEST_SIGN_VERIFY = 1
    Cryptography_HAS_OPENSSL_CLEANUP = 1
    Cryptography_HAS_OP_NO_COMPRESSION = 1
    Cryptography_HAS_PSK = 1
    Cryptography_HAS_PSS_PADDING = 1
    Cryptography_HAS_RAW_KEY = 1
    Cryptography_HAS_RELEASE_BUFFERS = 1
    Cryptography_HAS_RSA_OAEP_LABEL = 1
    Cryptography_HAS_RSA_OAEP_MD = 1
    Cryptography_HAS_RSA_R_PKCS_DECODING_ERROR = 1
    Cryptography_HAS_SCRYPT = 1
    Cryptography_HAS_SCT = 1
    Cryptography_HAS_SECURE_RENEGOTIATION = 1
    Cryptography_HAS_SET_CERT_CB = 1
    Cryptography_HAS_SET_ECDH_AUTO = 1
    Cryptography_HAS_SIGALGS = 1
    Cryptography_HAS_SSL2 = 0
    Cryptography_HAS_SSL3_METHOD = 0
    Cryptography_HAS_SSL_CTX_CLEAR_OPTIONS = 1
    Cryptography_HAS_SSL_CTX_SET_CLIENT_CERT_ENGINE = 1
    Cryptography_HAS_SSL_OP_MSIE_SSLV2_RSA_PADDING = 1
    Cryptography_HAS_SSL_OP_NO_TICKET = 1
    Cryptography_HAS_SSL_SET_SSL_CTX = 1
    Cryptography_HAS_SSL_ST = 0
    Cryptography_HAS_STATUS_REQ_OCSP_RESP = 1
    Cryptography_HAS_TLSEXT_HOSTNAME = 1
    Cryptography_HAS_TLSEXT_STATUS_REQ_CB = 1
    Cryptography_HAS_TLSEXT_STATUS_REQ_TYPE = 1
    Cryptography_HAS_TLS_ST = 1
    Cryptography_HAS_TLSv1_1 = 1
    Cryptography_HAS_TLSv1_2 = 1
    Cryptography_HAS_TLSv1_3 = 1
    Cryptography_HAS_X25519 = 1
    Cryptography_HAS_X448 = 1
    Cryptography_HAS_X509_STORE_CTX_GET_ISSUER = 1
    Cryptography_HAS_X509_V_FLAG_PARTIAL_CHAIN = 1
    Cryptography_HAS_X509_V_FLAG_TRUSTED_FIRST = 1
    @staticmethod
    def Cryptography_HMAC_CTX_free():
        'void Cryptography_HMAC_CTX_free(HMAC_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_HMAC_CTX_new():
        'HMAC_CTX *Cryptography_HMAC_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_X509_NAME_ENTRY_set():
        'int Cryptography_X509_NAME_ENTRY_set(X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_X509_REVOKED_dup():
        'X509_REVOKED *Cryptography_X509_REVOKED_dup(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_add_osrandom_engine():
        'int Cryptography_add_osrandom_engine();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_d2i_DHxparams_bio():
        'DH *Cryptography_d2i_DHxparams_bio(BIO *, DH * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_free_wrapper():
        'void Cryptography_free_wrapper(void *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_i2d_DHxparams_bio():
        'int Cryptography_i2d_DHxparams_bio(BIO *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_malloc_wrapper():
        'void *Cryptography_malloc_wrapper(size_t, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_osrandom_engine_id():
        pass
    
    @staticmethod
    def Cryptography_osrandom_engine_name():
        pass
    
    @staticmethod
    def Cryptography_pem_password_cb():
        'int Cryptography_pem_password_cb(char *, int, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_realloc_wrapper():
        'void *Cryptography_realloc_wrapper(void *, size_t, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def Cryptography_setup_ssl_threads():
        'int Cryptography_setup_ssl_threads();\n\nCFFI C function from _openssl.lib'
        pass
    
    DH_NOT_SUITABLE_GENERATOR = 8
    DH_R_INVALID_PUBKEY = 102
    @staticmethod
    def DH_compute_key():
        'int DH_compute_key(unsigned char *, BIGNUM *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_free():
        'void DH_free(DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_generate_key():
        'int DH_generate_key(DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_generate_parameters_ex():
        'int DH_generate_parameters_ex(DH *, int, int, BN_GENCB *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_get0_key():
        'void DH_get0_key(DH *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_get0_pqg():
        'void DH_get0_pqg(DH *, BIGNUM * *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_new():
        'DH *DH_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_set0_key():
        'int DH_set0_key(DH *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_set0_pqg():
        'int DH_set0_pqg(DH *, BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DH_size():
        'int DH_size(DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DHparams_dup():
        'DH *DHparams_dup(DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DIST_POINT_NAME_free():
        'void DIST_POINT_NAME_free(DIST_POINT_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DIST_POINT_NAME_new():
        'DIST_POINT_NAME *DIST_POINT_NAME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DIST_POINT_free():
        'void DIST_POINT_free(DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DIST_POINT_new():
        'DIST_POINT *DIST_POINT_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_free():
        'void DSA_free(DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_generate_key():
        'int DSA_generate_key(DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_generate_parameters_ex():
        'int DSA_generate_parameters_ex(DSA *, int, unsigned char *, int, int *, unsigned long *, BN_GENCB *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_get0_key():
        'void DSA_get0_key(DSA *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_get0_pqg():
        'void DSA_get0_pqg(DSA *, BIGNUM * *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_new():
        'DSA *DSA_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_set0_key():
        'int DSA_set0_key(DSA *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_set0_pqg():
        'int DSA_set0_pqg(DSA *, BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_sign():
        'int DSA_sign(int, unsigned char *, int, unsigned char *, unsigned int *, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_size():
        'int DSA_size(DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSA_verify():
        'int DSA_verify(int, unsigned char *, int, unsigned char *, int, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DSAparams_dup():
        'DSA *DSAparams_dup(DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLS_client_method():
        'SSL_METHOD *DTLS_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLS_get_link_min_mtu():
        'long DTLS_get_link_min_mtu(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLS_method():
        'SSL_METHOD *DTLS_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLS_server_method():
        'SSL_METHOD *DTLS_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLS_set_link_mtu():
        'long DTLS_set_link_mtu(SSL *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLSv1_client_method():
        'SSL_METHOD *DTLSv1_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLSv1_handle_timeout():
        'long DTLSv1_handle_timeout(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLSv1_method():
        'SSL_METHOD *DTLSv1_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def DTLSv1_server_method():
        'SSL_METHOD *DTLSv1_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDH_compute_key():
        'int ECDH_compute_key(void *, size_t, EC_POINT *, EC_KEY *, void *(*)(void *, size_t, void *, size_t *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_SIG_free():
        'void ECDSA_SIG_free(ECDSA_SIG *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_SIG_new():
        'ECDSA_SIG *ECDSA_SIG_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_do_sign():
        'ECDSA_SIG *ECDSA_do_sign(unsigned char *, int, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_do_verify():
        'int ECDSA_do_verify(unsigned char *, int, ECDSA_SIG *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_sign():
        'int ECDSA_sign(int, unsigned char *, int, unsigned char *, unsigned int *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_size():
        'int ECDSA_size(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ECDSA_verify():
        'int ECDSA_verify(int, unsigned char *, int, unsigned char *, int, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_free():
        'void EC_GROUP_free(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get0_generator():
        'EC_POINT *EC_GROUP_get0_generator(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get_curve_name():
        'int EC_GROUP_get_curve_name(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get_degree():
        'int EC_GROUP_get_degree(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_get_order():
        'int EC_GROUP_get_order(EC_GROUP *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_method_of():
        'EC_METHOD *EC_GROUP_method_of(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_GROUP_new_by_curve_name():
        'EC_GROUP *EC_GROUP_new_by_curve_name(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_free():
        'void EC_KEY_free(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_generate_key():
        'int EC_KEY_generate_key(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_get0_group():
        'EC_GROUP *EC_KEY_get0_group(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_get0_private_key():
        'BIGNUM *EC_KEY_get0_private_key(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_get0_public_key():
        'EC_POINT *EC_KEY_get0_public_key(EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_new():
        'EC_KEY *EC_KEY_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_new_by_curve_name():
        'EC_KEY *EC_KEY_new_by_curve_name(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_asn1_flag():
        'void EC_KEY_set_asn1_flag(EC_KEY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_group():
        'int EC_KEY_set_group(EC_KEY *, EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_private_key():
        'int EC_KEY_set_private_key(EC_KEY *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_public_key():
        'int EC_KEY_set_public_key(EC_KEY *, EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_KEY_set_public_key_affine_coordinates():
        'int EC_KEY_set_public_key_affine_coordinates(EC_KEY *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_METHOD_get_field_type():
        'int EC_METHOD_get_field_type(EC_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_add():
        'int EC_POINT_add(EC_GROUP *, EC_POINT *, EC_POINT *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_clear_free():
        'void EC_POINT_clear_free(EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_cmp():
        'int EC_POINT_cmp(EC_GROUP *, EC_POINT *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_dbl():
        'int EC_POINT_dbl(EC_GROUP *, EC_POINT *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_dup():
        'EC_POINT *EC_POINT_dup(EC_POINT *, EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_free():
        'void EC_POINT_free(EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_get_affine_coordinates_GF2m():
        'int EC_POINT_get_affine_coordinates_GF2m(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_get_affine_coordinates_GFp():
        'int EC_POINT_get_affine_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_invert():
        'int EC_POINT_invert(EC_GROUP *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_is_at_infinity():
        'int EC_POINT_is_at_infinity(EC_GROUP *, EC_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_is_on_curve():
        'int EC_POINT_is_on_curve(EC_GROUP *, EC_POINT *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_mul():
        'int EC_POINT_mul(EC_GROUP *, EC_POINT *, BIGNUM *, EC_POINT *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_new():
        'EC_POINT *EC_POINT_new(EC_GROUP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_oct2point():
        'int EC_POINT_oct2point(EC_GROUP *, EC_POINT *, unsigned char *, size_t, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_point2oct():
        'size_t EC_POINT_point2oct(EC_GROUP *, EC_POINT *, point_conversion_form_t, unsigned char *, size_t, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_affine_coordinates_GF2m():
        'int EC_POINT_set_affine_coordinates_GF2m(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_affine_coordinates_GFp():
        'int EC_POINT_set_affine_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, BIGNUM *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_compressed_coordinates_GF2m():
        'int EC_POINT_set_compressed_coordinates_GF2m(EC_GROUP *, EC_POINT *, BIGNUM *, int, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_POINT_set_compressed_coordinates_GFp():
        'int EC_POINT_set_compressed_coordinates_GFp(EC_GROUP *, EC_POINT *, BIGNUM *, int, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    EC_R_UNKNOWN_GROUP = 129
    @staticmethod
    def EC_curve_nid2nist():
        'char *EC_curve_nid2nist(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EC_get_builtin_curves():
        'size_t EC_get_builtin_curves(EC_builtin_curve *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_by_id():
        'ENGINE *ENGINE_by_id(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_ctrl_cmd():
        'int ENGINE_ctrl_cmd(ENGINE *, char *, long, void *, void(*)(), int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_finish():
        'int ENGINE_finish(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_free():
        'int ENGINE_free(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_default_RAND():
        'ENGINE *ENGINE_get_default_RAND();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_get_name():
        'char *ENGINE_get_name(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_init():
        'int ENGINE_init(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_set_default_RAND():
        'int ENGINE_set_default_RAND(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ENGINE_unregister_RAND():
        'void ENGINE_unregister_RAND(ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_GET_FUNC():
        'int ERR_GET_FUNC(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_GET_LIB():
        'int ERR_GET_LIB(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_GET_REASON():
        'int ERR_GET_REASON(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    ERR_LIB_ASN1 = 13
    ERR_LIB_DH = 5
    ERR_LIB_EC = 16
    ERR_LIB_EVP = 6
    ERR_LIB_PEM = 9
    ERR_LIB_PKCS12 = 35
    ERR_LIB_RSA = 4
    ERR_LIB_SSL = 20
    ERR_LIB_X509 = 11
    ERR_R_MALLOC_FAILURE = 65
    @staticmethod
    def ERR_clear_error():
        'void ERR_clear_error();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_error_string_n():
        'void ERR_error_string_n(unsigned long, char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_func_error_string():
        'char *ERR_func_error_string(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_get_error():
        'unsigned long ERR_get_error();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_lib_error_string():
        'char *ERR_lib_error_string(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_load_RAND_strings():
        'void ERR_load_RAND_strings();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_peek_error():
        'unsigned long ERR_peek_error();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_peek_last_error():
        'unsigned long ERR_peek_last_error();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_put_error():
        'void ERR_put_error(int, int, int, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ERR_reason_error_string():
        'char *ERR_reason_error_string(unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_cipher():
        'EVP_CIPHER *EVP_CIPHER_CTX_cipher(EVP_CIPHER_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_cleanup():
        'int EVP_CIPHER_CTX_cleanup(EVP_CIPHER_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_ctrl():
        'int EVP_CIPHER_CTX_ctrl(EVP_CIPHER_CTX *, int, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_free():
        'void EVP_CIPHER_CTX_free(EVP_CIPHER_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_new():
        'EVP_CIPHER_CTX *EVP_CIPHER_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_set_key_length():
        'int EVP_CIPHER_CTX_set_key_length(EVP_CIPHER_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CIPHER_CTX_set_padding():
        'int EVP_CIPHER_CTX_set_padding(EVP_CIPHER_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    EVP_CTRL_AEAD_GET_TAG = 16
    EVP_CTRL_AEAD_SET_IVLEN = 9
    EVP_CTRL_AEAD_SET_TAG = 17
    @staticmethod
    def EVP_CipherFinal_ex():
        'int EVP_CipherFinal_ex(EVP_CIPHER_CTX *, unsigned char *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CipherInit_ex():
        'int EVP_CipherInit_ex(EVP_CIPHER_CTX *, EVP_CIPHER *, ENGINE *, unsigned char *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_CipherUpdate():
        'int EVP_CipherUpdate(EVP_CIPHER_CTX *, unsigned char *, int *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestFinalXOF():
        'int EVP_DigestFinalXOF(EVP_MD_CTX *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestFinal_ex():
        'int EVP_DigestFinal_ex(EVP_MD_CTX *, unsigned char *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestInit_ex():
        'int EVP_DigestInit_ex(EVP_MD_CTX *, EVP_MD *, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestSign():
        'int EVP_DigestSign(EVP_MD_CTX *, unsigned char *, size_t *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestSignInit():
        'int EVP_DigestSignInit(EVP_MD_CTX *, EVP_PKEY_CTX * *, EVP_MD *, ENGINE *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestUpdate():
        'int EVP_DigestUpdate(EVP_MD_CTX *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestVerify():
        'int EVP_DigestVerify(EVP_MD_CTX *, unsigned char *, size_t, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_DigestVerifyInit():
        'int EVP_DigestVerifyInit(EVP_MD_CTX *, EVP_PKEY_CTX * *, EVP_MD *, ENGINE *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    EVP_F_EVP_ENCRYPTFINAL_EX = 127
    EVP_MAX_MD_SIZE = 64
    @staticmethod
    def EVP_MD_CTX_copy_ex():
        'int EVP_MD_CTX_copy_ex(EVP_MD_CTX *, EVP_MD_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PBE_scrypt():
        'int EVP_PBE_scrypt(char *, size_t, unsigned char *, size_t, uint64_t, uint64_t, uint64_t, uint64_t, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_dup():
        'EVP_PKEY_CTX *EVP_PKEY_CTX_dup(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_free():
        'void EVP_PKEY_CTX_free(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_new():
        'EVP_PKEY_CTX *EVP_PKEY_CTX_new(EVP_PKEY *, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_new_id():
        'EVP_PKEY_CTX *EVP_PKEY_CTX_new_id(int, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set0_rsa_oaep_label():
        'int EVP_PKEY_CTX_set0_rsa_oaep_label(EVP_PKEY_CTX *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_rsa_mgf1_md():
        'int EVP_PKEY_CTX_set_rsa_mgf1_md(EVP_PKEY_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_rsa_oaep_md():
        'int EVP_PKEY_CTX_set_rsa_oaep_md(EVP_PKEY_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_rsa_padding():
        'int EVP_PKEY_CTX_set_rsa_padding(EVP_PKEY_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_rsa_pss_saltlen():
        'int EVP_PKEY_CTX_set_rsa_pss_saltlen(EVP_PKEY_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_CTX_set_signature_md():
        'int EVP_PKEY_CTX_set_signature_md(EVP_PKEY_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    EVP_PKEY_DH = 28
    EVP_PKEY_DHX = 920
    EVP_PKEY_DSA = 116
    EVP_PKEY_EC = 408
    EVP_PKEY_ED25519 = 1087
    EVP_PKEY_ED448 = 1088
    EVP_PKEY_RSA = 6
    EVP_PKEY_X25519 = 1034
    EVP_PKEY_X448 = 1035
    @staticmethod
    def EVP_PKEY_assign_RSA():
        'int EVP_PKEY_assign_RSA(EVP_PKEY *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_bits():
        'int EVP_PKEY_bits(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_cmp():
        'int EVP_PKEY_cmp(EVP_PKEY *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_decrypt():
        'int EVP_PKEY_decrypt(EVP_PKEY_CTX *, unsigned char *, size_t *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_decrypt_init():
        'int EVP_PKEY_decrypt_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_derive():
        'int EVP_PKEY_derive(EVP_PKEY_CTX *, unsigned char *, size_t *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_derive_init():
        'int EVP_PKEY_derive_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_derive_set_peer():
        'int EVP_PKEY_derive_set_peer(EVP_PKEY_CTX *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_encrypt():
        'int EVP_PKEY_encrypt(EVP_PKEY_CTX *, unsigned char *, size_t *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_encrypt_init():
        'int EVP_PKEY_encrypt_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_free():
        'void EVP_PKEY_free(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_DH():
        'DH *EVP_PKEY_get1_DH(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_DSA():
        'DSA *EVP_PKEY_get1_DSA(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_EC_KEY():
        'EC_KEY *EVP_PKEY_get1_EC_KEY(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_RSA():
        'RSA *EVP_PKEY_get1_RSA(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get1_tls_encodedpoint():
        'size_t EVP_PKEY_get1_tls_encodedpoint(EVP_PKEY *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get_raw_private_key():
        'int EVP_PKEY_get_raw_private_key(EVP_PKEY *, unsigned char *, size_t *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_get_raw_public_key():
        'int EVP_PKEY_get_raw_public_key(EVP_PKEY *, unsigned char *, size_t *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_id():
        'int EVP_PKEY_id(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_keygen():
        'int EVP_PKEY_keygen(EVP_PKEY_CTX *, EVP_PKEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_keygen_init():
        'int EVP_PKEY_keygen_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_new():
        'EVP_PKEY *EVP_PKEY_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_new_raw_private_key():
        'EVP_PKEY *EVP_PKEY_new_raw_private_key(int, ENGINE *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_new_raw_public_key():
        'EVP_PKEY *EVP_PKEY_new_raw_public_key(int, ENGINE *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_DH():
        'int EVP_PKEY_set1_DH(EVP_PKEY *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_DSA():
        'int EVP_PKEY_set1_DSA(EVP_PKEY *, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_EC_KEY():
        'int EVP_PKEY_set1_EC_KEY(EVP_PKEY *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_RSA():
        'int EVP_PKEY_set1_RSA(EVP_PKEY *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set1_tls_encodedpoint():
        'int EVP_PKEY_set1_tls_encodedpoint(EVP_PKEY *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_set_type():
        'int EVP_PKEY_set_type(EVP_PKEY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_sign():
        'int EVP_PKEY_sign(EVP_PKEY_CTX *, unsigned char *, size_t *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_sign_init():
        'int EVP_PKEY_sign_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_size():
        'int EVP_PKEY_size(EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_type():
        'int EVP_PKEY_type(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_verify():
        'int EVP_PKEY_verify(EVP_PKEY_CTX *, unsigned char *, size_t, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_PKEY_verify_init():
        'int EVP_PKEY_verify_init(EVP_PKEY_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    EVP_R_AES_KEY_SETUP_FAILED = 143
    EVP_R_BAD_DECRYPT = 100
    EVP_R_CAMELLIA_KEY_SETUP_FAILED = 157
    EVP_R_CIPHER_PARAMETER_ERROR = 122
    EVP_R_CTRL_NOT_IMPLEMENTED = 132
    EVP_R_CTRL_OPERATION_NOT_IMPLEMENTED = 133
    EVP_R_DATA_NOT_MULTIPLE_OF_BLOCK_LENGTH = 138
    EVP_R_DECODE_ERROR = 114
    EVP_R_DIFFERENT_KEY_TYPES = 101
    EVP_R_INITIALIZATION_ERROR = 134
    EVP_R_INPUT_NOT_INITIALIZED = 111
    EVP_R_INVALID_KEY_LENGTH = 130
    EVP_R_KEYGEN_FAILURE = 120
    EVP_R_MEMORY_LIMIT_EXCEEDED = 172
    EVP_R_MISSING_PARAMETERS = 103
    EVP_R_NO_CIPHER_SET = 131
    EVP_R_NO_DIGEST_SET = 139
    EVP_R_PUBLIC_KEY_NOT_RSA = 106
    EVP_R_UNKNOWN_PBE_ALGORITHM = 121
    EVP_R_UNSUPPORTED_CIPHER = 107
    EVP_R_UNSUPPORTED_KEYLENGTH = 123
    EVP_R_UNSUPPORTED_KEY_DERIVATION_FUNCTION = 124
    EVP_R_UNSUPPORTED_PRIVATE_KEY_ALGORITHM = 118
    EVP_R_UNSUPPORTED_SALT_TYPE = 126
    EVP_R_WRONG_FINAL_BLOCK_LENGTH = 109
    @staticmethod
    def EVP_SignFinal():
        'int EVP_SignFinal(EVP_MD_CTX *, unsigned char *, unsigned int *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_SignInit():
        'int EVP_SignInit(EVP_MD_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_SignUpdate():
        'int EVP_SignUpdate(EVP_MD_CTX *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_VerifyFinal():
        'int EVP_VerifyFinal(EVP_MD_CTX *, unsigned char *, unsigned int, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_VerifyInit():
        'int EVP_VerifyInit(EVP_MD_CTX *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_VerifyUpdate():
        'int EVP_VerifyUpdate(EVP_MD_CTX *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_get_cipherbyname():
        'EVP_CIPHER *EVP_get_cipherbyname(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def EVP_get_digestbyname():
        'EVP_MD *EVP_get_digestbyname(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def FIPS_mode():
        'int FIPS_mode();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def FIPS_mode_set():
        'int FIPS_mode_set(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAMES_free():
        'void GENERAL_NAMES_free(struct stack_st_GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAMES_new():
        'struct stack_st_GENERAL_NAME *GENERAL_NAMES_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAME_free():
        'void GENERAL_NAME_free(GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAME_new():
        'GENERAL_NAME *GENERAL_NAME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_NAME_print():
        'int GENERAL_NAME_print(BIO *, GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def GENERAL_SUBTREE_new():
        'GENERAL_SUBTREE *GENERAL_SUBTREE_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    GEN_DIRNAME = 4
    GEN_DNS = 2
    GEN_EDIPARTY = 5
    GEN_EMAIL = 1
    GEN_IPADD = 7
    GEN_OTHERNAME = 0
    GEN_RID = 8
    GEN_URI = 6
    GEN_X400 = 3
    @staticmethod
    def HMAC_CTX_copy():
        'int HMAC_CTX_copy(HMAC_CTX *, HMAC_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def HMAC_Final():
        'int HMAC_Final(HMAC_CTX *, unsigned char *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def HMAC_Init_ex():
        'int HMAC_Init_ex(HMAC_CTX *, void *, int, EVP_MD *, ENGINE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def HMAC_Update():
        'int HMAC_Update(HMAC_CTX *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ISSUING_DIST_POINT_free():
        'void ISSUING_DIST_POINT_free(ISSUING_DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def ISSUING_DIST_POINT_new():
        'ISSUING_DIST_POINT *ISSUING_DIST_POINT_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    MBSTRING_UTF8 = 4096
    @staticmethod
    def NAME_CONSTRAINTS_free():
        'void NAME_CONSTRAINTS_free(NAME_CONSTRAINTS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NAME_CONSTRAINTS_new():
        'NAME_CONSTRAINTS *NAME_CONSTRAINTS_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_b64_decode():
        'NETSCAPE_SPKI *NETSCAPE_SPKI_b64_decode(char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_b64_encode():
        'char *NETSCAPE_SPKI_b64_encode(NETSCAPE_SPKI *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_free():
        'void NETSCAPE_SPKI_free(NETSCAPE_SPKI *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_get_pubkey():
        'EVP_PKEY *NETSCAPE_SPKI_get_pubkey(NETSCAPE_SPKI *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_new():
        'NETSCAPE_SPKI *NETSCAPE_SPKI_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_set_pubkey():
        'int NETSCAPE_SPKI_set_pubkey(NETSCAPE_SPKI *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_sign():
        'int NETSCAPE_SPKI_sign(NETSCAPE_SPKI *, EVP_PKEY *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NETSCAPE_SPKI_verify():
        'int NETSCAPE_SPKI_verify(NETSCAPE_SPKI *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    NID_ED25519 = 1087
    NID_ED448 = 1088
    NID_X25519 = 1034
    NID_X448 = 1035
    NID_crl_reason = 141
    NID_pbe_WithSHA1And3_Key_TripleDES_CBC = 146
    NID_subject_alt_name = 85
    NID_undef = 0
    @staticmethod
    def NOTICEREF_free():
        'void NOTICEREF_free(NOTICEREF *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def NOTICEREF_new():
        'NOTICEREF *NOTICEREF_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    OBJ_NAME_TYPE_MD_METH = 1
    @staticmethod
    def OBJ_NAME_do_all():
        'void OBJ_NAME_do_all(int, void(*)(OBJ_NAME *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_cleanup():
        'void OBJ_cleanup();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_cmp():
        'int OBJ_cmp(ASN1_OBJECT *, ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_create():
        'int OBJ_create(char *, char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_dup():
        'ASN1_OBJECT *OBJ_dup(ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_ln2nid():
        'int OBJ_ln2nid(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_nid2ln():
        'char *OBJ_nid2ln(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_nid2obj():
        'ASN1_OBJECT *OBJ_nid2obj(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_nid2sn():
        'char *OBJ_nid2sn(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_obj2nid():
        'int OBJ_obj2nid(ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_obj2txt():
        'int OBJ_obj2txt(char *, int, ASN1_OBJECT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_sn2nid():
        'int OBJ_sn2nid(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_txt2nid():
        'int OBJ_txt2nid(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OBJ_txt2obj():
        'ASN1_OBJECT *OBJ_txt2obj(char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_add_ext():
        'int OCSP_BASICRESP_add_ext(OCSP_BASICRESP *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_free():
        'void OCSP_BASICRESP_free(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_get_ext():
        'X509_EXTENSION *OCSP_BASICRESP_get_ext(OCSP_BASICRESP *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_get_ext_count():
        'int OCSP_BASICRESP_get_ext_count(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_BASICRESP_new():
        'OCSP_BASICRESP *OCSP_BASICRESP_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_CERTID_free():
        'void OCSP_CERTID_free(OCSP_CERTID *);\n\nCFFI C function from _openssl.lib'
        pass
    
    OCSP_NOCERTS = 1
    @staticmethod
    def OCSP_ONEREQ_get_ext():
        'X509_EXTENSION *OCSP_ONEREQ_get_ext(OCSP_ONEREQ *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_ONEREQ_get_ext_count():
        'int OCSP_ONEREQ_get_ext_count(OCSP_ONEREQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_REQUEST_add_ext():
        'int OCSP_REQUEST_add_ext(OCSP_REQUEST *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_REQUEST_free():
        'void OCSP_REQUEST_free(OCSP_REQUEST *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_REQUEST_get_ext():
        'X509_EXTENSION *OCSP_REQUEST_get_ext(OCSP_REQUEST *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_REQUEST_get_ext_count():
        'int OCSP_REQUEST_get_ext_count(OCSP_REQUEST *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_REQUEST_new():
        'OCSP_REQUEST *OCSP_REQUEST_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    OCSP_RESPID_KEY = 1024
    @staticmethod
    def OCSP_RESPONSE_free():
        'void OCSP_RESPONSE_free(OCSP_RESPONSE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_SINGLERESP_get0_id():
        'OCSP_CERTID *OCSP_SINGLERESP_get0_id(OCSP_SINGLERESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_SINGLERESP_get_ext():
        'X509_EXTENSION *OCSP_SINGLERESP_get_ext(OCSP_SINGLERESP *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_SINGLERESP_get_ext_count():
        'int OCSP_SINGLERESP_get_ext_count(OCSP_SINGLERESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_basic_add1_cert():
        'int OCSP_basic_add1_cert(OCSP_BASICRESP *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_basic_add1_nonce():
        'int OCSP_basic_add1_nonce(OCSP_BASICRESP *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_basic_add1_status():
        'OCSP_SINGLERESP *OCSP_basic_add1_status(OCSP_BASICRESP *, OCSP_CERTID *, int, int, struct asn1_string_st *, struct asn1_string_st *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_basic_sign():
        'int OCSP_basic_sign(OCSP_BASICRESP *, X509 *, EVP_PKEY *, EVP_MD *, Cryptography_STACK_OF_X509 *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_cert_to_id():
        'OCSP_CERTID *OCSP_cert_to_id(EVP_MD *, X509 *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_id_get0_info():
        'int OCSP_id_get0_info(struct asn1_string_st * *, ASN1_OBJECT * *, struct asn1_string_st * *, ASN1_INTEGER * *, OCSP_CERTID *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_onereq_get0_id():
        'OCSP_CERTID *OCSP_onereq_get0_id(OCSP_ONEREQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_request_add0_id():
        'OCSP_ONEREQ *OCSP_request_add0_id(OCSP_REQUEST *, OCSP_CERTID *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_request_add1_nonce():
        'int OCSP_request_add1_nonce(OCSP_REQUEST *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_request_onereq_count():
        'int OCSP_request_onereq_count(OCSP_REQUEST *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_request_onereq_get0():
        'OCSP_ONEREQ *OCSP_request_onereq_get0(OCSP_REQUEST *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_count():
        'int OCSP_resp_count(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_get0():
        'OCSP_SINGLERESP *OCSP_resp_get0(OCSP_BASICRESP *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_get0_certs():
        'Cryptography_STACK_OF_X509 *OCSP_resp_get0_certs(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_get0_id():
        'int OCSP_resp_get0_id(OCSP_BASICRESP *, struct asn1_string_st * *, X509_NAME * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_get0_produced_at():
        'ASN1_GENERALIZEDTIME *OCSP_resp_get0_produced_at(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_get0_respdata():
        'OCSP_RESPDATA *OCSP_resp_get0_respdata(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_get0_signature():
        'struct asn1_string_st *OCSP_resp_get0_signature(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_resp_get0_tbs_sigalg():
        'X509_ALGOR *OCSP_resp_get0_tbs_sigalg(OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_response_create():
        'OCSP_RESPONSE *OCSP_response_create(int, OCSP_BASICRESP *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_response_get1_basic():
        'OCSP_BASICRESP *OCSP_response_get1_basic(OCSP_RESPONSE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_response_status():
        'int OCSP_response_status(OCSP_RESPONSE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OCSP_single_get0_status():
        'int OCSP_single_get0_status(OCSP_SINGLERESP *, int *, ASN1_GENERALIZEDTIME * *, ASN1_GENERALIZEDTIME * *, ASN1_GENERALIZEDTIME * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    OPENSSL_BUILT_ON = 2
    OPENSSL_CFLAGS = 1
    OPENSSL_DIR = 4
    OPENSSL_EC_NAMED_CURVE = 1
    OPENSSL_NPN_NEGOTIATED = 1
    OPENSSL_PLATFORM = 3
    OPENSSL_VERSION = 0
    OPENSSL_VERSION_NUMBER = 269488175
    @staticmethod
    def OPENSSL_VERSION_TEXT():
        pass
    
    @staticmethod
    def OPENSSL_cleanup():
        'void OPENSSL_cleanup();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OPENSSL_config():
        'void OPENSSL_config(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OPENSSL_free():
        'void OPENSSL_free(void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OPENSSL_malloc():
        'void *OPENSSL_malloc(size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OPENSSL_no_config():
        'void OPENSSL_no_config();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OTHERNAME_free():
        'void OTHERNAME_free(OTHERNAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OTHERNAME_new():
        'OTHERNAME *OTHERNAME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OpenSSL_add_all_algorithms():
        'void OpenSSL_add_all_algorithms();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OpenSSL_version():
        'char *OpenSSL_version(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def OpenSSL_version_num():
        'unsigned long OpenSSL_version_num();\n\nCFFI C function from _openssl.lib'
        pass
    
    PEM_R_BAD_BASE64_DECODE = 100
    PEM_R_BAD_DECRYPT = 101
    PEM_R_BAD_END_LINE = 102
    PEM_R_BAD_IV_CHARS = 103
    PEM_R_BAD_PASSWORD_READ = 104
    PEM_R_ERROR_CONVERTING_PRIVATE_KEY = 115
    PEM_R_NOT_DEK_INFO = 105
    PEM_R_NOT_ENCRYPTED = 106
    PEM_R_NOT_PROC_TYPE = 107
    PEM_R_NO_START_LINE = 108
    PEM_R_PROBLEMS_GETTING_PASSWORD = 109
    PEM_R_READ_KEY = 111
    PEM_R_SHORT_HEADER = 112
    PEM_R_UNSUPPORTED_CIPHER = 113
    PEM_R_UNSUPPORTED_ENCRYPTION = 114
    @staticmethod
    def PEM_read_bio_DHparams():
        'DH *PEM_read_bio_DHparams(BIO *, DH * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_PKCS7():
        'PKCS7 *PEM_read_bio_PKCS7(BIO *, PKCS7 * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_PUBKEY():
        'EVP_PKEY *PEM_read_bio_PUBKEY(BIO *, EVP_PKEY * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_PrivateKey():
        'EVP_PKEY *PEM_read_bio_PrivateKey(BIO *, EVP_PKEY * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_RSAPublicKey():
        'RSA *PEM_read_bio_RSAPublicKey(BIO *, RSA * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_X509():
        'X509 *PEM_read_bio_X509(BIO *, X509 * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_X509_CRL():
        'X509_CRL *PEM_read_bio_X509_CRL(BIO *, X509_CRL * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_read_bio_X509_REQ():
        'X509_REQ *PEM_read_bio_X509_REQ(BIO *, X509_REQ * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_DHparams():
        'int PEM_write_bio_DHparams(BIO *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_DHxparams():
        'int PEM_write_bio_DHxparams(BIO *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_DSAPrivateKey():
        'int PEM_write_bio_DSAPrivateKey(BIO *, DSA *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_ECPrivateKey():
        'int PEM_write_bio_ECPrivateKey(BIO *, EC_KEY *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PKCS7():
        'int PEM_write_bio_PKCS7(BIO *, PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PKCS8PrivateKey():
        'int PEM_write_bio_PKCS8PrivateKey(BIO *, EVP_PKEY *, EVP_CIPHER *, char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PKCS8PrivateKey_nid():
        'int PEM_write_bio_PKCS8PrivateKey_nid(BIO *, EVP_PKEY *, int, char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PUBKEY():
        'int PEM_write_bio_PUBKEY(BIO *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_PrivateKey():
        'int PEM_write_bio_PrivateKey(BIO *, EVP_PKEY *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_RSAPrivateKey():
        'int PEM_write_bio_RSAPrivateKey(BIO *, RSA *, EVP_CIPHER *, unsigned char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_RSAPublicKey():
        'int PEM_write_bio_RSAPublicKey(BIO *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_X509():
        'int PEM_write_bio_X509(BIO *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_X509_CRL():
        'int PEM_write_bio_X509_CRL(BIO *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PEM_write_bio_X509_REQ():
        'int PEM_write_bio_X509_REQ(BIO *, X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    PKCS12_R_PKCS12_CIPHERFINAL_ERROR = 116
    @staticmethod
    def PKCS12_create():
        'PKCS12 *PKCS12_create(char *, char *, EVP_PKEY *, X509 *, Cryptography_STACK_OF_X509 *, int, int, int, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS12_free():
        'void PKCS12_free(PKCS12 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS12_parse():
        'int PKCS12_parse(PKCS12 *, char *, EVP_PKEY * *, X509 * *, Cryptography_STACK_OF_X509 * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS5_PBKDF2_HMAC():
        'int PKCS5_PBKDF2_HMAC(char *, int, unsigned char *, int, int, EVP_MD *, int, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS5_PBKDF2_HMAC_SHA1():
        'int PKCS5_PBKDF2_HMAC_SHA1(char *, int, unsigned char *, int, int, int, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    PKCS7_BINARY = 128
    PKCS7_DETACHED = 64
    PKCS7_NOATTR = 256
    PKCS7_NOCERTS = 2
    PKCS7_NOCHAIN = 8
    PKCS7_NOINTERN = 16
    PKCS7_NOSIGS = 4
    PKCS7_NOSMIMECAP = 512
    PKCS7_NOVERIFY = 32
    PKCS7_STREAM = 4096
    PKCS7_TEXT = 1
    @staticmethod
    def PKCS7_dataInit():
        'BIO *PKCS7_dataInit(PKCS7 *, BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_decrypt():
        'int PKCS7_decrypt(PKCS7 *, EVP_PKEY *, X509 *, BIO *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_encrypt():
        'PKCS7 *PKCS7_encrypt(Cryptography_STACK_OF_X509 *, BIO *, EVP_CIPHER *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_free():
        'void PKCS7_free(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_get0_signers():
        'Cryptography_STACK_OF_X509 *PKCS7_get0_signers(PKCS7 *, Cryptography_STACK_OF_X509 *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_sign():
        'PKCS7 *PKCS7_sign(X509 *, EVP_PKEY *, Cryptography_STACK_OF_X509 *, BIO *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_data():
        'int PKCS7_type_is_data(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_digest():
        'int PKCS7_type_is_digest(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_encrypted():
        'int PKCS7_type_is_encrypted(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_enveloped():
        'int PKCS7_type_is_enveloped(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_signed():
        'int PKCS7_type_is_signed(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_type_is_signedAndEnveloped():
        'int PKCS7_type_is_signedAndEnveloped(PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def PKCS7_verify():
        'int PKCS7_verify(PKCS7 *, Cryptography_STACK_OF_X509 *, X509_STORE *, BIO *, BIO *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    POINT_CONVERSION_COMPRESSED = 2
    POINT_CONVERSION_UNCOMPRESSED = 4
    @staticmethod
    def POLICYINFO_free():
        'void POLICYINFO_free(POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICYINFO_new():
        'POLICYINFO *POLICYINFO_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICYQUALINFO_free():
        'void POLICYQUALINFO_free(POLICYQUALINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICYQUALINFO_new():
        'POLICYQUALINFO *POLICYQUALINFO_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICY_CONSTRAINTS_free():
        'void POLICY_CONSTRAINTS_free(POLICY_CONSTRAINTS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def POLICY_CONSTRAINTS_new():
        'POLICY_CONSTRAINTS *POLICY_CONSTRAINTS_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_add():
        'void RAND_add(void *, int, double);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_bytes():
        'int RAND_bytes(unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_cleanup():
        'void RAND_cleanup();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RAND_status():
        'int RAND_status();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSAPublicKey_dup():
        'RSA *RSAPublicKey_dup(RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    RSA_F4 = 65537
    RSA_NO_PADDING = 3
    RSA_PKCS1_OAEP_PADDING = 4
    RSA_PKCS1_PADDING = 1
    RSA_PKCS1_PSS_PADDING = 6
    RSA_R_BLOCK_TYPE_IS_NOT_01 = 106
    RSA_R_BLOCK_TYPE_IS_NOT_02 = 107
    RSA_R_DATA_TOO_LARGE_FOR_KEY_SIZE = 110
    RSA_R_DATA_TOO_LARGE_FOR_MODULUS = 132
    RSA_R_DIGEST_TOO_BIG_FOR_RSA_KEY = 112
    RSA_R_OAEP_DECODING_ERROR = 121
    RSA_R_PKCS_DECODING_ERROR = 159
    @staticmethod
    def RSA_blinding_on():
        'int RSA_blinding_on(RSA *, BN_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_check_key():
        'int RSA_check_key(RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_free():
        'void RSA_free(RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_generate_key_ex():
        'int RSA_generate_key_ex(RSA *, int, BIGNUM *, BN_GENCB *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_get0_crt_params():
        'void RSA_get0_crt_params(RSA *, BIGNUM * *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_get0_factors():
        'void RSA_get0_factors(RSA *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_get0_key():
        'void RSA_get0_key(RSA *, BIGNUM * *, BIGNUM * *, BIGNUM * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_new():
        'RSA *RSA_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_print():
        'int RSA_print(BIO *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_private_decrypt():
        'int RSA_private_decrypt(int, unsigned char *, unsigned char *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_private_encrypt():
        'int RSA_private_encrypt(int, unsigned char *, unsigned char *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_public_decrypt():
        'int RSA_public_decrypt(int, unsigned char *, unsigned char *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_public_encrypt():
        'int RSA_public_encrypt(int, unsigned char *, unsigned char *, RSA *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_set0_crt_params():
        'int RSA_set0_crt_params(RSA *, BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_set0_factors():
        'int RSA_set0_factors(RSA *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_set0_key():
        'int RSA_set0_key(RSA *, BIGNUM *, BIGNUM *, BIGNUM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def RSA_size():
        'int RSA_size(RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_LIST_free():
        'void SCT_LIST_free(Cryptography_STACK_OF_SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    SCT_SOURCE_OCSP_STAPLED_RESPONSE = 3
    SCT_SOURCE_TLS_EXTENSION = 1
    SCT_SOURCE_UNKNOWN = 0
    SCT_SOURCE_X509V3_EXTENSION = 2
    SCT_VERSION_NOT_SET = -1
    SCT_VERSION_V1 = 0
    @staticmethod
    def SCT_get0_log_id():
        'size_t SCT_get0_log_id(SCT *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_get0_signature():
        'size_t SCT_get0_signature(SCT *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_get_log_entry_type():
        'ct_log_entry_type_t SCT_get_log_entry_type(SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_get_timestamp():
        'uint64_t SCT_get_timestamp(SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_get_version():
        'sct_version_t SCT_get_version(SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_new():
        'SCT *SCT_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_set1_log_id():
        'int SCT_set1_log_id(SCT *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_set_log_entry_type():
        'int SCT_set_log_entry_type(SCT *, ct_log_entry_type_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_set_source():
        'int SCT_set_source(SCT *, sct_source_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_set_timestamp():
        'void SCT_set_timestamp(SCT *, uint64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SCT_set_version():
        'int SCT_set_version(SCT *, sct_version_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SMIME_read_PKCS7():
        'PKCS7 *SMIME_read_PKCS7(BIO *, BIO * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SMIME_write_PKCS7():
        'int SMIME_write_PKCS7(BIO *, PKCS7 *, BIO *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    SSL3_RANDOM_SIZE = 32
    SSLEAY_BUILT_ON = 2
    SSLEAY_CFLAGS = 1
    SSLEAY_DIR = 4
    SSLEAY_PLATFORM = 3
    SSLEAY_VERSION = 0
    SSL_AD_ACCESS_DENIED = 49
    SSL_AD_BAD_CERTIFICATE = 42
    SSL_AD_BAD_CERTIFICATE_HASH_VALUE = 114
    SSL_AD_BAD_CERTIFICATE_STATUS_RESPONSE = 113
    SSL_AD_BAD_RECORD_MAC = 20
    SSL_AD_CERTIFICATE_EXPIRED = 45
    SSL_AD_CERTIFICATE_REVOKED = 44
    SSL_AD_CERTIFICATE_UNKNOWN = 46
    SSL_AD_CERTIFICATE_UNOBTAINABLE = 111
    SSL_AD_CLOSE_NOTIFY = 0
    SSL_AD_DECODE_ERROR = 50
    SSL_AD_DECOMPRESSION_FAILURE = 30
    SSL_AD_DECRYPT_ERROR = 51
    SSL_AD_HANDSHAKE_FAILURE = 40
    SSL_AD_ILLEGAL_PARAMETER = 47
    SSL_AD_INSUFFICIENT_SECURITY = 71
    SSL_AD_INTERNAL_ERROR = 80
    SSL_AD_NO_RENEGOTIATION = 100
    SSL_AD_PROTOCOL_VERSION = 70
    SSL_AD_RECORD_OVERFLOW = 22
    SSL_AD_UNEXPECTED_MESSAGE = 10
    SSL_AD_UNKNOWN_CA = 48
    SSL_AD_UNKNOWN_PSK_IDENTITY = 115
    SSL_AD_UNRECOGNIZED_NAME = 112
    SSL_AD_UNSUPPORTED_CERTIFICATE = 43
    SSL_AD_UNSUPPORTED_EXTENSION = 110
    SSL_AD_USER_CANCELLED = 90
    SSL_CB_ACCEPT_EXIT = 8194
    SSL_CB_ACCEPT_LOOP = 8193
    SSL_CB_ALERT = 16384
    SSL_CB_CONNECT_EXIT = 4098
    SSL_CB_CONNECT_LOOP = 4097
    SSL_CB_EXIT = 2
    SSL_CB_HANDSHAKE_DONE = 32
    SSL_CB_HANDSHAKE_START = 16
    SSL_CB_LOOP = 1
    SSL_CB_READ = 4
    SSL_CB_READ_ALERT = 16388
    SSL_CB_WRITE = 8
    SSL_CB_WRITE_ALERT = 16392
    @staticmethod
    def SSL_CIPHER_description():
        'char *SSL_CIPHER_description(SSL_CIPHER *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_auth_nid():
        'int SSL_CIPHER_get_auth_nid(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_bits():
        'int SSL_CIPHER_get_bits(SSL_CIPHER *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_cipher_nid():
        'int SSL_CIPHER_get_cipher_nid(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_digest_nid():
        'int SSL_CIPHER_get_digest_nid(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_id():
        'uint64_t SSL_CIPHER_get_id(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_kx_nid():
        'int SSL_CIPHER_get_kx_nid(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_name():
        'char *SSL_CIPHER_get_name(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_get_version():
        'char *SSL_CIPHER_get_version(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CIPHER_is_aead():
        'int SSL_CIPHER_is_aead(SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_COMP_get_name():
        'char *SSL_COMP_get_name(COMP_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_add_client_CA():
        'int SSL_CTX_add_client_CA(SSL_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_add_client_custom_ext():
        'int SSL_CTX_add_client_custom_ext(SSL_CTX *, unsigned int, int(*)(SSL *, unsigned int, unsigned char * *, size_t *, int *, void *), void(*)(SSL *, unsigned int, unsigned char *, void *), void *, int(*)(SSL *, unsigned int, unsigned char *, size_t, int *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_add_extra_chain_cert():
        'unsigned long SSL_CTX_add_extra_chain_cert(SSL_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_add_server_custom_ext():
        'int SSL_CTX_add_server_custom_ext(SSL_CTX *, unsigned int, int(*)(SSL *, unsigned int, unsigned char * *, size_t *, int *, void *), void(*)(SSL *, unsigned int, unsigned char *, void *), void *, int(*)(SSL *, unsigned int, unsigned char *, size_t, int *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_check_private_key():
        'int SSL_CTX_check_private_key(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_clear_options():
        'unsigned long SSL_CTX_clear_options(SSL_CTX *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_free():
        'void SSL_CTX_free(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_cert_store():
        'X509_STORE *SSL_CTX_get_cert_store(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_ex_data():
        'void *SSL_CTX_get_ex_data(SSL_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_ex_new_index():
        'int SSL_CTX_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_info_callback():
        'void(*SSL_CTX_get_info_callback(SSL_CTX *))(SSL *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_mode():
        'unsigned long SSL_CTX_get_mode(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_options():
        'unsigned long SSL_CTX_get_options(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_read_ahead():
        'long SSL_CTX_get_read_ahead(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_session_cache_mode():
        'unsigned long SSL_CTX_get_session_cache_mode(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_ssl_method():
        'SSL_METHOD *SSL_CTX_get_ssl_method(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_timeout():
        'long SSL_CTX_get_timeout(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_verify_callback():
        'int(*SSL_CTX_get_verify_callback(SSL_CTX *))(int, X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_verify_depth():
        'int SSL_CTX_get_verify_depth(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_get_verify_mode():
        'int SSL_CTX_get_verify_mode(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_load_verify_locations():
        'int SSL_CTX_load_verify_locations(SSL_CTX *, char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_new():
        'SSL_CTX *SSL_CTX_new(SSL_METHOD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_accept():
        'long SSL_CTX_sess_accept(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_accept_good():
        'long SSL_CTX_sess_accept_good(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_accept_renegotiate():
        'long SSL_CTX_sess_accept_renegotiate(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_cache_full():
        'long SSL_CTX_sess_cache_full(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_cb_hits():
        'long SSL_CTX_sess_cb_hits(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_connect():
        'long SSL_CTX_sess_connect(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_connect_good():
        'long SSL_CTX_sess_connect_good(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_connect_renegotiate():
        'long SSL_CTX_sess_connect_renegotiate(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_hits():
        'long SSL_CTX_sess_hits(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_misses():
        'long SSL_CTX_sess_misses(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_number():
        'long SSL_CTX_sess_number(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_sess_timeouts():
        'long SSL_CTX_sess_timeouts(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set1_sigalgs_list():
        'long SSL_CTX_set1_sigalgs_list(SSL_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_alpn_protos():
        'int SSL_CTX_set_alpn_protos(SSL_CTX *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_alpn_select_cb():
        'void SSL_CTX_set_alpn_select_cb(SSL_CTX *, int(*)(SSL *, unsigned char * *, unsigned char *, unsigned char *, unsigned int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_cert_cb():
        'void SSL_CTX_set_cert_cb(SSL_CTX *, int(*)(SSL *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_cert_store():
        'void SSL_CTX_set_cert_store(SSL_CTX *, X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_cert_verify_callback():
        'void SSL_CTX_set_cert_verify_callback(SSL_CTX *, int(*)(X509_STORE_CTX *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_cipher_list():
        'int SSL_CTX_set_cipher_list(SSL_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_ciphersuites():
        'int SSL_CTX_set_ciphersuites(SSL_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_client_CA_list():
        'void SSL_CTX_set_client_CA_list(SSL_CTX *, Cryptography_STACK_OF_X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_cookie_generate_cb():
        'void SSL_CTX_set_cookie_generate_cb(SSL_CTX *, int(*)(SSL *, unsigned char *, unsigned int *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_default_passwd_cb():
        'void SSL_CTX_set_default_passwd_cb(SSL_CTX *, int(*)(char *, int, int, void *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_default_passwd_cb_userdata():
        'void SSL_CTX_set_default_passwd_cb_userdata(SSL_CTX *, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_default_verify_paths():
        'int SSL_CTX_set_default_verify_paths(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_ecdh_auto():
        'long SSL_CTX_set_ecdh_auto(SSL_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_ex_data():
        'int SSL_CTX_set_ex_data(SSL_CTX *, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_info_callback():
        'void SSL_CTX_set_info_callback(SSL_CTX *, void(*)(SSL *, int, int));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_max_early_data():
        'int SSL_CTX_set_max_early_data(SSL_CTX *, uint32_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_mode():
        'unsigned long SSL_CTX_set_mode(SSL_CTX *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_next_proto_select_cb():
        'void SSL_CTX_set_next_proto_select_cb(SSL_CTX *, int(*)(SSL *, unsigned char * *, unsigned char *, unsigned char *, unsigned int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_next_protos_advertised_cb():
        'void SSL_CTX_set_next_protos_advertised_cb(SSL_CTX *, int(*)(SSL *, unsigned char * *, unsigned int *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_options():
        'unsigned long SSL_CTX_set_options(SSL_CTX *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_post_handshake_auth():
        'void SSL_CTX_set_post_handshake_auth(SSL_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_psk_client_callback():
        'void SSL_CTX_set_psk_client_callback(SSL_CTX *, unsigned int(*)(SSL *, char *, char *, unsigned int, unsigned char *, unsigned int));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_psk_server_callback():
        'void SSL_CTX_set_psk_server_callback(SSL_CTX *, unsigned int(*)(SSL *, char *, unsigned char *, unsigned int));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_read_ahead():
        'long SSL_CTX_set_read_ahead(SSL_CTX *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_session_cache_mode():
        'unsigned long SSL_CTX_set_session_cache_mode(SSL_CTX *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_session_id_context():
        'int SSL_CTX_set_session_id_context(SSL_CTX *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_timeout():
        'long SSL_CTX_set_timeout(SSL_CTX *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tlsext_servername_arg():
        'void SSL_CTX_set_tlsext_servername_arg(SSL_CTX *, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tlsext_servername_callback():
        'void SSL_CTX_set_tlsext_servername_callback(SSL_CTX *, int(*)(SSL *, int *, void *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tlsext_status_arg():
        'long SSL_CTX_set_tlsext_status_arg(SSL_CTX *, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tlsext_status_cb():
        'long SSL_CTX_set_tlsext_status_cb(SSL_CTX *, int(*)(SSL *, void *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tlsext_use_srtp():
        'int SSL_CTX_set_tlsext_use_srtp(SSL_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tmp_dh():
        'unsigned long SSL_CTX_set_tmp_dh(SSL_CTX *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_tmp_ecdh():
        'unsigned long SSL_CTX_set_tmp_ecdh(SSL_CTX *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_verify():
        'void SSL_CTX_set_verify(SSL_CTX *, int, int(*)(int, X509_STORE_CTX *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_set_verify_depth():
        'void SSL_CTX_set_verify_depth(SSL_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_PrivateKey():
        'int SSL_CTX_use_PrivateKey(SSL_CTX *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_PrivateKey_ASN1():
        'int SSL_CTX_use_PrivateKey_ASN1(int, SSL_CTX *, unsigned char *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_PrivateKey_file():
        'int SSL_CTX_use_PrivateKey_file(SSL_CTX *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_certificate():
        'int SSL_CTX_use_certificate(SSL_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_certificate_ASN1():
        'int SSL_CTX_use_certificate_ASN1(SSL_CTX *, int, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_certificate_chain_file():
        'int SSL_CTX_use_certificate_chain_file(SSL_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_certificate_file():
        'int SSL_CTX_use_certificate_file(SSL_CTX *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_CTX_use_psk_identity_hint():
        'int SSL_CTX_use_psk_identity_hint(SSL_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    SSL_ERROR_NONE = 0
    SSL_ERROR_SSL = 1
    SSL_ERROR_SYSCALL = 5
    SSL_ERROR_WANT_CONNECT = 7
    SSL_ERROR_WANT_READ = 2
    SSL_ERROR_WANT_WRITE = 3
    SSL_ERROR_WANT_X509_LOOKUP = 4
    SSL_ERROR_ZERO_RETURN = 6
    SSL_FILETYPE_ASN1 = 2
    SSL_FILETYPE_PEM = 1
    SSL_MODE_ACCEPT_MOVING_WRITE_BUFFER = 2
    SSL_MODE_AUTO_RETRY = 4
    SSL_MODE_ENABLE_PARTIAL_WRITE = 1
    SSL_MODE_RELEASE_BUFFERS = 16
    SSL_OP_ALL = 2147485780
    SSL_OP_ALLOW_UNSAFE_LEGACY_RENEGOTIATION = 262144
    SSL_OP_CIPHER_SERVER_PREFERENCE = 4194304
    SSL_OP_COOKIE_EXCHANGE = 8192
    SSL_OP_DONT_INSERT_EMPTY_FRAGMENTS = 2048
    SSL_OP_EPHEMERAL_RSA = 0
    SSL_OP_LEGACY_SERVER_CONNECT = 4
    SSL_OP_MICROSOFT_BIG_SSLV3_BUFFER = 0
    SSL_OP_MICROSOFT_SESS_ID_BUG = 0
    SSL_OP_MSIE_SSLV2_RSA_PADDING = 0
    SSL_OP_NETSCAPE_CA_DN_BUG = 0
    SSL_OP_NETSCAPE_CHALLENGE_BUG = 0
    SSL_OP_NETSCAPE_DEMO_CIPHER_CHANGE_BUG = 0
    SSL_OP_NETSCAPE_REUSE_CIPHER_CHANGE_BUG = 0
    SSL_OP_NO_COMPRESSION = 131072
    SSL_OP_NO_DTLSv1 = 67108864
    SSL_OP_NO_DTLSv1_2 = 134217728
    SSL_OP_NO_QUERY_MTU = 4096
    SSL_OP_NO_SSLv2 = 0
    SSL_OP_NO_SSLv3 = 33554432
    SSL_OP_NO_TICKET = 16384
    SSL_OP_NO_TLSv1 = 67108864
    SSL_OP_NO_TLSv1_1 = 268435456
    SSL_OP_NO_TLSv1_2 = 134217728
    SSL_OP_NO_TLSv1_3 = 536870912
    SSL_OP_PKCS1_CHECK_1 = 0
    SSL_OP_PKCS1_CHECK_2 = 0
    SSL_OP_SINGLE_DH_USE = 0
    SSL_OP_SINGLE_ECDH_USE = 0
    SSL_OP_SSLEAY_080_CLIENT_DH_BUG = 0
    SSL_OP_SSLREF2_REUSE_CERT_TYPE_BUG = 0
    SSL_OP_TLS_BLOCK_PADDING_BUG = 0
    SSL_OP_TLS_D5_BUG = 0
    SSL_OP_TLS_ROLLBACK_BUG = 8388608
    SSL_RECEIVED_SHUTDOWN = 2
    SSL_SENT_SHUTDOWN = 1
    @staticmethod
    def SSL_SESSION_free():
        'void SSL_SESSION_free(SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_get_id():
        'unsigned char *SSL_SESSION_get_id(SSL_SESSION *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_get_master_key():
        'size_t SSL_SESSION_get_master_key(SSL_SESSION *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_get_max_early_data():
        'uint32_t SSL_SESSION_get_max_early_data(SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_get_ticket_lifetime_hint():
        'long SSL_SESSION_get_ticket_lifetime_hint(SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_get_time():
        'long SSL_SESSION_get_time(SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_get_timeout():
        'long SSL_SESSION_get_timeout(SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_has_ticket():
        'int SSL_SESSION_has_ticket(SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_print():
        'int SSL_SESSION_print(BIO *, SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_SESSION_set1_id_context():
        'int SSL_SESSION_set1_id_context(SSL_SESSION *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    SSL_SESS_CACHE_BOTH = 3
    SSL_SESS_CACHE_CLIENT = 1
    SSL_SESS_CACHE_NO_AUTO_CLEAR = 128
    SSL_SESS_CACHE_NO_INTERNAL = 768
    SSL_SESS_CACHE_NO_INTERNAL_LOOKUP = 256
    SSL_SESS_CACHE_NO_INTERNAL_STORE = 512
    SSL_SESS_CACHE_OFF = 0
    SSL_SESS_CACHE_SERVER = 2
    SSL_ST_ACCEPT = 8192
    SSL_ST_BEFORE = 0
    SSL_ST_CONNECT = 4096
    SSL_ST_INIT = 0
    SSL_ST_MASK = 4095
    SSL_ST_OK = 0
    SSL_ST_RENEGOTIATE = 0
    SSL_TLSEXT_ERR_ALERT_FATAL = 2
    SSL_TLSEXT_ERR_ALERT_WARNING = 1
    SSL_TLSEXT_ERR_NOACK = 3
    SSL_TLSEXT_ERR_OK = 0
    SSL_VERIFY_CLIENT_ONCE = 4
    SSL_VERIFY_FAIL_IF_NO_PEER_CERT = 2
    SSL_VERIFY_NONE = 0
    SSL_VERIFY_PEER = 1
    SSL_VERIFY_POST_HANDSHAKE = 8
    @staticmethod
    def SSL_check_private_key():
        'int SSL_check_private_key(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_do_handshake():
        'int SSL_do_handshake(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_export_keying_material():
        'int SSL_export_keying_material(SSL *, unsigned char *, size_t, char *, size_t, unsigned char *, size_t, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_extension_supported():
        'int SSL_extension_supported(unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_free():
        'void SSL_free(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get0_alpn_selected():
        'void SSL_get0_alpn_selected(SSL *, unsigned char * *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get0_next_proto_negotiated():
        'void SSL_get0_next_proto_negotiated(SSL *, unsigned char * *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get0_param():
        'X509_VERIFY_PARAM *SSL_get0_param(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get1_session():
        'SSL_SESSION *SSL_get1_session(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_SSL_CTX():
        'SSL_CTX *SSL_get_SSL_CTX(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_app_data():
        'char *SSL_get_app_data(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_certificate():
        'X509 *SSL_get_certificate(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_cipher_list():
        'char *SSL_get_cipher_list(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_ciphers():
        'Cryptography_STACK_OF_SSL_CIPHER *SSL_get_ciphers(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_client_CA_list():
        'Cryptography_STACK_OF_X509_NAME *SSL_get_client_CA_list(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_client_random():
        'size_t SSL_get_client_random(SSL *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_current_cipher():
        'SSL_CIPHER *SSL_get_current_cipher(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_current_compression():
        'COMP_METHOD *SSL_get_current_compression(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_current_expansion():
        'COMP_METHOD *SSL_get_current_expansion(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_error():
        'int SSL_get_error(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_ex_data():
        'void *SSL_get_ex_data(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_ex_data_X509_STORE_CTX_idx():
        'int SSL_get_ex_data_X509_STORE_CTX_idx();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_ex_new_index():
        'int SSL_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_finished():
        'size_t SSL_get_finished(SSL *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_info_callback():
        'void(*SSL_get_info_callback(SSL *))(SSL *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_mode():
        'unsigned long SSL_get_mode(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_options():
        'unsigned long SSL_get_options(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_peer_cert_chain():
        'Cryptography_STACK_OF_X509 *SSL_get_peer_cert_chain(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_peer_certificate():
        'X509 *SSL_get_peer_certificate(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_peer_finished():
        'size_t SSL_get_peer_finished(SSL *, void *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_rbio():
        'BIO *SSL_get_rbio(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_secure_renegotiation_support():
        'long SSL_get_secure_renegotiation_support(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_selected_srtp_profile():
        'SRTP_PROTECTION_PROFILE *SSL_get_selected_srtp_profile(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_server_random():
        'size_t SSL_get_server_random(SSL *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_server_tmp_key():
        'long SSL_get_server_tmp_key(SSL *, EVP_PKEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_servername():
        'char *SSL_get_servername(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_session():
        'SSL_SESSION *SSL_get_session(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_shutdown():
        'int SSL_get_shutdown(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_sigalgs():
        'int SSL_get_sigalgs(SSL *, int, int *, int *, int *, unsigned char *, unsigned char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_tlsext_status_ocsp_resp():
        'long SSL_get_tlsext_status_ocsp_resp(SSL *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_verify_callback():
        'int(*SSL_get_verify_callback(SSL *))(int, X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_verify_depth():
        'int SSL_get_verify_depth(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_verify_mode():
        'int SSL_get_verify_mode(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_version():
        'char *SSL_get_version(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_get_wbio():
        'BIO *SSL_get_wbio(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_library_init():
        'int SSL_library_init();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_load_client_CA_file():
        'Cryptography_STACK_OF_X509_NAME *SSL_load_client_CA_file(char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_load_error_strings():
        'void SSL_load_error_strings();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_new():
        'SSL *SSL_new(SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_peek():
        'int SSL_peek(SSL *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_pending():
        'int SSL_pending(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_read():
        'int SSL_read(SSL *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_read_early_data():
        'int SSL_read_early_data(SSL *, void *, size_t, size_t *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_renegotiate():
        'int SSL_renegotiate(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_renegotiate_pending():
        'int SSL_renegotiate_pending(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_select_next_proto():
        'int SSL_select_next_proto(unsigned char * *, unsigned char *, unsigned char *, unsigned int, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_session_reused():
        'long SSL_session_reused(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_SSL_CTX():
        'SSL_CTX *SSL_set_SSL_CTX(SSL *, SSL_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_accept_state():
        'void SSL_set_accept_state(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_alpn_protos():
        'int SSL_set_alpn_protos(SSL *, unsigned char *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_app_data():
        'void SSL_set_app_data(SSL *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_bio():
        'void SSL_set_bio(SSL *, BIO *, BIO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_cert_cb():
        'void SSL_set_cert_cb(SSL *, int(*)(SSL *, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_connect_state():
        'void SSL_set_connect_state(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_ex_data():
        'int SSL_set_ex_data(SSL *, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_fd():
        'int SSL_set_fd(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_info_callback():
        'void SSL_set_info_callback(SSL *, void(*)(SSL *, int, int));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_mode():
        'unsigned long SSL_set_mode(SSL *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_options():
        'unsigned long SSL_set_options(SSL *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_post_handshake_auth():
        'void SSL_set_post_handshake_auth(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_read_ahead():
        'void SSL_set_read_ahead(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_session():
        'int SSL_set_session(SSL *, SSL_SESSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_shutdown():
        'void SSL_set_shutdown(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_tlsext_host_name():
        'void SSL_set_tlsext_host_name(SSL *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_tlsext_status_ocsp_resp():
        'long SSL_set_tlsext_status_ocsp_resp(SSL *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_tlsext_status_type():
        'long SSL_set_tlsext_status_type(SSL *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_tlsext_use_srtp():
        'int SSL_set_tlsext_use_srtp(SSL *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_verify():
        'void SSL_set_verify(SSL *, int, int(*)(int, X509_STORE_CTX *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_set_verify_depth():
        'void SSL_set_verify_depth(SSL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_shutdown():
        'int SSL_shutdown(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_state_string_long():
        'char *SSL_state_string_long(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_total_renegotiations():
        'long SSL_total_renegotiations(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_PrivateKey():
        'int SSL_use_PrivateKey(SSL *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_PrivateKey_ASN1():
        'int SSL_use_PrivateKey_ASN1(int, SSL *, unsigned char *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_PrivateKey_file():
        'int SSL_use_PrivateKey_file(SSL *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_certificate():
        'int SSL_use_certificate(SSL *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_certificate_ASN1():
        'int SSL_use_certificate_ASN1(SSL *, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_use_certificate_file():
        'int SSL_use_certificate_file(SSL *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_verify_client_post_handshake():
        'int SSL_verify_client_post_handshake(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_version():
        'int SSL_version(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_want_read():
        'int SSL_want_read(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_want_write():
        'int SSL_want_write(SSL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_write():
        'int SSL_write(SSL *, void *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSL_write_early_data():
        'int SSL_write_early_data(SSL *, void *, size_t, size_t *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLeay():
        'unsigned long SSLeay();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLeay_version():
        'char *SSLeay_version(int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv23_client_method():
        'SSL_METHOD *SSLv23_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv23_method():
        'SSL_METHOD *SSLv23_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv23_server_method():
        'SSL_METHOD *SSLv23_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv3_client_method():
        'SSL_METHOD *SSLv3_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv3_method():
        'SSL_METHOD *SSLv3_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def SSLv3_server_method():
        'SSL_METHOD *SSLv3_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    TLSEXT_NAMETYPE_host_name = 0
    TLSEXT_STATUSTYPE_ocsp = 1
    TLS_ST_BEFORE = 0
    TLS_ST_OK = 1
    @staticmethod
    def TLSv1_1_client_method():
        'SSL_METHOD *TLSv1_1_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_1_method():
        'SSL_METHOD *TLSv1_1_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_1_server_method():
        'SSL_METHOD *TLSv1_1_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_2_client_method():
        'SSL_METHOD *TLSv1_2_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_2_method():
        'SSL_METHOD *TLSv1_2_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_2_server_method():
        'SSL_METHOD *TLSv1_2_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_client_method():
        'SSL_METHOD *TLSv1_client_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_method():
        'SSL_METHOD *TLSv1_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def TLSv1_server_method():
        'SSL_METHOD *TLSv1_server_method();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def USERNOTICE_free():
        'void USERNOTICE_free(USERNOTICE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def USERNOTICE_new():
        'USERNOTICE *USERNOTICE_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    V_ASN1_GENERALIZEDTIME = 24
    @staticmethod
    def X509V3_EXT_add_alias():
        'int X509V3_EXT_add_alias(int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_conf_nid():
        'X509_EXTENSION *X509V3_EXT_conf_nid(Cryptography_LHASH_OF_CONF_VALUE *, X509V3_CTX *, int, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_d2i():
        'void *X509V3_EXT_d2i(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_i2d():
        'X509_EXTENSION *X509V3_EXT_i2d(int, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_nconf():
        'X509_EXTENSION *X509V3_EXT_nconf(CONF *, X509V3_CTX *, char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_EXT_print():
        'int X509V3_EXT_print(BIO *, X509_EXTENSION *, unsigned long, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_set_ctx():
        'void X509V3_set_ctx(X509V3_CTX *, X509 *, X509 *, X509_REQ *, X509_CRL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509V3_set_ctx_nodb():
        'void *X509V3_set_ctx_nodb(X509V3_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    X509_CHECK_FLAG_ALWAYS_CHECK_SUBJECT = 1
    X509_CHECK_FLAG_MULTI_LABEL_WILDCARDS = 8
    X509_CHECK_FLAG_NEVER_CHECK_SUBJECT = 32
    X509_CHECK_FLAG_NO_PARTIAL_WILDCARDS = 4
    X509_CHECK_FLAG_NO_WILDCARDS = 2
    X509_CHECK_FLAG_SINGLE_LABEL_SUBDOMAINS = 16
    @staticmethod
    def X509_CRL_add0_revoked():
        'int X509_CRL_add0_revoked(X509_CRL *, X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_add_ext():
        'int X509_CRL_add_ext(X509_CRL *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_cmp():
        'int X509_CRL_cmp(X509_CRL *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_dup():
        'X509_CRL *X509_CRL_dup(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_free():
        'void X509_CRL_free(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get0_by_serial():
        'int X509_CRL_get0_by_serial(X509_CRL *, X509_REVOKED * *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get0_signature():
        'void X509_CRL_get0_signature(X509_CRL *, struct asn1_string_st * *, X509_ALGOR * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_REVOKED():
        'Cryptography_STACK_OF_X509_REVOKED *X509_CRL_get_REVOKED(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_ext():
        'X509_EXTENSION *X509_CRL_get_ext(X509_CRL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_ext_count():
        'int X509_CRL_get_ext_count(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_issuer():
        'X509_NAME *X509_CRL_get_issuer(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_lastUpdate():
        'struct asn1_string_st *X509_CRL_get_lastUpdate(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_nextUpdate():
        'struct asn1_string_st *X509_CRL_get_nextUpdate(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_get_version():
        'long X509_CRL_get_version(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_new():
        'X509_CRL *X509_CRL_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_print():
        'int X509_CRL_print(BIO *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_set_issuer_name():
        'int X509_CRL_set_issuer_name(X509_CRL *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_set_lastUpdate():
        'int X509_CRL_set_lastUpdate(X509_CRL *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_set_nextUpdate():
        'int X509_CRL_set_nextUpdate(X509_CRL *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_set_version():
        'int X509_CRL_set_version(X509_CRL *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_sign():
        'int X509_CRL_sign(X509_CRL *, EVP_PKEY *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_sort():
        'int X509_CRL_sort(X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_CRL_verify():
        'int X509_CRL_verify(X509_CRL *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_create_by_OBJ():
        'X509_EXTENSION *X509_EXTENSION_create_by_OBJ(X509_EXTENSION * *, ASN1_OBJECT *, int, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_dup():
        'X509_EXTENSION *X509_EXTENSION_dup(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_free():
        'void X509_EXTENSION_free(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_get_critical():
        'int X509_EXTENSION_get_critical(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_get_data():
        'struct asn1_string_st *X509_EXTENSION_get_data(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_EXTENSION_get_object():
        'ASN1_OBJECT *X509_EXTENSION_get_object(X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    X509_LU_CRL = 2
    X509_LU_X509 = 1
    @staticmethod
    def X509_NAME_ENTRY_create_by_OBJ():
        'X509_NAME_ENTRY *X509_NAME_ENTRY_create_by_OBJ(X509_NAME_ENTRY * *, ASN1_OBJECT *, int, unsigned char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_ENTRY_free():
        'void X509_NAME_ENTRY_free(X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_ENTRY_get_data():
        'struct asn1_string_st *X509_NAME_ENTRY_get_data(X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_ENTRY_get_object():
        'ASN1_OBJECT *X509_NAME_ENTRY_get_object(X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_add_entry():
        'int X509_NAME_add_entry(X509_NAME *, X509_NAME_ENTRY *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_add_entry_by_NID():
        'int X509_NAME_add_entry_by_NID(X509_NAME *, int, int, unsigned char *, int, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_add_entry_by_OBJ():
        'int X509_NAME_add_entry_by_OBJ(X509_NAME *, ASN1_OBJECT *, int, unsigned char *, int, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_add_entry_by_txt():
        'int X509_NAME_add_entry_by_txt(X509_NAME *, char *, int, unsigned char *, int, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_cmp():
        'int X509_NAME_cmp(X509_NAME *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_delete_entry():
        'X509_NAME_ENTRY *X509_NAME_delete_entry(X509_NAME *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_dup():
        'X509_NAME *X509_NAME_dup(X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_entry_count():
        'int X509_NAME_entry_count(X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_free():
        'void X509_NAME_free(X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_get_entry():
        'X509_NAME_ENTRY *X509_NAME_get_entry(X509_NAME *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_get_index_by_NID():
        'int X509_NAME_get_index_by_NID(X509_NAME *, int, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_hash():
        'unsigned long X509_NAME_hash(X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_new():
        'X509_NAME *X509_NAME_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_oneline():
        'char *X509_NAME_oneline(X509_NAME *, char *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_NAME_print_ex():
        'int X509_NAME_print_ex(BIO *, X509_NAME *, int, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_OBJECT_get0_X509():
        'X509 *X509_OBJECT_get0_X509(X509_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_OBJECT_get_type():
        'int X509_OBJECT_get_type(X509_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_add_extensions():
        'int X509_REQ_add_extensions(X509_REQ *, X509_EXTENSIONS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_free():
        'void X509_REQ_free(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get0_signature():
        'void X509_REQ_get0_signature(X509_REQ *, struct asn1_string_st * *, X509_ALGOR * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get_extensions():
        'X509_EXTENSIONS *X509_REQ_get_extensions(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get_pubkey():
        'EVP_PKEY *X509_REQ_get_pubkey(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get_subject_name():
        'X509_NAME *X509_REQ_get_subject_name(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_get_version():
        'long X509_REQ_get_version(X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_new():
        'X509_REQ *X509_REQ_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_print_ex():
        'int X509_REQ_print_ex(BIO *, X509_REQ *, unsigned long, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_set_pubkey():
        'int X509_REQ_set_pubkey(X509_REQ *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_set_subject_name():
        'int X509_REQ_set_subject_name(X509_REQ *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_set_version():
        'int X509_REQ_set_version(X509_REQ *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_sign():
        'int X509_REQ_sign(X509_REQ *, EVP_PKEY *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REQ_verify():
        'int X509_REQ_verify(X509_REQ *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_add1_ext_i2d():
        'int X509_REVOKED_add1_ext_i2d(X509_REVOKED *, int, void *, int, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_add_ext():
        'int X509_REVOKED_add_ext(X509_REVOKED *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_delete_ext():
        'X509_EXTENSION *X509_REVOKED_delete_ext(X509_REVOKED *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_free():
        'void X509_REVOKED_free(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_get0_revocationDate():
        'struct asn1_string_st *X509_REVOKED_get0_revocationDate(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_get0_serialNumber():
        'ASN1_INTEGER *X509_REVOKED_get0_serialNumber(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_get_ext():
        'X509_EXTENSION *X509_REVOKED_get_ext(X509_REVOKED *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_get_ext_count():
        'int X509_REVOKED_get_ext_count(X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_new():
        'X509_REVOKED *X509_REVOKED_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_set_revocationDate():
        'int X509_REVOKED_set_revocationDate(X509_REVOKED *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_REVOKED_set_serialNumber():
        'int X509_REVOKED_set_serialNumber(X509_REVOKED *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    X509_R_CERT_ALREADY_IN_HASH_TABLE = 101
    X509_R_KEY_VALUES_MISMATCH = 116
    @staticmethod
    def X509_STORE_CTX_cleanup():
        'void X509_STORE_CTX_cleanup(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_free():
        'void X509_STORE_CTX_free(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get0_cert():
        'X509 *X509_STORE_CTX_get0_cert(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get0_param():
        'X509_VERIFY_PARAM *X509_STORE_CTX_get0_param(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get1_chain():
        'Cryptography_STACK_OF_X509 *X509_STORE_CTX_get1_chain(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get1_issuer():
        'int X509_STORE_CTX_get1_issuer(X509 * *, X509_STORE_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_chain():
        'Cryptography_STACK_OF_X509 *X509_STORE_CTX_get_chain(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_current_cert():
        'X509 *X509_STORE_CTX_get_current_cert(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_error():
        'int X509_STORE_CTX_get_error(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_error_depth():
        'int X509_STORE_CTX_get_error_depth(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_ex_data():
        'void *X509_STORE_CTX_get_ex_data(X509_STORE_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_get_ex_new_index():
        'int X509_STORE_CTX_get_ex_new_index(long, void *, CRYPTO_EX_new *, CRYPTO_EX_dup *, CRYPTO_EX_free *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_init():
        'int X509_STORE_CTX_init(X509_STORE_CTX *, X509_STORE *, X509 *, Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_new():
        'X509_STORE_CTX *X509_STORE_CTX_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set0_crls():
        'void X509_STORE_CTX_set0_crls(X509_STORE_CTX *, Cryptography_STACK_OF_X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set0_param():
        'void X509_STORE_CTX_set0_param(X509_STORE_CTX *, X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_cert():
        'void X509_STORE_CTX_set_cert(X509_STORE_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_chain():
        'void X509_STORE_CTX_set_chain(X509_STORE_CTX *, Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_default():
        'int X509_STORE_CTX_set_default(X509_STORE_CTX *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_error():
        'void X509_STORE_CTX_set_error(X509_STORE_CTX *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_ex_data():
        'int X509_STORE_CTX_set_ex_data(X509_STORE_CTX *, int, void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_set_verify_cb():
        'void X509_STORE_CTX_set_verify_cb(X509_STORE_CTX *, int(*)(int, X509_STORE_CTX *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_CTX_trusted_stack():
        'void X509_STORE_CTX_trusted_stack(X509_STORE_CTX *, Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_add_cert():
        'int X509_STORE_add_cert(X509_STORE *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_add_crl():
        'int X509_STORE_add_crl(X509_STORE *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_free():
        'void X509_STORE_free(X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_get0_objects():
        'Cryptography_STACK_OF_X509_OBJECT *X509_STORE_get0_objects(X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_get0_param():
        'X509_VERIFY_PARAM *X509_STORE_get0_param(X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_get_get_issuer():
        'int(*X509_STORE_get_get_issuer(X509_STORE *))(X509 * *, X509_STORE_CTX *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_load_locations():
        'int X509_STORE_load_locations(X509_STORE *, char *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_new():
        'X509_STORE *X509_STORE_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_set1_param():
        'int X509_STORE_set1_param(X509_STORE *, X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_set_default_paths():
        'int X509_STORE_set_default_paths(X509_STORE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_set_flags():
        'int X509_STORE_set_flags(X509_STORE *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_STORE_set_get_issuer():
        'void X509_STORE_set_get_issuer(X509_STORE *, int(*)(X509 * *, X509_STORE_CTX *, X509 *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_add0_policy():
        'int X509_VERIFY_PARAM_add0_policy(X509_VERIFY_PARAM *, ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_clear_flags():
        'int X509_VERIFY_PARAM_clear_flags(X509_VERIFY_PARAM *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_free():
        'void X509_VERIFY_PARAM_free(X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_get_depth():
        'int X509_VERIFY_PARAM_get_depth(X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_get_flags():
        'unsigned long X509_VERIFY_PARAM_get_flags(X509_VERIFY_PARAM *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_new():
        'X509_VERIFY_PARAM *X509_VERIFY_PARAM_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_email():
        'int X509_VERIFY_PARAM_set1_email(X509_VERIFY_PARAM *, char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_host():
        'int X509_VERIFY_PARAM_set1_host(X509_VERIFY_PARAM *, char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_ip():
        'int X509_VERIFY_PARAM_set1_ip(X509_VERIFY_PARAM *, unsigned char *, size_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_ip_asc():
        'int X509_VERIFY_PARAM_set1_ip_asc(X509_VERIFY_PARAM *, char *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set1_policies():
        'int X509_VERIFY_PARAM_set1_policies(X509_VERIFY_PARAM *, Cryptography_STACK_OF_ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_depth():
        'void X509_VERIFY_PARAM_set_depth(X509_VERIFY_PARAM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_flags():
        'int X509_VERIFY_PARAM_set_flags(X509_VERIFY_PARAM *, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_hostflags():
        'void X509_VERIFY_PARAM_set_hostflags(X509_VERIFY_PARAM *, unsigned int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_purpose():
        'int X509_VERIFY_PARAM_set_purpose(X509_VERIFY_PARAM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_time():
        'void X509_VERIFY_PARAM_set_time(X509_VERIFY_PARAM *, int64_t);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_VERIFY_PARAM_set_trust():
        'int X509_VERIFY_PARAM_set_trust(X509_VERIFY_PARAM *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    X509_V_ERR_AKID_ISSUER_SERIAL_MISMATCH = 31
    X509_V_ERR_AKID_SKID_MISMATCH = 30
    X509_V_ERR_APPLICATION_VERIFICATION = 50
    X509_V_ERR_CERT_CHAIN_TOO_LONG = 22
    X509_V_ERR_CERT_HAS_EXPIRED = 10
    X509_V_ERR_CERT_NOT_YET_VALID = 9
    X509_V_ERR_CERT_REJECTED = 28
    X509_V_ERR_CERT_REVOKED = 23
    X509_V_ERR_CERT_SIGNATURE_FAILURE = 7
    X509_V_ERR_CERT_UNTRUSTED = 27
    X509_V_ERR_CRL_HAS_EXPIRED = 12
    X509_V_ERR_CRL_NOT_YET_VALID = 11
    X509_V_ERR_CRL_PATH_VALIDATION_ERROR = 54
    X509_V_ERR_CRL_SIGNATURE_FAILURE = 8
    X509_V_ERR_DEPTH_ZERO_SELF_SIGNED_CERT = 18
    X509_V_ERR_DIFFERENT_CRL_SCOPE = 44
    X509_V_ERR_EMAIL_MISMATCH = 63
    X509_V_ERR_ERROR_IN_CERT_NOT_AFTER_FIELD = 14
    X509_V_ERR_ERROR_IN_CERT_NOT_BEFORE_FIELD = 13
    X509_V_ERR_ERROR_IN_CRL_LAST_UPDATE_FIELD = 15
    X509_V_ERR_ERROR_IN_CRL_NEXT_UPDATE_FIELD = 16
    X509_V_ERR_EXCLUDED_VIOLATION = 48
    X509_V_ERR_HOSTNAME_MISMATCH = 62
    X509_V_ERR_INVALID_CA = 24
    X509_V_ERR_INVALID_EXTENSION = 41
    X509_V_ERR_INVALID_NON_CA = 37
    X509_V_ERR_INVALID_POLICY_EXTENSION = 42
    X509_V_ERR_INVALID_PURPOSE = 26
    X509_V_ERR_IP_ADDRESS_MISMATCH = 64
    X509_V_ERR_KEYUSAGE_NO_CERTSIGN = 32
    X509_V_ERR_KEYUSAGE_NO_CRL_SIGN = 35
    X509_V_ERR_KEYUSAGE_NO_DIGITAL_SIGNATURE = 39
    X509_V_ERR_NO_EXPLICIT_POLICY = 43
    X509_V_ERR_OUT_OF_MEM = 17
    X509_V_ERR_PATH_LENGTH_EXCEEDED = 25
    X509_V_ERR_PERMITTED_VIOLATION = 47
    X509_V_ERR_PROXY_CERTIFICATES_NOT_ALLOWED = 40
    X509_V_ERR_PROXY_PATH_LENGTH_EXCEEDED = 38
    X509_V_ERR_SELF_SIGNED_CERT_IN_CHAIN = 19
    X509_V_ERR_SUBJECT_ISSUER_MISMATCH = 29
    X509_V_ERR_SUBTREE_MINMAX = 49
    X509_V_ERR_SUITE_B_CANNOT_SIGN_P_384_WITH_P_256 = 61
    X509_V_ERR_SUITE_B_INVALID_ALGORITHM = 57
    X509_V_ERR_SUITE_B_INVALID_CURVE = 58
    X509_V_ERR_SUITE_B_INVALID_SIGNATURE_ALGORITHM = 59
    X509_V_ERR_SUITE_B_INVALID_VERSION = 56
    X509_V_ERR_SUITE_B_LOS_NOT_ALLOWED = 60
    X509_V_ERR_UNABLE_TO_DECODE_ISSUER_PUBLIC_KEY = 6
    X509_V_ERR_UNABLE_TO_DECRYPT_CERT_SIGNATURE = 4
    X509_V_ERR_UNABLE_TO_DECRYPT_CRL_SIGNATURE = 5
    X509_V_ERR_UNABLE_TO_GET_CRL = 3
    X509_V_ERR_UNABLE_TO_GET_CRL_ISSUER = 33
    X509_V_ERR_UNABLE_TO_GET_ISSUER_CERT = 2
    X509_V_ERR_UNABLE_TO_GET_ISSUER_CERT_LOCALLY = 20
    X509_V_ERR_UNABLE_TO_VERIFY_LEAF_SIGNATURE = 21
    X509_V_ERR_UNHANDLED_CRITICAL_CRL_EXTENSION = 36
    X509_V_ERR_UNHANDLED_CRITICAL_EXTENSION = 34
    X509_V_ERR_UNNESTED_RESOURCE = 46
    X509_V_ERR_UNSUPPORTED_CONSTRAINT_SYNTAX = 52
    X509_V_ERR_UNSUPPORTED_CONSTRAINT_TYPE = 51
    X509_V_ERR_UNSUPPORTED_EXTENSION_FEATURE = 45
    X509_V_ERR_UNSUPPORTED_NAME_SYNTAX = 53
    X509_V_FLAG_ALLOW_PROXY_CERTS = 64
    X509_V_FLAG_CB_ISSUER_CHECK = 0
    X509_V_FLAG_CHECK_SS_SIGNATURE = 16384
    X509_V_FLAG_CRL_CHECK = 4
    X509_V_FLAG_CRL_CHECK_ALL = 8
    X509_V_FLAG_EXPLICIT_POLICY = 256
    X509_V_FLAG_EXTENDED_CRL_SUPPORT = 4096
    X509_V_FLAG_IGNORE_CRITICAL = 16
    X509_V_FLAG_INHIBIT_ANY = 512
    X509_V_FLAG_INHIBIT_MAP = 1024
    X509_V_FLAG_NOTIFY_POLICY = 2048
    X509_V_FLAG_PARTIAL_CHAIN = 524288
    X509_V_FLAG_POLICY_CHECK = 128
    X509_V_FLAG_SUITEB_128_LOS = 196608
    X509_V_FLAG_SUITEB_128_LOS_ONLY = 65536
    X509_V_FLAG_SUITEB_192_LOS = 131072
    X509_V_FLAG_TRUSTED_FIRST = 32768
    X509_V_FLAG_USE_CHECK_TIME = 2
    X509_V_FLAG_USE_DELTAS = 8192
    X509_V_FLAG_X509_STRICT = 32
    X509_V_OK = 0
    @staticmethod
    def X509_add_ext():
        'int X509_add_ext(X509 *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_alias_get0():
        'unsigned char *X509_alias_get0(X509 *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_check_ca():
        'int X509_check_ca(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_cmp():
        'int X509_cmp(X509 *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_digest():
        'int X509_digest(X509 *, EVP_MD *, unsigned char *, unsigned int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_dup():
        'X509 *X509_dup(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_free():
        'void X509_free(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get0_signature():
        'void X509_get0_signature(struct asn1_string_st * *, X509_ALGOR * *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get0_tbs_sigalg():
        'X509_ALGOR *X509_get0_tbs_sigalg(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_cert_dir():
        'char *X509_get_default_cert_dir();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_cert_dir_env():
        'char *X509_get_default_cert_dir_env();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_cert_file():
        'char *X509_get_default_cert_file();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_default_cert_file_env():
        'char *X509_get_default_cert_file_env();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_ext():
        'X509_EXTENSION *X509_get_ext(X509 *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_ext_count():
        'int X509_get_ext_count(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_ext_d2i():
        'void *X509_get_ext_d2i(X509 *, int, int *, int *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_issuer_name():
        'X509_NAME *X509_get_issuer_name(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_notAfter():
        'struct asn1_string_st *X509_get_notAfter(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_notBefore():
        'struct asn1_string_st *X509_get_notBefore(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_pubkey():
        'EVP_PKEY *X509_get_pubkey(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_serialNumber():
        'ASN1_INTEGER *X509_get_serialNumber(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_signature_nid():
        'int X509_get_signature_nid(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_subject_name():
        'X509_NAME *X509_get_subject_name(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_get_version():
        'long X509_get_version(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_gmtime_adj():
        'struct asn1_string_st *X509_gmtime_adj(struct asn1_string_st *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_new():
        'X509 *X509_new();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_print_ex():
        'int X509_print_ex(BIO *, X509 *, unsigned long, unsigned long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_issuer_name():
        'int X509_set_issuer_name(X509 *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_notAfter():
        'int X509_set_notAfter(X509 *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_notBefore():
        'int X509_set_notBefore(X509 *, struct asn1_string_st *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_pubkey():
        'int X509_set_pubkey(X509 *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_serialNumber():
        'int X509_set_serialNumber(X509 *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_subject_name():
        'int X509_set_subject_name(X509 *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_set_version():
        'int X509_set_version(X509 *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_sign():
        'int X509_sign(X509 *, EVP_PKEY *, EVP_MD *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_subject_name_hash():
        'unsigned long X509_subject_name_hash(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_up_ref():
        'int X509_up_ref(X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_verify_cert():
        'int X509_verify_cert(X509_STORE_CTX *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def X509_verify_cert_error_string():
        'char *X509_verify_cert_error_string(long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_ASN1_TYPE():
        'ASN1_TYPE *d2i_ASN1_TYPE(ASN1_TYPE * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_DHparams_bio():
        'DH *d2i_DHparams_bio(BIO *, DH * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_ECDSA_SIG():
        'ECDSA_SIG *d2i_ECDSA_SIG(ECDSA_SIG * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_ECPrivateKey_bio():
        'EC_KEY *d2i_ECPrivateKey_bio(BIO *, EC_KEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_EC_PUBKEY_bio():
        'EC_KEY *d2i_EC_PUBKEY_bio(BIO *, EC_KEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_GENERAL_NAMES():
        'struct stack_st_GENERAL_NAME *d2i_GENERAL_NAMES(struct stack_st_GENERAL_NAME * *, unsigned char * *, long);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_OCSP_REQUEST_bio():
        'OCSP_REQUEST *d2i_OCSP_REQUEST_bio(BIO *, OCSP_REQUEST * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_OCSP_RESPONSE_bio():
        'OCSP_RESPONSE *d2i_OCSP_RESPONSE_bio(BIO *, OCSP_RESPONSE * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PKCS12_bio():
        'PKCS12 *d2i_PKCS12_bio(BIO *, PKCS12 * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PKCS7_bio():
        'PKCS7 *d2i_PKCS7_bio(BIO *, PKCS7 * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PKCS8PrivateKey_bio():
        'EVP_PKEY *d2i_PKCS8PrivateKey_bio(BIO *, EVP_PKEY * *, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PUBKEY_bio():
        'EVP_PKEY *d2i_PUBKEY_bio(BIO *, EVP_PKEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_PrivateKey_bio():
        'EVP_PKEY *d2i_PrivateKey_bio(BIO *, EVP_PKEY * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_RSAPublicKey_bio():
        'RSA *d2i_RSAPublicKey_bio(BIO *, RSA * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_X509_CRL_bio():
        'X509_CRL *d2i_X509_CRL_bio(BIO *, X509_CRL * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_X509_REQ_bio():
        'X509_REQ *d2i_X509_REQ_bio(BIO *, X509_REQ * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def d2i_X509_bio():
        'X509 *d2i_X509_bio(BIO *, X509 * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2a_ASN1_INTEGER():
        'int i2a_ASN1_INTEGER(BIO *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ASN1_TYPE():
        'int i2d_ASN1_TYPE(ASN1_TYPE *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_DHparams_bio():
        'int i2d_DHparams_bio(BIO *, DH *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_DSAPrivateKey_bio():
        'int i2d_DSAPrivateKey_bio(BIO *, DSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ECDSA_SIG():
        'int i2d_ECDSA_SIG(ECDSA_SIG *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_ECPrivateKey_bio():
        'int i2d_ECPrivateKey_bio(BIO *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_EC_PUBKEY_bio():
        'int i2d_EC_PUBKEY_bio(BIO *, EC_KEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_GENERAL_NAMES():
        'int i2d_GENERAL_NAMES(struct stack_st_GENERAL_NAME *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_OCSP_REQUEST_bio():
        'int i2d_OCSP_REQUEST_bio(BIO *, OCSP_REQUEST *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_OCSP_RESPDATA():
        'int i2d_OCSP_RESPDATA(OCSP_RESPDATA *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_OCSP_RESPONSE_bio():
        'int i2d_OCSP_RESPONSE_bio(BIO *, OCSP_RESPONSE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PKCS12_bio():
        'int i2d_PKCS12_bio(BIO *, PKCS12 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PKCS7_bio():
        'int i2d_PKCS7_bio(BIO *, PKCS7 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PKCS8PrivateKey_bio():
        'int i2d_PKCS8PrivateKey_bio(BIO *, EVP_PKEY *, EVP_CIPHER *, char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PKCS8PrivateKey_nid_bio():
        'int i2d_PKCS8PrivateKey_nid_bio(BIO *, EVP_PKEY *, int, char *, int, int(*)(char *, int, int, void *), void *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PUBKEY_bio():
        'int i2d_PUBKEY_bio(BIO *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_PrivateKey_bio():
        'int i2d_PrivateKey_bio(BIO *, EVP_PKEY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_RSAPrivateKey_bio():
        'int i2d_RSAPrivateKey_bio(BIO *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_RSAPublicKey_bio():
        'int i2d_RSAPublicKey_bio(BIO *, RSA *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_CRL_bio():
        'int i2d_X509_CRL_bio(BIO *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_NAME():
        'int i2d_X509_NAME(X509_NAME *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_REQ_bio():
        'int i2d_X509_REQ_bio(BIO *, X509_REQ *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_X509_bio():
        'int i2d_X509_bio(BIO *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_re_X509_CRL_tbs():
        'int i2d_re_X509_CRL_tbs(X509_CRL *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_re_X509_REQ_tbs():
        'int i2d_re_X509_REQ_tbs(X509_REQ *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def i2d_re_X509_tbs():
        'int i2d_re_X509_tbs(X509 *, unsigned char * *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_free():
        'void sk_ACCESS_DESCRIPTION_free(Cryptography_STACK_OF_ACCESS_DESCRIPTION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_new_null():
        'Cryptography_STACK_OF_ACCESS_DESCRIPTION *sk_ACCESS_DESCRIPTION_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_num():
        'int sk_ACCESS_DESCRIPTION_num(Cryptography_STACK_OF_ACCESS_DESCRIPTION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_push():
        'int sk_ACCESS_DESCRIPTION_push(Cryptography_STACK_OF_ACCESS_DESCRIPTION *, ACCESS_DESCRIPTION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ACCESS_DESCRIPTION_value():
        'ACCESS_DESCRIPTION *sk_ACCESS_DESCRIPTION_value(Cryptography_STACK_OF_ACCESS_DESCRIPTION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_free():
        'void sk_ASN1_INTEGER_free(Cryptography_STACK_OF_ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_new_null():
        'Cryptography_STACK_OF_ASN1_INTEGER *sk_ASN1_INTEGER_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_num():
        'int sk_ASN1_INTEGER_num(Cryptography_STACK_OF_ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_push():
        'int sk_ASN1_INTEGER_push(Cryptography_STACK_OF_ASN1_INTEGER *, ASN1_INTEGER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_INTEGER_value():
        'ASN1_INTEGER *sk_ASN1_INTEGER_value(Cryptography_STACK_OF_ASN1_INTEGER *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_free():
        'void sk_ASN1_OBJECT_free(Cryptography_STACK_OF_ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_new_null():
        'Cryptography_STACK_OF_ASN1_OBJECT *sk_ASN1_OBJECT_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_num():
        'int sk_ASN1_OBJECT_num(Cryptography_STACK_OF_ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_push():
        'int sk_ASN1_OBJECT_push(Cryptography_STACK_OF_ASN1_OBJECT *, ASN1_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_ASN1_OBJECT_value():
        'ASN1_OBJECT *sk_ASN1_OBJECT_value(Cryptography_STACK_OF_ASN1_OBJECT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_free():
        'void sk_DIST_POINT_free(Cryptography_STACK_OF_DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_new_null():
        'Cryptography_STACK_OF_DIST_POINT *sk_DIST_POINT_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_num():
        'int sk_DIST_POINT_num(Cryptography_STACK_OF_DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_pop_free():
        'void sk_DIST_POINT_pop_free(Cryptography_STACK_OF_DIST_POINT *, void(*)(DIST_POINT *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_push():
        'int sk_DIST_POINT_push(Cryptography_STACK_OF_DIST_POINT *, DIST_POINT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_DIST_POINT_value():
        'DIST_POINT *sk_DIST_POINT_value(Cryptography_STACK_OF_DIST_POINT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_NAME_num():
        'int sk_GENERAL_NAME_num(struct stack_st_GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_NAME_pop_free():
        'void sk_GENERAL_NAME_pop_free(struct stack_st_GENERAL_NAME *, void(*)(GENERAL_NAME *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_NAME_push():
        'int sk_GENERAL_NAME_push(struct stack_st_GENERAL_NAME *, GENERAL_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_NAME_value():
        'GENERAL_NAME *sk_GENERAL_NAME_value(struct stack_st_GENERAL_NAME *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_free():
        'void sk_GENERAL_SUBTREE_free(Cryptography_STACK_OF_GENERAL_SUBTREE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_new_null():
        'Cryptography_STACK_OF_GENERAL_SUBTREE *sk_GENERAL_SUBTREE_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_num():
        'int sk_GENERAL_SUBTREE_num(Cryptography_STACK_OF_GENERAL_SUBTREE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_push():
        'int sk_GENERAL_SUBTREE_push(Cryptography_STACK_OF_GENERAL_SUBTREE *, GENERAL_SUBTREE *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_GENERAL_SUBTREE_value():
        'GENERAL_SUBTREE *sk_GENERAL_SUBTREE_value(Cryptography_STACK_OF_GENERAL_SUBTREE *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_free():
        'void sk_POLICYINFO_free(Cryptography_STACK_OF_POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_new_null():
        'Cryptography_STACK_OF_POLICYINFO *sk_POLICYINFO_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_num():
        'int sk_POLICYINFO_num(Cryptography_STACK_OF_POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_pop_free():
        'void sk_POLICYINFO_pop_free(Cryptography_STACK_OF_POLICYINFO *, void(*)(POLICYINFO *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_push():
        'int sk_POLICYINFO_push(Cryptography_STACK_OF_POLICYINFO *, POLICYINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYINFO_value():
        'POLICYINFO *sk_POLICYINFO_value(Cryptography_STACK_OF_POLICYINFO *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_free():
        'void sk_POLICYQUALINFO_free(Cryptography_STACK_OF_POLICYQUALINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_new_null():
        'Cryptography_STACK_OF_POLICYQUALINFO *sk_POLICYQUALINFO_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_num():
        'int sk_POLICYQUALINFO_num(Cryptography_STACK_OF_POLICYQUALINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_push():
        'int sk_POLICYQUALINFO_push(Cryptography_STACK_OF_POLICYQUALINFO *, POLICYQUALINFO *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_POLICYQUALINFO_value():
        'POLICYQUALINFO *sk_POLICYQUALINFO_value(Cryptography_STACK_OF_POLICYQUALINFO *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SCT_new_null():
        'Cryptography_STACK_OF_SCT *sk_SCT_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SCT_num():
        'int sk_SCT_num(Cryptography_STACK_OF_SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SCT_push():
        'int sk_SCT_push(Cryptography_STACK_OF_SCT *, SCT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SCT_value():
        'SCT *sk_SCT_value(Cryptography_STACK_OF_SCT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SSL_CIPHER_num():
        'int sk_SSL_CIPHER_num(Cryptography_STACK_OF_SSL_CIPHER *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_SSL_CIPHER_value():
        'SSL_CIPHER *sk_SSL_CIPHER_value(Cryptography_STACK_OF_SSL_CIPHER *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_free():
        'void sk_X509_CRL_free(Cryptography_STACK_OF_X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_new_null():
        'Cryptography_STACK_OF_X509_CRL *sk_X509_CRL_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_num():
        'int sk_X509_CRL_num(Cryptography_STACK_OF_X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_push():
        'int sk_X509_CRL_push(Cryptography_STACK_OF_X509_CRL *, X509_CRL *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_CRL_value():
        'X509_CRL *sk_X509_CRL_value(Cryptography_STACK_OF_X509_CRL *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_delete():
        'X509_EXTENSION *sk_X509_EXTENSION_delete(X509_EXTENSIONS *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_free():
        'void sk_X509_EXTENSION_free(X509_EXTENSIONS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_insert():
        'int sk_X509_EXTENSION_insert(X509_EXTENSIONS *, X509_EXTENSION *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_new_null():
        'X509_EXTENSIONS *sk_X509_EXTENSION_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_num():
        'int sk_X509_EXTENSION_num(X509_EXTENSIONS *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_pop_free():
        'void sk_X509_EXTENSION_pop_free(X509_EXTENSIONS *, void(*)(X509_EXTENSION *));\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_push():
        'int sk_X509_EXTENSION_push(X509_EXTENSIONS *, X509_EXTENSION *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_EXTENSION_value():
        'X509_EXTENSION *sk_X509_EXTENSION_value(X509_EXTENSIONS *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_dup():
        'Cryptography_STACK_OF_X509_NAME_ENTRY *sk_X509_NAME_ENTRY_dup(Cryptography_STACK_OF_X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_new_null():
        'Cryptography_STACK_OF_X509_NAME_ENTRY *sk_X509_NAME_ENTRY_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_num():
        'int sk_X509_NAME_ENTRY_num(Cryptography_STACK_OF_X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_push():
        'int sk_X509_NAME_ENTRY_push(Cryptography_STACK_OF_X509_NAME_ENTRY *, X509_NAME_ENTRY *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_ENTRY_value():
        'X509_NAME_ENTRY *sk_X509_NAME_ENTRY_value(Cryptography_STACK_OF_X509_NAME_ENTRY *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_free():
        'void sk_X509_NAME_free(Cryptography_STACK_OF_X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_new_null():
        'Cryptography_STACK_OF_X509_NAME *sk_X509_NAME_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_num():
        'int sk_X509_NAME_num(Cryptography_STACK_OF_X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_push():
        'int sk_X509_NAME_push(Cryptography_STACK_OF_X509_NAME *, X509_NAME *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_NAME_value():
        'X509_NAME *sk_X509_NAME_value(Cryptography_STACK_OF_X509_NAME *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_OBJECT_num():
        'int sk_X509_OBJECT_num(Cryptography_STACK_OF_X509_OBJECT *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_OBJECT_value():
        'X509_OBJECT *sk_X509_OBJECT_value(Cryptography_STACK_OF_X509_OBJECT *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_REVOKED_num():
        'int sk_X509_REVOKED_num(Cryptography_STACK_OF_X509_REVOKED *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_REVOKED_value():
        'X509_REVOKED *sk_X509_REVOKED_value(Cryptography_STACK_OF_X509_REVOKED *, int);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_free():
        'void sk_X509_free(Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_new_null():
        'Cryptography_STACK_OF_X509 *sk_X509_new_null();\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_num():
        'int sk_X509_num(Cryptography_STACK_OF_X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_push():
        'int sk_X509_push(Cryptography_STACK_OF_X509 *, X509 *);\n\nCFFI C function from _openssl.lib'
        pass
    
    @staticmethod
    def sk_X509_value():
        'X509 *sk_X509_value(Cryptography_STACK_OF_X509 *, int);\n\nCFFI C function from _openssl.lib'
        pass
    

