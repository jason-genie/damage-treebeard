from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from owner.models import Property, Item, Tenant, Damage

class MyAdmin(TreeAdmin):
    form = movenodeform_factory(Property)

admin.site.register([Property, Item, Tenant, Damage], MyAdmin)