FROM python:3.8-slim-bullseye

# 1. Install system dependencies
RUN apt-get update && apt-get install -y \
    libgl1 \
    git \
    wget \
    && rm -rf /var/lib/apt/lists/*

# 2. Install PyTorch with pinned versions
RUN pip install torch==1.7.1+cpu torchvision==0.8.2+cpu \
    -f https://download.pytorch.org/whl/torch_stable.html

# 3. Clone Real-ESRGAN with proper weights setup
RUN git clone --depth 1 https://github.com/xinntao/Real-ESRGAN.git && \
    mkdir -p /Real-ESRGAN/weights && \
    wget https://github.com/xinntao/Real-ESRGAN/releases/download/v0.1.0/RealESRGAN_x4plus.pth -O /Real-ESRGAN/weights/RealESRGAN_x4plus.pth

# 4. Install Real-ESRGAN dependencies
WORKDIR /Real-ESRGAN
RUN pip install basicsr==1.4.2 facexlib==0.2.5 gfpgan==1.3.8 && \
    pip install -r requirements.txt && \
    python setup.py develop

# 5. Copy API code
COPY app/ /app
WORKDIR /app

# 6. Install API requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]