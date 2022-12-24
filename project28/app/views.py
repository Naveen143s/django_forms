from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def insert_data(request):
    forms=NormalForm()
    d={'forms':forms}
    if request.method=='POST':
        from_data=NormalForm(request.POST)
        if from_data.is_valid():
            n=from_data.cleaned_data['name']
            a=from_data.cleaned_data['age']
            e=from_data.cleaned_data['email']
            d=from_data.cleaned_data['address']
            g=from_data.cleaned_data['gender']
            d1={'N':n,'A':a,'E':e,'D':d,'G':g}
            return render(request,'retrive.html',d1)

    return render(request,'insert_data.html',d)
