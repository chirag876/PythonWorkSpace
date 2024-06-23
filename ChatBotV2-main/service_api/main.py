from flask import Flask, request
import weather_api, timezone_api, translation_api, speech_recognition_api, pdf_api, facts_api
import risk_and_enhanced_property_details_api
import risk_and_enhanced_property_details_with_replacement_cost_data_api
import hazard_hub_api, rater_api

app = Flask(__name__)


@app.route("/timezone", methods=["GET", "POST"])
def timezone():
    city_name = request.args.get("city_name")
    return timezone_api.time_zone(city_name)


@app.route("/weather",  methods=["GET", "POST"])
def weather():
    city_name = request.args.get("city_name")
    return weather_api.weather_by_city_name(city_name)


@app.route("/translate", methods=["GET", "POST"])
def translation():
    lang_from = request.args.get("lang_from")
    lang_to = request.args.get("lang_to")
    text = request.args.get("text")
    return translation_api.translate_text(lang_from, lang_to, text)


@app.route("/speech", methods=["GET", "POST"])
def speech():
    return str(speech_recognition_api.SpeakText())


@app.route("/pdf", methods=["GET", "POST"])
def pdf():
    pdf_name = request.args.get("pdf_name")
    return str(pdf_api.generate_pdf(pdf_name))


@app.route("/facts",  methods=["GET", "POST"])
def facts():
    limit = request.args.get("limit")
    return facts_api.facts(limit)

@app.route("/riskandenhancedpropertydetails", methods=["GET", "POST"])
def riskandenhancedpropertydetails():
    address = request.args.get("address")
    city = request.args.get("city")
    state = request.args.get("state")
    zip = request.args.get("zipcode")
    return risk_and_enhanced_property_details_api.risk_and_enhanced_property_details(address, city, state, zip)

@app.route("/riskandenhancedpropertydetailswithreplacementcostdata", methods=["GET", "POST"])
def riskandenhancedpropertydetailswithreplacementcostdata():
    address = request.args.get("address")
    city = request.args.get("city")
    state = request.args.get("state")
    zip = request.args.get("zipcode")
    return risk_and_enhanced_property_details_with_replacement_cost_data_api.risk_and_enhanced_property_details_with_replacement_cost_data(address, city, state, zip)

@app.route("/hazardhub", methods=["GET", "POST"])
def hazard_hub():
    data = request.get_json()
    return hazard_hub_api.hazard_hub(data)

@app.route("/rater", methods=["GET", "POST"])
def rater():
    return rater_api.rater()

if __name__ == "__main__":
    app.run(debug=True, port='8080')