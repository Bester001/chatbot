echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.12"
conda create --prefix ./env python=3.12 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "installing requirment"
pip install -r requirments.txt
echo [$(date)]: "END"