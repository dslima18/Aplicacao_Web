from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Create your views here.

def logout_view(request):
    """Faz logout do usuário"""
    logout(request)
    return redirect(reverse('learning_logs:index'))