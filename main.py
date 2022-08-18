import re

postcodes= [
''
'M1 1AA',
'M60 1NW',
'CR2 6XH',
'DN55 1PT',
'W1A 1HQ',
'EC1A 1BB'
]

# A regular expression that matches a postcode based on the UK postcode rules
# This means it should have two sections; the first is 2-4 characters that begins with a letter (outward code)
# The second section contains 3 characters that begins with a number (inward code)
statement = r"([A-Z])([A-Z0-9]{1,3}) (\d)([A-Z0-9]{2})"


for postcode in postcodes:
    match = re.search(statement,postcode)
    if match:
        print (postcode,'is a valid UK postcode')
    else:
        print (postcode, 'is not a valid UK postcode')

