g-coin
======

G-coin server

### Deployment

```bash
# Install virtual environment
sudo easy_install virtualenv

git clone git@github.com:Goobs/g-coin.git gcoin
cd gcoin

# Create local configuration file from included example.
# NOTE: You MUST notify teammates in case you update configuration example.
cp gcoin/settings/local.py.example gcoin/settings/local.py

# Setup virtual environment within working directory.
virtualenv .
```

##### Updating after `git pull`'s

If you already have configured environment you need update requirements and maintain database structure.

```bash
# Activate virtual environment and install (update) requirements.
cd [project_root]
source bin/activate
pip install -r requirements.txt

# Update (or initialize) database.
./manage.py syncdb
./manage.py migrate
```

##### Running development server

```bash
./manage.py runserver
```

Navigate your browser to http://localhost:8000/. Here you go =)


