import streamlit as st
from pathlib import Path
from utils.helpers import load_data, render_profession_card, render_roadmap
from models.bert_recommender import get_recommendations
from models.roadmap_generator import generate_roadmap

# Configuration
st.set_page_config(
    page_title="ELEVATE Career Guide",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Initialize
    BASE_DIR = Path(__file__).parent.parent
    
    # Header
    st.title("🚀 ELEVATE Career Guide")
    st.markdown("### AI-powered career path recommendations")
    st.markdown("---")
    
    # Load data
    try:
        careers_df, _ = load_data(BASE_DIR)
        careers_df['keywords'] = careers_df['keywords'].str.lower()
    except Exception as e:
        st.error(f"Data loading failed: {str(e)}")
        return
    
    # User input
    user_input = st.text_area(
        "**Describe your interests:**",
        placeholder="e.g., 'I enjoy analyzing data and building models'",
        height=100
    )
    
    if st.button("✨ Get Recommendations") and user_input:
        with st.spinner("Finding your best career matches..."):
            try:
                # Get recommendations
                recommendations = get_recommendations(user_input.lower(), careers_df)
                
                if not recommendations.empty:
                    st.success(f"Found {len(recommendations)} career options:")
                    
                    # Show career options
                    for i, row in recommendations.iterrows():
                        render_profession_card(
                            row['profession'],
                            row['skills'],
                            row['resources'],
                            i
                        )
                    
                    # Roadmap display
                    selected = st.selectbox(
                        "**Select a career for roadmap:**",
                        recommendations['profession']
                    )
                    
                    roadmap = generate_roadmap(selected)
                    render_roadmap(roadmap)
                
                else:
                    st.warning("No matches found. Try different keywords")
            
            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()