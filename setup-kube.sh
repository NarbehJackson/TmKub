curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add
apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
sudo apt -qq update
apt-get install -y kubelet kubeadm kubectl kubernetes-cni --no-install-recommends

kubeadm init --pod-network-cidr=10.244.0.0/16

mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config

kubectl apply -f https://docs.projectcalico.org/v3.9/manifests/calico.yaml

kubectl taint nodes $(hostname) node-role.kubernetes.io/master-