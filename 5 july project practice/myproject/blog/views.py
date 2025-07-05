# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm # For handling login forms
from django.contrib.auth import login, logout, authenticate # For login/logout/authentication
from django.contrib import messages # For displaying feedback messages

# Assuming you already have these from previous discussions
# from .models import Post # If you have a Post model

def home(request):
    # Logic for your home page
    return render(request, 'home.html')

def create_post(request):
    if request.method == 'POST':
        # Handle post creation logic here
        # For example:
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # Post.objects.create(title=title, content=content)
        messages.success(request, "Post created successfully!") # Example message
        return redirect('home') # Redirect after post creation
    return render(request, 'create_post.html')

# --- FIX FOR LOGIN ---
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {username}!")
                return redirect('home')  # Redirect to your home page after successful login
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Optional: Logout view
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('home') # Redirect to home or login page after logout

# Assuming your register_view is similar to this (or you're using UserCreationForm)
def register_view(request):
    # This is a placeholder; you'd typically use UserCreationForm here
    # from django.contrib.auth.forms import UserCreationForm
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user) # Automatically log in the user after registration
    #         messages.success(request, "Registration successful!")
    #         return redirect('home')
    #     else:
    #         messages.error(request, "Registration failed. Please correct the errors.")
    # else:
    #     form = UserCreationForm()
    # return render(request, 'register.html', {'form': form})
    return render(request, 'register.html') # Placeholder for now