from django.shortcuts import render, redirect
from django.http import HttpResponse
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer  

# Create your views here.
def home(request):
	return render(request,'index.html') 
def checker(request):
	ls=[]
	val1= request.POST['message']
	sid_obj = SentimentIntensityAnalyzer()  
	sentiment_dict = sid_obj.polarity_scores(val1) 
	string = str(sentiment_dict['neg']*100) + "% Negative"
	ls.append(string)
	string1 = str(sentiment_dict['neu']*100) + "% Neutral"
	ls.append(string1)
	string2 = str(sentiment_dict['pos']*100) +"% Positive"
	ls.append(string2)
	if sentiment_dict['compound'] >= 0.05 :
		return render(request,'result.html', {'result':'Positive'})
	elif sentiment_dict['compound'] <= - 0.05 :
		return render(request,'result.html', {'result':'Negative'})
	else:
		return render(request,'result.html', {'result':'Neutral'})
def some(request):
	return redirect('home')   
  
