from django.http import HttpResponse


def index(request):
    return HttpResponse("Index")


def detail(request, book_id):
    return HttpResponse("detail %s" % book_id)


def edit(request, book_id):
    return HttpResponse("edit %s" % book_id)


def delete(request, book_id):
    return HttpResponse("delete %s" % book_id)


def create(request):
    return HttpResponse("create")


def mypage(request):
    return HttpResponse("mypage")


def login(request):
    return HttpResponse("login")


def logout(request):
    return HttpResponse("logout")


def signin(request):
    return HttpResponse("siginin")
