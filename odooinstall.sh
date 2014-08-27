apt-get install git git-core bzr
git clone https://github.com/odoo/odoo.git odoov7 -b 7.0
apt-get install postgresql-9.3
apt-get install python-dev libxml2-dev python-ldap libxslt1-dev libgutenprintui2-1 postgresql-contrib oidentd postgresql-doc-9.3 python-pip postgresql-server-dev-9.3 krb5-doc krb5-user
#python-szi ??
pip install dateutils feedparser gdata lxml Mako python-openid psycopg2 Babel pydot pyparsing reportlab simplejson pytz vatnumber vobject xlwt pyyaml zsi BabelGladeExtractor roman pygments PyWebDAV werkzeug CherryPy formencode dnslib dnspython pydns unittest2 mock docutils jinja2 pywsgi  -e bzr+http://download.gna.org/pychart/bzr-archive#egg=pychart
apt-get install python-pyhart
apt-get install libfreetype6-dev libjpeg-dev
# For Version 8.0 RC1
sudo pip install decorator psutil pypdf requests