import hashlib
choice = input("[*] 1) sha256 2) sha512 3) md5  ")
passwords = open("rockyou.txt")
rbt = open("rainbowtable.txt", "w")
def rainbow():
    for line in passwords.readlines():
        pwd = line.strip('\n')
        if choice == "1":
            hash = hashlib.sha256(str.encode(pwd))
        elif choice == "2":
            hash = hashlib.sha512(str.encode(pwd))
        elif choice == "3":
            hash = hashlib.md5(str.encode(pwd))
        output.write(hash.hexdigest() + "#" + pwd + "\n")
    rbt.close()
    passwords.close()
