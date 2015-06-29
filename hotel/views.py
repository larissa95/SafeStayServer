from django.shortcuts import render

# Create your views here.
import urllib2
import json
from .models import Hotel
from django.http import HttpResponse
from .serializers import HotelSerializer
from rest_framework.renderers import JSONRenderer


def delete_all_hotels():
    for hotel in Hotel.objects.all():
        hotel.delete()

# @api_view(['GET'])
# def get_hotels(request):
#
#     serializer = HotelSerializer(Hotel.objects.all(), many=True)
#     return JSONResponse(serializer.data)

# do not display sold out hotels
def get_hotels(request, check_in = '2015-06-28', check_out = '2015-07-02', max_rate = '700', number_of_results = '500'):
    url = 'http://api.sandbox.amadeus.com/v1.2/hotels/search-box?south_west_corner=37.707739,-122.503003&north_east_corner=37.808171,-122.404098&max_rate='+max_rate+'&check_in='+check_in+'&check_out='+check_out+'&show_sold_out=False&number_of_results='+number_of_results+'&apikey=' + get_amadeus_apikey()
    content = urllib2.urlopen(url)
    data = json.loads(content.read().decode("utf-8"))
    json_response = []
    for hotel_detail_information in data['results']:
        dic_location = hotel_detail_information['location']
        longitude = str(dic_location['longitude'])
        latitude = str(dic_location['latitude'])
        total_price = hotel_detail_information['total_price']['amount']
        min_daily_rate = hotel_detail_information['min_daily_rate']['amount']
        try:
            hotel = Hotel.objects.filter(latitude=latitude).filter(longitude=longitude).first()
            if hotel is not None:
                json_response.append({'name': str(hotel.name), 'phone_number' : str(hotel.phone_number), 'contact_url': str(hotel.url),
                                    'total_price': str(total_price), 'min_daily_rate': str(min_daily_rate)
                                    })
        except IndexError:
            print ('hotel not in database')
    return JSONResponse(json_response)

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

#get Apikey for Amadeus that is is not visible on gitHub
def get_amadeus_apikey():
    #'r' for reading in an existing file
    #'w' for creating a new file for writing
    #'a' for appending new content to an existing file
    #myfile = open("safestay/apikey_amadeus.txt", "r")
    myfile = open("safestay/apikey_amadeus.txt", "r")
    apikey = myfile.read()
    return apikey


