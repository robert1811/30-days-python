countries = {
    'germany': 'berlin',
    'france': 'paris',
    'spain': 'madrid',
    'united kingdom': 'london',
    'poland': 'warsaw',
    'russia':'moscow',
    'ukraine':'kiev',
    'italy':'rome',
    'netherlands':'amsterdam',
    'austria':'viena',
    'united states':'washington',
    'canada':'ottawa',
    'mexico':'mexico city',
    'venezuela':'caracas',
    'colombia':'bogota',
    'ecuador':'quito',
    'peru':'lima',
    'bolivia':'sucre',
    'paraguay':'asuncion',
    'chile':'santiago',
    'argentina': 'Buenos Aires',
    'uruguay':'montevideo',
    'brazil':'brasilia',
}

def capitalFinder():
    country = input('type a country: ')
    capital = countries.get(country.lower())

    if capital != None:
        print('The capital of ' + country.capitalize() + ' is ' + capital.capitalize())
    else:
         print('We havent that country')
    capitalFinder()
capitalFinder()