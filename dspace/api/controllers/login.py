from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth.models import User
import bcrypt
import json

try:
    from types import SimpleNamespace as Namespace
except ImportError:
    from argparse import Namespace

def auth_user(request):
  if request.method == 'POST':
    data = json.loads(request.body, object_hook=lambda d: Namespace(**d))
    user = User.objects.filter(email=data.email).get()
    print(user.password)

    try:
      hashed = bcrypt.hashpw(data.password.encode('utf8'), bcrypt.gensalt())
      
      if not checkPassword(user.password.encode('utf8'), hashed):
        return HttpResponse(status=401)
      else:
        return HttpResponse(status=200)

    except KeyError:
      return HttpResponseServerError('error')

def checkPassword(password, hashed):
  return bcrypt.checkpw(password, hashed)
