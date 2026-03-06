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


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    fire = partial(base_enchantment, power=50, element="Fire")
    ice = partial(base_enchantment, power=50, element="Ice")
    lightning = partial(base_enchantment, power=50, element="Lightning")

    return {
        "fire_enchant": fire,
        "ice_enchant": ice,
        "lightning_enchant": lightning,
    }


@lru_cache(maxsize=128)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:

    @singledispatch
    def dispatch(spell: any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: deals {spell * 10} damage!"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment spell: {spell.upper()} enchantment applied!"

    @dispatch.register(list)
    def _(spell: list) -> str:
        results = [dispatch(s) for s in spell]
        combined = "\n  ".join(results)
        return f"Multi-cast spell:\n  {combined}"

    return dispatch


def main():
    print("\nTesting spell reducer...")
    spells = [20, 40, 30, 10]
    print(f"Sum: {spell_reducer(spells, "add")}")
    print(f"Product: {spell_reducer(spells, "multiply")}")
    print(f"Max: {spell_reducer(spells, "max")}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")


if __name__ == "__main__":
    main()
