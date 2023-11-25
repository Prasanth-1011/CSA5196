import hashlib

def generate_md5_hash(data):
    md5_hash = hashlib.md5(data.encode()).hexdigest()
    return md5_hash

data_to_hash = "Hello, World!"
resulting_md5_hash = generate_md5_hash(data_to_hash)
print(f"MD5 hash of '{data_to_hash}': {resulting_md5_hash}")
