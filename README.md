# System commands for this project:

``` bash
conda create -n basic_demo python=3.7 -y

conda activate basic_demo

source activate basic_demo

conda activate base

conda activate basic_demo

``` 

``` bash

pip install dvc
touch stage_01.py
touch stage_02.py 
python stage_01.py
python stage_01.py
python stage_02.py
git init
dvc init
```


``` bash
touch dvc.yaml
dvc repro

python stage_01.py
python stage_02.py
```

``` bash
dvc repro
dvc dag
```

``` bash
git remote -v
git remote
git checkout -c demo
git branck demo
git branch demo
git add .
git commit -m "demo_data"
git branch
git branch demo
```


``` bash
git remote add testorigin https://github.com/Rahul-Shedge/basic_of_dvc_demo.git
```


``` bash
git push testorigin master
```
TO list the branches in the folder

``` bash
git branch -a

```