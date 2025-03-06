from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import TrainerRegistration  # Ensure this model exists

def trainer_registration(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('lms:trainer_registration')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('lms:trainer_registration')

            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=user_name,
                    email=email,
                    password=password1,
                    is_staff=True  # Adjust based on your needs
                )
                user.save()

                trainer_registration = TrainerRegistration.objects.create(
                    user=user,
                    status="Active"  # Modify based on your logic
                )
                trainer_registration.save()

                return redirect('lms:login')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('lms:trainer_registration')

    return render(request, 'lms/trainer_registration.html')

def learn_as_trainer(request):
    user = request.user
    trainer_registration = TrainerRegistration.objects.filter(user=user, status="Active").first()

    if trainer_registration:
        return render(request, 'lms/learn_as_trainer.html')
    else:
        messages.error(request, "You are not registered as a trainer.")
        return redirect('/')
