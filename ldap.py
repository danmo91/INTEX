#!/user/bin/env python3
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'chf.settings'
import django
django.setup()


#regular imports
import homepage.models as hmod
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO, SEARCH_SCOPE_WHOLE_SUBTREE


# # create server, make connection change server to cheritagefoundation.com later
# s = Server('128.187.61.56', port=12345, get_info=GET_ALL_INFO)
#
# c = Connection(
#       s,
#       auto_bind = True,
#       user = 'dan@cheritagefoundation.local',
#       password= 'Password1',
#       authentication=AUTH_SIMPLE,
#       client_strategy=ASYNC
#     )

# create server, make connection change server to cheritagefoundation.com later
s = Server('www.cheritagefoundation.com', port=12345, get_info=GET_ALL_INFO)

c = Connection(
      s,
      auto_bind=True,
      user = 'bri@cheritagefoundation.local',
      password= 'TS1989_5167',
      authentication=AUTH_SIMPLE,
      client_strategy=STRATEGY_SYNC
    )

search_results = c.search(
  search_base = 'CN=Users,DC=cheritagefoundation,DC=local',
  search_filter = '(samAccountName=bri)',
  search_scope = SEARCH_SCOPE_WHOLE_SUBTREE,
  attributes = [
    'givenName',
    'sn',
    'l',
    'streetAddress',
    'postalCode',
    'st',
    'mobile',
    'info',
  ])

if search_results:

    user_info = c.response[0]['attributes']

    print('user_info:', user_info)
    print('first_name:', user_info['givenName'])
    print('last_name:', user_info['sn'])
    print('city:', user_info['l'])
    print('street:', user_info['streetAddress'])
    print('zip_code:', user_info['postalCode'])
    print('state:', user_info['st'])
    print('phone:', user_info['mobile'])
    print('email:', user_info['info'])
