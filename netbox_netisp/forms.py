from django import forms
from django.urls import reverse
from utilities.forms import BootstrapMixin, SlugField

from .models import Customer, Address, BillingPackage, Account, Equipment, RadioAccessPoint


class CustomerForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "middle_name",
            "last_name",
            "slug",
        )


class AddressForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Address
        fields = (
            "street_number",
            "street_name",
            "street_suffix",
            "city",
            "state_code",
            "zip",
            "slug",
        )


class BillingPackageForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = BillingPackage
        fields = ("name", "price", "download_speed", "upload_speed", "data_cap", "slug")


class CustomerFilterForm(BootstrapMixin, forms.ModelForm):
    """Form for filtering BgpPeering instances."""

    q = forms.CharField(required=False, label="Search")

    first_name = forms.CharField(
        required=False,
        label="First Name",
    )

    last_name = forms.CharField(
        required=False,
        label="Last Name",
    )

    slug = forms.SlugField(
        required=True,
        label="Slug",
    )

    class Meta:
        model = Customer
        fields = []


class AccountForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Account
        fields = ("primary_applicant",)


class EquipmentForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ("serial", "manufacturer", "device_type")

class RadioAccessPointForm(BootstrapMixin, forms.ModelForm):
    return_url = forms.CharField(widget=forms.HiddenInput(), initial="/plugins/netbox_netisp/sector/")

    class Meta:
        model = RadioAccessPoint
        fields = ("name", "manufacturer", "device_type", "frequency", "antenna")
