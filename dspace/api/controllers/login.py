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

    try:
      hashed = bcrypt.hashpw(data.password.encode('utf8'), bcrypt.gensalt())
      response_data = {}
      if not checkPassword(user.password.encode('utf8'), hashed):
        response_data = [{"status": '401'}]
        return HttpResponse(json.dumps(response_data), content_type="application/json")
      else:
        response_data = [{"status": '200', "user": {
          'id': user.id,
          'username': user.username,
          'email': user.email,
          }
        }]
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    except KeyError:
      return HttpResponseServerError('error')

def checkPassword(password, hashed):
  return bcrypt.checkpw(password, hashed)
