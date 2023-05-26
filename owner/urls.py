from django.urls import path 
from owner import views

# define the urls
urlpatterns = [
    path("", views.index, name = "index"),
    path("login", views.login, name = "login"),

    # urls related properties crud
    path('properties/', views.properties, name = "properties"),
    path("property/<int:property_id>", views.property_detail, name = "property_detail"),
    
    # urls related items crud
    path('items/', views.items, name = "items"),
    path("item/<int:item_id>", views.item_detail, name = "item_detail"),

    # urls related tenants crud
    path('tenants/', views.tenants, name = "tenants"),
    path("tenant/<int:tenant_id>", views.tenant_detail, name = "tenant_detail"),

    # urls related damages crud
    path('damages/', views.damages, name = "damages"),
    path("damage/<int:damage_id>", views.damage_detail, name = "damage_detail"),
]