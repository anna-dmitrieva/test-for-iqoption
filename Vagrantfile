BRIDGE_NET="192.168.1."
INTERNAL_NET="192.168.15."
DOMAIN="test.net"
servers=[
  {
    :hostname => "minio1." + DOMAIN,
    :ip => BRIDGE_NET + "150",
    :ip_int => INTERNAL_NET + "1",
    :ram => 1000,
    :hdd_name => "db1_hdd.vdi",
    :hdd_size => "10000"
  },
  {
    :hostname => "minio2." + DOMAIN,
    :ip => BRIDGE_NET + "151",
    :ip_int => INTERNAL_NET + "2",
    :ram => 1000,
    :hdd_name => "db2_hdd.vdi",
    :hdd_size => "10000"
  },
  {
    :hostname => "minio3." + DOMAIN,
    :ip => BRIDGE_NET + "152",
    :ip_int => INTERNAL_NET + "3",
    :ram => 1000,
    :hdd_name => "db3_hdd.vdi",
    :hdd_size => "10000"
  }
]

Vagrant.configure(2) do |config|
    servers.each do |machine|
        config.vm.define machine[:hostname] do |node|
            config.vm.box = "ubuntu/xenial64"
            node.vm.hostname = machine[:hostname]
            node.vm.network "public_network", ip: machine[:ip], bridge: 'Intel(R) Ethernet Connection (2) I219-V'
            node.vm.network "private_network", ip: machine[:ip_int], virtualbox__intnet: "intnet"
            node.vm.provider "virtualbox" do |vb|
                vb.customize ["modifyvm", :id, "--memory", machine[:ram]]
                vb.customize ["createhd", "--filename", machine[:hdd_name], "--size", machine[:hdd_size]]
            end
        end
    end
end