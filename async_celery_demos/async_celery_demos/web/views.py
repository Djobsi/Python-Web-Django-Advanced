from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render

from async_celery_demos.web.tasks import slow_operation

UserModel = get_user_model()


def get_user_count():
    return UserModel.objects.count()


def get_groups_count():
    return Group.objects.count()


def index(request):
    user_count = get_user_count()
    groups_count = get_groups_count()

    title = "It works!"

    context = {
        "title": title,
        "user_count": user_count,
        "group_counts": groups_count,
    }

    slow_operation()
    return render(request, "web/index.html", context)
