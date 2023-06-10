from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.views import Item

@login_required
def index(request):
    items=Item.objects.filter(created_by=request.user).order_by('-created_at')
    return render(request, 'dashboard/index.html', {'items': items})