from django.urls import path
from django.utils.translation import gettext_lazy as _
from . import views
from blogs import views as contact_views
from django.conf.urls import url, include, handler404, handler500

# APP NAME
app_name = 'blogs'
# URLS
urlpatterns = [
    path('about/', views.about_page, name='about'),

    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.NewsDetailView.as_view(), name='news_detail'),

    path('tender/', views.TenderListView.as_view(), name='tender_list'),
    path('tender/<int:year>/<int:month>/<int:day>/<slug:slug>', views.TenderDetailView.as_view(),
         name='tender_detail'),

    path('product/', views.ProductListView.as_view(), name='product_list'),
    path('product/<int:_id>/', views.ProductItemView, name='product_item'),

    path('membership/', views.MembershipListView.as_view(), name='membership_list'),
    path('membership/<slug:slug>', views.MembershipDetailView.as_view(), name='membership_detail'),

    path('exhibitions/', views.ExhibitionListView.as_view(), name='exhibition'),
    path('exhibitions/<int:year>/<int:month>/<int:day>/<slug:slug>', views.ExhibitionDetailView.as_view(),
         name='exhibition_detail'),

    path('gallery/', views.GalleryListView.as_view(), name='gallery'),
    path('gallery/<int:_id>/', views.GalleryImagesView, name='gallery-images'),

    path('search/', views.NewsSearchView.as_view(), name='news_search_url'),

    path('media/', views.MediaListView.as_view(), name='media'),

    path('vacancy/', views.VacancyListView.as_view(), name='vacancy'),

    path('faq/', views.FAQListView.as_view(), name='faq'),

    path('contact/', contact_views.contact_view, name='contact_form'),

    path('virtual_reception/', views.virtual_reception_view, name='virtual_reception_form'),

    path('entrepreneurs/', views.EntrepreneursListView.as_view(), name='entrepreneurs'),

    path('press_service/', views.press_service_view, name='press_service'),

    path('how_to_join/', views.join_view, name='how_to_join'),

    path('moscow/', views.moscow_view, name='moscow'),

    path('events/', views.events_view, name='events'),

    path('presentations/', views.presentations_view, name='presentations'),

    path('press_releases/', views.press_releases_view, name='press_releases'),

    path('publications/', views.publications_view, name='publications'),

    path('leadership/', views.leadership_view, name='leadership'),
    path('leadership_press/', views.leadership_press_view, name='leadership_press'),

    path('investors/', views.investors_view, name='investors'),

    path('exporters/', views.exporters_view, name='exporters'),

    path('youth_policy/', views.youth_policy_view, name='youth_policy'),

    path('structure/', views.structure_view, name='structure'),

    path('partners/', views.partners_view, name='partners'),

    path('foreighn_representation/', views.foreighn_view, name='foreighn_representation'),

    path('doc_links/', views.foreighn_representation_links, name='foreighn_representation_links'),
    path('doc_links/<slug>/', views.foreighn_representation_items, name='foreighn_representation_items'),

    path('subsidaries/', views.subsidaries_view, name='subsidaries'),

    path('subsidaries2/', views.subsidaries2_view, name='subsidaries2'),

    path('territorial_admin/', views.territorial_view, name='territorial_admin'),

    path('history_of_organization/', views.history_view, name='history_of_organization'),

    path('menu_companys/<type_slug>/', views.menu_companys_view, name='menu_companys'),

    path('menu_companys/', views.companys_types_view, name='companys_types'),

    path('membership_procedure/', views.MembershipProcedureListView.as_view(), name='membership_procedure'),

    path('benefits/', views.benefits_view, name='benefits'),

    path('investment_potential/', views.investmentadmin_view, name='investment_potential'),

    path('export_potential/', views.export_potential_view, name='export_potential'),

    path('export_implementation/', views.export_implementation_view, name='export_implementation'),

    path('export_law/', views.export_law_view, name='export_law'),

    path('market_entry_strategies/', views.market_entry_strategies_view, name='market_entry_strategies'),

    path('content/<slug:slug>', views.StaticContentView.as_view(), name='static_page'),

    path('legal/', views.LegalDocumentListView.as_view(), name='legal'),

    path('legal/<slug:slug>', views.LegalDocumentView.as_view(), name='legal_detail'),

    path('statistic/', views.StatisticListView.as_view(), name='statistic_list'),

    path('statistic/<slug:slug>', views.StatisticDetailView.as_view(), name='statistic_detail'),

    path('lex_uz/', views.lex_uz_view, name='lex_uz'),

     path('<branch_name>/', views.foreighn_branch_view, name='foreighn_representation_branch'),
    path('', views.index_page, name='index'),
]