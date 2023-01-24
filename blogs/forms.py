from django import forms
from django.db.models.fields import TextField
from django.forms import ModelForm
from django.forms import widgets
from django.forms.fields import ChoiceField
from django.forms.widgets import DateInput
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from . import models
from .models import Contact, VirtualReception

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

STATUS_CHOICES = (
    ('single', 'Single'),
    ('married', 'Married'),
)

REGION_CHOICES = (
    ('andijan', ("Andijan")),
    ('bukhara', ("Bukhara")),
    ('fergana', ("Fergana")),
    ('jizzakh', ("Jizzakh")),
    ('khorezm', ("Khorezm")),
    ('namangan', ("Namangan")),
    ('navoiy', ("Navoiy")),
    ('kashkadarya', ("Kashkadarya")),
    ('samarkand', ("Samarkand")),
    ('sirdarya', ("Sirdarya")),
    ('surkhandarya', ("Surkhandarya")),
    ('tashkent', ("Tashkent")),
    ('tashkent_city', ("Tashkent city")),
    ('karakalpakstan', ("Karakalpakstan")),
)


class VirtualReceptionForm(ModelForm):
    class Meta:
        model = VirtualReception
        fields = "__all__"
        widgets = {
            "date_of_birth": DateInput(attrs={"type": "date"})
        }
        labels = {
            "full_name": _("Fullname"),
            "email": _("email"),
            "phone_number": _("phone_number"),
            "region": _("region"),
            "address": _("address"),
            "date_of_birth": _("date_of_birth"),
            "gender": _("gender"),
            "marital_status": _("marital_status"),
            "file_upload": _("file_upload"),
            "message": _("message"),
        }
    

    def __init__(self, *args, **kwargs):
        super(VirtualReceptionForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control input__form_con"

            if field == "file_upload":
                self.fields[field].widget.attrs["class"] = "file-input border-0"
            
            if field == "message":
                self.fields[field].widget.attrs["class"] = "w-100 form-control input__form_con"
                self.fields[field].widget.attrs["cols"] = "30"
                self.fields[field].widget.attrs["rows"] = "10"



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
