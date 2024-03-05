# Step 1

docker run -d --hostname rmq --name rabbit-server -p 8080:15672 -p 5672:5672 rabbitmq:3-management

# Step 2

go-to http://localhost:8080/
