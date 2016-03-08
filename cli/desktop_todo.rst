common
------

- WIFI connect
- battery
- screensaver(lock) & hibernate

  - https://wiki.archlinux.org/index.php/I3#Shutdown.2C_reboot.2C_lock_screen
  ::

      $ i3lock
      $ systemctl suspend

- sound

  - http://unix.stackexchange.com/a/67535
  ::

    pactl, pacmd
    $ pactl list short sinks
    $ pactl list short sources

- touchpad toggle
- light change
- volume change::

  Volume level     : 25 %
  Is sink muted    : no
  Is source muted  : no
  Detected sink    : 1
  Detected source  : 2
  Pulse version    : 7.1

  # Volume level
  $ pulseaudio-ctl up/down
  $ pulseaudio-ctl up/down n
  $ pulseaudio-ctl set n

  $ pulseaudio-ctl mute/mute-input
  
  Optionally, redefine an upper threshold in /home/susu/.config/pulseaudio-ctl/config
  

- input method

- multiple screen or display

me
--

- window directory mount::

  mount -t ntfs -o default_permissions /dev/sda3 /run/media/susu/OS
  mount -t ntfs -o default_permissions /dev/sda5 /run/media/susu/DATA

- file manager

  - preview of picture/video

Misc
----
libinoify & i3: https://faq.i3wm.org/question/121/whats-a-good-notification-daemon-for-i3/
