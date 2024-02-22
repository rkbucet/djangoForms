from django.shortcuts import render, redirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

def home(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'app/home.html', {'form': fm, 'stud':stud})

def deleteData(request, id):
    data = User.objects.get(id=id)
    data.delete()
    return redirect('home')

def updateData(request, id):
    if request.method == 'POST':
        data = User.objects.get(id=id)
        form = StudentRegistration(request.POST, instance=data)
        form.save()
        return redirect('home')
    else:
        data = User.objects.get(id=id)
        form = StudentRegistration(instance=data)
        return render(request, 'app/update.html', {'form':form})
        
