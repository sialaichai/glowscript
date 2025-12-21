import streamlit as st
import streamlit.components.v1 as components
import json
# 2. Advanced CSS to remove margins but keep Sidebar controls
st.markdown("""
    <style>
        /* 1. Remove padding from the main block-container */
        .block-container {
            padding-top: 0rem;
            padding-bottom: 0rem;
            padding-left: 0rem;
            padding-right: 0rem;
        }

        /* 2. Target the specific element that creates the top white-space gap */
        .stAppViewMain {
            margin-top: -3rem;
        }

        /* 3. Keep the Sidebar toggle button visible and clickable */
        .st-emotion-cache-12fmjuu, .st-emotion-cache-6q9sum {
            background-color: rgba(255, 255, 255, 0.5); /* Makes it visible over simulation */
            border-radius: 50%;
            z-index: 999999;
        }

        /* 4. Ensure the iframe fills the exact screen height minus the title/guide */
        iframe {
            border: none;
            width: 100vw;
        }
        
        /* Optional: Hide the standard Streamlit decoration line at the top */
        [data-testid="stDecoration"] {
            display: none;
        }
    </style>
    """, unsafe_allow_html=True)

st.set_page_config(page_title="Physics Simulations Hub", layout="wide")

# Load data
def load_data():
    with open('simulations.json', 'r') as f:
        return json.load(f)

ANIMATIONS = load_data()

# --- SIDEBAR SEARCH & NAV ---
st.sidebar.title("Find Simulation")

# Create a flat list of all simulation names for the search/filter
all_sim_names = []
for topic in ANIMATIONS:
    all_sim_names.extend(ANIMATIONS[topic].keys())

# Add a text search box
search_query = st.sidebar.text_input("🔍 Search by name:", "").lower()

# Filter names based on search
filtered_names = [name for name in all_sim_names if search_query in name.lower()]

if search_query:
    # If searching, show the filtered results in a radio list
    selected_script = st.sidebar.radio("Search Results:", options=filtered_names)
    
    # Find which topic this belongs to for the display
    selected_topic = next(t for t in ANIMATIONS if selected_script in ANIMATIONS[t])
else:
    # Standard Navigation if not searching
    selected_topic = st.sidebar.selectbox("Choose a Topic:", options=list(ANIMATIONS.keys()))
    available_animations = list(ANIMATIONS[selected_topic].keys())
    selected_script = st.sidebar.radio("Select Animation:", options=available_animations)

# --- MAIN PANEL ---
current_data = ANIMATIONS[selected_topic][selected_script]
st.write("Tip: Use the search box in the sidebar to find animations across all topics.")
st.caption(f"Category: {selected_topic}")
st.title(selected_script)

st.markdown("### Guide")
st.info(current_data["description"])
#st.markdown("---")

components.iframe(current_data["url"], height=600, scrolling=False)

