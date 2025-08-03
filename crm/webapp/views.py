from django.shortcuts import redirect, render

from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from . models import Record

from django.contrib import messages


def home(request): 
    return render(request, "webapp/index.html")


# - Register/Create a user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("my-login")
    context = {"form": form}
    return render(request, "webapp/register.html", context)


# - Login a user
def my_login(request):
    form2 = LoginForm()
    if request.method == "POST":
        form2 = LoginForm(request, data=request.POST)
        if form2.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have logged in successfully")
                return redirect("dashboard")
    context = {"form2": form2}
    return render(request, "webapp/my-login.html", context)


# - Dashboard
@login_required(login_url="my-login")
def dashboard(request):
    
    my_records = Record.objects.all()
    
    context = {"records": my_records}
    
    return render(request, "webapp/dashboard.html", context)


# - Logout a user
def user_logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out successfully")
    return redirect("my-login")







# - Create a new record
@login_required(login_url="my-login")
def create_record(request):
    
    form3 = CreateRecordForm()
    if request.method == "POST":
        form3 = CreateRecordForm(request.POST)
        if form3.is_valid():
            form3.save()
            messages.success(request, 'Record created successfully')
            return redirect("dashboard")
        
    context = {"form3": form3}
    
    
    return render(request, "webapp/create-record.html", context)


# - Update a record
@login_required(login_url="my-login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form4 = UpdateRecordForm(instance=record)
    if request.method == "POST":
        form4 = UpdateRecordForm(request.POST, instance=record)
        if form4.is_valid():
            form4.save()
            messages.success(request, 'Record updated successfully')
            return redirect("dashboard")
    context = {"form4": form4}
    return render(request, "webapp/update-record.html", context)



# - Read / View a singular record
@login_required(login_url="my-login")
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)
    context = {"record": all_records}
    return render(request, "webapp/view-record.html", context)


# - Delete a record
@login_required(login_url="my-login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, 'Record deleted successfully')
    return redirect("dashboard")
