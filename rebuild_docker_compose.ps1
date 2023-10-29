docker-compose down

$backendImageExists = docker images backend:latest
if ($backendImageExists) {
    docker image rm backend-backend:latest
}

$frontendImageExists = docker images frontend:latest
if ($frontendImageExists) {
    docker image rm backend-frontend:latest
}

$databaseVolumeExists = docker volume ls --quiet --filter name=database_volume
if ($databaseVolumeExists) {
    docker volume rm backend_database_volume
}

$staticVolumeExists = docker volume ls --quiet --filter name=static_volume
if ($staticVolumeExists) {
    docker volume rm backend_static_volume
}

$mediaVolumeExists = docker volume ls --quiet --filter name=media_volume
if ($mediaVolumeExists) {
    docker volume rm backend_media_volume
}

docker compose up
