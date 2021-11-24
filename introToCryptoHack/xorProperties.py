from Crypto.Util.number import bytes_to_long, long_to_bytes

key1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

def xorCompare(encryptKey1, encryptKey2):
    return long_to_bytes(bytes_to_long(bytes.fromhex(encryptKey1)) ^ bytes_to_long(bytes.fromhex(encryptKey2))).hex()

KEY2 = xorCompare(key1, key2)
print(KEY2)

KEY3 = xorCompare(KEY2, key3)
print(KEY3)

KEY4 = xorCompare(xorCompare(KEY3, KEY2), key1)
print(KEY4)

FLAG = bytes.fromhex(xorCompare(KEY4, flag))
print(FLAG)
