# docker snippets

## docker run

this command will run as daemon, from image `freeradius/freeradius-server`
```sh
docker run --name my-radius -d freeradius/freeradius-server
```

no daemon involved
```sh
docker run --name my-radius freeradius/freeradius-server
```

# logging running container
```sh
docker logs my-radius2
```