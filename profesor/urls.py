from django.urls import path

from profesor import views

urlpatterns = [
    path('create_new_teacher/', views.TeacherCreateView.as_view(), name='create-new-teacher'),
    path('all_teachers/', views.TeacherListView.as_view(), name='list-of-teachers'),
    path('update_teacher/<int:pk>/', views.TeacherUpdateView.as_view(), name='update-teacher'),
    path('detail_teacher/<int:pk>/', views.TeacherDetailView.as_view(), name='detail-teacher'),
    path('delete_teacher/<int:pk>/', views.TeacherDeleteView.as_view(), name='delete-teacher'),
    path('export_to_pdf_details_about_teacher/<int:pk>', views.details_per_teacher, name='export-to-pdf-detail-teacher')
]
