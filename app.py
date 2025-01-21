import pandas as pd
import streamlit as st
# from pandas.api.types import (
#     # is_categorical_dtype,
#     # # is_datetime64_any_dtype,
#     # is_numeric_dtype,
#     # is_object_dtype,
# )


# Setting page layout
st.set_page_config(
    page_title = "Associations of Exotic Insects with Plants in NZ",
    page_icon = "./static/icon.png",
    layout = "wide"
)

st.image('./static/icon.png', width = 100)
st.title("Associations of Exotic Insects with Plants in NZ")

tab1, tab2 = st.tabs(["About", "Data"])

with tab1:
    st.header("Background")
    st.markdown("There is concern that exotic insect herbivores may attack and damage plant species that are native and endemic to New Zealand. Having comprehensive data will allow robust analyses and underpin improved risk assessments for native plants.")
    st.markdown("Here we present 7946 records of exotic insect species in New Zealand and their associations with >1000 plant taxa. The dataset represents >260 insect species from several major groups of plant-feeding insects (herbivores), including aphids, leafhoppers, thrips, weevils, and scale insects (armoured scales, soft scales, mealybugs). Plant taxa include endemic species (only found in New Zealand); indigenous species (found naturally in New Zealand but also elsewhere); and exotic species (either accidentally or deliberately introduced into New Zealand by humans).")
    st.header("Instructions")
    st.markdown("Dropdown menus in the Data tab can be used to filter information on insect-plant associations. Either select or type your filter options. Filtered data can be downloaded by clicking the download button that appears when hovering over the table.")
    st.header("Sources of information")
    st.markdown("Insect specimens are from the New Zealand Arthropod Collection (except for data on aphids, see below) and are either pinned or slide mounted. Information on labels attached to insect specimens was manually transcribed.")
    st.markdown("Only some data fields are available here; complete records are available as Darwin Core in GBIF (https://www.gbif.org/) within the datasets: 'New Zealand Arthropod Collection (NZAC)'' or 'New Zealand Arthropod Collection - Symbiota'.")
    st.markdown("##### The aphids were initially digitised as a TFBIS project and include records from several international and New Zealand institutions")
    st.markdown(
    """
    - AQNZ. AsureQuality, Auckland, NZ
    - BMNH. Natural History Museum, London, United Kingdom
    - CNC. Canadian National Collection, Agriculture and Agri-food Canada, Ottawa, Canada
    - EMEC. Essig Collection, Berkeley, California, USA
    - FRNZ. Scion, Rotorua, NZ
    - LUNZ. Entomology Museum Lincoln University, Lincoln, NZ
    - MONZ. Te Papa, Wellington, NZ
    - NZAC. NZ Arthropod Collection, Landcare Research, Auckland, NZ
    - PANZ. Plant & Food Research, Lincoln, NZ
    - PCNZ. Plant Health Auckland, Ministry of Primary Industries, Auckland, NZ
    - PFNZ. Plant Health Christchurch, Ministry of Primary Industries, Christchurch, NZ
    """
    )
    st.markdown("##### Plant names and biostatus were obtained from google searches and the following:")
    st.markdown(
    """
    - NZOR. NZ Organisms Register (https://www.nzor.org.nz/)
    - NZPCN. NZ Plant Conservation Network (https://www.nzpcn.org.nz/)
    - GBIF. Global Biodiversity and Information Facility (https://www.gbif.org/)
    """
    )
    st.markdown(
        """
    <style> [data-testid="stMarkdownContainer"] ul{list-style-position: inside;} </style>
    """, unsafe_allow_html=True
    )
    st.markdown("The taxonomic names of the insect species were cross-referenced with GBIF.")
    st.header("Funding")
    st.markdown("These data were obtained and made accesible by funding from several sources, including: the Terrestrial and Freshwater Biodiversity Information System (TIFBIS) fund; SSIF infrastructure funding to the New Zealand Arthropod Collection; and more recently from SSIF funding through the B3 science collaboration (Better Border Biosecurity) and specifically projects B19.2 Supporting pest risk assessments in natural ecosystems and B22.6 Predicting the spillover of pests and pathogens into natural ecosystems.")
    st.header("Personnel")
    st.markdown("Manaaki Whenua Landcare Research: Darren Ward, Aaron Harmer")


with tab2:
    st.write("Use the filters below to search for insect-plant associations.")

    def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        modification_container = st.container()

        with modification_container:
            col1, col2 = st.columns([1,1])
            with col1:
                to_filter_columns = st.multiselect("Filter dataframe on", df.columns)
                for column in to_filter_columns:
                    dent, left, cent, right = st.columns([0.25,0.25,3,0.5])
                    left.write("↳")
                    user_cat_input = cent.multiselect(
                        f"Values for {column}",
                        df[column].unique(),   
                    )
                    df = df[df[column].isin(user_cat_input)]

        return df


    df = pd.read_csv('./static/plant_insect_dat.csv', encoding='utf-8')
    df = df.convert_dtypes()
    st.dataframe(filter_dataframe(df))