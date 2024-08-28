# Uncomment the required imports before adding the code

from django.shortcuts import render
# from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import logout
# from django.contrib import messages
# from datetime import datetime

from .models import CarMake, CarModel

from .restapis import get_request, analyze_review_sentiments, post_review

from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
import logging
import json
from django.views.decorators.csrf import csrf_exempt
#from django.views.generic.base import TemplateView
from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

def aboutus(request):
    return render(request,"About.html")

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    data={"userName":""}
    return JsonResponse(data)

# Create a `registration` view to handle sign up request
# @csrf_exempt
def registration(request):
    data = json.loads(request.body)
    username = data['userName']
    if(username == ""):
        data = {"username":username, "status": 1,"message": "failed: username cannot be empty"}
        return JsonResponse(data)
    password = data['password']
    if(len(password)<5):
        data = {"username":username, "status": 1,"message": "failed: Password too short! At least 5 characters"}
        return JsonResponse(data)
    firstname = data['firstName']
    lastname = data['lastName']
    email=data['email']
    try:
        User.objects.get(username=username)
        data = {"username":username, "status": 1,"message": "failed: username exists"}
        return JsonResponse(data)
    except:
        logger.debug("%s is registered", username)
        user = User.objects.create_user(username,email,password,first_name=firstname,last_name=lastname)
        login(request,user)
        data = {"username":username, "status":0}
        return JsonResponse(data)

def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count)
    if(count == 0):
        initiate()
    carModels = CarModel.objects.select_related("make")
    cars = []
    for model in carModels:
        print("appending",model)
        cars.append({"Model":model.name,"Make":model.make.name})
    return JsonResponse({"CarModels":cars})

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request, state='All'):
    endpoint = ""
    if(state == "All"):
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/" + state
    dealerships = get_request(endpoint)
    return JsonResponse({"status": 200, "dealers": dealerships})

# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request,dealer_id):
    endpoint = "/fetchReviews/dealer/"+str(dealer_id)
    reviews = get_request(endpoint)
    for review in reviews:
        data = review["review"]
        sentiment = analyze_review_sentiments(data)
        review["sentiment"] = sentiment['sentiment']
    return JsonResponse({"status":200, "review_details":reviews})

# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    if(dealer_id):
        endpoint = "/fetchDealer/"+str(dealer_id)
        dealership = get_request(endpoint)
        print()
        return JsonResponse({"status": 200, "dealer": dealership})
    return JsonResponse({"status":400, "message":"badrequest"})
# Create a `add_review` view to submit a review
def add_review(request):
    if(request.user.is_authenticated):
        data = json.loads(request.body)
        try:
            response = post_review(data)
            return JsonResponse({"status":200})
        except:
            return JsonResponse({"status":401, "message":"Failed to post reviews"})
    return JsonResponse({"status":403,"message":"Log in before you comment!"})