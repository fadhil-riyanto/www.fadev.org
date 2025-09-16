# mikrotik firewall

each firewall module (called as table in iptables) has its own predefined chain

- raw: 
	dipakai sebelum data dilihat oleh conntrack, NAT, masuk routing, dll. intinya di sinilah proses early sebelum benar2 di proses. karna belum sampai ke conntrack, maka akan sangat fast, dipakai untuk mitigasi ddos

	karna statenya ada sebelum conntrack, maka tidak ada status kayak estab, dll, tapi sangat fast + low cpu, only raw matching

	Karna raw table melihat packet sebelum NAT, maka
	- Destination IPs are still the original IPs from the client
	- Source IPs haven't been changed by masquerade or src-nat yet

	chain chain nya
	- prerouting: packet yang datang dari luar just sebelum masuk conntrack
	- output: packet yang digenerate oleh aplikasi, juga statenya sebelum di track oleh conntrack

	## contoh
	- `/ip firewall raw add chain=prerouting src-address=8.8.8.8 action=drop`

	## tambahan:

	letak raw di packet flow

	```
	IN → RAW → MANGLE (pre) → CONNECTION TRACKING → NAT (dstnat) → FILTER (input/forward) → MANGLE (post) → NAT (srcnat) → OUT
	```

- filter
    - input
    - forward
    - output

- mangle
    - prerouting
    - input
    - forward
    - output
    - postrouting
    - 
- nat
    - srcnat
    - dstnat

# chains
RouterOS consist of a few default chains. These chains allow you to filter packets at various points:

- The PREROUTING chain: Rules in this chain apply to packets as they just arrive on the network interface. This chain is present in the nat, mangle and raw tables.
- The INPUT chain: Rules in this chain apply to packets just before they’re given to a local process. This chain is present in the mangle and filter tables.
- The OUTPUT chain: The rules here apply to packets just after they’ve been produced by a process. This chain is present in the raw, mangle, nat, and filter tables.
- The FORWARD chain: The rules here apply to any packets that are routed through the current host. This chain is only present in the mangle and filter tables.
- The POSTROUTING chain: The rules in this chain apply to packets as they just leave the network interface. This chain is present in the nat and mangle tables.

