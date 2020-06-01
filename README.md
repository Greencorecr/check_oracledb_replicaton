# check_oracledb_replicaton
Nagios core and Nagios XI commands for reading the replication status in an Oracle DB cluster

## Description

Modern versions of Oracle use ACFS (cluster filesystem) as a replication subsystem for databases. This custom command for Nagios core and Nagios XI, checks the status of the ACFS replication.

## Install

### From NRPE host
- Remove the ``face_acfsutil.py`` script from line 4 of the ``check_oracledb_replication.py`` script, and replace with similar to ``/usr/sbin/acfsutil repl info -c /ACFS_DIR/".
- Copy the ``check_oracledb_replication.py`` script to ``/usr/local/nagios/libexec/`` on the NRPE host, with execution permissions, and root:nagios owner. Before moving on, check that you can run as nagios user the script and that it prints a correct anwer.
- Add a new file to ``/usr/local/nagios/etc/nrpe/`` with a content like:
```
command[check_oracledb_replication]=/usr/local/nagios/libexec/check_oracledb_replication $ARG1$
```
- Add a sudoers file to ``/etc/sudoers.d/`` with the appropriate content, as it is possible that the tool needs privileges. Remeber to configure those permissions to user ``nagios``

#### Tests

1. Run the check script, manually with python3 on the CLI
2. Run nrpe from localhost to ejecute the plugin

### From Nagios host

Add a new service where you use the ``check_nrpe`` plugin to execute the remote command that we configured on the NRPE host. Run a test check from the CLI or the web interface. If anything fails, double check the test on the side of the NRPE host.

Now, for this service add the hosts or hostsgroups that you need to monitor, plus any notification configuration needed.
Agregar servicio NRPE, con el comando agregado

## Tools

fake_acfsutil.py: For testing only. It will simulate how the cool acfsutil responds with argumets "repl info -c /dir"
check_oracledb_replication.py: Check command for nagios.

## TODO

- Run acfsutil once
- Accept directory to monitor as an argument. For the moment you need to copy multiple check scripts with different ``acfs_command`` values.

## About

This tool was written for a client of [Greencore Solutions](https://www.greencore.co.cr/). Please contact info@greencore.co.cr for any comercial inquiries.
