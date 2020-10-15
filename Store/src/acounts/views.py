from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login ,authenticate
from . models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import UserForm,ProfileForm
from django.contrib.auth.decorators import login_required

@login_required
def my_profile(request,username):
    main_profile=get_object_or_404(User,username=username)
    profile=get_object_or_404(Profile,id=main_profile.id)
    context={'main_profile':main_profile ,'profile':profile}
    return render(request,'registration/my_profile.html',context)

@login_required
def signup(request):
    if request.method=='POST' :
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('passwodr')
            user=authenticate(username='uesrname',password='password')
            login(request,user)
            return redirect('/products/')
    else:
        form=UserCreationForm()
        context={'form':form}
        return render(request,'registration/signup.html',context)
@login_required
def logout(request):
    logout(request)
    return redirect('/products/')

@login_required
def edit_profile(request):
    if request.method=='POST' :
        form=UserForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/products/')
    else :
        form=UserForm(instance=request.user)
        context={'form':form }
        return render(request,'registration/edit_profile.html',context)

@login_required
def edit_my_profile(request ,username):
    main_profile=get_object_or_404(User,username=username)
    usr=get_object_or_404(Profile,user=main_profile.id)
    if request.method=='POST':
        form2=ProfileForm(request.POST,instance=usr)
        if form2.is_valid():
            form2.save(commit=False)
            request.user=request.user
            form2.save()
            return redirect('/products/')
    else:
         
        form2=ProfileForm(instance=usr)
        context={'form2':form2,'main_profile':main_profile}
        return render(request,'registration/edit_my_profile.html',context)

@login_required
def changepassword(request):
    if request.method =='POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration/my_profile.html')
    else :
        form=PasswordChangeForm(request.user)
    context={'form':form}
    return render(request,'registration/password_change_form.html',context)
