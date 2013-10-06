from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class CustomFrontpageView(BrowserView):

    template = ViewPageTemplateFile('custom_frontpage_view.pt')

    def __call__(self):
        """"""
        return self.template()