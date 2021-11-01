from django.urls import path

from . import views

urlpatterns = [
    path('Account/', views.AccountList.as_view(), name="getNote"),
    path('Account/<int:pk>', views.AccountDetails.as_view(), name="getNotes"),
    path('Account/create-account/', views.AccountList.as_view(), name="create-note"),
    path('Account/update-account/<int:pk>', views.AccountDetails.as_view(), name="update-note"),
    path('Account/delete-account/<int:pk>', views.AccountDetails.as_view(), name="delete-note"),
    path('Account/otp/', views.OTPView.send_otp, name="getNotes"),
    path('Account/otp/verify/', views.OTPView.as_view(), name="getNotes"),
]