# Huge IP addr in firewall mikrotik

this is the technique to add huge ip addr into firewall without making it 100% cpu usage

lets create address list

![image](../_images/dfc6abeb56962e660d3f308876c180c80ff200769f107efd28e913da5122455b327427e32516c66e565a5d3fb24f249a53ccb074953b73a1e72ab93f.png)

![image](../_images/c06f6391c17e30ee1a1b18808f5ad48034920a383a8d11f458027b83857420fb4eb300ecd25ec5080b0c9cb0313014a7738672473825ce88ea767d28.png)

# doing this with routeros_api python

removing

```python
list_queues = api.get_resource('/ip/firewall/address-list');
prev_ips = list_queues.get(list='__cp_wg_allow')

# print(prev_ips)
for prev_ips_i in prev_ips:
    print(f"[removing] {prev_ips_i['address']}")
    list_queues.remove(id=prev_ips_i['id'])

```

adding

```python
for x in data:
print(f"[adding] {x}")
api.get_resource("/ip/firewall/address-list").call("add", 
                    {"list": "__cp_wg_allow", "address": x},
).done_message
```

add to walled garden
```python
print("installing walled garden ip lists")
api.get_resource("/ip/hotspot/walled-garden/ip").call("add", {
    "comment": "__cp_wg_allow__fw_list",
    "dst-address-list": "__cp_wg_allow",
},).done_message
```