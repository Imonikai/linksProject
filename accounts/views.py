from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from links.models import Link

@login_required
def mypage(request):
    links = Link.objects.filter(created_by=request.user)
    context = {'links':links}
    return render(request, 'accounts/mypage.html', context)