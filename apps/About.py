import streamlit as st



def app():

    st.markdown("<h1 style='text-align: center;'>About Project</h1>", unsafe_allow_html=True)
    #st.title("About Project")
    st.markdown("""India has one of the highest road accident rates in the world, with over 1,50,000 people losing their lives each year due to road accidents. In order to analyze and classify road accidents in India, we can look at various factors such as the causes, types of vehicles involved, types of accidents, and location.

In 2021, there were an estimated 1.53 lakh road accidents in India, which resulted in 1.54 lakh deaths and 4.12 lakh injuries. This means that on average, there were 1130 accidents, 422 deaths, and 3844 injuries every day.

The government of India is taking steps to address the problem of road accidents. These steps include improving road infrastructure, increasing driver training, and enforcing traffic laws more strictly.

We can all play a role in reducing road accidents. By following the rules of the road, driving safely, and being aware of our surroundings, we can help to make our roads safer for everyone.""")

    st.markdown("""## Features

    * Age band of driver
    * Vehicle type
    * Age of vehicle
    * Weather conditions
    * Day of week
    * Road surface conditions
    * Light conditions
    * Sex of driver
    * Season
    * Speed limit

    ## Target

     Our target is to predict Accident seriousness (fatal, serious, slight)

    ## Model

     A random forest model can be used to predict accident seriousness. 
     Random forest is an ensemble learning algorithm that consists of a collection of decision trees. 
     Each decision tree is trained on a random subset of the data, and the predictions of all the trees are combined to make a final prediction.

    ## Training

     The model can be trained on a dataset of road accident records. 
     The dataset should include the features listed above and the target variable, which is the accident seriousness. 
     The model can be trained using the scikit-learn library in Python.

    ## Inference

     Once the model is trained, it can be used to predict accident seriousness for new data points. 
     The model can be used to identify high-risk situations and take preventive measures.

    ## Limitations

     The model is not perfect and it can make mistakes. 
     The accuracy of the model depends on the quality of the training data. 
     The model is also limited by the features that are included in the dataset. 
     If important features are not included in the dataset, the model will not be able to make accurate predictions.

    ## Conclusion

     The ML model can be used to predict accident seriousness and help to reduce the number of road accidents in India. 
     The model can be used to identify high-risk situations and take preventive measures. 
     The model is not perfect, but it is a valuable tool that can help to save lives.""")


    st.markdown(""" 
     
    We can determine the root causes and take the necessary precautions to prevent road accidents in India by analysing and categorising them based on all of these factors. Road infrastructure improvements, raising public knowledge of traffic laws and regulations, and implementing harsher penalties for moving offences are a few of the actions that may be implemented.""")

if __name__ == "__main__":
    app()
