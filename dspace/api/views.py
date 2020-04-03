from django.shortcuts import render
from api.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index(request):
  return render(request, 'api/index.html')

@login_required
def special(request):
  return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
  logout(request)
  return HttpResponse("Success")

def register(request):
  registered = False
  if request.method == 'POST':
    user_form = UserForm(data=request.POST)
    if user_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()
      registered = True
    else:
      print(user_form.errors)
  else:
    return HttpResponse('Fail')
    # user_form = UserForm()
  
  return HttpResponse({'user_form': user_form, 'registered': registered})

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
      else:
        return HttpResponse('Your account was inactive.')
    else:
      print("Someone trie to login and failed.")
      print("They used username: {} and password: {}".format(username, password))
      return HttpResponse("Invalid login details given")
  else:
    return render(request, 'api/login.html', {})