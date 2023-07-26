import ip as p

ip1 = "192.168.1.1"
ip2 = "256.168.1.1"
ip3 = "10.10.10.256"
ip4 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
ips = [ip1, ip2, ip3, ip4]

for ip in ips:
    print(f'this is the IP:{ip}')
    print(f'And its:{p.is_valid_ipv4(ip)}')
