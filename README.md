1. Software installation.

Virtualbox: https://www.virtualbox.org/wiki/Downloads

Vagrant: https://www.vagrantup.com/downloads.html

Ansible: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html

2. Clone repository
```
git clone https://github.com/anna-dmitrieva/test-minio.git
cd test-minio
```
3. Generate ssh key for run ansible ad hoc
```
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
4. Run Vagrantfile
``` 
vagrant up 
```
When installing, you will need to select a network adapter.

5. Add user to hosts:
```
ansible all -m user -a "name=user1 group=minio password=cryptedpass" -i ./inventory
```
6. Copy file to minio bucket
```
ansible minio1 -m copy -a "src=~/test-minio/test.jpg dest=/data/minio/mybucketname/" -i inventory
```
7. Run script for download this file
```
python main.py 
```
