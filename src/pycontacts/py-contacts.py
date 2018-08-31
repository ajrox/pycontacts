import yaml
import argparse

def yaml_loader(filepath):
	"""Loads a yaml file"""
	with open(filepath, "r") as file_descriptor:
		data = yaml.load(file_descriptor)
		return data

def yaml_dump(filepath, data):
	"""Dumps data to a yaml file"""
	with open(filepath, "w") as file_descriptor:
		yaml.dump(data, file_descriptor,default_flow_style=False)

def get_contact(filepath, name):
	""" returns all the details of contacts that matches the name"""
	data = yaml_loader(filepath)
	for elem in data:
		if elem["name"] == name:
			print "Name: "+ name +"\t" + "Phone: " + str(elem["phone"])+ "\t\tEmail: " +elem["email"]

def list_all_contacts(filepath):
	"""returns all the contacts with all details"""
	data = yaml_loader(filepath)
	for elem in data:
		print "Name: " + elem["name"] + "\tphone: " + str(elem["phone"]) + "\temail: " + elem["email"]

if __name__ == "__main__":
	filepath = "data/pyContacts.yaml"
	parser = argparse.ArgumentParser()
	#Create all required arguments
	parser.add_argument('-sh', "--show", nargs = "*",help="shows details of saved contact of given name")
	parser.add_argument('-ls', "--list", action = "store_true",help="shows a list of all saved contacts")
	parser.add_argument('--add', nargs = "*", help="adds a new name to the contact")
	parser.add_argument('--number', help="adds number to the contacts file")
	parser.add_argument('--email', help="adds email to the contacts file")
	args = parser.parse_args()
	
	#Use_case 1
	#retrieve a contact
	if args.show != None and len(args.show) > 0:
		a = args.show[0]
		if len(args.show) > 1:
			a += " " + args.show[1]
		get_contact(filepath, a)

	#Use_case 2
	#show all contacts
	if args.list:
		list_all_contacts(filepath)

	#Use_case 3
	#add a new contact
	if args.add != None:
		if args.number == None:
			print "Phone number is required"
		elif args.email == None:
			print "email is required"
		else:
			newName = args.add[0]
			if len(args.add) > 1:
				newName += " " + args.add[1]
			data = yaml_loader(filepath)
			data2 = {'name': newName, 'email': args.email, 'phone': int(args.number)}
			data.append(data2)
			yaml_dump(filepath, data)