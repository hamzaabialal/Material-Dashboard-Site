from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomeViewTemplate.as_view(), name='home_template'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('map/', views.MapView.as_view()),
    path('notifications/', views.NotificationsView.as_view(), name='notifications'),
    path('icons/', views.IconView.as_view(), name='icons'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('billing/', views.BillingView.as_view(), name='billing'),
    path('rtl/', views.RtlView.as_view(), name='rtl'),
    path('login/', views.LtrView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('table/', views.TableView.as_view(), name='table'),
    path('blank/', views.BlankView.as_view(), name='blank'),
    path('typography/', views.TypographyView.as_view(), name='typography'),
    path('virtual-reality/', views.VirtualRealityView.as_view(), name='virtual-reality'),
]