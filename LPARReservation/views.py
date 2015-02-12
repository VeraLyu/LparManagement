from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from LPARReservation.models import LPAR

def home(request):
    lpars = LPAR.objects.filter()
    return render(request, 'home.html', {'lpars': lpars})
