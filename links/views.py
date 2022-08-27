from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ipware import get_client_ip

from links.models import Link
from links.forms import LinkForm

# Create your views here.

def top(request):
    links = Link.objects.all()
    context = {'links':links}
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