from django.shortcuts import render

from about.models import About


def home(request):
    abouts = About.objects.first()

    context = {
        # 'education': education,
        # 'skills': skills,
        # 'experiences': experience,
        # 'achievements': achievements,
        # 'extracurriculars': extracurriculars,
        'about': abouts
    }

    return render(request, 'index.html', context)