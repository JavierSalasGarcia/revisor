import os
import ftplib
import requests
import urllib.parse

# URL del sitio web
url = 'https://tudominio.com'

# Datos de acceso al FTP
ftp_host = 'ftp.tudominio.com'
ftp_user = 'admin@tudominio.com'
ftp_password = 'TuContraseña'
ftp_port = 21
ftp_remote_path = './uploadsavances'

# Conecta al FTP
ftp = ftplib.FTP()
ftp.connect(ftp_host, ftp_port)
ftp.login(ftp_user, ftp_password)

# Cambia al directorio "uploadsavances" en el servidor
ftp.cwd(ftp_remote_path)

# Hace una solicitud GET al sitio web y obtiene el HTML
response = requests.get(url)
html = response.text

# Extrae todos los enlaces de descarga de los archivos del HTML
links = []
for link in html.split('<a href=')[1:]:
    links.append(link.split('>')[0].replace('"',''))

# Descarga cada archivo y lo guarda en el directorio Pendientes
for link in links[5:]:
    file_name = link.split('/')[-1]
    file_name_corr = urllib.parse.unquote(link)
    response = requests.get(url + link)
    open('PendientesTesistas/' + file_name_corr, 'wb').write(response.content)
    print(f'Descargado {file_name_corr}')
    
    # Borra el archivo del servidor FTP
    ftp.delete(file_name_corr)


# Cierra la conexión FTP
ftp.quit()

print('Descarga completa')
