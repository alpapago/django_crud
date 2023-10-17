from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 회원가입
            user = form.save()
            # 로그인 후 리다이렉트
            auth_login(request, user)
            return redirect("shop:index")
    else:
        form = CustomUserCreationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)

    # redirect 는 요청을 보내는 거기 때문에, 뱅글뱅글 돌면서 순환할 것.
    # return redirect("accounts:signup")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # auth_login 이 세션을 만드는 역할을 한다.
            auth_login(request, form.get_user())
            return redirect("shop:index")
    else:
        form = AuthenticationForm()

    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("shop:index")


def profile(request, user_pk):
    return render(request, "accounts/profile.html")
