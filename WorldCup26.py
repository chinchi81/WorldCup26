#!/usr/bin/env python
# coding: utf-8

# In[13]:


#!/usr/bin/env python
# coding: utf-8

# In[71]:


import streamlit as st

st.set_page_config(page_title="World Cup 2026 Predictions", layout="wide")
st.cache_data.clear()


st.title("World Cup 2026 Predictions")

# Define tabs
tab_names = ["Group Fixtures", "Group Tables", "KO Probabilities", "Final Pathway"]
tabs = st.tabs(tab_names)

for tab, sheet in zip(tabs, tab_names):
    with tab:
        # --- Group Fixtures: only embed Datawrapper chart ---
        if sheet == "Group Fixtures":
            iframe = """
            <iframe src="https://datawrapper.dwcdn.net/aiSgh/" 
                    width="100%" 
                    height="100%" 
                    style="min-height: 90vh;" 
                    frameborder="0"></iframe>
            """
            st.components.v1.html(iframe, height=3800)

        # --- Group Tables: embed two Datawrapper charts under each other ---
        elif sheet == "Group Tables":
            subtab_names = ["Pre-Tournament", "Post 1st Round"]
            subtabs = st.tabs(subtab_names)
    
            with subtabs[0]:
                iframeA = """
                <iframe src="https://datawrapper.dwcdn.net/QltVC/" 
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeA, height=300)
                
                iframeB = """
                <iframe src="https://datawrapper.dwcdn.net/kZtBl/" 
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeB, height=240)
                
                iframeC = """
                <iframe src="https://datawrapper.dwcdn.net/HeaHl/" 
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeC, height=240)
                
                iframeD = """
                <iframe src="https://datawrapper.dwcdn.net/udsqv/" 
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeD, height=240)
                
                iframeE = """
                <iframe src="https://datawrapper.dwcdn.net/iApRy/" 
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeE, height=240)
                
                iframeF = """
                <iframe src="https://datawrapper.dwcdn.net/ZAWqK/" 
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeF, height=240)
                
                iframeG = """
                    <iframe src="https://datawrapper.dwcdn.net/c7H5c/" 
                            width="100%" 
                            height="500" 
                            frameborder="0"></iframe>
                    """
                st.components.v1.html(iframeG, height=240)
                
                iframeH = """
                    <iframe src="https://datawrapper.dwcdn.net/am0Vc/" 
                            width="100%" 
                            height="500" 
                            frameborder="0"></iframe>
                    """
                st.components.v1.html(iframeH, height=240)

                iframeI = """
                    <iframe src="https://datawrapper.dwcdn.net/qOcPa/" 
                            width="100%" 
                            height="500" 
                            frameborder="0"></iframe>
                    """
                st.components.v1.html(iframeI, height=240)
                
                iframeJ = """
                    <iframe src="https://datawrapper.dwcdn.net/BcWlG/" 
                            width="100%" 
                            height="500" 
                            frameborder="0"></iframe>
                    """
                st.components.v1.html(iframeJ, height=240)
                
                iframeK = """
                    <iframe src="https://datawrapper.dwcdn.net/hVQNb/" 
                            width="100%" 
                            height="500" 
                            frameborder="0"></iframe>
                    """
                st.components.v1.html(iframeK, height=240)
                
                iframeL = """
                    <iframe src="https://datawrapper.dwcdn.net/0nLmw/" 
                            width="100%" 
                            height="500" 
                            frameborder="0"></iframe>
                    """
                st.components.v1.html(iframeL, height=240)
                
                iframe3RD = """
                    <iframe src="https://datawrapper.dwcdn.net/n1Aaq/" 
                            width="100%" 
                            height="500" 
                            frameborder="0"></iframe>
                    """
                st.components.v1.html(iframe3RD, height=1250)

            with subtabs[1]:
                iframeA1 = """
                <iframe src="https://datawrapper.dwcdn.net/ekKYs/" 
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeA1, height=300)
                
                iframeB1 = """
                <iframe src="https://datawrapper.dwcdn.net/qRGT2/" 
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeB1, height=240)
                
                iframeC1 = """
                <iframe src="https://datawrapper.dwcdn.net/hPh5I/" 
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeC1, height=240)
                
                iframeD1 = """
                <iframe src="https://datawrapper.dwcdn.net/Ok1oz/"
                        width="100%" 
                        height="500" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframeD1, height=240)
                
                #iframeE1 = """
                #<iframe src="https://datawrapper.dwcdn.net/WXrOy/" 
                #        width="100%" 
                #        height="500" 
                #        frameborder="0"></iframe>
                #"""
                #st.components.v1.html(iframeE1, height=240)
                
                #iframeF1 = """
                #<iframe src="https://datawrapper.dwcdn.net/6wlnt/" 
                #        width="100%" 
                #        height="500" 
                #        frameborder="0"></iframe>
                #"""
                #st.components.v1.html(iframeF1, height=240)
                
                #iframeG1 = """
                #    <iframe src="https://datawrapper.dwcdn.net/zBvIH/" 
                #            width="100%" 
                #            height="500" 
                #            frameborder="0"></iframe>
                #    """
                #st.components.v1.html(iframeG1, height=240)
                
                #iframeH1 = """
                #    <iframe src="https://datawrapper.dwcdn.net/TYr4v/" 
                #            width="100%" 
                #            height="500" 
                #            frameborder="0"></iframe>
                #    """
                #st.components.v1.html(iframeH1, height=240)

                #iframeI1 = """
                #    <iframe src="https://datawrapper.dwcdn.net/HDiZE/" 
                #            width="100%" 
                #            height="500" 
                #            frameborder="0"></iframe>
                #    """
                #st.components.v1.html(iframeI1, height=240)
                
                #iframeJ1 = """
                #    <iframe src="https://datawrapper.dwcdn.net/X6ToB/" 
                #            width="100%" 
                #            height="500" 
                #            frameborder="0"></iframe>
                #    """
                #st.components.v1.html(iframeJ1, height=240)
                
                #iframeK1 = """
                #    <iframe src="https://datawrapper.dwcdn.net/bMyEC/" 
                #            width="100%" 
                #            height="500" 
                #            frameborder="0"></iframe>
                #    """
                #st.components.v1.html(iframeK1, height=240)
                
                #iframeL1 = """
                #    <iframe src="https://datawrapper.dwcdn.net/mOKZ6/" 
                #            width="100%" 
                #            height="500" 
                #            frameborder="0"></iframe>
                #    """
                #st.components.v1.html(iframeL1, height=240)
                
                iframe3RD1 = """
                    <iframe src="https://datawrapper.dwcdn.net/CAJRr/" 
                            width="100%" 
                            height="500" 
                            frameborder="0"></iframe>
                    """
                st.components.v1.html(iframe3RD1, height=1250)

        # --- Stage Probabilities: placeholder ---
        elif sheet == "KO Probabilities":
            subtab_names = ["Pre-Tournament", "Post 1st Round"]
            subtabs = st.tabs(subtab_names)

            with subtabs[0]:
                iframe = """
                <iframe src="https://datawrapper.dwcdn.net/BDQ4f/" 
                        width="100%" 
                        height="100%" 
                        style="min-height: 90vh;" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframe, height=2800)

            with subtabs[1]:
                iframe = """
                <iframe src="https://datawrapper.dwcdn.net/aw8iw/" 
                        width="100%" 
                        height="100%" 
                        style="min-height: 90vh;" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframe, height=2800)

        # --- Stage Probabilities: placeholder ---
        elif sheet == "Final Pathway":
            subtab_names = ["Pre-Tournament", "Post 1st Round"]
            subtabs = st.tabs(subtab_names)

            with subtabs[0]:
                iframe = """
                <iframe src="https://datawrapper.dwcdn.net/DFCtw/" 
                        width="100%" 
                        height="100%" 
                        style="min-height: 90vh;" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframe, height=2800)

            with subtabs[1]:
                iframe = """
                <iframe src="https://datawrapper.dwcdn.net/gT1y4/" 
                        width="100%" 
                        height="100%" 
                        style="min-height: 90vh;" 
                        frameborder="0"></iframe>
                """
                st.components.v1.html(iframe, height=2800)

        # --- Other tabs: placeholders ---
        else:
            st.info(f"{sheet} tab — visualization can be added here.")


# In[ ]:






# In[ ]:
