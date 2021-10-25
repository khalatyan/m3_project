from django.contrib.auth.models import Group, User, Permission

from objectpack.ui import ModelEditWindow, model_fields_to_controls, anchor100


class UserEditWindow(ModelEditWindow):

    def _init_components(self):
        super(ModelEditWindow, self)._init_components()
        self._controls = model_fields_to_controls(
            User, self)

    def _do_layout(self):
        super(ModelEditWindow, self)._do_layout()
        self.form.items.extend(list(map(anchor100, self._controls)))

    def set_params(self, params):
        super(ModelEditWindow, self).set_params(params)