# QGIS Server Deployment

* Virtual machine key
* IP address virtual machine `<ip virtual machine>`


## QGIS Server Installation

1. Open PowerShell
2. Go to the folder where is your .pem file (Key)
3. Connect to the virtual machine using the following code and replace the values `<key_file.pem>` and `<ip virtual machine>` as corresponse:

```powershell
ssh -i <key_file.pem> azureuser@<ip virtual machine>
```

4. Follow the Linux Apache instalation for [QGIS Server](https://qgis.org/resources/installation-guide/#linux). 

5. Create a folder to storage the project files:

```bash
mkdir /home/qgis/projects/
cd /home/qgis/projects/
```

6. Download the tutorial data:

```bash
wget https://github.com/qgis/QGIS-Training-Data/archive/release_3.40.zip
unzip release_3.40.zip
```

7. Copy tutorial files to projects folder:

```bash
mv QGIS-Training-Data-release_3.40/exercise_data/qgis-server-tutorial-data/world.qgs .
mv QGIS-Training-Data-release_3.40/exercise_data/qgis-server-tutorial-data/naturalearth.sqlite .
```

## Apache installation

1. Install Apache

```
sudo apt install apache2 libapache2-mod-fcgid
```

2. Go to the sites available folder

```
cd /etc/apache2/sites-available
```

3. Create the file `<ip virtual machine>`.conf

`sudo nano <ip virtual machine>.conf`

4. Copy the following data on the file created.

* Replace `<ServerAdmin>` with the email of the admin.
* Replace `<ServerName>` with the ip Address of your virtual machine 

```apache
<VirtualHost *:80>
  ServerAdmin <ServerAdmin>
  ServerName <ServerName>

  DocumentRoot /var/www/html

  # Apache logs (different than QGIS Server log)
  ErrorLog ${APACHE_LOG_DIR}/qgis.demo.error.log
  CustomLog ${APACHE_LOG_DIR}/qgis.demo.access.log combined

  # Longer timeout for WPS... default = 40
  FcgidIOTimeout 120

  FcgidInitialEnv LC_ALL "en_US.UTF-8"
  FcgidInitialEnv PYTHONIOENCODING UTF-8
  FcgidInitialEnv LANG "en_US.UTF-8"

  # QGIS log
  FcgidInitialEnv QGIS_SERVER_LOG_STDERR 1
  FcgidInitialEnv QGIS_SERVER_LOG_LEVEL 0

  # default QGIS project
  SetEnv QGIS_PROJECT_FILE /home/qgis/projects/world.qgs

  # QGIS_AUTH_DB_DIR_PATH must lead to a directory writeable by the Server's FCGI process user
  FcgidInitialEnv QGIS_AUTH_DB_DIR_PATH "/home/qgis/qgisserverdb/"
  FcgidInitialEnv QGIS_AUTH_PASSWORD_FILE "/home/qgis/qgisserverdb/qgis-auth.db"

  # Set pg access via pg_service file
  SetEnv PGSERVICEFILE /home/qgis/.pg_service.conf
  FcgidInitialEnv PGPASSFILE "/home/qgis/.pgpass"

  # if qgis-server is installed from packages in debian based distros this is usually /usr/lib/cgi-bin/
  # run "locate qgis_mapserv.fcgi" if you don't know where qgis_mapserv.fcgi is
  ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
  <Directory "/usr/lib/cgi-bin/">
    AllowOverride None
    Options +ExecCGI -MultiViews -SymLinksIfOwnerMatch
    Require all granted
  </Directory>

  <IfModule mod_fcgid.c>
  FcgidMaxRequestLen 26214400
  FcgidConnectTimeout 60
  </IfModule>

</VirtualHost>
```

1. Create the file `<ip virtual machine>`-ssl.conf 

2. dasd
3. dadas
4. dasdas
5.  dasdasd
6.  asdasd
7.  asdasd


Useful Links:

* [QGIS Server](https://qgis.org/resources/installation-guide/#linux)
* [QGIS Server Apache](https://docs.qgis.org/3.40/en/docs/server_manual/getting_started.html#installation-on-debian-based-systems)


{sub-ref}`today` | {sub-ref}`wordcount-words` words | {sub-ref}`wordcount-minutes` min read