## Practical Work @ Decision Modelling 👨🏻‍💻

### Table of contents

- [Introduction](#introduction)
- [About the course](#about-course)
  * [Main Topics](#main-topics)
- [Labs](#labs)
  * [Lab 01 - Testing Binary Relations](#lab-1)
- [Setup](#setup)
  * [Create new enviornment](#create-new-env)
  * [Setup `pre-commit` hooks](#setup-pre-commit)


#

<a id="introduction" />

### 1. Introduction

[__Decision modeling__](https://www.meiss.com/columbia/en/teaching/1998/summer/B6015/download/lectures/lec1.pdf) refers to the use of _mathematical_ or _scientific_ methods to determine an allocation of scarce resources which improves or optimizes the performance of a system.

#

<a id="about-course" />

### 2. About the course

A decision model provides a way to visualize the sequences of events that can occur following alternative decisions (or actions) in a logical framework.

<p align="center">
  <img alt="Decision Modelling Process" width="400" src="extra/assets/decision_modelling_process.png" />
</p>

There are two types of decision models in the literature:

1. Deterministic models
2. Probabilistic models

The purpose of this course is to study different ways to model a _deterministic_ decision model.

<a id="main-topics" />

#### 2.1. Main Topics

- [x] Introduction to Decision Modeling
- [x] Preferences as binary relations
- [x] Label propagation, Community detection, Influence maximisation
- [x] Graph analytics & Deep Learning

#

<a id="labs" />

### 3. Labs

The main aim of this repository is to keep track of the work we have done in __Decision Modelling (DeM)__ labs.
#

<a id="lab-1" />

#### 3.1. Lab 01 - Testing Binary Relations

[NetworkX](https://networkx.org/) is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.

Please checkout lab's details [here](https://github.com/mohammadzainabbas/MGMA-Lab/tree/main/src/lab1) 

#

<a id="setup" />

### 4. Setup

If you want to follow along with the lab exercises, make sure to clone and `cd` to the relevant lab's directory:

```bash
git clone https://github.com/mohammadzainabbas/MGMA-Lab.git
cd MGMA-Lab/src/<lab-of-your-choice>
```

> For e.g: if you want to practice lab # 1, then you should do `cd MGMA-Lab/src/lab1`.

<a id="create-new-env" />

#### 4.1. Create new enviornment

Before starting, you may have to create new enviornment for the lab. Kindly, checkout the [documentation](https://github.com/mohammadzainabbas/MGMA-Lab/blob/main/docs/SETUP_ENV.md) for creating an new environment.

#

Once, you have activated your new enviornment, we may have to install all the dependencies for a given lab (kindly check if `requirements.txt` file exists for a given lab before running the below command):

```bash
pip install -r requirements.txt
```

<a id="setup-pre-commit" />

#### 4.2. Setup `pre-commit` hooks

In order to setup `pre-commit` hooks, please refer to the [documentation](https://github.com/mohammadzainabbas/MGMA-Lab/blob/main/docs/SETUP_PRE-COMMIT_HOOKS.md).

#

