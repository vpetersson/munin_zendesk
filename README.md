munin_zendesk
=============

# About

munin_zendesk is a munin-plugin for plotting Zendesk statistics written by [Viktor Petersson](http://viktorpetersson.com/).

There are currently two plugins: 

 * zendesk_tickets
  * This plugin plots the number of tickets in the system (and their state)
 * zendesk_satisfaction
  * This plugin plots the satisfaction of tickets (bad/good)

# Installation

Simply copy the files (or symlink) to your plugins-directory and make sure they are executable.
The plugin also depends on two settings in plugins.conf -- 'credentials' and 'subdomain'.

## Credentials

For authentication, you can either authenticate with your username/password, username/token (preferred).
To enable token-authentication, visit http://[yoursubdomain].zendesk.com/settings/api

For token:
`email/token:[token]`

For username/password:
`you@domain.com:password`

## Subdomain

The subdomain is simply your instance at Zendesk. Please note that even if you use your 
own domain (ie. support.mydomain.com), this must be specified as the Zendesk that the 
CNAME points to (ie. foobar.zendesk.com).

## Example

`[zendesk_*]`

`env.credentials me@domain.com/token:abc123`

`env.subdomain myawesomeproduct`


# Credits

Thanks to [Adam Panzer](https://github.com/apanzerj), who wrote the [sample code](https://support.zendesk.com/entries/21457528-using-python-with-the-zendesk-api) for interacting with Zendesk's API.

