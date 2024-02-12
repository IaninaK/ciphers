# -= CAESAR CIPHER - ENCRYPTION =-
#input: shift and message that you want to encrypt
#output: encrypted message

# parts of the plaintext that aren't letters aren't changed in the cipher text 

alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
plaintext = "i'm the laughing gnome"
ciphertext = ""
shift = 2
for p in plaintext:
    if p.isalpha() == True:
        alpha_index = alphabet.index(p)
        shifted_index = alpha_index + shift
        # print(alpha_index, p, shifted_index)   #troubleshooting prints
        # print(alphabet[shifted_index])
        ciphertext = ciphertext + alphabet[shifted_index]
    else:
        ciphertext = ciphertext + p
print(ciphertext)

dec = "" #deciphered plaintext
for c in ciphertext:
    if c.isalpha() == True:
        al_index = alphabet.index(c)
        rev_index = al_index - shift #reversed index - inverse of shifted index
        dec = dec + alphabet[rev_index]
    else:
        dec = dec + c
print(dec)
