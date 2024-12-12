echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8 "
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "installing dev requiremtnts"
pip install -r requirments_dev.txt
echo [$(date)]: "END"