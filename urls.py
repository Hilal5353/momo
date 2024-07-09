from django.urls import path
from shop import views
from shop.forms import LoginForm, MyPasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView
urlpatterns = [
    path('', views.home, name='homePAGE'),
    path("shoppage/", views.shopPage, name='shoppage'),
    path("about/", views.about, name='AboutUs'),
    path("contact/", views.contact, name='ContactUs'),
    path("tracker/", views.tracker, name='TrackingStatus'),
    path("products/", views.productView, name="ProductView"),
    path("search/", views.search, name='Search'),
    path("checkout/", views.checkout, name='Checkout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='shop/login.html',
        authentication_form=LoginForm,
    ),name='login'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(
    template_name='shop/passwordchange.html',
    form_class=MyPasswordChangeForm), name='password_change'),

    path('passwordchangedone/', auth_views.PasswordChangeView.as_view(
    template_name='shop/passwordchangedone.html',), name='password_change_done'),

    path('password-reset/', auth_views.PasswordResetView.as_view(
    template_name='shop/password_reset.html',
    form_class=PasswordResetForm), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
    template_name='shop/password_rest_confirm.html',
    form_class=SetPasswordForm), name='password_reset_confirm'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
    template_name='shop/password_reset_done.html',
    ), name='password_reset_done'),

    path('password-reset-complate/', auth_views.PasswordResetCompleteView.as_view(
    template_name='shop/password_rest_complate.html',
    ), name= 'password_reset_complete' ),



    path('error2/', views.error2, name='error2'),
    path('error/', views.error, name='error'),
    path("logoutt/", views.Logout, name='logoutt'),
    path("logout/", views.LogoUt, name='LogOut')

]













