from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.models import AnonymousUser


class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = AnonymousUser()

        if request.path.startswith("/admin") and not request.user.is_superuser:
            return redirect("dashboard")
        return self.get_response(request)
