from django.urls import path

from .views import create_resume , delete_resume , edit_resume , resume

urlpatterns = [
    path("access/<slug:access_id>" , view=resume , name="Show Resume"),
    path("create_resume/" , view=create_resume , name="Create New Resume"),
    path("delete_resume/<slug:access_id>" , view=delete_resume , name="Delete Resume"),
    path("edit_resume/<slug:access_id>" , view=edit_resume , name="Edit Resume")
]