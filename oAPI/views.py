from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework import viewsets, permissions, mixins
from .models import MemberData
from .serialozers import MemberDataSerializer

class MemberDataView(viewsets.ModelViewSet):
    queryset = MemberData.objects.all()
    serializer_class = MemberDataSerializer
    lookup_fields = ('firstName', 'lastName', 'memberNumber', 'expirationDate')
    # permission_classes = (permissions.IsAuthenticated,)

# Create your views here.
@staff_member_required
def home(request):
    if request.method == "GET":
        pass
    if request.method == "POST":
        pass
    return render(request, "oAPI/home.html")
