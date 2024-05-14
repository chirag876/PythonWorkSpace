class PolicyAddress:
    def __init__(self):
        self.city = "New York"
        self.countryCode = "US"
        self.countryName = "United States"
        self.line1 = "123 Main Street"
        self.line2 = ""
        self.postalCode = "10001"
        self.stateOrProvinceCode = "NY"
        self.stateOrProvinceName = "New York"
        self.id = "ADDR123"
        self.latitude = 40.7128
        self.line3 = ""
        self.line4 = ""
        self.longitude = -74.006
        self.parentEntityId = "ENTITY456"
        self.parentEntityTypeName = "Business"
        self.regionCode = ""
        self.regionName = "Northeast"
        self.subRegionCode = ""
        self.subRegionName = "Mid-Atlantic"
        self.typeCode = ""
        self.detailAddress = PolicyAddressDetailAddress()
        self.reference = []


class Adjuster:
    def __init__(self):
        self.id = "ADJ456"
        self.parentEntityId = ""
        self.parentEntityTypeName = "Claim"
        self.fullName = "Sarah Johnson"
        self.givenName = "Sarah"
        self.otherGivenName = ""
        self.suffix = ""
        self.surname = "Johnson"
        self.titlePrefix = ""


class Amount:
    def __init__(self):
        self.appliesToCode = "ScheduledItem"
        self.currencyCode = "USD"
        self.id = "VALUATION123"
        self.parentEntityId = "ITEM123"
        self.parentEntityTypeName = "ScheduledItem"
        self.typeCode = "VALUATION"
        self.unitCount = 5
        self.value = 2500


class Claim:
    def __init__(self):
        self.id = ""
        self.parentEntityId = ""
        self.parentEntityTypeName = "GL Policy"
        self.lossDate = "2023-05-10"
        self.reportDate = "2023-05-11"
        self.status = "Open"
        self.description = "Property damage claim"
        self.amount = ""
        self.reserveAmount = 0
        self.adjuster = Adjuster()
        self.reference = []


class Coverage:
    def __init__(self):
        self.cancellationDate = "2022-11-04"
        self.cancellationReasonCode = ""
        self.description = "General Liability"
        self.effectiveDate = "2022-11-04"
        self.expirationDate = "2022-11-04"
        self.id = "COVERAGE123"
        self.inceptionDate = "2022-11-04"
        self.lineOfBusinessCode = "GL"
        self.parentEntityId = ""
        self.parentEntityTypeName = "GL"
        self.planName = "Standard"
        self.premiumBasisCode = ""
        self.productCode = ""
        self.typeCode = ""
        self.deductible = Deductible()
        self.limit = Limit()
        self.reference = []
        self.scheduledItem = []


class Deductible:
    def __init__(self):
        self.amount = 1000
        self.id = "DED123"
        self.parentEntityId = ""
        self.parentEntityTypeName = "GL"
        self.typeCode = "DED"


class PolicyAddressDetailAddress:
    def __init__(self):
        self.postDirectionCode = ""
        self.preDirectionCode = ""
        self.streetName = "Main"
        self.streetNumber = "123"
        self.streetTypeCode = ""
        self.unitNumber = ""


class ResponseInsured:
    def __init__(self):
        self.id = "INSURED123"
        self.parentEntityId = ""
        self.parentEntityTypeName = "GL"
        self.typeCode = "IND"
        self.fullName = ""
        self.givenName = ""
        self.otherGivenName = ""
        self.suffix = ""
        self.surname = ""
        self.titlePrefix = ""
        self.birthDate = "1990-01-01"
        self.roleCode = ""
        self.address = InsuredAddress()


class Limit:
    def __init__(self):
        self.amount = 1000000
        self.id = "LIMIT123"
        self.parentEntityId = "P1122"
        self.parentEntityTypeName = "GL"
        self.typeCode = "LIMIT"


class ResponseMessageInformation:
    def __init__(self):
        self.businessPurposeTypeCode = "ABC123"
        self.effectiveDate = "2022-11-04"
        self.trackingNumber = "TRK123456789"


class MessageStatus:
    def __init__(self):
        self.errorCode = "DataError"
        self.statusCode = "Error"
        self.statusDescription = "Data retrieval error"


class ResponsePolicy:
    def __init__(self):
        self.cancellationDate = ""
        self.cancelReasonDescription = "Cancellation due to non-payment"
        self.controllingStateOrProvinceCode = "NY"
        self.effectiveDate = ""
        self.expirationDate = ""
        self.RenewalDate = ""
        self.id = ""
        self.lineofBusinessCode = "GL"
        self.number = "POLICY987654321"
        self.originalEffectiveDate = "2022-11-04"
        self.parentEntityId = "ENTITY456"
        self.parentEntityTypeName = "Business"
        self.statusCode = "ACTIVE"
        self.renewalPremium = ""
        self.numberOfEmployees = ""
        self.businessIndustry = ""
        self.annualRevenue = ""
        self.paymentMethod = ""
        self.claimsCount = "1"
        self.durationInMonths = ""
        self.totalPremium = ""
        self.renewalStatus = ""
        self.address = []
        self.coverage = Coverage()
        self.insured = []
        self.producer = Producer()
        self.reference = []
        self.underwriter = Underwriter()


class PolicyHolder:
    def __init__(self):
        self.CustomerID = ""
        self.CustomerName = ""


class Producer:
    def __init__(self):
        self.branch = "ABC"
        self.id = "PROD789"
        self.number = "P12345"
        self.parentEntityId = ""
        self.parentEntityTypeName = "GL"
        self.fullName = "John Smith"
        self.givenName = "John"
        self.otherGivenName = ""
        self.suffix = ""
        self.surname = "Smith"
        self.titlePrefix = ""


class Quote:
    def __init__(self):
        self.id = ""


class Reference:
    def __init__(self):
        self.appliesTo = ""
        self.description = ""
        self.id = ""
        self.name = ""


class RetrievePolicyRequest:
    def __init__(self):
        self.messageInformation = RequestMessageInformation()
        self.policy = RequestPolicy()
        self.insured = RequestInsured()


class RetrievePolicyResponse:
    def __init__(self):
        self.messageInformation = ResponseMessageInformation()
        self.Quote = Quote()
        self.policyHolder = PolicyHolder()
        self.policy = ResponsePolicy()
        self.claim = Claim()


class Root:
    def __init__(self):
        self.RetrievePolicyRequest = RetrievePolicyRequest()
        self.RetrievePolicyResponse = RetrievePolicyResponse()


class ScheduledItem:
    def __init__(self):
        self.categoryCode = ""
        self.description = "Computers and peripherals"
        self.effectiveDate = "2022-11-04"
        self.expirationDate = "2022-11-04"
        self.id = "ITEM123"
        self.parentEntityId = "COVERAGE123"
        self.parentEntityTypeName = "Coverage"
        self.purchasedDate = "2022-11-04"
        self.limit = Limit()
        self.valuation = []


class Underwriter:
    def __init__(self):
        self.id = "UW123"
        self.parentEntityId = ""
        self.parentEntityTypeName = "GL"
        self.fullName = "Emily Johnson"
        self.givenName = "Emily"
        self.otherGivenName = ""
        self.suffix = ""
        self.surname = "Johnson"
        self.titlePrefix = ""


class Valuation:
    def __init__(self):
        self.amount = Amount()
        self.description = "Computers"
        self.effectiveDate = "2022-11-04"
        self.id = "VALUATION456"
        self.parentEntityId = "ITEM123"
        self.parentEntityTypeName = "ScheduledItem"
        self.typeCode = "VALUATION"


class RequestPolicy:
    def __init__(self):
        self.cancellationDate = ""
        self.cancelReasonDescription = "Cancellation due to non-payment"
        self.controllingStateOrProvinceCode = "NY"
        self.effectiveDate = ""
        self.expirationDate = ""
        self.id = ""
        self.lineofBusinessCode = "GL"
        self.number = "POLICY987654321"
        self.originalEffectiveDate = "2022-11-04"
        self.parentEntityId = "ENTITY456"
        self.parentEntityTypeName = "Business"
        self.statusCode = "ACTIVE"


class InsuredAddress:
    def __init__(self):
        self.city = "New York"
        self.countryCode = "US"
        self.countryName = "United States"
        self.line1 = "456 Elm Street"
        self.line2 = ""
        self.postalCode = "10002"
        self.stateOrProvinceCode = "NY"
        self.stateOrProvinceName = "New York"
        self.id = "ADDR456"
        self.latitude = 40.7128
        self.line3 = ""
        self.line4 = ""
        self.longitude = -74.006
        self.parentEntityId = "INSURED123"
        self.parentEntity = ""
        self.typeName = "Address"
        self.regionCode = ""
        self.regionName = ""
        self.subRegionCode = ""
        self.subRegionName = ""
        self.typeCode = "HOME"
        self.detailAddress = InsuredAddressDetailAddress()
        self.reference = []


class InsuredAddressDetailAddress:
    def __init__(self):
        self.postDirectionCode = " "
        self.preDirectionCode = " "
        self.streetName = "Elm"
        self.streetNumber = "456"
        self.streetTypeCode = "ST"
        self.unitNumber = " "


class RequestMessageInformation:
    def __init__(self):
        self.businessPurposeTypeCode = "ABC123"
        self.effectiveDate = "2022-11-04"
        self.trackingNumber = "TRK123456789"


class RequestInsured:
    def __init__(self):
        self.id = "INSURED123"
        self.parentEntityId = ""
        self.parentEntityTypeName = "GL"
        self.typeCode = "IND"
        self.fullName = ""
        self.givenName = ""
        self.otherGivenName = ""
        self.suffix = ""
        self.surname = ""
        self.titlePrefix = ""
