import datetime
from django.db import models
from django.utils import timezone
from treebeard.mp_tree import MP_Node

class Property(MP_Node):
    title = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    year_built = models.IntegerField()
    year_bought = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    tenant_list = models.CharField(max_length=200, null=True) #json array of ids
    item_list = models.CharField(max_length=200, null=True) #json array of ids
    def __str__(self):
        return self.title
    
# Create your models here.
class UserProfile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')
    def __str__(self):
        return self.last_name

class Item(MP_Node):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    item_type = models.CharField(max_length=200) #TODO enum list 
    quantity_present = models.IntegerField() #whatever units 
    cost_original = models.IntegerField()
    cost_replacement = models.IntegerField()
    def __str__(self):
        return self.title
    
        
class Tenant(MP_Node):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    rent_amount = models.IntegerField()
    deposit_amount = models.IntegerField()
    in_date = models.DateField('date in')
    out_date = models.DateField('date out')
    duration = models.IntegerField() #TODO calculate this 
    damage_list = models.CharField(max_length=200, null=True) #json array of ids
    def __str__(self):
        return self.name
    
class Damage(MP_Node):
    title = models.CharField(max_length=200)
    damage_type = models.CharField(max_length=200) #TODO enum list
    description = models.CharField(max_length=200)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT, null=True)
    quantity_damaged = models.IntegerField() #whatever units 
    cost_to_repair = models.IntegerField()
    #TODO add pictures
    def __str__(self):
        return self.description
    
class PropertyManager(models.Model):
    userprofile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)
    property_list = models.CharField(max_length=200, null=True) #json array of ids
    def __str__(self):
        return self.userprofile.first_name
