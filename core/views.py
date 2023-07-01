from django.shortcuts import render
from django.http import HttpResponse


def test_request(request):
    return HttpResponse('1212')
