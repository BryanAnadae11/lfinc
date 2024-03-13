from django.urls import path

from django.contrib.auth import views as auth_views

from django.conf import settings

from . import views

urlpatterns= [

	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('blockchainfund/', views.blockchainfund, name='blockchain-fund'),
	path('liquidtoken/', views.liquidtoken, name='liquid-token'),
	path('bitcointradingfund/', views.bitcointradingfund, name='bitcoin-trading-fund'),
	path('earlystagetoken/', views.earlystagetoken, name='early-stage-token'),
	path('stakingfund/', views.stakingfund, name='staking-fund'),
	path('energies/', views.energies, name='energies'),
	path('sharestrading/', views.sharestrading, name='shares-trading'),
	path('agriculturalfund/', views.agriculturalfund, name='agricultural-fund'),
	path('nonfarmpayroll/', views.nonfarmpayroll, name='non-farm-payroll'),
	path('renewableenergy/', views.renewableenergy, name='renewable-energy'),
	path('investmentmanagement/', views.investmentmanagement, name='investment-management'),
	path('financialservice/', views.financialservice, name='financial-service'),
	path('portfoliomanagementservice/', views.portfoliomanagementservice, name='portfolio-management-service'),
	path('financialadvising/', views.financialadvising, name='financial-advising'),
	path('pressrelease/', views.pressrelease, name='press-release'),
	path('faqs/', views.faqs, name='faqs'),
	path('terms/', views.terms, name='terms'),
	path('privacy/', views.privacy, name='privacy'),
	path('otherpayment/', views.otherpayment, name='otherpayment'),
	path('contact/', views.contact, name='contact'),
	path('main-view/', views.main_view, name='main-view'),
	path('main-view/<str:ref_code>/', views.main_view, name='main-view'),
	path('signin/', views.signin, name='signin'),
	path('signup/', views.signup, name='signup'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('loan/', views.loan, name='loan'),
	path('plans/', views.plans, name='plans'),
	path('notifications/', views.notifications, name='notifications'),
	path('admindashboard/', views.admindashboard, name="admindashboard"),
	path('deposit/', views.deposit, name='deposit'),
	path('withdrawal/', views.withdrawal, name='withdrawal'),
	path('history/', views.history, name='history'),
	path('pending_deposit/', views.pending_deposit, name='pending_deposit'),
	path('pending_withdrawal/', views.pending_withdrawal, name='pending_withdrawal'),
	path('portfolio/', views.portfolio, name='portfolio'),
	path('pending_bonus/', views.pending_bonus, name='pending_bonus'),
	path('completed_transaction/', views.completed_transaction, name='completed_transaction'),
	path('myreferals/', views.myreferals, name='myreferals'),
	path('confirm_withdrawal/', views.confirm_withdrawal, name='confirm_withdrawal' ),
	path('update_withdrawal/<str:pk>/', views.update_withdrawal, name='update_withdrawal' ),
	path('decline_wihdrawal/<str:pk>/', views.decline_wihdrawal, name='decline_wihdrawal'),
	path('confirm_deposit/', views.confirm_deposit, name='confirm_deposit' ),
	path('update_payment/<str:pk>/', views.update_payment, name='update_payment' ),
	path('account_settings/', views.account_settings, name='account_settings'),
	path('create_bonus/', views.create_bonus, name='create_bonus'),
	path('use_bonus/', views.use_bonus, name='use_bonus'),
	path('transfer_funds/', views.transfer_funds, name='transfer_funds'),
	path('reset_password/', auth_views.PasswordResetView.as_view(template_name="lfincsapp/password_reset.html"), name='reset_password'),
	path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="lfincsapp/password_reset_done.html"), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="lfincsapp/password_reset_form.html"), name='password_reset_confirm'),
	path('reset_password_complete/', auth_views.PasswordResetView.as_view(template_name="lfincsapp/password_reset_complete.html"), name='password_reset_complete'),
	path('video_page/', views.video_page, name='video_page'),
	path('logout/', views.logoutuser, name='logout'),
]