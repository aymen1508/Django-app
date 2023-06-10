from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Item,Category
from .forms import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q


def index(request):
    query=request.GET.get('query','')
    category_id=int(request.GET.get('category_id',0))
    categories=Category.objects.all()
    items=Item.objects.filter(is_sold=False)
    if query:
        items=items.filter(Q(name__icontains=query)| Q(description__icontains=query))
    if category_id:
        items=items.filter(category=category_id)
    return render(request,'item/index.html',{'items':items,'query':query,'categories':categories,'category_id':category_id})

def detail(request,pk):
    item=get_object_or_404(Item,pk=pk)
    other_items=Item.objects.exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{'item':item,'other_items':other_items})

@login_required
def add(request):
    if request.method=='POST':
        form=AddItemForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    else:
        form=AddItemForm()
        return render(request,'item/form.html',{'form':form,'title':'Add'})

@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method=='POST':
        form=EditItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:detail',pk=item.id)
    else:
        form=EditItemForm(instance=item)
        return render(request,'item/form.html',{'form':form,'title':'Edit'})