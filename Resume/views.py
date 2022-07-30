from django.shortcuts import render

from about.models import About
from education.models import Education
from skills.models import Skills


def home(request):
    abouts = About.objects.first()
    education = Education.objects.all().order_by('-id')
    skills = Skills.objects.all().order_by('-id')

    context = {
        'education': education,
        'skills': skills,
        # 'experiences': experience,
        # 'achievements': achievements,
        # 'extracurriculars': extracurriculars,
        'about': abouts
    }

    return render(request, 'index.html', context)