from django.shortcuts import render, HttpResponse
from django.template import Context
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import viewsets, filters
from .models import Rider
from .serializers import RiderSerializer


class RiderView(viewsets.ModelViewSet):
    queryset = Rider.objects.all()
    serializer_class = RiderSerializer
    lookup_fields = 'memberNumber'
    filter_backends = (filters.SearchFilter,)  # DjangoFilterBackend
    # filter_fields = ('firstName', 'active')
    search_fields = ('memberNumber', 'lastName', 'active')


# Create your views here.
@staff_member_required
def member(request):
    print(request.method)
    if request.method == "GET":
        content = {"request": "GET"}
        return render(request, "oAPI/member.html", content)
    if request.method == "POST":
        content = {"request": "POST"}
        return render(request, "oAPI/member.html", content)
    if request.method == "PATCH":
        content = {"request": "PATCH"}
        return render(request, "oAPI/member.html", content)
    if request.method == "DELETE":
        content = {"request": "DELETE"}
        return render(request, "oAPI/member.html", content)


def memberform(request):
    if request.method == "GET":
        content = "GET"
        return HttpResponse(content)
    if request.method == "POST":
        content = "POST"
        return HttpResponse(content)
    if request.method == "PATCH":
        content = "PATCH"
        return HttpResponse(content)
    if request.method == "DELETE":
        content = "DELETE"
        return HttpResponse(content)
