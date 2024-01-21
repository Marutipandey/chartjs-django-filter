from django.shortcuts import render
from django.db.models import Count
from .models import *
from django.db.models.functions import ExtractYear,ExtractMonth

def home(request):
    # Aggregate counts based on course and gender
    course_counts = Student.objects.filter(verified=True).values('course').annotate(count=Count('course'))
    gender_counts = Student.objects.filter(verified=True).values('gender').annotate(count=Count('gender'))
    teacher_counts = Teacher.objects.values('teacher_gender__gender').annotate(count=Count('teacher_gender'))
    teacher_counts = Teacher.objects.values('teacher_name').annotate(count=Count('teacher_name'))
    gender_year_counts = Student.objects.annotate(year=ExtractYear('dateField')).values('year').annotate(count=Count('year'))
    gender_month_counts = Student.objects.annotate(month=ExtractMonth('dateField')).values('month').annotate(count=Count('month'))
    # Extract data for rendering in the template
    cl = []
    cn = []
    gl = []
    gn = []
    tl = []
    tn = []
    gyl = []
    gyn = []
    gml = []
    gmn = []

    for i in gender_month_counts:
         gml.append(i['month'])
         gmn.append(i['count'])

    for i in teacher_counts:
        tl.append(i['teacher_name'])
        tn.append(i['count'])
    
    for item in gender_counts:
        gl.append(item['gender'])
        gn.append(item['count'])

    for item in gender_year_counts:
        gyl.append(item['year'])
        gyn.append(item['count'])
        

    for item in course_counts:
            cl.append(item['course'])
            cn.append(item['count'])
    context = {
        # 'cl': cl,
        # 'gl': gl,
        # 'cn': cn,
        # 'gn': gn,
        # 'tl':tl,
        # 'tn':tn,
        # 'gyl': gyl,
        # 'gyn': gyn,
        # 'gml':gml,
        # 'gmn':gmn
         
    
        'cl': cl,
        'gl': gl,
        'cn': cn,
        'gn': gn,
        'tl': tl,
        'tn': tn,
        'gyl': gyl,
        'gyn': gyn,
        'gml': gml,
        'gmn': gmn,
    
    }

    return render(request, 'index.html', context)
