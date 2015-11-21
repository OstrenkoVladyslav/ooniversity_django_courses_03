from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def contact(request):
    return render(request, 'contact.html')

def student_list(request):
    return render(request, 'student_list.html')

def student_detail(request):
    return render(request, 'student_detail.html')


urlpatterns = patterns('',
    url(r'^contact/$', contact, name='contact'),
    url(r'^student_list/$', student_list, name='student_list'),
    url(r'^student_detail/$', student_detail, name='student_detail'),
    url(r'^$', hello, name='home'),
    url(r'^admin/', include(admin.site.urls)),
)