from django.shortcuts import render
#from django.http import HttpResponse
import  random

def about(request):
    return render(request,'generator/about.html')
def home(request):
    return render(request,'generator/home.html')
def password(request) :
    
    characters = list('abcdefghijklmnopqrstuvwxyz') 
    generated_password = ''
    
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
             characters.extend(list('ABCEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
             characters.extend(list('+-*/,.#$%&/()=?¡@!°'))
    if request.GET.get('numbers'):
             characters.extend(list('1234567890'))         
             print("hello")
             print("hello1")
           
    for x in range(length):
        generated_password += random.choice(characters)
           
          
    return render(request, 'generator/password.html',{'password': generated_password})


def password(request) :
    
    characters = list('abcdefghijklmnopqrstuvwxyz') 
    generated_password = ''
    
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
             characters.extend(list('ABCEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
             characters.extend(list('+-*/,.#$%&/()=?¡@!°'))
    if request.GET.get('numbers'):
             characters.extend(list('1234567890'))         
             print("hello")
             print("hello1")
    
           
    for x in range(length):
        generated_password += random.choice(characters)
           
          
    return render(request, 'generator/password.html',{'password': generated_password})
