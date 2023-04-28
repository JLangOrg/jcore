def store(input):
  parts = input.split(' ')
  with open("store.json", "r") as storefile:
    store = storefile.read()
    store[parts[0]] = parts[2]
  with open("store.json", "w") as storefile:
    storefile.write(store)
