from django.utils.translation import ugettext_lazy as _

from grappelli.dashboard import modules, Dashboard

from interim_cms.modules import ExampleModule, StaticModule


class LeftDashboard(Dashboard):

    def init_with_context(self, context):
        self.children = []

        self.children.append(modules.ModelList(
            _('Day to day'),
            column=1,
            collapsible=False,
            exclude=('django.contrib.auth.*',),
        ))

        self.children.append(modules.ModelList(
            _('Access control'),
            column=1,
            collapsible=False,
            models=('django.contrib.auth.*',),
        ))


class CenterDashboard(Dashboard):

    def init_with_context(self, context):
        self.children = []

        self.children.append(StaticModule(
            title="Welcome",
            collapsible=False,
            template="interim_cms/welcome.html",
        ))


class RightDashboard(Dashboard):

    class Media:
        js = (
            "interim_cms/js/cms.js",
            "interim_cms/js/jquery.cookie.js",
        )
        css = {
            "all": ("interim_cms/css/cms.css", "interim_cms/css/skin.css")
        }

    def init_with_context(self, context):
        self.children = []

        if "empty" in context["request"].GET:
            return

        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=5,
            collapsible=False,
            column=1,
        ))

        if context["request"].user.is_authenticated():
            self.children.append(ExampleModule(
                title="Foo",
            ))
