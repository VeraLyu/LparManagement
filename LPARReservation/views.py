from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from LPARReservation.models import LPAR
import time

def home(request):
    is_login = False
    user_name = ""
    if request.user.is_authenticated():
        is_login = True
        user_name = request.user.email

    lpars = LPAR.objects.filter()
    return render(request, 'home.html', {'lpars': lpars, 'is_login': is_login, \
            'user_name': user_name})

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
    return render(request, 'home.html', {'lpars': lpars, 'is_login': is_login, \
            'user_name': user_name})

@login_required
def cancel(request):
    is_login = True
    user_name = request.user.email
    lpar_id = request.REQUEST.get('lparid')
    if lpar_id:
        lpar = LPAR.objects.get(id=lpar_id)
    if lpar and lpar.available == False:
        lpar.available = True
        lpar.rsv_person = None
        lpar.save()
    lpars = LPAR.objects.filter()
    return render(request, 'home.html', {'lpars': lpars, 'is_login': is_login, \
            'user_name': user_name})
