<?php
date_default_timezone_set('America/Mexico_City');
// Verificamos que se haya enviado el formulario
if (isset($_POST['carrera']) && isset($_POST['unidad']) && isset($_POST['num_equipo']) && isset($_POST['num_practica']) && isset($_FILES['archivo'])) 
{
  // Almacenamos los valores de los campos en variables
  $carrera = $_POST['carrera'];
  $unidad = $_POST['unidad'];
  $num_equipo = $_POST['num_equipo'];
  $num_practica = $_POST['num_practica'];
  $archivo = $_FILES['archivo'];
  $fecha_hora = date('ymdHis'); // Obtenemos la fecha y hora actual en el formato yymmddhhmmss

  // Verificamos que el archivo se haya subido correctamente
  if ($archivo['error'] == UPLOAD_ERR_OK) {

    $extension = pathinfo($archivo['name'], PATHINFO_EXTENSION);
    if ($extension == 'pdf')
    {
      // Creamos el nombre del archivo según el formato especificado
    $nombre_archivo =  $fecha_hora .'_' .$carrera . '_' . $unidad . '_' . $num_equipo . '_' . $num_practica . '.pdf' ;
 
    // Asignamos la ruta de la carpeta donde se guardará el archivo
    $ruta = 'uploadspracs2023a/' . $nombre_archivo;

    // Movemos el archivo a la carpeta especificada
    move_uploaded_file($archivo['tmp_name'], $ruta);
    echo 'El archivo se ha cambiado el nombre a '.  $nombre_archivo . ' y se ha subido correctamente' ;
    }else{
      echo "El archivo seleccionado NO es un PDF. Lee las instrucciones nuevamente";
    }
    
 }
}





   ?>
