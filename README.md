Firewall
=========

Graphical Firewall based on UFW created in python(using TKinter) that ease off the work of a network administrator to secure a network. The problem that the ‘FIREWALL’ aims, is to filter network packets according to some rules as set by the administrator. This tool scans a network packet for fields like source address, destination address, source port, destination port, service, protocol, flags(like SYN, ACK, FIN etc.) and other options(like fragmentation, physical address, length of payload, owner, connection options etc.). To provide all these filtering  facilities, the tool used the tables provided by the Linux kernel firewall (implemented as different Netfilter modules). The tool probes all the incoming, outgoing and forwarded network packets once it is enabled  in order to filter out or do as commanded by the administrator in case of a match. The tool aims to reduce human efforts required to filter and protect a particular network or a host as done using various packet scannin g and filtering techniques, by providing a automated graphical tool to do the same.  The need of this tool is for protecting and managing a network or a  host properly and efficiently in order to receive high throughput. Also the tool can be used to detect any potential attack or breach that may be attempted on a particular network or on any particular host by configuring it to generate custom warning messages when certain criteria is fulfilled. The need of this system exists because, even though functionalities pertaining to scanning and filtering the network have been in existence for such a long time, but still they require of huge man-power that can cause huge loss in time and varying consistency-levels, thus hampering the working efficiency of the network administration system. As this tool is Graphical thus it can be used with great ease without much difficulty.


SCANNED FIELDS
=================

Network packets are scanned for following key fields :

Addresses- Source Address and Destination Address 

Port Numbers- Source port and destination port numbers

Protocols- TCP, UDP, SCTP, ICMP, ESP, UDPLITE and AH.

Mask- Source-Address or Destination-Address mask.

Name- Source or Destination network  or  host name.

States- New, Established, Invalid, Ralated etc.

Interfaces- Name  of  an interface via which a packet was received  or is going to be sent.

Address type- Unicast,  Multicast, Broadcast, Anycast,  Unreachable, Blackhole and Local.

Others- Fragmentation, Connection byte, Connection limit, Payload length,Physical Address, Ownership



ACTIONS
==========

Based on the  above information a network packet following actions can be taken:

Accept
------
Allows the packet through the firewall. No subsequent rules are applied. This action has no parameters.


Deny
------
Silently drops the packet. No subsequent rules are applied. This action has no parameters.


Reject
-------
Packet is dropped and an appropriate message is sent back to the sender. No subsequent rules are applied. This action has a parameter that lets you specify how	the firewall reacts to the packet. Parameter options include TCP RST and a number of ICMP  messages.


Accounting/Count
------------------
Counts packets that match the rule, but makes no decision on the packet. Even if the packet matches, the inspection process continues with other rules below it. This action has a parameter for specifying the rule name for accounting.


Queue/Pipe
-----------
Passes the packet to a user space process for inspection. It is translated into QUEUE for iptables and "divert" for ipfw. This action is only supported by compilers for iptables and ipfw. This action has no parameters.
      

Routing
---------
Makes the firewall route matching packets through a specified interface or a 	gateway. This action is translated into ROUTE target for iptables and route option 	for PF and ipfilter. Compilers for PF and ipfilter support "fastroute", "route-to", "reply-to" and "dup-to" options. Parameters let you change the inbound and outbound interface and route the packet through a specified gateway. You can also tell the firewall to continue inspecting the packet after a match, and you can tell the firewall to make these changes to a copy of the packet while allowing the original packet to proceed normally.


Continue
---------
Essentially an empty action. Can be used when you want to assign an option, 	such as logging, to a match but take no other action in that rule. This action has no parameters.



FEATURES
===========


Functions
----------
-Enable firewall
-Disable firewall
-Flush iptables
-Insert rules to iptables
-Append rules to iptables
Remove rules from iptables
Save iptables rules
Restore iptables rules
Force default settings to iptables
List available interfaces
Display network connections (both incoming and outgoing)
List iptables rules
ICMP Filtration
Echo Request
Echo Reply
Timstamping
Address Masking
Source-Quenching
Redirection
Parameter Problem
Others
Attack Filtration
Syn Flooding Attack
Server Panic Attack
Xmas Attack
Null  Attack

Miscellaneous
--------------
-Machine-Architecture neutral
-GUI
-Portable
-Small Sized




REQUIREMENTS
===============

 * Software is independent of Machine-Architecture
 * Linux, Unix or Unix-like OS's
 * Python-2.6 or later
 * IPTables



