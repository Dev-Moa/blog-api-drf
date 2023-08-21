from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name=""), # sign up
    path('logout/blacklist/', views.BlacklistTokenUpdateView.as_view(), # logout
         name='blacklist'),
    path("", views.PostList.as_view(), name="home"), # post list
    path("<int:pk>/", views.PostDetail.as_view(), name="detail"), # post detail
]
