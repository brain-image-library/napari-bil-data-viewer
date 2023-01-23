import fsspec, requests
import json 
import os
from bs4 import BeautifulSoup
from skimage import io
from napari_bil_data_viewer.dataset_info import get_datasets

location_of_dir = os.path.dirname(os.path.abspath(__file__))
print(location_of_dir)

dataset_info = get_datasets()

dataset_imginfo = {}
for dset in dataset_info:

	bilData = dataset_info[dset]['url']
	ext = 'tif'
	

	def getFilesHttp(url: str,ext: str) -> list:
		def listFD(url, ext=''):
			page = requests.get(url,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}).text
			# print(page)
			soup = BeautifulSoup(page, 'html.parser')
			return [url + '/' + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
		
		files = []
		for file in listFD(url, ext):
			files.append(file)
			
		return files

	def getImage(fileObj):
		with fileObj as f:
			print('Reading {} \n'.format(f))
			return io.imread(f)


	data = []
	for ii in bilData:
		images = sorted(getFilesHttp(ii, ext))
		images = [fsspec.open(x,'rb') for x in images]
		data.append(images)


	dataset_imginfo[dset] = {}
	for idx,ii in enumerate(data):
		sampleImage = getImage(ii[0])
		dataset_imginfo[dset][idx] = (sampleImage.shape,str(sampleImage.dtype))

out_file = os.path.join(location_of_dir,'dataset_imginfo.json')
#Write JSON to disk
with open(out_file, "w") as outfile:
    json.dump(dataset_imginfo, outfile, indent=2)
    
