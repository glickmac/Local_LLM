# Local_LLM


![Python](https://img.shields.io/badge/python-v3.10.0-blue.svg)
![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)

This is a tutorial to deploy and query a Local LLM on a Mac M1 or Linux system. 

<p align="center"><img src="https://github.com/glickmac/Local_LLM/blob/main/images/red.jpg" width=60%></p>


## Table of Contents
[Installing requirements](#intro)    
[Downloading and activating the LLAMA-2 model](#importance)    
[Querying the model](#workflow)    
[Quickstart](#quickstart)    
[Building your own StreamLit Deployable Model](#install)       

## <a name="intro"></a>Installing requirements
The requirements for running this on an M1 are in part obtained through the GitHub requirements.txt file which can be used to build an Anaconda environment. For those that do not have Anaconda find it [here.](https://www.anaconda.com/download/) Build the chatbot-llm environment with the following command:
```
conda create -n chatbot-llm --file requirements.txt python=3.10 
conda activate chatbot-llm
```
Next, we need to install some other packages using pip that are not available via conda. In addition, for the LLM to work on a Mac or Linux system we must set the cmake arguments using the command below.
```
# Linux and Mac
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS"

pip install llama-cpp-python --force-reinstall --upgrade --no-cache-dir 
pip install sse_starlette
pip install starlette_context
pip install pydantic_settings
```

## <a name="importance"></a>Downloading and activating the LLAMA-2 model

Now it is time to download the model. For this example, we are using a relatively small LLM (only?!?! about 4.78 GB). You can download the model from [Hugging Face](https%3A%2F%2Fhuggingface.co%2FTheBloke%2FLlama-2-7B-Chat-GGUF%2Fresolve%2Fmain%2Fllama-2-7b-chat.Q5_K_M.gguf%3Fdownload%3Dtrue).

```
mkdir -p models/7B
wget -O models/7B/llama-2-7b-chat.Q5_K_M.gguf https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_M.gguf?download=true
```
Once the model and the packages have been installed, we are now ready to run the LLM locally. We begin by calling the llama_cpp.server with the downloaded LLAMA-2 model. This combination acts like ChatGPT (server) and GPT-4 (model) respectively.

```
python3 -m llama_cpp.server --model models/7B/llama-2-7b-chat.Q5_K_M.gguf
```

## <a name="workflow"></a>Querying the model
The server and model are now ready for user input. We are querying the server and model using query.py with our question of choice. To begin querying, we should open a new terminal tab and activate our conda environment again.
```
conda activate chatbot-llm
export MODEL="models/7B/llama-2-7b-chat.Q5_K_M.gguf"
python query.py
```

## <a name="install"></a>Recap and acknowledgments
In this demostration, we installed an LLM server (llama_cpp.server) and model (LLAMA-2) locally on a Mac. We were able to deploy our very own local LLM. Then we were able to query the server/model and adjust the size of the response. Congratulations you have built your very own LLM! The inspiration for this work and some of the code building blocks are derived from [Youness Mansar](https://medium.com/@CVxTz). Feel free to use or share the code.

