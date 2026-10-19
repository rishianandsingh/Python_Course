num = 12
secret = 89
encrypted_num = num ^ secret
print("sending", encrypted_num, "over internet")
print("reciever got it")
decrypted_num = encrypted_num ^ secret
print("reciever got", decrypted_num)
