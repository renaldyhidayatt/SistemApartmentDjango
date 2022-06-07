from django.http import Http404
from django.shortcuts import redirect


class AdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin") and not request.user.is_superuser:
            raise redirect("home")
        return self.get_response(request)