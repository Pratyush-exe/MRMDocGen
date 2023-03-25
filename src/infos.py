import json
import streamlit as st


class ModelDataInfo:
    def __init__(self):
        """Fetches all the required information about the model and datasets
        """
        ...

    def get_document_general_info(self):
        """Collectes the information from the user about
        - Given data
        - Approaches
        - Model approaches
        - Assumptions
        - Conclusion
        """

        info_json = {}
        st.write("Add Public and Model Informationn")

        self.overview = st.text_area(
            "Write a small overview of the problem statement"
        )
        self.data_prep = st.text_area("Data preparation approaches")

        self.model_name = st.text_input("Model name and info: ")
        self.model_methadology = st.text_area("Model methadology: ")

        # show a model performance report in dataframe

        self.assumptions = st.text_area("Assumptions")
        self.assumption_reasons = st.text_area("Reason for above decisions")
        self.conclusion = st.text_area("Add any of your conclusions")

        if self.overview:
            info_json["overview"] = self.overview

        if self.data_prep:
            info_json["data_prep"] = self.data_prep

        if self.model_name:
            info_json["model_name"] = self.model_name

        if self.model_methadology:
            info_json["model_methadology"] = self.model_methadology

        if self.assumptions:
            info_json["assumptions"] = self.assumptions

        if self.conclusion:
            info_json["conclusion"] = self.conclusion

        # Add a submit button
        if st.button("Submit"):
            st.write("Noted all your observations and assumptions")
            with open("Data/info_json.json", "w") as outfile:
                json.dump(info_json, outfile, indent=4)
            st.success("Noted all your assumptions and observations")
