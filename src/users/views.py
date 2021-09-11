from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView, FormView, ListView, TemplateView
from django.db.models import Q

from commons.utils import PaginatedListView
from estates.models import UserEstate, Estate
from users.forms import UserModelForm, UserDjangoCreationForm, UserDjangoModelForm
from users.mixings import ValidAuthorMixin
from users.models import User


class IndexView(PaginatedListView):
    template_name = 'index/index.html'
    model = UserEstate
    paginate_by = 5

    def get_queryset(self):
        queryset = super(IndexView, self).get_queryset()
        search = self.request.GET.get('search')
        estate_type = self.request.GET.get('estate_type')
        if search:
            queryset = queryset.filter(Q(user__document__icontains=search) |
                                       Q(user__user__first_name__icontains=search) |
                                       Q(user__user__username__icontains=search) |
                                       Q(user__user__last_name__icontains=search) |
                                       Q(estate__catastral_id__icontains=search) |
                                       Q(estate__name__icontains=search) |
                                       Q(estate__address__icontains=search)
                                       )
        if estate_type and estate_type != "------":
            print("NO ES")
            queryset = queryset.filter(estate__type=estate_type)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['url_search'] = self.request.get_full_path()
        context['estate_type'] = Estate.TYPE
        return context


class UserRegisterView(CreateView):
    template_name = 'user/register.html'
    model = User
    form_class = UserModelForm
    second_form_class = UserDjangoCreationForm

    def get_context_data(self, **kwargs):
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        if not 'form_user' in context:
            context['form_user'] = self.second_form_class
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        form_user = self.second_form_class(request.POST)

        if form.is_valid() and form_user.is_valid():
            return self.form_valid(form, form_user)
        else:
            return self.form_invalid(form, form_user)

    def form_valid(self, form, form_user=None):
        user = form_user.save()
        self.object = form.save(commit=False)
        self.object.user = user
        self.object.save()
        messages.success(self.request, 'Registro realizado correctamente!')
        login(
            self.request, self.object.user,
            backend='django.contrib.auth.backends.ModelBackend'
        )
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

    def form_invalid(self, form, form_user=None):
        return self.render_to_response(
            self.get_context_data(**{'form': form, 'form_user': form_user}),
            status=400
        )


class UserUpdateView(LoginRequiredMixin, ValidAuthorMixin, FormView):
    template_name = 'user/edit-profile.html'
    model = User
    form_class = UserModelForm
    second_form_class = UserDjangoModelForm

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(
            **self.get_form_kwargs(), instance=self.author_instance
        )

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        if not 'form_user' in context:
            context['form_user'] = self.second_form_class(
                instance=self.author_instance.user
            )
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form_user = self.second_form_class(
            request.POST, instance=self.author_instance.user
        )
        if form.is_valid() and form_user.is_valid():
            return self.form_valid(form, form_user)
        else:
            return self.form_invalid(form, form_user)

    def form_valid(self, form, form_user=None):
        user = form_user.save()
        self.object = form.save()
        self.object.save()
        messages.success(self.request, 'Tu perfil ha sido actualizado.')
        return HttpResponseRedirect(reverse('users:index'))

    def form_invalid(self, form, form_user=None):
        return self.render_to_response(
            self.get_context_data(**{'form': form, 'form_user': form_user}),
            status=400
        )
