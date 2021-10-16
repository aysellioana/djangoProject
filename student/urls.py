from django.urls import path, include
from rest_framework import routers

from student import views
from student.views import StudentViewSet

router = routers.DefaultRouter()
router.register('api_all_students', StudentViewSet)

urlpatterns = [
    path('create_new_student/', views.StudentCreateView.as_view(), name='create-new-student'),
    path('all_students/', views.StudentListView.as_view(), name='list-of-students'),
    path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
    path('detail_student/<int:pk>/', views.StudentDetailView.as_view(), name='detail-student'),
    path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='delete-student'),
    path('export_to_pdf/', views.all_students_to_pdf, name='export-to-pdf'),
    path('export_to_pdf_details_about_student/<int:pk>', views.details_per_student, name='export-to-pdf-details'),
    path('', include(router.urls))
]
