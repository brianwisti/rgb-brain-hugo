---
title: ComfyUI
created: 2024-01-19T15:51:14-08:00
updated: 2024-01-26T09:05:43-08:00
---

A pretty front-end for [Stable Diffusion](Stable%20Diffusion.md)

# Installation

* Put your SD checkpoints (the huge ckpt / safetensors files) in `models/checkpoints`
* Put your [VAE](VAE.md) in `models/vae`

## Installing ComfyUI on Windows

Portable builds for Window on NVidia GPUs (or CPU-only)

````
run_nvidia_gpu.bat
````

## Installing ComfyUI on Linux

Installing to a Python venv

````sh
git clone git@github.com:comfyanonymous/ComfyUI.git
pyenv virtualenv 3.11.7 comfy
pyenv local comfy
pip install torch torchvision torchaudio \
  --extra-index-url https://download.pytorch.org/whl/cu121
pip install -r requirements.txt
````

The run it directly from the checkout

````sh
python main.py
````

# ComfyUI-Manager

An extension designed to enhance the usability of ComfyUI

[GitHub - ltdrdata/ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)

Windows installation:

````
.\python_embeded\python.exe -s -m pip install gitpython
.\python_embeded\python.exe -c "import git; git.Repo.clone_from('https://github.com/ltdrdata/ComfyUI-Manager', './ComfyUI/custom_nodes/ComfyUI-Manager')"
````

Linux installation (from your existing ComfyUI checkout)

````sh
cd custom_nodes
git clone https://github.com/ltdrdata/ComfyUI-Manager.git
````

After installation, restart ComfyUI and select "Manager." This is where you install models.

# Related

* [GitHub - comfyanonymous/ComfyUI: The most powerful and modular stable diffusion GUI with a graph/nodes interface.](https://github.com/comfyanonymous/ComfyUI)
