

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts, key = lambda p:p['power'], reverse=True)
    return sorted_artifacts

def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    min_power = min(mages, key = lambda m:m['power'])
    return list(filter(lambda m: mages['power']>= min_power, mages))

def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s:'* ' + s + ' *', spells))

def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key = lambda p:p['power'])
    min_power = min(mages, key = lambda p:p['power'])
    avg_power = sum(mages, key = lambda p:p['power']) / len(mages)
    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power
    }

def main():
    print("Testing artifact sorter...")
    artifacts = [{"name":"Crystal Orb", "power":85}, {"name":"Fire Staff", "power":92}]
    sorted = artifact_sorter(artifacts)
    print(f"{sorted[0]['name']} ({sorted[0]['power']} power) comes before {sorted[1]['name']} ({sorted[1]['power']} power)")

    print("Testing spell transformer...")
    spells = ["fireball", "heal", "shield"]
    returned_spells = spell_transformer(spells)
    print(f"{" ".join(returned_spells)}")
main()