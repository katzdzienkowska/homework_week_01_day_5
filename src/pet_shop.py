#1st test:

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#2nd test:

def get_total_cash(total_cash):
    return total_cash["admin"]["total_cash"]

#3rd and 4th test:

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash

#5th test:
def get_pets_sold(sold):
    return sold["admin"]["pets_sold"]

#6th test:
def increase_pets_sold(pet_shop, number):
    pet_shop["admin"]["pets_sold"] += number

#7th test:
def get_stock_count(pet_shop):
   return len(pet_shop["pets"])

#8th and 9th test:
def get_pets_by_breed(pet_shop, breed):
    search_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            search_breed.append(pet)
    return search_breed

#10th test:
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet

#11th test:
def find_pet_by_name(pet_shop, name):
    for pet in pet_shop["pets"]:
        if pet["name"] == name:
            return pet
    return None

#12th test:
def remove_pet_by_name(pet_shop, name):
    for index, pet in enumerate(pet_shop["pets"]):        
       if pet["name"] == name:
            pet_shop["pets"].pop(index)
    return None

#13th test:
def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

#14th test:
def get_customer_cash(customers):
    return customers["cash"]

#15th test:
def remove_customer_cash(customers, cash):
    customers["cash"] -= cash

#16th test:
def get_customer_pet_count(customers):
   return len(customers["pets"])

#17th test:
def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

    # --- OPTIONAL ---

#18th, 19th and 20th test:
def customer_can_afford_pet(customers, new_pet):
    if customers["cash"] >= new_pet["price"]:
        return True
    return False