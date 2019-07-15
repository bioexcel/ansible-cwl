# Ansible scripts for installing CWL engines

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


## Running an implementation

### CWL

```
cd ~/cwl_test
bin/actvate 
toil-cwl-runner example.cwl example-job.yaml
```
### Toil

```
cd ~/toil_test
bin/actvate 
toil-cwl-runner example.cwl example-job.yaml
```

### Reana

? To do

### Airflow

```
cd ~/airflow_test
source bin/activate
cwl-airflow init
(airflow scheduler &> /dev/null &) && (airflow webserver&> /dev/null &) && cwl-airflow submit example.cwl example-job.yaml
```

