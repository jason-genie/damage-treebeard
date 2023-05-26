from rest_framework import serializers
from .models import Property, Item, Tenant, Damage
class OwnerPropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'title', 'address', 'year_built', 'year_bought', 'tenant_list', 'item_list']

class OwnerItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'item_type', 'cost_original', 'cost_replacement', 'quantity_present']

class OwnerTenantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tenant
        fields = ['id', 'name', 'rent_amount', 'deposit_amount', 'in_date', 'out_date', 'duration', 'damage_list']


class OwnerDamageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Damage
        fields = ['id', 'description', 'quantity_damaged', 'cost_to_repair', 'item_id', 'damage_type', 'title']