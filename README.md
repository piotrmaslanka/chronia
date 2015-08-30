chronia
=======

You have a device that doesn't have RTC? That sucks.
The device sometimes won't have Internet access, and it can reboot, so you will be lost without time? That sucks even more.

Chronia to the rescue!
----------------------
On the one hand, it's a NTP client, so it will sync your time. If it fails to, it will synchronize the time from the filesystem,
so that it will be *reasonably* recent (assuming short power fails).

Chronia was thought as a NTP-replacement service for Raspberry Pi in situations that Pi would spontaneously reboot and, upon
awakening, discover it was cut off from WAN. Chronia will sync time each interval (default a minute) with the filesystem,
so that when it wakes up and fails to roll NTP, it will get time from there. When WAN finally recovers, Chronia will
get time from there.

tl;dr - use Chronia when you think that time possibly late by some period is better than no time at all.