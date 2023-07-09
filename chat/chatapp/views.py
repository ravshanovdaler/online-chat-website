from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Messages
from .forms import MessageForm,MessageToAdminForm
from django.shortcuts import redirect

def login_required_view(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return function(request, *args, **kwargs)
    return wrapper

@login_required_view
def chat(request):
    messages = Messages.objects.all()
    form = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            instance = form.save(commit=False) 
            instance.save()
    context = {'messages': messages , 'form': form}
    return render(request, 'chat.html', context)
def home(request):
    return render(request, 'home.html')
def contact(request):
    form = MessageToAdminForm()
    if request.method == "POST":
        form = MessageToAdminForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'contact.html', context)