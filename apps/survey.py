import streamlit as st


def app():
    st.title("User Survey")
    st.subheader("This page will provide a mechaism out fill in a survey form")
    st.markdown("""
        <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSc6vA13BVVikPh3dKJpv37PUdvNL9ifkFUg4FDoiB0Kk3TwTw/viewform?embedded=true" width="700" height="520" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
       """, unsafe_allow_html=True)
    
#    with st.form("my_form"):
#        st.write("Inside the form")
#        slider_val = st.slider("Form slider")
#        checkbox_val = st.checkbox("Form checkbox")
#
#       # Every form must have a submit button.
#        submitted = st.form_submit_button("Submit")
#        if submitted:
#            st.write("slider", slider_val, "checkbox", checkbox_val)
    
#    st.write("Outside the form")