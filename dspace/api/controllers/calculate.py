from django.http import HttpResponse
from api.utils import distanceBetween
from decimal import Decimal

def distance(request, lat1, lon1, lat2, lon2):
  point1 = [Decimal(lat1), Decimal(lon1)]
  point2 = [Decimal(lat2), Decimal(lon2)]
  return HttpResponse(distanceBetween(point1, point2))
