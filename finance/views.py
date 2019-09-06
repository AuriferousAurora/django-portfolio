from django.shortcuts import render

def test_view(request):
  template = 'test_template.html'
  return render(request, template)