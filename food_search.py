#!/usr/bin/env python
# import pprint
from googleapiclient.discovery import build

dev_key = "AIzaSyAygzEMLRKF3dj98Yh5Rb1el2Vs0KcJ2Q0"
cx = "008895290161045775949:f2e3gyd_53y"

def main():
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build("customsearch", "v1",
            developerKey=dev_key)

    res = service.cse().list(
      q='bibimbap',
      cx=cx,
      safe="high",
      searchType="image"
    ).execute()
    link1 = res['items'][0]['link']
    link2 = res['items'][1]['link']
    link3 = res['items'][2]['link']
    print(link1, link2, link3)

if __name__ == '__main__':
  main()


# from google.appengine.api import search
# index = search.Index(name='productsearch1')
# geopoint = search.GeoPoint(latitude, longitude)
# fields = [search.TextField(name=docs.Store.STORE_NAME, value=storename),
#              search.TextField(name=docs.Store.STORE_ADDRESS, value=store_address),
#              search.GeoField(name=docs.Store.STORE_LOCATION, value=geopoint)
