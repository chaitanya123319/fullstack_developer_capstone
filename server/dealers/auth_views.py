
import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def register_user(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST method required'}, status=405)

    try:
        data = json.loads(request.body)

        username = data.get('username', '').strip()
        password = data.get('password', '')
        first_name = data.get('first_name', '').strip()
        last_name = data.get('last_name', '').strip()
        email = data.get('email', '').strip()

        if not all([username, password, first_name, last_name, email]):
            return JsonResponse(
                {'error': 'All fields are required'},
                status=400
            )

        if User.objects.filter(username=username).exists():
            return JsonResponse(
                {'error': 'Username already exists'},
                status=400
            )

        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )

        return JsonResponse({
            'message': 'User registered successfully',
            'username': user.username
        }, status=201)

    except (json.JSONDecodeError, TypeError):
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


@csrf_exempt
def login_user(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST method required'}, status=405)

    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return JsonResponse({
                'message': 'Login successful',
                'username': user.username
            })

        return JsonResponse(
            {'error': 'Invalid username or password'},
            status=401
        )

    except (json.JSONDecodeError, TypeError):
        return JsonResponse({'error': 'Invalid JSON'}, status=400)


@csrf_exempt
def logout_user(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST method required'}, status=405)

    if not request.user.is_authenticated:
        return JsonResponse(
            {'error': 'User is not logged in'},
            status=401
        )

    logout(request)

    return JsonResponse({'message': 'Logout successful'})
