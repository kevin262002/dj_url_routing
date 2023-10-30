from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect

def another_view(request):
    content = '<p>dummy content</p>'
    return HttpResponse(content)
def original_view(request):
    reversed_url = reverse(another_view)  # /another-url/
    return HttpResponseRedirect(reverse(another_view))
