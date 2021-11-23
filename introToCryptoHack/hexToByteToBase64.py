import base64

hexV = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

byte = bytes.fromhex(hexV)

base64bytes = base64.b64encode(byte)

print(base64bytes)
