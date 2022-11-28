# upload_service
# Solution Engineer

## Personal Information

Please provide all information in English.

|  |  |
| --- | --- |
| **⚠️ First Name:** | `Poonyavee` |
| **⚠️ Last Name:** | `Shomchom` |
| **⚠️ Email:** | `poonyavee.shomchom@gmail.com` |
| **⚠️ Phone Number:** | `0868452225` |

## Run upload_web

```
cd upload_web
source .env
docker-compose up -d
```

# .env for upload_web
```
VITE_API_URL=http://localhost:8000/v1
VITE_WS_URL=ws://localhost:8000/v1
```


## Run upload_api

```
cd upload_api
docker-compose up -d
```
