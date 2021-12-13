from django.shortcuts import render


def index(request):
    """display the home page of pure beurre app with template index.html"""
    return render(request, "PurBeurre/index.html")


def legal_notice(request):
    """display the home page of pure beurre app with template legal_notice.html"""
    return render(request, "PurBeurre/legal_notice.html")
