
import urllib2
import json
import urllib

#https://farm{farm-id}.staticflickr.com/{server-id}/{id}_{secret}.jpg
#download 25k img

jj=0
for ii in range(1,25):
	inp = urllib2.urlopen('https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=76711e1fc2a9195b21fe63994864ed1c&tags=fire&content_type=1&per_page=1000&page='+str(ii)+'&format=json&nojsoncallback=1')
	data = json.load(inp)
	for elm in data['photos']['photo']:
		while True:
			try:
				jj=jj+1
				urllib.urlretrieve("https://farm"+str(elm['farm'])+".staticflickr.com/"+str(elm['server'])+"/"+str(elm['id'])+"_"+str(elm['secret'])+".jpg", "fire_"+str(jj)+".jpg")
			except IOError:
				print "not able to download image"



