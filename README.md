# Youtube Integration



## Introduction
This project is mainly for interation with youtubeDataAPI. This intract the api for search and then show the video content. I use a html file or you can say a template for showing the searched content. This template interaction is basically same as you 	intract with youtube but with a limited facility.
This shows only four field which are:
Video title, Embed Video and Like and Dislike button.	


## Prerequisites:
You need the following programs properly installed on your computer/system.
```
					Python3.8
					Virtual enviroment
```
To install python3.8 go to:- 
```
				https://www.python.org/download
```
and download the specific version of python. When you are installing python, please make sure to tick the “Set path” option.
To make sure that python is installed or not, type “python --version” in terminal.
To install virtual environment in your system use:
```					
					pip install virtualenv 
						or
					pip3 install virtualenv
```

## Clone the Project

```
cd existing_repo
git remote add origin https://gitlab.com/Vicky_1999/youtube-integration.git
git branch -M main
git push -uf origin main
```

Now you have to install the dependencies or requirement library. So inorder to do that you have to  activate your virtual enviroment and type the following command:
For activate the virtual enviroment use:
```					
					venv_name\Scripts\activate 
			      				or
					source venv_name/bin/activate
```
For install the dependencies use:
```					
					pip install -r requirements.txt
```

## Run the project
To run this project use:
```					
					cd  youtube_integration
					python manage.py runserver
```

## Disclaimer
When you run this you get one error which is  “client_secret.json” is not found.

**Why:**
Because i used my “API key” in order to perform this operation. And my “client_secret.json” file in order to make credentials and absolutly, I didn’t gave these file with this project. 
So inorder to make them you have to follow some basic simple steps.

**Step1:** 
	you have to go to 	https://console.cloud.google.com/
	If you are not sign in then you have to first sign in. 
**Step2:**
	After sign in you found a beautiful page. At the top of the left side you will see 3 bar, click 	on it and 		choose “API and Services”.

**Step3:**
	Now you have to create new project. Give project Name. 
	Now click on “Enable APIS and serives”. Now in the search bar search for youtube Data API.
	Enable it.
**Step4:**
	Now you have to create credentials. At the create credentials, it ask you about the api so you 	have to put the 	“youtube data api v3” and select public data. Click on next and Done.
**Step5:** 
	Now for use this you have to configure the oauthclientid. So for this first you have to go to 	“Oauth consent 		screen” and select “external” and “create”.
	Fill the required details whatever you want with one restriction:
```
	at “Test users” you have to enter your mail id by which you want to access the app. And saved it.
```

**Step6:**
	Now go for again create credentials and click on “Oauth client Ids”.  In Application type, 	select “web 			application”. 

```
	Now  in  “Authorized JavaScript origins” you have to enter:
					http://127.0.0.1:8000
```

```
	In “Authorized redirect Urls” you have to enter:
					http://127.0.0.1:8000/search_youtube
					http://127.0.0.1:8000/get_token
```

and save.
You get your clientID and client secret number. Now there is a download sign to download 	client_secret file. 	Download it and save it in the “ youtube_integration” directory.

Please rename this file as “client_secret.json”.

Now there is another thing to do. You have to copy your "Youtube data API key" and open settings.py file(/youtube_integration/youtubeintegrationembded/settings.py). There, at bottom you have to write:

```
YOUTUBE_DATA_API_KEY = 'Paste Your downloaded API key'
```
and save this file.


_**Now you ready to roll.**_

##Thank you
