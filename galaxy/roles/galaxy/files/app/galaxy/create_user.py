# this script is based on @jmchilton's preseed.py (https://gist.github.com/jmchilton/1979583)
# it creates the admin user and sets an API key for it.
from scripts.db_shell import *

admin_user = User("galaxy@commonwl.org")
admin_user.set_password_cleartext("galaxy")
sa_session.add(admin_user)
sa_session.flush()

admin_key = APIKeys()
admin_key.user_id = admin_user.id
print 'Setting admin id as %s' % admin_user.id
admin_key.key = '111111111111111111111'
sa_session.add( admin_key )
sa_session.flush()
