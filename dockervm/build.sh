RESOURCEGROUP=linuxconf
SERVERNAME=pyvm2019
DNSNAME=$SERVERNAME.southafricanorth.cloudapp.azure.com

echo "$RESOURCEGROUP | $SERVERNAME | $DNSNAME"

az group create -n $RESOURCEGROUP -l southafricanorth

az vm create --name $SERVERNAME -l southafricanorth -g $RESOURCEGROUP --image Canonical:UbuntuServer:18.04-LTS:latest --public-ip-address-dns-name $SERVERNAME --public-ip-address-allocation static --size Standard_B2ms --custom-data cloud-init.yml --generate-ssh-keys

