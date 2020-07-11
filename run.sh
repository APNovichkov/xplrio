docker image build --compress -t xplrio:latest . && \
docker container run --publish 8080:8080 --env PROJECT_DB_HOST=docker.for.mac.host.internal --env DEBUG=True --env COMPRESS_ENABLED=True --env COMPRESS_OFFLINE=True --name=xplrio-app xplrio:latest
