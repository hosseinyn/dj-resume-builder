from django.urls import path

from .views import login , signup , panel , logout , delete_account , change_password

urlpatterns = [
    path("login/" , view=login , name="Login"),
    path("signup/" , view=signup , name="Signup"),
    path("panel/" , view=panel , name="User Panel"),
    path("logout/" , view=logout , name="Logout User"),
    path("delete-account/" , view=delete_account , name="Delete Account"),
    path("change-password/" , view=change_password , name="Change Password")
]