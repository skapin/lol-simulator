# Installation


* Cloner ce depot
```
cd skeleton-backend/src/
git clone https://git.aiotools.ovh/aio/be-common.git common
git remote add origin https://git.aiotools.ovh/<GROUP>/<YOUR_REPO>.git
```


* Init Database

```
docker-compose exec app bash
FLASK_APP=server_app.py flask create-all
```
exit docker and run in your favorite browser:
```
http://localhost:9021/status/family
http://localhost:9021/status/subfamily
http://localhost:9021/status/characteristic
http://localhost:9021/status/allproduct
http://localhost:9021/api/save_magento_categories
http://localhost:9021/api/add_category_to_product_from_presta
http://localhost:9021/api/generate_client_sage
```
