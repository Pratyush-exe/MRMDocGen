import streamlit as st 

class UploadAssets:
    def __init__(self) -> None:
        "Uploading a model in .ONNX format and uploading the validation data to generate the required documentation"
    
    def upload_model(self):
        "Upload a model in.ONNX format"
        st.title("Upload a model in.ONNX format.")
        model_file = st.file_uploader(label="Upload model (ONNX format)", type=[".onnx"])
        return model_file
    
    def upload_validation_data(self):
        st.title("Uploading validation data") 
        validation_data = st.file_uploader(label="Upload validation data", type=[".csv"])
        return validation_data
    
    
if __name__ == '__main__':
    assets = UploadAssets()
    model_file = assets.upload_model() 
    validation_data = assets.upload_validation_data()
    
    
    