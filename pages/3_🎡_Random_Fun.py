import os

import streamlit as st
import time
import numpy as np
import pandas as pd

st.set_page_config(page_title="Random Fun!", page_icon="🎡", layout="wide")


st.success("Coming Soon!")
selected = st.selectbox("Choose Demo", options=['Plotting Demo', 'Mapping Demo'])
if selected == 'Plotting Demo':
    st.markdown("# Plotting Demo")
    st.sidebar.header("Plotting Demo")
    st.write(
        """This demo illustrates a combination of plotting and animation with
    Streamlit. We're generating a bunch of random numbers in a loop for around
    5 seconds. Enjoy!"""
    )

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()

    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")
elif selected == 'Mapping Demo':
    DATE_COLUMN = 'date/time'
    DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                'streamlit-demo-data/uber-raw-data-sep14.csv.gz')


    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data




    import altair as alt
    import numpy as np
    import pandas as pd
    import pydeck as pdk
    import streamlit as st

    # SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON


    # LOAD DATA ONCE
    @st.experimental_singleton
    def load_data(nrows):
        data = pd.read_csv(
            DATA_URL,
            nrows=nrows,  # approx. 10% of data
            names=[
                "date/time",
                "lat",
                "lon",
            ],  # specify names directly since they don't change
            skiprows=1,  # don't read header since names specified directly
            usecols=[0, 1, 2],  # doesn't load last column, constant value "B02512"
            parse_dates=[
                "date/time"
            ],  # set as datetime instead of converting after the fact
        )

        return data


    # FUNCTION FOR AIRPORT MAPS
    def map(data, lat, lon, zoom):
        st.write(
            pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state={
                    "latitude": lat,
                    "longitude": lon,
                    "zoom": zoom,
                    "pitch": 50,
                },
                layers=[
                    pdk.Layer(
                        "HexagonLayer",
                        data=data,
                        get_position=["lon", "lat"],
                        radius=100,
                        elevation_scale=4,
                        elevation_range=[0, 1000],
                        pickable=True,
                        extruded=True,
                    ),
                ],
            )
        )


    # FILTER DATA FOR A SPECIFIC HOUR, CACHE
    @st.experimental_memo
    def filterdata(df, hour_selected):
        return df[df["date/time"].dt.hour == hour_selected]


    # CALCULATE MIDPOINT FOR GIVEN SET OF DATA
    @st.experimental_memo
    def mpoint(lat, lon):
        return (np.average(lat), np.average(lon))


    # FILTER DATA BY HOUR
    @st.experimental_memo
    def histdata(df, hr):
        filtered = data[
            (df["date/time"].dt.hour >= hr) & (df["date/time"].dt.hour < (hr + 1))
            ]

        hist = np.histogram(filtered["date/time"].dt.minute, bins=60, range=(0, 60))[0]

        return pd.DataFrame({"minute": range(60), "pickups": hist})


    # STREAMLIT APP LAYOUT
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(10000)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text('Loading data...done!')

    # LAYING OUT THE TOP SECTION OF THE APP
    row1_1, row1_2 = st.columns((2, 3))

    # SEE IF THERE'S A QUERY PARAM IN THE URL (e.g. ?pickup_hour=2)
    # THIS ALLOWS YOU TO PASS A STATEFUL URL TO SOMEONE WITH A SPECIFIC HOUR SELECTED,
    # E.G. https://share.streamlit.io/streamlit/demo-uber-nyc-pickups/main?pickup_hour=2
    if not st.session_state.get("url_synced", False):
        try:
            pickup_hour = int(st.experimental_get_query_params()["pickup_hour"][0])
            st.session_state["pickup_hour"] = pickup_hour
            st.session_state["url_synced"] = True
        except KeyError:
            pass


    # IF THE SLIDER CHANGES, UPDATE THE QUERY PARAM
    def update_query_params():
        hour_selected = st.session_state["pickup_hour"]
        st.experimental_set_query_params(pickup_hour=hour_selected)


    with row1_1:
        st.title("NYC Uber Ridesharing Data")
        hour_selected = st.slider(
            "Select hour of pickup", 0, 23, key="pickup_hour", on_change=update_query_params
        )

    with row1_2:
        st.write(
            """
        ##
        Examining how Uber pickups vary over time in New York City's and at its major regional airports.
        By sliding the slider on the left you can view different slices of time and explore different transportation trends.
        """
        )

    # LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS
    row2_1, row2_2, row2_3, row2_4 = st.columns((2, 1, 1, 1))

    # SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
    la_guardia = [40.7900, -73.8700]
    jfk = [40.6650, -73.7821]
    newark = [40.7090, -74.1805]
    zoom_level = 12
    midpoint = mpoint(data["lat"], data["lon"])

    with row2_1:
        st.write(
            f"""**All New York City from {hour_selected}:00 and {(hour_selected + 1) % 24}:00**"""
        )
        map(filterdata(data, hour_selected), midpoint[0], midpoint[1], 11)

    with row2_2:
        st.write("**La Guardia Airport**")
        map(filterdata(data, hour_selected), la_guardia[0], la_guardia[1], zoom_level)

    with row2_3:
        st.write("**JFK Airport**")
        map(filterdata(data, hour_selected), jfk[0], jfk[1], zoom_level)

    with row2_4:
        st.write("**Newark Airport**")
        map(filterdata(data, hour_selected), newark[0], newark[1], zoom_level)

    # CALCULATING DATA FOR THE HISTOGRAM
    chart_data = histdata(data, hour_selected)

    # LAYING OUT THE HISTOGRAM SECTION
    st.write(
        f"""**Breakdown of rides per minute between {hour_selected}:00 and {(hour_selected + 1) % 24}:00**"""
    )

    st.altair_chart(
        alt.Chart(chart_data)
        .mark_area(
            interpolate="step-after",
        )
        .encode(
            x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
            y=alt.Y("pickups:Q"),
            tooltip=["minute", "pickups"],
        )
        .configure_mark(opacity=0.2, color="red"),
        use_container_width=True,
    )