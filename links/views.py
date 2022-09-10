from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ipware import get_client_ip

from links.models import Link
from links.forms import LinkForm

from likes.models import Like

# Create your views here.

def top(request):
    tmplinks = Link.objects.all()
    if request.user.is_authenticated:
        links = []
        for link in tmplinks:
            record = Like.objects.filter(link=link, created_by=request.user)
            if record.exists():
                links.append({'link':link, 'like':True})
            else:
                links.append({'link':link, 'like':False})
        context = {'links':links}
    else:
        context = {'links':tmplinks}
    return render(request, 'links/top.html', context)

@login_required
def link_new(request):
    client_ip, is_routable = get_client_ip(request)
    if request.method == 'POST' and client_ip is not None:
        form = LinkForm(request.POST)
        if form.is_valid():
                link = form.save(commit=False)
                link.created_by = request.user
                link.ip_address = client_ip
                link.save()
                return redirect(top)
        else:
            form = LinkForm()
            return render(request, 'links/link_new.html', {'form':form})
    else:
        form = LinkForm()
        return render(request, 'links/link_new.html', {'form':form})