class Address:
    def __init__(self):
        self.city = "New York"
        self.countryCode = "US"
        self.countryName = "United States"
        self.line1 = "123 Main Street"
        self.postalCode = "10001"
        self.stateOrProvinceCode = "NY"
        self.stateOrProvinceName = "New York"
        self.detailAddress = DetailAddress()

class Business:
    def __init__(self):
        self.annualSales = 9999
        self.businessName = "ABC Company"
        self.id = "123456"
        self.NAICS = "123456"
        self.numberOfEmployeeTotal = 2500
        self.SIC = "987654"

class Communication:
    def __init__(self):
        self.phoneTypeCode = "phonecode"
        self.phoneNumber = "001-365-6445-897"
        self.websiteURL = "URL"

class Contact:
    def __init__(self):
        self.communication = []
        self.fullName = ""

class DetailAddress:
    def __init__(self):
        self.preDirectionCode = ""
        self.postDirectionCode = ""
        self.streetName = "Main"
        self.streetNumber = "123"
        self.streetTypeCode = "St"

class Insured:
    def __init__(self):
        self.address = Address()
        self.business = Business()
        self.contact = Contact()

class Location:
    def __init__(self):
        self.city = "New York"
        self.countryCode = "US"
        self.endDate = "31/12/2023"
        self.line1 = "456 Elm Street"
        self.postalCode = "10002"
        self.stateOrProvinceCode = "NY"
        self.startDate = "01/01/2023"

class ResponseMessageInformation:
    def __init__(self):
        self.businessPurposeTypeCode = "SubmitGeneralLiabilityQuote"
        self.messageStatus = []

class RequestMessageInformation:
    def __init__(self):
        self.businessPurposeTypeCode = "SubmitGeneralLiabilityQuote"
        self.sequenceNumber = 3456789

class MessageStatus:
    def __init__(self):
        self.statusCode = "Success"

class Period:
    def __init__(self):
        self.endDate = ""
        self.startDate = ""

class Premium:
    def __init__(self):
        self.amount = 0.0
        self.currencyCode = "$"
        self.period = Period()

class Quote:
    def __init__(self):
        self.id = ""
        self.insured = Insured()
        self.location = Location()
        self.premium = Premium()

class Root:
    def __init__(self):
        self.SubmitGeneralLiabilityQuoteRequest = SubmitGeneralLiabilityQuoteRequest()
        self.SubmitGeneralLiabilityQuoteResponse = SubmitGeneralLiabilityQuoteResponse()

class SubmitGeneralLiabilityQuoteRequest:
    def __init__(self):
        self.insured = Insured()
        self.location = Location()
        self.messageInformation = RequestMessageInformation()

class SubmitGeneralLiabilityQuoteResponse:
    def __init__(self):
        self.messageInformation = ResponseMessageInformation()
        self.quote = Quote()
