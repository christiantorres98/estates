from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from commons.utils import PaginatedListView
from estates.forms import EstateForm
from estates.models import UserEstate
from users.mixings import ValidAuthorMixin


class UserEstateListView(ValidAuthorMixin, PaginatedListView):
    template_name = 'estates/list.html'
    model = UserEstate
    paginate_by = 5

    def get_queryset(self):
        queryset = self.model.objects.filter(user=self.author_instance)
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(UserEstateListView, self).get_context_data(**kwargs)
        context['url_search'] = self.request.get_full_path()
        return context


class EstateCreateView(ValidAuthorMixin, CreateView):
    template_name = 'estates/create.html'
    model = UserEstate
    form_class = EstateForm
    success_url = reverse_lazy('estates:estate-list')

    def form_valid(self, form):
        user_logged = self.author_instance
        self.object = form.save(commit=False)
        self.object.save()
        UserEstate.objects.create(
            estate=self.object,
            user=user_logged
        )
        messages.success(self.request, 'Predio creado correctamente')
        return HttpResponseRedirect(self.get_success_url())
