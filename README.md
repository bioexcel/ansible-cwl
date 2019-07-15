# Ansible scripts for installing CWL engines

## Introduction

A series of playbooks to install and test various [implementations of CWL](https://www.commonwl.org/#Implementations)

## CWL Reference Runner

### Installation

Installation is simple, without issues for CWL.  Just issue:

```
ansible-playbook cwl.yml
```

This should ask for a root password to run (note, this uses `su` and not `sudo`).

### Running

```
cd ~/cwl_test
bin/actvate 
toil-cwl-runner example.cwl example-job.yaml
```


## Toil

### Installation

Installation is simple, without issues for toil.  Just issue:

```
ansible-playbook toil.yml
```

This should ask for a root password to run (note, this uses `su` and not `sudo`).

### Running

```
cd ~/toil_test
bin/actvate 
toil-cwl-runner example.cwl example-job.yaml
```
