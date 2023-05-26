from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Property, Tenant, Damage, Item
from django.contrib.auth import authenticate, login as auth_login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
import ast
from django.contrib.auth.models import User
# parsing data from the client
from rest_framework.parsers import JSONParser
# API definition for property, tenant, damage
from .serializers import OwnerPropertySerializer, OwnerItemSerializer, OwnerTenantSerializer, OwnerDamageSerializer

# Create your views here.
def owner(request):
    return HttpResponse("owner view")

def index(request):
    item = Item()
    item.quantity=2
    item.description = "doggy"
    item.save()
    return HttpResponse("index view")

@csrf_exempt
def login(request):
    body = json.loads(request.body)
    username = body["username"]
    password = body["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        data = {
            "code": 204,
            "data": { 
                "token": request.session["_auth_user_hash"],
                "username": user.username
            }
        }
        return JsonResponse(data)
    else:
        data = {
            "code": 60204,
            "message": "Account and password are incorrect."
        }
        return JsonResponse(data)

@csrf_exempt
def properties(request):
    '''
    List all properties snippets
    '''
    if(request.method == 'GET'):
        # get all the properties
        properties = Property.objects.all()
        # serialize the property data
        serializer = OwnerPropertySerializer(properties, many=True)
        return_data = []
        for property in serializer.data:
            try:
                item_list = ast.literal_eval(property['item_list'])
                property['itemList'] = []
                for item_id in item_list:
                    item = OwnerItemSerializer(Item.objects.get(pk=item_id)).data
                    property['itemList'].append(item)
            except:
                property['itemList'] = []
            try:
                tenant_list = ast.literal_eval(property['tenant_list'])
                property['tenantList'] = []
                for tenant_id in tenant_list:
                    tenant = OwnerTenantSerializer(Tenant.objects.get(pk=tenant_id)).data
                    try:
                        damage_list = ast.literal_eval(tenant['damage_list'])
                        tenant['damageList'] =[]
                        for damage_id in damage_list:
                            damage = OwnerDamageSerializer(Damage.objects.get(pk=damage_id)).data
                            tenant['damageList'].append(damage)
                    except:
                        tenant['damageList'] = []
                    property['tenantList'].append(tenant)
            except:
                property['tenantList'] = []
            return_data.append(property)
        # return a Json response
        data = {
            "items": return_data,
            "total": len(return_data)
        }
        return JsonResponse(data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = OwnerPropertySerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def property_detail(request, property_id):
    try:
        # obtain the property with the passed id.
        property = Property.objects.get(pk=property_id)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'GET'):
        # serialize the property data
        serializer = OwnerPropertySerializer(property)
        property_data = serializer.data
        try:
            item_list = ast.literal_eval(property_data['item_list'])
            property_data['itemList'] = []
            for item_id in item_list:
                item = OwnerItemSerializer(Item.objects.get(pk=item_id)).data
                property_data['itemList'].append(item)
        except:
            property_data['itemList'] = []
        try:
            tenant_list = ast.literal_eval(property_data['tenant_list'])
            property_data['tenantList'] = []
            for tenant_id in tenant_list:
                tenant = OwnerTenantSerializer(Tenant.objects.get(pk=tenant_id)).data
                property_data['tenantList'].append(tenant)
        except:
            property_data['tenantList'] = []
        return JsonResponse(property_data, status=201)
    elif(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = OwnerPropertySerializer(property, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the property
        property.delete() 
        # return a no content response.
        return HttpResponse(status=204)

@csrf_exempt
def items(request):
    '''
    List all items snippets
    '''
    if(request.method == 'GET'):
        # get all the items
        items = Item.objects.all()
        # serialize the item data
        serializer = OwnerItemSerializer(items, many=True)
        # return a Json response
        data = {
            "items": serializer.data,
            "total": len(serializer.data)
        }
        return JsonResponse(data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = OwnerItemSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def item_detail(request, item_id):
    try:
        # obtain the item with the passed id.
        item = Item.objects.get(pk=item_id)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'GET'):
        # serialize the item data
        serializer = OwnerItemSerializer(item)
        return JsonResponse(serializer.data, status=201)
    elif(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = OwnerItemSerializer(item, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the item
        item.delete() 
        # return a no content response.
        return HttpResponse(status=204)

@csrf_exempt
def tenants(request):
    '''
    List all tenants snippets
    '''
    if(request.method == 'GET'):
        # get all the tenants
        tenants = Tenant.objects.all()
        # serialize the tenant data
        serializer = OwnerTenantSerializer(tenants, many=True)
        # return a Json response
        data = {
            "items": serializer.data,
            "total": len(serializer.data)
        }
        return JsonResponse(data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = OwnerTenantSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def tenant_detail(request, tenant_id):
    try:
        # obtain the tenant with the passed id.
        tenant = Tenant.objects.get(pk=tenant_id)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'GET'):
        # serialize the tenant data
        serializer = OwnerTenantSerializer(tenant)
        return JsonResponse(serializer.data, status=201)
    elif(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = OwnerTenantSerializer(tenant, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the tenant
        tenant.delete() 
        # return a no content response.
        return HttpResponse(status=204)
    
@csrf_exempt
def damages(request):
    '''
    List all damages snippets
    '''
    if(request.method == 'GET'):
        # get all the damages
        damages = Damage.objects.all()
        # serialize the damage data
        serializer = OwnerDamageSerializer(damages, many=True)
        # return a Json response
        data = {
            "items": serializer.data,
            "total": len(serializer.data)
        }
        return JsonResponse(data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = OwnerDamageSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def damage_detail(request, damage_id):
    try:
        # obtain the damage with the passed id.
        damage = Damage.objects.get(pk=damage_id)
    except:
        # respond with a 404 error message
        return HttpResponse(status=404)  
    if(request.method == 'GET'):
        # serialize the tenant data
        serializer = OwnerDamageSerializer(damage)
        return JsonResponse(serializer.data, status=201)
    elif(request.method == 'PUT'):
        # parse the incoming information
        data = JSONParser().parse(request)  
        # instanciate with the serializer
        serializer = OwnerDamageSerializer(damage, data=data)
        # check whether the sent information is okay
        if(serializer.is_valid()):  
            # if okay, save it on the database
            serializer.save() 
            # provide a JSON response with the data that was submitted
            return JsonResponse(serializer.data, status=201)
        # provide a JSON response with the necessary error information
        return JsonResponse(serializer.errors, status=400)
    elif(request.method == 'DELETE'):
        # delete the damage
        damage.delete() 
        # return a no content response.
        return HttpResponse(status=204) 