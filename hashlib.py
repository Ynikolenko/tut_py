# Hash a single string with hashlib.sha256
import hashlib

a_string = 'this string holds important and private information'

hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
print(hashed_string)

# Returns:
# 4e7d696bce894548dded72f6eeb04e8d625cc7f2afd08845824a4a8378b428d1