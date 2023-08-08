from accounts.models import extra_user_info
from django.utils import timezone


class Custom_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            ip = request.META.get('REMOTE_ADDR')
            browser = request.headers.get('User-Agent').split()[2]
            user = request.user
            user.last_seen = timezone.now()
            user.save()
            if ip is not None:
                extra_user_info.objects.get_or_create(
                    user=user, ip=ip, browser=browser)
            else:
                ip = request.META.get('HTTP_X_FORWARDED_FOR')
                extra_user_info.objects.get_or_create(
                    user, ip=ip, browser=browser)
        response = self.get_response(request)
        return response