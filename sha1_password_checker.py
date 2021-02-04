import requests
import hashlib
import sys


def read_pw_file(filename):
    password_dict = dict()
    with open(filename, 'r') as my_file:
        line_hold = ''
        key = None
        for line in my_file:
            temp = line.split(': ', 1)
            if line_hold == '':
                key = line.strip()
            elif temp[0] == 'password':
                password = temp[1].strip()
                password_dict[key] = password
            line_hold = line.strip()
    return password_dict


def convert_to_hash(password):
    hash_object = hashlib.sha1(password.encode())
    hash_code = hash_object.hexdigest()
    return hash_code


def split_hash(full_hash):
    hash_parts = {
        'first 5 chars': full_hash[:5],
        'remaining chars': full_hash[5:]
    }
    return hash_parts


def contact_api(first_5_hash_chars):
    pwned_url = f'https://api.pwnedpasswords.com/range/{first_5_hash_chars}'
    r = requests.get(pwned_url)
    if r.status_code == 200:
        hashes_received = r.text
        return hashes_received
    else:
        raise Exception('error connecting to API')


def check_if_pwned(use_name, remaining_hash, hashes_received):
    hashes_to_list = hashes_received.split()
    hash_data = []
    for hash_item in hashes_to_list:
        hash_and_count = hash_item.split(':')
        hash_data.append(hash_and_count)
    for hash_item in hash_data:
        if remaining_hash.upper() == hash_item[0]:
            return print(f"Password for '{use_name}' was found in {hash_item[1]} data breeches. Change it!!")
    return print(f"Password for '{use_name}' is safe. Carry on.")


if __name__ == '__main__':
    file = sys.argv[1]
    password_dict = read_pw_file(file)
    for key, password in password_dict.items():
        new_hash = convert_to_hash(password)
        new_hash_split = split_hash(new_hash)
        hashes_received = contact_api(new_hash_split['first 5 chars'])
        check_if_pwned(key, new_hash_split['remaining chars'], hashes_received)