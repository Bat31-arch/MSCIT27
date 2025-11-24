key = [[3, 3], [2, 5]]
plain = "HI"
p1 = ord(plain[0]) - 65
p2 = ord(plain[1]) - 65
c1 = (key[0][0]*p1 + key[0][1]*p2) % 26
c2 = (key[1][0]*p1 + key[1][1]*p2) % 26
cipher = chr(c1 + 65) + chr(c2 + 65)
print("Plaintext:", plain)
print("Cipher:", cipher)