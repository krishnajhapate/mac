from django.urls import path
from . import views



urlpatterns =[
    path('',views.index ,name= "ShopHome"),
    path('about/',views.about , name ="About"),
    path('contact/',views.contact , name = 'contact'),
    path('tracker/',views.tracker , name = 'tracker'),
    path('search/',views.search , name = 'search'),
    path('checkout/',views.checkout , name = 'checkout'),
    path('view/<int:myid>',views.view , name = 'view'),
    path('handlerequest/',views.handlerequest , name = 'handlerequest'),
]