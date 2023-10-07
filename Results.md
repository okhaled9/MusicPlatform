## first import models

from artists.models import Artist  
from albums.models import Album

## Create some artists

Artist.objects.create(stage_name="Adele", social_link="https://www.instagram.com/adele/")  
Artist.objects.create(stage_name="Travis Scott", social_link="https://www.instagram.com/travisscott/")  
Artist.objects.create(stage_name="El Waili", social_link="https://www.instagram.com/elwaiillii/")

## list down all artists  

Artist.objects.all()

## list down all artists sorted by name 

Artist.objects.all().order_by('stage_name')  

## list down all artists whose name starts with a 

Artist.objects.all().filter(stage_name__startswith='a')

## in 2 different ways, create some albums and assign them to any artists (hint: use objects manager and use the related object reference)

elwaili = Artist.objects.get(stage_name="El Waili")  
travis = Artist.objects.get(stage_name="Travis Scott")

import pytz  
import datetime  
timezone = pytz.utc  
date1 = datetime.datetime(2022, 6, 30, 12, 30, 45, tzinfo=timezone)  
date2 = datetime.datetime(2018, 6, 30, 12, 30, 45, tzinfo=timezone)  
Album.objects.create(artist = elwaili, name="Tayarat w Sayarat", release_datetime=date1, cost=10)  
travis.album_set.create(name="AstroWorld", release_datetime=date2, cost=12)  

## get the latest released album  

Album.objects.all().order_by('-release_datetime')[:1]

## get all albums released before today  

Album.objects.all().filter(release_datetime__lt=datetime.datetime.now().date())

## get all albums released today or before but not after today  

Album.objects.all().filter(release_datetime__lte=datetime.datetime.now().date())

## count the total number of albums (hint: count in an optimized manner)  

Album.objects.count()

## in 2 different ways, for each artist, list down all of his/her albums (hint: use objects manager and use the related object reference)  

for artist in Artist.objects.all().iterator():
    print (artist.stage_name,": ")
    for album in artist.album_set.all().iterator():
        print(album.name)
    print("\n")

for a in Artist.objects.all().iterator():
    print(a.stage_name,': ')
    for al in Album.objects.all().filter(artist=a):
        print(al.name)
    print('\n')

## list down all albums ordered by cost then by name (cost has the higher priority)  

Album.objects.all().order_by('cost', 'name')