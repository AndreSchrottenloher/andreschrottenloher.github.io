import hashlib
from random import randrange, getrandbits
sha2 = hashlib.sha256


print(sha2(b"Hello world").hexdigest())
print(sha2("Hello world".encode()).hexdigest())

def sha2Trunc(x, N=32):
    fullHash = sha2(str(x).encode()).hexdigest()
    return int(fullHash[:N//4],16)

print( sha2Trunc(10) )





