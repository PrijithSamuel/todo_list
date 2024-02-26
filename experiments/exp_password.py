def strength(password):
    d = {'length': False, 'uppercase': False, 'digit': False}
    if len(password) > 8:
        d['length'] = True
    for char in password:
        if char.isupper():
            d['uppercase'] = True
        if char.isupper():
            d['digit'] = True

    if all(d.values()):
        return 'Strong Password'
    else:
        return 'Weak Password'


