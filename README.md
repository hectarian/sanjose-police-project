## 👮‍♂️ Police Incident Geocoding and Visualization: An ETL Project 🌎

<img src="https://github.com/hectarian/portfolio/blob/main/images/heatmap_SJ.png" width="850" alt="Heatmap-image">
* View my map in ArcGIS [here](https://osugisci.maps.arcgis.com/home/item.html?id=19bfe7cda5514ae3bfc6b4888ca34973)


### Overview
I created a Python script that performs ETL (Extract, Transform, Load) operations to generate geographic coordinates from CSV files containing addresses as text strings. This project was inspired by publicly available police incident data from the City of San Jose.

### Reasoning
While exploring the downloadable police incident reports from the San Jose city website, I noticed that the addresses of incident locations were provided as text fields. For example:

- "BIRD AV & COE AV" indicates a call originating from the intersection of Bird Avenue and Coe Avenue.
This sparked an idea: what if I could geolocate these text-based addresses and visualize the geographic distribution of incidents to identify hot spots? Such a visualization could not only provide valuable insights for analytical purposes but also potentially help the police optimize resource allocation and patrol strategies.

### Idea
The primary goals of this project were:

- Geolocate: Convert textual addresses into latitude and longitude coordinates.
- Visualize: Map the geolocated data to identify patterns, trends, and hot spots for police incidents.
- Analyze: Use analytics to tell a compelling story about incident distribution and demonstrate how such insights could assist decision-makers in the City of San Jose.

### ETL Process
This project follows a simplified ETL framework:

1. Extract:
  - Input: Read the CSV file containing police incident data with raw address fields.
2. Transform:
  - Standardize and clean address fields.
  - Append location context (San Jose, CA) to address strings.
  - Use the Nominatim API to geocode addresses into geographic coordinates.
  - Handle special cases such as intersections, ranges, and ambiguous addresses.
3. Load:
  - Append the geocoded latitude and longitude to the original dataset.
  - Save the enriched data into a new CSV file for further analysis and visualization.
    
### Steps Taken
1. Data Input: Loaded a CSV file with incident data containing address fields.
2. Address Transformation:
  - Appended "San Jose, CA" for context during geocoding.
  - Split and processed intersection-style addresses (e.g., "A & B") to find midpoint coordinates if needed.
3. Geocoding:
  - Utilized the Nominatim API to convert text addresses into geographic coordinates.
  - Handled timeouts, missing data, and edge cases to ensure robustness.
4. Output:
  - Saved the final dataset, enriched with latitude and longitude, into a new CSV file.
  - This file can be imported into GIS tools like ArcGIS or QGIS for visualization.
  - *** Some errors are still present regarding coordinates being generated outside of the target city. A temporary fix that I did was I opened the CSV file into ArcGIS and batched removed the points outside of my target area.

### Results
  - The processed data allows for the creation of heat maps showing police incident hot spots across the city of San Jose.
  - These visualizations could highlight high-frequency areas, aiding in data-driven decisions for resource allocation.
    
### Tools Used
  - Python: For scripting and data processing.
  - Nominatim API: For geocoding addresses.
  - Pandas: For data manipulation.
  - ArcGIS Online: For mapping and visualization of incident hot spots.

### Future Enhancements
  - Error Handling: The API and the script are not perfect. Some rows returned coordinates outside of my target city. 
  - Scalability: Adapt the script to handle larger datasets more efficiently using batch geocoding or parallel processing since the generation of the output file took several hours.
  - Interactive Dashboard: Integrate results into an interactive platform for real-time insights.
  - Predictive Analytics: Leverage historical data to predict future hot spots.

### Conclusion
This project demonstrates how public data can be transformed into actionable insights using a simple but effective ETL process. By visualizing police incident data, we can uncover patterns that help inform strategic decisions for public safety.

Feel free to explore the script and data, and let me know your thoughts or suggestions!
