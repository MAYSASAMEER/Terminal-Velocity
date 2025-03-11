from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

def health_check(request):
    return HttpResponse('Server is running')

@csrf_exempt
def serve_frontend(request, page='login'):
    # Map routes to template names
    templates = {
        'login': 'final_login.html',
        'signup': 'final_signup.html',
        'dashboard': 'final_dashboard.html',
        'landing': 'final_landing.html'
    }
    template_name = templates.get(page, 'final_login.html')
    return render(request, template_name)

urlpatterns = [
    # Frontend routes
    path('', lambda r: redirect('/login/'), name='root'),
    path('login/', serve_frontend, {'page': 'login'}, name='login'),
    path('signup/', serve_frontend, {'page': 'signup'}, name='signup'),
    path('dashboard/', serve_frontend, {'page': 'dashboard'}, name='dashboard'),
    path('landing/', serve_frontend, {'page': 'landing'}, name='landing'),
    
    # API routes
    path('api/auth/', include('authentication.urls')),
    path('api/health/', health_check, name='health-check'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 