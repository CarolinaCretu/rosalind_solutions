def gc_count(seq: str) -> float:
    count = 0
    for i in seq:
        if i == "G" or i == "C":
            count += 1
    return round(count * 100 / len(seq), 6)
