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

```apache

```

5. Create the file `<ip virtual machine>`-ssl.conf 

6. dasd
7. dadas
8. dasdas
9.  dasdasd
10. asdasd
11. asdasd


Useful Links:

* [QGIS Server](https://qgis.org/resources/installation-guide/#linux)
* [QGIS Server Apache](https://docs.qgis.org/3.40/en/docs/server_manual/getting_started.html#installation-on-debian-based-systems)


{sub-ref}`today` | {sub-ref}`wordcount-words` words | {sub-ref}`wordcount-minutes` min read