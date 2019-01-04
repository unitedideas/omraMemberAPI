from django.shortcuts import render, HttpResponse
from django import forms
from django.contrib.admin.views.decorators import staff_member_required
# from django_filters.rest_framework import DjangoFilterBackend
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
    if request.method == "GET":
        # content = {"GET": "GET"}
        return render(request, "oAPI/member.html")
    if request.method == "POST":
        content = "POST"
        return render(content)
    if request.method == "PATCH":
        content = "PATCH"
        return render(content)
    if request.method == "DELETE":
        content = "DELETE"
        return HttpResponse(content)


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
