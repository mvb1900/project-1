from django.shortcuts import render


def todo_list_view(request, **kwargs):
    context = {
        "list": [
            "Sleeping",
            "Grow up",
            "Working"
        ]
    }

    return render(request, "app_todolist/index.html", context)