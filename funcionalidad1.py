

def credentialsGenerator(txt, complement, year):
    name = txt[0:3].lower() + '.' + complement.lower()
    pwd = complement.lower + str(year)
    return name, pwd

class Person1:
    nombre = 'John'
    ap_paterno = 'Doe'
    year = 2020
                
autoUsername = credentialsGenerator(Person.nombre Person1.ap_paterno, Person1.year)
print('auto-username: ', autoUsername)