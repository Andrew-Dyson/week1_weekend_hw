def get_pet_shop_name(requested_pet_shop):
    return requested_pet_shop["name"]

def get_total_cash(requested_pet_shop):
    return requested_pet_shop["admin"]["total_cash"]

def add_or_remove_cash(requested_pet_shop, transacted_cash):
    requested_pet_shop["admin"]["total_cash"] += transacted_cash

def get_pets_sold(requested_pet_shop):
    return requested_pet_shop["admin"]["pets_sold"]

def increase_pets_sold(requested_pet_shop, change_in_number_of_pets_sold):
    requested_pet_shop["admin"]["pets_sold"] += change_in_number_of_pets_sold

def get_stock_count(requested_pet_shop):
    return len(requested_pet_shop["pets"])

def get_pets_by_breed(requested_pet_shop, requested_breed):
    matched_breeds = []
    for pet in range(len(requested_pet_shop["pets"])):
        if requested_pet_shop["pets"][pet]["breed"] == requested_breed:
            matched_breeds.append(requested_breed)
    return matched_breeds

# def find_pet_by_name(requested_pet_shop, pet_name_to_search):
#     for pet in range(len(requested_pet_shop["pets"])):
#         if requested_pet_shop["pets"][pet]["name"] == pet_name_to_search:
#             return pet
        # else: 
        #     return None     # Gives error
        
def find_pet_by_name(requested_pet_shop, pet_name_to_search):
    pets = requested_pet_shop["pets"]
    for pet in pets:
        if pet["name"] == pet_name_to_search:
            return pet   
        # else: 
        #     return None     # Gives error

def find_pet_by_name__returns_None(requested_pet_shop, pet_name_to_search):
    pets = requested_pet_shop["pets"]
    for pet in pets:
        if pet["name"] == pet_name_to_search:
            return pet
        else: 
            return None   


def remove_pet_by_name(requested_pet_shop, pet_name_to_remove):
    pets = requested_pet_shop["pets"]
    for pet in pets:
        if pet["name"] == pet_name_to_remove:
            pets.remove(pet)
            return None
        
def add_pet_to_stock(requested_pet_shop, pet_name_to_add):
    pets = requested_pet_shop["pets"]
    pets.append(pet_name_to_add)

def get_customer_cash(customers):
    return customers["cash"]

def remove_customer_cash(customer_to_remove_cash, amount_to_remove):
    customer_to_remove_cash["cash"] -= amount_to_remove

def get_customer_pet_count(customer_to_count_pets):
    return len(customer_to_count_pets["pets"])

def add_pet_to_customer(customer_to_add_pet_to, pet_to_add):
    customer_to_add_pet_to["pets"].append(pet_to_add)
    
def customer_can_afford_pet(customer_to_check_affordability, potential_new_pet):
    new_pet_price = potential_new_pet["price"]
    customer_current_cash = customer_to_check_affordability["cash"]
    if customer_current_cash >= new_pet_price:
        return True
    else:
        return False
    
# def sell_pet_to_customer(requested_pet_shop, pet_to_sell, customer_requesting_pet):
#     remove_pet_by_name(requested_pet_shop, pet_to_sell)
#     add_pet_to_customer(customer_requesting_pet, pet_to_sell)
#     pets = requested_pet_shop["pets"]
#     for pet in pets:
#         pet_price = pet_to_sell["price"]
#     add_or_remove_cash(requested_pet_shop, pet_price)
#     remove_customer_cash(customer_requesting_pet, pet_price)
#     increase_pets_sold(requested_pet_shop, len(customer_requesting_pet["pets"]))

def sell_pet_to_customer(requested_pet_shop, pet_to_sell, customer_requesting_pet):
    pets = requested_pet_shop["pets"]
    for pet in pets:
        if pet["name"] == pet_to_sell:
            remove_pet_by_name(requested_pet_shop, pet_to_sell)
            add_pet_to_customer(customer_requesting_pet, pet_to_sell)
            pets = requested_pet_shop["pets"]
            for pet in pets:
                pet_price = pet_to_sell["price"]
            add_or_remove_cash(requested_pet_shop, pet_price)
            remove_customer_cash(customer_requesting_pet, pet_price)
            increase_pets_sold(requested_pet_shop, len(customer_requesting_pet["pets"]))

# def sell_pet_to_customer(requested_pet_shop, pet_to_sell, customer_requesting_pet):
#     pets = requested_pet_shop["pets"]
#     for pet in pets:
#         pet_price = pet_to_sell["price"]
#         if pet["name"] == pet_to_sell:
#             remove_pet_by_name(requested_pet_shop, pet_to_sell)
#             add_pet_to_customer(customer_requesting_pet, pet_to_sell)
#             add_or_remove_cash(requested_pet_shop, pet_price)
#             remove_customer_cash(customer_requesting_pet, pet_price)
#             increase_pets_sold(requested_pet_shop, 1)