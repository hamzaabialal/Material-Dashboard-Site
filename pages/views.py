from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomeView(TemplateView):
    template_name = "home.html"


class HomeViewTemplate(TemplateView):
    template_name = "index.html"


class ProfileView(TemplateView):
    template_name = "profile.html"


class MapView(TemplateView):
    template_name = "map.html"    


class NotificationsView(TemplateView):
    template_name = "notifications.html"

class IconView(TemplateView):
    template_name = "icons.html"


class DashboardView(TemplateView):
    template_name = "dashboard.html"


class BillingView(TemplateView):
    template_name = "billing.html"  


class RtlView(TemplateView):
    template_name = 'rtl.html'


class LtrView(TemplateView):
    template_name = 'sign-in.html'

class RegisterView(TemplateView):
    template_name = 'sign-up.html'    


class TableView(TemplateView):
    template_name = 'tables.html'

class BlankView(TemplateView):
    template_name = 'template.html'    


class TypographyView(TemplateView):
    template_name = 'typography.html'    


class VirtualRealityView(TemplateView):
    template_name = 'virtual-reality.html'    