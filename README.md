# Ansible scripts for installing CWL engines

## Introduction

A series of playbooks to install and test various [implementations of CWL](https://www.commonwl.org/#Implementations)

toil
----
Deploy and test:

```
ansible-playbook ansible-cwl/toil/playbook.yml && cd ~/toil_test && bin/activate && toil-cwl-runner example.cwl example-job.yaml
```
