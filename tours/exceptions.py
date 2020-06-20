from django.http import Http404


class CustomHttp404(Http404):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return self.message
