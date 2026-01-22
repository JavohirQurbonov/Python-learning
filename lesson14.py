# PAYNET
PASSPORT = {
    "ad1234567": {"last_name": "Ermamatov", "first_name": "Nurulloh", "birthdate": "2005.09.26"},
    "ad7654321": {"last_name": "Isayev", "first_name": "Firdavs", "birthdate": "2005.06.05"},
    "ad2001129": {"last_name": "Qurbonov", "first_name": "JAvohir", "birthdate": "2001.09.12"},
    "ad2001156": {"last_name": "Abduhakimov", "first_name": "Javohir", "birthdate": "2001.06.15"},
}

BANK = {
    "ad1234567": {"account_b": 950.7, "karta": "1234567897654321", "birlik": "$"},
    "ad7654321": {"account_b": 1950.7, "karta": "1234567897654322", "birlik": "$"},
    "ad2001129": {"account_b": 650.7, "karta": "1234567897654323", "birlik": "$"},
    "ad2001156": {"account_b": 450.7, "karta": "1234567897654324", "birlik": "$"},
}

KAMUNAL = {
    "elektr": {
        "ad1234567": {"shot": "7654321", "qoldiq": 40},
        "ad7654321": {"shot": "7654322", "qoldiq": 42},
        "ad2001129": {"shot": "7654323", "qoldiq": 44},
        "ad2001156": {"shot": "7654324", "qoldiq": 45},
    }
}

PAYNET = {
    "ad1234567": {"username": "ali", "parol": "1234", "karta": "1234567897654321"},

}


# person_info

def person_info(id):
    standard = 9
    if len(id) != standard:
        return "9ta belgidan iborat emas"
    answer = PASSPORT.get(id, None)
    if answer is not None:
        answer = f"""
        Ismi:{answer['first_name']}
        Familiya:{answer['last_name']}
        Age:{answer["birthdate"]}   
    """
        return answer
    else:
        return None


def bank_info(id):
    standart = 9
    if len(id) != standart:
        return f"9 ta belgidan iborat bo'lishi kerak!!!"
    answer = BANK.get(id, None)
    if answer is not None:
        answer = f"""
        ID:{id}
        Account_Balance:{answer['account_b']}
        Karta:{answer['karta']}
        Birlik:{answer["birlik"]}   
    """
        return answer
    else:
        return None


def kamunal_info(id):
    standart = 9
    if len(id) != standart:
        return f"9 ta belgidan iborat bo'lishi kerak!!!"
    answer = KAMUNAL['elektr'].get(id)
    if answer is not None:

        answer = KAMUNAL['elektr'].get(id, "bunday fuqora mavjud emas")
        answer = f"""
        ID:{id}
        Shot:{answer['shot']}
        Qoldiq:{answer['qoldiq']} 
    """
        return answer
    else:
        return None


# print(kamunal_info("ad1234567"))


def create_paynet_account(id, username, parol):
    person = person_info(id)
    if person:
        PAYNET[id] = {}
        PAYNET[id]['username'] = username
        PAYNET[id]['parol'] = parol
        print(f"Xush kelibsiz {person}")

def add_card(id, card_number, card_date):
    if id in PASSPORT:
        PASSPORT[id]["card_number"] = card_number


print(create_paynet_account("ad1234567", "realchi", "2486"))
print(PAYNET)
