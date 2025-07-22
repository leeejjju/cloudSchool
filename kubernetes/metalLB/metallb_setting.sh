# kubernetes에 설치 
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.13.10/config/manifests/metallb-native.yaml

# 설치 확인 
kubectl get all -n metallb-system

# IP 대역 설정 
cat <<EOF | kubectl apply -f -
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
 name: my-ippool
 namespace: metallb-system
spec:
 addresses:
 - 192.168.49.2-192.168.49.50
EOF

# 로드밸런서 IP 풀 허용 : IP풀을 가지고 광고할 수 있도록 설정 
cat <<EOF | kubectl apply -f -
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
 name: my-l2-advertise
 namespace: metallb-system
spec:
 ipAddressPools:
 - my-ippool
EOF
# 위 명령어의 Yaml버전. 선택해서 사용
# kubectl apply -f metalb_config.yaml
