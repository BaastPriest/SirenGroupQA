import random
user_permanent = "Test User"

zip_code = "09090"

email_permanent = "testuser@gmail.com"


phone_num_permanent = "9143089421"

square_feet_int_random = random.randint(1,100)

phone_num_for_is_correct_question = "5858716227"

domains = ["gmail.com", "yahoo.com","hotmail.com", "aol.com", "outlook.com", "hotmail.com", "proton.me"]
names = ["James", "Michael", "Robert", "Maria", "Mary", "David"]
last_names = ["Smith","Garcia","Rodriguez","Hernandez"]

phone_num_codes = ["484","517", "610", "814","769","406","702", "603","205", "907","480","501","508", "310",
                   "860","302","316","319", "202","207","208","225", "270","612", "689","730","762","765","808",
                   "609","505","336","216","405","503","215"]

def create_email():
    return f'{random.choice(names)}{random.choice(last_names)}-{random.randint(1,2023)}@{random.choice(domains)}'

def create_full_name():
    return f'{random.choice(names)} {random.choice(last_names)}'

def create_phone_num():
    return f'{random.choice(phone_num_codes)}{random.randint(1000000,9999999)}' #TODO add "0000000"
