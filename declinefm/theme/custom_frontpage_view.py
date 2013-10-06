from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class CustomFrontpageView(BrowserView):

    template = ViewPageTemplateFile('custom_frontpage_view.pt')

    def __call__(self):
        """"""
        self.blog_posts = getattr(self.context, 'blog')
        self.news_posts = getattr(self.context, 'news')
        self.archive_posts = getattr(self.context, 'archive')
        return self.template()