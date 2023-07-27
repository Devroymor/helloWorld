import re


# Created the function is_valid_ipv4(argument: ip_address of type string)

def is_valid_ipv4(ip_address):
    if not (isinstance(ip_address, str)):
        return False

    # Pattrn ipv4
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

    # Check For Matches
    match = re.match(pattern, ip_address)

    if match:
        # IPV4
        groups = match.groups()
        for group in groups:
            if not (0 <= int(group) <= 255):
                return False
        return True
    else:
        return False



