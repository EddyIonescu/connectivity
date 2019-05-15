import partridge as ptg


inpath = 'inputs/SF_gtfs.zip'
# future: get the GTFS files from S3 (by default do it for all agencies)

# open them in partridge
_date, service_ids = ptg.read_busiest_date(inpath)
view = {
    'trips.txt': {'service_id': service_ids},
}
feed = ptg.load_feed(inpath, view)
# We define a VisualTrip as a trip, but with the unique ID being trip_headsign or
# route_short_name || route_name + ' ' + trip_headsign if does not contain the route name in it (varies between agencies).
# Each VisualTrip has a list of trip_ids,
# but one shape, which is the result of merging the shapes from each trip,
# and one list of stop_times, which are joined together.
# This is done to address cases like Muni's 38 Geary, which goes to Lands End or V.A Hospital, but both go to SF Transit Center inbound
# or like the TTC's 25 Don Mills, where the 25B and 25C branches have no overlap (it's a split of the route).
routes = {
    route.route_id: route for route in feed.routes
}
visual_trips = {}
# aggregate VisualTrips
for trip in feed.trips:
    route_short_name = routes[trip['route_id']].route_short_name or routes[trip['route_id']].route_name
    trip_headsign = trip['trip_headsign']
    visual_trip_key = trip_headsign if trip_headsign.contains(route_short_name) else route_short_name + ' ' + trip_headsign
    visual_trip = visual_trips.get(visual_trip_key, {
        'trip_ids': [],
        'shape': {},
        'stop_times': [],
    })
    # add trip_id

    # add shape

    # add stop times
    

# For each service period, determine the style to be used for drawing the shape based on anayzing the stop_times for the given service period config



# write a geojson of the agency for each service period

