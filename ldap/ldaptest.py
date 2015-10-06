#!/usr/bin/env python

import ldap,sys,time
import ldap.modlist as modlist
from ldap.controls import SimplePagedResultsControl

# con = ldap.initialize('ldap://iwtestb01:1389')
con = ldap.initialize('ldap://iwpostnlmwb01:1389')
# con.simple_bind_s("cn=Directory Manager","Pass*w0rd!")
con.simple_bind_s("cn=Directory Manager","Uywj!2Kr!GiA")
# print con.whoami_s()

ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)
ldap.set_option(ldap.OPT_REFERRALS, 0)
con.protocol_version = 3

# base_dn = "dc=test,dc=iwelcome,dc=com"
base_dn = "dc=postnlmw,dc=iwelcome,dc=com"
retrieveAttributes = ["dn"]
searchFilter = "(&(objectClass=top)(objectClass=iwelcomeUser))"
t0=time.time()
print t0
uids = con.search_s(base_dn, ldap.SCOPE_SUBTREE, searchFilter, retrieveAttributes)
print time.time()-t0


old_value = {"objectClass": ["top", "person", "organizationalPerson", "inetOrgPerson", "sunFMSAML2NameIdentifier", "iwelcomeUser"]}
new_value = {"objectClass": ["top", "person", "organizationalPerson", "inetOrgPerson", "sunFMSAML2NameIdentifier", "iwelcomeUser", "iplanet-am-user-service"]}
 
mod = modlist.modifyModlist(old_value, new_value)

cnt=0
t0=time.time()
for uid in uids:
	# print uid[0]
	cnt+=1
	con.modify_s(uid[0], mod)
	if cnt>100:
		print time.time()-t0
		t0=time.time()
		cnt=0