#%%
import json
# %%
from ibm_watson import NaturalLanguageUnderstandingV1
# %%
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# %%
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions
# %%
authenticator = IAMAuthenticator('EDekQ4Vgjmyqz69cbxb4cu30FVIGOVSLcaAEIAxGj0ub')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)
# %%
natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/02f03160-9fb7-4388-b3d1-06dbb5686e7a')
# %%
response = natural_language_understanding.analyze(
    url='https://es.wikipedia.org/wiki/Miguel_Grau',
    features=Features(categories=CategoriesOptions(limit=3))).get_result()
# %%
print(json.dumps(response, indent=2))
# %%
