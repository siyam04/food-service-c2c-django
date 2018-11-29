from django.contrib.auth.models import User
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
# Same App importing
from .forms import SignUpForm, ProfileForm
from .models import Profile
# Posts App importing
# from posts.models import Post


def sign_up(request):
    """Complex Signup View"""
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['repassword']
        user = User.objects.filter(username=username)
        if password == confirm_password:
            User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            # If User is Authenticated, then allow Login and go to Profile Create
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile-create')

    template = 'food_users_profile/sign_up.html'
    return render(request, template)


def sign_in(request):
    """Sign In view"""
    if request.method == "POST":
        username, password = request.POST['username'], request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
    return redirect('home')


def profile_create(request):
    """Creating profile is Mandatory"""
    name = request.user.first_name + ' ' + request.user.last_name
    initial_data = {
        "user_name": name,
        "email": request.user.email
    }

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user

            # Save to Database
            profile.save()
            return redirect('profile-detail', id=profile.id)

    context = {
        'form': ProfileForm(initial=initial_data),
        }

    template = 'food_users_profile/profile_create.html'
    return render(request, template, context)


@login_required(login_url='login')
def profile_detail(request, id=None):
    """Showing Profile Details"""
    try:
        profile = get_object_or_404(Profile, id=id)
        context = {
            'profile': profile,
            }
        template = 'food_users_profile/profile_detail.html'
        return render(request, template, context)

    except:
        try:
            profile = Profile.objects.get(user=request.user)
            context = {
                'profile': profile,
            }
            template = 'food_users_profile/profile_detail.html'
            return render(request, template, context)

        except:
            return redirect('profile-create')


@login_required(login_url='login')
def profile_edit(request):
    """Editing Profile"""
    profile = get_object_or_404(Profile, user=request.user)

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')

    context = {
        'form': form,
        }

    template = 'food_users_profile/profile_edit.html'
    return render(request, template, context)
