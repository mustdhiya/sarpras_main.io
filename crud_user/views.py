from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def user_list(request):
    users = User.objects.all()
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    return render(request, 'crud_user/user_list.html', {'users': users, 'form': form})

def user_update(request, pk):
    user = User.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    return render(request, 'crud_user/user_form.html', {'form': form})

def user_delete(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'crud_user/user_confirm_delete.html', {'user': user})
