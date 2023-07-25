import string
from client import  request

chars = string.printable
chars = list(chars)
print(chars)
username = 'test1'

'''
a= '0'
b = 'a'
c = '1'
d = '.'
response = request(username, str(a+b+c+d))
print(response)

 passwd = str(a+b+c+d)
                print(passwd)
                response = request(username, passwd)
                print(response)
                if response != "False":
                    print(passwd)
                    break
'''

breaker = False
for a in chars:
    if breaker is True:
        break
    for b in chars:
        if breaker is True:
            break
        for c in chars:
            if breaker is True:
                break
            for d in chars:
                passwd = str(a + b + c + d)
                print(passwd)
                response = request(username, passwd)
                if response != 'False':
                    print(f"password found {passwd}")
                    breaker = True
                    break
