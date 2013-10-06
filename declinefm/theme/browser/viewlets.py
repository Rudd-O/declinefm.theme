from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase

from zope.component.hooks import getSite

class SplashViewlet(ViewletBase):
    _render = ViewPageTemplateFile('splash.pt')

    def update(self):
        self.splash_text = getSite()['front-page-elements']['splash']
        pass

    def render(self):
        """ Render viewlet only in the front page"""
        if getSite().__class__ == self.context.__class__:
            # Call parent method which performs the actual rendering
            return self._render()
        else:
            # No output when the viewlet is disabled
            return ""

class MissionViewlet(ViewletBase):
    render = ViewPageTemplateFile('mission.pt')

    def update(self):
        self.mission = getSite()['front-page-elements']['mission']
        pass

class SocialViewlet(ViewletBase):
    render = ViewPageTemplateFile('social.pt')

    def update(self):
        self.social = getSite()['front-page-elements']['social']
        pass
