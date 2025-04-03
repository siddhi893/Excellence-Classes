# tuition_app/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'tuition_app'
# urlpatterns = [
#     path('register', views.register, name='register'),
#     path('login/', LoginView.as_view(template_name='tuition_app/filter_students.html', redirect_authenticated_user=True), name='login'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
#     path('filter_students/', views.filter_students, name = "filter_students"),
# ]


urlpatterns = [
    path('register', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='tuition_app/adminlogin.html', redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='/app/login'), name='logout'),
    path('filter_students/', views.filter_students, name = "filter_students"),
    path('student/<int:student_id>', views.student_detail, name="student_detail"),
    path('display', views.display),
    
    
    path('delete_student/<int:student_id>', views.delete_student, name="delete_student"),
    path('update_student/<int:student_id>', views.update_student, name="update_student")
]