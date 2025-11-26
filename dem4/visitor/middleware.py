from django.utils.deprecation import MiddlewareMixin
from .models import Visitor

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/admin/jsi18n/') or request.path.startswith('/.well-known/'):
            return
        if request.user.username == 'junior':
            return
        ip_address = self.get_client_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        path = request.path
        referer = request.META.get('HTTP_REFERER', '')
        if request.user.is_authenticated:
            user = request.user.username
        else:
            user = "неавторизованный"
        Visitor.objects.create(
            ip_address=ip_address,
            user_agent=user_agent,
            path=path,
            referer=referer,
            user=user
        )

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
