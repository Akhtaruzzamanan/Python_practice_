# fruits = ["apple", "banana", "chery", "mango", "orange", "lichi", "jackfruit", "coconut"]
# fruits.append("painaple")
# fruits.sort()
# fruits.reverse()
# fruits.insert(2, "plum")
# fruits.remove("coconut")
# item = fruits.pop(6)
# lis = " ".join(fruits)
# print(lis)
# print(fruits)

li = [1, 2, 3, 4]
# new_lis = []
# for x in li:
#     new_lis.append(x * 2)

new_lis = [x * x for x in li]
print(new_lis)