# About

munin_zendesk is a munin-plugin collection for plotting Zendesk statistics written by [Viktor Petersson](http://viktorpetersson.com/).

There are currently two plugins: 

 * zendesk_tickets
  * This plugin plots the number of tickets in the system (and their state)
 * zendesk_satisfaction
  * This plugin plots the satisfaction of tickets (bad/good)

# Installation

Simply copy the files (or symlink) to your plugins-directory and make sure they are executable.

The plugin also depends a cronjob-entry and a settings inside of the files. The reason why I didn't
use the global plugins.conf is simply because the cronjob need access to this information. 

## Cronjob

I quickly discovered after deploying the plugin that it would timeout (in Munin) if you have more 
than 1000 or so tickets. To resolve this, I added caching. This is also good, since Munin won't 
allow you to set an individual refresh rate for a given plugin. At least in my opinion, it is both 
pointless and abusive to Zendesk to fetch all of this data every 5th minute (the default value).

When called on like usual, zendesk_tickets and zendesk_satisfaction will simply go and retreive 
the cache from /tmp/zendesk_tickets.pkl and /tmp/zendesk_satisfaction.pkl.

To refresh the cache, you must add 'refreshcache' to the command. Here's how the crontab entry
would look like if you want to refresh the cache every 30 minutes and run munin as the user 'munin'.

`00,30	*	*	*	*	munin	python /path/to/zendesk_tickets refreshcache`

`15,45	*	*	*	*	munin	python /path/to/zendesk_satisfaction refreshcache`

## Inside the files

You need to configure two values in each file:

 * credentials
 * subdomain

### Credentials

For authentication, you can either authenticate with your username/password, username/token (preferred).
To enable token-authentication, visit http://[yoursubdomain].zendesk.com/settings/api

For token:
`email/token:[token]`

For username/password:
`you@domain.com:password`

### Subdomain

The subdomain is simply your instance at Zendesk. Please note that even if you use your 
own domain (ie. support.mydomain.com), this must be specified as the Zendesk that the 
CNAME points to (ie. foobar.zendesk.com).

### Example

`credentials = "me@domain.com/token:abc123"`

`subdomain = "myawesomeproduct"`

(Make sure you quote both strings, otherwise it won't work.)

# Credits

Thanks to [Adam Panzer](https://github.com/apanzerj), who wrote the [sample code](https://support.zendesk.com/entries/21457528-using-python-with-the-zendesk-api) for interacting with Zendesk's API.

