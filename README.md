to build an image:
```
docker build -t todoapp_image .
```
to run the container:
```
docker compose run app
```
to enter the containe
```
docker exec -it app bash
```
uruchom stronę:
```
172.18.0.2:8000
```
add image to dockerhub
```
docker tag todoapp_image jinglebellczyk/todo_app
```
push image to dockerhub
```
 docker push jinglebellczyk/todo_app
```
**Github:**
```
git add .
git commit -m "nazwa commitu"
git push
```