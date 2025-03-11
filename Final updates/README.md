# Terminal Velocity

Terminal Velocity is an interactive web application designed to help students learn Linux commands through an engaging game-based interface.

## Prerequisites

- Python 3.9 or higher
- Git
- A modern web browser (Chrome, Firefox, Safari)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Terminal-Velocity/Final\ updates
```

2. Set up the Python virtual environment:
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. Install Python dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory with your Firebase credentials:
```env
FIREBASE_ADMIN_TYPE="service_account"
FIREBASE_ADMIN_PROJECT_ID="your-project-id"
FIREBASE_ADMIN_PRIVATE_KEY_ID="your-private-key-id"
FIREBASE_ADMIN_PRIVATE_KEY="your-private-key"
FIREBASE_ADMIN_CLIENT_EMAIL="your-client-email"
FIREBASE_ADMIN_CLIENT_ID="your-client-id"
FIREBASE_ADMIN_AUTH_URI="https://accounts.google.com/o/oauth2/auth"
FIREBASE_ADMIN_TOKEN_URI="https://oauth2.googleapis.com/token"
FIREBASE_ADMIN_AUTH_PROVIDER_X509_CERT_URL="https://www.googleapis.com/oauth2/v1/certs"
FIREBASE_ADMIN_CLIENT_X509_CERT_URL="your-cert-url"
```

## Firebase Setup

1. Create a new project in [Firebase Console](https://console.firebase.google.com/)
2. Enable Email/Password authentication in Authentication > Sign-in method
3. Get your Firebase configuration:
   - Go to Project Settings > General
   - Scroll down to "Your apps" and click the web icon (</>)
   - Register your app and copy the Firebase configuration
4. Update the Firebase configuration in these files:
   - frontend/final_login.html
   - frontend/final_signup.html
   - frontend/final_landing.html
   - frontend/final_dashboard.html

## Running the Application

1. Start the Django backend server:
```bash
cd backend
source venv/bin/activate  # On Windows use: venv\Scripts\activate
python manage.py runserver 8001
```

2. Access the application:
- Open your web browser and navigate to `http://localhost:8001`
- You'll be redirected to the login page
- Create a new account or log in with existing credentials

## Features

- User Authentication with Firebase
- Interactive Linux Command Learning Interface
- Progress Tracking
- Real-time Command Execution
- Modern and Responsive UI

## Project Structure

```
Terminal-Velocity/Final updates/
├── backend/
│   ├── authentication/     # Django authentication app
│   ├── core/              # Django project settings
│   ├── venv/              # Python virtual environment
│   ├── manage.py          # Django management script
│   └── requirements.txt   # Python dependencies
└── frontend/
    ├── final_login.html    # Login page
    ├── final_signup.html   # Signup page
    ├── final_landing.html  # Landing page
    └── final_dashboard.html # Main dashboard
```

## Common Issues and Solutions

1. **Firebase Not Initialized Error**
   - Make sure your Firebase configuration is correctly set in all HTML files
   - Check if you're using the correct Firebase project credentials

2. **CORS Issues**
   - The application is configured to run on port 8001
   - If using a different port, update CORS_ALLOWED_ORIGINS in backend/core/settings.py

3. **Authentication Issues**
   - Ensure your Firebase project has Email/Password authentication enabled
   - Check if your .env file contains the correct Firebase Admin credentials

## Security Notes

- This setup is for development purposes
- For production:
  - Enable HTTPS
  - Set DEBUG = False in settings.py
  - Use secure session cookies
  - Update ALLOWED_HOSTS and CORS settings
  - Protect your Firebase credentials
  - Use environment variables for sensitive data

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 