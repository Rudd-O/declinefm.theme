from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.component.hooks import getSite

class CustomFrontpageView(BrowserView):

    template = ViewPageTemplateFile('custom_frontpage_view.pt')

    def __call__(self):
        """"""
        self.splash_text = getSite()['front-page-elements']['splash']
        return self.template()