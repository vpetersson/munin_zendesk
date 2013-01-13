import os, sys

common_plugin_conf_locations = [
    '/etc/munin/plugin-conf.d/munin-node', 
    '/usr/local/etc/munin/plugin-conf.d/plugins.conf',
    'munin-node',
    ]

munin_config_file = None
for file in common_plugin_conf_locations:
    if os.path.isfile(file):
        munin_config_file = file

if munin_config_file == None:
    print 'Unable to detect munin-config file. Exiting.'
    sys.exit(1)
    
config = {}
for line in open(munin_config_file, "r").readlines():
    if 'env.zendesk_' in line:
        data = line.strip('\n').split('=')
        key = data[0].strip()
        value = data[1].strip()
        config[key] = value

username = config['env.zendesk_username']
password = config['env.zendesk_password'] 
subdomain = config['env.zendesk_subdomain']
cache_folder = config['env.zendesk_cache_folder']
