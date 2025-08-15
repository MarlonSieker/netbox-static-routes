## netbox-static-routes

Display static routes in Netbox

### Install the Plugin

To install the Plugin clone the git repository and use following command in the right directory:
```
pip install .
```

### Migrate the database

```
./manage.py makemigrations netbox_static_routes
./manage.py migrate
```

### Include Plugin in Netbox

Now you have to include the Plugin to Netbox. Add following to your configuration file:
```
PLUGINS = ['netbox_static_routes']
```

And restart the services:
```
sudo systemctl restart netbox netbox-rq
```