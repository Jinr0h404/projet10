from django.shortcuts import render, redirect
from User.forms import SignupForm, SigninForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "User/index_user.html")


@login_required()
def account(request):
    return render(request, "User/account.html")


def signup(request):
    """we generate an instance of our form and send it form via the context. If post request and form data correct
    user is register and logged and redirect on user page"""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = SignupForm()
    return render(request, "User/signup.html", context={"form": form})


def signin(request):
    """we generate an instance of our form and send it form via the context. If post request and form data correct
    user is logged and redirect on user page else error message is display"""
    form = SigninForm()
    message = ""
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"], password=form.cleaned_data["password"]
            )
            if user is not None:
                login(request, user)
                obj = str(request.GET)
                if "next" in obj:
                    next_url = request.GET.get("next")
                    return redirect(next_url)
                else:
                    return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                message = "Identifiants incorrects"
    return render(
        request, "User/signin.html", context={"form": form, "message": message}
    )


def logout_user(request):
    """User is disconnect and redirect on the home page"""
    logout(request)
    return redirect("index")
