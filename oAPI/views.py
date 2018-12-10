from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@staff_member_required
def home(request):
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass
    return render(request, "oAPI/home.html")
