import re


def is_valid_ipv4(ip_address):
    if not (isinstance(ip_address,str)):
        return False

    # התבנית לבדיקת תקינות כתובת IP
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'

    # בדיקת התאמה של הכתובת לתבנית
    match = re.match(pattern, ip_address)

    if match:
        # המספרים נמצאים בטווח התקין לIPv4
        groups = match.groups()
        for group in groups:
            if not (0 <= int(group) <= 255):
                return False
        return True
    else:
        return False


# דוגמאות לבדיקה

