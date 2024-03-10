import logging
from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import render_to_string

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Index page accessed")
    data = {
        'title': 'главная',
    }
    return render(request, 'first_task_app/index.html', context=data)


def about(request):
    logger.debug('About page accessed')
    data = {
        'title': 'о себе',
    }
    return render(request, 'first_task_app/about.html', context=data)

