# About

munin_zendesk is a Munin-plugin collection for plotting Zendesk statistics written by [Viktor Petersson](http://viktorpetersson.com/).

There are currently three plugins: 

 * zendesk_tickets
  * This plugin plots the number of tickets in the system (and their state)
 * zendesk_closedtickets
  * I broke out closed tickets from the above plugin, as it was by nature several orders of magnitudes larger than the other states, and hence ruined the graph.
  * Consider this a sub-plugin to zendesk_tickets. It doesn't require any 'refreshcache' as it shares cache.
 * zendesk_satisfaction
  * This plugin plots the satisfaction of tickets (bad/good)

# Installation

Simply copy (or symlink) the following files to your plugins-directory and make sure they are executable (except helper.py):

 * zendesk_closedtickets
 * zendesk_satisfaction
 * zendesk_tickets
 * zendesk_helper.py

Next, you need to install the required Python dependencies. This can be done by simply running the following command from the path you checked out the code base:

    sudo pip install -r requirements.txt

In addition to the actual-plugins, the plugin also depends a cronjob-entry (see below). 

Once installed, you also need to add the configuration block (see the example) to your Munin plugin-file (*/etc/munin/plugin-conf.d/munin-node* on Ubuntu, and */usr/local/etc/munin/plugin-conf.d/plugins.conf* on FreeBSD).

Finally, verify that the plugins work by running:

    munin-run <the plugin you want to test>

If everything works as expected, restart munin-node.

## Cronjob

I quickly discovered after deploying the plugin that it would timeout (in Munin) if you have more  than 1,000 or so tickets. To resolve this, I added caching. This is also good, since Munin won't allow you to set an individual refresh rate for a given plugin. At least in my opinion, it is both pointless and abusive to Zendesk to fetch all of this data every 5th minute (the default value).

When called on like usual, zendesk_tickets and zendesk_satisfaction will simply go and retreive the cache from /tmp/zendesk_tickets.pkl and /tmp/zendesk_satisfaction.pkl.

To refresh the cache, you must add 'refreshcache' to the command. Here's how the crontab entry
would look like if you want to refresh the cache every 30 minutes and run munin as the user 'munin'.

    00,30	*	*	*	*	munin	python /path/to/zendesk_tickets refreshcache
    15,45	*	*	*	*	munin	python /path/to/zendesk_satisfaction refreshcache

## Credentials

For authentication, you can either authenticate with your username/password or username/token (preferred).
To enable token-authentication, visit http://yoursubdomain.zendesk.com/settings/api

## Subdomain

The subdomain is simply your instance at Zendesk. Please note that even if you use your 
own domain (ie. support.mydomain.com), this must be specified as the Zendesk that the 
CNAME points to (ie. foobar.zendesk.com).

## Example

Here's a sample of how the entry in munin-node/plugins.conf may look like:

    [zendesk]
    username = user@domain.com/token
    password = abc123
    subdomain = yoursubdomain
    cache_folder = /tmp

