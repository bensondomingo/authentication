import os
from urllib.parse import urlencode
from rest_auth.serializers import PasswordResetSerializer
from django.conf import settings


class CustomPasswordResetSerializer(PasswordResetSerializer):

    email_template_path = 'authentication/email/'

    def get_email_options(self):
        return {
            'subject_template_name': os.path.join(self.email_template_path,
                                                  'password_reset_subject.txt'),
            'email_template_name': os.path.join(self.email_template_path,
                                                'password_reset_body.txt'),
            'html_email_template_name': os.path.join(self.email_template_path,
                                                     'password_reset_email.html'),
            'extra_email_context': {
                'new_password_url': settings.NEW_PASSWORD_URL
            }
        }
