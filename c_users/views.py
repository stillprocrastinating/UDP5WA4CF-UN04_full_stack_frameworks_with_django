from allauth.account.models import EmailAddress
from .forms import EmailForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse


def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            return redirect('account_login')

    return render(request, 'c_users/profile.html', {'profile': profile})


@login_required
def profile_edit_view(request):
    form = ProfileForm(instance=request.user.profile)

    if request.method == 'POST':
        form = ProfileForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if form.is_valid():
            form.save()
            return redirect('profile')

    if request.path == reverse('profile-signup'):
        signup = True
    else:
        signup = False

    context = {
        'form': form,
        'signup': signup,
    }

    return render(request, 'c_users/profile_edit.html', context)


@login_required
def profile_settings_view(request):
    return render(request, 'c_users/profile_settings.html')


@login_required
def profile_email_change(request):

    if request.htmx:
        form = EmailForm(instance=request.user)
        return render(request, 'partials/email_form.html', {'form': form})

    if request.method == 'POST':
        form = EmailForm(request.POST, instance=request.user)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(email=email).exclude(
                    id=request.user.id).exists():
                messages.warning(request, f'{email} is already in use.')
                return redirect('profile-settings')
            form.save()
            # signal updates email address and unverifies
            email_address = EmailAddress.objects.get(
                user=request.user, email=request.user.email
            )
            email_address.send_confirmation(request)
            messages.success(request, f'{email} verification has been sent.')
            return redirect('profile-settings')
        else:
            messages.warning(request, 'Form not valid')
            return redirect('profile-settings')

    return redirect('home')


@login_required
def profile_email_verify(request):
    email_address = EmailAddress.objects.get(
        user=request.user, email=request.user.email
    )
    email_address.send_confirmation(request)
    messages.success(request, f'{email_address} verification has been sent.')
    return redirect('profile-settings')


@login_required
def profile_delete_view(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted')
        return redirect('home')

    return render(request, 'c_users/profile_delete.html')
