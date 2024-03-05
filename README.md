1.La arquitectura debe seguir los principios de microservicios basados en eventos. Por tal motivo, la comunicación entre los servicios debe hacerse usando comandos y eventos.

2.Sea claro en la definición de los eventos de acuerdo al escenario de calidad que desea satisfacer ¿Evento de integración o con carga de estado?¿Por qué? Elabore en el diseño del esquema, desde la tecnología hasta la evolución de los mismos ¿Avro o Protobuf? ¿Event Stream Versioning? Justifique sus decisiones.

3.Para probar las capacidades de escalado, los ingenieros esperan que usted desarrolle al menos 4 microservicios. Cabe aclarar que NO se espera tener los microservicios completamente desarrollados, solo los comandos, consultas e infraestructura necesaria (tablas, tópicos, repositorios, etc) para satisfacer los escenarios de calidad.

4.Dada la naturaleza de la comunicación por comandos y eventos, usted debe usar un Broker de eventos. Los ingenieros desean que usted use Apache Pulsar.

6.En términos de patrones para el almacenamiento, decida si va usar un modelo clásico CRUD o Event Sourcing. Recuerde que no necesariamente todos los servicios deben usar el mismo patrón de almacenamiento. Es su decisión definir que servicios pueden usar una u otra.

7.Finalmente, debe poder desplegar sus servicios en la plataforma de preferencia. Justifique el porqué de su decisión.

8.Para cada una de las entregas no olvide incluir en el README o documento anexo, la descripción de actividades por miembro (es decir que hizo cada uno y como colaboró al equipo).

Santiago Lozano:

Paola Forero:

Oscar Sanchez:

Leidy Beltran:

Intrucciones

#Correr flask (api que procesa los guardados) flask --app src/alpes/api --debug run

#Correr pulsar docker-compose --profile pulsar up

#Correr sidecar servidor para recibir comando rpc python src/sidecar/main.py

#Enviar comando por grpc python src/sidecar/cliente.py

#Recibir mensajes desde pulsar (topico de eventos) PENDING
