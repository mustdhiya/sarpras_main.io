from django.shortcuts import render, redirect
from .forms import RuangPercobaanForm
from .models import RuangPercobaan


def index(request):
    if request.method == 'POST':
        form = RuangPercobaanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_ruang')  
    else:
        form = RuangPercobaanForm()
    return render(request, 'room/index.html', {
        "head": 'table jadwal model',
        'form': form
        }
    )  

def daftar_ruang(request):
    ruang_list = RuangPercobaan.objects.all()
    return render(request, 'room/index.html', {'ruang_list': ruang_list})
