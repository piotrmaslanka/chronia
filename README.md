chronia
=======

You have a device that doesn't have RTC? That sucks.
The device sometimes won't have Internet access, and it can reboot, so you will be lost without time? That sucks even more.

What if your no-RTC device can't get on the Internet?
-----------------------------------------------------
Sometimes your no-RTC device will happen to reboot. Then, it will find out the hard way it has no Internet and no capability
to get current time.

Chronia was thought as a NTP supplement service for Raspberry Pi in situations that Pi would spontaneously reboot and, upon
awakening, discover it was cut off from WAN. Chronia will sync time each interval (default a minute) with the filesystem,
so that when it wakes up and fails to roll NTP, it will get time from there (correcting for uptime).

When WAN recovers, your system NTP client will synchronize the time properly. Chronia will notice this, and keep trailing
the proper time.

tl;dr - use Chronia when you think that time possibly late by some period is better than no time at all.

Recipe
------
Just run chronia alongside your NTP client. They will get together nicely.