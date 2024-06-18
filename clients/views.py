from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import include, reverse

from clients.models import Client


def index(request):
    current_user = request.user
    if current_user.is_authenticated:
        user_id = current_user.id
        clients = Client.objects.filter(responsible_id=user_id)
        if clients:
            context = {
                'title': 'Clients',
                'clients': clients,
            }
            return render(request, 'clients/index.html', context)
        else:
            context = {
                'title': 'Clients',
            }
            return render(request, 'clients/index.html', context)
    else:
        return HttpResponseRedirect(reverse('users:login'))


def update_status(request, account_number):
    current_user = request.user
    if current_user.is_authenticated:
        if request.method == 'POST':
            input_status = request.POST.get('status')
            client = Client.objects.get(account_number=account_number)
            if client:
                current_status = client.status
                if current_status != input_status:
                    client.status = input_status
                    current_status = input_status
                    client.save()
        context = {
            'title': 'Clients',
            'clients': Client.objects.filter(responsible_id=current_user.id),
            'account_number': account_number,
            'current_status': current_status
        }
        return render(request, 'clients/index.html', context)
    else:
        return HttpResponseRedirect(reverse('users:login'))
