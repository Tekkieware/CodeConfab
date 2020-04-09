from CodeConfab.models import Poke, Prompt
from django.contrib.auth.decorators import login_required
from django.views import generic
from braces.views import LoginRequiredMixin

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django_private_chat import models
from django_private_chat import utils
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db.models import Q



def Notify(request, **kwargs):
    if request.user.is_authenticated:
        pokes = Poke.objects.filter(poked = request.user, seen = False).count()
        promts = Prompt.objects.filter(prompted = request.user, seen = False).count()
        notifications = int(pokes) + int(promts)
        requests = request.user.received_requests.count()
        ws_server_path = '{}://{}:{}/'.format(
            settings.CHAT_WS_SERVER_PROTOCOL,
            settings.CHAT_WS_SERVER_HOST,
            settings.CHAT_WS_SERVER_PORT,
        )
        return {'notify':notifications, 'requests':requests,'ws_server_path':ws_server_path}
    else:
        return{}