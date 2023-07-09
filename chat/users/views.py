from django.shortcuts import render
from .forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from .models import CustomUser
from django.shortcuts import redirect

def login_required_view(function):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return function(request, *args, **kwargs)
    return wrapper

class UserCreationView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
def logoutView(request):
    return render(request, 'logoutpage.html')
@login_required_view
def profileView(request):
    return render(request, 'profile.html')
class ProfileEdit(UpdateView):
    form_class = UserChangeForm
    model = CustomUser
    template_name = 'profileedit.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self):
        return self.request.user