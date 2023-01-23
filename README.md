<h1 align="center">Potholes Engine</h1>
<div align="center">
Description
</div>

Related system components:
1. Frontend: https://github.com/Qitu/DrStreet
2. ESP32-CAM-Program: https://github.com/ba98/ESP32-CAM-Program
3. Potholes Detection Model: https://github.com/ba98/potholes-model
4. Notebook: https://colab.research.google.com/drive/1mY76NY9ychuCbh5SvEtZbluvKimAdKRn?usp=sharing

------

to setup backend:

```
python3.10 -m venv venv
```

```
source venv/bin/activate
```

```
pip install -r requirements.txt
```

```
python potholes/manage.py runserver
```


Make sure your db settings are set. You can change them in local_settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'potholes',
        'USER': 'potholes',
        'PASSWORD': 'potholes',
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}
MODEL_PATH = 'potholes/potholes/conf/ai_models/v1.h5'
DETECTION_CONFIG_PATH = 'potholes/potholes/conf/detection_config.json'

```


You can send requests to the api on this endpoint:
1.
```
    POST https://potholes-engine.taheralkamel.com/prediction/api/v1/case HTTP/1.1
    Content-Type: multipart/form-data
    Content-Disposition: form-data; name="image"; filename="test.jpg"
```

2.
```
    Get https://potholes-engine.taheralkamel.com/prediction/api/v1/case HTTP/1.1
    Content-Type: application/json
```

sample response:
```
HTTP/1.1 200 OK
Server: nginx/1.22.0 (Ubuntu)
Date: Sat, 21 Jan 2023 17:52:09 GMT
Content-Type: application/json
Content-Length: 4223
Connection: close
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Referrer-Policy: same-origin
Cross-Origin-Opener-Policy: same-origin

[
  {
    "uuid": "17894caa-562a-4e24-a3a4-6ab336a732cb",
    "status": "Predicted",
    "results": [
      {
        "image": "/static/images/img/test_DlOFDZ2.jpg",
        "result_image": "/static/images/processed/2410aee2-5452-4eb7-8669-0a684874ea8b.jpg",
        "detections": [
          {
            "name": "pothole",
            "box_points": [
              107,
              627,
              980,
              745
            ],
            "percentage_probability": 52.405279874801636
          },
          {
            "name": "pothole",
            "box_points": [
              1263,
              472,
              1433,
              513
            ],
            "percentage_probability": 61.177414655685425
          },
          {
            "name": "pothole",
            "box_points": [
              167,
              579,
              515,
              643
            ],
            "percentage_probability": 60.98626255989075
          },
          {
            "name": "pothole",
            "box_points": [
              1255,
              458,
              1431,
              491
            ],
            "percentage_probability": 47.68099784851074
          },
          {
            "name": "pothole",
            "box_points": [
              804,
              583,
              931,
              612
            ],
            "percentage_probability": 45.59263586997986
          },
          {
            "name": "pothole",
            "box_points": [
              1353,
              623,
              1446,
              669
            ],
            "percentage_probability": 48.65012764930725
          }
        ]
      }
    ],
    "created_at": "2023-01-21T17:40:23.731875Z",
    "updated_at": "2023-01-21T17:40:23.738755Z"
  },
  {
    "uuid": "f0edf565-5811-47ce-ab53-4bc39a070ef8",
    "status": "Predicted",
    "results": [
      {
        "image": "/static/images/img/test_DmtjubB.jpg",
        "result_image": "/static/images/processed/29906dc2-3341-46b4-b6e5-a0ec680ca7fc.jpg",
        "detections": [
          {
            "name": "pothole",
            "box_points": [
              107,
              627,
              980,
              745
            ],
            "percentage_probability": 52.405279874801636
          },
          {
            "name": "pothole",
            "box_points": [
              1263,
              472,
              1433,
              513
            ],
            "percentage_probability": 61.177414655685425
          },
          {
            "name": "pothole",
            "box_points": [
              167,
              579,
              515,
              643
            ],
            "percentage_probability": 60.98626255989075
          },
          {
            "name": "pothole",
            "box_points": [
              1255,
              458,
              1431,
              491
            ],
            "percentage_probability": 47.68099784851074
          },
          {
            "name": "pothole",
            "box_points": [
              804,
              583,
              931,
              612
            ],
            "percentage_probability": 45.59263586997986
          },
          {
            "name": "pothole",
            "box_points": [
              1353,
              623,
              1446,
              669
            ],
            "percentage_probability": 48.65012764930725
          }
        ]
      }
    ],
    "created_at": "2023-01-21T17:34:35.741816Z",
    "updated_at": "2023-01-21T17:34:35.746972Z"
  },
  {
    "uuid": "ed0b0434-546d-4f3a-96ab-93180c64cc03",
    "status": "Predicted",
    "results": [
      {
        "image": "/static/images/img/test_lsAWrhG.jpg",
        "result_image": "/static/images/processed/c79303d7-f730-461f-ad28-6d2e95870dec.jpg",
        "detections": []
      }
    ],
    "created_at": "2023-01-21T17:34:35.741816Z",
    "updated_at": "2023-01-21T17:34:35.746972Z"
  },
  {
    "uuid": "9c3bda09-cd23-410d-967a-f68dfc0b3ab5",
    "status": "Predicted",
    "results": [
      {
        "image": "/static/images/img/esp32-cam_4ImsJ8J.jpg",
        "result_image": "/static/images/processed/50d3d8f5-7044-4ed4-9562-58ed6e4ddb38.jpg",
        "detections": []
      }
    ],
    "created_at": "2023-01-21T17:34:35.741816Z",
    "updated_at": "2023-01-21T17:34:35.746972Z"
  },
  {
    "uuid": "63f657f0-473a-4594-977f-6fd62689e716",
    "status": "Predicted",
    "results": [
      {
        "image": "/static/images/img/esp32-cam_CoRbNjG.jpg",
        "result_image": "/static/images/processed/5f99bffd-77a4-4b79-9328-aad2237f4ef9.jpg",
        "detections": []
      }
    ],
    "created_at": "2023-01-21T17:34:35.741816Z",
    "updated_at": "2023-01-21T17:34:35.746972Z"
  },
  {
    "uuid": "8e8dd9a0-12fd-413b-8f31-e0ac24c2316b",
    "status": "Predicted",
    "results": [
      {
        "image": "/static/images/img/esp32-cam_EMJQxKz.jpg",
        "result_image": "/static/images/processed/e38ddf3c-ff2c-4f90-ac4c-b823532e14d1.jpg",
        "detections": []
      }
    ],
    "created_at": "2023-01-21T17:34:35.741816Z",
    "updated_at": "2023-01-21T17:34:35.746972Z"
  },
  {
    "uuid": "dbb46201-3d4a-41db-a48d-3f9502fee389",
    "status": "Predicted",
    "results": [
      {
        "image": "/static/images/img/test_TizXNtt.jpg",
        "result_image": "/static/images/processed/23792c76-5c10-4d8c-bd68-39ed0d7e9b0b.jpg",
        "detections": []
      }
    ],
    "created_at": "2023-01-21T17:37:03.554977Z",
    "updated_at": "2023-01-21T17:37:03.562022Z"
  },
  {
    "uuid": "83442921-0a93-4f13-89da-f5fe34495136",
    "status": "Predicted",
    "results": [
      {
        "image": "/static/images/img/test_VEv03UO.jpg",
        "result_image": "/static/images/processed/713a65e2-b746-40f3-954a-0d2689931f85.jpg",
        "detections": [
          {
            "name": "pothole",
            "box_points": [
              107,
              627,
              980,
              745
            ],
            "percentage_probability": 52.405279874801636
          },
          {
            "name": "pothole",
            "box_points": [
              1263,
              472,
              1433,
              513
            ],
            "percentage_probability": 61.177414655685425
          },
          {
            "name": "pothole",
            "box_points": [
              167,
              579,
              515,
              643
            ],
            "percentage_probability": 60.98626255989075
          },
          {
            "name": "pothole",
            "box_points": [
              1255,
              458,
              1431,
              491
            ],
            "percentage_probability": 47.68099784851074
          },
          {
            "name": "pothole",
            "box_points": [
              804,
              583,
              931,
              612
            ],
            "percentage_probability": 45.59263586997986
          },
          {
            "name": "pothole",
            "box_points": [
              1353,
              623,
              1446,
              669
            ],
            "percentage_probability": 48.65012764930725
          }
        ]
      }
    ],
    "created_at": "2023-01-21T17:47:15.726980Z",
    "updated_at": "2023-01-21T17:47:15.733269Z"
  }
]
```
