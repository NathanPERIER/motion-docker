# motion-docker

## Build the container

```bash
docker build . -t motion
```

## Run with Docker

Here is a docker-compose example : 

```yaml
version: '3.9'
  motion:
    image: motion:latest
    container_name: motion
    networks:
     - default
    volumes:
      - /path/to/conf:/etc/motion:ro
      - /path/to/logs:/var/log/motion
      - /path/to/data:/var/lib/motion
    devices:
      - /dev/video0:/dev/video0
    ports:
      - 8080:8080 # admin interface
      - 8081:8081 # /dev/video0
    user: 4000:44
```
