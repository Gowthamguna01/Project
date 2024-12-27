from django.shortcuts import render, redirect


from happ.forms import BusForm
from happ.models import Bus
from django.db.models import Sum,Avg

# Create your views here.
def std(request):
    if request.method == "POST":
        form=BusForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form=BusForm()
    return render(request,"index.html",{'std':std})

def show(request):
    academy= Bus.objects.all()
    for boys in academy:
        boys.total=boys.stamil + boys.senglish + boys.smaths + boys.sscience + boys.ssocial
        boys.average=boys.total/5
    return render(request,"show.html",{'academy':academy})


def edit(request, id):
    boys= Bus.objects.get(id=id)
    return render(request,"edit.html",{'boys':boys})


def update(request, id):
    fan= Bus.objects.get(id=id)
    form=BusForm(request.POST, instance=fan)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request,"edit.html",{'fan':fan})


def destroy(request, id):
    trash=Bus.objects.get(id=id)
    trash.delete()
    return redirect("/show")




