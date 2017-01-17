from django.contrib import admin
from django import forms

from core.models import Configuration

from redactor.widgets import RedactorEditor


class ConfigurationAdminForm(forms.ModelForm):
    class Meta:
        model = Configuration
        widgets = {
            'about': RedactorEditor(),
            'privacy_policy': RedactorEditor(),
            'terms_of_service': RedactorEditor(),
        }
        fields = ("header_img", "about", "privacy_policy", "terms_of_service")


class ConfigurationAdmin(admin.ModelAdmin):
    form = ConfigurationAdminForm

admin.site.register(Configuration, ConfigurationAdmin)
