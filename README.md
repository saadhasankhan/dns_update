What am I
_________

May be I will grow up into something more, but right now I am a single tool, ```dns_update```, that will let you add, create and update A and CNAME records in ops.cloud.cengage.com.

I install as a utility with pip.

I look like this:

MABOSSKHAN-M1:evergreen skhan$ dns_update --help
usage: dns_update [-h] -e ENVIRONMENT -n NAME -v VALUE -a
                  {CREATE,DELETE,UPSERT} -t {A,CNAME} [--TTL TTL]

Change records in route53/ops.cloud.cengage.com

optional arguments:
  -h, --help            show this help message and exit

required named arguments:
  -e ENVIRONMENT, --environment ENVIRONMENT
                        Enter AWS Profile
  -n NAME, --name NAME  Record name
  -v VALUE, --value VALUE
                        Record value, IP for A records, a host FQDN for CNAME
  -a {CREATE,DELETE,UPSERT}, --action {CREATE,DELETE,UPSERT}
                        Create, Update or Delete
  -t {A,CNAME}, --type {A,CNAME}
                        A or CNAME

optional named arguments:
  --TTL TTL

Instructions
____________

> Install with pip

- git clone
- in clones directory execute ```pip install```
- That should work but you should probably do it in a virtualenv.