def prioritize(tests, changed_paths):
# naive: tests containing changed path names first, then others alphabetically
changed = [t for t in tests if any(p in t for p in changed_paths)]
rest = [t for t in tests if t not in changed]
return sorted(set(changed)) + sorted(set(rest))