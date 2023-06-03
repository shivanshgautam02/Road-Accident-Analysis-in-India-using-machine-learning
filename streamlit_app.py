import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload  # import your app modules here

st.set_page_config(page_title="Road Accident Analysis", layout="wide")


apps = [
    {"func": home.app, "title": "Home", "icon": "house"},
    {"func": upload.app, "title": "Visual", "icon": "camera"},
    {"func": heatmap.app, "title": "About", "icon": "info"},
    
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    # st.sidebar.title("Contact")
    # st.sidebar.info(
    #     """
    #     git
    #     contact
    #     facebook
    # """
    # )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break