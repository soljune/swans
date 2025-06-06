from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import SwimWorkoutForm,PoolForm
from .models import SwimWorkout,Pool
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Invalid form input')
    return render(request, 'pool/register.html', {'form': form})

def loginUser(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # checked whether the user exists in the DB => Users table
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist!")
            return render(request, "pool/login.html")
            
        # authenticate the user and check whether the credentials are ok
        user = authenticate(request, username=username, password=password) 
        if user is not None: 
            login(request, user)
            messages.success(request, f"Welcome home {user.username}!")
            # Get the next parameter from the request, default to 'home' if not present
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, "Wrong Credentials")
    
    return render(request, "pool/login.html")

def logoutUser(request):
    if request.method == "POST":
        logout(request)
        messages.info(request, "See you soon!")
        return redirect('login')
    return render(request, "pool/logout_form.html")

@login_required
def workout_list(request):
    workouts = SwimWorkout.objects.filter(user=request.user).order_by('-date')
    return render(request, 'pool/workout_list.html', {'workouts': workouts})

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = SwimWorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = SwimWorkoutForm()
    return render(request, 'pool/add workout.html', {'form': form})

def home(request):
    return render(request, 'pool/home.html')

@login_required
def add_pool(request):
    if request.method == 'POST':
        form = PoolForm(request.POST)
        if form.is_valid():
            pool = form.save(commit=False)
            pool.user = request.user  # Store the User object
            pool.save()
            return redirect('pool_list')
    else:
        form = PoolForm()
    return render(request, 'pool/add_pool.html', {'form': form})
@login_required
def pool_list(request):
    pools = Pool.objects.filter(user=request.user)
    return render(request, 'pool/pool_list.html', {'pools': pools})

@login_required
def workout_detail(request, pk):
    workout = get_object_or_404(SwimWorkout, pk=pk, user=request.user)
    return render(request, 'pool/workout_detail.html', {'workout': workout})

@login_required
def workout_update(request, pk):
    workout = get_object_or_404(SwimWorkout, pk=pk, user=request.user)
    if request.method == 'POST':
        form = SwimWorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            form.save()
            return redirect('workout_detail', pk=pk)
    else:
        form = SwimWorkoutForm(instance=workout)
    return render(request, 'pool/workout_form.html', {'form': form})

@login_required
def workout_delete(request, pk):
    workout = get_object_or_404(SwimWorkout, pk=pk, user=request.user)
    if request.method == 'POST':
        workout.delete()
        return redirect('workout_list')
    return render(request, 'pool/workout_confirm_delete.html', {'workout': workout})

@login_required
def pool_detail(request, pk):
    pool = get_object_or_404(Pool, pk=pk)
    return render(request, 'pool/pool_detail.html', {'pool': pool})

@login_required
def pool_update(request, pk):
    pool = get_object_or_404(Pool, pk=pk)
    if request.method == 'POST':
        form = PoolForm(request.POST, instance=pool)
        if form.is_valid():
            form.save()
            return redirect('pool_detail', pk=pk)
    else:
        form = PoolForm(instance=pool)
    return render(request, 'pool/add_pool.html', {'form': form})

@login_required
def delete(request, pk):
    pool = Pool.objects.get( pk=pk)
    pool.delete()
    return redirect('pool_list')




