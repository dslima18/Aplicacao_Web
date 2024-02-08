from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def logout_view(request):
    """Faz logout do usuário"""
    logout(request)
    return redirect(reverse('learning_logs:index'))

def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':
        # Exibe o formulário de cadastro em branco
        form = UserCreationForm()
    else:
        # Processa o formulário preenchido
        form = UserCreationForm(data=request.POST)
    if form.is_valid():
        new_user = form.save()
        # Faz o login do usuário e o redireciona para a página inicial
        authenticated_user = authenticate(username=new_user.username, password = request.POST['password1'])
        login(request, authenticated_user)
        return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request, 'users/register.html', context)
