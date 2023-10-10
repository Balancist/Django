from django.urls import path
from . import views as here
from django.contrib.auth import views

app_name = 'Justice'
urlpatterns = [
	path('', here.Index.as_view(), name='index'),
    path('crime/<slug:slug>/', here.CrimeDetail.as_view(), name='crime'),
	path('signup/', here.Signup.as_view(), name='signup'),
	path('profile/', here.Profile.as_view(), name='profile'),
    path('profile/edit/', here.EditProfile.as_view(), name='edit_profile'),
    path('complaint/file/', here.FileComplaint.as_view(), name='file_complaint'),
    path('complaint/modify/<int:pk>/', here.ModifyComplaint.as_view(), name='modify_complaint'),
    path('complaint/handle/<int:pk>/', here.HandleComplaint.as_view(), name='handle_complaint'),
    path('complaint/close/<int:pk>/', here.CloseComplaint.as_view(), name='close_complaint'),
	path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("password_change/", views.PasswordChangeView.as_view(), name="password_change"),
    path("password_change/done/",views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("password_reset/done/",views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path("reset/done/",views.PasswordResetCompleteView.as_view(),name="password_reset_complete")
]