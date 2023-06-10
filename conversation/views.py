from django.shortcuts import render,redirect,get_object_or_404
from .models import Conversation
from .forms import ConversationMessageForm
from item.models import Item
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request,item_pk):
    item=get_object_or_404(Item,pk=item_pk)
    if item.created_by==request.user:
        redirect('dashboard:index')
    conversation=Conversation.objects.filter(members__in=[request.user]).filter(item=item)
    if conversation.exists():
        return redirect('conversation:detail',conversation.first().id)

    if request.method=='POST':
        form=ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation=Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            return redirect('item:detail',pk=item_pk)
    form=ConversationMessageForm()
    return render(request,'conversation/new.html',{'form':form})

@login_required
def inbox(request):
    conversations=Conversation.objects.filter(members__in=[request.user]).order_by('-updated_at')
    latest_messages=[]
    for i in conversations:
        latest_messages.append(i.messages.last())
    conversations_and_latest_messages=[(i,j) for i in conversations for j in latest_messages]
    return render(request,'conversation/inbox.html',{'conversations':conversations})

@login_required
def detail(request,conversation_pk):
    conversation=get_object_or_404(Conversation,pk=conversation_pk)
    if request.method=='POST':
        form=ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by=request.user
            conversation_message.save()
            return redirect('conversation:detail',conversation.id)
    else:
        form=ConversationMessageForm()
        return render(request,'conversation/detail.html',{'form':form,'conversation':conversation})
