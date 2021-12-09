import streamlit as st
import leafmap.foliumap as leafmap
from streamlit_player import st_player


def app():
    st.title("Cluster Vision")

    st.markdown(
        """
        This web app demonstrates various interactive tasks for visual explorations to aid decision making in Public Health 
        """
    )

    st.info("Click on the left sidebar menu to navigate to the different visualization aids.")

    st.subheader("Timelapse of early Covid -19 spread in US")
    st.markdown(
        """
        The following timelapse animation was produced using Google Earth Pro, to demonstrate the viral spread thought out the early pandemic according to phylogeographic analysis
    """
    ## possibly embed as a video instead gif
    ## <div style="padding: 56.25% 0 0 0; position: relative"><div style="height:100%;left:0;position:absolute;top:0;width:100%"><iframe height="100%" width="100%;" src="https://embed.wave.video/61b1016d46e0fb0001cf9ec3" frameborder="0" allow="autoplay; fullscreen" scrolling="no"></iframe></div></div>
    )

    #with row1_col2:
    #    st.image("https://github.com/giswqs/data/raw/main/timelapse/goes.gif")
    #    st.image("https://github.com/giswqs/data/raw/main/timelapse/fire.gif")
    st.image("https://github.com/rmbeard/data/raw/main/covid_vid_SparkVideo.gif",  width=350,)
    st.write("Any better ideas on how to produce a looping image than a gif?")