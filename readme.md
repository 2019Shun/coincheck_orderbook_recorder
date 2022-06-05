ビルド
```
docker build -t ubuntu_python:0.1 .
```

docker-composeによる起動
```
docker-compose up -d
```

docker-composeによる終了
```
docker-compose down
```

bashに入る
```
docker exec -i -t coincheck_orderbook_ubuntu /bin/bash
```

生存確認
```
docker exec -i -t coincheck_orderbook_ubuntu ps -u
```

