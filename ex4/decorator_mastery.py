from typing import Callable
from functools import wraps
import time

def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        # code before
        print(f"Casting {func.__name__}")
        start = time.time()
        result = func()
        end = time.time()
        print(f"Spell completed in {end - start} seconds")
        return result
    return wrapper



def power_validator(min_power: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(self, spell_name ,power, *arg, **kwargs):
            if power < min_power:
                return "Insufficient power for this spell"
            return func(self, spell_name, power, *arg, **kwargs)
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying...")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        if not name.replace(" ", "").isalpha():
            return False
        return True
    
    @power_validator(min_power = 10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"

def main():
    print("Testing spell timer...")
    @spell_timer
    def fireball():
        return "Fireball cast!"
    
    print(f"Result: {fireball()}")
    print("\nTesting MageGuild...")
    mageGuild = MageGuild()
    print(f"{mageGuild.validate_mage_name("Lightning")}")
    print(f"{mageGuild.validate_mage_name("Fireball_100")}")
    print(f"{mageGuild.cast_spell("Lightning",15)}")
    print(f"{mageGuild.cast_spell("Lightning",8)}")


main()


