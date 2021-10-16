from student.models import Student


def get_all_students(request):
    all_students = Student.objects.all()
    return {'allstudents': all_students}