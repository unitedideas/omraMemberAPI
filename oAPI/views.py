from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from .models import MemberData
from .serializers import MemberDataSerializer


class MemberDataView(viewsets.ModelViewSet):
    queryset = MemberData.objects.all()
    serializer_class = MemberDataSerializer
    lookup_fields = 'memberNumber'
    filter_backends = (filters.SearchFilter,)  # DjangoFilterBackend
    # filter_fields = ('firstName', 'active')
    search_fields = ('memberNumber', 'lastName', 'active')


# Create your views here.
@staff_member_required
def home(request):
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass
    return render(request, "oAPI/home.html")
