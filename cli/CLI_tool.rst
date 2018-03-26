- message show

  - cat -n: show line number
  - less(more, most): pager for viewing more-than-one-page CLI output 

NTP

::

    $ date
    $ date -u  # UTC time

    # start ntpd server
    $ sudo systemctl start ntpd.service  # [archlinux]
    # check ntpd server
    $ ntpq -p

    # sync manually without ntp server
    $ ntpd -q -p <ntp_server>

  - timezone: https://wiki.archlinux.org/index.php?title=Time&redirect=no#Time_zone

    - soft link ``/usr/share/zoneinfo/<zone>/<sub_zone>`` to ``/etc/timezone``

mount

basic::

    mount device dir
    mount [-t fstype] device dir
    mount [-t fstype] [-o options] device dir
