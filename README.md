# Real-ESRGAN API

https://github.com/xinntao/Real-ESRGAN

## 🚀 Getting Started

### 🛠 Build the Docker Image

To build the Docker image, run the following command:

```sh
# BUILD
docker build -t real-esrgan-api .
```

### ▶️ Run the API

Once built, you can run the API using:

```sh
# RUN
docker run -p 8000:8000 real-esrgan-api
```

This will start the API and expose it on port **8000**.

## 🔗 API Endpoint

After running the container, the API will be accessible at:

```
http://localhost:8000
```

### Example Usage

You can send a **POST request** with an image to process:

```sh
curl -X POST -F "image=@path/to/image.jpg" http://localhost:8000/enhance
```

This will return an enhanced version of the input image.

## 📸 Preview



## 🛠 Requirements

- Docker installed on your machine
- A valid Real-ESRGAN model inside the API

## 📝 License

This project is licensed under the MIT License.

---

Made with ❤️ by **Natnael9402**

