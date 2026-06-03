from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

# Create your views here.

# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# @api_view(['GET'])
# def home(request):

#     return Response({
#         "message":"ATS API Running"
#     })

from django.shortcuts import render, redirect
from django.contrib.auth.models import User


def register_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("/login/")

    return render(
        request,
        "accounts/register.html"
    )

def login_page(request):

    if request.method == "POST":

        username = request.POST.get(
            "username"
        )

        password = request.POST.get(
            "password"
        )

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                "dashboard"
            )

        return render(
            request,
            "accounts/login.html",
            {
                "error":
                "Invalid Username or Password"
            }
        )

    return render(
        request,
        "accounts/login.html"
    )
    
def logout_page(request):

    logout(request)

    return redirect(
        "login"
    )