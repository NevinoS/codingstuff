# unicode string
string = 'pythön!'

# print string
print('The string is:', string)

# default encoding to utf-8
string_utf = string.encode()

# print result
print('The encoded version is:', string_utf)

# try catching a UnicodeDecodeError

# Use bytes. decode() to decode a UTF-8-encoded byte string

# Call bytes. decode(encoding) with encoding as "utf8" to decode a UTF-8-encoded byte string bytes .
