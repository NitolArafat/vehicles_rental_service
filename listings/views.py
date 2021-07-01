from json import JSONEncoder

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Listing,Vehicle_type,OrderBooking
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from datetime import date, datetime, timedelta
from django.core.mail import send_mail
from django.core.paginator import Paginator



def index(request):
    listings = Listing.objects.order_by('-create_date').filter(is_published=True)
    paginator = Paginator(listings, 6) # Show 3 contacts per page.
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    vehicle_types = Vehicle_type.objects.all
    context={
        'listings':page_listings,
        'vehicle_types':vehicle_types,
    }
    return render(request,'listings/listings.html',context)

def listing(request,listing_id=None):
    listing=get_object_or_404(Listing,id=listing_id)
    pickup_ = request.session.get('pickup_')
    destination_ = request.session.get('destination_')
    pickup_date = request.session.get('pickup_date')
    days = request.session.get('days')

    pickup, destination, distance = calculateDistance(pickup_, destination_)
    if days:
        return_date = calculate_day(pickup_date, days)
    else:
        return_date=None
    context={
        'listing':listing,
        'pickup':pickup,
        'destination':destination,
        'distance':distance,
        'pickup_date':pickup_date,
        'return_date':return_date,
        'days':days,

    }
    return render(request,'listings/listing.html',context)

def listing_type(request,type_id):

    listings = Listing.objects.filter(vehicle_type_id=type_id , is_published=True)
    paginator = Paginator(listings, 6) # Show 3 contacts per page.
    page = request.GET.get('page')
    page_listings = paginator.get_page(page)
    vehicle_types = Vehicle_type.objects.all
    context={
        'listings':page_listings,
        'vehicle_types':vehicle_types,
    }
    return render(request, 'listings/listings.html', context)

def search(request):
    all_vehicle_types = Vehicle_type.objects.all
    if 'pickup_point' in request.GET:
        pickup_ = request.GET['pickup_point']
        request.session['pickup_'] = pickup_

    if 'destination' in request.GET:
        destination_ = request.GET['destination']
        request.session['destination_'] = destination_

    if 'pickup_date' in request.GET:
        pickup_date = request.GET['pickup_date']
        request.session['pickup_date'] = pickup_date

    if 'days' in request.GET:
        days = request.GET['days']
        request.session['days'] = days
        if days:
            print('------------days',days)
            return_date = calculate_day(pickup_date, days)
        else:
            return_date = None

    if 'vehicle_type' in request.GET:
        vehicle_type_value = request.GET['vehicle_type']
        listings = Listing.objects.filter(vehicle_type_id=vehicle_type_value).filter(is_published=True)
    else:
        vehicle_type_value = None
        listings = Listing.objects.all

    if pickup_ and destination_:
        pickup,destination,distance=calculateDistance(pickup_, destination_)
        distance = round(distance)
    else:
        warning= 'There is no location like that'
        destination = None
        pickup = None
        distance = 0

    context = {
        'destination': destination,
        'pickup': pickup,
        'distance': distance,
        'pickup_date': pickup_date,
        'return_date': return_date,
        'days': days,
        'all_vehicle_types': all_vehicle_types,
        'vehicle_type_value' : vehicle_type_value,
        'listings' : listings,
    }
    return render(request,'listings/search.html',context)

def calculate_day(pickup_date, days):
    days=int(days)
    pickup_date = datetime.strptime(pickup_date, "%m/%d/%Y %I:%M %p")
    return_date = pickup_date + \
                            timedelta(days=days)
    return return_date
def calculateDistance(pickup_,destination_):
    geolocator = Nominatim(user_agent="rent_service", timeout=20)
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

def place_order(request):
    if request.method=='POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        username = request.POST['username']
        user_id = request.POST['user_id']
        pickup_point = request.POST['pickup_point']
        destination = request.POST['destination']
        pickup_date = request.POST['pickup_date']
        return_date = request.POST['return_date']
        distance = request.POST['distance']
        days = request.POST['days']
        price = request.POST['price']
        phone = request.POST['phone']
        message = request.POST['message']
        contact_person_name = request.POST['contact_person_name']
        contact_person_email = request.POST['contact_person_email']


        # if request.user.is_authencated:
        #     user_id = request.user.id
        #     has_request = OrderBooking.objects.all().filter(listing_id=listing_id,user_id=user_id)
        #     if has_request:
        #         price('You have already made an request for this vehicle')
        #         return redirect('/listings/' + listing_id)

    placeOrder=OrderBooking(listing_id=listing_id,listing=listing,username=username,
                            user_id=user_id, pickup_point=pickup_point,
                            destination=destination,pickup_date=pickup_date,
                            return_date=return_date,distance=distance,days=days,
                            price=price,phone=phone,message=message)
    placeOrder.save()
    send_mail(
        'Nitol Express - rental service',
        ' Hello Mr. '+ contact_person_name +
        ''', There has been a request for ''' + listing + '''. sign to 
        admin panel for more information''',
        'mdaaanitol@gmail.com',
        [contact_person_email],
        fail_silently=False,
    )
    messages.success(request, 'Your request has been send')
    return redirect('/listings/'+ listing_id)