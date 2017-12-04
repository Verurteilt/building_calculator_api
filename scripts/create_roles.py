"""
	03/12/2017
	Victor Castillo
	This script will populate the Roles table
""" 


def run():
	import time
	from roles.models import Roles

	t1 = time.time()
	Roles.objects.get_or_create(key="organization_admin", defaults={'name': 'Organization Admin'})
	Roles.objects.get_or_create(key="seller", defaults={'name': 'Seller'})
	t2 = time.time()
	print("Roles created, Time=", t2-t1)
