from django.contrib.admin.options import StackedInline
from users.models import Message
from django.shortcuts import redirect, render
from django.db import transaction
from django.contrib.auth import login, authenticate, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q


import os


User = get_user_model()


def register_user(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname", None)
        username = request.POST.get("username", None)
        password1 = request.POST.get("password1", None)
        password2 = request.POST.get("password2", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        details = request.POST.get("organization-details", None)
        projections = request.POST.get("financial-projections", None)
        charter = request.FILES.get("organization-charter", None)

        with transaction.atomic():
            if not username:
                messages.add_message(request, messages.WARNING, "You haven't provided username")
                return redirect(reverse("register"))
            
            if password1 and password2 and password1.strip() != password2.strip():
                messages.add_message(request, messages.WARNING, "Passwords doesn't match")
                return redirect(reverse("register"))
            
            if User.objects.filter(username=username.strip()).exists():
                messages.add_message(request, messages.ERROR, "Username already exists. Please, try with another one.")
                return redirect(reverse("register"))
            
            user = User.objects.create_user(username, password1.strip())
            user.fullname = fullname
            user.email = email
            user.phone = phone
            user.organization_details = details
            user.financial_projections = projections
            user.organization_charter = charter
            user.save()

            messages.add_message(request, messages.SUCCESS, "You have successfully registered")
            return redirect(reverse("login"))

    return render(request, "users/register.html")


def login_user(request):
    if request.user.is_authenticated:
        return redirect(reverse("profile"))

    if request.POST:
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        if not username or not password:
            messages.add_message(request, messages.WARNING, "Please, provide both username and password")
            return redirect(reverse("login"))
        
        user = authenticate(username=username.strip(), password=password)
        if not user:
            messages.add_message(request, messages.ERROR, "User doesn't exist. Please, try with other credentials")
            return redirect(reverse("login"))
        
        login(request, user)
        messages.add_message(request, messages.SUCCESS, "You have successfully logged in!")
        return redirect(reverse("profile"))


    return render(request, "users/login.html")


def logout_user(request):
    logout(request)
    return redirect(reverse("login"))


@login_required(login_url="/user/login/")
def profile(request):
    superadmin = User.objects.filter(is_superuser=True).first()
    
    if request.method == "POST":
        attachment = request.FILES.get("attachment", None)
        text = request.POST.get("text", None)

        message = Message(sender=request.user, reciever=superadmin)

        if text:
            message.text = text
        
        if attachment:
            message.attachment = attachment
        
        message.save()
    

    chat_messages = Message.objects.filter(Q(sender=request.user, reciever=superadmin) | Q(sender=superadmin, reciever=request.user)).order_by("created_date")
    received_messages = Message.objects.filter(seen=False, reciever=request.user, sender=superadmin)
    to_superadmin_chats = User.objects.filter(is_superuser=False, is_active=True)

    context = {
        "chat_messages": chat_messages,
        "unread_messages_count": received_messages.count(),
        "to_superadmin_chats": to_superadmin_chats
    }
    received_messages.update(seen=True)
    
    return render(request, "users/profile.html", context)


@login_required(login_url="/user/login/")
def settings(request):
    if request.GET.get("action", None) == "delete-charter":
        user = User.objects.get(username=request.user.username)
        try:
            os.unlink(os.path.join(os.getcwd(), user.organization_charter.url))
        except Exception as e:
            print(e)
        user.organization_charter = None
        user.save()
        return redirect(reverse("settings"))
    
    elif request.method == "POST":
        fullname = request.POST.get("fullname", None)
        username = request.POST.get("username", None)
        password1 = request.POST.get("password1", None)
        password2 = request.POST.get("password2", None)
        email = request.POST.get("email", None)
        phone = request.POST.get("phone", None)
        details = request.POST.get("organization-details", None)
        projections = request.POST.get("financial-projections", None)
        charter = request.FILES.get("organization-charter", None)

        with transaction.atomic():
            if not username:
                messages.add_message(request, messages.WARNING, "You haven't provided username")
                return redirect(reverse("register"))
            
            if request.user.username != username and User.objects.filter(username=username.strip()).exists():
                messages.add_message(request, messages.ERROR, "Username already exists. Please, try with another one.")
                return redirect(reverse("register"))
            
            user = User.objects.filter(id=request.user.id).first()
            user.username = username
            user.fullname = fullname
            user.email = email
            user.phone = phone
            user.organization_details = details
            user.financial_projections = projections
            user.organization_charter = charter
            user.save()

            messages.add_message(request, messages.SUCCESS, "You have updated your settings")
            return redirect(reverse("settings"))
    
    superadmin = User.objects.filter(is_superuser=True).first()
    context = {
        "unread_messages_count": Message.objects.filter(seen=False, reciever=request.user, sender=superadmin).count()
    }
    return render(request, "users/settings.html", context)


@login_required(login_url="/user/login/")
def admin_profile(request, _id):
    to_superadmin_chats = User.objects.filter(is_superuser=False, is_active=True)

    user = User.objects.filter(id=_id)
    if user.exists():
        user = user.first()
    else:
        return redirect(reverse("profile"))

    if request.method == "POST":
        attachment = request.FILES.get("attachment", None)
        text = request.POST.get("text", None)

        message = Message(sender=request.user, reciever=user)

        if text:
            message.text = text
        
        if attachment:
            message.attachment = attachment
        
        message.save()
    
    chat_messages = Message.objects.filter(Q(sender=request.user, reciever=user) | Q(sender=user, reciever=request.user)).order_by("created_date")
    received_messages = Message.objects.filter(seen=False, reciever=request.user, sender=user)
    received_messages.update(seen=True)

    context = {
        "chat_messages": chat_messages,
        "to_superadmin_chats": to_superadmin_chats
    }
    return render(request, "users/admin_profile.html", context)