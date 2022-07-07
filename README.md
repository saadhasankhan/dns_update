## This is what I can do

dns_update --help
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
