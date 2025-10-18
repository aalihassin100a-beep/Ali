import hashlib
import requests

def check_password_leak(password: str) -> bool:

    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f"فشل الاتصال بـ API: {response.status_code}")

    hashes = (line.split(':') for line in response.text.splitlines())
    for hash_suffix, count in hashes:
        if hash_suffix == suffix:
            print(f" تم تسريب كلمة المرور {count} مرة.")
            return True

    print(" كلمة المرور آمنة ولم يتم تسريبها.")
    return False
