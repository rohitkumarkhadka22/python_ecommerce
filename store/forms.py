from django import forms
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Enter your password",
            }
        )
    )

    confirm_password = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Confirm your password",
            }
        )
    )

    class Meta:
        model = User

        fields = [
            "username",
            "email",
            "password",
            "confirm_password",
        ]

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Enter your username",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500",
                    "placeholder": "Enter your email",
                }
            ),
        }

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:

            if password != confirm_password:
                raise forms.ValidationError(
                    "Passwords do not match."
                )

        return cleaned_data