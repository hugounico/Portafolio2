from django.shortcuts import render

# Create your views here.
def home(request):                                  #un request es la solicitud que hace el usuariod esde al pag web
    return render(request, 'core/home.html')        #render lo usamos para renderizar los html