# Uploader

## Install using Docker

How to build<br>

1. Clone this repo to your local machine<br>
2. Copy & paste your gcp key into gcp_key/key.json
3. Run this command:<br>
   ``docker build [your_repo_path] -t uploader --build-arg bucket_name=[value]``<br>
   *if you want to save locally:<br>
   ``docker build [your_repo_path] -t uploader``

How to save<br>
``docker save uploader | gzip > uploader.tar.gz``

How to load<br>
``docker load < uploader.tar.gz``

How to run<br>
``docker run -p [access_port]:80 --name uploader -d uploader``
