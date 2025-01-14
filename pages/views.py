from django.shortcuts import render

def mainpage(request):
 return render(request, 'pages/mainpage.html')
def company(request):
 return render(request, 'pages/company_info.html')


# 추가 
def main(request):
    return render(request, 'pages/main.html')

def login(request):
    return render(request, 'pages/login.html')

def about(request):
    return render(request, 'pages/about.html')

def category1(request):
    return render(request, 'pages/category1.html')

def notice(request):
    return render(request, 'pages/notice.html')