# Timbrar desde Perl

Para poder ejecutar los ejemplos es necesario tener Perl instalado en la version 5.18.1 o superior, en Windows es preferible tenerlo instalado usando ActivePerl.

## Parametros de prueba

- La URL de prueba es: **http://213.239.207.18:4444/stamp**

- El token de seguridad de prueba es: **abc**

- El RFC emisor de prueba es: **AAA010101AAA**

- El certificado de prueba lo puedes descargar de: **----LLENAR-----**

## Windows
Para ejecutar un timbrado de prueba unicamente ejecuta el script desde la linea de comandos usando:

```sh
# Timbrar
C:\> "C:\Perl64\perl.exe" timbrar.pl

# Cancelar
C:\> "C:\Perl64\perl.exe" cancelar.pl
```

**Nota** Es posible que el archivo perl.exe se encuentre en una ruta distinta dependiendo de la configuración del sistema.

## Unix/Linux/OSX
Para ejecutar un timbrado de prueba unicamente ejecuta el script desde la terminal usando:

```sh
# Timbrar
$ perl timbrar.pl

# Cancelar
$ perl cancelar.pl
```