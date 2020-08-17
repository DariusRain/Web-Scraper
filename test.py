from address_parser import Parser

parser=Parser()
adr = parser.parse("719 S. Burnside Ave, Suite D, Gonzales, LA , Gonzales, Louisiana 70737, United States".replace("United States", ""))
print(adr.dict)
