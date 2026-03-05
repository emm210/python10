from typing import Callable
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(operator.add, spells)
    elif operation == "multiply":
        return reduce(operator.mul, spells)
    elif operation == "max":
        return reduce(lambda acc, x: acc if acc > x else x, spells) 
    elif operation == "min":
        return reduce(lambda acc, x: acc if acc < x else x, spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fire_enchant = partial(base_enchantment,  power=50, element = "Fire")
    ice_enchant = partial(base_enchantment, power = 50, element = "Ice")
    lightning_enchant = partial(base_enchantment, power = 50, element = "Lightning")

    return {
        "fire_enchant": fire_enchant,
        "ice_enchant": ice_enchant,
        "lightning_enchant": lightning_enchant
    }
@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)

@singledispatch
def spell_dispatcher() -> Callable:

    @singledispatch
    def dispatch(spell):
        return "Unknown spell type"
    @dispatch.register(int)
    def _(spell):
        return f"Damage spell: deals {spell * 10} damage!"
    
    @dispatch.register(str)
    def _(spell):
        return f"Enchantment spell: {spell.upper()} enchantment applied!"
    
    @dispatch.register(list)
    def _(spell):
        results = [dispatch(s) for s in spell]
        combined = "\n  ".join(results)
        return f"Multi-cast spell:\n  {combined}"
    
    return dispatch

def main():
    print("Testing spell reducer...")
    spells = [20, 40, 30, 10]
    print(f"Sum: {spell_reducer(spells, "add")}")
    print(f"Product: {spell_reducer(spells, "multiply")}")
    print(f"Max: {spell_reducer(spells, "max")}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

main()