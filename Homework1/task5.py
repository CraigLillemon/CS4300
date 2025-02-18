listing = ["Harry potter", "Percy jackson", "Lord of the rings", "The hobbit"]
diction = {12312: "Craig", 1232141: "Mike"}

print(listing[0:3])
print(diction)
assert diction[12312] == "Craig"
assert listing[0:3] == ["Harry potter", "Percy jackson", "Lord of the rings"]