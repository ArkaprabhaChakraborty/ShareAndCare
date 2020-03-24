from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required


def home_page_view(request):
    return render(request, 'account/home.html')
