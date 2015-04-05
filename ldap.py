#!/user/bin/env python3
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'chf.settings'
import django
django.setup()


#regular imports
import homepage.models as hmod
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO


# create server, make connection change server to cheritagefoundation.com later
s = Server('128.187.61.56', port=12345, get_info=GET_ALL_INFO)

c = Connection(
      s,
      auto_bind = True,
      user = 'dan@cheritagefoundation.local',
      password= 'Password1',
      authentication=AUTH_SIMPLE,
      client_strategy=STRATEGY_SYNC
    )


print('info:', s.info)
print('returned:', c)
print('user:', c.user)
