from django.urls import path

from clients.views import index, update_status

# from clients.views import clients, basket_add, basket_remove

app_name = 'clients'

urlpatterns = [
    path('', index, name='index'),
    path('update_status/<int:account_number>', update_status, name='update_status'),
]
