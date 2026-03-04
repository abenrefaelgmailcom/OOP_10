# =========================
# Q1 - Hash + Equality (set + dict)
# =========================

class AlwaysEqual:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        # Always return the same hash value (forces hash collisions)
        return 999

    def __eq__(self, other):
        # Only comparable to the same class
        if not isinstance(other, AlwaysEqual):
            return False
        # Always say "we are equal" no matter the internal value
        return True


class NeverEqual:
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        # Always return the same hash value (forces hash collisions)
        return 999

    def __eq__(self, other):
        # Only comparable to the same class
        if not isinstance(other, NeverEqual):
            return False
        # Always say "we are NOT equal" even if value is identical
        return False


def demo_version_a():
    obj_a = AlwaysEqual(10)
    obj_b = AlwaysEqual(10)

    s = set()
    s.add(obj_a)
    s.add(obj_b)

    print("=== Version A (AlwaysEqual) ===")
    print("Set length:", len(s))

    d = {}
    d[obj_a] = "apple"
    d[obj_b] = "banana"

    print("Dict length:", len(d))
    print("d[obj_a]:", d[obj_a])
    print("Did second insert override first? ->", d[obj_a] == "banana")
    print()


def demo_version_b():
    obj_a = NeverEqual(10)
    obj_b = NeverEqual(10)

    s = set()
    s.add(obj_a)
    s.add(obj_b)

    print("=== Version B (NeverEqual) ===")
    print("Set length:", len(s))

    d = {}
    d[obj_a] = "cat"
    d[obj_b] = "dog"

    print("Dict length:", len(d))
    print("d[obj_a]:", d[obj_a])
    print("d[obj_b]:", d[obj_b])
    print()


# =========================
# Q2 - *args: duplicates
# =========================

def has_duplicates(*args):
    # Return True if any value appears at least twice, else False
    seen = set()
    for x in args:
        if x in seen:
            return True
        seen.add(x)
    return False


def find_duplicates(*args):
    # Return a set of values that appear 2+ times
    seen = set()
    dupes = set()
    for x in args:
        if x in seen:
            dupes.add(x)
        else:
            seen.add(x)
    return dupes


# =========================
# Q3 - **kwargs: pick keys by prefix
# =========================

def pick_keys(prefix="is_", **kwargs):
    # Return a new dict with only keys that start with the given prefix
    result = {}
    for k, v in kwargs.items():
        if k.startswith(prefix):
            result[k] = v
    return result


if __name__ == "__main__":
    # Run demos for Q1
    demo_version_a()
    demo_version_b()

    # Demo for Q2
    print("=== Q2 Demos ===")
    print(has_duplicates(1, 2, 3))              # expected: False
    print(has_duplicates(1, 2, 2, 3))           # expected: True
    print(has_duplicates("a", "b", "a"))        # expected: True
    print(find_duplicates(1, 2, 2, 3, 3, 3))    # expected: {2, 3}
    print()

    # Demo for Q3
    print("=== Q3 Demos ===")
    result = pick_keys(name="Dana", is_admin=True, age=20, is_active=False)
    print(result)  # expected: {'is_admin': True, 'is_active': False}

    result2 = pick_keys(prefix="has_", has_car=True, has_pet=False, is_admin=True)
    print(result2)  # expected: {'has_car': True, 'has_pet': False}
