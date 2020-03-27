from CodeConfab.models import Poke, Prompt
from django.contrib.auth.decorators import login_required



def Notify(request):
    if request.user.is_authenticated:
        pokes = Poke.objects.filter(poked = request.user, seen = False).count()
        promts = Prompt.objects.filter(prompted = request.user, seen = False).count()
        notifications = int(pokes) + int(promts)
        requests = request.user.received_requests.count()
        return {'notify':notifications, 'requests':requests}
    else:
        return{}

    
   