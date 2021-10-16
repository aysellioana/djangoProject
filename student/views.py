from io import BytesIO

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from rest_framework import viewsets
from xhtml2pdf import pisa

from student.forms import StudentForm
from student.models import Student
from student.serializers import StudentSerializer


class StudentCreateView(LoginRequiredMixin,PermissionRequiredMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    #fields = '__all__' SAUU
    success_url = reverse_lazy('create-new-student')
    form_class = StudentForm
    permission_required = 'student.add_student'


class StudentListView(LoginRequiredMixin,PermissionRequiredMixin, ListView):
    template_name = 'student/list_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.view_list_of_student'


class StudentUpdateView(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.change_student'


class StudentDetailView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
    template_name = 'student/detail_student.html'
    model = Student
    permission_required = 'student.detail_student'


class StudentDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.delete_student'


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def all_students_to_pdf(request):
    all_students = Student.objects.filter(active=True)  #interogam tabel student si luam toti studentii active=true
    # x = [student.first_name for student in all_students if student.active == 1]
    context = {'students': all_students}  #creem un dictionar numit context unde stocam intr-o cheie numita students toti studenti
    pdf = render_to_pdf('student/student_pdf.html', context)  #apelam functia render_to_pdf prin care trimitem template-ul si contextul
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
    filename = "List of Students"
    content = "inline; filename=%s" % filename
    response['Content-Disposition'] = content
    return response

def details_per_student(request, pk):
    details_student = Student.objects.get(id=pk)
    context = {'details': details_student}
    pdf = render_to_pdf('student/details_student_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
    filename = f"Student - {details_student.first_name} {details_student.last_name}"
    content = "inline; filename=%s" % filename
    response['Content-Disposition'] = content
    return response


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer