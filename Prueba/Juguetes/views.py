from django.shortcuts import render,redirect
from Juguetes.models import Juguetes
from  Juguetes.forms import RegistroJuguete
# Create your views here.

def Index(request):
    return render(request,'Index/index.html')

def Juguetess(request):
    juguete = Juguetes.objects.all()
    data = {'Juguete':juguete}
    return render(request,'Listado/ListadoJuguetes.html',data)

def RegistroJuguetesView(request):
    form = RegistroJuguete()
    if request.method == 'POST':
        form = RegistroJuguete(request.POST)
        if form.is_valid():
            form.save()
        return Juguetess(request)    
    data = {'form': form}
    return render(request, 'Registro/Registro.html',data)
    
def Eliminar(request,id):
    juguete = Juguetes.objects.get(id = id)
    juguete.delete()
    return redirect('/juguetes')

def Actualizar(request,id):
    juguete = Juguetes.objects.get(id = id)
    form = RegistroJuguete(instance=juguete)
    if request.method == 'POST':
        form = RegistroJuguete(request.POST, instance=juguete)
        if form.is_valid():
            form.save()
        return Juguetess(request)    
    data = {'form':form}
    return render(request,'Registro/Registro.html',data)    
