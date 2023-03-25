## **MRMDocGen** 

An automatic document generator for generating customizable Machine Learning risk management documents by just 

- uploading your models and validation dataset 
- writing very bare minimum about the model performance and general information
- Watch different charts and choose which are required to export 
- Using chatGPT API `MRMDocGen` can generate professional reports from just bare minimum information 
- Get your Documentation with customizable templates within seconds 

-----
 
### **How to run the project** 

First clone the project by the following command:
```bash 
git clone https://github.com/Pratyush-exe/MRMDocGen.git
```

**`Linux`** 

You can either locally install everything by create your virtual environment first by:

```bash 
make virtualenv
```
and then just install it by:
```
make install 
```
Additionally you can also run other `make` commands get started with linting and formatting.

Then just run the following command for running the project

```bash 
streamlit run main.py 
```

**`Windows`**

In windows if you are in `WSL` then doing the same as above will be just fine. Else you can install `cmake` using `choco` with this command:

```bash
choco install cmake
```

And then do the samee thing as followd. 

**`Docker`** 

If you have docker installed then you can build the image by the following: 

```bash 
docker build -t mrm-doc:v1 . 
```

And then run the following command to start the container 

```bash
docker run mrm-doc:v1
```

---- 


### **Future Scopes and Roadmap**

**`Web`**

- [ ] Building a dedicated backend using FastAPI / Flask 
- [ ] Better UI with React/Angular 

**`ML/MLOps`**

- [ ] Tracking data and model drift and visualization 
- [ ] Using XAI (Explainable AI) for providing better root cause analysis 
- [ ] Using automatics CI/CD for generating major data/model version control information on the doc. 
- [ ] Also showing other information metric required for deployement including CPU Usages, disk usage and latency 