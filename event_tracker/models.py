from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# from django.contrib.sessions.models import Session
from .signals import post_viewed_signal, page_viewed_signal
from .utils import get_client_ip
# from django.http import HttpRequest


User = settings.AUTH_USER_MODEL

class Event(models.Model):
    session_id = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ip_address = models.CharField(max_length=220, blank=True, null=True)
    host = models.CharField(max_length=220, blank=True, null=True)
    path = models.CharField(max_length=220, blank=True, null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed on %s" %(self.content_object, self.timestamp)
        class meta:
            ordering = ['-timestamp']
            verbose_name = 'Object viewed'
            verbose_name_plural = 'Objects viewed'

def post_viewed_receiver(sender, post, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)

    try:
        ip_address = get_client_ip(request)
        if not request.session or not request.session.session_key:
            request.session.save()
            session_id = request.session.session_key
        else:
            session_id = request.session.session_key

        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

    except:
        pass

    host = request.META['HTTP_HOST']
    path = request.META['REQUEST_URI']


    Event.objects.create(
            session_id = session_id,
            user = user,
            content_type = c_type,
            object_id = post.id,
            ip_address = ip_address,
            host = host,
            path = path
            )

post_viewed_signal.connect(post_viewed_receiver)


def page_viewed_receiver(sender, host, path, request, *args, **kwargs):
    c_type = ContentType.objects.get_for_model(sender)

    try:
        ip_address = get_client_ip(request)
        if not request.session or not request.session.session_key:
            request.session.save()
            session_id = request.session.session_key
        else:
            session_id = request.session.session_key

        if request.user.is_authenticated:
            user = request.user
        else:
            user = None

    except:
        pass

    host = request.META['HTTP_HOST']
    path = request.META['REQUEST_URI']


    Event.objects.create(
            session_id = session_id,
            user = user,
            content_type = c_type,
            ip_address = ip_address,
            host = host,
            path = path
            )

page_viewed_signal.connect(page_viewed_receiver)

