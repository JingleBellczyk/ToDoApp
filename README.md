## ToDoList - App

App for making to-do lists.  
After registration you can create lists, mark tasks as completed or edit date of them.   
Back-end is wrote in **Python** with **Django**, front-end in **html**.

# Set-up
## Docker
[DockerHub](https://hub.docker.com/r/jinglebellczyk/todo_app)

to build an image:
```
docker build -t todoapp_image . 
```
to run the container:
```
docker compose run app
```
to enter the container
```
docker exec -it app bash
```
add image to dockerhub
```
docker tag todoapp_image jinglebellczyk/todo_app
```
push image to dockerhub
```
 docker push jinglebellczyk/todo_app
```
delete images
```
docker system prune --all 
```
## UI
open web UI:
```
172.18.0.2:8000
```

## Github:
```
git add .
git commit -m "commit name"
git push
```
