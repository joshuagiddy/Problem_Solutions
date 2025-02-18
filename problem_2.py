fish = ["flounder", "sole", "blue cod", "snapper", "terakihi", "john dory", "red cod"]

for f in fish:
    print(f[0])

for f in fish:
    print(f[:3])

for f in fish:
    if f == "flounder":
        print(f)

for f in fish:
    if " " in f:
        print(f)

for f in fish:
    if "cod" in f:
        print(f)
