from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def central(request):
    return render(request,'central.html')

def lugari(request):
    return render(request,'lugari.html')

def ikolomani(request):
    return render(request,'ikolomani.html')

def butere(request):
    return render(request,'butere.html')

def khwisero(request):
    return render(request,'khwisero.html')

def likuyani(request):
    return render(request,'likuyani.html')

def malava(request):
    return render(request,'malava.html')

def mumiaseast(request):
    return render( request,'mumiaseast.html')

def mumiaswest(request):
    return render( request,'mumiaswest.html')

def mumiaseast(request):
    return render( request,'mumiaseast.html')

def navakholo(request):
    return render( request,'navakholo.html')

def shinyalu(request):
    return render( request,'shinyalu.html')

def contact(request):
    return render(request,'contact.html' )
    


        
    



