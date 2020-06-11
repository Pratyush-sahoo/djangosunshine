#this is the views.py file
from django.shortcuts import render

# Create your views here.
def home(request):
	import json
	import requests

	api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20004&distance=25&API_KEY=636A7664-397E-49EE-A073-56E393CAB78C")

	try:
		api = json.loads(api_request.content)

	except Exception as e:
	    api = "Error..."

	if api[0]['Category']['Name'] == "Good" :
		category_description ==	"0 - 50       Good,Air quality is considerd satisfactory."
		 category_color = ""

    elif api[0]['Category']['Name'] == " Moderate":
        category_description = "51 - 100  air quality is acceptable"
        category_color = ""
    elif api[0]['Category']['Name'] == "unhealthy sensetive groups": 
        category_description = "101 - 150    Unhealthy for Sensitive Groups (USG) people having lung disese will get affected"
         category_color = ""
    elif api[0]['Category']['Name'] == "UNHEALTHY" :
        category_description = "151 - 200    Unhealthy everyone may start to exprience health effects"
         category_color = ""
    elif api[0]['Category']['Name'] == "VERYUNHEALTHY": 
        category_description = "201 - 300    Very Unhealthy everyone may exprience more serious health effects"
         category_color = ""
    elif api[0]['Category']['Name'] == "HAZARDOUS":   	
        category_description = "301 - 500 the entire population is going to be affected" category_color = ""


       	    	

	#api.openweathermap.org/data/2.5/weather?q={city name}&appid={2fc3a54c9d316c151a54476b26ba50d1}
	return render(request, 'home.html', {'api':api,'category_description':category_description})

def about(request):
	return render(request, 'about.html', {})