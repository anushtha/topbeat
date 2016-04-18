

import os
os.system("curl -L -O https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.1/elasticsearch-2.3.1.tar.gz")

os.system("tar -xvf elasticsearch-2.3.1.tar.gz")

os.system("cd elasticsearch-2.3.1/bin")

os.system("./elasticsearch")

os.system("./elasticsearch --cluster.name first_project --node.name Anustha")
