phones = {
    'Oleg': ['0501112233', '0112223366'],
    'Max': ['0223336677'],
    'Lena': ['0112223366', '03322335544'],
}

sorted_phones = {}

for person in phones:
    for phone in phones[person]:
        # print(phone)
        sorted_phones.setdefault(phone, [])
        sorted_phones[phone].append(person)

print(sorted_phones)