from django.shortcuts import render, HttpResponse

# Create your views here.

def post_index(request):
    return HttpResponse('<b> Burası Anasayfa</b>')


def post_detail(request):
    return HttpResponse('<b> Burası Detay</b>')


def post_create(request):
    return HttpResponse('<b> Burası Create</b>')


def post_update(request):
    return HttpResponse('<b> Burası Update</b>')


def post_delete(request):
    return HttpResponse('<b> Burası Delete</b>')
