from django.shortcuts import render

# Create your views here.

from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('accounts:login')

class UserRegisterView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    
    def get_success_url(self):
        return reverse_lazy('accounts:home')
    

from .models import Avatar
from .forms import CustomUserForm, AvatarForm
from django.shortcuts import render
from django.views import View

class UserChangeView(LoginRequiredMixin, View):
    def get(self, request):
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        user_form = CustomUserForm (instance=request.user) 
        avatar_form = AvatarForm (instance=avatar)
        return render(request, 'accounts/change-user.html', {
            'user_form': user_form,
            'avatar_form': avatar_form,
        })

    def post(self, request):
        avatar, _ = Avatar.objects.get_or_create(user=request.user) 
        user_form = CustomUserForm (request. POST, instance=request.user) 
        avatar_form = AvatarForm(request. POST, request.FILES, instance=avatar) 
        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save() 
            avatar_form.save()
            return redirect('accounts:edit')
        return render(request, 'accounts/change-user.html', {
            'user_form': user_form,
            'avatar_form': avatar_form,
        })


class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = 'accounts/upload_avatar.html'
    success_url = reverse_lazy('accounts:upload_avatar')

    def get_object(self, queryset=None):
        avatar, _ = Avatar.objects.get_or_create(user=self.request.user)
        return avatar
    
    