# Deploy Ekeel App on Server
----------


## Update and Setup Video Annotation App
Go inside EKEELVideoAnnotation app folder
```bash
cd /var/www/apps/annotator/code
```

Update prune (TODO not always works, sometimes happen that one has to delete environment and reinstall due to conflicts) and restart
```bash
conda activate ekeel_anno_env
conda env update --file conda_environment.yml --prune
sudo systemctl restart ekeel
```

-----
## Launch gunicorn
*(done automatically by "systemctl ekeel", use only for debugging)*

For infos about linux services used in this project look [here](../../prerequisites/linux-services.md)

```bash
cd /var/www/apps/annotator/code
/home/torre/anaconda3/envs/ekeel_anno_env/bin/gunicorn --bind 127.0.0.1:5050 connector:app --timeout 180 --limit-request-line 0
```

### View gunicorn instances
```bash
ps -ef|grep gunicorn
```

-----
## Run manually Video Augmentation App
*(done automatically by "systemctl ekeel", use only for debugging)*
```bash
cd /var/www/apps/augmentator/src/flask-server
sudo /home/torre/anaconda3/envs/ekeel_aug_env/bin/python ./main.py
```

-----
## In case of broken environment that requires reinstall
Go inside code app folder
```bash
cd /var/www/apps/annotator/code
```

Create the Annotator conda environment
```bash
conda env create --file=conda_environment.yml
```