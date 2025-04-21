import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(page_title="Shaadi Mein Swagat Hai Vatsalla!", page_icon="💐", layout="centered")

# Sidebar navigation
st.sidebar.title("📋 Navigate")
page = st.sidebar.radio("Choose a section:", ["🏠 Welcome", "👩‍❤️‍👨 About Vatsalla", "🖼️ Memory Gallery", "💌 Message Wall"])

# Welcome Page
if page == "🏠 Welcome":
    st.title("💐 Swagat Hai, Vatsalla Singh!")
    st.subheader("Shaadi ke is khas mauke par tumhara hardik swagat hai! 💖")

    st.markdown("""
    Hey **Vatsalla**,  

    Ye sirf ek welcome nahi, balki ek dil se diya gaya *shaandar* swagat hai – meri sabse pyari cousin sister ke liye!  
    Jab se suna ki tum aa rahi ho, excitement level high ho gaya hai! 🎉

    Is shaadi mein tumhara hona matlab – aur bhi zyada masti, hasi, aur dance! 💃  
    Chal milkar banate hain kuch naye yaadein, jaisa ki humesha karte aaye hain – full-on drama, full-on fun! 😄

    Tumhara saath sab kuch aur bhi rangin bana deta hai.  
    Toh taiyaar ho jao – outfits ready rakho, energy full charge karo, aur aa jao apne sabse pyare cousin ke saath shaadi ke maze lene! 😍

    **Bohot saara pyaar**,  
    _Tumhara favorite cousin_ 💜
    """)

    st.write("🕒 Aaj ki date aur time:", datetime.now().strftime("%A, %d %B %Y - %I:%M %p"))
    st.balloons()

# About Cousin Page
elif page == "👩‍❤️‍👨 About Vatsalla":
    st.title("👩‍❤️‍👨 Vatsalla – Ek Choti Si Kahani")
    st.markdown("""
    **Vatsalla Singh** – meri inspiration, meri sabse special partner, aur meri zindagi ki ek important hissa! 💖  
    Uski hansi, uska style, aur uski vibe – sab kuch ek dum classy hai! ✨

    ### Kuch khas baatein:
    - 🎨 Creativity mein master
    - 💬 Har kisi ki sunne wali aur dil se connect karne wali
    - 💃 Dance floor ki jaan
    - 📸 Har photo mein star jaisi shine karti hai

    Vatsalla, tu sirf ek cousin nahi – tu ek emotion hai 💕
    """)

# Memory Gallery Page
elif page == "🖼️ Memory Gallery":
    st.title("🖼️ Humari Yadein")
    st.markdown("Chalo ek baar un moments ko yaad karte hain jo hamesha dil ke kareeb rahenge 💫")

    st.image("vatsalla.png", caption="Wo lamhe jo hamesha yaad rahenge 💖", use_container_width=True)




# Message Wall Page
elif page == "💌 Message Wall":
    st.title("💌 Message Wall")
    st.subheader("Apna pyaar, wishes ya memories yahaan likho 💖")

    message = st.text_area("Vatsalla ke liye ek pyara message likho:")

    if st.button("Send"):
        st.success("Tumhara message Vatsalla tak pahunch gaya! 💌")
        st.balloons()
