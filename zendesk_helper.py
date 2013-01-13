import os, ConfigParser

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

config = ConfigParser.ConfigParser()
config.read(munin_config_file)

username = config.get('zendesk', 'username')
password = config.get('zendesk', 'password') 
subdomain = config.get('zendesk', 'subdomain')
cache_folder = config.get('zendesk', 'cache_folder')
