import os 
import yaml
import json
import base64
import joblib
from ensure import ensure_annotations
from src.cnnClassifier import logger
from box import ConfigBox
from box.exceptions import BoxValueError
from pathlib import Path 
from typing import Any  

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """
    
    Reads the yaml file and returns

    Args : 
        path_to_yaml (str) : path like input 

    Raises :
        ValueError : if yaml file is empty
        e : empty file

    Returns : 
        ConfigBox: ConfigBox type        
    
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_read(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e            