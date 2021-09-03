# This is a Readme File for Youtubeintegrations with embedding the youtube videos project

first a brief introduction about This Project. 

#Introduction:
	This project is mainly for interation with youtubeDataAPI. This intract the api for search and then show the video content.
	I use a html file or you can say a template for showing the searched content. This template interaction is basically same as you 
	intract with youtube but with a limited facility.
	This shows only four field which are:
	
		title: Which is the Video title extract from the youtubeAPI
		Video: Which is the embedding link of the youtube video
		like:  For like the video
		dislike: For dislike the video
	
So lets get started first I have to talk about the requirements like libraris or etc.

#requirements:
	You must have
		
		Python 3.6	install via:-   https://www.python.org/downloads/
		django 3.2.6	install via:	pip install django
	

Now when you are ready to roll so you have to download this project by clicking the "Download sign". You will have tons of options like .zip, .tar etc. I always prefer .zip files so you have to download .zip file.

Now after downloading the zip file you have to extract the files in your perfer location. 



#Run the project:

	To run this project you have to open your terminal, go to that directory where you extract this project(by cd foldername), then run a particular command:
	
		python manage.py runserver
	
	when you run this command(if you successfully extract all the files then it should run fine) it gives you a url at which this project is running. you have to go to that URL. there is a search bar in which you have to enter your search.
	

#Functionality:
	It shows the title, and youtube video it self as a picture in picture mode
	About the functionality, If you enter any text in the search bar you get the top 10 videos. 
	If you didn't enter any searchbar, it shows the random videos.
	
	For like you have to just click on the like and if liked is successful then you must see that like is now converted into liked.

	For dislike you have to just click on the dislike and if dislike is successful then you must see that dislike is now converted into disliked
