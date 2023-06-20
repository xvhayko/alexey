def count_skills(tree, required):
    unlocked = set()
    for skill in required:
        while skill not in unlocked:
            unlocked.add(skill)
            skill = tree[skill]
    return len(unlocked)