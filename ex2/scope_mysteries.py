def mage_counter() -> callable:
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def accumulator(power: int):
        nonlocal total
        total += power
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:

    def enchantment(item_name: str):
        return f"{enchantment_type} {item_name}"

    return enchantment


def memory_vault() -> dict[str, callable]:
    result_dict: dict[str, any] = {}

    def store(key: str, value: any) -> None:
        result_dict[key] = value

    def recall(key: str) -> any:
        return result_dict.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:
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


if __name__ == "__main__":
    main()
