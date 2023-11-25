import hashlib

def generate_sha1_hash(data):
    sha1_hash = hashlib.sha1(data.encode()).hexdigest()
    return sha1_hash

data_to_hash = "Hello, World!"
resulting_sha1_hash = generate_sha1_hash(data_to_hash)
print(f"SHA-1 hash of '{data_to_hash}': {resulting_sha1_hash}")
