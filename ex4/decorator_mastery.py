from typing import Callable
from functools import wraps

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        pass

    def cast_spell(self, spell_name: str, power: int) -> str:
        pass




def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper():
        # code before
        print(f"Casting {func.__name__}")
        result = func()   # original function runs here
        # code after
        print("Spell completed in time seconds")
        return result
    return wrapper



def power_validator(min_power: int) -> Callable:
    def wrapper(power):
        if power >= min_power:
            result = 
    return wrapper

def retry_spell(max_attempts: int) -> Callable:


def main():
    print("Testing spell timer...")


