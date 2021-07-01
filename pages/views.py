from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from listings.models import Listing,Vehicle_type

# Create your views here.




def index(request):
    listings=Listing.objects.all().order_by('-create_date').filter(is_published=True)[:6]
    vehicle_types=Vehicle_type.objects.all()
    context={
        'vehicle_types':vehicle_types,
        'listings':listings
    }
    return render(request,'pages/index.html',context)

def calculateDistance(pickup_,destination_):
    geolocator = Nominatim(user_agent="rent_service", timeout=30)
    pickup = geolocator.geocode(pickup_)
    destination = geolocator.geocode(destination_)
    if pickup and destination:
        p_lat = pickup.latitude
        p_lon = pickup.longitude
        pointA=(p_lat,p_lon)

        d_lat=destination.latitude
        d_lon=destination.longitude
        pointB=(d_lat,d_lon)

        distance=round(geodesic(pointA,pointB).km,2)

        return pickup, destination, distance
    else:
        return False



def pricing(distance,days):
    per_km=10
    per_day=2000
    if days == '' :
        price = distance * per_km
    else:
        price = int(days) * per_day
    price=round(price)
    return price

def demo(request):
    pickup_ = request.GET['pickup']
    destination_ = request.GET['destination']
    days=request.GET['days']
    try:
        pickup,destination,distance=calculateDistance(pickup_, destination_)
        price = pricing(distance,days)

        context = {

            'destination': destination,
            'pickup': pickup,
            'distance': distance,
            'price': price,
        }
    except:
        warning = 'There is no location like that'
        context = {
            'warning': warning
        }

    return render(request,'pages/gemo.html',context)

def about(request):
    ip = request.META.get("REMOTE_ADDR")
    context={
        ip:ip
    }

    print('my clint ip-----',ip)
    return render(request,'pages/about.html')