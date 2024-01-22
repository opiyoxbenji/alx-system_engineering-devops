0x13. Firewall

Overview
This project involves configuring the Uncomplicated Firewall (UFW) to enhance the security of a server by blocking all incoming traffic except for specific TCP ports. The permitted ports include:

Port 22 (SSH)
Port 80 (HTTP)
Port 443 (HTTPS SSL)
Before proceeding, it is essential to understand the basics of firewalls and how they function to control network traffic.

Resources
Firewall: Learn about what a firewall is and how it helps in securing a system.
Testing and Debugging
To ensure proper configuration and functionality, the readme provides guidance on using the telnet tool. This tool helps in checking if sockets are open by attempting connections to specific IP addresses and ports. The readme provides examples of testing ports 22 and 2222 on a server.

Important Notes and Warnings
Firewall Rules: Careful consideration is emphasized when configuring firewall rules. The readme warns against denying port 22/TCP without ensuring an alternate means of access to prevent potential lockouts.

Network Limitations: Due to the school network's outgoing connection filtering, certain ports on servers outside the school network may not be directly accessible. The readme advises testing from a server outside the school network, such as the provided web-02 server.

Container Limitation: The use of Containers on Demand (Docker containers) is not allowed for this project due to limitations.

Warning!
It is crucial to exercise caution when working with firewall rules. Blocking port 22 without proper considerations can lead to loss of SSH access, and recovery may be challenging. When installing UFW, the default blocking of port 22 is highlighted, emphasizing the need to unblock it immediately to prevent accidental lockouts.

Note: This readme provides comprehensive information to guide users through the project, ensuring proper firewall configuration without compromising system access.
