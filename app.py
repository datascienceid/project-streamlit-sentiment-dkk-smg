import streamlit as st
from menu_home import display_home
from menu_data_collection import display_data_collection
from menu_data_annotation import display_data_annotation
from menu_eda import display_eda
from menu_data_preprocessing import display_data_preprocessing
from menu_feature_extraction import display_feature_extraction
from menu_modeling import display_modeling
from menu_inference import display_inference


st.set_page_config(layout="wide")

# menu sidebar
list_menu = ['Home', 'Data Collection', 'Data Annotation', 'Exploratory Data Analysis', 'Data Preprocessing', 
             'Feature Extraction', 'Modeling', 'Inference', 'Deployment']
menu_choice = st.sidebar.selectbox("Select a menu", list_menu)

### MENU: HOME ###
if menu_choice == 'Home':
    display_home()
    
### MENU: DATA COLLECTION ###
if menu_choice == 'Data Collection':
    display_data_collection()

### MENU: DATA ANNOTATION ###
if menu_choice == 'Data Annotation':
    display_data_annotation()

### MENU: EXPLORATORY DATA ANALYSIS ###
if menu_choice == 'Exploratory Data Analysis':
    display_eda()

### MENU: DATA PREPROCESSING ###
if menu_choice == 'Data Preprocessing':
    display_data_preprocessing()

### MENU: FEATURE EXTRACTION ###
if menu_choice == 'Feature Extraction':
    display_feature_extraction()

### MENU: MODELING ###
if menu_choice == 'Modeling':
    display_modeling()

### MENU: INFERENCE ###
if menu_choice == 'Inference':
    display_inference()