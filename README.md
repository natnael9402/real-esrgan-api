#BUILD
docker build -t real-esrgan-api .

#RUN 
docker run -p 8000:8000 real-esrgan-api
