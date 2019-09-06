from django.shortcuts import render

def test_view(request):
  template = 'test_template.html'
  context = {}
  return render(request, template, context=context)