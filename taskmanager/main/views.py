from django.shortcuts import render
from django.http import HttpResponse


def index(reqest):
    return render(reqest, 'main/index.html')


def about(reqest):
    return render(reqest, 'main/about.html')