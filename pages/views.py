from django.views.generic import TemplateView

# Create your views here.


"""A class-based generic views is used to render the template """
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"