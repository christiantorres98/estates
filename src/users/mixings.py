from django.contrib.auth.mixins import UserPassesTestMixin

from commons.templatetags.core_tags import get_current_user


class ValidAuthorMixin(UserPassesTestMixin):
    author_instance = None

    def test_func(self):
        self.author_instance = get_current_user(self.request)
        if self.author_instance:
            return True
        else:
            return False