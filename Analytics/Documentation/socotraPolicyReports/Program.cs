using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Net.Http;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;
using static Policy;

namespace APICallToCSV
{
    class Program
    {
        static async Task Main(string[] args)
        {
            string authenticateUrl = "https://api.sandbox.socotra.com/account/authenticate";
            string apiUrl = "https://api.sandbox.socotra.com/report/allPoliciesPreview";

            HttpClient client = new HttpClient();

            // Authenticate and get authorization token
            var authPayload = new
            {
                hostName = "ravendra_socotra-configeditor.co.sandbox.socotra.com",
                username = "alice.lee",
                password = "socotra"
            };

            // Serialize authentication payload to JSON
            string jsonAuthPayload = JsonConvert.SerializeObject(authPayload);

            // Make the POST request for authentication
            HttpResponseMessage authResponse = await client.PostAsync(authenticateUrl, new StringContent(jsonAuthPayload, Encoding.UTF8, "application/json"));

            if (authResponse.IsSuccessStatusCode)
            {
                // Read authentication response content
                string authResponseContent = await authResponse.Content.ReadAsStringAsync();

                // Parse JSON response to get authorization token
                JObject authJsonResponse = JObject.Parse(authResponseContent);
                string authorizationToken = authJsonResponse["authorizationToken"].ToString();

                // Set the payload
                var payload = new
                {
                    reportStartTimestamp = "1672560000000",
                    reportEndTimestamp = "1698217200000",
                    productNames = new[] { "Personal Auto", "Workers Compensation" },
                    policyFields = new[]
                    {
                    "channel",
                     "multiple_drivers",
                     "drivers",
                     "10_year_felony_conviction",
                     "insurance_fraud_conviction",
                     "atfault_claims_past_5_years",
                     "run_third_party_reports",
                     "uw_company",
                     "year_business_started",
                     "affinity_group",
                     "governing_class_code",
                     "experience_mod",
                     "business_type",
                     "fein",
                     "sic_code",
                     "sic_description",
                     "naics_code",
                     "naics_description",
                     "note",
                     "named_insureds",
                     "owners_officers",
                     "parties_involved",
                     "prior_coverages",
                     "prior_losses",
                     "email",
                     "street",
                     "city",
                     "state",
                     "postal_code",
                     "q_work_above_15",
                     "q_work_over_water",
                     "q_subcontractors_used",
                     "q_percent_subcontracted",
                     "q_work_without_cert_ins",
                     "q_employees_oos",
                     "q_prior_cov_declined",
                     "q_other_business",
                     "q_own_lease_watercraft_aircraft",
                     "q_workers_from_peo_or_3rd_party",
                     "q_written_safety_program",
                     "q_health_plans_provided",
                     "renewal_direction",
                     "scheduled_credits_premises",
                     "scheduled_credits_class_peculiarities",
                     "scheduled_credits_medical_facilities",
                     "scheduled_credits_safety_devices",
                     "scheduled_credits_employees_training",
                     "scheduled_credits_mgmt_coop_w_carrier",
                     "scheduled_credits_mgmt_safety_org"
                    },
                    exposureFields = new[]
                    {
                     "vehicle_type",
                     "body_style",
                     "motorcycle_cc",
                     "vin",
                     "year",
                     "make",
                     "model",
                     "vehicle_value",
                     "unrepaired_damage",
                     "ownership_indicator",
                     "vehicle_plated_state",
                     "license_plate",
                     "annual_miles",
                     "primary_vehicle_use",
                     "travel_radius",
                     "travel_radius_farm",
                     "distance_to_work_school",
                     "experience_mod",
                     "street",
                     "city",
                     "_description",
                     "postal_code"
                    },
                    perilFields = new string[] {
                     "name",
                     "street",
                     "city",
                     "state",
                     "postal_code",
                     "description",
                     "governing_law",
                     "class_code",
                     "wages",
                     "basis",
                     "_description",
                     "class_description",
                     "estimated_wages",
                     "number_employees",
                     "if_any_basis"
                    }
                };

                // Serialize payload to JSON
                string jsonPayload = JsonConvert.SerializeObject(payload);

                // Add authorization token to the request headers
                client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", authorizationToken);

                // Make the POST request to allPoliciesPreview API
                HttpResponseMessage response = await client.PostAsync(apiUrl, new StringContent(jsonPayload, Encoding.UTF8, "application/json"));

                if (response.IsSuccessStatusCode)
                {
                    string responseContent = await response.Content.ReadAsStringAsync();

                    // Deserialize the JSON response
                    JObject jsonResponse = JObject.Parse(responseContent);
                    List<List<string>> rows = jsonResponse["previewRows"].ToObject<List<List<string>>>();

                    // Extracting headers from the response content
                    List<string> headers = jsonResponse["headers"].ToObject<List<string>>();

                    // Creating a StringBuilder to build CSV content
                    StringBuilder csvContent = new StringBuilder();

                    // Adding headers to the CSV content
                    csvContent.AppendLine(string.Join(",", headers));

                    // Adding rows to the CSV content
                    foreach (var row in rows)
                    {
                        csvContent.AppendLine(string.Join(",", row));
                    }

                    // Writing the CSV content to a file
                    string filePath = "output1222.csv"; // Replace with your desired file path
                    File.WriteAllText(filePath, csvContent.ToString());

                    Console.WriteLine("CSV file created successfully!");


                    List<Policy> policies = new List<Policy>();

                    foreach (List<string> row in rows)
                    {
                        string policyId = row[1];

                        // Check if the policy with the same ID already exists
                        Policy existingPolicy = policies.FirstOrDefault(p => p.PolicyId == policyId);

                        if (existingPolicy != null)
                        {
                            // Update the existing policy's exposure
                            var exposurePolicy = new Exposure
                            {
                                id = row[3],
                                lineOfBusiness = row[0],
                                exposureName = row[4],
                            };

                            var exposurePeril = new Peril
                            {
                                id = row[5],
                                name = row[6],
                            };

                            var perilCharacteristics = new Characteristics
                            {
                                indemnityPerItem = row[9],
                            };

                            exposurePeril.characteristics = new List<Characteristics> { perilCharacteristics };
                            exposurePolicy.perils = new List<Peril> { exposurePeril };
                            existingPolicy.exposure.Add(exposurePolicy);
                        }
                        else
                        {
                            // Create a new policy
                            Policy policy = new Policy
                            {
                                //LineOfBusinessCode = row[0],
                                PolicyId = policyId,
                                EffectiveDate = ConvertStringToDate(row[7]),
                                TotalPremium = row[8]
                            };

                            var exposurePolicy = new Exposure
                            {
                                id = row[3],
                                lineOfBusiness = row[0],
                                exposureName = row[4],
                                CoverageStartDate = ConvertStringToDate(row[14]),
                                CoverageEndDate = ConvertStringToDate(row[15]),
                            };

                            var exposurePeril = new Peril
                            {
                                id = row[5],
                                name = row[6],
                            };

                            var perilCharacteristics = new Characteristics
                            {
                                indemnityPerItem = row[9],
                                indemnityPerEvent = row[10],
                                indemnityInAggregate = row[11],
                                lumpSumPayment = row[12],
                                deductible = row[13],

                            };

                            exposurePeril.characteristics = new List<Characteristics> { perilCharacteristics };
                            exposurePolicy.perils = new List<Peril> { exposurePeril };
                            policy.exposure = new List<Exposure> { exposurePolicy };

                            policies.Add(policy);
                        }
                    }

                    string policiesJson = JsonConvert.SerializeObject(policies);

                    Console.WriteLine(policiesJson);
                }
                else
                {
                    Console.WriteLine("Failed to get response from API.");
                    // Handle the failure case accordingly
                }
            }
            else
            {
                Console.WriteLine("Failed to authenticate.");
            }
        }
        public static DateTime ConvertStringToDate(string date)
        {
            // Parse the string to DateTime
            if (DateTime.TryParseExact(date, "yyyyMMdd", CultureInfo.InvariantCulture, DateTimeStyles.None, out DateTime parsedDate))
            {
                // Successfully parsed the date string
                return parsedDate;
            }
            else
            {
                throw new Exception("datetime not convert");
            }
        }
    }
}
