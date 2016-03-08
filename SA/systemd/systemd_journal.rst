systemd logging system - journal

journal will log

  - kmsg
  - syslog
  - stdout/stderr of system service
  - audit

usage

  - journal --list-boots: show all boot number, timestamp ... 
  - journal -k: only dmesg (kernel log)
  - journal -k -b -1: dmesg of previous boot

related 

  - man journalctl
  - man systemd-journald.service


