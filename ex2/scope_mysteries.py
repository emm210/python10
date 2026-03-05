from typing import Callable


def mage_counter() -> Callable:
    count = 0             
    
    def increment():
        nonlocal count     
        count += 1
        return count

    return increment

def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power
    def accumulator(power: int):
        nonlocal total
        total += power
        return total
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    
    def enchantment(item_name):
        return f"{enchantment_type} {item_name}"
    return enchantment

def memory_vault() -> dict[str, Callable]:
    result_dict = {}
    def store(key, value):
        result_dict[key] = value
    def recall(key):
        return result_dict.get(key, "Memory not found")

    return {"store": store, "recall": recall}

# # accumulator = spell_accumulator(10)
# # print(f"{accumulator(10)}")
# # print(f"{accumulator(10)}")
# ench = enchantment_factory("Flaming")
# print(f"{ench('Sword')}")

def main():
    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")
    print("\nTesting enchantment factory...")
    ench1 = enchantment_factory("Flaming")
    print(f"{ench1("Sword")}")
    ench2 = enchantment_factory("Frozen")
    print(f"{ench2("Shield")}")

main()