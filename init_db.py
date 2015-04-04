#!/user/bin/env python3

#initialize django

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'chf.settings'
import django
django.setup()


#regular imports

import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess, sys


#empty (or drop) db

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")

#create db

cursor.execute("CREATE SCHEMA PUBLIC")

#Migrage db

subprocess.call([sys.executable, "manage.py", "migrate"])

#initialize tables

####################################### Groups #######################################

#Delete old groups

Group.objects.all().delete()

#Create new groups, Admin, Manager, Guest
for data in [
  ['Admin'],
  ['Manager'],
  ['Guest'],
]:

    #create group, set name
    g = Group()
    g.name = data[0]

    #save
    g.save()


####################################### Permission #######################################

permissions = Permission.objects.all()

# Give admin permission

for p in permissions:
    g = Group.objects.get(name="Admin")
    g.permissions.add(p)

    g.save()

for p in permissions:
    g = Group.objects.get(name="Manager")

    #if permission is in the right range, then add to group
    if p.id > 15:
        g.permissions.add(p)

    g.save()


####################################### User #######################################

#Delete old users
hmod.User.objects.all().delete()

#Create new users: username, password, first_name, last_name, is_superuser, group, full_name, email
for data in [
  ['danmo91', 'password', 'Dan', 'Morain', True, True, 'Admin', 'Dan Morain', 'dan.morain91@gmail.com'],
  ['mojok13', 'password', 'Morgs', 'Kap', False, True, 'Manager', 'Morgs Kap', 'mojo@gmail.com'],
  ['breezy', 'password', 'Bri', 'Sor', False, False, 'Guest', 'Bri Sor', 'breezy@gmail.com'],
  ['urge', 'password', 'Rj', 'Smith', False, False, 'Guest', 'Rj Smith', 'urge@gmail.com'],
]:

    #set attributes
    u = hmod.User()
    u.username = data[0]
    u.set_password(data[1])
    u.first_name = data[2]
    u.last_name = data[3]
    u.is_superuser = data[4]
    u.is_staff = data[5]
    u.full_name = data[7]
    u.account_balance = 0.00
    u.email = data[8]

    #save
    u.save()

    # Add user to group
    g = Group.objects.get(name=data[6])
    u.groups.add(g)

####################################### Venue #######################################

# Delete old Venue
hmod.Venue.objects.all().delete()

#Create new venue
for data in [
  ['Velor', 'Hipster paradise', '123 University', 'Provo', 'UT', '84606'],
  ['Scera', 'Theatre', '123 State', 'Orem', 'UT', '84606'],
  ['Brigham Young University', 'My school', '456 University', 'Provo', 'UT', '84606'],
  ['Home', 'Where i sleep', '123 900 E', 'Provo', 'UT', '84606'],
]:

    v = hmod.Venue()


    # set attributes
    v.name = data[0]
    v.description = data[1]
    v.street = data[2]
    v.city = data[3]
    v.state = data[4]
    v.zip_code = data[5]

    #save
    v.save()


####################################### event #######################################

#Delete old events
hmod.Event.objects.all().delete()

#Create new events: name, description, start, end, venue
for data in [
  ['Questival','The best day of your life','2015-04-06','2015-04-07','Velor'],
  ['Baptism','For Dan','2015-03-12','2015-03-12','Velor'],
  ['Bonfire','For the besties','2015-02-28','2015-02-28','Velor'],
  ['Dinner Nite','Going away dinner for Jeff','2015-05-05','2015-05-05','Velor'],
]:

    #set attributes
    e = hmod.Event()
    e.name = data[0]
    e.description = data[1]
    e.start = data[2]
    e.end = data[3]
    e.venue = hmod.Venue.objects.get(name=data[4])

    #save
    e.save()

####################################### Area #######################################

# Delete old Area
hmod.Area.objects.all().delete()

#Create new Area
for data in [
  ['Candle Shop', 'Sell scented candles', 'Scera', 'Questival'],
  ['Bricks', 'Sell scented bricks', 'Scera', 'Baptism'],
  ['Gun power', 'Get blasted', 'Home', 'Dinner Nite'],
  ['Bakery', 'Sell scented bread', 'Scera', 'Bonfire'],
]:

    a = hmod.Area()

    # set attributes
    a.name = data[0]
    a.description = data[1]
    a.venue = hmod.Venue.objects.get(name=data[2])
    a.event = hmod.Event.objects.get(name=data[3])

    #save
    a.save()

####################################### Items #######################################

#Delete old items
hmod.Item.objects.all().delete()

#Create new items: name, description, value, rental_price
for data in [
  ['Knife' , 'Stabbed Julius Caesar.  Still soaked with blood', '999.99', '9.99'],
  ['Rope' , 'Judas Iscariot hung himself with this rope', '1.15', '1.99'],
  ['Backpack' , 'From Cotopaxi, features real llama fit.  Really, its nice', '29.50', '12.99'],
  ['Canteen' , '12 oz. of this stuff will quench your thirst for a while', '5.55', '5.99'],
]:

    i = hmod.Item()
    i.name = data[0]
    i.description = data[1]
    i.value = data[2]
    i.rental_price = data[3]

    i.save()

####################################### Products #######################################

#Delete old Products
hmod.Product.objects.all().delete()

#Create new Products: name, description, category, current_price
for data in [
  ['Poem Journal', 'Jot down anything that comes to your mind.  I sure have a lot.', 'Crafts', '14.00'],
  ['Ice', 'Cool off with this stuff.  It really has a chill feeling.', 'Household', '2.00'],
  ['Quill', 'Birds of a feather, make me want to kill them so i can write with their feathers', 'Collectors', '8.00'],
  ['Abacus', 'Count better than anyone', 'Business', '13.00'],

]:

    p = hmod.Product()
    p.name = data[0]
    p.description = data[1]
    p.category = data[2]
    p.current_price = data[3]

    p.save()

####################################### Rentals #######################################

#Delete old Rentals
hmod.Rental.objects.all().delete()

#Create new Rentals: description,rental_date,due_date, user
for data in [
  # under 30
  ['Pony Ride', '2015-03-06', '2014-03-06', '1'],
  ['Icecream Maker', '2015-03-06', '2015-03-06', '1'],
  ['Colonial Flag', '2015-03-06', '2015-03-06', '1'],
  ['Abicus', '2015-03-06', '2015-03-06', '1'],
  # over 30
  ['Napkin', '2015-03-06', '2015-03-01', '1'],
  ['Charger', '2015-03-06', '2015-03-01', '1'],
  ['Monitor', '2015-03-06', '2015-03-01', '1'],
  ['Window', '2015-03-06', '2015-03-01', '1'],
  # over 60
  ['Mouse', '2015-03-06', '2015-02-01', '1'],
  ['Caffine', '2015-03-06', '2015-02-01', '1'],
  ['Cliff Bar', '2015-03-06', '2015-02-01', '1'],
  ['Paper', '2015-03-06', '2015-02-01', '1'],
  # over 90
  ['Heart Break', '2015-03-06', '2015-01-01', '1'],
  ['Clock', '2015-03-06', '2015-01-01', '1'],
  ['Cable', '2015-03-06', '2015-01-01', '1'],
  ['Conference', '2015-03-06', '2015-01-01', '1'],

]:

    r= hmod.Rental()
    r.description = data[0]
    r.rental_date = data[1]
    r.due_date = data[2]
    user = hmod.User.objects.get(id=data[3])
    r.user = user

    print('Rental:', r)

    r.save()

####################################### Orders #######################################

#Delete old Orders
hmod.Order.objects.all().delete()

#Create new Rentals: order_date, total, user
for data in [
  ['2015-03-06', '20.22', '1'],
  ['2015-03-06', '30.33', '2'],
  ['2015-03-06', '40.44', '3'],
  ['2015-03-06', '50.55', '4'],

]:

    o = hmod.Order()
    o.order_date = data[0]
    o.total = data[1]

    user = hmod.User.objects.get(id=data[2])

    o.user = user

    o.save()
