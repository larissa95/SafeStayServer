__author__ = 'larissa'
import django
import urllib
import datetime
import crime.views as crime_views
import hotel.views as hotel_views
import urllib2
import json
import crime.models as crime_models
import hotel.models as hotel_models


def generate_crimes():
    #delete all existing crimes from Database
    crime_views.delete_all_crimes()
    #Crime.objects.filter(latitude=2006.0)
    #just 9000 data points => because of heroku db
    url = 'http://sanfrancisco.crimespotting.org/crime-data?format=json&count=9000&dstart=2011-04-20'
    content = urllib2.urlopen(url)
    data = json.loads(content.read().decode("utf-8"))
    for crime in data['features']:
        c = crime_models.Crime(longitude = crime['geometry']['coordinates'][0], latitude = crime['geometry']['coordinates'][1], type = crime['properties']['crime_type'], datetime = crime['properties']['date_time'])
        c.save()


def generate_hotels():
    hotel_views.delete_all_hotels()
    #check hotels out on future dates
    check_in = str((datetime.datetime.today()+ datetime.timedelta(days=19)).date())
    check_out = str((datetime.datetime.now() + datetime.timedelta(days=20)).date())
    #default value is 20
    number_of_results='1000'
    #set show false out auf true => just save all hotels that are theoretically available
    url = 'http://api.sandbox.amadeus.com/v1.2/hotels/search-box?south_west_corner=37.707739,-122.503003&north_east_corner=37.808171,-122.404098&check_in='+check_in+'&check_out='+check_out+'&show_sold_out=True&number_of_results='+number_of_results+'&apikey=' + get_amadeus_apikey()
    content = urllib2.urlopen(url)
    data = json.loads(content.read().decode("utf-8"))
    for hotel in data['results']:
         h = hotel_models.Hotel(name = hotel['property_name'],
                                longitude = hotel['location']['longitude'],
                                latitude = hotel['location']['latitude'],
                                phone_number = get_phone_number(hotel['contacts']),
                                url = get_url('%s %s'%(hotel['property_name'],'San Francisco Hotel')))
         h.save()

#get Apikey for Amadeus that is is not visible on gitHub
def get_amadeus_apikey():
    #'r' for reading in an existing file
    #'w' for creating a new file for writing
    #'a' for appending new content to an existing file
    #myfile = open("safestay/apikey_amadeus.txt", "r")
    myfile = open("apikey_amadeus.txt", "r")
    apikey = myfile.read()
    return apikey

def get_phone_number(contacts):
    for dic in contacts:
        if dic['type'] == 'PHONE':
            return dic['detail']
    return 'No phone number provided' #e.g for Nob Hill Hotel is no contact information

def get_url(search_subject):
    #api is deprecated since 2010
    #better use new API Custom Search search (but: API key required)
    #https://developers.google.com/api-client-library/python/start/get_started
    query = urllib.urlencode({'q': search_subject})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urllib.urlopen(url)
    search_results = search_response.read()
    results = json.loads(search_results)
    data = results['responseData']
    if data is None:
        return 'No website available-No data'
    for dic in data['results']:
        short_url = dic['visibleUrl']
        #return the fist url that does not contain wikipedia, yelp, expedia or tripadvisor
        if not ('wikipedia' in short_url or 'yelp' in short_url or 'expedia' in short_url or 'tripadvisor' in short_url):
            return short_url
    return 'No website available'


#important that django models and views are available
django.setup()
#save crimes in database
generate_crimes()
generate_hotels()
