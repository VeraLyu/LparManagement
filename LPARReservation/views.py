from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from LPARReservation.models import LPAR
from LPARReservation.models import Server
import time, thread

def home(request):
    is_login = False
    user_name = ""
    if request.user.is_authenticated():
        is_login = True
        user_name = request.user.email

    lpars = LPAR.objects.filter()
    for lpar in lpars:
        t = str(lpar.reservation_time)[:19]
        t1 = time.time() - time.mktime(time.strptime(str(t),'%Y-%m-%d %H:%M:%S')) - 3600 * 8
        if (t1 >= 3600*4 and not lpar.available):
            lpar.available = True
            lpar.last_rsv_person = lpar.rsv_person
            lpar.rsv_person = None
            lpar.save()
    lpars = LPAR.objects.filter()
    servers = Server.objects.filter()
    return render(request, 'home.html', {'lpars': lpars, 'is_login': is_login, \
            'user_name': user_name, 'servers': servers})

@login_required
def reserve(request):
    is_login = True
    user_name = request.user.email
    lpar_id = request.REQUEST.get('lparid')
    if lpar_id:
        lpar = LPAR.objects.get(id=lpar_id)
    if lpar and lpar.available == True:
        lpar.available = False
        lpar.rsv_person = request.user.email
        lpar.reservation_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        lpar.save()
    lpars = LPAR.objects.filter()
    return redirect('/')

@login_required
def rsv(request):
    is_login = True
    user_name = request.user.email
    server_id = request.REQUEST.get('serverid')
    if server_id:
        server = Server.objects.get(id=server_id)
    if server and server.available == True:
        server.available = False
        server.rsv_person = request.user.email
        server.save()
    servers = Server.objects.filter()
    lpars = LPAR.objects.filter()
    return render(request, 'home.html', {'lpars': lpars, 'is_login': is_login, \
            'user_name': user_name, 'servers': servers, 'active': 'label2'})

@login_required
def cancel(request):
    is_login = True
    user_name = request.user.email
    lpar_id = request.REQUEST.get('lparid')
    if lpar_id:
        lpar = LPAR.objects.get(id=lpar_id)
    if lpar and lpar.available == False and lpar.rsv_person == user_name:
        lpar.available = True
        lpar.last_rsv_person = lpar.rsv_person
        lpar.rsv_person = None
        lpar.save()
    lpars = LPAR.objects.filter()
    return redirect('/')

@login_required
def ccl(request):
    is_login = True
    user_name = request.user.email
    server_id = request.REQUEST.get('serverid')
    if server_id:
        server = Server.objects.get(id=server_id)
    if server and server.available == False and server.rsv_person == user_name:
        server.available = True
        server.rsv_person = None
        server.save()
    lpars = LPAR.objects.filter()
    servers = Server.objects.filter()
    return render(request, 'home.html', {'lpars': lpars, 'is_login': is_login, \
            'user_name': user_name, 'servers': servers, 'active': 'label2'})
