from PIL import Image
import streamlit as st


def app():
    # Define a dictionary of images with headings and content
    image_list = {
        "image_1": {"heading": "Accident per Month", "content": "Number Of Accident V/S Month.", "path": "acc_month.png"},
        "image_2": {"heading": "Accident on different times in day", "content": "Accident Different Time Of Day.", "path": "acc_russ.png"},
        "image_3": {"heading": "Realation of features", "content": "This Heat Map Shows The Relation Between Different Features.", "path": "heat_map.png"},
        "image_4": {"heading": "Accident in different Seasions", "content": "Numbers Of Accident In Different Seasions.", "path": "acc_season.png"}
    }

    # Define the main headline
    st.markdown("<h1 style='text-align: center;'>Visualization of Finding</h1>", unsafe_allow_html=True)

    # Loop over each image in the dictionary and display it with a heading and content
    for key, value in image_list.items():
        # Load the image from the file path
        image = Image.open(value["path"])

        # Display the image with a heading and content
        st.subheader(value["heading"])
        st.image(image, caption=value["content"], use_column_width=True)


if __name__ == "__main__":
    app()
