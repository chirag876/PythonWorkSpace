import openai
YOUR_PROMPT="chirag' with a crime score of 'C' indicating 'Moderate crime rate', an earthquake fault score of 'D' with a description 'More than 5 Miles from Known Earthquake Fault', a fire protection score of 'C' with a description 'Within Municipality & > 3 & <= 5 Drive Miles from Fire Station', a flood score of 'B' indicating 'Low risk of flood damage', a hail score of 'A' indicating 'Very Low' risk, a lightning score of 'B' indicating 'Low' risk, a sinkhole score of 'B' indicating '5 miles from Reported Sinkhole' risk, and a tornado score of 'A' indicating 'Very low' risk. Using this data, I'm interested in understanding any patterns, correlations, or trends between the different risk assessment factors and their associated descriptions."
FINE_TUNED_MODEL="curie:ft-personal-2023-08-17-07-31-30"
completion=openai.Completion.create(
    model=FINE_TUNED_MODEL,
    prompt=YOUR_PROMPT,
    max_tokens=300)
print(completion.choices[0]["text"])