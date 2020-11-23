# part 1
dct = {"city": "Москва", "temperature": "20"}
print(dct['city'])
dct['temperature'] = str(int(dct['temperature']) - 5)
print(dct)

# part 2
k = 'country'
print(f"key '{k}' {'not' if dct.get(k) is None else ''} found")
print(dct.get(k, "Россия"))
dct['date'] = "27.05.2019"
print(len(dct))
