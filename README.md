# Ansible scripts for installing CWL engines

Caution, these are currently setup for CentOS7 only and insome cases use a specific username.

## Introduction

A series of playbooks to install and test various [implementations of CWL](https://www.commonwl.org/#Implementations)


## Installation

### CWL Runner

```
ansible-playbook cwl.yml
```

### Toil

```
ansible-playbook toil.yml
```

### Reana

```
ansible-playbook reana.yml
```

### Airflow

```
ansible-playbook airflow.yml
```

### Cromwell

```
ansible-playbook cromwell.yml
```

### Galaxy
```
ansible-playbook -i inventory galaxy.yml -k -K --extra-vars 'my_pass=<your_hashed_root_password>'
```



## Running an implementation

### CWL

```
cd ~/cwl_test
source bin/actvate 
cwl-runner example.cwl example-job.yaml
```
### Toil

```
cd ~/toil_test
source bin/actvate 
toil-cwl-runner example.cwl example-job.yaml
```

### Reana

? To do
? Not working.  Install seems fine, but does not start.

```
helm init
# deploy new cluster and check progress
reana-cluster init --traefik
reana-cluster status
# set environment variables for reana-client
eval $(reana-cluster env --include-admin-token) # since you are admin
cd ~/reana_test
source bin/actvate
reana-client create -n my-analysis
export REANA_WORKON=my-analysis
# upload input code and data to the workspace
reana-client upload
# start computational workflow
reana-client start
# check its progress
reana-client status
# list workspace files
reana-client ls
# download output results
reana-client download
```

### Airflow

```
cd ~/airflow_test
source bin/activate
cwltool example.cwl example-job.yaml
```

### Cromwell

```
cd ~/cromwell_test
conda activate cromwell_test
cromwell run example.cwl -i example-job.yaml
```

... #cwl-airflow init
... #(airflow scheduler &> /dev/null &) && (airflow webserver&> /dev/null &) && cwl-airflow submit example.cwl example-job.yaml


