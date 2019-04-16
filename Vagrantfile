BRIDGE_NET="192.168.1."
INTERNAL_NET="192.168.15."
DOMAIN="test.net"
servers=[
  {
    :hostname => "minio-host1." + DOMAIN,
    :ip => BRIDGE_NET + "154",
    :ip_int => INTERNAL_NET + "2",
    :ram => 512,
    :hdd_name => "hdd.vdi",
    :hdd_size => "10000"
  },
  {
    :hostname => "minio-host2." + DOMAIN,
    :ip => BRIDGE_NET + "155",
    :ip_int => INTERNAL_NET + "3",
    :ram => 512,
    :hdd_name => "hdd2.vdi",
    :hdd_size => "10000"
  },
  {
    :hostname => "minio-host3." + DOMAIN,
    :ip => BRIDGE_NET + "156",
    :ip_int => INTERNAL_NET + "4",
    :ram => 512,
    :hdd_name => "hdd3.vdi",
    :hdd_size => "10000"
  }, 
  {
    :hostname => "minio-host4." + DOMAIN,
    :ip => BRIDGE_NET + "157",
    :ip_int => INTERNAL_NET + "5",
    :ram => 512,
    :hdd_name => "hdd4.vdi",
    :hdd_size => "10000"
  }
]

Vagrant.configure(2) do |config|
    servers.each do |machine|
        config.vm.define machine[:hostname] do |node|
            config.vm.box = "ubuntu/xenial64"
            node.vm.hostname = machine[:hostname]
            node.vm.network "public_network", ip: machine[:ip]
            node.vm.network "private_network", ip: machine[:ip_int], virtualbox__intnet: "intnet"
            node.vm.provider "virtualbox" do |vb|
                vb.customize ["modifyvm", :id, "--memory", machine[:ram]]
                vb.customize ["createhd", "--filename", machine[:hdd_name], "--size", machine[:hdd_size]]
            config.vm.provision "ansible" do |ansible|
                ansible.verbose = "v"
                ansible.playbook = "playbook.yml"
                end
            end
        end
    end
    # servers.each do |machine|
    #     config.vm.provision "ansible" do |ansible|
    #         ansible.verbose = "v"
    #         ansible.playbook = "playbook2.yml"
    #     end
    # end    
end