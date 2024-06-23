public class Policy
{
    public string Id { get; set; }
    public string QuoteId { get; set; }
    public string CancellationDate { get; set; }
    public string CancelReasonDescription { get; set; }
    public string ControllingStateOrProvinceCode { get; set; }
    public DateTime EffectiveDate { get; set; }
    public DateTime ExpirationDate { get; set; }
    public string PolicyId { get; set; }
    public string LineOfBusinessCode { get; set; }
    public string Number { get; set; }
    public DateTime OriginalEffectiveDate { get; set; }
    public string ParentEntityId { get; set; }
    public string ParentEntityTypeName { get; set; }
    public string StatusCode { get; set; }
    public string TotalPremium { get; set; }
    public int AgentCode { get; set; }
    public DateTime AccountingDate { get; set; }
    public int ReferalCode { get; set; }
    public string RenewalStatus { get; set; }
    public string TransactionType { get; set; }


    public List<Address> address { get; set; }
    public List<Exposure> exposure { get; set; }


    public List<Insured> insured { get; set; }
    public Producer producer { get; set; }


    public List<Reference> reference { get; set; }
    public Underwriter underwriter { get; set; }
    public Claim claim { get; set; }

    public class Address
    {
        public string City { get; set; }
        public string CountryCode { get; set; }
        public string CountryName { get; set; }
        public string Line1 { get; set; }
        public string Line2 { get; set; }
        public string PostalCode { get; set; }
        public string StateOrProvinceCode { get; set; }
        public string StateOrProvinceName { get; set; }
        public DetailAddress DetailAddress { get; set; }

        public List<Reference> Reference { get; set; }
    }
    public class DetailAddress
    {
        public string PostDirectionCode { get; set; }
        public string PreDirectionCode { get; set; }
        public string StreetName { get; set; }
        public string StreetNumber { get; set; }
        public string StreetTypeCode { get; set; }
        public string UnitNumber { get; set; }
    }
    public class Reference
    {
        public string AppliesTo { get; set; }
        public string Description { get; set; }
        public string Id { get; set; }
        public string Name { get; set; }
    }
    public class Characteristics
    {
        public string id { get; set; }
        public string exposureCharacteristicsid { get; set; }
        public string perilid { get; set; }
        public string indemnityPerItem { get; set; }
        public string indemnityPerEvent { get; set; }
        public string indemnityInAggregate { get; set; }
        public string lumpSumPayment { get; set; }
        public string deductible { get; set; }
    }
    public class Peril
    {
        public string id { get; set; }
        public string exposureid { get; set; }
        public string name { get; set; }
        public string renewalGroup { get; set; }
        public List<Characteristics> characteristics { get; set; }
        public string policyholderid { get; set; }
        public string productid { get; set; }
        public string policyid { get; set; }
        public string createdTimestamp { get; set; }
        public string updatedTimestamp { get; set; }
    }
    public class Exposure
    {
        public string id { get; set; }
        public string lineOfBusiness { get; set; }
       public string  exposureName { get ; set; }
        public DateTime CoverageEndDate { get; set; }
        public DateTime CoverageStartDate { get; set; }

        public List<Peril> perils { get; set; }
    }

    public class Valuation
    {
        public Amount Amount { get; set; }
        public string Description { get; set; }
        public string EffectiveDate { get; set; }
        public string Id { get; set; }
        public string ParentEntityId { get; set; }
        public string ParentEntityTypeName { get; set; }
        public string TypeCode { get; set; }
    }
    public class Amount
    {
        public string AppliesToCode { get; set; }
        public string CurrencyCode { get; set; }
        public string Id { get; set; }
        public string ParentEntityId { get; set; }
        public string ParentEntityTypeName { get; set; }
        public int UnitCount { get; set; }
        public int Value { get; set; }
    }
    public class Insured
    {
        public int InsuredId { get; set; }
        public string ParentEntityId { get; set; }
        public string ParentEntityTypeName { get; set; }
        public string TypeCode { get; set; }
        public string BirthDate { get; set; }
        public string FullName { get; set; }
        public string GivenName { get; set; }
        public string Surname { get; set; }
        public Address Address { get; set; }
        public string CountryCode { get; set; }
    }
    public class Producer
    {
        public string Branch { get; set; }
        public string Id { get; set; }
        public string Number { get; set; }
        public string ParentEntityId { get; set; }
        public string ParentEntityTypeName { get; set; }
        public string FullName { get; set; }
        public string GivenName { get; set; }
        public string Surname { get; set; }
    }
    public class Underwriter
    {
        public string Id { get; set; }
        public string ParentEntityId { get; set; }
        public string ParentEntityTypeName { get; set; }
        public string FullName { get; set; }
        public string GivenName { get; set; }
        public string Surname { get; set; }
    }

    public class Claim
    {
        public int ClaimId { get; set; }
        public int ClaimNo { get; set; }
        public DateTime AccidentDate { get; set; }
        public DateTime ReportedDate { get; set; }
        public string RegisterDate { get; set; }
        public string AccidentZipCode { get; set; }
        public double AccidentLatitude { get; set; }
        public double AccidentLongitude { get; set; }
        public string AccidentMonth { get; set; }
        public int AccidentMonthOrder { get; set; }
        public int ClaimSuffix { get; set; }
        public string TypeOfLoss { get; set; }
        public string Adjuster { get; set; }
        public string AccidentQuarter { get; set; }
        public int AccidentQuarterOrder { get; set; }
        public string Estado { get; set; }
        public string SuffixRegisterDate { get; set; }
        public int IdSuffixStatus { get; set; }
        public string SuffixStatus { get; set; }
        public string FullName { get; set; }
        public string DateOfBirth { get; set; }
        public string LicenseNo { get; set; }
        public string LossDescription { get; set; }
        public string Claimant { get; set; }
        public string ReportedBy { get; set; }
        public string Litigation { get; set; }
        public string AccidentCity { get; set; }
        public string AccidentCountry { get; set; }
        public string DriverState { get; set; }
        public string FirstClaimIndReserveDate { get; set; }
        public string FirstClaimExpReserveDate { get; set; }
        public string FirstClaimReserveDate { get; set; }
        public string FirstSuffixIndReserveDate { get; set; }
        public string FirstSuffixExpReserveDate { get; set; }
        public string FirstSuffixReserveDate { get; set; }
    }


}

