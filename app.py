import json, re, cgi
from flask import Flask, jsonify, request
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from pytz import timezone
import atexit
import Levenshtein
import flight_library
import facility_library
import baggage_library

app = Flask(__name__)
tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
tz = timezone('Asia/Jakarta')

# Function for scheduler
################################################################################
sched = BackgroundScheduler()
sched.start()
atexit.register(lambda: sched.shutdown())

def cetak_teks(teks):
    print("kentil")

def schedule_task(time_year, time_month, time_day, time_hour, time_minute):
    exec_date = tz.localize(datetime(time_year, time_month, time_day, time_hour, time_minute, 0))
    one_hour_notice = exec_date - timedelta(minutes=90)
    day_notice = exec_date - timedelta(days=1)

    # One day reminder and one hour and a half reminder
    sched.add_job(cetak_teks, 'date', run_date=one_hour_notice, args=['One Hour Reminder'])
    sched.add_job(cetak_teks, 'date', run_date=day_notice, args=['Previous Day Reminder'])

@app.route("/schedule_reminder")
def schedule_reminder():
    time_year = int(request.args.get('year'))
    time_month = int(request.args.get('month'))
    time_day = int(request.args.get('day'))
    time_hour = int(request.args.get('hour'))
    time_minute = int(request.args.get('minute'))

    response = {}
    try:
        schedule_task(time_year, time_month, time_day, time_hour, time_minute)
        response['error'] = 'no'
        return jsonify(response)
    except Exception as e:
        print e
        response['error'] = 'yes'
        return jsonify(response)

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
            break

    flight_info = {}
    flight_info['data'] = flights_by_flight_number
    if flights_by_flight_number == {}:
        flight_info['error'] = "yes"
    else:
        flight_info['error'] = "no"

        got  = flight['GATE_OPEN_TIME']
        gct  = flight['GATE_CLOSE_TIME']
        bcot = flight['BAGGAGE_CLAIM_OPEN_TIME']
        bcct = flight['BAGGAGE_CLAIM_CLOSE_TIME']

        got_day = None
        got_month = None
        got_year = None
        got_hour = None
        got_minute = None

        gct_day = None
        gct_month = None
        gct_year = None
        gct_hour = None
        gct_minute = None

        bcot_day = None
        bcot_month = None
        bcot_year = None
        bcot_hour = None
        bcot_minute = None

        bcct_day = None
        bcct_month = None
        bcct_year = None
        bcct_hour = None
        bcct_minute = None

        if got != None:
            got_splits = got.split(" ")
            got_date = got_splits[0]
            got_clock = got_splits[1]

            got_date_splits = got_date.split("-")
            got_year = got_date_splits[0]
            got_month = got_date_splits[1]
            got_day = got_date_splits[2]

            got_clock_splits = got_clock.split(":")
            got_hour = got_clock_splits[0]
            got_minute = got_clock_splits[1]
        if gct != None:
            gct_splits = gct.split(" ")
            gct_date = gct_splits[0]
            gct_clock = gct_splits[1]

            gct_date_splits = gct_date.split("-")
            gct_year = gct_date_splits[0]
            gct_month = gct_date_splits[1]
            gct_day = gct_date_splits[2]

            gct_clock_splits = gct_clock.split(":")
            gct_hour = gct_clock_splits[0]
            gct_minute = gct_clock_splits[1]
        if bcot != None:
            bcot_splits = bcot.split(" ")
            bcot_date = bcot_splits[0]
            bcot_clock = bcot_splits[1]

            bcot_date_splits = bcot_date.split("-")
            bcot_year = bcot_date_splits[0]
            bcot_month = bcot_date_splits[1]
            bcot_day = bcot_date_splits[2]

            bcot_clock_splits = bcot_clock.split(":")
            bcot_hour = bcot_clock_splits[0]
            bcot_minute = bcot_clock_splits[1]
        if bcct != None:
            bcct_splits = bcct.split(" ")
            bcct_date = bcct_splits[0]
            bcct_clock = bcct_splits[1]

            bcct_date_splits = bcct_date.split("-")
            bcct_year = bcct_date_splits[0]
            bcct_month = bcct_date_splits[1]
            bcct_day = bcct_date_splits[2]

            bcct_clock_splits = bcct_clock.split(":")
            bcct_hour = bcct_clock_splits[0]
            bcct_minute = bcct_clock_splits[1]

        flight_info['data']['got_day'] = got_day
        flight_info['data']['got_month'] = got_month
        flight_info['data']['got_year'] = got_year
        flight_info['data']['got_hour'] = got_hour
        flight_info['data']['got_minute'] = got_minute

        flight_info['data']['gct_day'] = gct_day
        flight_info['data']['gct_month'] = gct_month
        flight_info['data']['gct_year'] = gct_year
        flight_info['data']['gct_hour'] = gct_hour
        flight_info['data']['gct_minute'] = gct_minute

        flight_info['data']['bcot_day'] = bcot_day
        flight_info['data']['bcot_month'] = bcot_month
        flight_info['data']['bcot_year'] = bcot_year
        flight_info['data']['bcot_hour'] = bcot_hour
        flight_info['data']['bcot_minute'] = bcot_minute

        flight_info['data']['bcct_day'] = bcct_day
        flight_info['data']['bcct_month'] = bcct_month
        flight_info['data']['bcct_year'] = bcct_year
        flight_info['data']['bcct_hour'] = bcct_hour
        flight_info['data']['bcct_minute'] = bcct_minute

    return jsonify(flight_info)

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
            temp = restaurant['OBJECT_ADDRESS']
            re.sub('<br />', '\n', temp)
            no_tags = tag_re.sub('', temp)
            ready = cgi.escape(no_tags)

            restaurant['OBJECT_ADDRESS'] = ready
            restaurant_by_category.append(restaurant)
        if len(restaurant_by_category) > 3:
            break

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
