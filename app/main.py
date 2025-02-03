import os
import tempfile
import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from basicsr.archs.rrdbnet_arch import RRDBNet
from realesrgan import RealESRGANer

app = FastAPI()

# Initialize Real-ESRGAN model
model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=23, num_grow_ch=32, scale=4)
upsampler = RealESRGANer(
    scale=4,
    model_path="/Real-ESRGAN/weights/RealESRGAN_x4plus.pth",
    model=model,
    tile=0,
    tile_pad=10,
    pre_pad=0,
    half=False  # Set to True for GPU support
)

@app.post("/upscale/")
async def upscale_image(file: UploadFile = File(...)):
    # Create temporary directory
    with tempfile.TemporaryDirectory() as tmp_dir:
        try:
            # Save uploaded file
            input_path = os.path.join(tmp_dir, file.filename)
            with open(input_path, "wb") as buffer:
                buffer.write(await file.read())
            
            # Process image
            img = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)
            output, _ = upsampler.enhance(img, outscale=4)
            
            # Save output
            output_path = os.path.join(tmp_dir, "output.png")
            cv2.imwrite(output_path, output)
            
            return FileResponse(output_path, media_type="image/png")
        
        except Exception as e:
            return {"error": str(e)}