'''
Algorithm:

rotation_value_letter = (ord(char) + rotation_factor) % 26
rotation_value_number = (num_char + rotation_factor) % 9

0. Edge cases: empty string?
1. Create a new string to populate it after iterating through the old str
2. Cipher
3. Return

'''

def rotationalCipher(input, rotation_factor):
  if not input or not rotation_factor:
    return input
  ciphered_string = ""
  for char in input:
    if not char.isalnum():
      ciphered_string += char
    elif char.isalpha():
      rotation_value = (ord(char) + rotation_factor)
      if rotation_value > 25:
        rotation_value %= 26
        ciphered_string += chr(rotation_value)
      elif char.isdigit():
        rotation_value = (ord(char) + rotation_factor)
        if rotation_value > 9:
          rotation_value %= 9
    
    if ord(char) >= 48 and ord(char) <= 57:
      rotation_value = (ord(char) + rotation_factor) % 9
    elif (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <= 122):
      rotation_value = (ord(char) + rotation_factor) % 26
    else:
      rotation_value = ord(char)
    ciphered_string += chr(rotation_value)
  return ciphered_string
