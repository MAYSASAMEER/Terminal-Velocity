from django.http import JsonResponse
from firebase_admin import auth, credentials, initialize_app
import firebase_admin
from django.conf import settings
import json

def initialize_firebase():
    try:
        return firebase_admin.get_app()
    except ValueError:
        try:
            # Get credentials from settings
            creds_dict = settings.FIREBASE_ADMIN_CREDENTIALS
            
            
            # Clean up the private key - replace escaped newlines with actual newlines
            if 'private_key' in creds_dict:
                creds_dict['private_key'] = creds_dict['private_key'].replace('\\n', '\n')
            
            cred = credentials.Certificate(creds_dict)
            return initialize_app(cred)
        except Exception as e:
            print(f"Failed to initialize Firebase: {str(e)}")
            return None

# Initialize Firebase when the module loads
firebase_app = initialize_firebase()

class FirebaseAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.firebase_initialized = firebase_app is not None

    def __call__(self, request):
        # Skip authentication for non-API routes and specific API endpoints
        if not request.path.startswith('/api/') or \
           request.path.startswith('/api/auth/signup/') or \
           request.path.startswith('/api/auth/login/') or \
           request.path.startswith('/api/auth/check-auth/') or \
           request.path.startswith('/static/') or \
           request.path == '/':
            return self.get_response(request)

        if not self.firebase_initialized:
            return JsonResponse({
                'error': 'Firebase authentication is not properly configured'
            }, status=503)

        try:
            session_id = request.session.get('user_id')
            if not session_id:
                return JsonResponse({'error': 'Authentication required'}, status=401)

            # Verify the user exists in Firebase
            try:
                user = auth.get_user(session_id)
                request.user_id = user.uid
                request.user_email = user.email
            except:
                request.session.flush()
                return JsonResponse({'error': 'Invalid session'}, status=401)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=401)

        return self.get_response(request) 