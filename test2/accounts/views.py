from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views
from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        return self.success_url
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')