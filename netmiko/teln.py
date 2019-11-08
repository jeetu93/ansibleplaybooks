from netmiko import ConnectHandler

R1 = {
	'device_type':  'cisco_xr_telnet',
	'ip': '10.106.254.105',
        'port': 23,
	'username': 'cisco',
	'password': 'cisco'
}


net_connect = ConnectHandler(**R1)
output = net_connect.send_command('show run')
print (output)
