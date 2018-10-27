<VirtualHost 127.0.0.1:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.



	ServerName www.trialsite.com
	DocumentRoot /home/danish/virtualenv/trialsite/trialsite
	ServerAlias www.trialsite.com
	Alias /static /home/danish/virtualenv/trialsite/static
    
	<Directory /home/danish/virtualenv/trialsite>
        	Require all granted
    	</Directory>

        WSGIDaemonProcess www.trialsite.com python-home=/home/danish/virtualenv python-path=/home/danish/virtualenv/trialsite/trialsite
        WSGIProcessGroup www.trialsite.com

        WSGIScriptAlias / /home/danish/virtualenv/trialsite/trialsite/wsgi.py

        <Directory /home/danish/virtualenv/trialsite/trialsite>
                Require all granted
		<Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        <Directory /home/danish/virtualenv/trialsite/static>
                Require all granted
        </Directory>

        <Directory /home/danish/virtualenv/trialsite/media>
                Require all granted
        </Directory>

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


DocumentRoot /home/danish/virtualenv/trialsite/trialsite
Alias /static /home/danish/virtualenv/trialsite/static