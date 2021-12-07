def person():
    {"dict1":{"name":"mel"},"dict2":{"age":11  },"dict3":{"complexion":"dark"}}
for key,value in person.items():
    print(key)
    for stuff in value:
        print(stuff)
    for key in value:
        print(value[key])
    