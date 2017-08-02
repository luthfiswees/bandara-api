# Bandara API

Used for Airport Chatbot Assistant
Currently live on `https://airport-bot-assistant.herokuapp.com/`


## Local Setup

There's some things that you need to setup.
- Off course, clone this repo, duh!
- Setup `virtualenv`
- Run your app

#### Setup `virtualenv`

- Install `pip` on your local computer. Make it global.
- Run this command ->  ``` pip install virtualenv ```
- `cd` to your directory where you clone the repo.
- There should be a directory named `venv`, activate it by using this -> ```source  venv/bin/activate ```. Your virtual environment should bootup by now.
- Then you should install project dependency by executing this command -> ``` pip install -r requirements.txt```. You could lookup the dependency of this project on `requirements.txt`.

#### Run your app

Now you can run the app by executing `gunicorn apps:app`


## API Details

#### Get All Flight
- URL: `/get_all_flight`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Flight by Airline Name
- URL: `/get_flight_by_airline_name`
- Method: GET
- Params: `airline_name`
- Return Value: JSON List

#### Get Flight by Flight Number
- URL: `/get_flight_by_flight_number`
- Method: GET
- Params: `flight_number`
- Return Value: JSON Object

#### Get All Restaurant
- URL: `/get_all_restaurant`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Restaurant by Name
- URL: `/get_restaurant_by_name`
- Method: GET
- Params: `restaurant_name`
- Return Value: JSON Object

#### Get All Facility
- URL: `/get_all_facility`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Taxi Service facilities
- URL: `/get_taxi_service`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Car Rental facilities
- URL: `/get_car_rental`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Shuttle Bus facilities
- URL: `/get_shuttle_bus`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Parking facilities
- URL: `/get_parking_facility`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get ATM facilities
- URL: `/get_atm`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Mosque facilities
- URL: `/get_mosque`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Money Changer facilities
- URL: `/get_money_changer`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Bank facilities
- URL: `/get_bank`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Toilet
- URL: `/get_toilet`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Baggage Wrapping facilities
- URL: `/get_baggage_wrapping`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Travel facilities
- URL: `/get_travel`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Nursery facilities
- URL: `/get_nursery_room`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Smoking Room facilities
- URL: `/get_smoking_room`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Baggage Service facilities
- URL: `/get_baggage_service`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Hotel facilities
- URL: `/get_hotel`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Shop facilities
- URL: `/get_shop`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Important Phone Numbers
- URL: `/get_important_numbers`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Airline Phone Numbers
- URL: `/get_airline_numbers`
- Method: GET
- Params: None
- Return Value: JSON List

#### Get Baggage Claim Data
- URL: `/get_baggage_claim_data`
- Method: GET
- Params: None
- Return Value: JSON List
