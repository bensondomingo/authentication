# djangorestframework settings
AUTH_INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
]

#
AUTH_REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ]
}

# Adds allauth accounts endpoint if set to false
AUTHENTICATION_API_ONLY = True

# django-rest-auth
AUTH_INSTALLED_APPS += [
    # rest-api basic authencation
    'rest_auth',

    # rest-api registration
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    # Do not remove. Causes exception when
    # deleting a user instance on the admin page
    'allauth.socialaccount',
]

AUTHENTICATION_BACKENDS = [
    # Default django auth backend
    "django.contrib.auth.backends.ModelBackend",
    # Backend used by allauth (required by rest_auth)
    "allauth.account.auth_backends.AuthenticationBackend"
]

REST_AUTH_SERIALIZERS = {
    'PASSWORD_RESET_SERIALIZER': 'authentication.api.serializers.CustomPasswordResetSerializer'
}

ACCOUNT_AUTHENTICATION_METHOD = 'username'
ACCOUNT_EMAIL_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_ON_EMAIL_CONFIRMATION = False

# Implement this urls in vue
LOGIN_URL = '/auth/login/'
LOGIN_REDIRECT_URL = '/accounts/profile/'

# Implement this NEW_PASSWORD_URL in vue.
# Should accept uid and token as props
# Should accept password and password confirmation forms
# POST the content to /auth/api/password/reset/confirm/
NEW_PASSWORD_URL = '/auth/password/reset'

SITE_ID = 1


# Email settings using sendgrid
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'support@djangorest.com'
