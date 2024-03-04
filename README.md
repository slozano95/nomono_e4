#Correr flask (api que procesa los guardados)
flask --app src/alpes/api --debug run

#Correr pulsar
docker-compose --profile pulsar up

#Correr sidecar servidor para recibir comando rpc
python src/sidecar/main.py 

#Enviar comando por grpc
python src/sidecar/cliente.py

#Recibir mensajes desde pulsar (topico de eventos)
PENDING