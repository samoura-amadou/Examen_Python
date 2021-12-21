data = [{
"first_name":"Ilyès",
"last_name":"Fleury",
"address_street":"Rue Paul Bert",
"address_number":73,
"city":"Dunkerque",
"postcode":12681
},{
"first_name":"Lia",
"last_name":"Dumont",
"address_street":"Rue Louis-Blanqui",
"address_number":30,
"city":"Lille",
"postcode":63996
},{
"first_name":"Eléonore",
"last_name":"Caron",
"address_street":"Avenue du Château",
"address_number":87,
"city":"Rennes",
"postcode":78482
},{
"first_name":"Eva",
"last_name":"Girard",
"address_street":"Rue du Bon-Pasteur",
"address_number":9,
"city":"Rueil-Malmaison",
"postcode":23879
}]


class Persona:
    def __init__(self,first_name = 'Emilien', last_name = 'Duval'):
        self._first_name = first_name
        self._last_name = last_name
        self._address_street = ""
        self._address_number = 0
        self._city = ""
        self._postcode = ""

 
    def __str__(self):
        return "Hi ! I'm " + self._first_name + " " + self._last_name + "."

    def set_adress(self, address_street, address_number, city, postcode):
    	self._address_street = address_street
    	self._address_number = address_number
    	self._city = city
    	self._postcode = postcode   

    def show_address(self):
    	print(f"My full address is : {self._address_number}  {self._address_street} , {self._city} ({self._postcode})")
 
for i in data:
	objet = Persona(i["first_name"],i["last_name"])
	print(objet)
	objet.set_adress(i["address_street"], i["address_number"], i["city"], i["postcode"])
	objet.show_address()
	print("--")