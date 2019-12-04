
# Build, train & debug, and deploy & monitor with Amazon SageMaker

## Introduction

Amazon SageMaker is a fully managed service that removes the heavy lifting from each step of the machine learning workflow, and provides every developer and data scientist with the ability to build, train, and deploy machine learning (ML) models quickly. In this interactive workshop, we will work on the different aspects of the ML workflow to build, train, and deploy a model using all the capabilities of SageMaker including the ones that we announced at re:Invent this week. We will use the Amazon SageMaker to build and share notebooks, train and debug models with SageMaker Debugger, and deploy and monitor with SageMaker Model Monitor. Let’s build together!


## Datasets

In this workshop, we will go through the steps of training, debugging, deploying and monitoring a **network traffic classification model**.

For training our model we will be using datasets <a href="https://registry.opendata.aws/cse-cic-ids2018/">CSE-CIC-IDS2018</a> by CIC and ISCX which are used for security testing and malware prevention.
These datasets include a huge amount of raw network traffic logs, plus pre-processed data where network connections have been reconstructed and  relevant features have been extracted using CICFlowMeter, a tool that outputs network connection features as CSV files. Each record is classified as benign traffic, or it can be malicious traffic, with a total number of 15 classes.

The goal is to demonstrate how to execute training of a network traffic classification model using the Amazon SageMaker framework container for XGBoost, training and debugging. Once trained how to then deploy and monitor the model performance.


## Getting started

Initially have an open AWS account, with privileges to create and run Amazon SageMaker notebooks and access to S3 buckets.

### Setting Up The environment

In the console goto Amazon SageMaker and create a new notebook instance. 
Give the created notebook a name, use the default settings and the instance size of ml.t2.medium. If you are using an Event Engine account, the execution role for the notebook will have been created during the account creation process. (The notebooks only access Amazon S3 and Amazon SageMaker services in this workshop)

Once created open your notebook and from the terminal run:

```
cd SageMaker/
git clone https://github.com/aws-samples/reinvent2019-aim362-sagemaker-debugger-model-monitor  
```

Exit the terminal and open your notebook.

## Modules

This workshops consists of 2 modules:

- <a href="01_train_and_debug/">**01\_train\_and\_debug**</a> - Train and debug with Amazon SageMaker Debugger
- <a href="02_deploy_and_monitor/">**02\_deploy\_and\_monitor**</a> - Deploy and Monitor with Amazon SageMaker Model Monitor

You must comply with the order of modules, since the outputs of a module are inputs of the following one.


## License

The contents of this workshop are licensed under the [Apache 2.0 License](./LICENSE).

## Authors

[Giuseppe A. Porcelli](https://it.linkedin.com/in/giuporcelli) - Principal, ML Specialist Solutions Architect - Amazon Web Services EMEA<br />
[Paul Armstrong](https://www.linkedin.com/in/paul-armstrong-532bb41) - Principal Solutions Architect - Amazon Web Services EMEA
