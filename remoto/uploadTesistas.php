<?php
date_default_timezone_set('America/Mexico_City');
// Verificamos que se haya enviado el formulario
if (isset($_POST['nombre']) && isset($_FILES['archivo'])) 
{
  // Almacenamos los valores de los campos en variables
  $nombre = $_POST['nombre'];
  $archivo = $_FILES['archivo'];
  $fecha_hora = date('ymdHis'); // Obtenemos la fecha y hora actual en el formato yymmddhhmmss

  // Verificamos que el archivo se haya subido correctamente
  if ($archivo['error'] == UPLOAD_ERR_OK) {

    $extension = pathinfo($archivo['name'], PATHINFO_EXTENSION);
    if ( $extension== 'zip' or  $extension == 'pdf')
    {
      // Creamos el nombre del archivo según el formato especificado
    $nombre_archivo =  $fecha_hora . '_' . $nombre . '.'. $extension ;
 
    // Asignamos la ruta de la carpeta donde se guardará el archivo
    $ruta = 'uploadsavances/' . $nombre_archivo;

    // Movemos el archivo a la carpeta especificada
    move_uploaded_file($archivo['tmp_name'], $ruta);
    echo 'El archivo se ha cambiado el nombre a '.  $nombre_archivo . ' y se ha subido correctamente' ;
    }else{
      // echo  $extension;
      echo "En las instrucciones que les envié dice que acepto archivos en formato PDF o ZIP solamente";
    }
    
 }
}





   ?>
