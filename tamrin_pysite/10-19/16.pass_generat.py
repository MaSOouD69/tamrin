import random
#old me
count=int(input("ENTER lenth of pass: "))
s='qwertyuiopasdfghjklzxcvbnm01234567890QWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()_+'
a=random.sample(s,count)
passw=""
for item in a:
    passw += item
print(passw)

#new me # new version
s="QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*()_+=-"
while 1:
    print("\033c", end='')
    print("".join(random.sample(s,int(input("tell your password lengh: ")))))
    input("Enter to regenerate")

# site selution
import string
import random

def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
	return ''.join(random.choice(chars) for _ in range(size))

print(pw_gen(int(input('How many characters in your password?'))))