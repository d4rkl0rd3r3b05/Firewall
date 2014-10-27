## Firewall
Graphical Firewall based on UFW created in python(using TKinter) that ease off the work of a network administrator to secure a network. The problem that the ‘FIREWALL’ aims, is to filter network packets according to some rules as set by the administrator. This tool scans a network packet for fields like source address, destination address, source port, destination port, service, protocol, flags(like SYN, ACK, FIN etc.) and other options(like fragmentation, physical address, length of payload, owner, connection options etc.). To provide all these filtering  facilities, the tool used the tables provided by the Linux kernel firewall (implemented as different Netfilter modules). The tool probes all the incoming, outgoing and forwarded network packets once it is enabled  in order to filter out or do as commanded by the administrator in case of a match. The tool aims to reduce human efforts required to filter and protect a particular network or a host as done using various packet scannin g and filtering techniques, by providing a automated graphical tool to do the same.  The need of this tool is for protecting and managing a network or a  host properly and efficiently in order to receive high throughput. Also the tool can be used to detect any potential attack or breach that may be attempted on a particular network or on any particular host by configuring it to generate custom warning messages when certain criteria is fulfilled. The need of this system exists because, even though functionalities pertaining to scanning and filtering the network have been in existence for such a long time, but still they require of huge man-power that can cause huge loss in time and varying consistency-levels, thus hampering the working efficiency of the network administration system. As this tool is Graphical thus it can be used with great ease without much difficulty.


#### SCANNED FIELDS

Network packets are scanned for following key fields :
- *Addresses* 	  - `Source Address and Destination Address `
- *Port Numbers*  - `Source port and destination port numbers`
- *Protocols*     - `TCP, UDP, SCTP, ICMP, ESP, UDPLITE and AH.`
- *Mask*	  - `Source-Address or Destination-Address mask.`
- *Name*	  - `Source or Destination network  or  host name.`
- *States*	  - `New, Established, Invalid, Ralated etc.`
- *Interfaces*	  - `Name  of  an interface via which a packet was received  or is going to be sent.`
- *Address type*  - `Unicast,  Multicast, Broadcast, Anycast,  Unreachable, Blackhole and Local.`
- *Others*        - `Fragmentation, Connection byte, Connection limit, Payload length,Physical Address, Ownership`



#### IPTABLES
IPtables is an administration tool for IPv4 packet filtering and NAT. It is a user space application program that allows a system administrator to configure the tables provided by the Linux kernel firewall (implemented as different Netfilter modules) and the chains and rules it stores. Different kernel modules and programs are currently used for different protocols; iptables applies to IPv4, ip6tables to IPv6, arptables to ARP, and ebtables  for Ethernet frames.

	
IPtables requires elevated privileges to operate and must be executed by user root, otherwise it fails to function. On most Linux systems, iptables is installed as /usr/sbin/iptables and documented in its man page, which can be opened using man iptables when installed. It may also be found in /sbin/iptables, but since iptables is not an "essential binary", but more like a service, the preferred location remains /usr/sbin.

IPtables is also commonly used to inclusively refer to the kernel-level components. x_tables is the name of the kernel module carrying the shared code portion used by all four modules that also provides the API used for extensions; subsequently, Xtables is more or less used to refer to the entire firewall (v4,v6,arp,eb) architecture.

IPtables firewall contains 3 tables, every table contains chains. Those chains are default. User is able to define new chains and link from default chains to those user defined chains.



#### TYPES OF IPTABLES TABLES


##### Filter Table
This table is used to filter packets that pass the firewall. Its purpose is only packet filtering, and will filter packets that comes to the machine (incoming), packets that goes out (outgoing) and packets that are forwarded between network cards (filtering), in case that machine has two or more network cards.
That table contains 3 chains: INPUT chain, OUTPUT chain and FORWARD chain.

 - INPUT chain - used to filter incoming packets

 - OUTPUT chain - used to filter outgoing packets

 - FORWARD chain - used to filter forwarded packets (between network cards).


##### Nat Table
This table is used to change source of the IP.
 
 - PREROUTING chain - used to change IP before forwarding take place

 - POSTROUTING chain - used to change IP after forwarding take place

 - OUTPUT chain - used to filter on outgoing


##### Mangling Table
This tables is used to modify packets.



#### ACTIONS

Based on the  above information a network packet following actions can be taken:

##### Accept
Allows the packet through the firewall. No subsequent rules are applied. This action has no parameters.


##### Deny
Silently drops the packet. No subsequent rules are applied. This action has no parameters.


##### Reject
Packet is dropped and an appropriate message is sent back to the sender. No subsequent rules are applied. This action has a parameter that lets you specify how	the firewall reacts to the packet. Parameter options include TCP RST and a number of ICMP  messages.


##### Accounting/Count
Counts packets that match the rule, but makes no decision on the packet. Even if the packet matches, the inspection process continues with other rules below it. This action has a parameter for specifying the rule name for accounting.


##### Queue/Pipe
Passes the packet to a user space process for inspection. It is translated into QUEUE for iptables and "divert" for ipfw. This action is only supported by compilers for iptables and ipfw. This action has no parameters.
      

##### Routing
Makes the firewall route matching packets through a specified interface or a 	gateway. This action is translated into ROUTE target for iptables and route option 	for PF and ipfilter. Compilers for PF and ipfilter support "fastroute", "route-to", "reply-to" and "dup-to" options. Parameters let you change the inbound and outbound interface and route the packet through a specified gateway. You can also tell the firewall to continue inspecting the packet after a match, and you can tell the firewall to make these changes to a copy of the packet while allowing the original packet to proceed normally.


##### Continue
Essentially an empty action. Can be used when you want to assign an option, 	such as logging, to a match but take no other action in that rule. This action has no parameters.



#### FEATURES


##### Functions
 - Enable firewall
 - Disable firewall
 - Flush iptables
 - Insert rules to iptables
 - Append rules to iptables
 - Remove rules from iptables
 - Save iptables rules
 - Restore iptables rules
 - Force default settings to iptables
 - List available interfaces
 - Display network connections (both incoming and outgoing)
 - List iptables rules
 - **ICMP Filtration**
   - Echo Request
   - Echo Reply
   - Timstamping
   - Address Masking
   - Source-Quenching
   - Redirection
   - Parameter Problem
   - Others
 - **Attack Filtration**
   - Syn Flooding Attack
   - Server Panic Attack
   - Xmas Attack
   - Null  Attack

##### Miscellaneous
 - Machine-Architecture neutral
 - GUI
 - Portable
 - Small Sized




#### REQUIREMENTS
 - Software is independent of Machine-Architecture
 - Linux, Unix or Unix-like OS's
 - Python-2.6 or later
 - IPTables
 - Tkinter
 

#### HOW TO RUN
In order to run the project execute the file **firewall.pyw** with python.
 

#### PROBLEMS

##### Inability  to Distinguish
The tool cannot distinguish between a genuine packet and a malicious packet. It simply follow the set rules in order to filter packets, which may sometimes  disrupt normal services.

##### Speed
Use of scripting language results in a speed constraints. But the constraint is acceptable, as use of python provides complete portability.

##### Memory
Large amount of memory is consumed if there are many rules to be handled. And system may sometime hang. 

##### Weakness
The tool can still be cheated to get through it, using various advance skills. The tool does not check for tunneling and wrap-up connection, and can thus be breached.


#### REFERENCES

##### BOOKS
 - Python 2.1 bible
 - IPtables - tutorial
 - TCP-IP Network Administration, 3rd Edition
 - IPtables  manpages

##### WEBSITES
 - www.linuxforums.org
 - www.python-forum.org
 - www.linuxreport.org
 - [en.wikipedia.org](en.wikipedia.org)
 

#### LICENSE
##### The MIT License (MIT)
> Copyright (c) 2014 d4rkl0rd3r3b05

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.




