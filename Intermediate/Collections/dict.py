# Dictionary is a key : value function, duplicate Keys not allowed.

user = {
    "name": "Surya",
    "age":20,
    "college":"IFET"
}

print(user)
print(type(user))
print(user["name"])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())

for i in user:          # iterate keys and values.
    # print(i)
    # print(user[i])
    print(i,'',user[i])

for i in user.keys():   # iterate only keys using keys() function.
    print(i)

for i in user.values(): # iterate only values using values() function.
    print(i)

for i in user.items():  # iterate all elements using items() function with One variable.
    print(i)

for i,j in user.items(): # iterate all elements using items() function with Two variable.
    print(i,j)

if "age" in user:        # if "age" key is available in Dict means it'll print Presetn else None.
    print("Present")

# update() ==> adding keys and values to dict that exist or created already.

user.update({"sex":"male"})
print(user)

user["age"] = 19
print(user)

user.pop("age")
print(user)

user.clear()
print(user)

del user
# print(user)

users = {
    "user1" :{
        'name' : 'gowtham',
        'age' : 18,
        'college' : 'IFET'
    },
    "user2" :{
        'name' : 'muthamizh',
        'age' : 20,
        'college' : 'IFET'
    },
    "user3" :{
        'name' : 'vignesh',
        'age' : 17,
        'college' : 'IFET'
    }
}

for i,j in users.items():     # iterate nested dict with all indexes.
    print(i,j)

for i,j in users["user1"].items(): # iterate particular index.
    print(i,j)