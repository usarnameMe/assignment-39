from django.urls import path
from .views import RegisterView, LoginView, LogoutView, NoteList, NoteDetail

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("notes/", NoteList.as_view(), name="notes"),
    path("notes/<int:pk>/", NoteDetail.as_view(), name="note_detail"),
]
