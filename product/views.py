from django.shortcuts import render
from .models import MainContent

# Create your views here.
def index(request):
    # 가장 최신 콘텐츠를 상단 노출
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list': content_list}
    return render(request, 'product/content_list.html', context)

