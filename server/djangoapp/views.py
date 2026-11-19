import json
import logging

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CarMake, CarModel
from .populate import initiate
from .restapis import analyze_review_sentiments, get_request, post_review

logger = logging.getLogger(__name__)


def _json_body(request):
    """Return the request body as a dict, or None if it is not valid JSON."""
    try:
        return json.loads(request.body)
    except ValueError:
        return None


@csrf_exempt
def login_user(request):
    """POST /djangoapp/login  {"userName": "...", "password": "..."}"""
    data = _json_body(request)
    if not data or 'userName' not in data or 'password' not in data:
        return JsonResponse({"status": 400, "message": "userName and password are required"}, status=400)
    username = data['userName']
    user = authenticate(username=username, password=data['password'])
    response = {"userName": username}
    if user is not None:
        login(request, user)
        response["status"] = "Authenticated"
    return JsonResponse(response)


def logout_request(request):
    """GET /djangoapp/logout"""
    logout(request)
    return JsonResponse({"userName": ""})


@csrf_exempt
def registration(request):
    """POST /djangoapp/register"""
    data = _json_body(request)
    required = ('userName', 'password', 'firstName', 'lastName', 'email')
    if not data or any(key not in data for key in required):
        return JsonResponse({"status": 400, "message": "Missing registration fields"}, status=400)
    username = data['userName']
    if User.objects.filter(username=username).exists():
        return JsonResponse({"userName": username, "error": "Already Registered"})
    user = User.objects.create_user(
        username=username,
        first_name=data['firstName'],
        last_name=data['lastName'],
        password=data['password'],
        email=data['email'],
    )
    login(request, user)
    return JsonResponse({"userName": username, "status": "Authenticated"})


def get_cars(request):
    """GET /djangoapp/get_cars"""
    if CarMake.objects.count() == 0:
        initiate()
    car_models = CarModel.objects.select_related('car_make')
    cars = [{"CarModel": car.name, "CarMake": car.car_make.name} for car in car_models]
    return JsonResponse({"CarModels": cars})


def get_dealerships(request, state="All"):
    """GET /djangoapp/get_dealers  or  /djangoapp/get_dealers/<state>"""
    endpoint = "/fetchDealers" if state == "All" else "/fetchDealers/" + state
    dealerships = get_request(endpoint)
    if dealerships is None:
        return JsonResponse({"status": 502, "message": "Dealer service unavailable"}, status=502)
    return JsonResponse({"status": 200, "dealers": dealerships})


def get_dealer_details(request, dealer_id):
    """GET /djangoapp/dealer/<id>"""
    dealership = get_request("/fetchDealer/" + str(dealer_id))
    if dealership is None:
        return JsonResponse({"status": 502, "message": "Dealer service unavailable"}, status=502)
    return JsonResponse({"status": 200, "dealer": dealership})


def get_dealer_reviews(request, dealer_id):
    """GET /djangoapp/reviews/dealer/<id>  (each review gets a 'sentiment' field)"""
    reviews = get_request("/fetchReviews/dealer/" + str(dealer_id))
    if reviews is None:
        return JsonResponse({"status": 502, "message": "Review service unavailable"}, status=502)
    for review_detail in reviews:
        response = analyze_review_sentiments(review_detail['review'])
        review_detail['sentiment'] = response.get('sentiment', 'neutral')
    return JsonResponse({"status": 200, "reviews": reviews})


@csrf_exempt
def add_review(request):
    """POST /djangoapp/add_review (logged-in users only)"""
    if request.user.is_anonymous:
        return JsonResponse({"status": 403, "message": "Unauthorized"}, status=403)
    data = _json_body(request)
    if data is None:
        return JsonResponse({"status": 400, "message": "Invalid JSON"}, status=400)
    response = post_review(data)
    if response is None:
        return JsonResponse({"status": 401, "message": "Error in posting review"}, status=401)
    return JsonResponse({"status": 200})
