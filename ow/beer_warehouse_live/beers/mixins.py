class AddMyBirthdayToContextMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['b_day'] = "Mi cumple es el 27 de agosto"
        return context
