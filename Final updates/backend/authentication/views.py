from django.http import JsonResponse
from django.shortcuts import render, redirect
from firebase_admin import auth
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

def landing_page(request):
    return render(request, 'authentication/final_landing.html')

def login_page(request):
    if request.session.get('user_id'):
        return redirect('dashboard')
    return render(request, 'authentication/final_login.html')

def signup_page(request):
    if request.session.get('user_id'):
        return redirect('dashboard')
    return render(request, 'authentication/final_signup.html')

def dashboard_page(request):
    if not request.session.get('user_id'):
        return redirect('login')
    return render(request, 'authentication/final_dashboard.html')

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def signup(request):
    if request.method == "OPTIONS":
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    try:
        data = json.loads(request.body)
        id_token = data.get('idToken')
        
        # Verify the Firebase token
        decoded_token = auth.verify_id_token(id_token)
        user_id = decoded_token['uid']
        
        # Set session
        request.session['user_id'] = user_id
        
        return JsonResponse({
            'message': 'User registered successfully',
            'user_id': user_id
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def login(request):
    if request.method == "OPTIONS":
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    try:
        data = json.loads(request.body)
        id_token = data.get('idToken')
        
        # Verify the Firebase token
        decoded_token = auth.verify_id_token(id_token)
        user_id = decoded_token['uid']
        
        # Set session
        request.session['user_id'] = user_id
        
        return JsonResponse({
            'message': 'Login successful',
            'user_id': user_id
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=401)

@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def logout(request):
    if request.method == "OPTIONS":
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    try:
        # Clear session
        request.session.flush()
        return JsonResponse({'message': 'Logout successful'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@csrf_exempt
@require_http_methods(["GET", "OPTIONS"])
def check_auth(request):
    if request.method == "OPTIONS":
        response = JsonResponse({})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    user_id = request.session.get('user_id')
    if user_id:
        try:
            # Verify user still exists in Firebase
            user = auth.get_user(user_id)
            return JsonResponse({
                'authenticated': True,
                'user_id': user_id,
                'email': user.email
            })
        except:
            request.session.flush()
    
    return JsonResponse({'authenticated': False}) 