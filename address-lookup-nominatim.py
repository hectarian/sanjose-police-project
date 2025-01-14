import pandas as pd
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut

def geocode_address(address):
    # Initialize Nominatim API with increased timeout
    geolocator = Nominatim(
        user_agent="my_intersection_finder",
        timeout=4  # Timeout in seconds
    )
    try:
        # Add context to address by appending 'San Jose, CA'
        address_with_context = f"{address}, San Jose, CA"
        location = geolocator.geocode(address_with_context, exactly_one=True)
        
        if location:
            return {
                'latitude': location.latitude,
                'longitude': location.longitude
            }
        else:
            # Attempt to find midpoint coordinates if original method fails
            street_names = address.split(' & ')
            if len(street_names) == 2:
                address1 = f"{street_names[0]} San Jose CA"
                address2 = f"{street_names[1]} San Jose CA"
                
                location1 = geolocator.geocode(address1, exactly_one=True)
                location2 = geolocator.geocode(address2, exactly_one=True)
                
                if location1 and location2:
                    midpoint_latitude = (location1.latitude + location2.latitude) / 2
                    midpoint_longitude = (location1.longitude + location2.longitude) / 2
                    
                    return {
                        'latitude': midpoint_latitude,
                        'longitude': midpoint_longitude
                    }
            return None
    except GeocoderTimedOut:
        print("The request timed out. Please try again.")
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

def main():
    # Load the original CSV file
    original_file = 'FULL-police-indient-reports-Q4-2024.csv'
    partial_file = 'geocoded_addresses_partial.csv'
    final_file = 'geocoded_addresses.csv'

    # Load the original file
    original_df = pd.read_csv(original_file)
    try:
        # If a partial file exists, load it and calculate how many rows have been processed
        partial_df = pd.read_csv(partial_file)
        processed_rows = len(partial_df)
        print(f"Resuming from row {processed_rows}.")
    except FileNotFoundError:
        # If no partial file exists, start fresh
        partial_df = pd.DataFrame()
        processed_rows = 0
        print("Starting from the beginning.")

    # Filter the remaining rows to process
    remaining_df = original_df.iloc[processed_rows:]

    # Process each row and append to the partial file
    results = []
    for idx, row in remaining_df.iterrows():
        result = geocode_address(row['ADDRESS'])
        if result:
            results.append(result)
        else:
            results.append({'latitude': None, 'longitude': None})

        # Add the result to the DataFrame
        row['latitude'] = results[-1]['latitude']
        row['longitude'] = results[-1]['longitude']
        partial_df = pd.concat([partial_df, pd.DataFrame([row])])

        # Save to partial file every 100 rows
        if len(partial_df) % 100 == 0:
            partial_df.to_csv(partial_file, index=False)
            print(f"Saved progress at row {len(partial_df)}.")

    # Save the final results to the final file
    partial_df.to_csv(final_file, index=False)
    print(f"Processing complete. Final file saved as {final_file}.")

if __name__ == "__main__":
    main()
