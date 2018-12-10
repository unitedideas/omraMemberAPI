from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.
@staff_member_required
def home(request):
    if request.method == "GET":
        print("GET Request")
    if request.method == "POST":
        print("POST Request")
    return render(request, 'oAPI/home.html')
