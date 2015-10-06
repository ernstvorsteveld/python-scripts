import sys
import ldap
 
# If you're talking to LDAP, you should be using LDAPS for security!
LDAPSERVER='ldap://iwtestb01:1389'
BASEDN="dc=test,dc=iwelcome,dc=com"
LDAPUSER = 'cn=Directory Manager'
LDAPPASSWORD = 'Pass*w0rd!'
PAGESIZE = 1
ATTRLIST = ['uid']
SEARCHFILTER='uid=*'
 
# Ignore server side certificate errors (assumes using LDAPS and
# self-signed cert). Not necessary if not LDAPS or it's signed by
# a real CA.
ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_ALLOW)
# Don't follow referrals
ldap.set_option(ldap.OPT_REFERRALS, 0)
 
l = ldap.initialize(LDAPSERVER)
l.protocol_version = 3          # Paged results only apply to LDAP v3
try:
    l.simple_bind_s(LDAPUSER, LDAPPASSWORD)
except ldap.LDAPError as e:
    exit('LDAP bind failed: %s' % e)
 
# Initialize the LDAP controls for paging. Note that we pass ''
# for the cookie because on first iteration, it starts out empty.
lc = ldap.controls.SimplePagedResultsControl(ldap.LDAP_CONTROL_PAGE_OID, True,
                                             (PAGESIZE,''))
 
# This is essentially a placeholder callback function. You would do your real
# work inside of this. Really this should be all abstracted into a generator...
def process_entry(dn, attrs):
    """Process an entry. The two arguments passed are the DN and
       a dictionary of attributes."""
    print dn, attrs
 
# Do searches until we run out of "pages" to get from
# the LDAP server.
while True:
    # Send search request
    try:
        # If you leave out the ATTRLIST it'll return all attributes
        # which you have permissions to access. You may want to adjust
        # the scope level as well (perhaps "ldap.SCOPE_SUBTREE", but
        # it can reduce performance if you don't need it).
        msgid = l.search_ext(BASEDN, ldap.SCOPE_ONELEVEL, SEARCHFILTER,
                             ATTRLIST, serverctrls=[lc])
    except ldap.LDAPError as e:
        sys.exit('LDAP search failed: %s' % e)
 
    # Pull the results from the search request
    try:
        rtype, rdata, rmsgid, serverctrls = l.result3(msgid)
    except ldap.LDAPError as e:
        sys.exit('Could not pull LDAP results: %s' % e)
 
    # Each "rdata" is a tuple of the form (dn, attrs), where dn is
    # a string containing the DN (distinguished name) of the entry,
    # and attrs is a dictionary containing the attributes associated
    # with the entry. The keys of attrs are strings, and the associated
    # values are lists of strings.
    for dn, attrs in rdata:
        process_entry()
 
    # Look through the returned controls and find the page controls.
    # This will also have our returned cookie which we need to make
    # the next search request.
    pctrls = [
        c for c in serverctrls if c.controlType == ldap.LDAP_CONTROL_PAGE_OID
    ]
    if not pctrls:
        print >> sys.stderr, 'Warning: Server ignores RFC 2696 control.'
        break
 
    # Ok, we did find the page control, yank the cookie from it and
    # insert it into the control for our next search. If however there
    # is no cookie, we are done!
    est, cookie = pctrls[0].controlValue
    if not cookie:
        break
    lc.controlValue = (page_size, cookie)