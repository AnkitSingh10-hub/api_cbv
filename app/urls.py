from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [

    path('instructors', views.InstructorListView.as_view()),
    path('courses', views.CourseListView.as_view()),
    path('courses/<int:pk>', views.CourseListView.as_view(), name="course-detail"),
    path('courses/<int:pk>', views.InstructorDetailView.as_view(), name="instructor-detail"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



]
