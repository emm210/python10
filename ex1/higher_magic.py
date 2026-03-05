from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs):
        return  base_spell(*args, **kwargs) * multiplier
    return amplified

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditionally_cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return conditionally_cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        spells_list = []
        for s in spells:
            spells_list.append(s(*args, **kwargs))
        return spells_list
    return sequence


def main():
    print("Testing spell combiner...")
    def fireball():
        return "Fireball hits Dragon"
    def heal():
        return "Heals Dragon"
    
    combined = spell_combiner(fireball, heal)
    # combined = spell_combiner(lambda : "Fireball hits Dragon", lambda : "Heals Dragon")
    print(f"Combined spell result: {", ".join(combined())}")

    print("\nTesting power amplifier...")
    def dragon_ball():
        return 10
    amplified = power_amplifier(dragon_ball, 3)
    print(f"Original: {dragon_ball()}, Amplified: {amplified()}")

main()