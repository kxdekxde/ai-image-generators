#@title AGGA's UtopiaXL V2.0
!pip install -q --upgrade pip

# Clean up any broken previous installs
!rm -rf stable-diffusion-webui
!pip uninstall -y xformers -q
!pip install -q pytorch-lightning==2.2.1

# Clone the WebUI
!git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui
%cd stable-diffusion-webui

# Download the Civitai model (fp16 safetensors)
!mkdir -p models/Stable-diffusion
!wget -O "models/Stable-diffusion/CivitaiModel1763468_fp16.safetensors" "https://civitai.com/api/download/models/1763468?type=Model&format=SafeTensor&size=pruned&fp=fp16"

# Launch the WebUI (skip torch/cuda test to avoid xformers issues)
!COMMANDLINE_ARGS="--share --skip-torch-cuda-test" python launch.py