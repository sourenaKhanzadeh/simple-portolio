import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Sourena Khanzadeh")
    content = """
        Hello! I'm Suren, a passionate and driven Ph.D. student in Computer Science with a specialized focus on Reinforcement Learning (RL) in the dynamic realm of cybersecurity. My academic journey is a testament to my commitment to unraveling the complexities of cutting-edge technology and its applications in safeguarding digital landscapes.

In the vast expanse of computer science, my research delves into the fascinating intersection of RL and cybersecurity. I am dedicated to understanding how RL algorithms can be harnessed to enhance the resilience of systems, fortify defenses against cyber threats, and pioneer innovative solutions to the ever-evolving challenges in the digital domain.

My academic pursuits have equipped me with a robust foundation in both theoretical and practical aspects of computer science. From exploring the depths of RL frameworks to dissecting intricate cybersecurity paradigms, I am continually pushing the boundaries of knowledge in pursuit of groundbreaking insights. My research not only seeks to contribute to the academic discourse but also aims to have a tangible impact on the real-world security landscape.

Beyond the realm of academia, I am an avid advocate for collaboration and knowledge sharing. I thrive on engaging with fellow researchers, industry professionals, and enthusiasts alike, fostering a community-driven approach to addressing the multifaceted issues surrounding cybersecurity.

As I navigate the exciting and challenging landscape of doctoral research, my goal is to bridge the gap between theoretical advancements and practical implementations. Through my work, I aspire to make meaningful contributions to the field of RL in cybersecurity, ultimately shaping a more secure and resilient digital future.

Join me on this intellectual journey where curiosity meets computation, and together, let's unravel the mysteries of the digital world!
    """
    st.info(content)

content2 = """
    Below you can find some of the apps I have built. Feel free to contact me!
"""
st.write(content2)


col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")