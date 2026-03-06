def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined

def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return  base_spell(*args, **kwargs) * multiplier
    return amplified

def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditionally_cast(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return conditionally_cast


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        return list(map(lambda s: s(*args, **kwargs), spells))
    return sequence


def main() -> None:
    print("Testing spell combiner...")
    def fireball():
        return "Fireball hits Dragon"
    def heal():
        return "Heals Dragon"
    
    combined = spell_combiner(fireball, heal)
    print(f"Combined spell result: {', '.join(combined())}")

    print("\nTesting power amplifier...")
    def dragon_ball():
        return 10
    amplified = power_amplifier(dragon_ball, 3)
    print(f"Original: {dragon_ball()}, Amplified: {amplified()}")


if __name__ == "__main__":
    main()