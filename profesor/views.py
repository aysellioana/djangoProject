from io import BytesIO

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from xhtml2pdf import pisa

from profesor.forms import TeacherForm
from profesor.models import Teacher


class TeacherCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'teacher/create_new_teacher.html'
    model = Teacher
    success_url = reverse_lazy('create-new-teacher')
    form_class = TeacherForm
    permission_required = 'profesor.add_teacher'


class TeacherListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'teacher/list_teachers.html'
    model = Teacher
    context_object_name = 'all_teachers'
    permission_required = 'profesor.view_list_of_professor'


class TeacherUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'teacher/update_teacher.html'
    model = Teacher
    form_class = TeacherForm
    success_url = reverse_lazy('list-of-teachers')
    permission_required = 'profesor.change_teacher'


class TeacherDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'teacher/detail_teacher.html'
    model = Teacher
    permission_required = 'profesor.view_teacher'


class TeacherDeleteView(LoginRequiredMixin,PermissionRequiredMixin, DeleteView):
    template_name = 'teacher/delete_teacher.html'
    model = Teacher
    success_url = reverse_lazy('list-of-teachers')
    permission_required = 'profesor.delete_teacher'


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def details_per_teacher(request, pk):
    details_teacher = Teacher.objects.get(id=pk)
    context = {'detailss': details_teacher}
    pdf = render_to_pdf('teacher/details_teacher_pdf.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
    filename = f"Teacher - {details_teacher.first_name} {details_teacher.last_name}"
    content = "inline; filename=%s" % filename
    response['Content-Disposition'] = content
    return response
