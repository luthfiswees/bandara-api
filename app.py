import json
from flask import Flask, jsonify, request
import Levenshtein
import flight_library
import facility_library
import baggage_library

app = Flask(__name__)

# API for fetching flight
################################################################################
@app.route("/get_all_flight")
def get_flight():
    return jsonify(flight_library.get_flights())

@app.route("/get_flight_by_airline_name")
def get_flight_by_airline_name():
    flights = flight_library.get_flights()
    flights_by_airline = []

    for flight in flights:
        if flight['AIRLINE_NAME'] == request.args.get('airline_name'):
            flights_by_airline.append(flight)

    return jsonify(flights_by_airline)

@app.route("/get_flight_by_flight_number")
def get_flight_by_flight_number():
    flights = flight_library.get_flights()
    flights_by_flight_number = {}

    for flight in flights:
        if flight['FLIGHT_NO'] == request.args.get('flight_number'):
            flights_by_flight_number = flight

    return jsonify(flights_by_flight_number)

# API for fetching restaurant
################################################################################
@app.route("/get_all_restaurant")
def get_restaurant():
    return jsonify(facility_library.get_restaurants())

@app.route("/get_restaurant_by_name")
def get_restaurant_by_name():
    restaurants = facility_library.get_restaurants()
    restaurant_by_name = {}
    levenshtein_distance = -1

    for restaurant in restaurants:
        current_distance = Levenshtein.distance(str(restaurant['OBJECT_NAME']).lower(), str(request.args.get('restaurant_name')).lower())
        if current_distance == 0:
            restaurant_by_name = restaurant
            break
        if current_distance <= levenshtein_distance or levenshtein_distance < 0:
            restaurant_by_name = restaurant
            levenshtein_distance = current_distance

    return jsonify(restaurant_by_name)

@app.route("/get_restaurant_by_category")
def get_restaurant_by_category():
    with open('restaurants.json') as data:
        restaurants = json.load(data)
    restaurant_by_category = []
    category_name = request.args.get('restaurant_category')

    for restaurant in restaurants:
        if restaurant['RESTAURANT_CATEGORY'] == category_name:
            restaurant_by_category.append(restaurant)

    return jsonify(restaurant_by_category)

# API for fetching facility
################################################################################
@app.route("/get_all_facility")
def get_facilities():
    return jsonify(facility_library.get_facilities())

@app.route("/get_taxi_service")
def get_taxis():
    facilities = facility_library.get_facilities()
    taxis = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Taxi':
            taxis.append(facility)

    return jsonify(taxis)

@app.route("/get_car_rental")
def get_car_rentals():
    facilities = facility_library.get_facilities()
    rentals = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Rent Car':
            rentals.append(facility)

    return jsonify(rentals)

@app.route("/get_shuttle_bus")
def get_shuttle_busses():
    facilities = facility_library.get_facilities()
    shuttle_busses = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Shuttle Service':
            shuttle_busses.append(facility)

    return jsonify(shuttle_busses)

@app.route("/get_parking_facility")
def get_parking_facilities():
    facilities = facility_library.get_facilities()
    parking_facilities = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Parking':
            parking_facilities.append(facility)

    return jsonify(parking_facilities)

@app.route("/get_atm")
def get_atms():
    facilities = facility_library.get_facilities()
    atms = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'ATM':
            atms.append(facility)

    return jsonify(atms)

@app.route("/get_mosque")
def get_mosques():
    facilities = facility_library.get_facilities()
    mosques = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Mosque':
            mosques.append(facility)

    return jsonify(mosques)

@app.route("/get_money_changer")
def get_money_changer():
    facilities = facility_library.get_facilities()
    money_changers = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Money Changer':
            money_changers.append(facility)

    return jsonify(money_changers)

@app.route("/get_bank")
def get_banks():
    facilities = facility_library.get_facilities()
    banks = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Bank':
            banks.append(facility)

    return jsonify(banks)

@app.route("/get_toilet")
def get_toilets():
    facilities = facility_library.get_facilities()
    toilets = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Toilet':
            toilets.append(facility)

    return jsonify(toilets)

@app.route("/get_baggage_wrapping")
def get_baggage_wrappings():
    facilities = facility_library.get_facilities()
    baggage_wrappings = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Baggage Wrapping':
            baggage_wrappings.append(facility)

    return jsonify(baggage_wrappings)

@app.route("/get_travel")
def get_travels():
    facilities = facility_library.get_facilities()
    travels = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Travel':
            travels.append(facility)

    return jsonify(travels)

@app.route("/get_nursery_room")
def get_nursery_rooms():
    facilities = facility_library.get_facilities()
    nursery_rooms = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Nursery Room':
            nursery_rooms.append(facility)

    return jsonify(nursery_rooms)

@app.route("/get_smoking_room")
def get_smoking_rooms():
    facilities = facility_library.get_facilities()
    smoking_rooms = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Smooking Room':
            smoking_rooms.append(facility)

    return jsonify(smoking_rooms)

@app.route("/get_baggage_service")
def get_left_baggage_services():
    facilities = facility_library.get_facilities()
    baggage_services = []

    for facility in facilities:
        if facility['CATEGORY_NAME_ENG'] == 'Left Baggage Service' or facility['CATEGORY_NAME_ENG'] == 'Baggage Services':
            baggage_services.append(facility)

    return jsonify(baggage_services)

@app.route("/get_hotel")
def get_all_hotel():
    return jsonify(facility_library.get_hotels())

@app.route("/get_shop")
def get_shops():
    return jsonify(facility_library.get_shops())

# API for fetching important phone numbers
################################################################################
@app.route("/get_important_numbers")
def get_important_numbers():
    return jsonify(facility_library.get_important_numbers())

@app.route("/get_airline_numbers")
def get_airline_numbers():
    numbers = facility_library.get_important_numbers()
    airline_numbers = []

    for number in numbers:
        if number['CATEGORY_NAME_ENG'] == 'Airlines':
            airline_numbers.append(number)

    return jsonify(airline_numbers)

# API for fetching baggages data
################################################################################
@app.route("/get_baggage_claim_data")
def get_baggage_data():
    return jsonify(baggage_library.get_baggages())
