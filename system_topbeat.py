"""
author @ Anustha Singh

"""
import os
os.system("curl -L -O https://download.elastic.co/beats/topbeat/topbeat_1.2.1_amd64.deb")
os.system("sudo dpkg -i topbeat_1.2.1_amd64.deb")

# configure topbeat
with open("/etc/topbeat/topbeat.yml", 'a') as f :
         if "elasticserach:" in f:
             f.write('hosts: ["localhost"]')

# now running a shell script to load this template

os.system("curl -XPUT 'http://localhost:9200/_template/topbeat' -d@/etc/topbeat/topbeat.template.json")
os.system("sudo /etc/init.d/topbeat start")

# for testing
os.system("curl -XGET 'http://localhost:9200/topbeat-*/_search?pretty")



