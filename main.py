import ip as p
import is_gmail as g

# seprated fucntion which was defined in ip.py
ip1 = "192.168.1.1"
ip2 = "256.168.1.1"
ip3 = "10.10.10.256"
ip4 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
ips = [ip1, ip2, ip3, ip4]
# insted of using static code I used for loop to run all tests
for ip in ips:
    # insted four lines printing in diffrerent lines, used f' & {}
    print(f'this is the IP:{ip}')
    print(f'And its:{p.is_valid_ipv4(ip)}')


##test is_gmail.py
# test is_gmail.py
mail1 = "example@gmail.com"
mail2 = "bad_mail@.com"
mail3 = "anotherexample@domain.com"
mail4 = "wrong_mail@@gmail.com"
mails = {mail1, mail2, mail3, mail4}

for mail in mails:
    print(f'This is the mail: {mail}')
    print(f'Is this a valid mail: {g.is_valid_mail(mail)}\n')