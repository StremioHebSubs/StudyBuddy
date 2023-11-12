# Set the working directory to the project root
cd /project/root

# Download and install Python 3.11.4
curl -O https://www.python.org/ftp/python/3/3.11.4/Python-3.11.4.tgz
tar -xf Python-3.11.4.tgz
cd Python-3.11.4
./configure --prefix=/opt/python3.11.4
make -j4
sudo make install

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic