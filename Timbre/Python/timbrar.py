# -*- coding: UTF-8 -*-
import httplib, urllib

# Creamos una variable para guardar el XML del CFD que queremos timbrar, por facilidad
# en este caso lo tenemos de manera estatica
cfd = """<?xml version="1.0" encoding="UTF-8"?>
<cfdi:Comprobante 
    xsi:schemaLocation="http://www.sat.gob.mx/cfd/3 http://www.sat.gob.mx/sitio_internet/cfd/3/cfdv32.xsd" 
    xmlns:cfdi="http://www.sat.gob.mx/cfd/3" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    LugarExpedicion="D.F.,MEXICO" 
    NumCtaPago="DESCONOCIDO" 
    formaDePago="PAGO EN UNA SOLA EXHIBICION" 
    metodoDePago="TRANSFERENCIA ELECTRONICA"
    subTotal="1000.00" 
    total="1160.00" 
    fecha="2013-12-02T22:18:24" 
    certificado="MIIEdDCCA1ygAwIBAgIUMjAwMDEwMDAwMDAxMDAwMDU4NjcwDQYJKoZIhvcNAQEFBQAwggFvMRgwFgYDVQQDDA9BLkMuIGRlIHBydWViYXMxLzAtBgNVBAoMJlNlcnZpY2lvIGRlIEFkbWluaXN0cmFjacOzbiBUcmlidXRhcmlhMTgwNgYDVQQLDC9BZG1pbmlzdHJhY2nDs24gZGUgU2VndXJpZGFkIGRlIGxhIEluZm9ybWFjacOzbjEpMCcGCSqGSIb3DQEJARYaYXNpc25ldEBwcnVlYmFzLnNhdC5nb2IubXgxJjAkBgNVBAkMHUF2LiBIaWRhbGdvIDc3LCBDb2wuIEd1ZXJyZXJvMQ4wDAYDVQQRDAUwNjMwMDELMAkGA1UEBhMCTVgxGTAXBgNVBAgMEERpc3RyaXRvIEZlZGVyYWwxEjAQBgNVBAcMCUNveW9hY8OhbjEVMBMGA1UELRMMU0FUOTcwNzAxTk4zMTIwMAYJKoZIhvcNAQkCDCNSZXNwb25zYWJsZTogSMOpY3RvciBPcm5lbGFzIEFyY2lnYTAeFw0xMjA3MjcxNzAyMDBaFw0xNjA3MjcxNzAyMDBaMIHbMSkwJwYDVQQDEyBBQ0NFTSBTRVJWSUNJT1MgRU1QUkVTQVJJQUxFUyBTQzEpMCcGA1UEKRMgQUNDRU0gU0VSVklDSU9TIEVNUFJFU0FSSUFMRVMgU0MxKTAnBgNVBAoTIEFDQ0VNIFNFUlZJQ0lPUyBFTVBSRVNBUklBTEVTIFNDMSUwIwYDVQQtExxBQUEwMTAxMDFBQUEgLyBIRUdUNzYxMDAzNFMyMR4wHAYDVQQFExUgLyBIRUdUNzYxMDAzTURGUk5OMDkxETAPBgNVBAsTCFVuaWRhZCAxMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC2TTQSPONBOVxpXv9wLYo8jezBrb34i/tLx8jGdtyy27BcesOav2c1NS/Gdv10u9SkWtwdy34uRAVe7H0a3VMRLHAkvp2qMCHaZc4T8k47Jtb9wrOEh/XFS8LgT4y5OQYo6civfXXdlvxWU/gdM/e6I2lg6FGorP8H4GPAJ/qCNwIDAQABox0wGzAMBgNVHRMBAf8EAjAAMAsGA1UdDwQEAwIGwDANBgkqhkiG9w0BAQUFAAOCAQEATxMecTpMbdhSHo6KVUg4QVF4Op2IBhiMaOrtrXBdJgzGotUFcJgdBCMjtTZXSlq1S4DG1jr8p4NzQlzxsdTxaB8nSKJ4KEMgIT7E62xRUj15jI49qFz7f2uMttZLNThipunsN/NF1XtvESMTDwQFvas/Ugig6qwEfSZc0MDxMpKLEkEePmQwtZD+zXFSMVa6hmOu4M+FzGiRXbj4YJXn9Myjd8xbL/c+9UIcrYoZskxDvMxc6/6M3rNNDY3OFhBK+V/sPMzWWGt8S1yjmtPfXgFs1t65AZ2hcTwTAuHrKwDatJ1ZPfa482ZBROAAX1waz7WwXp0gso7sDCm2/yUVww==" 
    noCertificado="20001000000100005867" 
    sello="qTzEwNUDvk/WpeFstpf/FLNmiHMxiL8pDTXGNb+DCFO0Z7SXMZJCim3JAlBw8Astvr0/jiVfo3WdWbaX88cC1l1+iipOLdedbFNHZUmsW86nC1YQHWw0S6mEiGH0ZxGa5KOl/1mrvPlDweeCiyYavNQeEuO1r0/ELobMi07w6ps=" 
    tipoDeComprobante="ingreso"
    version="3.2" >
    <cfdi:Emisor nombre="EMPRESA DEMO" rfc="AAA010101AAA">
        <cfdi:DomicilioFiscal codigoPostal="34343" pais="MEXICO" estado="DISTRITO FEDERAL" municipio="BENITO JUAREZ" calle="REFORMA"/>
        <cfdi:RegimenFiscal Regimen="PERSONA FISCA"/>
    </cfdi:Emisor>
    <cfdi:Receptor nombre="PUBLICO EN GENERAL" rfc="XAXX010101000">
        <cfdi:Domicilio pais="MEXICO" calle="INSURGENTES"/>
    </cfdi:Receptor>
    <cfdi:Conceptos>
        <cfdi:Concepto importe="1000.00" valorUnitario="1000.00" descripcion="PZA" unidad="CANT" cantidad="1"/>
    </cfdi:Conceptos>
    <cfdi:Impuestos>
        <cfdi:Traslados>
            <cfdi:Traslado importe="160.00" tasa="160.00" impuesto="IVA"/>
        </cfdi:Traslados>
    </cfdi:Impuestos>
    <cfdi:Addenda/>
</cfdi:Comprobante>"""

# Recuerda que:
# La URL de prueba es: http://213.239.207.18:4444/stamp
# El token de seguridad de prueba es: abc
# El RFC emisor de prueba es: AAA010101AAA
# El certificado de prueba lo puedes descargar de: ----LLENAR-----

# Creamos una nueva instancia del objeto HTTPConnection con la dirección URL 
# del servicio de timbrado y el puerto que utilizaremos, en este caso 4444
connection = httplib.HTTPConnection("213.239.207.18:4444")

# Agregamos un header a la petición indicando el token que utilizaremos, en este caso el de 
# prueba 'abc'. Este debe ser modificado una vez que querramos utilizar nuestra propia cuenta
# para timbrar
headers = {"x-auth-token": "abc"}

# Solicitamos el timbrado enviando una petición HTTP usando el metodo POST a la URL "/stamp",
# agregando el header previamente instanciado y enviando el CFD en el cuerpo.
connection.request("POST", "/stamp", cfd, headers)

# Extraemos la respuesta del servidor de timbrado
response = connection.getresponse()

# Obtenemos el codigo de respuesta del servidor y el timbre para nuestro CFD
response_code = str(response.status) + " " + response.reason
stamp = response.read()

# Cerramos la conexión con el servicio
connection.close()

print "Codigo HTTP: " + response_code
print "Timbre: " + stamp
