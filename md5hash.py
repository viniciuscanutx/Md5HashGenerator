import hashlib

textonormal = input("Qual o texto que deseja converter?")

def md5hasher(data):
    md5hash = hashlib.md5()
    md5hash.update(data.encode("utf8"))
    print(md5hash.hexdigest())
