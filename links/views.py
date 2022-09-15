from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from ipware import get_client_ip

from links.models import Link
from links.forms import LinkForm

from likes.models import Like

# Create your views here.

def top(request):
    context = []
    links = Link.objects.all().order_by('created_at').reverse()
    if request.user.is_authenticated:
        for link in links:
            if Like.objects.filter(link=link, created_by=request.user).exists():
                context.append({'link':link, 'like':True, 'like_count':link.like_count})
            else:
                context.append({'link':link, 'like':False, 'like_count':link.like_count})
    else:
        for link in links:
            context.append({'link':link, 'like':False, 'like_count':link.like_count})

    context = {'context':context}
    return render(request, 'links/top.html', context)

def order_like(request):
    context = []
    links = Link.objects.all().order_by('like_count').reverse()
    if request.user.is_authenticated:
        for link in links:
            if Like.objects.filter(link=link, created_by=request.user).exists():
                context.append({'link':link, 'like':True, 'like_count':link.like_count})
            else:
                context.append({'link':link, 'like':False, 'like_count':link.like_count})
    else:
        for link in links:
            context.append({'link':link, 'like':False, 'like_count':link.like_count})

    context = {'context':context}
    return render(request, 'links/order_like.html', context)


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