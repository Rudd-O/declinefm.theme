from collections import deque
from datetime import datetime

import transaction
from zope.app.component.hooks import setSite
from Testing.makerequest import makerequest
from AccessControl.SecurityManagement import newSecurityManager


site_id = 'Plone'     # adjust to match your Plone site object id.
admin_user = 'admin'  # usually 'admin', probably won't need adjusting
app = makerequest(app)
site = app["declinefm.com"]["declinefm.com"]
setSite(site)
user = app.acl_users.getUser(admin_user).__of__(site.acl_users)
newSecurityManager(None, user)


def treeWalker(root):
    # stack holds (parent, id, obj) tuples
    stack = deque([(None, None, root)])
    while stack:
        parent, id, next = stack.popleft()
        try:
            stack.extend((next, id, child) for id, child in next.objectItems())
        except AttributeError:
            # No objectItems method
            pass
        yield parent, id, next


#from collective.flowplayer.interfaces import IFlowPlayerSite

count = 0
for parent, id, obj in treeWalker(site):
    print "inspecting", id
    if obj.getLayout() == "flowplayer":
         obj.setLayout("file_view")
#    if IFlowPlayerSite.providedBy(obj):
#        print 'flowplayersite provided by', id
#        obj._p_changed = True  # mark it as changed, force a commit
#        count += 1
#        if count % 100 == 0:
#            # flush changes so far to disk to minimize memory usage
#            transaction.savepoint(True)
#            print '{} - Processed {} items'.format(datetime.now(), count)

transaction.commit()
