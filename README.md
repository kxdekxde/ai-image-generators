# Colab Code Generator for Civitai Checkpoint Models
A simple tool to generate Colab notebooks code to use some [Civitai](https://civitai.com) Checkpoint models with Google Colab.

## Models for the list:

  - [WAI-NSFW-illustrious-SDXL v14.0](https://civitai.com/models/827184/wai-nsfw-illustrious-sdxl) by [WAI0731](https://civitai.com/user/WAI0731)
  - [WAI-ANI-NSFW-PONYXL v14.0](https://civitai.com/models/404154/wai-ani-nsfw-ponyxl) by [WAI0731](https://civitai.com/user/WAI0731)
  - [Hassaku XL (Illustrious) v2.2](https://civitai.com/models/140272/hassaku-xl-illustrious) by [Ikena](https://civitai.com/user/Ikena)
  - [Hassaku (SD1.5) v1.3](https://civitai.com/models/2583/hassaku-sd15) by [Ikena](https://civitai.com/user/Ikena)
  - [Nova Anime XL v7.0](https://civitai.com/models/376130/nova-anime-xl) by [Crody](https://civitai.com/user/Crody)
  - [Nova Orange XL v9.0](https://civitai.com/models/967405/nova-orange-xl) by [Crody](https://civitai.com/user/Crody)
  - [Nova Cartoon XL v1.0](https://civitai.com/models/1570391/nova-cartoon-xl) by [Crody](https://civitai.com/user/Crody)
  - [Nova Furry XL v7B](https://civitai.com/models/503815/nova-furry-xl) by [Crody](https://civitai.com/user/Crody)
  - [Sudachi XL (Illustrious) v1](https://civitai.com/models/1288125/sudachi-xl-illustrious) by [Ikena](https://civitai.com/user/Ikena)
  - [Sudachi v1.0](https://civitai.com/models/85909/sudachi) by [Ikena](https://civitai.com/user/Ikena)
  - [Amanatsu (Illustrious) v1.1](https://civitai.com/models/1325426/amanatsu-illustrious) by [Ikena](https://civitai.com/user/Ikena)
 

## Requirements to use the script:

  - Double-click on _install_Python.bat_ to install Python 3.13
 
 
## Usage:

1. Double-click on _create_notebook.py_ to launch the tool.
2. Select the model you want to use. Hit enter.
3. The tool will ask you if you want to add some [LoRA](https://www.reddit.com/r/aiArt/comments/17wvc0e/comment/k9k9gtp/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button). You can add them going to Civitai, copying the download link of the LoRA you want and pasting it on the tool. If you don't want to add LoRA just input "n" and the terminal window will close.
4. Go to the folder "notebooks" and open the generated text file.
5. Copy the whole content.
6. Go to [Google Colab](https://colab.research.google.com/) and click `File>New notebook in Drive`.
7. Name the new *.ipynb* file to whatever you want, then click on `Runtime>Change runtime type` and select `T4 GPU`. Save.
8. Paste the code you copied previously from the generated text file and click on `Run Cell` (the "play" button to the left side of the code).
9. Wait until the script finish to run and you will see an URL like `https://XXXXXXXXXXXXXXXXXX.gradio.live`, open that URL.
10. If everything worked you will see the UI where you can input your prompts with the LoRA/s you added listed as well so you can use them there.

