# imports for view
from django.core import mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse
from django.utils.decorators import method_decorator
from django.views import generic
from django.conf import settings
from django.http import HttpResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.contrib import messages
from django.db.models import Q
from .forms import ContactForm, VirtualReceptionForm
from .models import Post, GalleryImage, GalleryCategory, Product
from . import models, forms

###Pagination
CONST_PAGINATOR_NUMBER = 10


# 404 page
def error_404(request, exception):
    return render(request, 'errors/404.html')


# 500 page
def error_500(request):
    return render(request, 'errors/500.html', status=500)


# Home page
def index_page(request):
    context = {
        'useful_links': models.UsefulLink.objects.all(),
        'partners': models.Partner.objects.all(),
        'news': models.Post.objects.all()[:6],
        'product_categories': models.CompanyTypes.objects.all(),
        'photogallery': models.GalleryCategory.objects.all().order_by("-created")[:3],
        'media': models.Media.objects.all()[:8],
        'questions': models.FAQ.objects.all()[:6],
        'company_info': models.CompanyInfo.objects.all(),
        'menu': models.Menu.objects.all(),
        'infographics': models.Infographic.objects.all(),
        'expolinks': models.ExpoLink.objects.all(),
        'short_links': models.ShortLink.objects.filter(parent__isnull=True),
        'menu_links': models.MenuOverlay.objects.all(),
        'vacancys': models.Vacancy.objects.all(),
        'joins': models.HowToJoin.objects.all()
    }
    return render(request, 'blogs/index.html', context)


# About page
def about_page(request):
    context = {
        'vacancy': models.Vacancy.objects.all(),
        'items': models.CompanyInfo.objects.all(),
        'legislation': models.Legislation.objects.all(),
        'regional': models.RegionalAdministration.objects.all(),
    }
    return render(request, 'blogs/pages/about/indexAbout.html', context)


# Login Page
def login_page(request):
    return render(request, 'blogs/pages/login/index.html')


# Search
class NewsSearchView(generic.ListView):
    queryset = models.Post.objects.filter()
    template_name = 'blogs/pages/news/search_post_result.html'
    context_object_name = 'news'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(NewsSearchView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        q = self.request.GET.get('search')

        return self.queryset.filter(
            Q(translations__title__icontains=q) |
            Q(translations__main_text__icontains=q)
        )


# Join View
def join_view(request):
    joins = models.HowToJoin.objects.all()
    context = {
        "joins": joins
    }
    return render(request, "blogs/pages/how_to_join/how_to_join.html", context)


# Structure Page
def structure_view(request):
    structure = models.StructureAdmin.objects.all().first()
    context = {
        "structure": structure
    }
    return render(request, "blogs/pages/structure/structure.html", context)


# History page
def history_view(request):
    history = models.HistoryAdmin.objects.all()
    context = {
        "history": history
    }
    return render(request, "blogs/pages/history_of_organization/history_of_organization.html", context)


# Partners page
def partners_view(request):
    partner = models.Partner.objects.all()
    context = {
        "partner": partner
    }
    return render(request, "blogs/pages/partners/partners.html", context)


# Press service page
def press_service_view(request):
    press_service = models.PressServiceAdmin.objects.all()
    context = {
        "press_service": press_service
    }
    return render(request, "blogs/pages/press_service/press_service.html", context)


# Moscow Page
def moscow_view(request):
    moscow = models.MoscowAdmin.objects.all()
    context = {
        "moscow": moscow
    }
    return render(request, "blogs/pages/press_service/press_service.html", context)


# Benefits Page
def benefits_view(request):
    benefit = models.BenefitsAdmin.objects.all().first()
    print(benefit)
    print("salom")
    context = {
        "benefit": benefit
    }
    return render(request, "blogs/pages/benefits/benefits.html", context)


# Events Page
def events_view(request):
    events = models.EventsAdmin.objects.all()
    context = {
        "events": events
    }
    return render(request, "blogs/pages/events/events.html", context)


# Presentations Page
def presentations_view(request):
    presentations = models.PresentationsAdmin.objects.all()
    context = {
        "presentations": presentations
    }
    return render(request, "blogs/pages/presentations/presentations.html", context)


# Press Releases Page
def press_releases_view(request):
    press_releases = models.PressReleasesAdmin.objects.all()
    context = {
        "press_releases": press_releases
    }
    return render(request, "blogs/pages/press_releases/press_releases.html", context)


# Publications Page
def publications_view(request):
    publications = models.PublicationsAdmin.objects.all()
    context = {
        "publications": publications
    }
    return render(request, "blogs/pages/publications/publications.html", context)


# Youth Policy Page
def youth_policy_view(request):
    youth_policy = models.YouthPolicyAdmin.objects.all()
    context = {
        "youth_policy": youth_policy
    }
    return render(request, "blogs/pages/youth_policy/youth_policy.html", context)


# Territorial Page
def territorial_view(request):
    territorial = models.TerritorialAdmin.objects.all()
    context = {
        "territorial": territorial
    }
    return render(request, "blogs/pages/territorial_administrations/territorial_administrations.html", context)


# Investment Page
def investmentadmin_view(request):
    potential = models.InvestmentPotentialAdmin.objects.all()
    context = {
        "potential": potential
    }
    return render(request, "blogs/pages/investment_potential/investment_potential.html", context)


# Export Potential Page
def export_potential_view(request):
    export_potential = models.ExportPotentialAdmin.objects.all()
    context = {
        "export_potential": export_potential
    }
    return render(request, "blogs/pages/export_potential/export_potential.html", context)


# Export Implementation Page
def export_implementation_view(request):
    export_implementation = models.ExportImplementationAdmin.objects.all().first()
    context = {
        "export_implementation": export_implementation
    }
    return render(request, "blogs/pages/export_implementation/export_implementation.html", context)


# Export Law
def export_law_view(request):
    export_law = models.ExportLawAdmin.objects.all().first()
    context = {
        "export_law": export_law
    }
    return render(request, "blogs/pages/export_law/export_law.html", context)


# LEX UZ
def lex_uz_view(request):
    return redirect("https://lex.uz")


# Market Entry Strategies Page
def market_entry_strategies_view(request):
    market_entry_strategy = models.MarketEntryStrategies.objects.all().first()
    context = {
        "market_entry_strategy": market_entry_strategy
    }
    return render(request, "blogs/pages/market_entry_strategies/market_entry_strategies.html", context)


# Subsidaries Page
def subsidaries_view(request):
    subsidaries = models.SubsidariesAdmin.objects.all()
    context = {
        "subsidaries": subsidaries
    }
    return render(request, "blogs/pages/subsidaries/subsidaries.html", context)


# Subsidaries 2 Page
def subsidaries2_view(request):
    subsidaries2 = models.SubsidariesAdmin.objects.all()
    context = {
        "subsidaries2": subsidaries2
    }
    return render(request, "blogs/pages/subsidaries/subsidaries2.html", context)


# Leadership Page
def leadership_view(request):
    leadership = models.Staff.objects.filter(_type="directors")
    context = {
        "leadership": leadership,
        "type": "directors"
    }
    return render(request, "blogs/pages/about2/leadership.html", context)


def leadership_press_view(request):
    leadership = models.Staff.objects.filter(_type="press")
    context = {
        "leadership": leadership,
        "type": "press"
    }
    return render(request, "blogs/pages/about2/leadership.html", context)


# Investors page
def investors_view(request):
    investors = models.InvestorsAdmin.objects.all()
    context = {
        "investors": investors
    }
    return render(request, "blogs/pages/investors/investors.html", context)


# Exporters Page
def exporters_view(request):
    exporter = models.ExportersAdmin.objects.all().first()
    context = {
        "exporter": exporter
    }
    return render(request, "blogs/pages/exporters/exporters.html", context)


# Foreighn Representation Page
def foreighn_view(request):
    foreigns = models.ForeighnAdmin.objects.all()
    context = {
        "foreigns": foreigns
    }
    return render(request, "blogs/pages/foreighn_representations/foreign_representations.html", context)


def foreighn_branch_view(request, branch_name):
    branch_name = branch_name + "/"
    foreign = models.ForeighnAdmin.objects.filter(menu_item__link=branch_name).first()
    context = {
        "foreign": foreign
    }
    return render(request, "blogs/pages/foreighn_representations/branch.html", context)


# Company Types Page
def companys_types_view(request):
    company_types = models.CompanyTypes.objects.all()
    context = {
        "company_types": company_types
    }
    return render(request, "blogs/pages/menu_companys/company_types.html", context)


# Menu Companys Page
def menu_companys_view(request, type_slug):
    stir = request.GET.get("stir", None)
    company_type = models.CompanyTypes.objects.filter(slug=type_slug).first()
    context = {
        "company_type": company_type
    }
    return render(request, "blogs/pages/menu_companys/detail.html", context)


# News List Page
class NewsListView(generic.ListView):
    template_name = "blogs/pages/news/list.html"
    model = models.Post
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'posts'

    def get_queryset(self):
        return self.model.objects.filter(status='published')


# News detail Page
class NewsDetailView(generic.DetailView):
    template_name = "blogs/pages/news/detail.html"
    queryset = models.Post.published.all()
    context_object_name = 'post'


# Static Content Page
class StaticContentView(generic.DetailView):
    template_name = "blogs/pages/static_content/detail.html"
    queryset = models.StaticContent.objects.all()
    slug_url_kwarg = 'slug'


# Statistic List Page
class StatisticListView(generic.ListView):
    template_name = "blogs/pages/statistics/list.html"
    model = models.Statistic
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'items'


# Statistic Detail Page
class StatisticDetailView(generic.DetailView):
    template_name = "blogs/pages/statistics/detail.html"
    queryset = models.Statistic.objects.all()
    context_object_name = 'item'


# Tender List Page
class TenderListView(generic.ListView):
    template_name = "blogs/pages/tender/list.html"
    model = models.Tender
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'tenders'

    def get_queryset(self):
        return self.model.objects.filter()


# Tender Detail Page
class TenderDetailView(generic.DetailView):
    template_name = "blogs/pages/tender/detail.html"
    queryset = models.Tender.published.all()
    context_object_name = 'tender'


# Product List page
class ProductListView(generic.ListView):
    template_name = "blogs/pages/product/product_list.html"
    model = models.ProductCategory
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'categories'

    def get_queryset(self):
        return self.model.objects.filter()



def ProductItemView(request, _id):
    products = Product.objects.filter(category__id=_id)
    context = {
        "products": products
    }
    return render(request, "blogs/pages/product/item.html", context)


# Membership List Page
class MembershipListView(generic.ListView):
    template_name = "blogs/pages/membership/list.html"
    model = models.Product
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'memberships'

    def get_queryset(self):
        return self.model.objects.filter()


# Membership Detail Page
class MembershipDetailView(generic.DetailView):
    template_name = "blogs/pages/membership/detail.html"
    context_object_name = 'membership'


# Vacancy List Page
class VacancyListView(generic.ListView):
    template_name = "blogs/pages/vacancy/vacancy_list_view.html"
    model = models.Vacancy
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'vacancy'

    def get_queryset(self):
        return self.model.objects.filter()


# Legal Document List Page
class LegalDocumentListView(generic.ListView):
    template_name = "blogs/pages/legaldocument/list.html"
    model = models.LegalDocument
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'legal'

    def get_queryset(self):
        return self.model.objects.filter()


# Legal Documment Detail Page
class LegalDocumentView(generic.DetailView):
    template_name = "blogs/pages/legaldocument/detail.html"
    queryset = models.LegalDocument.objects.all()
    slug_url_kwarg = 'slug'


# Gallery List Page
class GalleryListView(generic.ListView):
    template_name = "blogs/pages/gallery/indexG.html"
    model = models.GalleryCategory
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'gallery'

    def get_queryset(self):
        return self.model.objects.filter()


# Gallery List Page
def GalleryImagesView(request, _id):
    context = {
        "images": models.GalleryImage.objects.filter(category__id=_id)
    }

    return render(request, "blogs/pages/gallery/images.html", context)


# Media List View
class MediaListView(generic.ListView):
    template_name = "blogs/pages/video/index.html"
    model = models.Media
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'media'

    def get_queryset(self):
        return self.model.objects.filter()


# FAQ List Page
class FAQListView(generic.ListView):
    template_name = "blogs/pages/faq/list_view.html"
    model = models.FAQ
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'faqs'

    def get_queryset(self):
        return self.model.objects.filter()


# Virtual Reception Page
def virtual_reception_view(request):
    form = VirtualReceptionForm()

    if request.method == "POST":
        form = VirtualReceptionForm(request.POST, request.FILES)
        if form.is_valid():
            vr = form.save(commit=False)
            vr.save()
            print(vr.id)
            return redirect(reverse("blogs:index"))
        else:
            return HttpResponse(str(form.errors))
    
    context = {
        "form": form
    }
    return render(request, "blogs/pages/virtual_reception/virtual_reception_form.html", context)


# Enterpreneurs List Page
class EntrepreneursListView(generic.FormView):
    template_name = "blogs/pages/for_entrepreneurs/entrepreneurs.html"
    form_class = forms.ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['number'] = "entrepreneurs"
        return context


# Membership Page
class MembershipProcedureListView(generic.ListView):
    template_name = "blogs/pages/membership_procedure/membership_procedure.html"
    model = models.FAQ

    def get_queryset(self):
        return self.model.objects.filter()


# Exhibitions List page
class ExhibitionListView(generic.ListView):
    template_name = "blogs/pages/exhibition/exhibition_list.html"
    model = models.Exhibition
    paginate_by = CONST_PAGINATOR_NUMBER
    context_object_name = 'exhibitions'

    def get_queryset(self):
        return self.model.objects.filter()


# Exhibitions Paga
class ExhibitionDetailView(generic.DetailView):
    template_name = "blogs/pages/exhibition/exhibition_detail.html"
    queryset = models.Exhibition.published.all()
    context_object_name = 'exhibition'


# Contact Page
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['message']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
            messages.success(request,
                             'Thank you for your inquiry. Your contact information and message was successfully submitted.')
            return render(request, 'blogs/pages/contact_page/contact_form.html')
        else:
            for error in form.errors:
                messages.error(request, f"{error}: {form.errors[error][0]}")
    form = ContactForm()
    context = {'form': form}
    return render(request, 'blogs/pages/contact_page/contact_form.html', context)



def foreighn_representation_links(request):
    links = models.ForeignRepresentativeLinks.objects.all()
    return render(request, "blogs/pages/foreighn_representations/links.html", {"links": links})


def foreighn_representation_items(request, slug):
    items = models.ForeignRepresentativeItems.objects.filter(link__slug=slug)
    return render(request, "blogs/pages/foreighn_representations/items.html", {"items": items})