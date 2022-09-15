from ipaddress import ip_address
from django.shortcuts import render
from django.http import JsonResponse

from likes.models import Like
from links.models import Link

from ipware import get_client_ip

# Create your views here.

def like_change(request, link_pk):
    client_ip, is_routable = get_client_ip(request)
    link = Link.objects.get(pk=link_pk)
    if request.user.is_authenticated and link is not None:
        record = Like.objects.filter(
            link=link,
            created_by=request.user
        )
        if record.exists():
            record.delete()
            link.like_count -= 1
            link.save()
        else:
            new_record = Like(
                link=link,
                created_by=request.user,
                ip_address=client_ip
            )
            new_record.save()
            link.like_count += 1
            link.save()

        data = {
            "status":"OK",
        }
        return JsonResponse(data)
    else:
        data = {
            "status":"NG",
        }
        return JsonResponse(data)